# HTMX 中文示例库 | 快速上手 HTMX 的实战代码集合

欢迎来到 HTMX 中文示例库！这是一个专注于 HTMX 技术的中文示例代码库，旨在帮助开发者快速掌握 HTMX 的核心功能，并通过丰富的实战示例提升开发效率。

你可以在 [htmx中文网](https://gethtmx.com "htmx中文网") 查阅 HTMX 的中文文档。

## 项目亮点
🚀 从入门到进阶：涵盖 HTMX 的基础用法和高级技巧，适合初学者和资深开发者。

🌍 中文友好：所有示例和文档均以中文编写，方便中文开发者学习和使用。

💡 实战驱动：提供真实场景的示例代码，如动态表单、无刷新加载、实时搜索等。

🛠️ 即拿即用：每个示例都附带详细说明和代码片段，可直接集成到你的项目中。

## 示例内容

| 内容 | GitHub仓库 | 图文说明 |
| :--- | :--- | :--- |
| htmx实现用户登录：完整的动态交互 | [GitHub仓库](https://github.com/hhuayuan/htmx-chinese-examples/tree/main/01_login) | [图文教程](https://gethtmx.com/articles/htmx-flask-user-login) |
| htmx + 原生 CSS 实现 HTML 模态弹出窗口 | [GitHub仓库](https://github.com/hhuayuan/htmx-chinese-examples/tree/main/02_popup) | [图文教程](https://gethtmx.com/articles/htmx-pure-css-modal-popup) |
| HTMX 实现用户注册时邮箱地址实时查询可用性 | [GitHub仓库](https://github.com/hhuayuan/htmx-chinese-examples/tree/main/03_check_email) | [图文教程](https://gethtmx.com/articles/htmx-register-email-keyup-changed) |
| HTMX 实现数据加载时加载中动画 | [GitHub仓库](https://github.com/hhuayuan/htmx-chinese-examples/tree/main/04_loading_indicator) | [图文教程](https://gethtmx.com/articles/htmx-indicator-loading-request) |
| HTMX OOB | [GitHub仓库](https://github.com/hhuayuan/htmx-chinese-examples/tree/main/05_oob) | [图文教程](https://gethtmx.com/articles/htmx-out-of-band-oob-flask)) |

## 适合人群

- 前端开发者

- 全栈开发者

- 对 HTMX 感兴趣的技术爱好者

## 为什么选择 HTMX？
HTMX 是一个轻量级的 JavaScript 库，通过扩展 HTML 语法实现动态交互，无需编写复杂的 JavaScript 代码。它可以帮助你快速构建现代化的 Web 应用，同时保持代码简洁和可维护性。

## 立即开始

1. 克隆本仓库：

```bash
git clone https://github.com/hhuayuan/htmx-chinese-examples.git
```

2. 查看示例代码和 [文档](https://gethtmx.com)，快速上手 HTMX！

3. 如果你觉得这个项目有帮助，别忘了点个 ⭐ 支持我们！


## 示例代码片段
```html
<!-- 动态表单提交示例 -->
<form hx-post="/submit" hx-target="#result">
    <input type="text" name="username" placeholder="请输入用户名">
    <button type="submit">提交</button>
</form>
<div id="result"></div>
```

## 贡献与支持
欢迎提交 Issue 和 PR，帮助我们完善这个项目！如果你有任何问题或建议，请通过 GitHub Issues 联系我们。

## 链接
[GitHub 仓库](https://github.com/hhuayuan/htmx-chinese-examples)

[HTMX 官方文档](https://htmx.org)

[HTMX 中文网](https://gethtmx.com)

[爬虫练习网站](https://spiderbuf.cn)
