---
title: "添付ファイルの追加"
linktitle: "添付ファイルの追加"
type: docs
weight: 10
url: /ja/java/add-attachment/
description: "Aspose.PDF の PdfContentEditor ファサードを使用して、Java で外部ファイルを PDF ドキュメントに添付する方法を学習します。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での PDF にファイル添付の追加"
Abstract: この記事では、PDF をバインドし、添付ファイルをストリームとして開き、説明付きでドキュメント添付を追加し、Aspose.PDF for Java の PdfContentEditor ファサードを使用して更新されたファイルを保存する方法を示します。
---
## ドキュメント添付の追加

1. ソース PDF を `PdfContentEditor` ファサードにバインドしてください。
2. 添付ファイルを入力ストリームとして開いてください。
3. `addDocumentAttachment(...)` を、ストリーム、ファイル名、および説明を引数として呼び出してください。
4. 更新された PDF ドキュメントを保存してください。

```java
public static void addAttachment(Path inputFile, Path attachmentFile, Path outputFile) throws Exception {
    PdfContentEditor editor = new PdfContentEditor();
    try (InputStream attachmentStream = Files.newInputStream(attachmentFile)) {
        editor.bindPdf(inputFile.toString());
        editor.addDocumentAttachment(attachmentStream, attachmentFile.getFileName().toString(), "Sample attachment.");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
