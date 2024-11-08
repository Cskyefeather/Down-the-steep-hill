image pure_black = "#000"
image pure_white =  "#ffffff"
image act_1 = Text("{font=SourceBirdsong.ttf}Act 1 第一章", color="#000000")
image act_1_title = Text("{font=SourceBirdsong.ttf}一个不幸的意外【Down the rabbit hole】", color="#000000")
image scene_1 = Text("{font=SourceBirdsong.ttf}Scene 1 幕一", color="#000000")
image scene_1_title= Text("{font=SourceBirdsong.ttf} 不平凡的一天【A day as usual】", color="#000000")
image scene_2 = Text("{font=SourceBirdsong.ttf}Scene 2 幕二" , color="#000000")
image scene_2_title= Text("{font=SourceBirdsong.ttf} 冰可乐和莎士比亚【Ice coke and Shakespeare】", color="#000000")
image scene_3 = Text("{font=SourceBirdsong.ttf}Scene 3 幕三", color="#000000")
image scene_2_title= Text("{font=SourceBirdsong.ttf} 对讲机【Radio】", color="#000000")
image bg = Text("{font=SourceBirdsong.ttf}背景占位符", color="#000000")
image end = Text("{font=SourceBirdsong.ttf}第一章 完", color="#000000")


define c1 = Character(None)
define c2 = Character(None)
define mind = Character(None, kind=nvl, color="#000000")


style drop_shadow_1:
    size 40
    outlines [ (0, "#101010", 2, 2) ]

label start:
    scene pure_black
    show pure_white with Dissolve(2.0)
    show act_1 at truecenter with Dissolve(1.0)
    pause 0.5
    hide act_1 with Dissolve(1.0)
    show act_1_title at truecenter with Dissolve(1.0)
    pause 0.5
    hide act_1_title with Dissolve(1.0)
    show scene_1 at truecenter with Dissolve(1.0)
    pause 0.5
    hide scene_1 with Dissolve(1.0)
    show scene_1_title at truecenter with Dissolve(1.0)
    pause 0.5
    hide scene_1_title with Dissolve(1.0)
    hide pure_white with Dissolve(2.0)

    ##我其实觉得这个开场太长了，字体太小了，你按着你的喜好调整一下。

    show 0020 with Dissolve(1.0)

    window show 
    
    play music "<loop 2.999>3001.ogg"

    mind"""
    这是我第二个无所事事的暑假，也是我在街上晃悠的第二周。
    
    天气热得令人发指，让在外面逗留变成了一种折磨。
    
    附近的百货超市已经逛腻味了，而售货员也大概记得我的脸了吧？一个背着书包，从来不花一分钱的年轻学生总归是十分显眼的。
    
    我已经开始想家了，至少家旁边的商城有不花钱的闲书可看。
    
    算了。回了家就没空去那看书了。

    {clear}

    """
    window hide
    
    show 0010 with Dissolve(2.0)

    window show

    mind"""
    这里，是我外祖父母的家。

    因为我拒绝在中考结束后参加任何补习班，也不愿意留在家里给我妈做饭，她就姑且将我寄存在这个南方工业小城。
    
    这里有着永远炎热潮湿的夏季，湿淋淋的墙壁，可以发霉的一切东西。

    由于外婆见不得我终日待在家中无所事事，我便只好改为在外面闲逛。一整个职工宿舍区已经走了个遍，然后是大街，百货商场，步行街……徒步能到的地方我都去过了，除了依山而建的住宅区。
    
    {clear}"""

    show 0020 with Dissolve(0.8)

    mind"""
    我讨厌山。就是这样。

    从小我妈就恐吓我，只要我不乖，就将我遗弃在山里。夏季的山林中只有蝉鸣，反而生出一种毛骨悚然的寂静。

    我偶尔会迷失在城市里，但山林……它有着吞噬我的能力。
    
    因此我偶尔会假设乡村里存在着什么神秘的力量，将我冥冥之中隔离于其外。
    
    {clear}"""   
    
    mind"""
    还是好热。

    除开日常积蓄以外，我的口袋里还剩6块钱，够买一份豆花，或是两瓶可乐。随着年龄增长，我开始逐渐对饮料失去兴趣，简直是一种不祥的，长大的征兆。
    
    因而除开家外，可以解暑的地方只剩下更高的山。翠绿的边沿总是与背景暧昧不清，被水汽蒙上了一层毛边，更显突兀。
    
    {clear}"""

    
    mind"""唉。更高的山。

    于是我咬咬牙，从职工宿舍区的后门出去，沿着大路一路向上。"""

    window hide

    show 0070 with Dissolve(2.0)

    window show

    mind"""
    除了树叶被风吹动的沙沙声，还有永无止息的蝉鸣，路上不会有其它的声音，热量好像把时间都要扭曲。

    {clear}
    
    也对，现在是下午2点，一天中最热的时候，当地人都躲在家里睡午觉，几乎不会有什么人甘愿在阳光下暴晒————

    除了我这个无所事事的外乡人。

    {clear}

    一步，两步，三步。

    被铁链锁上的旧工厂大门，公交站牌，空荡荡的职高。

    我先数停靠在路边的电动车，再数地上的光斑，最后退无可退。

    ……这里真的不会有什么山精野怪吗？
    
    """

    window hide

    show 0040 with Dissolve(1.5)

    """
    
    我就是在那里遇见的她。

    那是一个小公园。说是公园，其实只有坑坑洼洼的登山步道和几张大理石凳，在这个城市很常见，都是退休的老头老太太们集资修的。"""
    
    show 0060 with Dissolve(1.5)
    
    """

    圆凳触感滚烫，根本不能在上面歇息。
    
    """

    show 0050 with Dissolve(1.5)
    """

    我抬起头，一个黑色的运动挎包孤零零地在树枝上挂着。

    周围的一切都太安静了。

    我想回家。

    """
    show 0001
    play music "3005.ogg" fadeout 4.0 fadein 5.0

    ## 这里我不想让对话框消失，但是如果写 window show变得很不自然，师傅救一下
    
    """

    我讨厌放假，真的。

    我只是不想待在这里，也不想待在家而已。

    不喜欢蝉鸣，不喜欢夏天，不喜欢山林。

    我的心声总是在这样寂静而空旷的地方回荡，无路可走，无处可藏。
    
    「什么都不喜欢，那你怎么不赶紧去死啊！死你喜欢吗？」
    
    老实说，我不知道。

    活着很辛苦，但是我还是有在努力。

    不清楚努力的意义，但是也懒得去质疑。
    
    或许这样反而能长命一点吧，要做的事情有这么多，这些事情实在没空去想。
       
    但是哪怕如此这般地自我说服着，独自一人的时候，还是打心底里感到恐慌。
    
    ......就像现在一样。

    """
    stop music fadeout 3.0
    hide 0001
    ##莫名其妙变红了但是竟然没出bug

    """

    树上发出窸窸窣窣的声音，听起来像某种小动物。

    我下意识抬头，才发现树上有一个模糊身影。

    那是一个女孩子。我看不太清她的脸，但看穿着似乎与我年纪相仿。
    
    「喂——你在干什么？」我大声喊道。

    你问我哪来的勇气？

    废话，这是我在过去的两周内遇到的唯一一个同龄人。

    我已经很久没能和人心平气和地说上话了。
 
    只要不是山精野怪，什么都好。
    """
    show 10002
    play music "<loop 47.999>3002.ogg" fadeout 0.2 fadein 2.0
    """
    她没搭话，探出头来看了我一眼。
    """
    show 20005
    show 11002
    hide 10002
    
    c2"""
    「请问你是怎么上去的？」
    """
    show 10001
    show 21005
    hide 20005
    hide 11002
    """
    她用手指了指树的背面。
    """
    show 11001
    show 20019
    hide 10001
    hide 21005
    """
    我绕过去看，才发现后面有一个用麻绳编织而成的梯子，看起来很结实地被钉在树上。
      
    """
    show 11002
    show 20013
    hide 11002
    hide 20019
    c2"""
    「那请问，我可以上来吗？」
    """
    show 21013
    show 10005
    hide 11001
    hide 20013
    """
    她转过头来盯着我，似乎很用力地在思考，但最后还是点了点头。

    """
    show 11002
    show 20005
    hide 21013
    hide 10005
      
    """
    于是我把书包留在了树下，手脚并用地向上爬。
    """
    show 20016
    hide 21013
    hide 20005

    c2"""
    「嘿咻。」

    「同学你好厉害，我第一次见到有人在树上坐着。」
    """
    show 10003
    show 21016
    hide 20016
    hide 11002
    """
    她隐晦地笑了一下，往右边挪了一截，给我腾出了一个位置。
    """
    show 11003
    show 20010
    hide 21016
    hide 10003
    """
    !

    我两脚凌空，终于尝出三分胆怯。

    """
    show 20014
    hide 20010

    """
    又转念一想，为自己仍旧能够感到害怕而欣喜。
    """
    show 20013
    hide 20014
    c2"""
    「你在树上干什么？」
    """
    show 10007
    show 21013
    hide 20013
    hide 11003
    c1"""
    「看书。」
    """
    show 11016
    hide 10007
    show 20016 
    hide 21013
    c2"""
    「什么书？」
    """
    show 10016
    hide 11016
    show 21016
    hide 20016
    """
    她把书的封面举起来，对着我的脸。
    """
    show 20013
    hide 21016
    show 11002
    hide 10016
    c2"""
    「《仲夏夜之梦》？莎士比亚的四大喜剧？」
    """
    show 10004
    hide 11002
    show 21016
    hide 20013
    """
    她点了点头，看起来很满意我的反应。
    """
    show 20007
    hide 21016
    show 11005
    hide 10004
    c2"""
    「你喜欢那个英国老头吗？」
    """
    show 21016
    show 10010
    hide 20007
    hide 11005
    """
    ......
    """
    show 10013
    hide 10010

    """
    她又把视线放在了书上。
    """
    show 20013
    hide 21016
    show 11013
    hide 10013
    
    c2"""
    「同学？」

    """
    hide 20013
    hide 11013
    
    ##转场没做 声效没加

    """
    下一秒，我的视线天旋地转。
    
    再然后发现，我的书包好端端地坐在我的背后。

    我抬起头，发现那个家伙正在歪着头看着我。
    
    """
    show 11001
    """
    
    察觉我的视线，她又很快地把整个人缩了回去。
    
    """
    hide 11001
    """

    这都什么人啊。

    不过，这确实给这个炎热的夏季带来了一丝真实的凉意。
    """
    stop music fadeout 4.0
    """


    我是怎么下来的？
    """

    scene pure_black with Dissolve(2.0)
    show pure_white with Dissolve(2.0)
    show scene_2 at truecenter with Dissolve(1.0)
    pause 0.5
    hide scene_2 with Dissolve(1.0)
    show scene_2_title at truecenter with Dissolve(1.0)
    pause 0.5
    hide scene_2_title with Dissolve(1.0)
    hide pure_white with Dissolve(2.0)

    ""
    show 0030

    """"
    嗯，所以事情就是这样。我还要去找那家伙。那样做太危险了。
    
    平白无故地把人从树上推下来，是我就算了，要是让其他不明所以的人受伤了怎么办？

    ……除了这样一个冠冕堂皇的借口，我也不得不承认，她真的有点奇怪。

    我在学校可以交流的女同学不多，但据我所知，没有一个女孩是这个样子的。

    哪怕是我初中年级第一的大学霸，也是会屈尊和人搭话的。

    这家伙安静，漂亮——和颜值无关，任何一个愿意和我接近的女生都很漂亮——但是确实不太对劲。

    她实在是……太安静了。

    不过，能把莎士比亚看得津津有味的应该也不是什么常人，这位神仙小姐只是嫌我烦到她看书了也说不定。
    """
    show 0030

    """

    "老板，两瓶可乐。"
    小卖部的老板用带着浓重口音的方言问我:"""
    "小伙子，你不在这边读书吧？"
    "嗯。这不是放暑假嘛，到我外公外婆家来玩。"
    "这都放假了怎么还穿校服？这么爱学习啊。"
    "穿久了就习惯了，方便。"
    """我随便敷衍了两句，接过了可乐。"""
    """
    非要说的话确实是因为麻烦。

    每天对着镜子漱口的时候，我都能发现我开始越来越像亲爹。

    无论穿新衣服还是旧衣服都等同于在他人面前提起他，点背了还会招来一顿臭骂。

    最开始还会试图争辩这也不是我能控制的，是基因，基因。时间久了以后我习惯不去开口辩解，才发现还是校服最安全无害。

    算了。不想这个。还不如想想今天运气好不好，能不能碰上她。
    """
    """所幸，黑色挎包还是在同一个树杈上晃荡。"""
    
    show 0050

    """

    "请问——我可以上来吗——"
    ""她微微探出头来，看了我一眼。"""
    """我只好走到梯子旁边再问一次。"""
    """还是没有任何回应。"""
    "那个……我需要征求你的同意。"
    "……好吧。"

    "嗯……这是我给你带的汽水。"
    "嗯？"
    """她很惊讶地看着我。"""
    c2"你一直在树上坐着，很热吧。"
    c1"不热啊。"
    """……诶？"""
    c1"是你觉得我热。我有带水杯的，还有扇子。树上也很凉快。准备充分的话，坐一下午也不会有事。"
    """这样吗。"""
    c1"话说……你是人贩子吗？"
    c2"……什么？"
    c1"""
    我妈说的，只有人贩子才会请人喝东西，然后在里面下药，迷晕然后带走我。

    你是第一个请我喝东西的人，所以你很有可能是人贩子。

    只是你看起来太小了……感觉比我都还小。
    """
    """这都哪跟哪啊。"""
    c2"难道没有朋友请你喝过饮料吗？"
    c1"没有。"
    c1"我妈总是让我跟别人说不要吃太多垃圾食品，久而久之他们就不会带我一起吃东西了。"
    c2"好可怜。"
    c1"所以，你真没在里面下药？"
    c2"没。你看瓶盖都没有拧开。重点不是这个……"
    c2"我才15岁啊。你见过15岁的人贩子吗？"
    """虽然整天在街上装作成年人乱晃就是了。"""
    c1"说不定你没考上高中，所以随便加入了一个犯罪集团呢？"
    c1"仗着长得年轻哄骗小朋友替你做事的那种..."
    """那是什么混搭风格的故事情节啊？你书读太多把脑子给看坏了吧？"""
    c2"算了。一句话。你不喝就还给我。"
    c1"……不要。"
    c1"这好像是我第…嗯，第三次喝可乐。还是别人请我的。感觉很珍贵。"
    c2"你这人——"
    c2"算了，要我帮你拧开吗？"
    c1"不要。那样会很麻烦吧。汽水会冒出来弄脏手。"
    c2"没事，小心一点就不会了。把瓶子给我。"
    """（拧开瓶子）"""
    """可能因为刚刚的攀爬，气泡疯狂地从瓶口往外涌。所幸我手伸的远，没有打湿衣服。"""
    c1"我去拿纸。"
    """
    她很不情愿地把书放下，在旁边的挎包中摸索。

    接过饮料瓶的时候非常小心地用纸巾擦了一遍，又分了一张湿纸巾给我。
    """
    c1"谢谢。"
    c2"这哪用谢啊。应该的应该的。"
    """我哪里有过这么好的待遇，一时间有点受宠若惊。"""
    c2"你看，我不是人贩子吧。"
    """她抿起嘴，（居然）认真地想了想。"""
    c1"好吧，我暂时持保留意见。"
    """危机总算解除——虽然并不知道究竟算不算解除，但好在她并不太讨厌这样的对话。"""
    c2"对了..."
    c2"这不是聊得好好的吗。昨天，你为什么要推我下去啊？"

    """
    沉默。

    超级沉默。

    只有蝉鸣声的沉默。

    气氛一下子变得凝重起来。
    """
    c1"……你又不会受伤。"
    """她说得很小声。"""
    c2"""
    我不是在问结果啦，我是在问起因。

    再怎么说都不能随随便便就推人下去啊。

    这么高的树，我是运气好没事，但是其他人的话可能会崴到脚，运气差的说不定还会骨折。
    """
    c1"……哦。"
    c1"那你今天也想这么下去吗？"
    c2"""
    唉，你怎么也跟我家里人一样喜欢用威胁别人的方式岔开话题。
    
    在家里就暂且不提，怎么到了外面还来。
    """
    c1"哦。"
    c2"哦什么哦！你先说，我哪里做错了，让你想弄断我的腿？"
    c1" ……你又没做错。"
    c2"所以你就是无缘无故想弄断我的腿？"
    c1"……"
    c1"也不是。"
    c2"那总得有个理由吧！"
    c1"嗯……行吧。"
    c1"你真的要听？会很吓人哦。"
    c2"真的。"
    c1"你确定？"
    c2"确——定——"
    c1"嗯——嗯——"
    "她一拍大腿。"
    c1"这么说好了！"
    c1"……你问的那个问题，我没有办法回答。"
    c2"哪个？"
    c1"什么哪个？就你昨天问的那个啊！最后那个！"
    c2"你先等等，让我想一想。"
    """昨天问的问题……最后一个问题……"""
    c2"难不成是“你喜不喜欢莎士比亚”？"
    c1"不对，是“你喜欢那个英国老头吗”。"
    c2"那不是一回事吗？"
    c1"不是！！！"
    c1"……好吧，是一回事。"
    c1"就是那个。我回答不了。"
    c2"因为不知道喜不喜欢？"
    c1"""
    嗯。我还没把这本书看完，所以做不了决定。

    而且哪怕把这本书看完，还有其它的书。

    如果不看完一个作家所有的书，就没有办法确定喜不喜欢这个作家，所以我没有喜欢的作家。
    """
    c2"原来是觉得随便下判断有失偏颇？"
    c1"""
    嗯，而且一本书也会出现“前期很好看，但是后期一塌糊涂”的情况。

    人也是一样。如果是作家的话，可能至多只能确定“能不能读完全本”“会不会看下一本”。

    虽然我有时候也会管这个叫“喜欢”，但是这个喜欢和你问的，对作者本人的喜欢，不是一个东西。
    """
    c2"听起来好复杂，"
    c2"但感觉你说得还挺有道理的。"
    c2"但是，如果是这样的话，直接告诉我“我不知道”不就好了？"
    c1"不好。"
    """啊？"""
    """她气鼓鼓地看向我。"""
    c1"一般来说，这会有两种可能。"
    c1"一种人会说，“怎么会有人不知道自己喜不喜欢呢？”，扭着我要一个说法。"
    c1"另一种人会说，“那你觉得什么是喜欢呢？你有喜欢什么别的东西吗？”"
    c1"无论怎么样都很烦。"
    c2"我懂了。所以我就活该摔断腿？"
    c1"嗯嗯。"
    """她点点头。"""
    c2"真的啊？"
    c1"真的。谢谢你的理解。"
    """哇。处处透露着问题却完全无法反驳的感觉。"""
    c1"但是妈妈也告诉我，喜欢问东问西并不是他们的错，所以他们不能得到实质性的惩罚。"
    c1"也就是说，无论怎样你都不会摔断腿的。"
    c2"这又是基于什么个原理？"
    c1"嗯……姑且告诉你好啦，可不要往外说哦。"
    c2"好。"
    c1"我不算是人哦。"
    c2"...啊？"
    c1"""
    就是字面意思，我不算完全的人。

    传统习俗中也有“童子命”的说法吧，说某一类人是下凡来历劫的，和普通人不一样，我也是差不多的情况。

    作为补偿，我可以掌握一定程度的异能。
    """
    """哇，穿越到灵异片场了耶。"""
    c2"哦，现在天这么热，你赶紧指挥个下雨来试试看。"
    c1"那个难度太高了做不到。我能做的只是在小范围内实现他人认知里的愿望哦，比如说……"
    c2"“从树上掉下去但不想受伤” ？"
    c1"答对啦。你真的有在听我说话诶。"
    c1"""
    当然这也有限制的，不可以是太执着的愿望。

    比如‘想要找不到的家门钥匙马上出现在我面前’，这个我就没办法了。
    """
    """与其说是异能，还不如说你是个隐藏的老好人吧……整天想办法解决别人的问题什么的。"""
    """不过，敢把我从这么高的树上推下来……上辈子还真是神仙也说不定。"""
    c1"所以你放心好啦，我有分寸的，至少你现在不会轻易受伤。"
    c2"也就是说，以后有可能会喽。"
    c1"嗯……有可能。"
    c1"如果哪天你很害怕摔着，或者我心情很差，事情很有可能就会失控。"
    c1"不过到目前为止我还挺喜欢你的，所以现在不会。"
    c2"......"
    c1"你话问完了吗？问完就可以走了。我要继续看书了。"
    c2"请问……我可以再坐一会吗？"
    c1"可以是可以啦……但是我也不会再理你了，因为今天的额度用完了。"
    c1"你要么就快点走，要么就待在这一句话也不说。"
    c2"好吧。"
    c2"那……再见？"
    c1"嗯。再见。"
    c1"诶对了，需要我把你送下去吗？这样比较快。"
    c2"...谢谢，我觉得梯子就很好。"
    c1"……好吧。我还以为别人都喜欢刺激呢。"
    c1"你想，虽然坐上去会尖叫，但大家还是会去坐云霄飞车什么的。"
    """完全不是啊神仙小姐！像您这样没有安全保障（物理）的游乐园是不可以营业的！"""

    scene pure_black with Dissolve(2.0)
    show pure_white with Dissolve(2.0)
    show scene_3 at truecenter with Dissolve(1.0)
    pause 0.5
    hide scene_3 with Dissolve(1.0)
    show scene_3_title at truecenter with Dissolve(1.0)
    pause 0.5
    hide scene_3_title with Dissolve(1.0)
    hide pure_white with Dissolve(2.0)


    ""
    show 0020

    ""
    show 0040

    ""
    show 0050

    """

    c2"抱歉，今天来晚了一点。"
    ""她仍旧坐在树上静静地看着我。"""
    c2"你生气了吗？"
    """她很疑惑地看了我一眼。"""
    c1"没有。"
    c2"那我可以上来吗？"
    c1"可以。"
    c2"抱歉，家里发生了一点事情。"
    """她若有所思地盯着我。""
    ""完蛋，不会真的生气了吧。"""
    c1"……你今天又有新的问题想问我？"
    """……这家伙居然是在烦恼这个？"""
    c1"……我不知道。别人都是有问题才来找我的。既然没有问题..."
    c1"那你肯定是想拐卖我！"
    c2"......"
    c1"哈哈哈哈哈哈哈哈——昨天你的饮料里面没有毒，真是谢谢你。所以今天你下定决心要拐卖我了吗？"
    c2"啊，实在是惭愧，今天我没有买饮料。"
    c1"......"
    c2"不过非要说问题的话，也不是没有。"
    c1"你快说。"
    c2"你脖子上挂的那个，是传呼机吗？就是出租车师傅用的那种。"
    """她取下挂在脖子上的那个硬铁块。"""
    """真的是传呼机。"""
    c2 "虽然我不知道这是不是你说的那个东西啦……这个是音量键，这个是开机键，然后按着这个键就能说话，特别像港片里面的警察！"
    c2"所以说为什么你会有这样的东西啊？！"
    c1"因为大家要靠这个叫我回家吃饭！"
    c2"你没有……其它的通讯工具？"
    c1"以前是有的。可是我出门从不看手机，妈妈就把那个给外婆了。"
    c2"......"
    c1"其实……还是有点伤心的，但是我也确实不用嘛。"
    c1"把手机挂在脖子上又太显眼了，很容易被人盯上。"
    c1"但是你看，这个就不会。"
    """"最适合你的其实是大功率的老年机吧。听起来外婆比你都先进。"""
    c1"虽然它音量很大，我不想注意都不行，但是看在它长得很酷的份上，我也可以勉为其难地接受。"
    c1"如果要买手机，肯定是要买一个喜欢到一定会带出门，并且随时会查看的那种吧，我想这个也一样。"
    c2"原来这居然是有选择的吗。我以为大家都是捡爸妈用剩的。"
    c1"嗯……"
    c1"等一等。你是不是在偷偷笑我？"
    c2"没有！绝对没有！我也认为带着传呼机出门是很酷的事情！我还从来没碰过呢！"
    c1"我也这么觉得。"
    c2"可以给我看看吗？"
    c1"......"
    c2"没关系，不可以就算了。"
    c1"......"
    c2"你在想什么？"
    c1"……"
    c1"外婆说……不能把这个随便给别人。"
    c2"为什么？"
    c1"......"
    c1"你先答应我，不要和别人说。也不要生气。"
    
    c2"嗯。"
    c1"真的？"
    """姑且顺着她的意思往下说好了..."""
    c2"真的。"
    c1"他们会嫉妒，会弄坏这个，然后就得重新买。重新买要花钱。你生气了吗？"
    """我倒觉得你幼稚得有些好笑……算了。"""
    c2"你的外婆说的不完全错，但也不完全对。我就不会嫉妒。"
    c1"为什么？"
    c2"因为当然是手机更方便啊！背着个大铁块到处乱跑，我想想就觉得麻烦。"
    c1"但是你也对它很感兴趣对不对？"
    c2"这完全不是一回事。传呼机对我来说是很新鲜，但是我拿它来干嘛？和你家人联系吗？"
    c1"说不定你想要窥探他人隐私呢？"
    c2"……我不是变态跟踪狂。但你要是这么觉得，我也没有办法。"
    c1" ……好吧。但是你之前还说带着传呼机出门很酷。"
    c2"我并不想也看起来很酷。"
    c1"为什么？"
    c2"你是真心在发问吗？"
    c1"你生气了。"
    c2"我没有。"
    c2"……没事，你继续说。"
    c1"""
    如果你觉得酷是好事，那么你也会试着往那个方向发展。

    人总是想成为“更好的自己”，对不对？

    但是你说“我并不想这样”，所以其实对你来讲，酷并不是一个优点。你也在骗我。
    """
    """糟了，客套话也被她听进去了。她看起来真的很难过。"""
    c2"对不起。"
    c1"？"
    c1"我没说你错了啊？"
    c2"看到别人伤心了就赶紧道歉，这算是常识吧？"
    c1"!"
    c2"虽然不知道是什么原因，但是伤害了别人的感情，也算是做错了事。并不是你说我错了我就错了，也不是你说我没错我就没错。"
    c2"对错这种东西，有的时候是靠自己衡量的。"
    c1"是这样吗？"
    c2"是的。这也可以算是我的生活小妙招吧。别人一有不高兴，只要赶紧道歉然后把责任揽到自己身上就可以了。"
    c1"那么……"
    c1"你知道错哪了吗？"
    c2"……嗯，让我想想该怎么说好了。"
    c1"（盯——）"
    c2"你不喜欢别人用一套不同的标准来衡量你吧。"
    c1"..."
    """真诚其实是非常珍贵的东西……要是这么说她恐怕会更加生气。"""
    c2"在“我并不想成为你这样的人”的基础上，“我觉得你很酷”对你来说就是一种敷衍……也是。本来就是敷衍。"
    c2"尽管如此，别人也只是出于善意，希望你感觉良好才这么说的。"
    c2"他们以为……不，是我以为这样你会开心，以为你在炫耀自己的与众不同。"
    c2"但是现在看来并不是这样。"
    c2"那么，说回到我。对我来说，酷并不是一件好事。"
    c2"我并不希望自己与众不同……或者说万众瞩目吧。我不认为我有承载它的能力，所以我确实觉得你很厉害。"
    c2"就像我觉得佩戴着传呼机的你很酷，并不意味着我也觉得我自己需要它。"
    c2"但这并不代表你的行为就不……"
    c2"……唔。总之这是纯粹的赞美！不是恭维！"
    c1"真的？"
    c2"真的真的。"
    c1"你先答应我不会弄坏我的东西。"
    c2"好，我答应你。"
    c1"伸出手。"
    """我老老实实地把手交出来。"""
    c1"拿好了。要是把它弄坏了，我今天就摔断你的腿。我说到做到。"
    """结果其实很好哄嘛……好沉！"""
    c2"等等。平常你就挂个这么沉的东西在脖子上？"
    c1"对啊。放包里我听不见呼叫，放到兜里会很容易掉出来，没发现就惨了。"
    c2"你腰上不是有根绳子吗？你把挂脖子上那根带子绑在上面，再把传呼机放到口袋里，就不会弄掉了。"
    c1"......"
    c1"我不会打结。"
    c2"你……"
    c1"不准说我蠢。"
    c1"自理能力差也不行。"
    c2" ……其实是个生活白痴吧？"
    c1"那不是一个意思吗？"
    c2"嗯，白痴小姐，转过来一下。"
    c1"不准！这么！叫我！"
    c2"好好好，你把头转过来嘛。我把鞋带散开，你跟着我系。"
    c1"诶？"
    c2"""
    虽然不是最常用的打结方式，但是这个应该对你来说比较好理解。

    先把带子交叉，然后将其中一根绕过另一根，穿过去，再交叉。你再把其中一根绳子卷成一个圈，套进交叉的部分，拉紧……

    是圈，你别全穿进去了。然后再把另一根绳子绕着它打一个相同的圈，就行了。
    """
    c1"嗯。"
    c1"但是说不定我会忘记的。"
    c2"那把结打死一点好了，洗衣服的时候就不会掉。"
    """我的话都还没说完，就眼睁睁地看见了她把结扯开了。"""
    c2"不是，我，你……你能告诉我你在干什么吗？"
    c1"你生气了？"
    c2"……我保证不对你发脾气，但我真的很需要一个解释。"
    c1"结总会散的。"
    c2"嗯。"
    c1"到了那时候我会恨你的，我不想这样。"
    c2"啊？"
    c1"我不知道什么时候你会不耐烦，但我希望在那之前学会这个。我知道我可能很蠢，教我对别人的时间是一种浪费……"
    c1"对不起。对不起。对不起对不起对……"
    """完蛋。"""
    """我最不想遇见女人在我面前哭。"""
    c2"你先、给我、打住——！"
    c1"——唔——"
    """
    哇哦，居然听进去了。

    她用嘴咬住了食指，硬生生停住了抽泣。因为刹车刹得太快，还是噎了两下。
    """
    c1"......"
    c2"我其实觉得你的学习能力很强，真的。一点都不笨。"
    c1"?"
    c2"我刚刚教会你怎么随时随地道歉，你马上就用上了。"
    """妈呀，她的眼泪又要掉下来了。"""
    c2"裙子上的结又不是鞋带，开了其实也无所谓。你看，你脖子上挂个大铁块挂了这么久，不也过来了吗？哪有这么严重。"
    c1"但你生气了。"
    c2"嗯。但我还什么都没说呢，你就一声不吭地开始哭起来了。"
    "她低低地应了一声。"
    c2"还有，你知道什么是恨吗？"
    c1"知道。"
    c2"那你告诉我什么是恨。"
    c1"......"
    c1"好吧，我不知道..."
    """我恨不得给她脑袋上一个暴栗，又自觉太过亲密，只好把伸出的手又悄悄收了回去。"""
    c2"所以说，不会的词语就不要乱用！"
    c1"......知道了。"
    c2"你还要再试一次吗？.....打结。"
    c1"......"
    c2"如果不想的话，我下次来的时候我们再一起弄。"
    c1"要。但是你先把手伸出来。……右手。"
    """我只好乖乖地听她的话。"""
    """她手上变出了个小瓶子，对着我右手的虎口就是一喷。"""
    c2"啊——"
    c2"你就是这么对我恩将仇报的吗？！我险些把手甩出残影。"
    """是碘伏。"""
    c1"把手拿过来。"
    """我低头看着她，被她巧妙地错开视线。"""
    c1"拿过来。"
    """我一咬牙，还是从了。"""
    """没想到接下来居然只是用棉签抹匀四处乱跑的液体，顺带把我伤口上的脏东西都清理干净。"""
    c1"你刚刚的系鞋带的动作很别扭，应该还是疼的吧，为什么不包扎？"
    """外婆家里没找到创口贴，钱又不够了嘛……"""
    c2"我看血都止住了，过两天就好了，没那个必要。"
    c1"这么大的豁口，只要动一动大拇指都会疼吧。"
    c2"我懒得，行了吧。这不有你吗？"
    c1"我不会一直都在的。"
    c2"我不管。现在能享受到我就已经很满足了。"
    c1"嗯？"
    c2"我说谢谢，你是除了我幼儿园的老师以外第一个这么给我处理的人。"
    c1"嗯——其实我还是有一点照顾人的天赋吧？"
    c2"我想应该是有的。"
    c1"嘿嘿。"
    """果然，把伤口粘起来以后，打结还是利索多了。"""
    """本来以为今天终于可以圆满结束，直到她冷不丁问到——"""
    c1"喂，你是被什么划到的？"
    c2"碎瓷片。"
    """我头也不抬地说。"""
    c1"是谁一不小心打碎了碗吗？下次收拾的时候要小心点啊。"
    """我手上的动作一顿。"""
    c1"你看，我打完了，居然比你还快——"
    c1"嗯？"
    c2"没事。我看看。打得很好。虽然不是传统绑法，不过以后也可以用了。"
    c1"谢谢！我今天很开心，你下次还可以来！"
    c1"如果你没有准备问题的话，我可以给你带书来看。你喜欢什么？"
    c2"......那种被老师批的一无是处的闲书，像你这种整天在名著的海洋里遨游的人显然是没有吧。"
    c1"有的哦。你要看我给你带。"
    c2"真的假的。"
    c1"当然，我可是什么都看的。"
    c2"那你随便带两本吧，反正我都没看过。"
    c1"好！"
    c1"那，一定还要来哦！"
    """完全从十几分钟前的悲伤氛围挣脱了出来啊，真是善变的家伙。"""
    """想着这样不着边际的事情，我摸索着下了树。"""

    scene pure_black with Dissolve(2.0)
    show pure_white with Dissolve(2.0)
    show end at truecenter with Dissolve(1.0)
    pause 0.5
    hide end with Dissolve(1.0)
    hide pure_white with Dissolve(2.0)
    
    return
