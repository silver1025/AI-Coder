# AI-Coder

[![Join the chat at https://gitter.im/AI-Coder/community](https://badges.gitter.im/AI-Coder/community.svg)](https://gitter.im/AI-Coder/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

AI-Code 是一个通过深度学习实现代码词、代码句、代码块推荐的PyCharm插件，采用C/S的方式获取推荐结果。

<a href="README.md">English Version</a>

## 目录结构

project 项目目录

├─model 模型相关文件

│	├─model_1 第一组模型

│	├─model_2 第二组模型

│	└─model_3 第三组模型	

├─dataset 数据集相关文件

│	├─original 未作任何处理

│	├─preprocessed 预处理后

│	└─. . . 相关爬虫及预处理代码文件

├─backend 后端相关文件

├─plugin 插件相关文件

└─doc 文档

## git commit 简单规范

message 要求全英文，格式如下：

```bash
model / dataset / backend / plugin / doc ( - issue ) - body
```

body 部分有两个注意点：

- 使用第一人称现在时，比如使用`change`而不是`changed`或`changes`。

- 应该说明代码变动的动机，以及与以前行为的对比。

如果当前 commit 针对某个 issue，那么需要注明 issue ，并在 body 部分说明关闭了哪个或哪几个 issue。

如果一行不够，可以只执行`git commit`，就会跳出文本编辑器，让你写多行。

例： 

```bash
git commit -m"model - Try a new model"
```

```bash
git commit -m"model - Adjust model parameters to improve accuracy"
```

```bash
git commit -m"backend - Improve security and prevent cross-attacks"
```

```bash
git commit -m"plugin - issue - Close #123, #245, #992; Solve the space problem"
```

还有一种特殊情况，如果当前 commit 用于撤销以前的 commit，则必须以`revert:`开头，后面跟着被撤销 commit 的 message 以及被撤销 commit 的 SHA 标识符。

例：

```bash
git commit -m"revert: add 'graphiteWidth' option SHA:667ecc1654a317a13331b17617d973392f415f02."
```

## 深度学习开发环境

python 3.7.3

tensorflow 1.13.1

keras 2.2.4

## 后端

### 1. 准备

如果没有安装 flask，先安装 flask。anaconda 自带了 flask。
`pip install flask`

### 2. 运行

进入 backend 文件夹，运行 serve.py。

在浏览器中输入 localhost:9078/plugin_test?keyword=helloworld ，浏览器返回内容如下。

<img src="doc/img/backend_helloworld.jpg" width="50%"/>

后端获取 keyword 中的数据，处理之后返回。后续我们使用模型处理输入，道理是一样的。

## 插件

### 1. 准备

- 开发插件所用的编辑器——IDEA 测试时使用版本 IntelliJ IDEA 2019.1 x64

- 插件适用对象——Pycharm 测试时使用版本 JetBrains PyCharm Community Edition 2019.1.1 x64

注：Pycharm必须安装社区版！否则不能调试。

### 2. 插件项目的导入与运行

打开IDEA,File->open->我们项目的根目录

然后需要配置：

1) 在IDEA中选择项目根目录右键Open module settings

<img src="doc/img/plugin_step1.jpg" width="50%"/>

设置项目的SDK为本机安装的Pycharm社区版，新建一个SDK，路径选择为安装的pycharm社区版根目录

<img src="doc/img/plugin_step2.jpg" width="50%"/>

<img src="doc/img/plugin_step3.jpg" width="50%"/>

2) 运行项目时会启动一个Pycahrm 窗口，是带有我们这个插件效果的。

<img src="doc/img/plugin_example.jpg" width="50%"/>