# AI-Coder

[![Join the chat at https://gitter.im/AI-Coder/community](https://badges.gitter.im/AI-Coder/community.svg)](https://gitter.im/AI-Coder/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

AI-Coder is a PyCharm plugin that implements code words, code sentences, and code block recommendations through deep learning, and uses C/S to obtain recommendation results.

<a href="README_zh.md">中文版</a>

## Directory Structure

project 

├─model 

│	├─model_1 

│	├─model_2 

│	└─model_3 	

├─dataset 

│	├─original 

│	├─preprocessed 

│	└─. . . code files

├─backend

├─plugin

└─doc 

## Git Commit Message Conventions

Format is as follows:

```bash
model / dataset / backend / plugin / doc ( - issue ) - body
```

There are two points of attention in body:

- use imperative, present tense: “change” not “changed” nor “changes”
- includes motivation for the change and contrasts with previous behavior

If the current commit is for an issue, you need to specify the issue and indicate which issue or issues are closed in the body section.

If the line is not enough, you can just execute `git commit`, and the text editor will pop up, allowing you to write multiple lines.

examples： 

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

If the commit reverts a previous commit, its header should begin with `revert:`, followed by the message and SHA of the reverted commit 

example:

```bash
git commit -m"revert: add 'graphiteWidth' option SHA:667ecc1654a317a13331b17617d973392f415f02."
```

## Deep Learning Development Environment

python 3.7.3

tensorflow 1.13.1

keras 2.2.4

## Backend

### 1. Preparation

Install flask
`pip install flask`

### 2. Run

Go to the backend folder and run serve.py.

Enter `localhost:9078/plugin_test?keyword=helloworld` in your browser and the browser returns as follows.

<img src="/doc/img/backend_helloworld.jpg" width="50%"/>

The backend gets the data in keyword and returns after processing. Subsequent we use the model to process the input, the reason is the same.

## Plugin

### 1. Preparation

- The IDE used to develop the plugin: IDEA 
- The version used in the test: IntelliJ IDEA 2019.1 x64
- The object to which the plugin applies: Pycharm 
- The version used in the test: JetBrains PyCharm Community Edition 2019.1.1 x64

**Attention**: Pycharm must have a community version installed! Otherwise it cannot be debugged.

### 2. Import and run of plugin projects

Open IDEA, File->open->the root directory of our project

Then you need to configure:

- Select the project root directory and right click in IDEA, Open module settings

<img src="/doc/img/plugin_step1.jpg" width="50%"/>

- Set the SDK of the project to the Pycharm community version installed on the machine, create a new SDK, and select the pycharm community root directory for the installation.

<img src="/doc/img/plugin_step2.jpg" width="50%"/>

<img src="/doc/img/plugin_step3.jpg" width="50%"/>

-  A Pycahrm window is launched when the project is run, with the effect of our plugin.

<img src="doc/img/plugin_example.jpg" width="50%"/>
