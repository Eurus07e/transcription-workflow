from pathlib import Path
import textwrap
import re
import importlib.util


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "transcripts" / "raw"
OUT = ROOT / "transcripts" / "welearn_theme2_bilingual_reviewed.tex"
REVISED_TRANSLATIONS_PATH = Path(__file__).resolve().parent / "revised_translations.py"

if REVISED_TRANSLATIONS_PATH.exists():
    spec = importlib.util.spec_from_file_location("revised_translations", REVISED_TRANSLATIONS_PATH)
    revised_translations = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(revised_translations)
else:
    revised_translations = None


ITEMS = [
    ("S2.1-ac4&5", "Session 2.1 Activity 4 & 5", "AGI, the Top One Emerging Technology that Are Changing Our World"),
    ("S2.1-ac7", "Session 2.1 Activity 7", "How Blockchain Works (Part 1)"),
    ("S2.1-ac8", "Session 2.1 Activity 8", "How Blockchain Works (Part 2)"),
    ("S2.2-ac4", "Session 2.2 Activity 4", "Automation in Workplaces and Its Implication (Part 1)"),
    ("S2.2-ac5", "Session 2.2 Activity 5", "Automation in Workplaces and Its Implication (Part 2)"),
    ("s2.2-ac7", "Session 2.2 Activity 7", "The Digital Divide (Part 1)"),
    ("s2.2-ac8", "Session 2.2 Activity 8", "The Digital Divide (Part 2)"),
    ("s2.3-ac7&8", "Session 2.3 Activity 7 & 8", "How to Keep Human Bias Out of AI"),
    ("s2.3-ac14", "Session 2.3 Activity 14", "Ethics of AI: Challenges and Governance"),
    ("s2.4-ac4", "Session 2.4 Activity 4", "How I'm Fighting Bias in Algorithms (Part 1)"),
    ("s2.4-ac5", "Session 2.4 Activity 5", "How I'm Fighting Bias in Algorithms (Part 2)"),
    ("S2.4-ac7", "Session 2.4 Activity 7", "The Ethical Dilemma of Self-Driving Cars (Part 1)"),
    ("s2.4-ac8", "Session 2.4 Activity 8", "The Ethical Dilemma of Self-Driving Cars (Part 2)"),
    ("s2.4-ac14", "Session 2.4 Activity 14", "Let's Not Use Mars as a Backup Planet"),
    ("s2.5-ac4", "Session 2.5 Activity 4", "The Art of Debate (Part 1)"),
    ("s2.5-ac5", "Session 2.5 Activity 5", "The Art of Debate (Part 2)"),
    ("s2.6-ac7&8", "Session 2.6 Activity 7 & 8", "How Our Food Choices Affect Climate Change"),
]


TRANSLATIONS = {
    "S2.1-ac4&5": """
技术正在永久改变我们的世界，但方式未必如人们想象。以人工通用智能为例。人工通用智能通常被称为 AGI，指的是一种机器能够像人类一样理解、学习并运用智能来解决任何问题。与只为特定任务而设计的窄域人工智能不同，AGI 将具备处理广泛认知任务的能力，并能自主适应新的情境。

OpenAI、Google DeepMind 等领先机构正在 AGI 研究方面取得重要进展。其中一种路径是深度学习和神经网络，它们试图模仿人脑的结构和功能。研究人员正在扩展这些模型，使其能够处理更复杂、更抽象的任务，而不只是模式识别和数据处理。另一个有趣的发展方向是强化学习，即 AI 系统通过试错来学习决策，并在成功结果后获得奖励。人们认为，这可能是通向更通用的问题解决能力的一条道路。

展望未来，AGI 的演进可能带来深远影响。一旦实现，AGI 可以执行从复杂科学研究、医学诊断到艺术创作和决策制定等大量任务。我们或许会进入一个阶段：AGI 能处理任何与计算机相关的工作，并可能在某些领域超过人类智能，从而推动多个领域取得突破。

AGI 还可能催生更直观、更灵活的个人助手，能够理解并回应人类多样化的需求和偏好。在工业领域，AGI 可以自动化复杂任务，显著提升效率。随着时间推移，人工通用智能甚至可能具备改进自身算法和架构的能力，从而产生超级智能 AI。这些超级智能的能力可能超过人类数千倍甚至数百万倍，并有潜力创造突破性技术，以当下难以完全理解的方式改变社会。
""",
    "S2.1-ac7": """
它被称为区块链。这个词听起来并不优美，但演讲者认为，它正在成为下一代互联网，并且对每一个企业、每一个社会以及每一个个体都蕴含巨大潜力。

过去几十年，我们拥有的是“信息互联网”。当我给你发邮件、PPT 或其他文件时，我实际上并不是把原件发给你，而是发给你一份副本。这很好，因为它让信息更加民主化。但是，当对象变成资产时，复制就会成为严重问题。钱、股票、债券、积分、知识产权、音乐、艺术品、投票权、碳信用等资产都不能被随意复制。如果我给你 100 美元，关键在于我不能同时还拥有这 100 美元，也不能再把同一笔钱发给别人。

密码学家长期以来把这称为“双重支付问题”。如今，我们几乎完全依赖银行、政府、大型社交媒体公司、信用卡公司等大型中介来建立经济中的信任。这些中介承担着各种商业和交易逻辑：认证、身份识别、清算、结算和记账。总体上它们做得不错，但问题正在增长。

首先，中介是中心化的，因此可能被黑客攻击，而且这种情况越来越多。摩根大通、美国联邦政府、LinkedIn、Home Depot 等都曾付出代价。其次，它们把数十亿人排除在全球经济之外，例如没有足够资金开银行账户的人。第三，它们拖慢了交易速度。电子邮件一秒钟就能传遍全球，而钱通过银行系统跨城转移却可能需要几天甚至几周。第四，它们抽取高额费用，跨国汇款往往要拿走 10% 到 20%。第五，它们掌握我们的数据，使我们无法从中获益，也难以用数据更好地管理生活，同时隐私不断被侵蚀。最大的问题是，数字时代创造的财富被这些中介以不对称方式占有，财富在增长，社会不平等也在加剧。
""",
    "S2.1-ac8": """
如果不仅有“信息互联网”，还存在一个“价值互联网”呢？想象一个庞大、全球化、分布式的账本，运行在数以百万计的计算机上，对所有人开放。各种资产，从金钱到音乐，都可以在其中被存储、转移、交易、交换和管理，而不需要强大的中介机构。换句话说，价值本身也可以拥有一种原生媒介。

2008 年金融业崩溃后，一个名为中本聪的匿名个人或群体发表了一篇论文，提出了一种数字现金协议，其底层加密货币就是比特币。这种加密货币使人们能够在没有第三方的情况下建立信任并完成交易。看似简单的行为点燃了一场全球性的火花，引发了人们的兴奋、恐惧和广泛关注。

不要把比特币本身与真正关键的东西混为一谈。比特币是一种资产，价格会上下波动，投机者会关注它。更广泛地说，它是一种加密货币，而不是由民族国家控制的法定货币。但真正重要的是它背后的底层技术：区块链。

在人类历史上，人们第一次可以在全球范围内点对点地相互信任并交易。信任不再依赖大型机构，而是通过协作、密码学和巧妙的代码来建立。因为信任已经成为技术本身的一部分，演讲者称它为“信任协议”。

区块链的工作方式可以这样理解：数字资产并不存放在某个中心位置，而是通过最高级别的密码学分布在全球账本中。当一笔交易发生时，它会被发布到全球数以百万计的计算机上。世界各地有一群被称为“矿工”的人，他们拥有巨大的算力，甚至远超 Google 在全球的算力规模。每隔十分钟，网络像心跳一样生成一个区块，包含过去十分钟的所有交易。矿工们竞争解决难题，第一个验证区块真实性的人会获得数字货币奖励，在比特币区块链上就是比特币。

关键在于，新区块会连接到前一个区块，前一个区块又连接到更早的区块，形成一条区块链。每个区块都有时间戳，就像数字火漆印章。如果有人想篡改一个区块，比如用同一笔钱同时支付给两个人，他就必须同时篡改该区块以及之前所有区块，也就是整条区块链上的商业历史；而且不是在一台计算机上篡改，而是要在数百万台计算机上同时完成，还要面对世界上最强大的计算资源和最高级别的加密保护。这几乎难以做到。因此，区块链比今天许多计算机系统更安全。
""",
    "S2.2-ac4": """
未来的配送正在到来。小型机器人即将在伦敦格林尼治开始把包裹和食品送到家门口。过去，由于现实世界具有不可预测的复杂性，最后一公里配送中存在无穷无尽的危险和障碍，因此需要人类参与。但现在情况似乎正在改变。

人们常常为了等待一个五小时的配送窗口而不得不待在家里，甚至请一天假，这既耗时又浪费。机器人和当今的技术已经可以解决这些问题，而这正是相关公司正在做的事情。

毫无疑问，自动化、人工智能和这类机器人即将带来一波浪潮，为社会创造巨大优势。它们会改变我们的生活，使生活更加便利。但问题在于，它们是否也会带来社会难以应对的新问题，尤其是更严重的不平等。

可能出现的情形是：配送机器人、无人驾驶货车、仓库机器人和在线零售结合起来，使极少数人能够控制一个过去曾雇用几十万甚至数百万人的市场。少数人可能因此变得极其富有，而其他人则被排除在外。

在以往的技术变革中，机械化把农民赶离土地，但也在城镇中创造了新的、薪水更高的工作。当体力劳动减少时，人类转向脑力劳动。但很快，机器不仅会比我们更强壮，也会比我们更聪明。确实会产生一些新工作，例如机器人操控员可以在配送机器人遇到麻烦时接管控制。真正令人担心的是，这类新岗位究竟会有多少。

一项研究估计，未来 10 到 20 年内，英国 35% 的工作可能被自动化取代，年薪低于 3 万英镑的岗位受到自动化冲击的风险，是年薪高于 10 万英镑岗位的五倍。麦肯锡的研究警告说，这场转型发生的速度是工业革命的 10 倍，规模是工业革命的 300 倍。换言之，它的影响可能是改变维多利亚时代世界那场变革的 3000 倍。面对这种挑战，大多数政治人物至今的反应就像雕塑一样迟缓而僵硬。
""",
    "S2.2-ac5": """
欧洲议会即将讨论的一个想法是：如果摧毁就业岗位的机器人正在取代纳税的人类，那么也许我们需要向机器人征税。提议者认为，应当精确监测劳动力市场和就业部门正在发生的变化。如果机器人接管的岗位多于新创造的岗位，那么成员国和治理机构将很难筹集足够资金来支付社会所需的各种服务。因此，如果情况确实如此，就应该考虑向机器人征税，因为总有人必须为正常生活、基础设施以及政府应向人民提供的服务买单。

但这件事会有多简单呢？有些机器人容易识别，例如公司用 Baxter 这样的机器人替代工人，对其征税相对直接。然而，这一波创新并不完全发生在实体世界。革命的很大一部分其实发生在视线之外，发生在外观熟悉的电脑机箱和服务器机架内部。这些新机器正在学习和思考，而学习和思考正是许多人谋生的方式。

柏林初创公司 SMAC 代表“智能会计”。它利用人工智能，试图改变传统而枯燥的会计行业。过程看起来很熟悉：客户把发票和收据扫描进电脑。但在系统内部，软件正在完成非凡的工作。不是由人类会计查看文件，而是由计算机识别数字，并把它们添加到正确的账户中。

纸面文字本身相对容易处理，难点在于解释文字：系统必须知道哪个数字是什么，收据上的文字信息在哪里，以及这些信息意味着什么。这种“解释信息”的能力正在许多领域带来革命。例如自动驾驶汽车必须判断街上出现的是一个行人，还是路面积水反射出的影像；必须决定可以继续行驶还是必须停车。这就是理解和解释的工作，会计系统也需要完成同样的解释任务。

SMAC 表示，这将使人类会计摆脱枯燥工作，转向更有趣的任务。但问题依旧是：究竟还有多少人类岗位能够保留下来？技术创新正在非常迅速地推进，但我们并不知道自己要去哪里、想抵达哪里。现在，政府和私营部门似乎都乐于依靠新自由主义和市场力量，让市场决定创新方向，而这非常危险。

这种危险有多大？看看马匹的命运就能理解。仅仅一个世纪前，英国有数百万匹马可以在农业、矿山、工业和运输中谋生。如今，马曾经垄断的几乎所有工作都不再需要它们，它们连饲料和马厩的成本都不值，甚至免费提供劳动力也无人需要。我们只能希望，机器人对人类能比人类当年对马更有同情心。
""",
    "s2.2-ac7": """
想象一下：你坐在舒适的咖啡馆里，一边喝咖啡，一边刷手机观看这个视频。你拥有高速互联网、无限的信息来源，也能与世界各地的人联系。现在，再想象世界另一端，或者也许只是隔壁城镇中的某个人，没有这样的便利。他们没有稳定的网络，没有可用的设备，甚至缺乏在当今技术驱动世界中行动所需的数字素养。

问题是：在教育、工作、医疗乃至政府服务都转移到线上的时代，那些被落下的人会怎么样？数字鸿沟并不只是有没有互联网的问题，它关乎机会、权力，以及技术如何悄悄塑造一种新的不平等。

技术原本被认为是伟大的平衡器。互联网承诺创造一个知识免费、机会无限、任何人都能不受背景限制而建设更好未来的世界。但现实是，世界越互联，拥有接入条件的人和没有接入条件的人之间的差距反而越深。数字鸿沟不只是拥有智能手机或电脑的问题，而是谁能够参与数字经济，谁会被排除在外的问题。

数字鸿沟主要有三个层面。第一是接入：谁拥有互联网和设备，谁没有。第二是可用性：谁懂得有效使用技术，谁在数字素养方面遇到困难。第三是赋权：谁真正从技术中受益，谁即使有了接入条件仍处于劣势。

先看接入。全球超过 26 亿人无法上网，接近全球人口的三分之一被隔绝在现代世界之外。即使在已经联网的人群中，接入质量也差异巨大。有些人享受高速光纤网络，另一些人只能使用缓慢且不稳定的连接，连最基本的在线任务都令人沮丧。

教育就是一个例子。新冠疫情期间，数百万学生转向线上学习。但农村地区或低收入家庭中没有笔记本电脑、没有稳定网络的孩子怎么办？他们落后了，并不是因为缺乏智力或动力，而是因为缺乏接入条件。失去一年的教育可能意味着更少的机会、更低的收入潜力，以及被限制定义的未来。

第二层是可用性。即便人们拥有网络，也不是每个人都知道如何有效利用它。想象一个发展中国家的农民，虽然有智能手机，却不知道如何进入线上市场，以公平价格出售农作物。或者一位老年人不会使用网上银行，因为不了解数字安全而被骗。问题不只是拥有设备，而是拥有用设备改善生活的技能。

第三层，也许是最危险的一层，是赋权。即使人们拥有接入和技能，真正的问题仍然是：谁从技术中获益？大型企业、政府和科技精英正在利用数字进步扩张权力，而边缘化群体往往处于劣势。就业市场正在向自动化和数字技能转移，能够适应的人会繁荣，不能适应的人则被挤出劳动力市场。
""",
    "s2.2-ac8": """
再想想：技术岗位、自由职业和远程工作机会正在快速增长。但如果你没有笔记本电脑或稳定网络怎么办？如果你从未学过编程，也不会使用数字平台怎么办？如今的鸿沟不再只是“谁拥有技术”，而是谁能够利用技术创造更好生活。

数字鸿沟并不只是发展中国家的问题。即使在富裕国家，差距也在扩大。在美国，数百万农村社区缺乏可靠宽带。在大城市，低收入社区通常公共 Wi-Fi 更少，电脑实验室设备陈旧，数字素养培训也有限。

更严重的是，数字鸿沟不只是便利性问题，而是生存问题。疫情期间，拥有互联网的人可以远程工作；没有互联网的人中，许多人失去了工作。医疗服务也在转向线上。远程医疗、在线健康门户和电子处方正在成为常态。但那些负担不起网络费用，或不知道如何使用数字医疗服务的人怎么办？他们只是因为无法接触到屏幕，就得到更差的医疗照护。

民主也同样受到影响。政治辩论、新闻更新，甚至投票都越来越数字化。当人们缺乏数字接入时，他们失去的不只是技术连接，也是在决策过程中的参与权。
""",
    "s2.3-ac7&8": """
人工智能正在被用来帮助决定你能否获得工作面试、你要为车险支付多少钱、你的信用评分有多好，甚至你在年度绩效评估中得到什么评价。但这些决定都经过了 AI 对我们身份、种族、性别和年龄的假设过滤。这是如何发生的？

想象一套 AI 系统正在帮助招聘经理寻找公司下一位技术负责人。如果过去经理主要雇用了男性，那么 AI 会学到：男性比女性更可能成为程序员。很快，这就会滑向“男性比女性更适合当程序员”的结论。我们把自己的偏见强化进 AI 之中，于是 AI 开始筛掉女性候选人。

如果人类招聘经理这样做，我们会愤怒，也不会允许这种性别歧视。但奇怪的是，当机器做出决定时，AI 似乎就被置于法律之上。问题还不止于此，我们也通过与 AI 互动的方式强化偏见。常见的语音助手，如 Siri、Alexa、Cortana，有两个共同点：一是它们经常读不准演讲者的名字；二是它们几乎都是女性化的。它们被设计成顺从的仆人，为你开灯关灯、帮你购物。男性化的 AI 也存在，但通常更强势、更高权力，例如 IBM Watson 做商业决策，Salesforce Einstein 或机器人律师 Ross。

这些设计会影响在 AI 环境中长大的孩子。孩子做学校项目时搜索“CEO”的图片，算法大多展示男性；搜索“私人助理”时，结果大多是女性。随后他们播放音乐、点餐时，又对一个顺从的女性语音助手发号施令。今天最聪明的一批人正在创造这些技术，他们本可以用任何方式设计它们，却选择了类似 20 世纪 50 年代电视剧里秘书的风格。

不过，演讲并不是要告诉我们世界会被充满性别主义和种族主义的机器统治。关于 AI 的好消息是，它完全在我们的控制之内。我们可以教给 AI 正确的价值观和伦理。我们可以做三件事：第一，意识到我们自身的偏见以及周围机器中的偏见；第二，确保由多元化团队来建设这些技术；第三，让 AI 从多样化的经验中学习。

演讲者用亲身经历说明前两点。在科技行业，如果你看起来不像 Mark Zuckerberg 或 Elon Musk，你的生活会更困难，你的能力会受到质疑。她在网上技术论坛以自己的照片和名字登录时，经常收到诸如“你凭什么谈 AI”“你凭什么懂机器学习”这样的质疑。于是她创建了一个新账号，用一只背着喷气背包的猫作为头像，并选择了不暴露性别的名字。这一次，她没有再收到那些居高临下的评论，也终于能真正完成工作。

这令人沮丧。她 15 岁起就开始做机器人，拥有计算机科学方面的学位，却仍然不得不隐藏性别，才能让自己的工作被认真对待。这说明问题并不是男性天生比女性更擅长技术。另一项研究发现，在一个平台上，当女性程序员隐藏性别时，她们的代码被接受的比例比男性高 4%。所以问题不在能力，而在 AI 领域的一种精英主义偏见：它默认程序员应该长成某种特定样子。
""",
    "s2.3-ac14": """
你是否会使用导航应用躲避交通拥堵？当你向下滑动社交媒体信息流时，发生了什么？你会听从流媒体平台给你的推荐吗？到一天结束时，我们知道 AI 就在那里，但我们真的理解背后发生了什么吗？我们能信任这些应用的输出吗？

到目前为止，我们对这些技术的处理方式往往是：消费者可以自己弄明白。他们可以阅读网站上的条款和条件，也可以选择不参与某些数字环境。但是，这些产品和平台越来越成为我们生活的一部分。它们是我们提供教育的方式，是我们寻找工作的方式。仅仅给消费者更多信息，或者赋予他们个人投诉权，并不能解决这种权力不平衡。

如果我们想改变这些技术在结构层面的设计方式，最终必须把责任推回到设计者身上，推回到依赖技术的组织身上，要求它们改变实践。人工智能等技术有潜力赋能人们、拓宽人们的视野；也可能扩大不平等，无法帮助我们解决社会挑战。但我们不能把责任归咎于技术本身。问题不在技术，而在我们是否建立了框架、塑造了规则，使这些技术能够实现我们希望它们达成的目标。

我们必须确保把重要的伦理原则嵌入其中，包括保护和促进人权与人的尊严。最终，决定结果的是这些原则。没有大型科技公司和其他企业的参与，负责任的 AI 治理是不可能的。我们需要找到方法向它们说明：伦理并不是抽象原则。伦理应当自下而上，是一个动态系统；它应当促进创新，并最终带来对公司产品的信任，而这种信任会帮助企业实现其商业目标。

过去五年中，伦理讨论在塑造 AI 监管话语方面发挥了重要作用。我们看到大量宪章和 AI 伦理原则宣言出现，也看到这些原则正在被非常实际地应用。拉丁美洲许多国家已经提出了自己的人工智能国家战略，其中一些国家更进一步，开始通过硬法来规范人工智能原则。欧盟正在讨论 AI 法案草案，美国国会也开始详细讨论科技公司的垄断权力。全球各地都可以看到车轮正在转动：各国正在从提高意识，走向制定战略，再走向实施和监管尝试。
""",
    "s2.4-ac4": """
事情是怎么发生的？为什么我会戴着白色面具坐在电脑前，试图让一个廉价摄像头检测到我？当我不以“代码诗人”的身份对抗“编码凝视”时，我是 MIT 媒体实验室的研究生。在那里，我有机会参与各种充满想象力的项目，包括 Aspire Mirror。这个项目可以把数字面具投射到我的镜中倒影上：如果早上我想感到强大，可以戴上狮子面具；如果想获得鼓舞，也可以显示一句引语。

我使用通用人脸识别软件来构建系统，但发现如果不戴白色面具，就很难测试它。不幸的是，我以前也遇到过这个问题。本科在佐治亚理工学习计算机科学时，我曾研究社交机器人。其中一项任务是让机器人玩“躲猫猫”：双方遮住脸再露出来，说“peek-a-boo”。问题是，如果机器人看不见我，游戏就无法进行，而我的机器人确实看不见我。

为了完成项目，我借用了室友的脸，提交了作业，并以为总会有别人解决这个问题。没过多久，我去香港参加创业比赛。组织者带参赛者参观当地初创公司，其中一家公司展示了一个社交机器人。演示对每个人都有效，直到轮到我。你大概可以猜到，它检测不到我的脸。

我问开发者原因，结果发现我们使用的是同一套通用人脸识别软件。跨越半个世界，我明白了一个事实：算法偏见的传播速度，可以和从互联网上下载文件一样快。
""",
    "s2.4-ac5": """
问题到底出在哪里？为什么我的脸无法被检测到？我们需要看看机器视觉是如何被赋予的。计算机视觉使用机器学习技术进行人脸识别。基本过程是创建一个包含人脸样例的训练集：这是脸，这是脸，这不是脸。随着时间推移，计算机就学会识别其他人脸。

然而，如果训练集不够多样化，任何偏离既定规范太多的脸都会更难被检测到，这正是发生在演讲者身上的情况。但也有好消息：训练集不是凭空产生的，我们可以主动创造它们。因此，我们有机会创建覆盖完整光谱的训练集，更丰富地反映人类样貌。

演讲者的经历展示了社交机器人如何让她发现算法偏见带来的排斥。但算法偏见也可能导致歧视性实践。在美国，警察部门开始把人脸识别软件纳入打击犯罪的工具库。乔治城大学法学院的一份报告显示，美国每两个成年人中就有一个，也就是 1.17 亿人，已经出现在人脸识别网络中。警察部门目前可以在缺乏监管的情况下使用这些网络，而所用算法并未经过准确性审计。

我们知道，人脸识别并非万无一失，持续准确地标注人脸仍然是挑战。你也许在 Facebook 上见过这样的情况：朋友被照片系统误标，我们会觉得好笑。但误认犯罪嫌疑人绝不是笑话，侵犯公民自由也不是小事。

机器学习不仅用于人脸识别，也正在延伸到计算机视觉之外。数据科学家 Cathy O'Neil 在《数学毁灭性武器》中谈到新型“大规模杀伤性武器”：广泛、神秘且具有破坏性的算法越来越多地被用来决定生活的多个方面。谁被雇用或解雇？你能否获得贷款？能否买到保险？能否进入理想大学？你和我在同一平台购买同一产品时是否支付相同价格？

执法部门也开始使用机器学习进行预测性警务。一些法官使用机器生成的风险评分来决定一个人要在监狱中待多久。因此，我们必须认真思考这些决定是否公平。我们已经看到，算法偏见并不一定带来公平结果。
""",
    "S2.4-ac7": """
这是一个思想实验。假设在不久的将来，你驾驶自动驾驶汽车高速行驶在公路上，四周都被其他车辆包围。突然，前方卡车上掉下一个巨大而沉重的物体。你的车无法及时刹停以避免碰撞，因此它必须做出选择：直行撞上物体，向左撞上一辆 SUV，还是向右撞上一辆摩托车？

它应该通过撞向摩托车来优先保护你的安全吗？或者为了尽量减少对他人的危险而不转向，即使这意味着撞上大物体并牺牲你的生命？又或者采取折中方案，撞向一辆乘客安全评级较高的 SUV？自动驾驶汽车到底应该怎么做？

如果是我们在手动模式下驾驶那辆被包围的车，无论我们作何反应，都会被理解为一种反应，而不是深思熟虑的决定。那是出于本能和恐慌的动作，没有预谋，也没有恶意。但如果程序员事先指示汽车在未来感知到某些条件时做出同样动作，这看起来就更像是预谋杀人。

公平地说，自动驾驶汽车预计会通过消除驾驶中的人为错误，大幅减少交通事故和死亡人数。此外，它们还可能带来其他好处：缓解道路拥堵、减少有害排放，并减少低效且令人紧张的驾驶时间。但事故仍然可能发生。一旦发生，结果可能早在几个月甚至几年前，就已经由程序员或政策制定者决定好了。
""",
    "s2.4-ac8": """
自动驾驶汽车会面临困难决定。人们很容易提出“尽量减少伤害”这样的总体原则，但即使如此，也会迅速进入道德上的灰色地带。例如，仍然是类似情景：左边有一名戴头盔的摩托车手，右边有一名没戴头盔的摩托车手。你的自动驾驶汽车应该撞向谁？

如果你选择撞向戴头盔的人，因为她更可能存活，这是否等于惩罚了负责任的驾驶者？如果你选择撞向没戴头盔的人，因为他行为不负责任，那你就已经远远超出了最初“减少伤害”的设计原则，自动驾驶汽车开始执行某种街头正义。

伦理考虑在这里变得更加复杂。在这两个情景中，底层设计实际上像某种目标选择算法。换言之，它系统性地偏向或歧视某类将被撞击的对象。而目标车辆的车主会在没有任何过错的情况下，承受该算法带来的负面后果。

新技术正在打开许多新的伦理困境。比如，如果你必须在两种车之间选择：一种车在事故中总是尽可能拯救最多人的生命，另一种车无论如何都优先救你，你会买哪一种？如果车辆开始分析并考虑乘客身份及其人生细节，会发生什么？随机决策是否可能仍然优于预先设计的“最小伤害”决策？这些决定究竟应该由谁来做：程序员、公司还是政府？

现实不一定会完全按照思想实验发展，但这不是重点。思想实验的目的，是像科学实验检验物理世界一样，分离并压力测试我们的伦理直觉。现在识别这些道德急转弯，将帮助我们在技术伦理这条陌生道路上更好地行驶，也让我们能够更自信、更有良知地驶向勇敢的新未来。
""",
    "s2.4-ac14": """
我们正处在人类历史的转折点：一个物种站在获得星辰与失去家园之间。仅仅过去几年，我们就大大拓展了对地球在宇宙中位置的理解。NASA 的 Kepler 任务在其他恒星周围发现了数千颗潜在行星，表明地球只是银河系数十亿颗行星中的一颗。

Kepler 是一台空间望远镜，它通过测量行星经过恒星前方时造成的微弱变暗来寻找行星。Kepler 的数据揭示了行星的大小，以及它们与母恒星的距离。这些信息帮助我们判断行星是否像太阳系中的类地行星一样小而岩质，也帮助我们了解它们从母恒星获得多少光，从而推测这些新发现的行星是否可能宜居。

不幸的是，当我们发现这些潜在宜居世界的宝库时，我们自己的星球也正承受着人类活动的重压。2014 年是有记录以来最热的一年。存在了数千年的冰川和海冰正在几十年内消失。我们引发的全球尺度环境变化，正在迅速超过我们改变其走向的能力。

演讲者并不是气候科学家，而是天文学家。她研究恒星如何影响行星宜居性，希望找到宇宙中可能存在地外生命的地方。她说自己寻找的是“优质外星地产”。但越是寻找类似地球的行星，就越能体会地球本身的珍贵。每一个新世界都会促使我们把它与自己最熟悉的行星，也就是太阳系中的行星进行比较。

以邻居火星为例。火星小而岩质，虽然离太阳稍远，但如果由 Kepler 这样的任务发现，它可能会被视为潜在宜居世界。事实上，火星过去可能曾经宜居，这也是我们如此重视研究火星的原因。Curiosity 等探测车在其表面爬行，寻找生命起源的线索；MAVEN 等轨道器采样火星大气，试图理解火星如何失去过去的宜居性。私人航天公司如今不仅提供近太空短途旅行，还提出了在火星生活的诱人可能。

然而，尽管火星景观类似地球上的沙漠，并与我们想象中的开拓和边疆联系在一起，但与地球相比，火星是一个非常糟糕的居住地。想想我们甚至还没有殖民地球上的沙漠，而那些地方与火星相比已经肥沃得多。即使在地球最干燥、最高的地方，空气也充满氧气，那是数千英里外雨林呼出的甜美厚重的空气。

演讲者担心，围绕殖民火星和其他行星的兴奋背后，带着一个漫长而阴暗的影子：有人暗示并相信，火星会拯救我们，使我们逃离对唯一真正宜居星球地球的自我毁灭。她热爱星际探索，但深深反对这种想法。去火星有很多充分理由，但如果有人说火星可以作为人类备份，那就像泰坦尼克号船长告诉乘客，真正的派对稍后会在救生艇上举行。

星际探索和行星保护的目标并不冲突。相反，它们是一同理解、保护并改善未来生命这一目标的两个方面。地球上的极端环境本身就是外星景观，只是离家更近。如果我们能够理解如何在地球上充满敌意、不宜居的环境中创造并维持宜居空间，也许就能同时满足保护自身环境和走向地球之外的需求。

最后是费米悖论。物理学家 Enrico Fermi 多年前提出：宇宙已经存在很长时间，而且我们认为其中有许多行星，那么我们现在应该已经发现外星生命的证据了。那么他们在哪里？费米悖论的一种可能解释是：当文明发展到足以考虑在群星之间生活时，它们会忘记保护孕育这种进步的母星有多么重要。

相信仅靠行星际殖民就能把我们从自身手中拯救出来，是一种傲慢。但行星保护和星际探索可以并行。如果我们真的相信自己有能力改造火星这种敌对环境，使其适合人类居住，那么我们也应当能够完成一个容易得多的任务：保持地球的宜居性。
""",
    "s2.5-ac4": """
当演讲者告诉别人自己在辩论队时，通常会得到两种反应。第一种是：“我永远做不到。”第二种是：“哇，大家一直说我很适合辩论，我很喜欢吵架。”这两种反应都说明了我们今天看待辩论方式中的一个真实问题：辩论被视为一场争斗。

如果论证被看作争斗，那么赢家似乎就是声音最大、舞台上最漂亮、或者能够获得最多支持的人。但真正的辩论远不止如此。它关乎谁是更好的表达者，谁能更有力地阐明观点。

演讲者并不是单纯为了拉人加入辩论队，虽然她也半开玩笑地说你应该加入。她真正想做的是让我们重新审视自己形成论点和观点的方式，因为真正的辩论需要事实、逻辑、推理和反驳来支撑。

她讲了自己第一次记得输掉辩论的故事。那时她和妈妈、姐姐坐在车里放学回家，她告诉她们当天学到的知识：珠穆朗玛峰是世界上最高的山。姐姐立刻反驳说，夏威夷的 Mauna Kea 其实高得多。演讲者开始大喊，说姐姐错了。剧透一下：错的是演讲者。

Mauna Kea 是夏威夷的一座火山，如果从海平面以下算起，它比珠穆朗玛峰大约高一英里。但演讲者当时并不知道。她从老师那里学到珠穆朗玛峰最高，于是相信这一点，并用语言奋力维护它。姐姐会赢这场“争斗”，而演讲者则是在信息不完整的情况下拼命维护自己的观点。
""",
    "s2.5-ac5": """
那么，怎样才能避免在争论中显得完全无知？你需要学会建立一个有依据的论点。第一步，是理解问题以及问题的语境。回到山的例子，如果问题被表述为“包括海平面以上和以下高度在内，最高的山是哪一座”，演讲者就有机会思考并审视自己的立场。她会意识到自己的统计数据只适用于海平面以上，还是包括海平面以下；也会明白在这个语境中，自己的数据并不相关，答案可能还有其他可能性。

这并不只适用于山。当你在讨论中建立观点时，你必须知道自己在说什么，必须理解被问到的问题是什么。由于演讲者没有弄清是否包括海平面以下的高度，她无法建立有依据的论点。对于人们更有激情的话题，大家更容易忘记审视论证背后的推理和语境，而这些对形成并捍卫观点至关重要。

第二，你需要从多个相关视角理解论点。再回到 Mauna Kea 的例子，演讲者当时只知道珠穆朗玛峰是最高的山，因为她只听说过这座山。如果她研究过其他山，就可能发现有些山的高度会把海平面以下和以上都计算进去。这样，她就能在问题语境中重新评估自己的论点，并理解为什么姐姐认为她错了。

这一点也适用于许多争论。人们在讨论中显得无知，常常是因为没有考虑所有与争论相关的人。世界上有很多不同于你的观点；一个在你看来非黑即白的问题，在别人看来可能充满色彩。要形成论点，你需要看见所有相关视角。

最后，也是最重要的一点：你必须审视与你相反的一方。在辩论中，这被称为你的正方对应的反方，或你的反方对应的正方。对方从根本上认为你错了。辩论之所以存在，正是因为有人认为你错，并且他们有理由相信自己正确，还会捍卫这个理由。

如果你理解为什么自己正确，并发现对方为什么错误，你就能在争论中证明自己的观点。回到山的例子，姐姐认为自己正确，是因为她从海平面以下和以上的总高度来看问题。如果演讲者把论点重新表述为“珠穆朗玛峰是世界上海平面以上最高的山”，她每次都能赢得这个论证。

在现实中，人们辩论时常常依赖快速判断，并激烈维护这些判断，尽管后来常常发现自己信息不足或回答错误。真正的辩论要求你慢下来，成为更好的信息消费者。为了证明一个观点，你需要看见所有视角和语境，需要在理解问题语境的同时审视反方观点。做到这些，你就能用理智表达内心所信，而不是让情绪支配理智对信息的理解。

所以下一次当你陷入争论或讨论，感到慌乱时，演讲者恳请你：不要提高嗓门，而要改进你的论证。最后，她再次邀请大家加入辩论队。
""",
    "s2.6-ac7&8": """
演讲者承认，在食物面前自己很容易被诱惑。无论是糖、油脂还是碳水，他都很难拒绝。他常去蒙大拿州，对他来说，一块五分熟、草饲的肋眼牛排几乎是美味的极致。虽然他并不常吃，但每次吃时都会有些矛盾，其中一个原因就是地球。

问题是：我吃什么到底有多大影响？它真的能影响全球变暖这样巨大的问题吗？事实证明，我们放在盘子里的食物非常重要。全球气候变化问题中约 25% 可以追溯到食物，以及我们每天关于吃什么所做的选择。这一比例高于地球上所有汽车造成的影响，事实上，食物相关的全球变暖污染大约是汽车的两倍。

加州大学戴维斯分校的 Ben Houlton 和 Maya Almaraz 研究气候与饮食之间的关系。他们追踪食物生产方式如何产生温室气体并推动全球变暖。通过数据，他们计算不同食物和不同饮食会产生多少碳污染。许多人在气候变化面前感到无力，觉得自己无法产生影响。但研究显示，个人选择确实可能带来巨大影响。

以演讲者喜爱的草饲肋眼牛排为例。如果把一份牛肉背后的所有环节都算进去，大约会排放 330 克碳，相当于开车 3 英里。如果改吃鸡肉，排放量会下降五倍以上；换成鱼，数字还会更低；如果完全用扁豆替代牛肉，排放几乎降到接近零。

为什么牛肉，以及羊肉，对地球影响如此大？畜牧业占全球温室气体排放的 14% 多一点。如果这个数字看起来不高，要知道它大约等于整个交通运输部门，包括全球所有汽车、卡车、飞机、火车和船舶的排放总和。部分原因是牛羊等反刍动物会产生大量气体，其中甲烷的温室效应至少是二氧化碳的 25 倍。此外，饲养牲畜还需要大量土地、化肥和约 10 亿吨谷物，而这些谷物本可以养活 35 亿人。如果我们直接食用这些谷物，就能消除许多来自牛肉生产的二氧化碳排放。

肉类显然具有很大的碳负担，但也要记住，并非所有牲畜饲养方式都相同。例如在美国西部的一些地区，牧场主正在尝试以有助于恢复土地的方式饲养牲畜，并探索如何利用土壤和草地把碳污染留在空气之外。即使是这些可持续牧场主也会说，我们可能吃了太多肉。在美国，如果午餐或晚餐没有肉，许多人会问：“肉什么时候上？” 美国的人均肉类足迹已经处于世界较高水平。

那么完全不吃肉如何？从对地球影响最小的角度看，纯素饮食最好。但在排放方面，纯素饮食与素食饮食差别并不大。研究团队还发现，地中海饮食的环境影响与纯素和素食饮食相近。它比美国人习惯的饮食少很多肉：每周吃几次鱼和禽肉，每月也许吃一次牛肉，大量植物性食物，当然还有许多橄榄油。

减少 90% 的肉类摄入，比彻底消除所有肉类更重要。我们不必人人都成为纯素者，甚至不必人人都成为素食者。只要减少肉类摄入，每一点都有效；如果减少很多，就能对气候帮助很大。如果所有人都改向地中海饮食，到 2050 年可能解决 15% 的全球变暖污染。若每个人都朝这个方向转变，其效果相当于每年让约 10 亿辆汽车从道路上消失。

如果你仍然想吃比地中海饮食建议更多的肉，只要把份量减少到医生建议的 4 盎司，就能把排放减少一半。这非常可观。事实上，医生告诉我们，为了健康饮食，我们现在吃的肉大约是实际需要的两倍。好消息是，人们正在听从医生建议。过去十年，我们吃的牛肉量下降了 19%。这些已经被告知对健康有益的事情，恰好也对地球有益。

所以，我们吃什么确实是气候拼图的重要部分。并不是每个人都负担得起电动车或在房屋上安装太阳能板，但每个人每天都要吃饭。这些选择加在一起会形成巨大数字。由于肉类具有较大碳负担，我们需要认真思考吃多少肉。至于演讲者深爱的肋眼牛排，他也真诚地在努力减少，也许只是吃更小块的牛排，或者把一道肉菜换成素食汉堡。看似小事，累积起来却能产生重大影响。
""",
}

SENTENCE_BREAKS = {
    "S2.1-ac4&5": [4, 9, 12],
    "S2.1-ac7": [3, 8, 12],
    "S2.1-ac8": [3, 6, 15, 18, 32],
    "S2.2-ac4": [4, 10, 13, 16, 22],
    "S2.2-ac5": [5, 12, 18, 26, 31],
    "s2.2-ac7": [4, 7, 12, 16, 21, 26, 31],
    "s2.2-ac8": [3, 7, 15],
    "s2.3-ac7&8": [3, 7, 20, 30, 38, 50],
    "s2.3-ac14": [4, 10, 15, 21],
    "s2.4-ac4": [5, 10, 17],
    "s2.4-ac5": [7, 12, 17, 21, 29],
    "S2.4-ac7": [5, 9, 12],
    "s2.4-ac8": [4, 6, 10, 18],
    "s2.4-ac14": [3, 7, 11, 17, 24, 27, 32, 37, 41],
    "s2.5-ac4": [6, 9, 12, 20],
    "s2.5-ac5": [7, 11, 17, 21, 28, 31, 36],
    "s2.6-ac7&8": [8, 14, 19, 26, 35, 41, 47, 55, 62],
}


ENGLISH_CORRECTIONS = {
    "S2.1-ac7": [
        (
            "If I send you $100, it's really important that I don't still have money and that I can't send it to you.",
            "If I send you $100, it's really important that I don't still have the money and that I can't send the same money to someone else.",
        ),
    ],
    "S2.1-ac8": [
        ("a nation's state", "a nation-state"),
        ("And everyone is time stamped", "And every block is time-stamped"),
    ],
    "S2.2-ac4": [
        ("due to starting Greenwich, London next year", "due to start in Greenwich, London next year"),
        ("Thanks very much.", "Think of this."),
        ("Research by McKinsey's", "Research by McKinsey"),
        ("changes that transform the Victorian world", "changes that transformed the Victorian world"),
    ],
    "S2.2-ac5": [
        ("most of member states and of the governance", "most member states and governance bodies"),
        ("think on taxing robots", "think about taxing robots"),
        ("feed and stapling", "feed and stabling"),
    ],
    "s2.3-ac7&8": [
        (
            "And it's very shortly from there to men make better programmers than women.",
            "And it's a very short leap from there to the idea that men make better programmers than women.",
        ),
        ("Salesforce Science Team", "Salesforce Einstein"),
        ("1950s Mad Men Secretary", "1950s Mad Men secretary"),
        ("sexist racist machines", "sexist, racist machines"),
        ("their code was accepted 4% more than men", "their code was accepted 4% more than men's code"),
    ],
    "s2.4-ac4": [
        ("white mass", "white mask"),
        ("unless if I wore a white mask", "unless I wore a white mask"),
        ("I could put on a lion.", "I could put on a lion mask."),
        ("and then uncover it saying peek-a-boo", "and then uncover it, saying peek-a-boo"),
        ("But I barred my roommate's face", "But I borrowed my roommate's face"),
    ],
    "s2.4-ac5": [
        (
            "how social robots was how I found out about exclusion with algorithmic bias",
            "how social robots were how I found out about exclusion through algorithmic bias",
        ),
        ("facial recognition is not felt proof", "facial recognition is not foolproof"),
        ("Data Scientist, Kathy O'Neill", "data scientist Cathy O'Neil"),
    ],
    "S2.4-ac7": [
        ("benefits— eased", "benefits - eased"),
    ],
    "s2.4-ac8": [
        ("meeting out street justice", "meting out street justice"),
    ],
    "s2.4-ac14": [
        ("planets sizes", "planet sizes"),
        ("choice-alien real estate", "choice alien real estate"),
    ],
    "s2.5-ac4": [
        ("Yeah, debate is so much more than that.", "Yet debate is so much more than that."),
        ("who can illustrate their points the strongest", "who can illustrate their points most strongly"),
        (
            "But I fought to get that point together, even though I didn't have all the information.",
            "But I fought to defend that point anyway, even though I didn't have all the information.",
        ),
    ],
    "s2.5-ac5": [
        (
            "For this question, I was let, I didn't understand if we were including below and above sea level",
            "For this question, I was led astray; I didn't understand if we were including below and above sea level",
        ),
        ("mountains that heights was included", "mountains whose height was included"),
        ("Often people come across as ignorant or in a discussion", "Often people come across as ignorant in a discussion"),
        ("Everyone, there are lots of different opinions than yours", "There are lots of opinions different from yours"),
        ("can be seen as very colorful and someone else's", "can be seen as very colorful in someone else's"),
        ("all the responsive perspectives", "all the relevant perspectives"),
        ("the con to your pro or the affirmation to your negation", "the con to your pro, or the affirmative to your negative"),
        ("we use quick judgments and we make and we avidly defend those", "we make quick judgments and avidly defend them"),
        ("and answered it wrongly", "and answered wrongly"),
        (
            "And you need to look at the question in a context additionally to looking at the opposing side of the argument.",
            "You also need to look at the question in context, in addition to looking at the opposing side of the argument.",
        ),
    ],
    "s2.6-ac7&8": [
        ("Ben Holton and Maya Almoroz", "Ben Houlton and Maya Almaraz"),
    ],
}


def apply_english_corrections(stem: str, text: str) -> str:
    for old, new in ENGLISH_CORRECTIONS.get(stem, []):
        text = text.replace(old, new)
    return text


def clean_text(text: str) -> str:
    return " ".join(text.split())


def tex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def format_paragraphs(text: str) -> str:
    paras = [clean_text(p) for p in textwrap.dedent(text).strip().split("\n\n") if clean_text(p)]
    return "\n\n".join(tex_escape(p) for p in paras)


def raw_paragraphs(text: str) -> list[str]:
    return [clean_text(p) for p in textwrap.dedent(text).strip().split("\n\n") if clean_text(p)]


def translation_text(stem: str) -> str:
    if revised_translations and stem in revised_translations.TRANSLATIONS:
        return revised_translations.TRANSLATIONS[stem]
    return TRANSLATIONS[stem]


def read_english(stem: str) -> str:
    path = RAW / f"{stem}.txt"
    if not path.exists():
        return "[Missing transcript]"
    return apply_english_corrections(stem, clean_text(path.read_text(encoding="utf-8")))


def split_sentences(text: str) -> list[str]:
    text = clean_text(text)
    parts = re.split(r"(?<=[.!?])\s+", text)
    return [p.strip() for p in parts if p.strip()]


def capitalize_initial(text: str) -> str:
    match = re.search(r"[A-Za-z]", text)
    if not match:
        return text
    i = match.start()
    return text[:i] + text[i].upper() + text[i + 1 :]


def split_by_reference_lengths(text: str, refs: list[str]) -> list[str]:
    sentences = split_sentences(text)
    count = len(refs)
    if count <= 1 or len(sentences) <= 1:
        return [capitalize_initial(text)]

    sentence_word_totals = []
    running_words = 0
    for sentence in sentences:
        running_words += len(sentence.split())
        sentence_word_totals.append(running_words)

    ref_lengths = [max(1, len(re.sub(r"\s+", "", ref))) for ref in refs]
    total_ref_length = sum(ref_lengths)
    total_words = sentence_word_totals[-1]
    targets = []
    running_ref = 0
    for ref_length in ref_lengths[:-1]:
        running_ref += ref_length
        targets.append(total_words * running_ref / total_ref_length)

    breaks = []
    previous = 0
    for idx, target in enumerate(targets):
        remaining_chunks = len(targets) - idx
        max_boundary = len(sentences) - remaining_chunks
        candidates = range(previous + 1, max_boundary + 1)
        boundary = min(candidates, key=lambda j: abs(sentence_word_totals[j - 1] - target))
        breaks.append(boundary)
        previous = boundary
    return chunks_from_breaks(sentences, breaks)


def chunks_from_breaks(sentences: list[str], breaks: list[int]) -> list[str]:
    chunks = []
    previous = 0
    for boundary in breaks + [len(sentences)]:
        chunks.append(capitalize_initial(" ".join(sentences[previous:boundary]).strip()))
        previous = boundary
    return chunks


def aligned_english_chunks(stem: str, zh_paras: list[str]) -> list[str]:
    sentences = split_sentences(read_english(stem))
    breaks = SENTENCE_BREAKS.get(stem)
    if breaks and len(breaks) == len(zh_paras) - 1 and all(0 < b < len(sentences) for b in breaks):
        return chunks_from_breaks(sentences, breaks)
    return split_by_reference_lengths(read_english(stem), zh_paras)


def paired_rows(stem: str) -> str:
    zh_paras = raw_paragraphs(translation_text(stem))
    en_chunks = aligned_english_chunks(stem, zh_paras)
    rows = []
    for i, zh in enumerate(zh_paras):
        en = en_chunks[i] if i < len(en_chunks) else ""
        rows.append(
            r"\textbf{%02d}\quad %s & \textbf{%02d}\quad %s \\ \hline"
            % (i + 1, tex_escape(en), i + 1, tex_escape(zh))
        )
    return "\n".join(rows)


def main() -> None:
    sections = []
    for idx, (stem, session, title) in enumerate(ITEMS, start=1):
        section_title = f"{session}: {title}"
        sections.append(
            rf"""
\clearpage
\section{{{tex_escape(section_title)}}}
\addcontentsline{{toc}}{{subsection}}{{{tex_escape('中文译名：' + chinese_title(title))}}}

\renewcommand{{\arraystretch}}{{1.23}}
\begin{{longtable}}{{>{{\TranscriptColumn}}p{{0.47\textwidth}} >{{\TranscriptColumn}}p{{0.47\textwidth}}}}
\rowcolor{{headerBg}}\textbf{{English Transcript}} & \textbf{{中文翻译}} \\ \hline
{paired_rows(stem)}
\end{{longtable}}
"""
        )

    body = "\n".join(sections)
    tex = rf"""
\documentclass[UTF8,zihao=-4,fontset=fandol]{{ctexart}}
\usepackage[a4paper,margin=2.15cm,headheight=15pt]{{geometry}}
\usepackage{{fontspec}}
\usepackage{{xeCJK}}
\usepackage{{xcolor}}
\usepackage{{hyperref}}
\usepackage{{bookmark}}
\usepackage{{titlesec}}
\usepackage{{fancyhdr}}
\usepackage{{array}}
\usepackage{{longtable}}
\usepackage{{colortbl}}
\usepackage[most]{{tcolorbox}}
\usepackage{{enumitem}}
\usepackage{{microtype}}

\definecolor{{ink}}{{HTML}}{{111827}}
\definecolor{{muted}}{{HTML}}{{64748B}}
\definecolor{{accent}}{{HTML}}{{1F3A5F}}
\definecolor{{accentLight}}{{HTML}}{{EEF3F8}}
\definecolor{{headerBg}}{{HTML}}{{F1F5F9}}
\definecolor{{line}}{{HTML}}{{CBD5E1}}
\definecolor{{soft}}{{HTML}}{{F8FAFC}}

\hypersetup{{
  colorlinks=true,
  linkcolor=accent,
  urlcolor=accent,
  citecolor=accent,
  pdftitle={{智汇大学英语听说教程4 Theme 2 中英对照文字稿}},
  pdfauthor={{Codex}},
  pdfsubject={{WE Learn transcript bilingual notes}}
}}

\pagestyle{{fancy}}
\fancyhf{{}}
\lhead{{\textcolor{{muted}}{{智汇大学英语听说教程4 / Theme 2}}}}
\rhead{{\textcolor{{muted}}{{中英对照文字稿}}}}
\cfoot{{\thepage}}
\renewcommand{{\headrulewidth}}{{0.4pt}}
\arrayrulecolor{{line}}

\titleformat{{\section}}
  {{\Large\bfseries\color{{accent}}}}
  {{\thesection}}
  {{0.75em}}
  {{}}
\titleformat{{\subsection}}
  {{\large\bfseries\color{{ink}}}}
  {{\thesubsection}}
  {{0.75em}}
  {{}}
\titlespacing*{{\section}}{{0pt}}{{1.2em}}{{0.6em}}

\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0.72em}}
\setlist{{nosep,leftmargin=1.4em}}
\hyphenpenalty=10000
\exhyphenpenalty=10000
\emergencystretch=2em
\newcommand{{\TranscriptColumn}}{{\raggedright\arraybackslash\hyphenpenalty=10000\exhyphenpenalty=10000\sloppy}}

\newtcolorbox{{infobox}}{{
  enhanced,
  breakable,
  colback=accentLight,
  colframe=accent,
  boxrule=0.45pt,
  arc=2mm,
  left=8pt,
  right=8pt,
  top=6pt,
  bottom=6pt,
  before upper={{\raggedright}}
}}

\begin{{document}}
\begin{{titlepage}}
\centering
\vspace*{{2.9cm}}
{{\Huge\bfseries\textcolor{{accent}}{{智汇大学英语听说教程4}}\par}}
\vspace{{0.45cm}}
{{\LARGE Theme 2 中英对照视频文字稿\par}}
\vspace{{0.55cm}}
{{\textcolor{{line}}{{\rule{{0.52\textwidth}}{{0.6pt}}}}\par}}
\vfill
{{\large\textcolor{{muted}}{{生成日期：2026-06-02}}\par}}
\end{{titlepage}}

\pagenumbering{{roman}}
\tableofcontents
\clearpage
\pagenumbering{{arabic}}

{body}

\end{{document}}
"""
    OUT.write_text(tex.strip() + "\n", encoding="utf-8")
    print(OUT)


def chinese_title(title: str) -> str:
    mapping = {
        "AGI, the Top One Emerging Technology that Are Changing Our World": "改变世界的顶尖新兴技术：人工通用智能",
        "How Blockchain Works (Part 1)": "区块链如何运作（上）",
        "How Blockchain Works (Part 2)": "区块链如何运作（下）",
        "Automation in Workplaces and Its Implication (Part 1)": "职场自动化及其影响（上）",
        "Automation in Workplaces and Its Implication (Part 2)": "职场自动化及其影响（下）",
        "The Digital Divide (Part 1)": "数字鸿沟（上）",
        "The Digital Divide (Part 2)": "数字鸿沟（下）",
        "How to Keep Human Bias Out of AI": "如何避免人类偏见进入人工智能",
        "Ethics of AI: Challenges and Governance": "人工智能伦理：挑战与治理",
        "How I'm Fighting Bias in Algorithms (Part 1)": "我如何对抗算法偏见（上）",
        "How I'm Fighting Bias in Algorithms (Part 2)": "我如何对抗算法偏见（下）",
        "The Ethical Dilemma of Self-Driving Cars (Part 1)": "自动驾驶汽车的伦理困境（上）",
        "The Ethical Dilemma of Self-Driving Cars (Part 2)": "自动驾驶汽车的伦理困境（下）",
        "Let's Not Use Mars as a Backup Planet": "不要把火星当作备用星球",
        "The Art of Debate (Part 1)": "辩论的艺术（上）",
        "The Art of Debate (Part 2)": "辩论的艺术（下）",
        "How Our Food Choices Affect Climate Change": "我们的食物选择如何影响气候变化",
    }
    return mapping.get(title, title)


if __name__ == "__main__":
    main()
