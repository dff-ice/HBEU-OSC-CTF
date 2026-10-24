# HBEU-OSC 网络安全学习仓库

本仓库用于整理和维护网络安全方向的学习资料与实践内容，面向湖北工程学院开放原子社团（HBEU-OSC）的成员及其他网络安全学习者。内容以 CTF 入门和常见安全技术为主，帮助读者循序了解安全方向、搭建练习环境并通过动手实践巩固知识。

HBEU-OSC 是湖北工程学院的校园开源社团，倡导开放、协作、共享与贡献，致力于推广开源文化、开展技术交流并参与开源项目。社团介绍见 [HBEU-OSC GitHub 组织主页](https://github.com/HBEU-OSC/)。

## 仓库内容

- `docs/`：CTF 与网络安全学习文档，涵盖 MISC、Web、Crypto、Reverse、Pwn、AWD、AI 和区块链安全等方向，并包含环境配置、练习指引及工具导航。
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

浏览器访问 [http://127.0.0.1:8000](http://127.0.0.1:8000)。也可以使用 Docker Compose：

```bash
docker compose up --build
```

## 参与维护

欢迎 HBEU-OSC 社团成员和网络安全学习者补充资料、修正文档或改进工具。新增或改写内容时，请标明必要来源，并检查相关许可证与授权要求。
