**更换 Python 解释器**

如果你系统里有多个版本的python，你想更换解释器，请使用下面的方法：

在File->Setting->Projec: xxx 下找到 Project Interpreter。然后修改为你需要的 Python 解释器。注意这个地方一定要注意的是：在选择 Python 解释器的时候，一定要选择到 python.exe 这个文件，而不是 python 的安装文件夹。

**File--settings  设置文件编码**

![4.jpg](https://www.django.cn/media/upimg/4_20180829211506_484.jpg)

**File--settings  修改文件背景颜色**

![6.jpg](https://www.django.cn/media/upimg/6_20180829212144_757.jpg)

**让一个 tab 键代替 4 个空格键**

![7.jpg](https://www.django.cn/media/upimg/7_20180829212323_724.jpg)

**设置模板**

![9.jpg](https://www.django.cn/media/upimg/9_20180829214759_189.jpg)

其他操作https://www.cnblogs.com/djangocn/p/10227015.html

**把文件打包成exe**

首先我们需要安装 PyInstaller， 当然用pip命令安装喽，如下

```
pip install pyinstaller
```

只打包成exe可执行文件

```python3
pyinstaller file.py --noconsole
```

```text
pyinstaller -F -w file.py
```

-F 表示生成单个可执行文件 

-w 表示去掉控制台窗口，这在GUI界面时非常有用。不过如果是命令行程序的话那就把这个选项删除吧！

 -p 表示你自己自定义需要加载的类路径，一般情况下用不到 

-i 表示可执行文件的图标

```
pyinstaller byhy.py --workpath d:\pybuild  --distpath d:\pybuild\dist
```

注意：

参数 `--workpath` 指定了制作过程中临时文件的存放目录

参数 `--distpath` 指定了最终的可执行文件目录所在的父目录

上面的命令执行结束后，我们进入到 目录 `d:\pybuild\dist` 中，就会发现有一个目录叫byhy （和我们的入口文件byhy同名），该目录中包含了如下文件