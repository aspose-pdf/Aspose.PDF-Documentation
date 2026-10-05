---
title: "PDF ドキュメントをプログラムで保存"
linktitle: "PDF の保存"
type: docs
weight: 30
url: /ja/java/save-pdf-document/
description: Aspose.PDF を使用して、Java で PDF ドキュメントをファイルに保存する方法、ストリームに保存する方法、または PDF 標準として保存する方法を学びます。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での Aspose.PDF ライブラリを使用して PDF ドキュメントの保存"
Abstract: この記事では、Aspose.PDF を使用して Java で PDF ドキュメントを保存する方法について説明します。ファイル パスへの保存、OutputStream への保存、PDF/X 標準ファイルとして保存する前のドキュメント変換についてカバーしています。
---
Aspose.PDF for Java は、ターゲットの宛先や出力要件に応じて、ドキュメントを保存するさまざまな方法を提供します。

## Java での PDF ドキュメントの保存

ドキュメントを保存できます：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) をディスク上のファイルに直接保存してください。
1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を `OutputStream` に保存してください。
1. [PdfFormatConversionOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformatconversionoptions/) を使用して [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を変換し、[PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) などの標準形式で保存してください。

## ドキュメントをファイルに保存

```java
public static void saveDocumentToFile(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.save(outputFile.toString());
    document.close();
}
```

## ストリームにドキュメントを保存

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

## PDF/X として文書を保存

```java
public static void saveDocumentAsStandard(Path inputFile, Path outputFile) {
    Document document = new Document(inputFile.toString());
    document.getPages().add();
    document.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
    document.save(outputFile.toString());
    document.close();
}
```
