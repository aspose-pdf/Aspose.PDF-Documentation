---
title: JavaでPDFをEPUB、テキスト、XPS、その他に変換
linktitle: PDFを他の形式に変換
type: docs
weight: 90
url: /ja/java/convert-pdf-to-other-files/
lastmod: "2026-10-05"
description: Java と Aspose.PDF を使用して、PDF ファイルを EPUB、LaTeX、Markdown、テキスト、XPS、MobiXML に変換する方法を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Java で PDF を他の形式に変換する方法
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ファイルを EPUB、TeX、Markdown、テキスト、XPS、MobiXML 形式に変換する方法を、必要に応じて形式固有の保存オプションとともに説明します。
---
Aspose.PDF for Java は、PDF ドキュメントをテキスト、電子書籍、印刷、およびマークアップ指向の出力形式にエクスポートできます。

## PDFをEPUBに変換

PDF ドキュメントを EPUB 電子書籍フォーマットにエクスポートする必要がある場合は、この例を使用してください。

1. ソース PDF を a で開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`EpubSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/epubsaveoptions/) 認識モードを設定して `Flow`。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` そのため、PDFコンテンツは再フロー可能なEPUBマークアップとしてエクスポートされます。
1. 変換されたEPUBファイルを保存してください。

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

1. ソース PDF を a で開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`TeXSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/texsaveoptions/) TeX のシリアライズ用に。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` そのため、PDF コンテンツは TeX マークアップとして出力されます。
1. 結果の TeX ファイルを保存してください。

```java
public static void convertPdfToTex(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), new TeXSaveOptions());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF をプレーンテキストに変換

PDF ドキュメントをテキストファイルとしてエクスポートする必要がある場合は、この例を使用してください。

1. ソース PDF を a で開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`TextDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/textdevice/) PDFページからテキストコンテンツを抽出してください。
1. 呼び出す `device.process(document.getPages().get_Item(1), outputFile.toString())` 最初のページをプレーンテキストとして書く。
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

## PDF を XPS に変換

PDF ドキュメントを XPS 形式に変換する必要がある場合は、この例を使用してください。

1. ソース PDF を a で開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`XpsSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/xpssaveoptions/) そして、埋め込みTrueTypeフォントを有効にしてください。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` その結果、PDFは埋め込みフォントリソース付きのXPSとしてシリアライズされます。
1. 変換されたXPSファイルを保存してください。

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

## PDF を Markdown に変換する

PDF コンテンツを Markdown としてエクスポートする必要がある場合は、この例を使用してください。

1. ソース PDF を a で開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`MarkdownSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/markdownsaveoptions/) そして、画像リソースディレクトリを構成し、HTML画像タグの出力を行います。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` そのため、PDF コンテンツは外部画像リソースを含む Markdown として出力されます。
1. 生成されたMarkdownファイルを保存してください。

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

## PDF を Mobi XML に変換する

PDFコンテンツをMobi互換XMLにエクスポートする必要がある場合は、この例を使用してください。

1. ソース PDF を a で開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 選択 [`SaveFormat`](https://reference.aspose.com/pdf/java/com.aspose.pdf/saveformat/) `MobiXml` 対象のシリアライズ形式として。
1. 呼び出す `document.save(outputFile.toString(), SaveFormat.MobiXml)` したがって、PDFはMobi互換のXMLとしてエクスポートされます。
1. 変換されたファイルを保存してください。

```java
public static void convertPdfToMobiXml(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.save(outputFile.toString(), SaveFormat.MobiXml);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
