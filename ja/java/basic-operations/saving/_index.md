---
title: PDF ドキュメントをプログラムで保存する
linktitle: "PDF の保存"
type: docs
weight: 30
url: /ja/java/save-pdf-document/
description: Aspose.PDF を使用して、Java で PDF ドキュメントをファイルに保存する方法、ストリームに保存する方法、または PDF 標準として保存する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で Aspose.PDF ライブラリを使用して PDF ドキュメントを保存する
Abstract: この記事では、Aspose.PDF を使用して Java で PDF ドキュメントを保存する方法について説明します。ファイル パスへの保存、OutputStream への保存、PDF/X 標準ファイルとして保存する前のドキュメント変換についてカバーしています。
---
Aspose.PDF for Java は、ターゲットの宛先や出力要件に応じて、ドキュメントを保存するさまざまな方法を提供します。

## Java での PDF ドキュメントの保存

ドキュメントを保存できます：

1. 保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) ディスク上のファイルに直接。
1. 保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) へ `OutputStream`。
1. 変換する [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) で [PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) そして、標準形式（例：）で保存する [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/)。

## ドキュメントをファイルに保存

```java
public static void saveDocumentToFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.save(outputFile.toString());
    document.close();
}
```

## ストリームにドキュメントの保存

```java
public static void saveDocumentToStream(Path inputFile, Path outputFile) throws Exception {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    try (OutputStream stream = Files.newOutputStream(outputFile)) {
        document.save(stream);
    } finally {
        document.close();
    }
}
```

## PDF/X として文書の保存

```java
public static void saveDocumentAsStandard(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    document.save(outputFile.toString());
    document.close();
}
```
