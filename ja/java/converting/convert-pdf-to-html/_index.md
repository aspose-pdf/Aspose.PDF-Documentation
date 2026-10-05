---
title: "Java での PDF の HTML への変換"
linktitle: "PDF の HTML 形式への変換"
type: docs
weight: 50
url: /ja/java/convert-pdf-to-html/
lastmod: "2026-10-06"
description: Aspose.PDF を使用して Java で PDF を HTML に変換する方法を学びます。マルチページ出力、外部画像フォルダー、SVG の処理、レイヤード HTML レンダリングを含みます。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Java で PDF を HTML に変換する方法
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF ファイルを HTML に変換する方法を説明します。基本的な HTML エクスポートに加え、画像フォルダー、ページ分割、SVG 出力、圧縮 SVG グラフィック、PNG ページ背景、ボディのみのマークアップ、透明テキストレンダリング、およびドキュメントレイヤー変換のオプションについて取り上げています。"
---
Aspose.PDF for Java は、画像、SVG、ページ分割、透過、およびレイヤーレンダリングのオプションを使用した HTML エクスポートをサポートしています。[`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) を使用して、PDF ページ、リソース、マークアップが HTML 出力に書き込まれる方法を制御してください。

## PDF を HTML に変換

PDF を標準的な HTML ドキュメントにエクスポートする必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. 標準 HTML シリアライズ用に、デフォルトの [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) を作成してください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出してください。これにより、PDF ページのコンテンツが HTML マークアップとしてエクスポートされます。
1. 生成された HTML 出力を保存してください。

```java
public static void convertPdfToHtml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF から HTML への変換と画像の別途保存

HTML エクスポート時に抽出された画像を別々のファイルとして書き込む必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) を作成し、`setSpecialFolderForAllImages(...)` を専用の画像出力ディレクトリに設定してください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出してください。これにより、ラスタ画像がインラインのみの出力ではなく、別々のリソースファイルとして出力されます。
1. 生成された画像資産とともに HTML 出力を保存してください。

```java
public static void convertPdfToHtmlStoringImages(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForAllImages(inputFile.getParent().resolve("images").toString());
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF からマルチページ HTML への変換

各 PDF ページを HTML 出力で個別に表現する必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) を作成し、`setSplitIntoPages(true)` を有効にしてください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出してください。これにより、各 PDF ページが個別の HTML 出力として書き出されます。
1. 生成された HTML ファイルを保存してください。

```java
public static void convertPdfToHtmlMultiPage(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSplitIntoPages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF から HTML への変換と SVG の別途保存

ベクター コンテンツを個別の SVG リソースとして出力する場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) を作成し、`setSpecialFolderForSvgImages(...)` を外部 SVG リソース ディレクトリに設定してください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出してください。これにより、ベクターグラフィックはメインの HTML ファイルの外部に保存されます。
1. HTML 出力と SVG アセットを保存してください。

```java
public static void convertPdfToHtmlStoringSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF から圧縮 SVG を含む HTML への変換

HTML エクスポート時に SVG 出力を最適化する必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) を作成し、SVG リソース用の専用フォルダーを設定してください。
1. `setCompressSvgGraphicsIfAny(true)` を有効にして、SVG アセットをエクスポート時に圧縮してください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出して、変換された HTML ファイルを保存してください。

```java
public static void convertPdfToHtmlCompressSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSpecialFolderForSvgImages(inputFile.getParent().resolve("svg_images").toString());
        saveOptions.setCompressSvgGraphicsIfAny(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF から PNG ページ背景付き HTML への変換

ページの背景を HTML 出力で PNG 画像としてレンダリングする必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) を作成し、ラスター画像の保存モードを PNG ページ背景に設定してください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出してください。ページの背景コンテンツが PNG を使用した HTML レイヤーとして出力されます。
1. 変換された HTML 出力を保存してください。

```java
public static void convertPdfToHtmlPngBackground(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setRasterImagesSavingMode(
                HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF から HTML の本文のみへの変換

HTML 全体の文書シェルではなく、本文のマークアップだけが必要な場合にこの例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) を作成し、マークアップ生成モードを `WriteOnlyBodyContent` に設定してください。
1. `setSplitIntoPages(true)` を有効のままにしてください。本文のみの出力でもページ区切りを維持する必要がある場合に有効です。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出して、HTML 出力を保存してください。

```java
public static void convertPdfToHtmlBodyContent(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setHtmlMarkupGenerationMode(
                HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
        saveOptions.setSplitIntoPages(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF から透明テキストレンダリングで HTML への変換

透明なテキストを HTML エクスポートで保持する必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) を作成し、透明テキストおよび影付きテキストの保存を有効にしてください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出してください。これにより、透過に関連するテキストの外観が HTML の結果に保持されます。
1. 変換された HTML 出力を保存してください。

```java
public static void convertPdfToHtmlTransparentTextRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setSaveTransparentTexts(true);
        saveOptions.setSaveShadowedTextsAsTransparentTexts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 文書レイヤーレンダリングを使用して PDF を HTML に変換

PDF レイヤーの可視性を HTML の結果に反映させたい場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) を作成し、`setConvertMarkedContentToLayers(true)` を有効にしてください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出してください。これにより、マークされた PDF コンテンツが HTML レイヤーにマッピングされます。
1. エクスポートされた HTML ファイルを保存してください。

```java
public static void convertPdfToHtmlDocumentLayersRendering(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        saveOptions.setConvertMarkedContentToLayers(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
