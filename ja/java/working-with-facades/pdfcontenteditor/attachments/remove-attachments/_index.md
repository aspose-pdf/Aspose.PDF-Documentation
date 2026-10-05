---
title: "添付ファイルの削除"
linktitle: "添付ファイルの削除"
type: docs
weight: 50
url: /ja/java/remove-attachments/
description: Aspose.PDF の PdfContentEditor ファサードを使用して、Java で PDF からすべての文書添付ファイルを削除する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF のすべての添付ファイルを削除
Abstract: この記事では、PdfContentEditor ファサードを使用して、Aspose.PDF for Java で PDF をバインドし、すべての文書添付ファイルを削除し、更新されたファイルを保存する方法を示します。
---
## すべての添付ファイルの削除

1. ソースPDFをバインドする `PdfContentEditor` ファサード。
2. 呼び出し `deleteAttachments()` すべての埋め込み添付ファイルを削除するために。
3. 更新された PDF ドキュメントを保存してください。

```java
public static void removeAttachments(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.deleteAttachments();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
