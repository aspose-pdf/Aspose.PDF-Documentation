---
title: JavaでPDFを画像形式に変換
linktitle: PDFを画像に変換
type: docs
weight: 70
url: /ja/java/convert-pdf-to-images-format/
lastmod: "2026-10-05"
description: Java と Aspose.PDF を使用して、PDF ページを TIFF、BMP、EMF、JPEG、PNG、GIF、SVG ファイルとしてレンダリングする方法を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Java で PDF ページを TIFF、PNG、JPEG、GIF、BMP、EMF、SVG に変換します。
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ファイルを一般的な画像形式に変換する方法を説明します。ドキュメント全体の TIFF エクスポート、画像デバイスによるページ単位のラスタ生成、PNG エクスポート時のフォント置換オプション、そして `SvgSaveOptions` を使用した SVG 出力についてカバーしています。
---
Aspose.PDF for Java は、形式固有のデバイスオプションを使用して、PDF ページをラスタ画像およびベクタ画像フォーマットにレンダリングできます。

## PDF を BMP に変換

PDF ページを BMP 画像としてレンダリングする必要がある場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`BmpDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/bmpdevice/) と [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI の。
1. 繰り返し処理する `document.getPages()` そして呼び出す `device.process(...)` 各ページごとに。
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

## PDFをEMFに変換

PDF ページを EMF ベクター画像としてエクスポートする必要がある場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`EmfDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/emfdevice/) と [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI の。
1. ページを反復処理し、呼び出す `device.process(...)` 各ページごとに。
1. EMF出力を番号付きのファイルパスに保存してください。

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

## PDFをGIFに変換

PDFページをGIF画像に変換する必要がある場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`GifDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/gifdevice/) と [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI の。
1. ページを反復処理し、呼び出す `device.process(...)` 各ページをレンダリングしてください。
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

## PDF を JPEG に変換

PDFページをJPEG画像としてエクスポートする必要がある場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`JpegDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/jpegdevice/) と [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI の。
1. ページを反復処理し、呼び出す `device.process(...)` 各ページをJPEGにラスタライズしてください。
1. JPEG出力ファイルを番号付きのパスに保存してください。

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

## PDF を PNG に変換する

PDF ページを PNG 画像に変換する場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) と [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI の。
1. ページを反復処理し、呼び出す `device.process(...)` 各 PDF ページごとに。
1. PNG出力を番号付きのファイルパスに保存してください。

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

## PDF を PNG に変換し、デフォルトのフォントフォールバックの使用

レンダリングで欠落したグリフに対してフォールバックフォントを使用すべき場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`PngDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/pngdevice/) と [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI の。
1. 有効にする `document.setAbsentFontTryToSubstitute(true)` 欠落したグリフは、レンダリング中に代替フォントにフォールバックできるようにしてください。
1. ページをレンダリングし、PNG ファイルを保存します。

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

## PDF を SVG に変換

PDF ページを SVG グラフィックとしてエクスポートする必要がある場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`SvgSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgsaveoptions/) そして、生の状態でZIP圧縮を無効にします `.svg` 出力が必要です。
1. 有効にする `setTreatTargetFileNameAsDirectory(true)` したがって、ページごとの SVG 出力はターゲット パスの下に整理できます。
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

## PDF を TIFF に変換

PDF ページが 1 つ以上 TIFF にエクスポートされる場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`TiffSettings`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffsettings/) 圧縮、カラー深度、空白ページの動作を構成してください。
1. 作成 [`TiffDevice`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice/) と [`Resolution`](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/resolution/) 300 DPI と、用意された TIFF 設定の
1. ページをレンダリングし、TIFF 出力を保存します。

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
