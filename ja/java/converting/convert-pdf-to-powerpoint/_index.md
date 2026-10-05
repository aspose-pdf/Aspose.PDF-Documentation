---
title: JavaでPDFをPowerPointに変換する
linktitle: PDFをPowerPointに変換する
type: docs
weight: 30
url: /ja/java/convert-pdf-to-powerpoint/
description: Aspose.PDF を使用して、Java で PDF ファイルを PowerPoint に変換する方法を学びます。編集可能な PPTX スライド、画像ベースのスライド、カスタム画像解像度が含まれます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFをPowerPointに変換する方法
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ファイルを PowerPoint プレゼンテーションに変換する方法を説明します。標準の PPTX 変換、スライドを画像として出力する方法、そして `PptxSaveOptions` を使用した画像解像度の制御についてカバーしています。
---
Aspose.PDF for Java は、スライド描画オプションを使用して PDF ページを編集可能な PowerPoint プレゼンテーションにエクスポートすることをサポートしています。使用 [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) PDF ページが PowerPoint スライドにマッピングされる方法を制御します。

## PDF を PPTX に変換

PDF ドキュメントを標準の PowerPoint プレゼンテーションとしてエクスポートする必要がある場合は、この例を使用してください。

1. ソース PDF を開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. デフォルトを作成 [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) 編集可能な PowerPoint エクスポート用。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` そのため、PDF ページは a としてシリアライズされます `.pptx` プレゼンテーション。
1. 変換された PPTX ファイルを保存してください。

```java
public static void convertPdfToPptx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF をスライドを画像として PPTX に変換

各 PDF ページを画像ベースの PowerPoint スライドにする場合は、この例を使用してください。

1. ソース PDF を開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) そして有効にする `setSlidesAsImages(true)`。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` そのため、各 PDF ページはプレゼンテーション内で画像を背景にしたスライドとしてレンダリングされます。
1. 生成されたPPTXファイルを保存してください。

```java
public static void convertPdfToPptxSlidesAsImages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        saveOptions.setSlidesAsImages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## カスタム画像解像度でPDFをPPTXに変換する

PDF から PPTX へのエクスポート時にスライド画像の品質を制御したい場合は、この例を使用してください。

1. ソース PDF を開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) そして設定 `setImageResolution(300)` より高いスライド画像の忠実度のために。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` したがって、ラスタライズされたスライドコンテンツは要求された解像度で生成されます。
1. 出力プレゼンテーションを保存してください。

```java
public static void convertPdfToPptxImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PptxSaveOptions saveOptions = new PptxSaveOptions();
        saveOptions.setImageResolution(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
