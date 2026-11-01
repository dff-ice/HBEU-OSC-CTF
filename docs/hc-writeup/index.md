# 比赛 WP · 解题报告

比赛结束不是终点。把思路、踩坑和脚本整理下来，才真正变成自己的东西。

本栏目收录 HBEU-OSC 成员在各类 CTF / 网安竞赛中的解题报告（Writeup），也欢迎社团外的同学投稿。

## 快速入口

| 我想… | 去哪里 |
| --- | --- |
| 学习怎么写一篇合格的 WP | [写作教程](guide.md) |
| 浏览全部比赛 WP | [比赛 WP 列表](../sidebar/writeups.html) |
| 直接开始投稿 | 复制[投稿模板](template.md.txt)，见下方「投稿流程」 |
| 看现成示例 | [ISCC 2026 的 5 篇 WP](../sidebar/writeups.html) |

## 收录范围

- CTF 赛事（Jeopardy / AWD / 混战）的赛后复盘；
- 校内赛、新生赛、招新赛的题目解析；
- 网安相关竞赛（靶场、渗透、取证、AI 安全等）的实践记录。

不收录：未到公开时间的赛题内容、未经授权的真实目标渗透记录、他人隐私信息。

## 写作要求（摘要）

- **以"能复现"为目标**：环境、命令、脚本、结果缺一不可；
- **结构对齐模板**：题目信息 → 解题思路 → 分析与复现 → 核心代码 → 结果验证 → 复盘；
- **脱敏**：真实 Flag、令牌、账号、公网地址一律去掉；
- **合规**：遵守比赛规则与仓库许可证（代码 GPLv3 / 文档 CC BY-SA 4.0）。

完整规范、字段说明与审核清单见[写作教程](guide.md)。

## 投稿流程

1. 复制[投稿模板](template.md.txt)，保存为 `.md`；
2. 在 `docs/hc-writeup/<年份>/<比赛名>/` 下新建文件，例如
   `docs/hc-writeup/2026/ISCC2026/ez-sql.md`，图片和附件放同级 `assets/`；
3. 填写好 front matter（`type: writeup` 必填）；
4. 本地运行 `python -m mkdocs serve` 预览，确认页面和链接正常；
5. 发起 Pull Request，管理员按[审核清单](guide.md#review-checklist)检查后合并，站点自动部署。

!!! note "关于列表"
    构建时 `hooks/generate_writeups.py` 会扫描所有带 `type: writeup` 的页面并生成列表数据。
    只要 front matter 正确，文章就会自动出现在[比赛 WP 列表](../sidebar/writeups.html)里，不需要手动改导航。

!!! warning "发布前必读"
    比赛未允许公开前请不要发布；只对比赛授权的题目环境做复现；分享前移除令牌、口令和非公开地址。
    详细要求见写作教程的[脱敏与合规](guide.md#sanitize)一节。
