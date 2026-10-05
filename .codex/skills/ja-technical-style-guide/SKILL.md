---
name: ja-technical-style-guide
description: Use this skill when writing, translating, reviewing, or editing Japanese programming documentation. It normalizes headings, step-by-step instructions, figure captions, terminology, particles, API identifiers, and technical formatting to consistent Japanese.
---

# Japanese Technical Documentation Style

## Goal

Normalize Japanese programming documentation to a clear, concise, consistent style suitable for developers.

Use modern standard Japanese（標準語）.

Use **です・ます調** for explanatory prose unless a project-specific style guide specifies another convention.

## Priority

When rules conflict, apply them in this order:

1. Project-specific localization instructions.
2. Approved terminology glossary.
3. Product and API terminology.
4. This style guide.
5. General Japanese writing conventions.

Never change API identifiers, commands, paths, filenames, or actual UI labels merely to satisfy a linguistic rule.

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

Do not apply transformations mechanically.

Japanese grammatical structure depends strongly on the role of the text.

---

## 2. General prose

Use concise **です・ます調** for explanatory text.

Good:

- このメソッドは PDF ドキュメントを保存します。
- 次の例では、PDF ファイルを DOCX 形式に変換します。

Avoid mixing styles.

Bad:

- このメソッドは PDF ドキュメントを保存します。
- 戻り値は変換されたデータである。

Prefer:

- このメソッドは PDF ドキュメントを保存します。
- 戻り値は変換されたデータです。

Do not use unnecessarily literary or excessively polite language.

---

## 3. Headings

Use concise noun phrases by default.

Good:

- PDF ドキュメントの作成
- ページの追加
- テキストの抽出
- PDF から DOCX への変換
- 変換オプションの設定

Avoid unnecessarily verbose forms.

Avoid:

- PDF ドキュメントを作成する方法について

Prefer:

- PDF ドキュメントの作成

Do not normally end headings with `。`.

Good:

- PDF ドキュメントの作成

Bad:

- PDF ドキュメントの作成。

---

## 4. Task headings

For task-oriented headings, prefer noun-based action phrases.

Good:

- PDF ドキュメントの作成
- ページの追加
- PDF ファイルの変換
- テキストの抽出
- ドキュメントの保存

Avoid mixing heading structures among sibling sections.

Bad:

- PDF ドキュメントの作成
- ページを追加する
- フォント設定について
- ドキュメントを保存してください

Prefer:

- PDF ドキュメントの作成
- ページの追加
- フォントの設定
- ドキュメントの保存

---

## 5. Conceptual headings

Use concise noun phrases.

Good:

- 前提条件
- 変換オプション
- サポートされている形式
- 既知の制限事項
- フォント管理
- ドキュメント構造
- API リファレンス

Do not convert conceptual headings into procedural instructions.

---

## 6. Step-by-step instructions

Use `〜してください` for explicit procedural instructions.

Good:

- `Document` オブジェクトを作成してください。
- PDF ファイルを開いてください。
- ページを追加してください。
- 変換オプションを設定してください。
- ドキュメントを保存してください。

Avoid dictionary-form instructions.

Bad:

- `Document` オブジェクトを作成する。
- PDF ファイルを開く。
- ページを追加する。

Avoid noun fragments for numbered instructions.

Bad:

- `Document` オブジェクトの作成。
- PDF ファイルの読み込み。

Avoid excessive politeness.

Bad:

- `Document` オブジェクトを作成していただきますようお願いいたします。

Prefer:

- `Document` オブジェクトを作成してください。

---

## 7. Common instruction normalization

| Concept | Preferred form |
|---|---|
| open | 開いてください |
| create | 作成してください |
| add | 追加してください |
| configure | 設定してください |
| select | 選択してください |
| run | 実行してください |
| save | 保存してください |
| delete | 削除してください |
| install | インストールしてください |
| specify | 指定してください |
| check | 確認してください |
| convert | 変換してください |
| extract | 抽出してください |
| import | インポートしてください |
| export | エクスポートしてください |
| call | 呼び出してください |
| get | 取得してください |
| use | 使用してください |
| enter | 入力してください |

Follow the approved glossary when another term is specified.

Do not randomly alternate between:

- 使用してください
- 利用してください
- お使いください

unless the context requires the distinction.

---

## 8. Numbered procedures

Use numbered lists when actions must be performed in sequence.

Good:

1. `Document` オブジェクトを作成してください。
2. ドキュメントにページを追加してください。
3. `TextFragment` オブジェクトを作成してください。
4. テキストをページに追加してください。
5. PDF ドキュメントを保存してください。

Each step should normally represent one primary action.

Avoid:

1. ドキュメントを作成し、ページを追加し、フォントを設定してテキストを追加してから保存してください。

Split meaningful stages into separate steps.

---

## 9. Step punctuation

Write procedural steps as complete sentences and end them with `。`.

Good:

1. PDF ファイルを開いてください。
2. 処理するページを選択してください。
3. テキストを抽出してください。

Bad:

1. PDF を開く
2. ページ選択
3. テキスト抽出

---

## 10. Japanese word order

Do not force English or European-language word order onto Japanese instructions.

Natural:

- `Document` オブジェクトを作成してください。
- `save()` メソッドを呼び出してください。

Do not try to make Japanese instructions begin with the action merely because another language's style guide requires action-first steps.

Japanese instructions should preserve natural Japanese syntax.

---

## 11. Context before action

When useful, establish the context before the action.

Good:

- **ファイル** メニューで、**名前を付けて保存** を選択してください。
- `PdfSaveOptions` オブジェクトで、`Compliance` プロパティを設定してください。
- Visual Studio で、**NuGet パッケージ マネージャー**を開いてください。

---

## 12. Explanations are not steps

Keep explanatory information outside the numbered action when possible.

Preferred:

1. `Document` オブジェクトを作成してください。

   このオブジェクトは、処理対象の PDF ドキュメントを表します。

Do not number explanatory sentences merely because they appear between actions.

---

## 13. Figure captions

Use this default pattern:

`図 N. 説明`

Examples:

- 図 1. PDF ドキュメントの構造
- 図 2. 変換オプションの設定
- 図 3. 変換結果

Use concise descriptive noun phrases.

Avoid:

- Figure 3: Conversion Result
- 図 3. これは変換結果を示しています
- 図 3. スクリーンショット

A figure caption should identify what the figure communicates.

If the project uses `図 N 説明` without a period, preserve that established convention consistently.

---

## 14. Figure references

Use `図 N` in running text.

Good:

- 図 2 を参照してください。
- 変換結果を図 3 に示します。
- 図 4 はプロジェクトの構成を示しています。

Avoid `Figure` or `Fig.` unless required by the publication system.

---

## 15. API identifiers

Never translate:

- class names;
- method names;
- property names;
- namespaces;
- enum members;
- variable names in code;
- package names;
- command-line options;
- file extensions.

Good:

- `Document` オブジェクトを作成してください。
- `save()` メソッドを呼び出してください。
- `page_info` プロパティを設定してください。

Do not localize identifiers.

---

## 16. Particles and identifiers

Place Japanese particles outside inline-code formatting.

Good:

- `Document` を作成してください。
- `save()` を呼び出してください。
- `Document` のインスタンスを作成してください。
- `pages` にアクセスしてください。

Bad:

- `Document を`作成してください。
- `Document の`インスタンスを作成してください。

Code formatting contains only the literal identifier.

---

## 17. Files, paths, and commands

Format literal filenames, paths, commands, and extensions as code.

Good:

- `input.pdf` を開いてください。
- 結果を `output.pdf` として保存してください。
- `dotnet build` を実行してください。
- `C:\Samples\PDF` ディレクトリを開いてください。

Do not translate literal values.

---

## 18. UI labels

Preserve the exact label displayed by the documented product.

Japanese UI:

- **名前を付けて保存** を選択してください。

English UI:

- **Save As** を選択してください。

Do not invent localized UI labels.

---

## 19. Latin text and Japanese

Follow the project's typography convention consistently.

For general developer documentation, spacing between Japanese and independent Latin-script technical terms is acceptable and often improves readability.

Examples:

- PDF ファイル
- REST API を使用します。
- Python アプリケーション
- Visual Studio でプロジェクトを開きます。

Preserve product and identifier spelling:

- Aspose.PDF
- .NET
- GitHub
- `PdfSaveOptions`

Do not mechanically insert or remove spaces inside product names or identifiers.

---

## 20. Technical terminology

Prefer established Japanese technical terms.

Examples:

- アプリケーション
- オブジェクト
- メソッド
- プロパティ
- インターフェイス
- パラメーター
- コンストラクター
- ディレクトリ
- パッケージ
- ライブラリ
- ソースコード
- データベース

Preserve technologies and product names:

- .NET
- Python
- Java
- JSON
- REST API
- NuGet
- GitHub

Avoid unnecessary English when natural Japanese exists.

Avoid:

- ドキュメントを save してください。

Prefer:

- ドキュメントを保存してください。

But preserve actual API identifiers:

- `save()` メソッドを呼び出してください。

---

## 21. Terminology consistency

Use one preferred term for one concept.

Do not randomly alternate among:

- ドキュメント / 文書
- ディレクトリ / フォルダー
- 構成 / 設定
- 使用 / 利用
- 削除 / 消去

Use distinctions when they carry different meanings in context.

The approved project glossary takes precedence.

---

## 22. Notes and warnings

Use consistent labels:

- **注:** supplementary information.
- **ヒント:** optional advice.
- **重要:** information necessary for successful completion.
- **警告:** risk, destructive operation, security issue, or possible data loss.

Do not alternate labels without a semantic reason.

---

## 23. Parallel structure

Keep sibling headings grammatically parallel.

Good:

- PDF ドキュメントの作成
- ページの追加
- フォントの設定
- ドキュメントの保存

Bad:

- PDF ドキュメントの作成
- ページを追加する
- フォント設定について
- ドキュメントを保存してください

Keep procedural instructions parallel:

- 作成してください。
- 追加してください。
- 設定してください。
- 保存してください。

---

## 24. Normalization examples

### Heading

Before:

`PDF ドキュメントを作成する方法`

After:

`PDF ドキュメントの作成`

### Step

Before:

`PDF ファイルを開く。`

After:

`PDF ファイルを開いてください。`

### Fragment

Before:

`ページの選択。`

After:

`ページを選択してください。`

### Figure

Before:

`Figure 2: Conversion Result`

After:

`図 2. 変換結果`

### API

Before:

`Document クラスを使用してください。`

After:

`` `Document` クラスを使用してください。 ``

Apply formatting changes without translating the identifier.

---

## 25. Review checklist

Before completing a Japanese technical-documentation task, verify:

- [ ] Headings use concise noun phrases.
- [ ] Sibling headings have parallel structures.
- [ ] Headings do not end with unnecessary `。`.
- [ ] Explicit procedural steps use `〜してください`.
- [ ] Steps use natural Japanese word order.
- [ ] Steps end with `。`.
- [ ] Numbered steps contain clear actions.
- [ ] Explanatory prose consistently uses the project's chosen style.
- [ ] Figure captions follow the project's `図 N` convention.
- [ ] Figure captions describe their content.
- [ ] API identifiers have not been translated.
- [ ] Japanese particles remain outside code formatting.
- [ ] Commands, filenames, and paths remain unchanged.
- [ ] UI labels match the actual product UI.
- [ ] Japanese technical terminology is consistent.
- [ ] The approved glossary takes precedence over generic terminology.

## Core rule

**見出しには簡潔な名詞句、操作手順には「〜してください」、図のキャプションには説明的な名詞句を使用します。**

In English:

**Use concise noun phrases for headings, `〜してください` for procedural instructions, and descriptive noun phrases for figure captions.**

Example:

Heading:

> PDF ドキュメントの作成

Step:

> `Document` オブジェクトを作成してください。

Figure:

> 図 1. PDF ドキュメントの構造