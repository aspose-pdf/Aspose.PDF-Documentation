---
title: PDFをC#で異なる画像形式に変換
linktitle: PDFを画像に変換
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ja/net/convert-pdf-to-images-format/
lastmod: "2021-11-01"
description: このトピックでは、Aspose.PDFを使用してPDFをTIFF、BMP、EMF、JPEG、PNG、GIF、SVGなどのさまざまな画像形式に変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Different Image Formats in C#",
    "alternativeHeadline": "Convert PDF Files to Multiple Image Formats in C#",
    "abstract": "Aspose.PDF for .NETの機能により、ユーザーはPDFファイルをTIFF、BMP、EMF、JPEG、PNG、GIF、SVGなどの複数の画像形式にシームレスに変換できます。この機能は、C#の数行のコードで変換を可能にすることで文書の取り扱いを簡素化し、汎用的なPDF処理機能をアプリケーションに追加したい開発者にとって不可欠なツールとなります。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1635",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/convert-pdf-to-images-format/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-images-format/"
    },
    "dateModified": "2025-04-09",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーや開発者向けの情報を確認してください。"
}
</script>

## 概要

この記事では、C#を使用してPDFを異なる画像形式に変換する方法を説明します。以下のトピックをカバーしています。

- [PDFをTIFFに変換](#csharp-pdf-to-tiff)
- [PDFをBMPに変換](#csharp-pdf-to-bmp)
- [PDFをEMFに変換](#csharp-pdf-to-emf)
- [PDFをJPGに変換](#csharp-pdf-to-jpg)
- [PDFをPNGに変換](#csharp-pdf-to-png)
- [PDFをGIFに変換](#csharp-pdf-to-gif)
- [PDFをSVGに変換](#csharp-pdf-to-svg)

## C# PDFを画像に変換

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

**Aspose.PDF for .NET**は、PDFを画像に変換するためのいくつかのアプローチを使用します。一般的に、デバイスアプローチを使用した変換とSaveOptionを使用した変換の2つのアプローチを使用します。このセクションでは、これらのアプローチのいずれかを使用して、PDF文書をBMP、JPEG、GIF、PNG、EMF、TIFF、SVG形式の画像に変換する方法を示します。

ライブラリには、画像を変換するための仮想デバイスを使用できるいくつかのクラスがあります。DocumentDeviceは文書全体の変換に向いていますが、ImageDeviceは特定のページに向いています。

## DocumentDeviceクラスを使用してPDFを変換

**Aspose.PDF for .NET**は、PDFページをTIFF画像に変換することを可能にします。

TiffDevice（DocumentDeviceに基づく）クラスは、PDFページをTIFF画像に変換することを可能にします。このクラスは、PDFファイル内のすべてのページを単一のTIFF画像に変換するための`Process`というメソッドを提供します。

{{% alert color="success" %}}
**オンラインでPDFをTIFFに変換してみてください**

Aspose.PDF for .NETは、機能と品質を調査できるオンライン無料アプリケーション["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)を提供します。

[![Aspose.PDF PDFをTIFFに変換する無料アプリ](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### PDFページを1つのTIFF画像に変換

Aspose.PDF for .NETは、PDFファイル内のすべてのページを単一のTIFF画像に変換する方法を説明します：

<a name="csharp-pdf-to-tiff"><strong>PDFをTIFFに変換</strong></a>

1. **Document**クラスのオブジェクトを作成します。
2. **TiffSettings**および**TiffDevice**オブジェクトを作成します。
3. **TiffDevice.Process()**メソッドを呼び出して、PDF文書をTIFFに変換します。
4. 出力ファイルのプロパティを設定するには、**TiffSettings**クラスを使用します。

以下のコードスニペットは、すべてのPDFページを単一のTIFF画像に変換する方法を示しています。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTIFF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFtoTIFF.pdf"))
    {
        // Create Resolution object
        var resolution = new Aspose.Pdf.Devices.Resolution(300);

        // Create TiffSettings object
        var tiffSettings = new Aspose.Pdf.Devices.TiffSettings
        {
            Compression = Aspose.Pdf.Devices.CompressionType.None,
            Depth = Aspose.Pdf.Devices.ColorDepth.Default,
            Shape = Aspose.Pdf.Devices.ShapeType.Landscape,
            SkipBlankPages = false
        };

        // Create TIFF device
        var tiffDevice = new Aspose.Pdf.Devices.TiffDevice(resolution, tiffSettings);

        // Convert a particular page and save the image to stream
        tiffDevice.Process(document, dataDir + "PDFtoTIFF_out.tif");
    }
}
```

### 1ページをTIFF画像に変換

Aspose.PDF for .NETは、PDFファイル内の特定のページをTIFF画像に変換することを可能にします。変換のためにページ番号を引数として受け取るProcess(..)メソッドのオーバーロード版を使用します。以下のコードスニペットは、PDFの最初のページをTIFF形式に変換する方法を示しています。

1. **Document**クラスのオブジェクトを作成します。
2. **TiffSettings**および**TiffDevice**オブジェクトを作成します。
3. **fromPage**および**toPage**パラメータを使用してオーバーロードされた**TiffDevice.Process()**メソッドを呼び出し、PDF文書のページをTIFFに変換します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTiffSinglePage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFtoTiffSinglePage.pdf"))
    {
        // Create Resolution object
        var resolution = new Aspose.Pdf.Devices.Resolution(300);

        // Create TiffSettings object
        var tiffSettings = new Aspose.Pdf.Devices.TiffSettings
        {
            Compression = Aspose.Pdf.Devices.CompressionType.None,
            Depth = Aspose.Pdf.Devices.ColorDepth.Default,
            Shape = Aspose.Pdf.Devices.ShapeType.Landscape,
        };

        // Create TIFF device
        var tiffDevice = new Aspose.Pdf.Devices.TiffDevice(resolution, tiffSettings);

        // Convert a particular page and save the image to stream
        tiffDevice.Process(document, 1, 1, dataDir + "PDFtoTiffSinglePage_out.tif");
    }
}
```

### 変換中にブラッドリーアルゴリズムを使用

Aspose.PDF for .NETは、LZW圧縮を使用してPDFをTIFに変換する機能をサポートしており、その後AForgeを使用して二値化を適用できます。ただし、顧客の1人が特定の画像について、Otsuを使用してしきい値を取得する必要があるため、ブラッドリーも使用したいとリクエストしました。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoTiffBradleyBinarization()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFtoTiffBradleyBinarization.pdf"))
    {
        string outputImageFile = dataDir + "PDFtoTiffBradleyBinarization_out.tif";
        string outputBinImageFile = dataDir + "PDFtoTiffBradleyBinarization-bin_out.tif";

        // Create Resolution object
        var resolution = new Aspose.Pdf.Devices.Resolution(300);

        // Create TiffSettings object
        var tiffSettings = new Aspose.Pdf.Devices.TiffSettings
        {
            Compression = Aspose.Pdf.Devices.CompressionType.LZW,
            Depth = Aspose.Pdf.Devices.ColorDepth.Format1bpp
        };

        // Create TIFF device
        var tiffDevice = new Aspose.Pdf.Devices.TiffDevice(resolution, tiffSettings);

        // Convert a particular page and save the image to stream
        tiffDevice.Process(document, outputImageFile);

        // Binarize the image using Bradley method
        using (var inStream = new FileStream(outputImageFile, FileMode.Open))
        {
            using (var outStream = new FileStream(outputBinImageFile, FileMode.Create))
            {
                tiffDevice.BinarizeBradley(inStream, outStream, 0.1);
            }
        }
    }
}
```

## ImageDeviceクラスを使用してPDFを変換

`ImageDevice`は`BmpDevice`、`JpegDevice`、`GifDevice`、`PngDevice`、`EmfDevice`の祖先です。

- [BmpDevice](https://reference.aspose.com/pdf/ja/net/aspose.pdf.devices/bmpdevice)クラスは、PDFページを<abbr title="Bitmap Image File">BMP</abbr>画像に変換することを可能にします。
- [EmfDevice](https://reference.aspose.com/pdf/ja/net/aspose.pdf.devices/emfdevice)クラスは、PDFページを<abbr title="Enhanced Meta File">EMF</abbr>画像に変換することを可能にします。
- [JpegDevice](https://reference.aspose.com/pdf/ja/net/aspose.pdf.devices/jpegdevice)クラスは、PDFページをJPEG画像に変換することを可能にします。
- [PngDevice](https://reference.aspose.com/pdf/ja/net/aspose.pdf.devices/pngdevice)クラスは、PDFページを<abbr title="Portable Network Graphics">PNG</abbr>画像に変換することを可能にします。
- [GifDevice](https://reference.aspose.com/pdf/ja/net/aspose.pdf.devices/gifdevice)クラスは、PDFページを<abbr title="Graphics Interchange Format">GIF</abbr>画像に変換することを可能にします。

PDFページを画像に変換する方法を見てみましょう。

`BmpDevice`クラスは、PDFファイルの特定のページをBMP画像形式に変換するための[Process](https://reference.aspose.com/pdf/ja/net/aspose.pdf.devices/bmpdevice/methods/process)というメソッドを提供します。他のクラスも同じメソッドを持っています。したがって、PDFページを画像に変換する必要がある場合は、必要なクラスをインスタンス化するだけです。

<a name="csharp-pdf-to-bmp"></a>
<a name="csharp-pdf-to-emf"></a>
<a name="csharp-pdf-to-jpg"></a>
<a name="csharp-pdf-to-png"></a>
<a name="csharp-pdf-to-gif"></a>

1. **Document**クラスを使用してPDFファイルを読み込みます。
2. **ImageDevice**のサブクラスのインスタンスを作成します。
   * **BmpDevice**（PDFをBMPに変換するため）。
   * **EmfDevice**（PDFをEmfに変換するため）。
   * **JpegDevice**（PDFをJPGに変換するため）。
   * **PngDevice**（PDFをPNGに変換するため）。
   * **GifDevice**（PDFをGIFに変換するため）。
3. **ImageDevice.Process()**メソッドを呼び出してPDFから画像への変換を実行します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFusingImageDevice()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create Resolution object            
    var resolution = new Aspose.Pdf.Devices.Resolution(300);
    var bmpDevice = new Aspose.Pdf.Devices.BmpDevice(resolution);
    var jpegDevice = new Aspose.Pdf.Devices.JpegDevice(resolution);
    var gifDevice = new Aspose.Pdf.Devices.GifDevice(resolution);
    var pngDevice = new Aspose.Pdf.Devices.PngDevice(resolution);
    var emfDevice = new Aspose.Pdf.Devices.EmfDevice(resolution);

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertAllPagesToBmp.pdf"))
    {
        ConvertPDFtoImage(bmpDevice, "bmp", document, dataDir);
        ConvertPDFtoImage(jpegDevice, "jpeg", document, dataDir);
        ConvertPDFtoImage(gifDevice, "gif", document, dataDir);
        ConvertPDFtoImage(pngDevice, "png", document, dataDir);
        ConvertPDFtoImage(emfDevice, "emf", document, dataDir);
    }
}

private static void ConvertPDFtoImage(ImageDevice imageDevice,
        string ext, Document document, var dataDir)
{
    for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
    {
        using (FileStream imageStream =
            new FileStream($"{dataDir}image{pageCount}_out.{ext}",
            FileMode.Create))
        {
            // Convert a particular page and save the image to stream
            imageDevice.Process(document.Pages[pageCount], imageStream);
        }
    }
}
```

### 透明な背景でPDFを画像に変換

PDFページは、白い背景の代わりに透明な背景を持つPNG画像に変換できます。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoImageWithTransparentBackground()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertPDFtoImageWithTransparentBackground.pdf"))
    {
        var pngDevice = new Aspose.Pdf.Devices.PngDevice();
        pngDevice.TransparentBackground = true;
        using (var pngStream = new FileStream(dataDir + "ConvertPDFtoImageWithTransparentBackground.png", FileMode.Create))
        {
            // Convert page to PNG image
            pngDevice.Process(document.Pages[1], pngStream);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoImageWithTransparentBackground()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "ConvertPDFtoImageWithTransparentBackground.pdf");
    var pngDevice = new Aspose.Pdf.Devices.PngDevice()
    {
        TransparentBackground = true
    };
    using var pngStream = new FileStream(dataDir + "ConvertPDFtoImageWithTransparentBackground.png", FileMode.Create);
    // Convert page to PNG image
    pngDevice.Process(document.Pages[1], pngStream);
}
```
{{< /tab >}}
{{< /tabs >}}

### 特定のページ領域を画像に変換

ページの特定の領域をCropBoxを使用して画像に変換できます。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertParticularPageRegionToImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ConvertParticularPageRegionToImage.pdf"))
    {
        // Get rectangle of particular XImage
        var imagePlacementAbsorber = new Aspose.Pdf.ImagePlacementAbsorber();
        document.Pages[1].Accept(imagePlacementAbsorber);
        var imageRectangle = imagePlacementAbsorber.ImagePlacements[1].Rectangle;
        var pageRect = new Aspose.Pdf.Rectangle(imageRectangle.LLX, imageRectangle.LLY, imageRectangle.URX, imageRectangle.URY);

        // Set CropBox value as per rectangle of desired page region
        document.Pages[1].CropBox = pageRect;
        var resolution = new Aspose.Pdf.Devices.Resolution(300);

        // Create PNG device with specified attributes
        var pngDevice = new Aspose.Pdf.Devices.PngDevice(resolution);

        // Convert a particular page and save the image
        pngDevice.Process(document.Pages[1], dataDir + "ConvertParticularPageRegionToImage_out.png");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertParticularPageRegionToImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "ConvertParticularPageRegionToImage.pdf");
    // Get rectangle of particular XImage
    var imagePlacementAbsorber = new Aspose.Pdf.ImagePlacementAbsorber();
    document.Pages[1].Accept(imagePlacementAbsorber);
    var imageRectangle = imagePlacementAbsorber.ImagePlacements[1].Rectangle;
    var pageRect = new Aspose.Pdf.Rectangle(imageRectangle.LLX, imageRectangle.LLY, imageRectangle.URX, imageRectangle.URY);

    // Set CropBox value as per rectangle of desired page region
    document.Pages[1].CropBox = pageRect;
    var resolution = new Aspose.Pdf.Devices.Resolution(300);

    // Create PNG device with specified attributes
    var pngDevice = new Aspose.Pdf.Devices.PngDevice(resolution);

    // Convert a particular page and save the image
    pngDevice.Process(document.Pages[1], dataDir + "ConvertParticularPageRegionToImage_out.png");
}
```
{{< /tab >}}
{{< /tabs >}}

{{% alert color="success" %}}
**オンラインでPDFをPNGに変換してみてください**

私たちの無料アプリケーションがどのように機能するかの例として、次の機能を確認してください。

Aspose.PDF for .NETは、機能と品質を調査できるオンライン無料アプリケーション["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)を提供します。

[![無料アプリを使用してPDFをPNGに変換する方法](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## SaveOptionsクラスを使用してPDFを変換

この記事のこの部分では、C#とSaveOptionsクラスを使用してPDFを<abbr title="Scalable Vector Graphics">SVG</abbr>に変換する方法を示します。

{{% alert color="success" %}}
**オンラインでPDFをSVGに変換してみてください**

Aspose.PDF for .NETは、機能と品質を調査できるオンライン無料アプリケーション["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)を提供します。

[![Aspose.PDF PDFをSVGに変換する無料アプリ](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**スケーラブルベクターグラフィックス（SVG）**は、静的および動的（インタラクティブまたはアニメーション）の2次元ベクターグラフィックス用のXMLベースのファイル形式の仕様のファミリーです。SVG仕様は、1999年からWorld Wide Web Consortium（W3C）によって開発されているオープンスタンダードです。

SVG画像とその動作はXMLテキストファイルで定義されています。これは、検索、インデックス作成、スクリプト化、必要に応じて圧縮できることを意味します。XMLファイルとして、SVG画像は任意のテキストエディタで作成および編集できますが、Inkscapeなどの描画プログラムを使用して作成する方が便利です。

Aspose.PDF for .NETは、SVG画像をPDF形式に変換する機能をサポートし、PDFファイルをSVG形式に変換する機能も提供します。この要件を達成するために、[`SvgSaveOptions`](https://reference.aspose.com/pdf/ja/net/aspose.pdf/svgsaveoptions/methods/index)クラスがAspose.PDF名前空間に導入されました。SvgSaveOptionsのオブジェクトをインスタンス化し、[`Document.Save(..)`](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document/methods/save/index)メソッドの第2引数として渡します。

以下のコードスニペットは、.NETを使用してPDFファイルをSVG形式に変換する手順を示しています。

<a name="csharp-pdf-to-svg"><strong>PDFをSVGに変換</strong></a>

1. **Document**クラスのオブジェクトを作成します。
2. 必要な設定で**SvgSaveOptions**オブジェクトを作成します。
3. **Document.Save()**メソッドを呼び出し、**SvgSaveOptions**オブジェクトを渡してPDF文書をSVGに変換します。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoSVG()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFtoSVG.pdf"))
    {
        // Instantiate an object of SvgSaveOptions
        var saveOptions = new Aspose.Pdf.SvgSaveOptions
        {
            // Do not compress SVG image to Zip archive
            CompressOutputToZipArchive = false,
            TreatTargetFileNameAsDirectory = true                
        };

        // Save SVG file
        document.Save(dataDir + "PDFToSVG_out.svg", saveOptions);
    }
}
```