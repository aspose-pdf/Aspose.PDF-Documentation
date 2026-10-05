---
title: ドキュメント アクションの追加
linktitle: ドキュメント アクションの追加
type: docs
weight: 10
url: /ja/java/add-document-action/
description: Aspose.PDF の PdfContentEditor ファサードを使用して、Java で PDF に document-open アクションを追加する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF に document-open アクションを追加する
Abstract: この記事では、PDF をバインドし、document-open イベントに JavaScript アクションを添付し、Aspose.PDF for Java の PdfContentEditor ファサードを使用して更新されたドキュメントを保存する方法を示します。
---
## document-open アクションの追加

1. ソース PDF をバインドする `PdfContentEditor` ファサード。
2. 呼び出す `addDocumentAdditionalAction(...)` と `DOCUMENT_OPEN` イベントとJavaScriptアクションテキスト。
3. 更新された PDF ドキュメントを保存してください。

```java
public static void addDocumentAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.addDocumentAdditionalAction(PdfContentEditor.DOCUMENT_OPEN, "app.alert('Document opened with PdfContentEditor action');");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
