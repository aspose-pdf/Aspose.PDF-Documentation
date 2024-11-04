---
title: PDFを画像形式に変換する 
linktitle: PDFを画像に変換する
type: docs
weight: 70
url: /java/convert-pdf-to-images-format/
lastmod: "2021-11-19"
description: このトピックでは、Aspose.PDFがPDFをさまざまな画像形式に変換する方法を示します。数行のコードでPDFページをPNG、JPEG、BMP画像に変換します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

**Aspose.PDF for Java**は、BMP、JPEG、GIF、PNG、EMF、TIFF、SVGなどの画像形式にPDFドキュメントを変換することができます。変換は、Deviceを使用する方法とSaveOptionを使用する方法の2つのアプローチで行われます。

ライブラリには、仮想デバイスを使用して画像を変換するためのいくつかのクラスがあります。DocumentDeviceはドキュメント全体の変換を目的としていますが、ImageDeviceは特定のページのためのものです。

## DocumentDeviceクラスを使用してPDFを変換する

**Aspose.PDF for Java**は、PDFページをTIFF画像に変換することが可能です。

[TiffDeviceクラス](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/tiffdevice)を使用すると、PDFページをTIFF画像に変換することができます。
 このクラスは、PDFファイル内のすべてのページを単一のTIFF画像に変換するためのメソッド「Process」を提供します。

### PDFページを1つのTIFF画像に変換

Aspose.PDF for Javaは、PDFファイル内のすべてのページを単一のTIFF画像に変換する方法を説明します：

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスのオブジェクトを作成します。
1. ドキュメントを変換するために [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/DocumentDevice#process-com.aspose.pdf.IDocument-int-int-java.io.OutputStream-) メソッドを呼び出します。
1. 出力ファイルのプロパティを設定するには、[TiffSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/TiffSettings) クラスを使用します。

以下のコードスニペットは、PDFのすべてのページを単一のTIFF画像に変換する方法を示しています。

```java
// ドキュメントを開く
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

// 解像度オブジェクトを作成
Resolution resolution = new Resolution(300);

// TiffSettingsオブジェクトを作成
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.None);
tiffSettings.setDepth(ColorDepth.Default);
tiffSettings.setShape(ShapeType.Landscape);
tiffSettings.setSkipBlankPages(false);

// TIFFデバイスを作成
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

// 特定のページを変換し、画像をストリームに保存
tiffDevice.process(document, DATA_DIR + "AllPagesToTIFF_out.tif");
```

### 単一ページをTIFF画像に変換

Aspose.PDF for Javaを使用すると、PDFファイル内の特定のページをTIFF画像に変換できます。変換には、ページ番号を引数として受け取るProcess(..)メソッドのオーバーロードされたバージョンを使用します。以下のコードスニペットは、PDFの最初のページをTIFF形式に変換する方法を示しています。

```java
// ドキュメントを開く
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
String tiffFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF_out.tif").toString();
Document document = new Document(documentFileName);

// 解像度オブジェクトを作成
Resolution resolution = new Resolution(300);

// TiffSettingsオブジェクトを作成
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.None);
tiffSettings.setDepth(ColorDepth.Default);
tiffSettings.setShape(ShapeType.Landscape);

// TIFFデバイスを作成
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

// 特定のページを変換し、イメージをストリームに保存
tiffDevice.process(document, 1, 1, tiffFileName);
```


### 変換中にBradleyアルゴリズムを使用する

Aspose.PDF for Javaは、LZW圧縮を使用してPDFをTIFFに変換する機能をサポートしており、その後AForgeを使用して二値化を適用できます。しかし、ある顧客は、いくつかの画像に対して大津の方法を使用して閾値を取得する必要があるため、Bradleyも使用したいと要望しました。

```java
// ドキュメントを開く
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

String outputImageFileName = Paths.get(DATA_DIR.toString(), "resultant_out.tif").toString();
String outputBinImageFileName = Paths.get(DATA_DIR.toString(), "tiff-bin_out.tif").toString();

java.io.OutputStream outputImageFile = new java.io.FileOutputStream(outputImageFileName);
java.io.OutputStream outputBinImageFile = new java.io.FileOutputStream(outputBinImageFileName);

// 解像度オブジェクトを作成
Resolution resolution = new Resolution(300);
// TiffSettingsオブジェクトを作成
TiffSettings tiffSettings = new TiffSettings();
tiffSettings.setCompression(CompressionType.LZW);
tiffSettings.setDepth(ColorDepth.Format1bpp);

// TIFFデバイスを作成
TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
// 特定のページを変換し、画像をストリームに保存
tiffDevice.process(document, outputImageFile);
outputImageFile.close();

// 出力画像を保存するためのストリームオブジェクトを作成
java.io.InputStream inStream = new java.io.FileInputStream(outputImageFileName);
tiffDevice.binarizeBradley(inStream, outputBinImageFile, 0.1);
```


### PDFページをピクセル化されたTIFF画像に変換する

PDFファイル内のすべてのページをピクセル化されたTIFF形式に変換するには、IndexedConversionTypeのPixelatedオプションを使用します。

```java
// PDFページをピクセル化されたTIFF画像に変換する
// PDFファイル内のすべてのページをピクセル化されたTIFF形式に変換するには、IndexedConversionTypeのPixelatedオプションを使用します。

// ドキュメントを開く
String documentFileName = Paths.get(DATA_DIR.toString(), "PageToTIFF.pdf").toString();
Document document = new Document(documentFileName);

// 出力画像を保存するためのストリームオブジェクトを作成
java.io.OutputStream imageStream = new java.io.FileOutputStream("Image.tiff");

// 解像度オブジェクトを作成
com.aspose.pdf.devices.Resolution resolution = new com.aspose.pdf.devices.Resolution(300);

// TiffSettingsオブジェクトをインスタンス化
com.aspose.pdf.devices.TiffSettings tiffSettings = new com.aspose.pdf.devices.TiffSettings();

// 生成されたTIFF画像の圧縮を設定
tiffSettings.setCompression(com.aspose.pdf.devices.CompressionType.CCITT4);
// 生成された画像の色深度を設定
tiffSettings.setDepth(com.aspose.pdf.devices.ColorDepth.Format4bpp);
// PDFをTIFFにレンダリングする際に空白ページをスキップ
tiffSettings.setSkipBlankPages(true);
// 画像の明るさを設定
tiffSettings.setBrightness(.5f);

// IndexedConversion Typeを設定、デフォルト値はsimple
tiffSettings.setIndexedConversionType(IndexedConversionType.Pixelated);

// 特定の解像度でTiffDeviceオブジェクトを作成
TiffDevice tiffDevice = new TiffDevice(2480, 3508, resolution, tiffSettings);

// 特定のページ（ページ1）を変換し、画像をストリームに保存
tiffDevice.process(document, 1, 1, imageStream);

// ストリームを閉じる
imageStream.close();
```


{{% alert color="success" %}}
**PDFをTIFFにオンラインで変換してみてください**

Aspose.PDF for Javaは、オンラインで無料のアプリケーション「[PDF to TIFF](https://products.aspose.app/pdf/conversion/pdf-to-tiff)」を提供しており、その機能と作業の品質を調査してみることができます。

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## ImageDeviceクラスを使用してPDFを変換

`ImageDevice`は、`BmpDevice`、`JpegDevice`、`GifDevice`、`PngDevice`、`EmfDevice`の先祖です。

- [BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice)クラスは、PDFページを<abbr title="Bitmap Image File">BMP</abbr>画像に変換することを可能にします。
- [EmfDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/EmfDevice)クラスは、PDFページを<abbr title="Enhanced Meta File">EMF</abbr>画像に変換することを可能にします。

- [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice)クラスは、PDFページをJPEG画像に変換することを可能にします。
- [PngDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/PngDevice) クラスを使用すると、PDF ページを <abbr title="Portable Network Graphics">PNG</abbr> 画像に変換できます。
- [GifDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/GifDevice) クラスを使用すると、PDF ページを <abbr title="Graphics Interchange Format">GIF</abbr> 画像に変換できます。

PDF ページを画像に変換する方法を見てみましょう。

[BmpDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice) クラスは、PDF ファイルの特定のページを BMP 画像形式に変換できる [Process](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/BmpDevice#process-com.aspose.pdf.Page-com.aspose.ms.System.Drawing.Graphics-) という名前のメソッドを提供します。他のクラスも同じメソッドを持っています。したがって、PDF ページを画像に変換する必要がある場合は、必要なクラスをインスタンス化するだけです。

次のコードスニペットは、この可能性を示しています。

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.devices.*;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * PDF を画像に変換します。
 */
public final class ConvertPDFtoImage {
    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertPDFtoImage() {

    }

    public static void run() throws IOException {
        runConvertPdfUsingImageDevice();
    }

    public static void runConvertPdfUsingImageDevice() throws IOException {
        // Resolution オブジェクトを作成
        Resolution resolution = new Resolution(300);
        BmpDevice bmpDevice = new BmpDevice(resolution);
        JpegDevice jpegDevice = new JpegDevice(resolution);
        GifDevice gifDevice = new GifDevice(resolution);
        PngDevice pngDevice = new PngDevice(resolution);
        EmfDevice emfDevice = new EmfDevice(resolution);

        Document document = new Document(DATA_DIR + "ConvertAllPagesToBmp.pdf");

        convertPDFtoImages(bmpDevice, "bmp", document);
        convertPDFtoImages(jpegDevice, "jpeg", document);
        convertPDFtoImages(gifDevice, "gif", document);
        convertPDFtoImages(pngDevice, "png", document);
        convertPDFtoImages(emfDevice, "emf", document);
    }

    public static void convertPDFtoImages(
            ImageDevice imageDevice,
            String ext,
            Document document)
            throws IOException {
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            java.io.OutputStream imageStream = new java.io.FileOutputStream(
                    DATA_DIR + "image" + pageCount + "_out." + ext);
            // 特定のページを変換し、画像をストリームに保存
            imageDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // ストリームを閉じる
            imageStream.close();
        }
    }
}
```


{{% alert color="success" %}}
**PDFをPNGにオンラインで変換してみてください**

私たちの無料アプリケーションがどのように機能するかの例として、次の機能を確認してください。

Aspose.PDF for Javaは、オンライン無料アプリケーション["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)を提供しており、その機能と品質を試して調査することができます。

[![無料アプリを使用してPDFをPNGに変換する方法](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## SaveOptionsクラスを使用してPDFを変換する

この記事のこの部分では、JavaとSaveOptionsクラスを使用してPDFを<abbr title="Scalable Vector Graphics">SVG</abbr>に変換する方法を示します。

{{% alert color="success" %}}
**PDFをSVGにオンラインで変換してみてください**

Aspose.PDF for Javaは、オンライン無料アプリケーション["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)を提供しており、その機能と品質を試して調査することができます。

[![無料アプリを使用してPDFをSVGに変換する方法](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**スケーラブルベクターグラフィックス (SVG)** は、二次元ベクターグラフィックスのためのXMLベースのファイル形式の仕様ファミリーであり、静的および動的（インタラクティブまたはアニメーション）なものがあります。SVGの仕様はオープンスタンダードであり、1999年以来ワールドワイドウェブコンソーシアム (W3C) によって開発されています。

SVG画像とその動作はXMLテキストファイルで定義されています。これは、それらが検索、インデックス化、スクリプト化され、必要に応じて圧縮できることを意味します。XMLファイルとして、SVG画像は任意のテキストエディタで作成および編集できますが、Inkscapeのような描画プログラムで作成する方が便利です。

### PDFページをSVG画像に変換する

Aspose.PDF for Javaは、PDFファイルをSVG形式に変換する機能をサポートしています。
 この要件を達成するために、[SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) クラスが com.aspose.pdf パッケージに導入されました。[SvgSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SvgSaveOptions) のオブジェクトをインスタンス化し、[Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) メソッドの第2引数として渡します。

次のコードスニペットは、PDFファイルをSVG形式に変換する手順を示しています。

```java
package com.aspose.pdf.examples.conversion;

import com.aspose.pdf.Document;
import com.aspose.pdf.SvgSaveOptions;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * PDFをSVGに変換します。
 */
public class ConvertPDFtoSVG {
    // ドキュメントディレクトリへのパス。
    private static final Path DATA_DIR = Paths.get("/home/aspose/pdf-examples/Samples");

    private ConvertPDFtoSVG() {

    }

    public static void run() throws IOException {
        String pdfFileName = Paths.get(DATA_DIR.toString(), "input.pdf").toString();
        String svgFileName = Paths.get(DATA_DIR.toString(), "PDFToSVG_out.svg").toString();

        // PDFドキュメントを読み込む
        Document document = new Document(pdfFileName);

        // SvgSaveOptionsのオブジェクトをインスタンス化する
        SvgSaveOptions saveOptions = new SvgSaveOptions();

        // SVG画像をZipアーカイブに圧縮しない
        saveOptions.setCompressOutputToZipArchive(false);

        // 出力をSVGファイルに保存する
        document.save(svgFileName, saveOptions);
        document.close();
    }
}
```