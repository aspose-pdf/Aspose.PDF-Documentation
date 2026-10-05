---
title: "Submit フラグの設定"
linktitle: "Submit フラグの設定"
type: docs
weight: 40
url: /ja/java/set-submit-flag/
description: "Aspose.PDF の FormEditor ファサードを使用して PDF フォーム ボタンに submit フラグを設定する場合の、現在の Java カバレッジを確認してください。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Java FormEditor の例における Submit フラグの構成
Abstract: "現在の Java サンプルセットでは、submit フラグの構成は別個のスタンドアロンの例メソッドとして公開されていません。その代わり、`setSubmitUrl(...)` メソッド内で submit URL の構成とともに示されています。"
---
Java の `FormEditorExamples.setSubmitUrl(...)` メソッドには、以下の内容が含まれます。

## Submit フラグの構成

1. ソース PDF を `FormEditor` ファサードにバインドしてください。
2. ボタンフィールドの送信 URL を設定してください。
3. 必要な形式の送信フラグを設定してください。
4. 更新されたドキュメントを保存してください。

```java
editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
```

このリポジトリでサブミットフラグを設定するための、ソースバックされた Java ワークフローとして、その結合例を使用してください。
