---
title: "PDFへのページ番号の追加"
linktitle: "PDFへのページ番号の追加"
type: docs
weight: 30
url: /ja/java/page-number/
description: "Java で PdfFileStamp ファサードを使用して PDF 文書にページ番号を追加する方法を学びます。"
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java で PDF にページ番号を追加"
Abstract: "Aspose.PDF for Java を使用し、PdfFileStamp ファサードで PDF 文書にページ番号を追加する方法を学びます。Java の例では、デフォルト配置、明示的な座標指定、余白を使用した整列配置、カスタム開始番号によるローマ数字出力を扱います。"
---
## PDFへのページ番号の追加

`PdfFileStamp` を使用するのは、PDF コンテンツがすでに作成された後にページ番号付けを適用しなければならない場合です。

### 手順

1. `PdfFileStamp` インスタンスを作成し、ソース PDF をバインドしてください。
2. 必要なページ番号配置戦略を選択してください。
3. スタンプを付ける前に、必要に応じて番号付けスタイルと開始番号を設定してください。
4. `addPageNumber` を必要なオーバーロードで呼び出してください。
5. 出力を保存し、ファサードオブジェクトを閉じてください。

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
