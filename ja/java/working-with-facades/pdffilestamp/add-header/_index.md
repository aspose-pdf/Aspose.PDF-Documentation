---
title: "PDFにヘッダーの追加"
linktitle: "PDFにヘッダーの追加"
type: docs
weight: 20
url: /ja/java/add-header/
description: JavaのPdfFileStampファサードを使用して、PDFページにテキストと画像のヘッダーを追加する方法を学びます。
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFにテキストと画像のヘッダーを追加
Abstract: Aspose.PDF for Java の PdfFileStamp ファサードを使用して、PDFドキュメントにヘッダーコンテンツを追加する方法を学びます。Java の例では、プレーンテキストヘッダー、ストリームから読み込んだ画像ヘッダー、明示的なマージン値を持つスタイル化されたヘッダーを取り上げています。
---
## PDFにヘッダーの追加

使用 `PdfFileStamp` 各ページに繰り返しヘッダーコンテンツが必要なとき。

### 手順

1. 作成 `PdfFileStamp` インスタンス化してソースPDFにバインドしてください。
2. ヘッダーコンテンツを構築する `FormattedText` または、画像ストリームからロードしてください。
3. 適切なものを呼び出す `addHeader` 過負荷。
4. 出力を保存し、Facade オブジェクトを閉じます。

### Java の例

```java
public static void addTextHeader(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText("Sample Header");
        pdfStamper.addHeader(text, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addImageHeader(Path inputFile, Path imageFile, Path outputFile) throws Exception {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try (InputStream imageStream = Files.newInputStream(imageFile)) {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addHeader(imageStream, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addHeaderWithMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        FormattedText text = new FormattedText(
                "Sample Header",
                Color.BLUE,
                FontStyle.Helvetica,
                EncodingType.Winansi,
                true,
                12.0f);
        pdfStamper.addHeader(text, 20, 20, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
