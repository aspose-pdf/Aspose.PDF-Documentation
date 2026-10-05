---
title: "Java で PDF を EPUB、テキスト、XPS などに変換"
linktitle: "PDF を他の形式に変換"
type: docs
weight: 90
url: /ja/java/convert-pdf-to-other-files/
lastmod: "2026-10-06"
description: "Java と Aspose.PDF を使用して、PDF ファイルを EPUB、LaTeX、Markdown、テキスト、XPS、MobiXML に変換する方法を学びます。"
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Java で PDF を他の形式に変換する方法
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ファイルを EPUB、TeX、Markdown、テキスト、XPS、MobiXML 形式に変換する方法を、必要に応じて形式固有の保存オプションとともに説明します。
---
Aspose.PDF for Java は、PDF ドキュメントをテキスト、電子書籍、印刷、およびマークアップ指向の出力形式にエクスポートできます。

## PDF を EPUB に変換

PDF ドキュメントを EPUB 電子書籍フォーマットにエクスポートする必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`EpubSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubsaveoptions/) インスタンスを作成し、認識モードを `Flow` に設定してください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出して、PDF コンテンツを再フロー可能な EPUB マークアップとしてエクスポートしてください。
1. 変換された EPUB ファイルを保存してください。

```java
public static void convertPdfToEpub(Path inputFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            EpubSaveOptions saveOptions = new EpubSaveOptions();
            saveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.Flow);
            document.save(outputFile.toString(), saveOptions);
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## PDF を TeX に変換

PDF コンテンツを TeX マークアップにエクスポートする必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. TeX のシリアライズ用に [`TeXSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texsaveoptions/) を作成してください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出して、PDF コンテンツを TeX マークアップとして出力してください。
1. 結果の TeX ファイルを保存してください。

```java
public static void convertPdfToTex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), new TeXSaveOptions());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF からプレーンテキストへの変換

PDF ドキュメントをテキストファイルとしてエクスポートする必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. PDF ページからテキストコンテンツを抽出するために [`TextDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/textdevice/) を作成してください。
1. `device.process(document.getPages().get_Item(1), outputFile.toString())` を呼び出して、最初のページをプレーンテキストとして出力してください。
1. テキスト出力ファイルを保存してください。

```java
public static void convertPdfToTxt(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextDevice device = new TextDevice();
        device.process(document.getPages().get_Item(1), outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF から XPS への変換

PDF ドキュメントを XPS 形式に変換する必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`XpsSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpssaveoptions/) を作成し、TrueType フォントの埋め込みを有効にしてください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出してください。その結果、PDF は埋め込みフォントリソース付きの XPS としてシリアライズされます。
1. 変換された XPS ファイルを保存してください。

```java
public static void convertPdfToXps(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        XpsSaveOptions saveOptions = new XpsSaveOptions();
        saveOptions.setUseEmbeddedTrueTypeFonts(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF から Markdown への変換

PDF コンテンツを Markdown としてエクスポートする必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`MarkdownSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/markdownsaveoptions/) を作成し、画像リソースのディレクトリと HTML 画像タグの出力を設定してください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出してください。これにより、PDF コンテンツは外部画像リソースを含む Markdown として出力されます。
1. 生成された Markdown ファイルを保存してください。

```java
public static void convertPdfToMd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
        saveOptions.setResourcesDirectoryName("images");
        saveOptions.setUseImageHtmlTag(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF から Mobi XML への変換

PDF コンテンツを Mobi 互換 XML にエクスポートする必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. 選択 [`SaveFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/saveformat/) `MobiXml` を対象のシリアライズ形式としてください。
1. `document.save(outputFile.toString(), SaveFormat.MobiXml)` を呼び出してください。これにより、PDF は Mobi 互換の XML としてエクスポートされます。
1. 変換されたファイルを保存してください。

```java
public static void convertPdfToMobiXml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), SaveFormat.MobiXml);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
