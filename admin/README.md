# Hello-CTF 站点管理面板

Flask 后端与原生 HTML/JS 前端，用于管理首页内容、文档、工具页数据和本地预览/部署。

## 安装与首次运行

项目依赖安装在仓库根目录的 `.venv` 中：

```bash
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
```

创建 `admin/config.json`，至少设置管理密码：

```json
{
  "admin_password": "请替换为强密码",
  "port": 9000
}
```

也可以通过 `ADMIN_PASSWORD` 环境变量设置密码，然后运行：

```bash
python admin/app.py
```

面板监听 `0.0.0.0:9000`，内网访问地址为 `http://<本机IP>:9000`。部署和预览任务会优先使用 `.venv` 中的 Python 与 MkDocs。

## 功能

- **首页内容**：编辑 `docs/index_content.json` 中的公告、项目推荐和导航卡片。
- **工具页**：管理 `docs/sidebar/tools_data.json`，支持按标签分组。
- **文档编辑**：浏览并编辑 `docs/` 下的 Markdown 文件，支持预览和新建。
- **部署与预览**：构建 MkDocs 站点、部署当前配置的 Git 远程仓库，或启动本地预览。
- **仓库同步**：查看 Git 状态并执行拉取、推送和中止变基操作。

面板的 Git 同步和部署会使用本地仓库配置的远程地址；当前仓库未配置远程时，这些推送操作不可用。
