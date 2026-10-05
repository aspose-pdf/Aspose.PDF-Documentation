---
title: JavaでPDFドキュメントを比較
linktitle: PDFを比較
type: docs
weight: 130
url: /ja/java/compare-pdf-documents/
description: Aspose.PDF を使用して、サイドバイサイドおよびグラフィカルな差分出力で、Java で PDF ドキュメントを比較する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaで視覚的な差分出力を使用してPDFページおよび全文書を比較
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントを比較する方法を説明します。特定のページまたは PDF 全体を並べて表示する出力で比較する方法、グラフィカルな PDF 差分レポートの生成、およびページ単位の画像差分のエクスポート方法を学びます。
---
Aspose.PDF for Java は、PDF ファイル間の差分を検出するための並べて表示する比較とグラフィカルな比較の両方の API を提供します。

## ページを比較し、差分画像のエクスポート

特定の PDF ページのペアに対して画像ベースの差分出力が必要な場合は、このサンプルを使用してください。

1. 両方のソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクト。
1. 使用する [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) ページレベルを取得する [ImagesDifference](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/imagesdifference/)。
1. 'GraphicalPdfComparer' を使用してページレベルの 'ImagesDifference' を取得してください。
1. 生成された差分画像をエクスポートし、比較結果を破棄してください。

```java
public static void comparePdfWithGetDifferenceMethod(
        Path inputFile1, Path inputFile2, Path diffOutputFile, Path destinationOutputFile) throws Exception {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        GraphicalPdfComparer comparer = new GraphicalPdfComparer();
        ImagesDifference imagesDifference = comparer.getDifference(document1.getPages().get_Item(1),
                document2.getPages().get_Item(1));

        ImageIO.write(imagesDifference.differenceToImage(Color.getRed(), Color.getWhite()),
                "png", diffOutputFile.toFile());
        ImageIO.write(imagesDifference.getDestinationImage(), "png", destinationOutputFile.toFile());
        imagesDifference.dispose();
    }
    System.out.println("Difference images saved to " + diffOutputFile + " and " + destinationOutputFile);
}
```

## 特定のページを並べて比較する

選択したページだけを比較し、横並びの PDF 結果として保存する場合は、この例を使用してください。

1. 両方のソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクト。
1. 構成 [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) 必要な比較モード用に。
1. 選択したページを比較し、出力PDFを保存します。

```java
public static void comparingSpecificPages(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        SideBySideComparisonOptions options = new SideBySideComparisonOptions();
        options.setAdditionalChangeMarks(true);
        options.setComparisonMode(ComparisonMode.IgnoreSpaces);

        SideBySidePdfComparer.compare(document1.getPages().get_Item(1), document2.getPages().get_Item(1),
                outputFile.toString(), options);
    }
    System.out.println("Specific pages comparison saved to " + outputFile);
}
```

## PDF文書全体をグラフィカルに比較する

この例は、文書全体の視覚的な違いを強調するグラフィカルなPDFレポートを生成します。

1. 両方のソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクト。
1. 設定 [GraphicalPdfComparer](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/graphicalpdfcomparer/) しきい値、色、解像度。
1. 全文書を比較し、グラフィカルな出力PDFを保存します。

```java
public static void comparePdfWithCompareDocumentsToPdfMethod(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        GraphicalPdfComparer pdfComparer = new GraphicalPdfComparer();
        pdfComparer.setThreshold(3.0);
        pdfComparer.setColor(Color.getBlue());
        pdfComparer.setResolution(new Resolution(300));
        pdfComparer.compareDocumentsToPdf(document1, document2, outputFile.toString());
    }
    System.out.println("Graphical comparison saved to " + outputFile);
}
```

## 文書全体を横に並べて比較する

文書全体をページごとに並べて比較し、サイドバイサイドのPDF出力にしたい場合はこの例を使用してください。

1. 両方のソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクト。
1. 構成 [SideBySideComparisonOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/comparison/sidebysidecomparisonoptions/) 目的の比較動作のために。
1. 全文書を比較し、結果をPDFとして保存します。

```java
public static void comparingEntireDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        SideBySideComparisonOptions options = new SideBySideComparisonOptions();
        options.setAdditionalChangeMarks(true);
        options.setComparisonMode(ComparisonMode.IgnoreSpaces);

        SideBySidePdfComparer.compare(document1, document2, outputFile.toString(), options);
    }
    System.out.println("Entire document comparison saved to " + outputFile);
}
```
