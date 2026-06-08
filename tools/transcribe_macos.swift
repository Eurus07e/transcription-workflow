import AVFoundation
import Foundation
import Speech

struct Segment: Codable {
    let start: Double
    let duration: Double
    let text: String
}

struct Transcript: Codable {
    let file: String
    let locale: String
    let text: String
    let segments: [Segment]
}

func fail(_ message: String) -> Never {
    FileHandle.standardError.write((message + "\n").data(using: .utf8)!)
    exit(1)
}

let args = Array(CommandLine.arguments.dropFirst())
guard args.count >= 2 else {
    fail("Usage: transcribe_macos <audio-file> <output-json> [locale]")
}

let audioPath = args[0]
let outputPath = args[1]
let localeID = args.count >= 3 ? args[2] : "en-US"

let authSemaphore = DispatchSemaphore(value: 0)
var authStatus: SFSpeechRecognizerAuthorizationStatus = .notDetermined
SFSpeechRecognizer.requestAuthorization { status in
    authStatus = status
    authSemaphore.signal()
}
authSemaphore.wait()

guard authStatus == .authorized else {
    fail("Speech recognition permission not authorized: \(authStatus.rawValue)")
}

guard let recognizer = SFSpeechRecognizer(locale: Locale(identifier: localeID)) else {
    fail("Cannot create recognizer for locale \(localeID)")
}

guard recognizer.isAvailable else {
    fail("Speech recognizer is not available for locale \(localeID)")
}

let audioURL = URL(fileURLWithPath: audioPath)
let request = SFSpeechURLRecognitionRequest(url: audioURL)
request.shouldReportPartialResults = false

let resultSemaphore = DispatchSemaphore(value: 0)
var finalResult: SFSpeechRecognitionResult?
var finalError: Error?

let task = recognizer.recognitionTask(with: request) { result, error in
    if let result {
        finalResult = result
        if result.isFinal {
            resultSemaphore.signal()
        }
    }
    if let error {
        finalError = error
        resultSemaphore.signal()
    }
}

let waitResult = resultSemaphore.wait(timeout: .now() + 600)
if waitResult == .timedOut {
    task.cancel()
    fail("Timed out while recognizing \(audioPath)")
}

if let finalError, finalResult == nil {
    fail("Recognition failed for \(audioPath): \(finalError.localizedDescription)")
}

guard let best = finalResult?.bestTranscription else {
    fail("No transcription result for \(audioPath)")
}

let segments = best.segments.map {
    Segment(
        start: $0.timestamp,
        duration: $0.duration,
        text: $0.substring
    )
}

let transcript = Transcript(
    file: audioPath,
    locale: localeID,
    text: best.formattedString,
    segments: segments
)

let encoder = JSONEncoder()
encoder.outputFormatting = [.prettyPrinted, .sortedKeys]
let data = try encoder.encode(transcript)
try data.write(to: URL(fileURLWithPath: outputPath), options: .atomic)
