---
title: "PDFへのヘッダーの追加"
linktitle: "PDFへのヘッダーの追加"
type: docs
weight: 20
url: /ja/java/add-header/
description: "Java の PdfFileStamp ファサードを使用して、PDF ページにテキストおよび画像のヘッダーを追加する方法を学びます。"
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF へのテキストと画像のヘッダーの追加"
Abstract: "Aspose.PDF for Java の PdfFileStamp ファサードを使用して、PDF ドキュメントにヘッダーコンテンツを追加する方法を学びます。Java の例では、プレーンテキストヘッダー、ストリームから読み込んだ画像ヘッダー、明示的なマージン値を持つスタイル化されたヘッダーを取り上げています。"
---
## PDFへのヘッダーの追加

各ページに繰り返しヘッダーコンテンツが必要な場合は、`PdfFileStamp` を使用してください。

### 手順

1. `PdfFileStamp` インスタンスを作成し、ソース PDF にバインドしてください。
2. ヘッダーコンテンツを `FormattedText` として構築するか、画像ストリームから読み込んでください。
3. 適切な `addHeader` オーバーロードを呼び出してください。
4. 出力を保存し、Facade オブジェクトを閉じてください。

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
