---
title: "送信ボタンの作成"
linktitle: "送信ボタンの作成"
type: docs
weight: 60
url: /ja/java/create-submit-button/
description: Aspose.PDF の FormEditor ファサードを使用して、Java で PDF ドキュメントに送信ボタンを追加する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF の送信ボタンを作成
Abstract: この記事では、既存の PDF をバインドし、ターゲット URL を持つ送信ボタン フィールドを追加し、Aspose.PDF for Java の FormEditor ファサードを使用して変更されたドキュメントを保存する方法を示します。
---
使用する `FormEditorExamples.createSubmitButton(...)` フォームデータを送信するボタンを作成するために。

## 送信ボタンの作成

1. ソースPDFをバインドする `FormEditor` ファサード。
2. 呼び出す `addSubmitBtn(...)` ボタン名、ページ、ラベル、対象 URL、および矩形と共に。
3. 更新されたドキュメントを保存してください。

```java
public static void createSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show", 100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
