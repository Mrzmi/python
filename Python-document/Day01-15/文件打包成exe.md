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