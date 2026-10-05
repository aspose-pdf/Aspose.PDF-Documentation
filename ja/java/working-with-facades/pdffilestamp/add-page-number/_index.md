---
title: "PDFにページ番号の追加"
linktitle: "PDFにページ番号の追加"
type: docs
weight: 30
url: /ja/java/page-number/
description: JavaでPdfFileStampファサードを使用してPDF文書にページ番号を追加する方法を学びます。
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFにページ番号を追加
Abstract: Aspose.PDF for Javaを使用し、PdfFileStampファサードでPDF文書にページ番号を追加する方法を学びます。Javaの例では、デフォルト配置、明示的な座標指定、余白を使用した整列配置、カスタム開始番号によるローマ数字出力を扱います。
---
## PDFにページ番号の追加

使用 `PdfFileStamp` PDF コンテンツがすでに作成された後にページ番号付けを適用しなければならない場合。

### 手順

1. 作成 `PdfFileStamp` インスタンスを作成し、ソース PDF をバインドしてください。
2. 必要なページ番号配置戦略を選択します。
3. スタンプを付ける前に、必要に応じて番号付けスタイルと開始番号を設定します。
4. 呼び出し `addPageNumber` 必要なオーバーロードとともに。
5. 出力を保存し、ファサードオブジェクトを閉じます。

### Java の例

```java
public static void addPageNumbersDefault(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #");
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersAtCoordinates(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #", 300, 20);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersWithPositionAndMargins(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.addPageNumber("Page #", PdfFileStamp.POS_BOTTOM_RIGHT, 10, 10, 10, 10);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}

public static void addPageNumbersWithRomanStyle(Path inputFile, Path outputFile) {
    PdfFileStamp pdfStamper = new PdfFileStamp();
    try {
        pdfStamper.bindPdf(inputFile.toString());
        pdfStamper.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);
        pdfStamper.setStartingNumber(42);
        pdfStamper.addPageNumber("Page #", PdfFileStamp.POS_UPPER_RIGHT);
        pdfStamper.save(outputFile.toString());
    } finally {
        pdfStamper.close();
    }
}
```
