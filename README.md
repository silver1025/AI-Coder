<a href="README_zh.md">中文版</a>

## Directory Structure

[![Join the chat at https://gitter.im/AI-Coder/community](https://badges.gitter.im/AI-Coder/community.svg)](https://gitter.im/AI-Coder/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

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

