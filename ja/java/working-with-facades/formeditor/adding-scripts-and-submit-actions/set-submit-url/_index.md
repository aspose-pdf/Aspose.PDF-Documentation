---
title: "送信 URL の設定"
linktitle: "送信 URL の設定"
type: docs
weight: 30
url: /ja/java/set-submit-url/
description: Aspose.PDF の FormEditor ファサードを使用して、Java で PDF フォーム ボタンの送信 URL を設定する方法を学びます。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での PDF フォームの送信 URL の構成"
Abstract: この記事では、既存の PDF をバインドし、ボタン フィールドの送信 URL と送信フラグを設定し、Aspose.PDF for Java の FormEditor ファサードを使用して更新されたドキュメントを保存する方法を示します。
---
## 送信 URL の設定

1. ソース PDF を `FormEditor` ファサードにバインドしてください。
2. ボタン フィールドに対して `setSubmitUrl(...)` を呼び出してください。
3. 送信形式のために送信フラグを適用してください。
4. 更新されたドキュメントを保存してください。

```java
public static void setSubmitUrl(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.setSubmitUrl("Script_Demo_Button", "http://www.example.com/submit");
        editor.setSubmitFlag("Script_Demo_Button", SubmitFormFlag.Xfdf);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
