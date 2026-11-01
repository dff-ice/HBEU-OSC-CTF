# HBEU-OSC 网络安全学习仓库

本仓库用于整理和维护网络安全方向的学习资料与实践内容，面向湖北工程学院开放原子社团（HBEU-OSC）的成员及其他网络安全学习者。内容以 CTF 入门和常见安全技术为主，帮助读者循序了解安全方向、搭建练习环境并通过动手实践巩固知识。

HBEU-OSC 是湖北工程学院的校园开源社团，倡导开放、协作、共享与贡献，致力于推广开源文化、开展技术交流并参与开源项目。社团介绍见 [HBEU-OSC GitHub 组织主页](https://github.com/HBEU-OSC/)。

## 仓库内容

- `docs/`：CTF 与网络安全学习文档，涵盖 MISC、Web、Crypto、Reverse、Pwn、AWD、AI 和区块链安全等方向，并包含环境配置、练习指引及工具导航。
- `docs/hc-writeup/`：比赛 WP 与投稿规范（见下方「比赛 WP 投稿」），含投稿模板与自动索引。
- `overrides/`：MkDocs Material 主题模板和站点页面覆写。
- `admin/`：用于编辑首页内容、文档和工具列表的本地管理面板。
- `mkdocs.yml`：站点构建配置。

## 与 Hello-CTF 的关系

本仓库是在 [ProbiusOfficial/Hello-CTF](https://github.com/ProbiusOfficial/Hello-CTF) 基础上进行的二次创作。当前仓库保留并整理了上游项目中的部分 CTF 教程、站点样式和管理工具，后续将按 HBEU-OSC 网安方向的需要继续维护和扩展。

本项目与 Hello-CTF 上游分别维护；本地 Git 仓库已移除指向上游的远程地址，不会自动同步上游。二次创作过程中保留原项目的许可证与来源信息，使用或分发相关内容时请同时遵守仓库内许可证及内容自身的授权说明。HBEU-OSC 与 Hello-CTF 上游项目之间的关系以各自公开信息为准。

## 本地预览

需要 Python 环境。安装依赖后启动 MkDocs：

```bash
python -m pip install -r requirements.txt
python -m mkdocs serve
```

本地预览和静态构建都通过 Python 运行 MkDocs：

```bash
# 启动本地预览
python -m mkdocs serve

# 构建静态站点到 site/ 目录
python -m mkdocs build
```

浏览器访问 [http://127.0.0.1:8000](http://127.0.0.1:8000) 查看预览。

## 比赛 WP 投稿

比赛结束后，欢迎把解题过程整理成 WP 投到站点「比赛 WP」栏目。要求如下。

**目录与命名**：`docs/hc-writeup/<年份>/<比赛名>/<题目>.md`，图片和附件放同级 `assets/`，文件名用英文小写加连字符（如 `ez-sql.md`）。

**Front matter**（列表页靠它收录）：

```yaml
---
title: "比赛名称 - 方向 - 题目名称"
type: writeup
date: 2026-01-01
authors: ["作者名"]
competition: "比赛名称"
category: "Web"
description: "一句话概括考点和思路"
comments: true
---
```

`type: writeup` 是收录开关，漏了不会出现在列表页；`date` 决定排序。

**正文结构**：题目信息 → 解题思路 → 分析与复现（命令和输出）→ 核心代码 → 结果验证 → 复盘与经验 → 参考资料。

**发布要求**：

- 以「别人能复现」为标准，环境、命令、脚本、结果写全；
- 删除真实 Flag、token、账号、公网地址等敏感信息；
- 遵守比赛公开规则，只对授权环境复现；
- 引用他人思路注明来源；代码 GPLv3、文档 CC BY-SA 4.0。

**投稿流程**：fork 仓库 → 新建分支 → 按规范添加文件 → 本地 `python -m mkdocs build` 自检 → 发起 Pull Request，审核合并后自动部署。模板见 [WP 投稿模板](docs/hc-writeup/template.md.txt)。

## 参与维护

欢迎 HBEU-OSC 社团成员和网络安全学习者补充资料、修正文档或改进工具。新增或改写内容时，请标明必要来源，并检查相关许可证与授权要求。
