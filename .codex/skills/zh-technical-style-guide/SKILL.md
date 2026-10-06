---
name: zh-technical-style-guide
description: Use this skill when writing, translating, reviewing, or editing Simplified Chinese programming documentation. It normalizes headings, procedural instructions, figure captions, terminology, Chinese punctuation, mixed-script spacing, API identifiers, UI labels, and technical formatting.
---

# Simplified Chinese Technical Documentation Style

## Goal

Normalize programming documentation written in **Simplified Chinese** to a clear, concise, consistent style suitable for developers.

Use modern written Chinese and Simplified Chinese characters. Unless the project specifies another regional convention, prefer terminology used in mainland Chinese developer documentation.

`zh-Hans` identifies the Simplified Chinese script; `zh-CN` identifies Chinese for China. They are not interchangeable locale identifiers. A repository directory named `zh` does not by itself establish a regional locale. Preserve the project's existing locale codes and paths.

## Priority

When rules conflict, apply them in this order:

1. Project-specific localization instructions.
2. Approved Simplified Chinese terminology glossary.
3. Product and API terminology.
4. This style guide.
5. General Simplified Chinese conventions.

Never change API identifiers, commands, paths, filenames, macros, placeholders, or actual UI labels merely to satisfy a linguistic rule.

Preserve technical meaning, requirements, conditions, negation, quantities, and operation order. A style review is not permission to change API behavior or add undocumented steps.

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

Use Simplified Chinese characters in authored prose and the approved regional terminology.

Typical mainland Chinese preferences include:

| Concept | Preferred prose | Forms to review when unintended |
|---|---|---|
| file | 文件 | 檔案 / 档案 |
| user | 用户 | 使用者 |
| software | 软件 | 軟體 / 软体 |
| source code | 源代码 | 原始碼 / 原始码 |
| settings | 设置 | 設定 / 设定 |
| default | 默认 | 預設 / 预设 |
| mouse | 鼠标 | 滑鼠 |
| print | 打印 | 列印 |

This table describes contextual localization preferences, not a universal character-conversion map. Words such as `设定` can be natural in other contexts. Do not replace them without checking their meaning.

Converting Traditional Chinese characters to Simplified Chinese does not by itself produce a suitable localization. Review vocabulary, syntax, and technical meaning as well.

Preserve intentional quotations, proper names, literal UI labels, and technical literals even when they contain Traditional Chinese characters.

---

## 3. General writing style

Use concise, direct Chinese. Prefer explicit subjects and active constructions where they clarify which component performs an action.

Good:

- 此方法保存 PDF 文档。
- 以下示例将 PDF 文件转换为 DOCX 文件。
- `Document` 类表示一个 PDF 文档。
- 此选项控制图像质量。

Avoid formulaic introductions such as `值得注意的是`、`众所周知`、`我们可以看到` when the information can be stated directly.

Instead of:

> 值得注意的是，此方法需要密码。

Prefer:

> 此方法需要密码。

Use `仅`、`必须`、`可以`、`建议`、`不支持` accurately. Do not turn an optional action into a requirement or remove a limitation to make a sentence shorter.

---

## 4. Addressing the reader

Use direct instructions without unnecessary pronouns or repeated politeness markers.

Good:

- 打开文件。
- 配置转换选项。
- 保存文档。

Usually avoid:

- 您需要打开文件。
- 用户应该配置转换选项。
- 请您将文档进行保存。

Use `你` or `您` only when needed for clarity or when required by the project's voice. Do not alternate between them arbitrarily. Keep `请` when a product message or established tone requires it.

---

## 5. Headings

Use concise headings with no unnecessary final punctuation.

Good:

- 创建 PDF 文档
- 将 PDF 转换为 DOCX
- 提取 PDF 中的文本
- 配置转换选项

Avoid redundant wrappers such as `关于如何创建 PDF 文档的说明` when `创建 PDF 文档` expresses the section's purpose.

Chinese has no capitalization distinction. Preserve the official capitalization of embedded Latin names and identifiers, such as `Java`、`PDF`、`JSON`、`Document` and `.NET`.

Do not apply English title case to embedded phrases or change an identifier's case to match a heading.

---

## 6. Task headings

Use direct verb-object phrases for headings describing tasks or operations.

Good:

- 创建 PDF 文档
- 添加页面
- 将 PDF 转换为 DOCX
- 提取图像
- 配置转换选项
- 保存文档

Chinese verbs do not have the infinitive-versus-imperative distinction used in some European languages. Do not invent different verb forms for headings and steps.

Avoid mixing `创建文档`、`页面的添加`、`如何配置字体` among equivalent task headings unless their different roles justify it.

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

Do not turn a conceptual heading into a command merely because the section discusses an operation.

---

## 8. Step-by-step instructions

Start procedural steps with a clear action verb, or with necessary context followed by the action.

Good:

- 创建一个 `Document` 对象。
- 打开 PDF 文件。
- 向文档添加一个页面。
- 配置转换选项。
- 保存文档。

Avoid nominalized or needlessly passive instructions:

- `Document` 对象的创建。
- 对 PDF 文件进行打开操作。
- 文档应被保存。

Prefer `保存文档。` when instructing the reader. Preserve a declarative construction when describing what software does automatically.

---

## 9. Common action verbs

Use natural action verbs rather than translating English verbs word for word.

| Intended action | Preferred instruction verb |
|---|---|
| access | 访问 |
| add | 添加 |
| open | 打开 |
| download | 下载 |
| upload | 上传 |
| call a method | 调用 |
| configure | 配置 |
| convert | 转换 |
| copy | 复制 |
| create | 创建 |
| set a value | 设置 |
| delete | 删除 |
| run | 运行 |
| execute a command | 执行 |
| export | 导出 |
| extract | 提取 |
| import | 导入 |
| install | 安装 |
| get | 获取 |
| save | 保存 |
| select | 选择 |
| specify | 指定 |
| use | 使用 |
| check | 检查 |

Follow the approved glossary when it specifies another term. Distinguish `运行程序` from `执行命令` and `调用方法` from `访问属性` according to the actual action.

Prefer `创建对象` to `进行对象的创建` and `设置属性` to `对属性进行设置`.

---

## 10. Numbered procedures

Use numbered lists when actions must be performed in sequence.

Good:

1. 创建一个 `Document` 对象。
2. 向文档添加一个页面。
3. 创建一个 `TextFragment` 对象。
4. 将文本添加到页面中。
5. 保存 PDF 文档。

Avoid packing an entire workflow into one numbered item. Split meaningful stages while preserving the source's operation order.

Use unnumbered lists for independent options or requirements, not for a sequence whose order matters.

---

## 11. Complete sentences in steps

Write procedural steps as complete instructions ending with appropriate Chinese punctuation.

Good:

1. 打开 PDF 文档。
2. 选择要处理的页面。
3. 提取页面中的文本。

Avoid mixing action sentences with bare labels such as `页面选择` in the same procedure.

Chinese does not require a written subject in every instruction. Do not add `您` merely to make an otherwise complete instruction appear grammatically complete.

---

## 12. Context before action

When useful, state the location or condition before the action.

Good:

- 在 **File** 菜单中，选择 **Save As**。
- 在项目目录中，执行 `dotnet build`。
- 如果文件受密码保护，请提供密码。

The UI example assumes those English labels are actually displayed. Use verified localized labels when documenting a localized UI.

Preserve conditions: `如果` is not interchangeable with `当` in every technical statement. Do not imply that an optional or uncertain condition always occurs.

---

## 13. One primary action per step

Prefer one primary action per numbered step. Closely related operations may remain together when they form one logical action.

Acceptable:

> 创建一个 `Document` 对象，并将文件路径传递给构造函数。

Do not split every API call into its own step when this would fragment a single logical stage. Do not combine unrelated actions merely to shorten a list.

---

## 14. Explanations are not steps

Do not number explanatory information unless the reader must perform an action.

Preferred:

1. 创建一个 `Document` 对象。

   此对象表示要处理的 PDF 文档。

Keep an explanation or expected result in a supporting paragraph. Distinguish `系统会保存文档。` from the instruction `保存文档。`.

---

## 15. Figure captions

Unless nearby pages establish another format, use:

`图 N：说明`

Examples:

- 图 1：PDF 文档结构
- 图 2：转换选项
- 图 3：转换结果
- 图 4：项目配置

Keep captions concise and descriptive. Avoid generic captions such as `截图`、`图片` or `示例` when the figure communicates a more specific result.

Preserve figure numbers and existing cross-reference anchors. Do not renumber figures as a linguistic fix.

---

## 16. Referencing figures

Use `图` followed by the existing figure number in running text.

Good:

- 请参见图 2。
- 图 3 显示了转换结果。
- 项目配置如图 4 所示。

Do not introduce English `Figure` into ordinary Chinese prose unless it is a literal label or a required publishing convention.

---

## 17. API identifiers

Never translate or change the spelling or case of:

- class and method names;
- property names and namespaces;
- enum members and source-code variables;
- package names and command-line options;
- file extensions.

Good:

- 创建一个 `Document` 对象。
- 调用 `save()` 方法。
- 设置 `page_info` 属性。

Incorrect when the real identifiers are `Document` and `save()`:

- 创建一个 `文档` 对象。
- 调用 `保存()` 方法。

Use inline code for identifiers. Preserve the documented platform's actual API spelling; do not change `Save()` to `save()` merely because another platform uses it.

---

## 18. Grammar around API identifiers

Put Chinese particles and explanatory nouns outside inline code.

Good:

- 创建 `Document` 的实例。
- 使用 `save()` 方法。
- 访问 `pages` 集合。
- 将对象传递给 `convert()`。

Bad:

- 创建 `Document的` 实例。
- 使用 `save()方法`。

Clarify whether a term is a class, instance, method, property, parameter, or return value without changing the identifier or inventing an API relationship.

---

## 19. Files, paths, commands, and values

Format literal filenames, paths, commands, extensions, and values as code.

Good:

- 打开 `input.pdf`。
- 将结果保存为 `output.pdf`。
- 执行 `dotnet build`。
- 打开 `C:\Samples\PDF` 目录。
- 将值设置为 `true`。

Do not translate literal values, filename components, command options, or path separators. Keep ASCII syntax inside literals even when surrounding Chinese prose uses full-width punctuation.

Preserve numeric values, units, version numbers, and meaningful leading zeros. Do not convert an ASCII period in a version or decimal number into `。`.

---

## 20. UI terminology

Preserve the exact text displayed by the documented product.

If the actual UI displays **另存为**, write:

> 选择 **另存为**。

If the actual UI displays **Save As**, write:

> 选择 **Save As**。

Do not invent localized UI labels or convert an observed Traditional Chinese label to Simplified Chinese. A prose explanation may accompany an unfamiliar label, but must not replace it.

Use the project's established formatting for UI labels, normally bold rather than inline code.

---

## 21. Preferred Chinese technical terminology

Use established terminology consistently. The approved project glossary takes precedence over this table.

| Concept | Preferred Simplified Chinese |
|---|---|
| file | 文件 |
| user | 用户 |
| screen | 屏幕 |
| source code | 源代码 |
| database | 数据库 |
| directory | 目录 |
| folder | 文件夹 |
| application | 应用程序 |
| settings | 设置 |
| configuration | 配置 |
| library | 库 |
| class | 类 |
| object | 对象 |
| instance | 实例 |
| method | 方法 |
| property | 属性 |
| parameter | 参数 |
| argument | 实参, when the distinction from parameter matters |
| interface | 接口 |
| user interface | 用户界面 |
| package | 包 / 软件包, according to context |
| framework | 框架 |
| runtime | 运行时 / 运行环境, according to meaning |
| server | 服务器 |
| client | 客户端 |
| browser | 浏览器 |
| namespace | 命名空间 |
| exception | 异常 |

Do not conflate an API interface with a user interface, or a runtime component with the overall execution environment.

---

## 22. Chinese punctuation and mixed-script spacing

Use Chinese punctuation in ordinary prose: `，`、`。`、`：`、`；`、`（ ）` and `“ ”`. Use `、` for suitable short enumerations.

Do not convert punctuation inside code, URLs, identifiers, commands, HTML, or other machine-readable syntax. Preserve Markdown delimiters and front matter syntax.

Unless the project establishes another convention, insert one space between Chinese prose and independent Latin terms, numbers, or inline code:

- 使用 Java 创建 PDF 文件。
- 调用 `save()` 方法。
- 处理第 2 页。
- 将值设置为 `true`。

Do not add spaces between Chinese words or before Chinese punctuation. Keep `50%`、`3.12`、`.NET` and other indivisible tokens intact. Follow the project's unit convention rather than mechanically splitting numbers from units.

Good:

> 调用 `save()`。

Bad:

> 调用 `save()` 。

---

## 23. English technical terms

Translate established concepts when natural Chinese terminology exists, but preserve technology and product names such as `.NET`、`Python`、`Java`、`JSON`、`REST API`、`NuGet` and `GitHub`.

Avoid unnecessary English verbs in Chinese prose.

Instead of:

> 对文档执行 save 操作。

Prefer:

> 保存文档。

But preserve the real API identifier:

> 调用 `save()` 方法。

For an unfamiliar acronym, provide a Chinese explanation at first use when useful and supported by the source. Do not invent expansions or translate proper names.

---

## 24. Download and upload terminology

Use `下载` for download and `上传` for upload unless product terminology specifies otherwise.

Good:

- 下载文件。
- 将文件上传到服务器。

Distinguish `上传` from `加载`: loading a local file into memory does not necessarily involve uploading it. Preserve actual UI labels such as **Download** or **Upload**.

---

## 25. Terminology consistency

Use one preferred term for one concept. Do not alternate regional vocabulary without a reason.

Keep genuine distinctions:

- `保存` describes saving a document; `存储` may describe storage more generally.
- `删除` and `移除` can describe different operations or lifecycle effects.
- `目录` can describe a filesystem directory; `文件夹` may be the actual UI label.
- `设置` and `配置` are not automatically interchangeable in every context.
- `信息`、`数据` and `元数据` name different concepts.

Retain distinctions such as `字符` versus `字节` and `页面` versus `工作表`. Do not sacrifice technical accuracy for vocabulary uniformity.

---

## 26. Notes, tips, and warnings

Use consistent labels and preserve the original severity.

Recommended defaults when no local convention exists:

- **说明：** supplementary information.
- **提示：** optional guidance or a more efficient approach.
- **重要：** information needed to complete the task correctly.
- **警告：** destructive actions, security risks, or possible data loss.

If the project uses **注意：** for notes, preserve that convention consistently. Do not downgrade a warning into a tip or invent a new risk during a style review.

Preserve existing admonition shortcodes and their type identifiers; localize visible text only when in scope.

---

## 27. Macros and placeholders

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

Incorrect:

> 安装 `{{产品名称}}` 包。

Preserve spelling, case, braces, and delimiters exactly. Do not replace ASCII delimiters with full-width Chinese characters.

Preserve Markdown link destinations, Hugo shortcode syntax, embedded HTML, structured-data keys, and code blocks. For Hugo pages, keep front matter structure intact; do not change `url`, `aliases`, `weight`, or locale paths as a style fix. Translate visible metadata such as `title` and `linktitle` when the task includes them.

---

## 28. Parallel structure

Keep equivalent sibling headings and steps structurally parallel.

Good task headings:

- 创建文档
- 添加页面
- 配置字体
- 保存文档

Prefer this sequence to an arbitrary mixture of `创建文档`、`页面的添加`、`如何配置字体` and `文档保存操作`.

Keep conceptual headings as concepts and procedural instructions as actions. Parallelism does not justify changing a section's purpose.

---

## 29. Normalization examples

### Task heading

Before:

> 关于如何创建PDF文档的说明。

After:

> 创建 PDF 文档

### Procedural instruction

Before:

> 用户需要对文档进行保存操作。

After, when this is a reader action:

> 保存文档。

### Regional vocabulary

Before, in unintended mixed-locale prose:

> 開啟檔案並儲存結果。

After:

> 打开文件并保存结果。

Do not apply this rewrite to a quotation or literal UI label.

### Figure caption

Before:

> Figure 2: Conversion Result

After, when no different local caption convention exists:

> 图 2：转换结果

### API identifier

Incorrect when the actual method is `save()`:

> 调用 `保存()` 方法。

Correct:

> 调用 `save()` 方法。

Restore an identifier only after confirming its actual spelling. Do not guess from its translated meaning.

### Mixed-script punctuation

Before:

> 打开input.pdf文件,然后保存结果.

After:

> 打开 `input.pdf` 文件，然后保存结果。

### UI label

If the actual UI says **Save As**, preserve:

> 选择 **Save As**。

Do not replace it with **另存为** unless that is the verified label of the documented localized UI.

---

## 30. Agent decision order

When reviewing Simplified Chinese documentation:

1. Determine the structural role and scope of the text.
2. Preserve technical literals, actual UI labels, code, and protected document structure.
3. Check Simplified Chinese characters and the project's regional terminology.
4. Distinguish task headings from conceptual headings.
5. Use concise verb-object task headings and noun-phrase conceptual headings.
6. Use direct action sentences for procedural steps.
7. Preserve conditions, requirements, negation, quantities, and operation order.
8. Apply the approved glossary and keep related headings and steps parallel.
9. Check figure captions, references, Chinese punctuation, and mixed-script spacing.
10. Recheck that linguistic edits did not alter identifiers, links, placeholders, UI labels, or technical behavior.

Do not normalize documentation mechanically or transmit it to an external review service without the required authorization.

---

## 31. Review checklist

Before completing a Simplified Chinese technical-documentation task, verify:

- [ ] Authored prose uses Simplified Chinese and the approved regional terminology.
- [ ] Locale identifiers and repository paths have not been renamed.
- [ ] Intentional quotations, proper names, and literal UI labels are preserved.
- [ ] Task headings use concise verb-object phrases.
- [ ] Conceptual headings use appropriate noun phrases.
- [ ] Headings have no unnecessary final punctuation.
- [ ] Embedded Latin names retain their official spelling and capitalization.
- [ ] Procedural steps contain clear actions and appropriate final punctuation.
- [ ] Explanations and automatic software behavior have not become reader actions.
- [ ] Related headings and steps have parallel structures.
- [ ] Conditions, obligation levels, negation, quantities, and operation order are unchanged.
- [ ] Figure captions and references follow local conventions without renumbering.
- [ ] Chinese punctuation and mixed-script spacing are consistent.
- [ ] API identifiers, commands, filenames, paths, values, and placeholders are unchanged.
- [ ] UI labels match the actual documented UI.
- [ ] Technical terms are consistent without erasing meaningful distinctions.
- [ ] Markdown, links, shortcodes, front matter, code, and structured data remain intact.
- [ ] The approved project glossary takes precedence.

## Core rule

**Use Simplified Chinese consistently: concise verb-object task headings, direct action sentences for procedural instructions, and descriptive phrases for figure captions. Preserve technical meaning and literals.**

Heading:

> 创建 PDF 文档

Step:

> 创建一个 `Document` 对象。

Figure:

> 图 1：PDF 文档结构

Target:

> Simplified Chinese; follow the project's existing locale identifier.
