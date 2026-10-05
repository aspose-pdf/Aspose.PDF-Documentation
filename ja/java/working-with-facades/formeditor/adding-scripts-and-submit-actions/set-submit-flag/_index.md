---
title: "Submit フラグの設定"
linktitle: "Submit フラグの設定"
type: docs
weight: 40
url: /ja/java/set-submit-flag/
description: Aspose.PDF の FormEditor ファサードを使用して PDF フォーム ボタンに submit フラグを設定するための現在の Java カバレッジを確認してください。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java FormEditor の例における Submit フラグの構成
Abstract: 現在の Java サンプルセットでは、submit-flag の構成が別個のスタンドアロン例メソッドとして公開されていません。その代わり、`setSubmitUrl(...)` 内で submit URL の構成と一緒に示されています。
---
その Java `FormEditorExamples.setSubmitUrl(...)` メソッドには以下が含まれます:

## Submit フラグを構成する

1. ソースPDFをバインドする `FormEditor` ファサード。
2. ボタンフィールドの送信URLを設定してください。
3. 必要な形式の送信フラグを設定してください。
4. 更新されたドキュメントを保存してください。

```java
editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
```

このリポジトリでサブミットフラグを設定するための、ソースバックされた Java ワークフローとして、その結合例を使用してください。
