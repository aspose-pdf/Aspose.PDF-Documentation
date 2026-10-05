---
title: "オープンアクションの削除"
linktitle: "オープンアクションの削除"
type: docs
weight: 20
url: /ja/java/remove-open-action/
description: Aspose.PDF の PdfContentEditor ファサードを使用して、Java で PDF から文書オープンアクションを削除する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF の文書オープンアクションを削除する
Abstract: この記事では、PDF をバインドし、文書オープンアクションを削除し、更新されたドキュメントを Aspose.PDF for Java の PdfContentEditor ファサードを使用して保存する方法を示します。
---
## 文書オープンアクションの削除

1. ソース PDF をバインドする `PdfContentEditor` ファサード。
2. 呼び出し `removeDocumentOpenAction()`。
3. 更新された PDF ドキュメントを保存してください。

```java
public static void removeOpenAction(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.removeDocumentOpenAction();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
