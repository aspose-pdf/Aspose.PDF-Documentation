---
title: "Java で PDF を画像形式に変換"
linktitle: "PDF を画像に変換"
type: docs
weight: 70
url: /ja/java/convert-pdf-to-images-format/
lastmod: "2026-10-06"
description: "Java と Aspose.PDF を使用して、PDF ページを TIFF、BMP、EMF、JPEG、PNG、GIF、SVG ファイルとしてレンダリングする方法を学びます。"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: "Java で PDF ページを TIFF、PNG、JPEG、GIF、BMP、EMF、SVG に変換"
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF ファイルを一般的な画像形式に変換する方法を説明します。ドキュメント全体の TIFF エクスポート、画像デバイスによるページ単位のラスタ生成、PNG エクスポート時のフォント置換オプション、および `SvgSaveOptions` を使用した SVG 出力について解説します。"
---
Aspose.PDF for Java では、形式固有のデバイスオプションを使用して、PDF ページをラスタ画像およびベクタ画像フォーマットにレンダリングできます。

## PDF から BMP への変換

PDF ページを BMP 画像としてレンダリングする必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. 300 DPI の [`BmpDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/bmpdevice/) と [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) を作成してください。
1. `document.getPages()` を繰り返し処理し、各ページに対して `device.process(...)` を呼び出してください。
1. 生成された BMP 画像を番号付きの出力パスに保存してください。

```java
public static void convertPdfToBmp(Path inputFile, Path outputPrefix) {
       try (Document document = new Document(inputFile.toString())) {
           BmpDevice device = new BmpDevice(new Resolution(300));
           for (int page = 1; page <= document.getPages().size(); page++) {
               device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "bmp"));
           }
       }
       System.out.println(inputFile + " converted into " + outputPrefix);
   }
```

## PDF から EMF への変換

PDF ページを EMF ベクター画像としてエクスポートする必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`EmfDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/emfdevice/) と [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) を 300 DPI で作成してください。
1. ページを反復処理し、各ページに対して `device.process(...)` を呼び出してください。
1. EMF 出力を番号付きのファイルパスに保存してください。

```java
public static void convertPdfToEmf(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        EmfDevice device = new EmfDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "emf"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## PDF から GIF への変換

PDF ページを GIF 画像に変換する必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`GifDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/gifdevice/) と [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) を 300 DPI で作成してください。
1. ページを反復処理し、各ページをレンダリングするために `device.process(...)` を呼び出してください。
1. GIF ファイルを番号付きの出力パスに保存してください。

```java
public static void convertPdfToGif(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        GifDevice device = new GifDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "gif"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## PDF から JPEG への変換

PDF ページを JPEG 画像としてエクスポートする必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. 300 DPI の [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) を指定して [`JpegDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/jpegdevice/) を作成してください。
1. ページを反復処理し、各ページを JPEG にラスタライズするために `device.process(...)` を呼び出してください。
1. JPEG 出力ファイルを番号付きのパスに保存してください。

```java
public static void convertPdfToJpeg(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        JpegDevice device = new JpegDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "jpeg"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## PDF から PNG への変換

PDF ページを PNG 画像に変換する場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. 300 DPI の [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) を指定して [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) を作成してください。
1. ページを反復処理し、各 PDF ページごとに `device.process(...)` を呼び出してください。
1. PNG 出力を番号付きのファイルパスに保存してください。

```java
public static void convertPdfToPng(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        PngDevice device = new PngDevice(new Resolution(300));
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "png"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## PDF から PNG への変換（デフォルトのフォントフォールバックの使用）

レンダリングで欠落したグリフに対してフォールバックフォントを使用すべき場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. 300 DPI の [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) を指定して [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) を作成してください。
1. `document.setAbsentFontTryToSubstitute(true)` を有効にして、欠落したグリフがレンダリング中に代替フォントにフォールバックできるようにしてください。
1. ページをレンダリングし、PNG ファイルを保存してください。

```java
public static void convertPdfToPngWithDefaultFont(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        PngDevice device = new PngDevice(new Resolution(300));
        document.setAbsentFontTryToSubstitute(true);
        for (int page = 1; page <= document.getPages().size(); page++) {
            device.process(document.getPages().get_Item(page), numberedOutput(outputPrefix, page, "png"));
        }
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## PDF から SVG への変換

PDF ページを SVG グラフィックとしてエクスポートする必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`SvgSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgsaveoptions/) を作成し、生の `.svg` 出力が必要な場合は ZIP 圧縮を無効にしてください。
1. `setTreatTargetFileNameAsDirectory(true)` を有効にして、ページごとの SVG 出力をターゲット パスの下に整理できるようにしてください。
1. SVG 出力を保存してください。

```java
public static void convertPdfToSvg(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        SvgSaveOptions saveOptions = new SvgSaveOptions();
        saveOptions.setCompressOutputToZipArchive(false);
        saveOptions.setTreatTargetFileNameAsDirectory(true);
        document.save(outputPrefix + ".svg", saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```

## PDF から TIFF への変換

PDF ページが 1 つ以上 TIFF にエクスポートされる場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`TiffSettings`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffsettings/) を作成し、圧縮方式、色深度、および空白ページの処理を設定してください。
1. 300 DPI の [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) と準備した TIFF 設定を指定して、[`TiffDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice/) を作成してください。
1. ページをレンダリングし、TIFF 出力を保存してください。

```java
public static void convertPdfToTiff(Path inputFile, Path outputPrefix) {
    try (Document document = new Document(inputFile.toString())) {
        TiffSettings tiffSettings = new TiffSettings();
        tiffSettings.setCompression(CompressionType.LZW);
        tiffSettings.setDepth(ColorDepth.Default);
        tiffSettings.setSkipBlankPages(false);

        TiffDevice tiffDevice = new TiffDevice(new Resolution(300), tiffSettings);
        tiffDevice.process(document, outputPrefix + ".tiff");
    }
    System.out.println(inputFile + " converted into " + outputPrefix);
}
```
