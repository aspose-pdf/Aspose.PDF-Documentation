---
title: C#でPDFをさまざまな画像形式に変換する
linktitle: PDFを画像に変換
type: docs
weight: 70
url: /net/convert-pdf-to-images-format/
lastmod: "2021-11-01"
description: このトピックでは、Aspose.PDFを使用してPDFをTIFF、BMP、EMF、JPEG、PNG、GIF、SVGなどのさまざまな画像形式に変換する方法を説明します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 概要

この記事では、C#を使用してPDFを異なる画像形式に変換する方法について説明します。次のトピックをカバーしています。

_画像形式_: **TIFF**
- [C# PDFをTIFFに変換](#csharp-pdf-to-tiff)
- [C# PDFをTIFFに変換](#csharp-pdf-to-tiff)
- [C# PDFの単一ページまたは特定のページをTIFFに変換](#csharp-pdf-to-tiff-pages)

_画像形式_: **BMP**
- [C# PDFをBMPに変換](#csharp-pdf-to-bmp)
- [C# PDFをBMPに変換](#csharp-pdf-to-bmp)
- [C# PDFをBMPに変換するコンバーター](#csharp-pdf-to-bmp)

_画像形式_: **EMF**
- [C# PDFをEMFに変換](#csharp-pdf-to-emf)
- [C# PDFをEMFに変換](#csharp-pdf-to-emf)
- [C# PDFをEMFに変換するコンバーター](#csharp-pdf-to-emf)
 - [C# PDFをEMFに変換](#csharp-pdf-to-emf)


_画像形式_: **JPG**
- [C# PDFをJPGに変換](#csharp-pdf-to-jpg)
- [C# PDFをJPGに変換する](#csharp-pdf-to-jpg)
- [C# PDFをJPGコンバーター](#csharp-pdf-to-jpg)


_画像形式_: **PNG**
- [C# PDFをPNGに変換](#csharp-pdf-to-png)
- [C# PDFをPNGに変換する](#csharp-pdf-to-png)
- [C# PDFをPNGコンバーター](#csharp-pdf-to-png)


_画像形式_: **GIF**
- [C# PDFをGIFに変換](#csharp-pdf-to-gif)
- [C# PDFをGIFに変換する](#csharp-pdf-to-gif)
- [C# PDFをGIFコンバーター](#csharp-pdf-to-gif)

_画像形式_: **SVG**
- [C# PDFをSVGに変換](#csharp-pdf-to-svg)
- [C# PDFをSVGに変換する](#csharp-pdf-to-svg)
- [C# PDFをSVGコンバーター](#csharp-pdf-to-svg)

## C# PDFを画像に変換

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリでも機能します。

**Aspose.PDF for .NET** は、いくつかのアプローチを使用してPDFを画像に変換します。
**Aspose.PDF for .NET** は、PDFを画像に変換するためにいくつかのアプローチを使用しています。

このライブラリには、仮想デバイスを使用して画像を変換することを可能にするいくつかのクラスがあります。DocumentDeviceは文書全体の変換向けですが、ImageDeviceは特定のページ向けです。

## DocumentDevice クラスを使用してPDFを変換する

**Aspose.PDF for .NET** は、PDFページをTIFF画像に変換することを可能にします。

TiffDevice（DocumentDeviceに基づく）クラスは、PDFページをTIFF画像に変換することを可能にします。このクラスは `Process` というメソッドを提供しており、PDFファイルのすべてのページを単一のTIFF画像に変換することができます。

{{% alert color="success" %}}
**オンラインでPDFをTIFFに変換してみる**

Aspose.PDF for .NETは、無料のオンラインアプリケーション ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff) を提供しており、その機能と品質を試すことができます。

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}
{{% /alert %}}

### PDFページを1つのTIFFイメージに変換する

Aspose.PDF for .NETについて、PDFファイル内の全ページを単一のTIFFイメージに変換する方法を説明します:

<a name="csharp-pdf-to-tiff"><strong>手順: C#でPDFをTIFFに変換する</strong></a>

1. **Document** クラスのオブジェクトを作成します。
2. **TiffSettings** と **TiffDevice** オブジェクトを作成します
3. PDFドキュメントをTIFFに変換するために **TiffDevice.Process()** メソッドを呼び出します。
4. 出力ファイルのプロパティを設定するために **TiffSettings** クラスを使用します。

以下のコードスニペットは、PDFの全ページを単一のTIFFイメージに変換する方法を示しています。

```csharp
public static void ConvertPDFtoTIFF()
{
    // 文書を開く
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // Resolutionオブジェクトを作成
    Resolution resolution = new Resolution(300);

    // TiffSettingsオブジェクトを作成
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
        SkipBlankPages = false
    };

    // TIFFデバイスを作成
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // 特定のページを変換し、イメージをストリームに保存
    tiffDevice.Process(pdfDocument, _dataDir + "AllPagesToTIFF_out.tif");
}
```
### PDFの1ページをTIFF画像に変換

Aspose.PDF for .NETは、PDFファイルの特定のページをTIFF画像に変換することができます。変換のためのページ番号を引数として取るProcess(..)メソッドのオーバーロード版を使用します。次のコードスニペットは、PDFの最初のページをTIFF形式に変換する方法を示しています。

<a name="csharp-pdf-to-tiff-pages"><strong>手順: C#でPDFの単一または特定のページをTIFFに変換</strong></a>

1. **Document** クラスのオブジェクトを作成します。
2. **TiffSettings** と **TiffDevice** オブジェクトを作成します
3. **TiffDevice.Process()** メソッドのオーバーロードを **fromPage** と **toPage** パラメーターで呼び出し、PDFドキュメントのページをTIFFに変換します。

```csharp
public static void ConvertPDFtoTiffSinglePage()
{
    // ドキュメントを開く
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // Resolutionオブジェクトを作成
    Resolution resolution = new Resolution(300);

    // TiffSettingsオブジェクトを作成
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
    };

    // TIFFデバイスを作成
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // 特定のページを変換してイメージをストリームに保存
    tiffDevice.Process(pdfDocument, 1, 1, _dataDir + "PageToTIFF_out.tif");
}
```
### Bradleyアルゴリズムを変換中に使用する

Aspose.PDF for .NETは、LZW圧縮を使用してPDFをTIFに変換する機能をサポートしており、AForgeを使用して2値化を適用できます。しかし、顧客の一人が画像に対してOtsuを使用してしきい値を取得する必要があるため、Bradleyの使用も希望しています。

```csharp
  public static void ConvertPDFtoTiffBradleyBinarization()
{
     // ドキュメントを開く
     Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    string outputImageFile = _dataDir + "resultant_out.tif";
    string outputBinImageFile = _dataDir + "37116-bin_out.tif";

    // Resolutionオブジェクトを作成する
    Resolution resolution = new Resolution(300);
    // TiffSettingsオブジェクトを作成する
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.LZW,
        Depth = Aspose.Pdf.Devices.ColorDepth.Format1bpp
    };
    // TIFFデバイスを作成する
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
    // 特定のページを変換して画像をストリームに保存する
    tiffDevice.Process(pdfDocument, outputImageFile);

    using (FileStream inStream = new FileStream(outputImageFile, FileMode.Open))
    {
        using (FileStream outStream = new FileStream(outputBinImageFile, FileMode.Create))
        {
            tiffDevice.BinarizeBradley(inStream, outStream, 0.1);
        }
    }
} 
```
## ImageDevice クラスを使用して PDF を変換する

`ImageDevice` は `BmpDevice`、`JpegDevice`、`GifDevice`、`PngDevice`、`EmfDevice` の祖先です。

- [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) クラスは、PDF ページを <abbr title="Bitmap Image File">BMP</abbr> 画像に変換することができます。
- [EmfDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/emfdevice) クラスは、PDF ページを <abbr title="Enhanced Meta File">EMF</abbr> 画像に変換することができます。
- [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) クラスは、PDF ページを JPEG 画像に変換することができます。
- [PngDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/pngdevice) クラスは、PDF ページを <abbr title="Portable Network Graphics">PNG</abbr> 画像に変換することができます。
- [GifDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/gifdevice) クラスは、PDF ページを <abbr title="Graphics Interchange Format">GIF</abbr> 画像に変換することができます。

PDF ページを画像に変換する方法を見てみましょう。
PDFページを画像に変換する方法を見てみましょう。

`BmpDevice` クラスは、PDFファイルの特定のページをBMP画像形式に変換するためのメソッド [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) を提供しています。他のクラスも同じメソッドを持っています。したがって、PDFページを画像に変換する必要がある場合は、必要なクラスをインスタンス化するだけです。

<a name="csharp-pdf-to-bmp"></a>
<a name="csharp-pdf-to-emf"></a>
<a name="csharp-pdf-to-jpg"></a>
<a name="csharp-pdf-to-png"></a>
<a name="csharp-pdf-to-gif"></a>

次の手順とC#のコードスニペットでこの可能性を示します

 - [C#でPDFをBMPに変換](#csharp-pdf-to-image)
 - [C#でPDFをEMFに変換](#csharp-pdf-to-image)
 - [C#でPDFをJPGに変換](#csharp-pdf-to-image)
 - [C#でPDFをPNGに変換](#csharp-pdf-to-image)
 - [C#でPDFをGIFに変換](#csharp-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>手順: C#でPDFから画像(BMP, EMF, JPG, PNG, GIF)への変換</strong></a>

1.
1.
2. **ImageDevice** のサブクラスのインスタンスを作成します。
   * **BmpDevice** (PDFをBMPに変換するため)
   * **EmfDevice** (PDFをEmfに変換するため)
   * **JpegDevice** (PDFをJPGに変換するため)
   * **PngDevice** (PDFをPNGに変換するため)
   * **GifDevice** (PDFをGIFに変換するため)
3. PDFから画像への変換を実行するために **ImageDevice.Process()** メソッドを呼び出します。

```csharp
public static class ExampleConvertPdfToImage
{
     private static readonly string _dataDir = @"C:\Samples\";
    // BMP, JPEG, GIF, PNG, EMF
    public static void ConvertPDFusingImageDevice()
    {
        // 解像度オブジェクトを作成            
        Resolution resolution = new Resolution(300);
        BmpDevice bmpDevice = new BmpDevice(resolution);
        JpegDevice jpegDevice = new JpegDevice(resolution);
        GifDevice gifDevice = new GifDevice(resolution);
        PngDevice pngDevice = new PngDevice(resolution);
        EmfDevice emfDevice = new EmfDevice(resolution);

        Document document = new Document(_dataDir + 
            "ConvertAllPagesToBmp.pdf");
            
        ConvertPDFtoImage(bmpDevice, "bmp", document);
        ConvertPDFtoImage(jpegDevice,"jpeg", document);
        ConvertPDFtoImage(gifDevice, "gif", document);
        ConvertPDFtoImage(pngDevice, "png", document);
        ConvertPDFtoImage(emfDevice, "emf", document);
            
    }
}

public static void ConvertPDFtoImage(ImageDevice imageDevice, 
        string ext, Document pdfDocument)
{
    for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
    {
        using (FileStream imageStream = 
        new FileStream($"{_dataDir}image{pageCount}_out.{ext}", 
        FileMode.Create))
        {
            // 特定のページを変換して画像をストリームに保存
            imageDevice.Process(pdfDocument.Pages[pageCount], imageStream);

            // ストリームを閉じる
            imageStream.Close();
        }
    }
}
```
{{% alert color="success" %}}
**PDFをオンラインでPNGに変換してみてください**

無料アプリケーションがどのように機能するかの例として、次の機能をご覧ください。

Aspose.PDF for .NETは、無料のオンラインアプリケーション ["PDFをPNGに"](https://products.aspose.app/pdf/conversion/pdf-to-png) 提供しており、その機能や品質を調査することができます。

[![無料アプリを使用してPDFをPNGに変換する方法](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## SaveOptionsクラスを使用してPDFを変換

この記事の部分では、C#とSaveOptionsクラスを使用してPDFを<abbr title="Scalable Vector Graphics">SVG</abbr>に変換する方法を示しています。

{{% alert color="success" %}}
**PDFをオンラインでSVGに変換してみてください**

Aspose.PDF for .NETは、無料のオンラインアプリケーション ["PDFをSVGに"](https://products.aspose.app/pdf/conversion/pdf-to-svg) 提供しており、その機能や品質を調査することができます。

[![Aspose.PDF 変換 PDFをSVGに無料アプリで](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
[![Aspose.PDF 変換 PDFからSVGへ 無料アプリ](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**スケーラブルベクターグラフィックス (SVG)** は、静的および動的（インタラクティブまたはアニメーション）の二次元ベクターグラフィックスのためのXMLベースのファイル形式の仕様ファミリーです。SVG仕様は、1999年からWorld Wide Web Consortium (W3C)によって開発が進められているオープンスタンダードです。

SVG画像とその振る舞いは、XMLテキストファイルで定義されます。これは、検索、インデックス作成、スクリプト化、必要に応じて圧縮が可能であることを意味します。XMLファイルとして、SVG画像は任意のテキストエディタで作成および編集できますが、Inkscapeのようなドロープログラムで作成する方が便利な場合が多いです。

Aspose.PDF for .NETは、SVG画像をPDF形式に変換する機能をサポートしており、PDFファイルをSVG形式に変換する機能も提供しています。
Aspose.PDF for .NETは、SVGイメージをPDF形式に変換する機能をサポートしており、PDFファイルをSVG形式に変換する機能も提供しています。

次のコードスニペットは、.NETでPDFファイルをSVG形式に変換する手順を示しています。

<a name="csharp-pdf-to-svg"><strong>手順: C#でPDFをSVGに変換</strong></a>

1. **Document** クラスのオブジェクトを作成します。
2. 必要な設定で **SvgSaveOptions** オブジェクトを作成します。
3. **Document.Save()** メソッドを呼び出し、PDFドキュメントをSVGに変換するために **SvgSaveOptions** オブジェクトを渡します。

```csharp
public static void ConvertPDFtoSVG()
{
    // PDFドキュメントをロード
    Document document = new Document(System.IO.Path.Combine(_dataDir, "input.pdf"));
    // SvgSaveOptionsのオブジェクトをインスタンス化
    SvgSaveOptions saveOptions = new SvgSaveOptions
    {
        // SVGイメージをZipアーカイブに圧縮しない
        CompressOutputToZipArchive = false,
        TreatTargetFileNameAsDirectory = true                
    };
            
    // 出力をSVGファイルで保存
    document.Save(System.IO.Path.Combine(_dataDir, "PDFToSVG_out.svg"), saveOptions);
}
```

