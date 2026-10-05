---
title: JavaでPDFをHTMLに変換する
linktitle: PDFをHTML形式に変換する
type: docs
weight: 50
url: /ja/java/convert-pdf-to-html/
lastmod: "2026-10-05"
description: Aspose.PDF を使用して Java で PDF を HTML に変換する方法を学びます。マルチページ出力、外部画像フォルダー、SVG の処理、レイヤード HTML レンダリングを含みます。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Java で PDF を HTML に変換する方法
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ファイルを HTML に変換する方法を説明します。基本的な HTML エクスポートに加え、画像フォルダー、ページ分割、SVG 出力、圧縮 SVG グラフィック、PNG ページ背景、ボディのみのマークアップ、透明テキストレンダリング、そしてドキュメントレイヤー変換のオプションについて取り上げています。
---
Aspose.PDF for Java は、画像、SVG、ページ分割、透過、およびレイヤーレンダリングのオプションを使用したHTMLエクスポートをサポートしています。 使用 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) PDF ページ、リソース、マークアップが HTML 出力に書き込まれる方法を制御するために。

## PDF を HTML に変換

PDF を標準的な HTML ドキュメントにエクスポートする必要がある場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. デフォルトを作成 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) 標準HTMLシリアライズ用に。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` そのため、PDFページのコンテンツはHTMLマークアップとしてエクスポートされます。
1. 生成されたHTML出力を保存してください。

```java
public static void convertPdfToHtml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HtmlSaveOptions saveOptions = new HtmlSaveOptions();
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF を HTML に変換し、画像を別々に保存する

HTMLエクスポート時に抽出された画像を別々のファイルとして書き込む必要がある場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) そして設定 `setSpecialFolderForAllImages(...)` 専用の画像出力ディレクトリへ。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` したがって、ラスタ画像はインラインのみの出力ではなく、別々のリソースファイルとして出力されます。
1. 生成された画像資産とともにHTML出力を保存してください。

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

## PDF をマルチページ HTML に変換

各 PDF ページを HTML 出力で個別に表現する必要がある場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) そして有効にする `setSplitIntoPages(true)`。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` したがって、各PDFページは別々のHTML出力として書き出されます。
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

## PDF を HTML に変換し、SVG を別々に保存する

ベクター コンテンツを別々の SVG リソースとして出力する場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) そして設定 `setSpecialFolderForSvgImages(...)` 外部 SVG リソース ディレクトリへ。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` そのためベクターグラフィックはメインのHTMLファイルの外部に保存されます。
1. HTML出力とSVGアセットを保存してください。

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

## PDF を圧縮された SVG で HTML に変換する

HTML エクスポート時に SVG 出力を最適化すべき場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) そして、SVGリソース用に専用フォルダーを設定してください。
1. 有効にする `setCompressSvgGraphicsIfAny(true)` そのため、SVG アセットはエクスポート時に圧縮されます。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` そして変換されたHTMLファイルを保存してください。

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

## PDF を PNG ページ背景付きの HTML に変換する

ページの背景を HTML 出力で PNG 画像としてレンダリングする必要がある場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) そして、ラスター画像の保存モードを PNG ページ背景に設定してください。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` その結果、ページの背景コンテンツは PNG バックの HTML レイヤーとして出力されます。
1. 変換されたHTML出力を保存してください。

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

## PDF を HTML の本文だけに変換

HTML全体の文書シェルではなく、本文のマークアップだけが必要な場合にこの例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) そしてマークアップ生成モードを設定します `WriteOnlyBodyContent`。
1. 保持 `setSplitIntoPages(true)` 本文のみの出力でもページ区切りを維持すべき場合に有効です。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` そしてHTML出力を保存してください。

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

## PDF を透明テキストレンダリングで HTML に変換

透明なテキストをHTMLエクスポートで保持する必要がある場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) 透明および影付きテキストの保存を有効にしてください。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` そのため、透過に関連するテキストの外観はHTML結果に保持されます。
1. 変換されたHTML出力を保存してください。

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

PDFレイヤーの可視性がHTML結果に反映される場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`HtmlSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/) そして有効にする `setConvertMarkedContentToLayers(true)`。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` そのようにマークされたPDFコンテンツはHTMLレイヤーにマッピングされます。
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
