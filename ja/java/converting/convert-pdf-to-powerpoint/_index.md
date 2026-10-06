---
title: "Java での PDF の PowerPoint への変換"
linktitle: "PDF の PowerPoint への変換"
type: docs
weight: 30
url: /ja/java/convert-pdf-to-powerpoint/
description: "Aspose.PDF を使用して、Java で PDF ファイルを PowerPoint に変換する方法を学習します。編集可能な PPTX スライド、画像ベースのスライド、およびカスタム画像解像度が含まれます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java で PDF を PowerPoint に変換する方法"
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF ファイルを PowerPoint プレゼンテーションに変換する方法を説明します。標準の PPTX 変換、スライドを画像として出力する方法、および `PptxSaveOptions` を使用した画像解像度の制御について取り上げます。"
---
Aspose.PDF for Java は、スライド描画オプションを使用して PDF ページを編集可能な PowerPoint プレゼンテーションにエクスポートすることをサポートしています。[`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) を使用して、PDF ページが PowerPoint スライドにマッピングされる方法を制御してください。

## PDF から PPTX への変換

PDF ドキュメントを標準の PowerPoint プレゼンテーションとしてエクスポートする必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. 編集可能な PowerPoint エクスポート用に、デフォルトの [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) を作成してください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出してください。PDF ページが `.pptx` プレゼンテーションとして保存されます。
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

## PDF から PPTX への変換（スライドを画像として）

各 PDF ページを画像ベースの PowerPoint スライドに変換する場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) を作成し、`setSlidesAsImages(true)` を有効にしてください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出してください。これにより、各 PDF ページはプレゼンテーション内で画像を背景にしたスライドとしてレンダリングされます。
1. 生成された PPTX ファイルを保存してください。

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

## カスタム画像解像度で PDF の PPTX への変換

PDF から PPTX へのエクスポート時にスライド画像の品質を制御したい場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/pptxsaveoptions/) を作成し、より高いスライド画像の忠実度のために `setImageResolution(300)` を設定してください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出してください。これにより、ラスタライズされたスライドコンテンツが指定された解像度で生成されます。
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
