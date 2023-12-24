## Git教程

菜鸟教程：https://www.runoob.com/git/git-tutorial.html

尚硅谷：https://www.bilibili.com/video/BV1wm4y1z7Dg/?spm_id_from=333.337.search-card.all.click

黑马程序员：https://www.bilibili.com/video/BV1MU4y1Y7h5/?spm_id_from=333.337.search-card.all.click



##  Git 的安装流程及步骤

首先，进入 Git 的官网：git - -fast-version-control

![img](https://pic1.zhimg.com/80/v2-00d5d602b3189d9d68cc21c0d0d19c0c_720w.webp)

如上图所示，在 Git 的官网中点击Downloads，进入如下页面：

![img](https://pic1.zhimg.com/80/v2-f545a732ae782ed2161fc7ef4e1367f8_720w.webp)

如上图所示，选择对应的操作系统，以博主为例，点击Windows，进入如下页面：

![img](https://pic1.zhimg.com/80/v2-6de0b5d054aedd87dc635ef8c43fc154_720w.webp)

如上图所示，正常情况下，会自动弹出下载框，否则的话，手动点击红色箭头所示的 **click here to download manually** 亦可进入如下界面：

![img](https://pic3.zhimg.com/80/v2-d0d78a634600a8862402d7ce029bdf62_720w.webp)



如上图所示，直接点击 下载 即可，下载完成后，双击打开，进入如下界面：

![img](https://pic2.zhimg.com/80/v2-4db10d46c91241ef12a4f154b1b8a885_720w.webp)



如上图所示，这是 Git 的安装界面，点击Next，进入如下界面：

![img](https://pic4.zhimg.com/80/v2-96dd5d5cc3bb024b33893905b78762df_720w.webp)



如上图所示，选择 Git 的安装目录，默认安装到C盘的Program Files目录下，想换的话，点击Browse进入更换。在这里，我们选择将其安装到D盘的Program Files目录下，选择完成后，点击Next，进入如下界面：

![img](https://pic3.zhimg.com/80/v2-9844aa1bdc196ed98cff879fe3c9a756_720w.webp)



如上图所示，这里有一些可勾选的项，我们可以按自己的实际需求进行选择（后面同样如此），例如勾选Additional icons，将在 Git 安装完成后，在桌面创建一个图标，也就是打开 Git 的快捷方式。在这一步，建议大家选择默认即可，例如默认勾选的Windows Explorer integration，就可以让我们在点击鼠标右键的时候，快速选择打开Git GUI或者 Git Bash。选择完成后，点击Next，进入如下界面：

![img](https://pic1.zhimg.com/80/v2-f9defb43b351d034cd2063e8dbe6219c_720w.webp)

如上图所示，选择 开始菜单文件夹，默认即可，点击Next，进入如下界面：

![img](https://pic1.zhimg.com/80/v2-63b85e815eb8b48424c3a7aa387375ec_720w.webp)

标注 1：仅使用 Git Bash 进行操作；

标注 2：在选择使用 Git Bash 进行操作的同时，也可以使用 Windows 命令行操作，建议选择此项；

标注 3：在选择使用 Git 的同时，也把 Unix 工具加入到了我们的配置之中，而且此操作会覆盖 Windows 的一些工具，强烈不建议选择此项。

如上图所示，我们选择 标注2 所示的Use Git from the Windows Command Prompt，点击Next，进入如下界面：

![img](https://pic4.zhimg.com/80/v2-62ea0015dc10c4e78e5f7ba69bae7487_720w.webp)

如上图所示，选择 HTTPS 传输后台，默认即可，点击Next，进入如下界面：

![img](https://pic3.zhimg.com/80/v2-35358c89c7f06aa27d8268be85de87d6_720w.webp)

如上图所示，配置行结束标记，默认即可，点击Next，进入如下界面：

![img](https://pic2.zhimg.com/80/v2-6a8a65389d2dfcdf9d6547563c523aed_720w.webp)

如上图所示，配置 Git Bash 的终端模拟器，默认即可，点击Next，进入如下界面：

![img](https://pic1.zhimg.com/80/v2-0ae4232597443003d5dcf0347f864280_720w.webp)

如上图所示，配置补充功能，默认即可，点击Next，进入如下界面：



![img](https://pic1.zhimg.com/80/v2-9e9dc9f37cfe25acd9577069ec156c50_720w.webp)

如上图所示，展示了 Git 安装中的界面，安装完成后，弹出如下窗口：

![img](https://pic3.zhimg.com/80/v2-2627b078897d946c3a40bdb42bb97b5a_720w.webp)



如上图所示，这表示 Git 已经安装完成了，至于图中的两个选择，则分别表示 打开 Git Bash 和 浏览 Git 版本信息，可以都选，也可以都不选，在这里，我们选择Launch Git Bash，进入如下界面：

![img](https://pic3.zhimg.com/80/v2-bfc4ff7316d0881f4a5ccfe9c326cf16_720w.webp)



如上图所示，我们打开了 Git Bash，输入git命令，将显示如下结果：

![img](https://pic2.zhimg.com/80/v2-aa7c81c70554d4aba11e56baddb80fa9_720w.webp)

如上图所示，Git 已经准备就绪啦，接下来就是你的 show time 啦！

## **Git 初体验及其常用命令介绍**

接下来介绍 Git 的命令操作，包含 init、add 等，在 Git 中，所有的命令都是以`git`开头，例如，`git init`其作用就是初始一个 Git 仓库。

为了方便演示，我们先在`D`盘的`CoderLife`目录下创建一个名为`demo`的子目录，并在其中新建一个名为`hit.txt`的文件，接下来我们的 Git 操作都是基于此目录和文件的。

![img](https://pic2.zhimg.com/80/v2-30263746fb2b0bc3f37b560c2d3df05d_720w.webp)

此外，在这里还要强调一点，那就是：在我们进行任何的git操作之前，我们都得先切换到 Git 的仓库目录。

换言之，我们得到先进入到（我们定义的）Git 仓库的最顶层文件目录下，然后从此目录中进入 Git Bash，这样之后的操作才能顺利进行。

如果是 Linux 操作系统，则可以直接cd到仓库目录。

以博主为例，选择demo目录作为 Git 仓库，然后进入demo目录之中，点击鼠标右键，再选择Git Bash Here，即可打开 Git Bash 的命令行窗口。

![img](https://pic1.zhimg.com/80/v2-ff4b6b4436077764af5ce83ee41f76dc_720w.webp)

如上图所示，Git 会自动定位到进入的位置，如我们选择的demo目录，这也是为什么我们需要先进入到 Git 仓库的最顶层目录下，然后再打开 Git Bash 的原因。下面，我们结合 Git 的常用命令演示一下 Git 的相关操作。

**第 1 个命令：git status**

在命令行窗口的光标处，输入git status命令，查看仓库的状态：

![img](https://pic1.zhimg.com/80/v2-41af87497f490ee0e93147921a3dfa4c_720w.webp)

如上图所示，结果显示demo不是一个 Git 仓库，这是很正常的反应，因为我们还没有在计算机中声明demo为 Git 仓库，之前说demo是 Git 仓库只是我们口头上的说的，计算机当然不会认可。

**第 2 个命令：git init**

在命令行窗口的光标处，输入git init命令，初始化 Git 仓库：

![img](https://pic3.zhimg.com/80/v2-2d758c4a4090bce9fb8d4d0447f88546_720w.webp)

如上图所示，结果显示已经初始化demo为一个空的 Git 仓库啦！在这里大家可以会有些疑问，因为我们在建立demo目录的同时也在里面新建了一个名为hit.txt的文件，怎么初始化仓库之后，demo目录就变成空的了呢？这个问题稍后解惑，我们重新输入git status命令检查一下仓库的状态：

![img](https://pic1.zhimg.com/80/v2-0215d2df12ba1ceb300c4fe7f512b890_720w.webp)

如上图所示，在我们初始化仓库之后，demo目录已经成为一个 Git 仓库了，并且默认进入 Git 仓库的master分支，即主分支。在这里，我们需要注意的是Untracked fies提示，它表示demo仓库中有文件没有被追踪，并提示了具体没有被追踪的文件为hit.txt，还提示了我们可以使用git add命令操作这个文件，简直不要太好。

**第 3 个命令：git add**

在命令行窗口的光标处，输入git add hit.txt命令，将hit.txt文件添加到 Git 仓库：

![img](https://pic3.zhimg.com/80/v2-6932af42aa149c735cd429ae5d8b350a_720w.webp)

如上图所示，如果没有报错，就说明命令已经执行啦！接下来，输入git status命令查看仓库状态：

![img](https://pic2.zhimg.com/80/v2-7658f1c05af7c4dfd277d85889026275_720w.webp)

如上图所示，已经显示Initial commit初始化提交了，同时已经没有Untracked files提示了，这说明文件hit.txt已经被添加到 Git 仓库了，而在我们没有进行git add操作之前，文件hit.txt并不被 Git 仓库认可，因此才会出现提示初始化仓库为空的现象。在这里，需要声明一点，那就是：git add命令并没有把文件提交到 Git 仓库，而是把文件添加到了「临时缓冲区」，这个命令有效防止了我们错误提交的可能性。

**第 4 个命令：git commit**

在命令行窗口的光标处，输入git commit -m "text commit"命令，将hit.txt文件提交到 Git 仓库：

![img](https://pic2.zhimg.com/80/v2-7bae7e33584a12b55dbaf6268769afe1_720w.webp)



如上图所示，我们成功将文件hit.txt提交到了 Git 仓库，其中commit表示提交，-m表示提交信息，提交信息写在双引号""内。接下来，再输入git status命令查看仓库状态：

![img](https://pic3.zhimg.com/80/v2-341e2394a657effef0c38f445bbe9bb6_720w.webp)

如上图所示，结果显示nothing to commit, working tree clean，这表示已经没有内容可以提交了，即全部内容已经提交完毕。

**第 5 个命令：git log**

在命令行窗口的光标处，输入git log"命令，打印 Git 仓库提交日志：

![img](https://pic3.zhimg.com/80/v2-365628061daef5e1b857f4337990981e_720w.webp)

如上图所示，显示了我们的提交记录，提交记录的内容包括Author提交作者、Date提交日期和提交信息。

通过以上的操作，我们会发现一个现象，那就是：在每个git操作之后，我们基本都会输入git status命令，查看仓库状态。

这也从侧面说明了git status命令使用的频率之高，也建议大家在操作 Git 仓库的时候多使用git status命令，这能帮助我们实时了解仓库的状态，显然非常有用。

**第 6 个命令：git branch**

在命令行窗口的光标处，输入git branch命令，查看 Git 仓库的分支情况：

![img](https://pic4.zhimg.com/80/v2-229c8f677bea969708a39a4c853ba98f_720w.webp)

如上图所示，显示了仓库demo中的分支情况，现在仅有一个master分支，其中master分支前的*号表示“当前所在的分支”，例如* master就意味着我们所在的位置为demo仓库的主分支。输入命令git branch a，再输入命令git branch，结果如下图所示：

![img](https://pic2.zhimg.com/80/v2-ce8506d523068e526e5b9164846f18f5_720w.webp)

如上图所示，我们创建了一个名为a的分支，并且当前的位置仍然为主分支。

**第 7 个命令：git checkout**

在命令行窗口的光标处，输入git checkout a命令，切换到a分支：

![img](https://pic2.zhimg.com/80/v2-ce8506d523068e526e5b9164846f18f5_720w.webp)

如上图所示，我们已经切换到a分支啦！也可以通过命令git branch查看分支情况：

![img](https://pic3.zhimg.com/80/v2-3b28d0015bd823222db84211c034741e_720w.webp)

在这里，我们还有一个更简单的方法来查看当前的分支，即通过观察上图中用红色框圈起来的部分。此外，我们也可以在创建分支的同时，直接切换到新分支，命令为git checkout -b，例如输入git checkout -b b命令：

![img](https://pic2.zhimg.com/80/v2-bd7b115a3f411746658bf44eb78b00f9_720w.webp)

如上图所示，我们在a分支下创建b分支（b为a的分支），并直接切换到b分支。

**第 8 个命令：git merge**

切换到master分支，然后输入git merge a命令，将a分支合并到master分支：

![img](https://pic2.zhimg.com/80/v2-807514785bdbb725053f4e30458bf5f5_720w.webp)

如上图所示，我们已经将a分支合并到主分支啦！此外，在这里需要注意一点，那就是：在合并分支的时候，要考虑到两个分支是否有冲突，如果有冲突，则不能直接合并，需要先解决冲突；反之，则可以直接合并。



**第 9 个命令：git branch -d & git branch -D**

在命令行窗口的光标处，输入git branch -d a命令，删除a分支：

![img](https://pic4.zhimg.com/80/v2-e22b97be855bf2c358db3c158d9cdc3f_720w.webp)

如上图所示，我们已经将分支a删除啦！不过有的时候，通过git branch -d命令可以出现删除不了现象，例如分支a的代码没有合并到主分支等，这时如果我们一定要删除该分支，那么我们可以通过命令git branch -D进行强制删除。

**第 10 个命令：git tag**

在命令行窗口的光标处，输入git tag v1.0命令，为当前分支添加标签：

![img](https://pic1.zhimg.com/80/v2-341de31e1046fe7dbd0f7d5d823a198c_720w.webp)

如上图所示，我们为当前所在的a分支添加了一个v1.0标签。通过命令git tag即可查看标签记录：

![img](https://pic4.zhimg.com/80/v2-7f4bbacebd1903677fb9e3235edbf36f_720w.webp)

如上图所示，显示了我们添加标签的记录。通过命令git checkout v1.0即可切换到该标签下的代码状态：

![img](https://pic1.zhimg.com/80/v2-36840bbe7c7f25a4afd62580348a1550_720w.webp)

如上图所示，我们已经成功切换到a分支的v1.0标签啦！