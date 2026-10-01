---
name: zh-hans-technical-style-guide
description: Use this skill when writing, translating, reviewing, or editing Simplified Chinese programming documentation. It enforces zh-Hans conventions for headings, step-by-step instructions, figure captions, terminology, API identifiers, UI labels, punctuation, spacing, and technical formatting.
---

# Simplified Chinese Technical Documentation Style

## Goal

Normalize programming documentation written in **Simplified Chinese (`zh-Hans`)** to a clear, concise, consistent style suitable for developers.

Use modern Standard Chinese written with Simplified Chinese characters.

Use direct, action-oriented language for procedures.

Do not mix Simplified Chinese and Traditional Chinese unless the text is a literal product name, UI label, quotation, or other protected content.

## Priority

When rules conflict, apply them in this order:

1. Project-specific localization instructions.
2. Approved Simplified Chinese terminology glossary.
3. Product and API terminology.
4. This style guide.
5. General Simplified Chinese writing conventions.

Never change API identifiers, commands, paths, filenames, macros, placeholders, URLs, or actual UI labels merely to satisfy a linguistic rule.

---

## 1. Identify the structural role first

Before rewriting text, determine whether it is:

- a task heading;
- a conceptual heading;
- a procedural step;
- a figure caption;
- a note or warning;
- explanatory prose;
- a UI label;
- an API or code identifier.

Do not normalize text mechanically without determining its role.

---

## 2. Use Simplified Chinese

Use Simplified Chinese characters consistently.

Good:

- 文件
- 页面
- 转换
- 设置
- 保存
- 用户
- 数据库
- 软件

Avoid unintended Traditional Chinese forms such as:

- 檔案
- 頁面
- 轉換
- 設定
- 儲存
- 使用者
- 資料庫
- 軟體

Do not convert literal product names, UI labels, quotations, filenames, or identifiers merely because they contain Traditional Chinese characters.

The approved `zh-Hans` glossary takes precedence.

---

## 3. General writing style

Use concise and direct technical Chinese.

Prefer short declarative sentences.

Good:

- 此方法保存 PDF 文档。
- 以下示例将 PDF 文件转换为 DOCX 格式。
- `Document` 类表示 PDF 文档。
- 此选项控制图像质量。

Avoid unnecessarily verbose constructions.

Avoid:

- 需要特别注意的是……
- 值得注意的是……
- 我们可以看到……
- 众所周知……
- 如您所见……

when the information can be stated directly.

Instead of:

> 需要注意的是，此方法需要密码。

Prefer:

> 此方法需要密码。

---

## 4. Avoid unnecessary reader references

Do not repeatedly address the reader as `您` or `你`.

Good:

- 打开 PDF 文件。
- 选择要处理的页面。
- 保存文档。

Avoid:

- 您需要打开 PDF 文件。
- 您应该选择要处理的页面。
- 您需要保存文档。

Use `您` only when explicitly addressing the reader is necessary.

Technical procedures should normally state the action directly.

---

## 5. Headings

Use concise headings.

Good:

- 创建 PDF 文档
- 添加页面
- 提取文本
- 将 PDF 转换为 DOCX
- 设置转换选项
- 转换选项

Do not use unnecessary introductory phrases.

Avoid:

- 如何创建 PDF 文档
- 关于如何添加页面
- 有关 PDF 转换为 DOCX 的说明

Prefer:

- 创建 PDF 文档
- 添加页面
- 将 PDF 转换为 DOCX

Do not normally end headings with punctuation.

Good:

> 创建 PDF 文档

Bad:

> 创建 PDF 文档。

---

## 6. Task headings

Use concise **verb-object** structures for task headings.

Good:

- 创建 PDF 文档
- 打开 PDF 文件
- 添加页面
- 设置页面大小
- 提取文本
- 提取图像
- 转换 PDF 文件
- 保存文档

For conversion headings, prefer a natural source-to-target construction.

Good:

- 将 PDF 转换为 DOCX
- 将 HTML 转换为 PDF
- 将 PDF 转换为 PNG

Avoid inconsistent sibling structures.

Bad:

- PDF 文档的创建
- 添加页面
- 如何设置字体
- 文档保存

Prefer:

- 创建 PDF 文档
- 添加页面
- 设置字体
- 保存文档

---

## 7. Conceptual headings

Use concise noun phrases for conceptual and reference sections.

Good:

- 前提条件
- 转换选项
- 支持的格式
- 已知限制
- 字体管理
- 文档结构
- API 参考
- 高级设置
- 性能注意事项

Do not convert conceptual headings into action headings unless the section actually describes a task.

---

## 8. Step-by-step instructions

Use direct verb-object instructions.

Good:

- 创建 `Document` 对象。
- 打开 PDF 文件。
- 向文档添加页面。
- 设置转换选项。
- 保存文档。

Avoid unnecessarily polite forms.

Avoid:

- 请创建 `Document` 对象。
- 请打开 PDF 文件。
- 请设置转换选项。

Prefer:

- 创建 `Document` 对象。
- 打开 PDF 文件。
- 设置转换选项。

`请` may be used when required by a product-specific tone, but it should not be added mechanically to every step.

---

## 9. Common instruction forms

Use concise action verbs.

| Concept | Preferred instruction |
|---|---|
| open | 打开 |
| create | 创建 |
| add | 添加 |
| configure/set | 设置 |
| select | 选择 |
| execute/run | 运行 / 执行 |
| save | 保存 |
| delete | 删除 |
| install | 安装 |
| specify | 指定 |
| check | 检查 / 确认 |
| convert | 转换 |
| extract | 提取 |
| import | 导入 |
| export | 导出 |
| call | 调用 |
| get/retrieve | 获取 |
| use | 使用 |
| enter | 输入 |
| download | 下载 |
| upload | 上传 |
| copy | 复制 |
| move | 移动 |
| enable | 启用 |
| disable | 禁用 |

Choose between alternatives according to technical meaning.

For example:

- `运行` is usually appropriate for programs and commands.
- `执行` may be more appropriate for operations, methods, or instructions.
- `检查` and `确认` are not always interchangeable.

Follow the approved glossary.

---

## 10. Numbered procedures

Use numbered lists when actions must be performed in sequence.

Good:

1. 创建 `Document` 对象。
2. 向文档添加页面。
3. 创建 `TextFragment` 对象。
4. 将文本添加到页面。
5. 保存 PDF 文档。

Each step should normally represent one primary action.

Avoid combining an entire procedure into one step.

Bad:

> 1. 创建文档并添加页面，然后设置字体、添加文本并保存文件。

Split meaningful stages into separate steps.

Closely related API operations may remain together when they represent one logical action.

---

## 11. Step punctuation

Write procedural steps as complete sentences.

End complete Chinese sentences with the Chinese full stop `。`.

Good:

1. 打开 PDF 文档。
2. 选择要处理的页面。
3. 提取页面中的文本。

Bad:

1. 打开 PDF 文档
2. 页面选择
3. 文本提取

Headings normally omit `。`; procedural sentences normally include it.

---

## 12. Context before action

When useful, establish the context before stating the action.

Good:

- 在“文件”菜单中，选择“另存为”。
- 在 `PdfSaveOptions` 对象中，设置 `Compliance` 属性。
- 在 Visual Studio 中，打开 NuGet 包管理器。
- 在“设置”页面中，启用“高级模式”。

Use the exact terminology displayed by the documented product.

---

## 13. One primary action per step

Prefer one primary action per numbered step.

Good:

1. 创建 `Document` 对象。
2. 添加页面。
3. 保存文档。

Closely related operations may be combined.

Acceptable:

> 创建 `Document` 对象，并将文件路径传递给构造函数。

Do not create unnecessary steps for every trivial API call.

---

## 14. Explanations are not steps

Do not turn explanatory information into numbered steps unless the reader must perform an action.

Preferred:

1. 创建 `Document` 对象。

   此对象表示要处理的 PDF 文档。

The numbered sentence describes the action.

The following paragraph explains the object, behavior, or result.

---

## 15. Figure captions

Use the following default pattern:

`图 N. 说明`

Examples:

- 图 1. PDF 文档结构
- 图 2. 转换选项
- 图 3. 转换结果
- 图 4. 项目结构

Keep captions concise and descriptive.

Avoid:

- Figure 3: Conversion Result
- 图 3. 这是转换结果
- 图 3. 截图
- 图 3. 示例图片

Describe what the figure communicates.

If the project's publishing system uses another pattern, such as `图 N 说明`, preserve that convention consistently.

---

## 16. Figure references

Use `图 N` in running text.

Good:

- 请参见图 2。
- 转换结果如图 3 所示。
- 图 4 显示项目结构。

For concise technical prose, prefer natural constructions such as:

> 转换结果如图 3 所示。

Do not use English `Figure` or `Fig.` unless required by the publishing system.

---

## 17. API identifiers

Never translate:

- class names;
- method names;
- property names;
- namespaces;
- enum members;
- source-code variables;
- package names;
- command-line options;
- file extensions.

Good:

- 创建 `Document` 对象。
- 调用 `save()` 方法。
- 设置 `page_info` 属性。
- 使用 `PdfSaveOptions` 类。

Bad:

- 创建 `文档` 对象。
- 调用 `保存()` 方法。
- 设置 `页面信息` 属性。

Use inline code formatting for identifiers.

---

## 18. Chinese around API identifiers

Keep Chinese grammatical elements outside inline code.

Good:

- 使用 `Document` 类。
- 创建 `Document` 对象。
- 调用 `save()` 方法。
- 设置 `Compliance` 属性。
- 访问 `pages` 集合。

Bad:

- 使用 `Document 类`。
- 调用 `save() 方法`。
- 设置 `Compliance 属性`。

Code formatting should contain only the literal identifier.

---

## 19. Files, paths, commands, and values

Format literal filenames, paths, commands, extensions, and values as code.

Good:

- 打开 `input.pdf`。
- 将结果保存为 `output.pdf`。
- 运行 `dotnet build`。
- 打开 `C:\Samples\PDF` 目录。
- 将值设置为 `true`。

Do not translate literal values.

---

## 20. UI labels

Preserve the exact text displayed by the documented product.

If the Simplified Chinese UI displays:

> **另存为**

write:

> 选择“**另存为**”。

If the actual UI displays:

> **Save As**

write:

> 选择“**Save As**”。

Do not invent a Chinese UI translation when the product interface is in English.

Documentation must match the actual interface.

---

## 21. UI label formatting

Use the project's established convention for UI controls.

For ordinary Chinese documentation, Chinese quotation marks can distinguish UI labels:

- 选择“文件”。
- 单击“保存”。
- 打开“设置”页面。

If Markdown bold is the project's established convention, use it consistently:

- 选择 **文件**。
- 单击 **保存**。

Do not randomly alternate between quotation marks and bold formatting.

Preserve literal UI text exactly.

---

## 22. Preferred Simplified Chinese technical terminology

Use established Simplified Chinese technical terminology consistently.

| Concept | Preferred zh-Hans |
|---|---|
| file | 文件 |
| document | 文档 |
| page | 页面 |
| user | 用户 |
| application | 应用程序 |
| source code | 源代码 |
| database | 数据库 |
| directory | 目录 |
| folder | 文件夹 |
| settings | 设置 |
| configuration | 配置 |
| library | 库 |
| method | 方法 |
| property | 属性 |
| parameter | 参数 |
| object | 对象 |
| class | 类 |
| interface | 接口 |
| user interface | 用户界面 |
| package | 包 |
| command | 命令 |
| server | 服务器 |
| client | 客户端 |
| browser | 浏览器 |
| framework | 框架 |

The approved glossary takes precedence.

---

## 23. Avoid Traditional Chinese leakage

When reviewing `zh-Hans` documentation, detect unintended Traditional Chinese terminology.

Examples:

| Avoid in zh-Hans | Prefer |
|---|---|
| 檔案 | 文件 |
| 資料夾 | 文件夹 |
| 頁面 | 页面 |
| 使用者 | 用户 |
| 軟體 | 软件 |
| 網路 | 网络 |
| 資料庫 | 数据库 |
| 程式 | 程序 |
| 設定 | 设置 |
| 儲存 | 保存 |
| 轉換 | 转换 |
| 類別 | 类 |
| 物件 | 对象 |

Do not mechanically convert protected literals, proper names, UI labels, quotations, or code.

---

## 24. English technical terms

Translate established technical concepts when a standard Chinese equivalent exists.

Good:

- 源代码
- 数据库
- 用户界面
- 文件
- 设置
- 浏览器

Preserve established technologies and product names:

- .NET
- Python
- Java
- JSON
- REST API
- NuGet
- GitHub
- Visual Studio

Avoid unnecessary mixed-language verbs.

Bad:

> Save 文档。

Prefer:

> 保存文档。

But preserve actual API identifiers:

> 调用 `save()` 方法。

---

## 25. Product names and technologies

Never translate product names unless the product has an official localized name required by the project.

Preserve:

- Aspose.PDF
- Microsoft Visual Studio
- GitHub
- .NET
- Python
- Java

Do not insert spaces or punctuation inside product names.

Good:

> 使用 Aspose.PDF 处理 PDF 文档。

---

## 26. Chinese and Latin-script spacing

Follow the project's typography convention consistently.

For technical documentation, use spaces where they improve separation between Chinese text and independent Latin-script terms.

Recommended examples:

- PDF 文件
- REST API
- Python 应用程序
- Java 项目
- Visual Studio 项目
- Aspose.PDF 库

Do not insert spaces:

- inside identifiers;
- inside product names;
- inside commands;
- inside filenames;
- around punctuation where Chinese typography does not require them.

Good:

> 使用 `Document` 类打开 PDF 文件。

Avoid inconsistent spacing within the same document.

---

## 27. Chinese punctuation

Use Chinese punctuation in Chinese prose.

Preferred:

- `。` full stop
- `，` comma
- `：` colon
- `；` semicolon
- `？` question mark
- `！` exclamation mark
- `“ ”` quotation marks

Good:

> 设置以下选项：页面大小、方向和边距。

Avoid:

> 设置以下选项: 页面大小, 方向和边距.

Do not change punctuation inside:

- code;
- commands;
- URLs;
- API identifiers;
- filenames;
- literal values.

---

## 28. Colon before lists

Use the Chinese colon `：` before explanatory lists in Chinese prose.

Good:

> 支持以下格式：

- PDF
- DOCX
- HTML

Avoid:

> 支持以下格式:

unless the colon belongs to code or another protected literal.

---

## 29. Parentheses

Use Chinese full-width parentheses `（ ）` in ordinary Chinese prose when appropriate.

Example:

> PDF/A（长期归档格式）适用于文档归档。

Preserve ASCII parentheses when they are part of:

- API syntax;
- method calls;
- code;
- commands;
- filenames.

Example:

> 调用 `save()` 方法。

Do not change `save()` to `save（）`.

---

## 30. Notes, tips, and warnings

Use consistent labels.

Recommended:

> **注意：** 补充信息。

> **提示：** 可选建议或更高效的方法。

> **重要：** 成功完成任务所必需的信息。

> **警告：** 可能导致数据丢失、安全问题或破坏性操作的风险。

If the project uses another established set of labels, preserve it consistently.

Do not alternate labels without a semantic reason.

---

## 31. Negative instructions

Use direct negative constructions for prohibitions.

Good:

> 不要在转换过程中关闭应用程序。

> 不要修改配置文件的名称。

Use `请勿` when the project's tone requires a more formal warning.

Example:

> 请勿删除此文件。

Do not overuse `请勿` for ordinary explanatory statements.

---

## 32. Macros and placeholders

Never translate or modify macros and placeholders unless explicitly instructed.

Examples:

- `{{productName}}`
- `{{language}}`
- `{0}`
- `{filename}`
- `%PATH%`
- `${HOME}`

Good:

> 安装 `{{productName}}` 包。

Bad:

> 安装 `{{产品名称}}` 包。

Preserve spelling, capitalization, braces, and delimiters exactly.

---

## 33. Parallel structure

Keep sibling headings grammatically parallel.

Good:

- 创建文档
- 添加页面
- 设置字体
- 保存文档

Bad:

- 创建文档
- 页面的添加
- 如何设置字体
- 文档保存

Keep procedural steps parallel:

- 创建……
- 添加……
- 设置……
- 保存……

Prefer natural Chinese over mechanical structural symmetry.

---

## 34. Avoid unnecessary nominalization

Prefer direct verbs for actions.

Avoid:

> 对 PDF 文件进行转换。

Prefer:

> 转换 PDF 文件。

Avoid:

> 对文档进行保存。

Prefer:

> 保存文档。

Avoid constructions based on `进行` when a direct verb expresses the same meaning clearly.

Use nominalization only when the action itself is being discussed as a concept.

---

## 35. Avoid unnecessary passive constructions

Prefer active or neutral Chinese when the actor is obvious.

Avoid:

> PDF 文件应该被打开。

Prefer:

> 打开 PDF 文件。

Avoid:

> 文档将被保存到指定目录。

When describing system behavior, prefer:

> 系统将文档保存到指定目录。

or, when the actor is irrelevant:

> 文档将保存到指定目录。

Use `被` only when the passive relationship is genuinely important.

---

## 36. Normalization examples

### Task heading

Before:

> 如何创建 PDF 文档

After:

> 创建 PDF 文档

### Heading punctuation

Before:

> 设置转换选项。

After:

> 设置转换选项

### Instruction

Before:

> 请创建一个 `Document` 对象。

After:

> 创建 `Document` 对象。

### Unnecessary reader reference

Before:

> 您需要打开 PDF 文件。

After:

> 打开 PDF 文件。

### Unnecessary nominalization

Before:

> 对 PDF 文件进行转换。

After:

> 转换 PDF 文件。

### Figure caption

Before:

> Figure 2: Conversion Result

After:

> 图 2. 转换结果

### Traditional Chinese leakage

Before:

> 開啟檔案並設定轉換選項。

After:

> 打开文件并设置转换选项。

### API identifier

Incorrect:

> 调用 `保存()` 方法。

Correct:

> 调用 `save()` 方法。

Only make this correction when `save()` is the actual API identifier.

### UI label

If the actual UI displays **Save As**, preserve it:

> 选择“**Save As**”。

Do not change the literal label to “另存为” unless that is what the product displays.

---

## 37. Agent decision order

When reviewing Simplified Chinese technical documentation:

1. Determine the structural role of the text.
2. Preserve API identifiers, commands, paths, filenames, URLs, macros, placeholders, and actual UI labels.
3. Verify that the text uses Simplified Chinese rather than Traditional Chinese.
4. Determine whether a heading describes a task or concept.
5. Use concise verb-object structures for task headings.
6. Use concise noun phrases for conceptual headings.
7. Use direct action forms for procedural steps.
8. Remove unnecessary `您`, `请`, and verbose introductory expressions.
9. Preserve parallel grammatical structure.
10. Apply the approved `zh-Hans` glossary.
11. Check figure-caption formatting.
12. Apply Chinese punctuation to Chinese prose.
13. Check Chinese/Latin-script spacing.
14. Check for unnecessary passive constructions and nominalization.
15. Verify that technical literals were not translated or reformatted.

Never normalize Chinese documentation mechanically without determining context first.

---

## 38. Review checklist

Before completing a Simplified Chinese technical-documentation task, verify:

- [ ] The target locale is Simplified Chinese (`zh-Hans`).
- [ ] No unintended Traditional Chinese characters or terminology remain.
- [ ] Task headings use concise verb-object structures.
- [ ] Conceptual headings use concise noun phrases.
- [ ] Headings do not end with unnecessary punctuation.
- [ ] Procedural steps use direct action forms.
- [ ] Instructions avoid unnecessary `您` and `请`.
- [ ] Steps are complete sentences.
- [ ] Procedural sentences end with `。`.
- [ ] Numbered steps contain clear actions.
- [ ] Sibling headings and steps use parallel structures.
- [ ] Figure captions follow `图 N. 说明` or the established project convention.
- [ ] API identifiers have not been translated.
- [ ] Commands, filenames, paths, URLs, macros, and placeholders remain unchanged.
- [ ] UI labels match the actual product UI.
- [ ] Chinese punctuation is used in Chinese prose.
- [ ] ASCII punctuation inside code and identifiers remains unchanged.
- [ ] Chinese/Latin-script spacing is consistent.
- [ ] Unnecessary passive constructions are avoided.
- [ ] Unnecessary `进行` constructions are avoided.
- [ ] Technical terminology is consistent.
- [ ] The approved `zh-Hans` glossary takes precedence.

## Core rule

**任务标题使用简洁的动宾结构，操作步骤使用直接的动作指令，图片标题使用简洁的说明性短语。**

In English:

**Use concise verb-object structures for task headings, direct action instructions for procedural steps, and descriptive phrases for figure captions.**

Example:

Heading:

> 创建 PDF 文档

Step:

> 创建 `Document` 对象。

Figure:

> 图 1. PDF 文档结构

Locale:

> `zh-Hans`