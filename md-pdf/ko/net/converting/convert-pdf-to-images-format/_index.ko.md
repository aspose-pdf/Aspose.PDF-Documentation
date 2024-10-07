---
title: C#에서 PDF를 다양한 이미지 형식으로 변환
linktitle: PDF를 이미지로 변환
type: docs
weight: 70
url: /net/convert-pdf-to-images-format/
lastmod: "2021-11-01"
description: 이 주제는 몇 줄의 코드로 Aspose.PDF를 사용하여 PDF를 TIFF, BMP, EMF, JPEG, PNG, GIF, SVG 등 다양한 이미지 형식으로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 개요

이 글은 C#을 사용하여 PDF를 다양한 이미지 형식으로 변환하는 방법을 설명합니다. 다음 주제를 다룹니다.

_이미지 형식_: **TIFF**
- [C# PDF를 TIFF로](#csharp-pdf-to-tiff)
- [C# PDF를 TIFF로 변환](#csharp-pdf-to-tiff)
- [C# PDF의 단일 또는 특정 페이지를 TIFF로 변환](#csharp-pdf-to-tiff-pages)

_이미지 형식_: **BMP**
- [C# PDF를 BMP로](#csharp-pdf-to-bmp)
- [C# PDF를 BMP로 변환](#csharp-pdf-to-bmp)
- [C# PDF를 BMP로 변환하는 변환기](#csharp-pdf-to-bmp)

_이미지 형식_: **EMF**
- [C# PDF를 EMF로](#csharp-pdf-to-emf)
- [C# PDF를 EMF로 변환](#csharp-pdf-to-emf)
- [C# PDF를 EMF로 변환하는 변환기](#csharp-pdf-to-emf)
- [C# PDF를 EMF로 변환](#csharp-pdf-to-emf)

_이미지 형식_: **JPG**
- [C# PDF를 JPG로 변환](#csharp-pdf-to-jpg)
- [C# PDF를 JPG로 변환](#csharp-pdf-to-jpg)
- [C# PDF를 JPG로 변환하는 변환기](#csharp-pdf-to-jpg)

_이미지 형식_: **PNG**
- [C# PDF를 PNG로 변환](#csharp-pdf-to-png)
- [C# PDF를 PNG로 변환](#csharp-pdf-to-png)
- [C# PDF를 PNG로 변환하는 변환기](#csharp-pdf-to-png)

_이미지 형식_: **GIF**
- [C# PDF를 GIF로 변환](#csharp-pdf-to-gif)
- [C# PDF를 GIF로 변환](#csharp-pdf-to-gif)
- [C# PDF를 GIF로 변환하는 변환기](#csharp-pdf-to-gif)

_이미지 형식_: **SVG**
- [C# PDF를 SVG로 변환](#csharp-pdf-to-svg)
- [C# PDF를 SVG로 변환](#csharp-pdf-to-svg)
- [C# PDF를 SVG로 변환하는 변환기](#csharp-pdf-to-svg)

## C# PDF를 이미지로 변환

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리에서도 작동합니다.

**Aspose.PDF for .NET**은 PDF를 이미지로 변환하기 위해 여러 접근 방식을 사용합니다.
**Aspose.PDF for .NET**은 PDF를 이미지로 변환하기 위해 여러 가지 접근 방식을 사용합니다.

라이브러리에는 가상 장치를 사용하여 이미지를 변환할 수 있는 여러 클래스가 있습니다. DocumentDevice는 전체 문서의 변환을 위해, ImageDevice는 특정 페이지를 위해 사용됩니다.

## DocumentDevice 클래스를 사용하여 PDF 변환

**Aspose.PDF for .NET**은 PDF 페이지를 TIFF 이미지로 변환할 수 있습니다.

TiffDevice( DocumentDevice 기반) 클래스는 PDF 페이지를 TIFF 이미지로 변환할 수 있습니다. 이 클래스는 PDF 파일의 모든 페이지를 단일 TIFF 이미지로 변환할 수 있는 `Process`라는 메서드를 제공합니다.

{{% alert color="success" %}}
**PDF를 TIFF로 온라인으로 변환해 보세요**

Aspose.PDF for .NET은 기능과 품질을 조사해 볼 수 있는 무료 온라인 애플리케이션 ["PDF to TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff)을 제공합니다.

[![Aspose.PDF conversion PDF to TIFF with Free App](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}
{{% /alert %}}

### PDF 페이지를 하나의 TIFF 이미지로 변환

Aspose.PDF for .NET은 PDF 파일의 모든 페이지를 단일 TIFF 이미지로 변환하는 방법을 설명합니다:

<a name="csharp-pdf-to-tiff"><strong>단계: C#에서 PDF를 TIFF로 변환</strong></a>

1. **Document** 클래스의 객체를 생성합니다.
2. **TiffSettings** 및 **TiffDevice** 객체를 생성합니다.
3. PDF 문서를 TIFF로 변환하려면 **TiffDevice.Process()** 메소드를 호출합니다.
4. 출력 파일의 속성을 설정하려면 **TiffSettings** 클래스를 사용합니다.

다음 코드 스니펫은 모든 PDF 페이지를 단일 TIFF 이미지로 변환하는 방법을 보여줍니다.

```csharp
public static void ConvertPDFtoTIFF()
{
    // 문서 열기
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // Resolution 객체 생성
    Resolution resolution = new Resolution(300);

    // TiffSettings 객체 생성
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
        SkipBlankPages = false
    };

    // TIFF 장치 생성
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // 특정 페이지를 변환하고 이미지를 스트림에 저장
    tiffDevice.Process(pdfDocument, _dataDir + "AllPagesToTIFF_out.tif");
}
```
### 한 페이지를 TIFF 이미지로 변환

Aspose.PDF for .NET은 PDF 파일의 특정 페이지를 TIFF 이미지로 변환할 수 있습니다. 페이지 번호를 인수로 사용하는 Process(..) 메소드의 오버로드된 버전을 사용하십시오. 다음 코드 스니펫은 PDF의 첫 페이지를 TIFF 형식으로 변환하는 방법을 보여줍니다.

<a name="csharp-pdf-to-tiff-pages"><strong>단계: C#에서 PDF의 단일 또는 특정 페이지를 TIFF로 변환</strong></a>

1. **Document** 클래스의 객체를 생성합니다.
2. **TiffSettings** 및 **TiffDevice** 객체를 생성합니다.
3. **fromPage** 및 **toPage** 매개변수와 함께 오버로드된 **TiffDevice.Process()** 메소드를 호출하여 PDF 문서 페이지를 TIFF로 변환합니다.

```csharp
public static void ConvertPDFtoTiffSinglePage()
{
    // 문서 열기
    Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    // 해상도 객체 생성
    Resolution resolution = new Resolution(300);

    // TiffSettings 객체 생성
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.None,
        Depth = ColorDepth.Default,
        Shape = ShapeType.Landscape,
    };

    // TIFF 장치 생성
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);

    // 특정 페이지를 변환하고 이미지를 스트림에 저장
    tiffDevice.Process(pdfDocument, 1, 1, _dataDir + "PageToTIFF_out.tif");
}
```
### 변환 시 브래들리 알고리즘 사용하기

Aspose.PDF for .NET은 LZW 압축을 사용하여 PDF를 TIF로 변환하는 기능을 지원하며, AForge를 사용하여 이진화를 적용할 수 있습니다. 그러나 일부 고객은 특정 이미지에 대해 Otsu를 사용하여 임계값을 얻어야 하므로 브래들리 사용도 원한다고 요청했습니다.

```csharp
  public static void ConvertPDFtoTiffBradleyBinarization()
{
     // 문서 열기
     Document pdfDocument = new Document(_dataDir + "PageToTIFF.pdf");

    string outputImageFile = _dataDir + "resultant_out.tif";
    string outputBinImageFile = _dataDir + "37116-bin_out.tif";

    // 해상도 객체 생성
    Resolution resolution = new Resolution(300);
    // Tiff 설정 객체 생성
    TiffSettings tiffSettings = new TiffSettings
    {
        Compression = CompressionType.LZW,
        Depth = Aspose.Pdf.Devices.ColorDepth.Format1bpp
    };
    // TIFF 장치 생성
    TiffDevice tiffDevice = new TiffDevice(resolution, tiffSettings);
    // 특정 페이지를 변환하고 이미지를 스트림에 저장
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
## ImageDevice 클래스를 사용하여 PDF 변환

`ImageDevice`는 `BmpDevice`, `JpegDevice`, `GifDevice`, `PngDevice`, `EmfDevice`의 상위 클래스입니다.

- [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) 클래스는 PDF 페이지를 <abbr title="Bitmap Image File">BMP</abbr> 이미지로 변환할 수 있습니다.
- [EmfDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/emfdevice) 클래스는 PDF 페이지를 <abbr title="Enhanced Meta File">EMF</abbr> 이미지로 변환할 수 있습니다.
- [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) 클래스는 PDF 페이지를 JPEG 이미지로 변환할 수 있습니다.
- [PngDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/pngdevice) 클래스는 PDF 페이지를 <abbr title="Portable Network Graphics">PNG</abbr> 이미지로 변환할 수 있습니다.
- [GifDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/gifdevice) 클래스는 PDF 페이지를 <abbr title="Graphics Interchange Format">GIF</abbr> 이미지로 변환할 수 있습니다.

PDF 페이지를 이미지로 변환하는 방법을 살펴보겠습니다.
PDF 페이지를 이미지로 변환하는 방법을 살펴보겠습니다.

`BmpDevice` 클래스는 PDF 파일의 특정 페이지를 BMP 이미지 형식으로 변환할 수 있는 [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process)라는 메소드를 제공합니다. 다른 클래스도 같은 메소드를 가지고 있습니다. 따라서 PDF 페이지를 이미지로 변환해야 하는 경우, 필요한 클래스를 인스턴스화하기만 하면 됩니다.

<a name="csharp-pdf-to-bmp"></a>
<a name="csharp-pdf-to-emf"></a>
<a name="csharp-pdf-to-jpg"></a>
<a name="csharp-pdf-to-png"></a>
<a name="csharp-pdf-to-gif"></a>

다음 단계와 C#에서의 코드 스니펫은 이 가능성을 보여줍니다.
 
 - [C#에서 PDF를 BMP로 변환](#csharp-pdf-to-image)
 - [C#에서 PDF를 EMF로 변환](#csharp-pdf-to-image)
 - [C#에서 PDF를 JPG로 변환](#csharp-pdf-to-image)
 - [C#에서 PDF를 PNG로 변환](#csharp-pdf-to-image)
 - [C#에서 PDF를 GIF로 변환](#csharp-pdf-to-image)

<a name="csharp-pdf-to-image"><strong>단계: C#에서 PDF를 이미지(BMP, EMF, JPG, PNG, GIF)로 변환</strong></a>

1.
1.
2. **ImageDevice**의 서브클래스 인스턴스를 생성하세요. 예를 들어:
   * **BmpDevice** (PDF를 BMP로 변환)
   * **EmfDevice** (PDF를 Emf로 변환)
   * **JpegDevice** (PDF를 JPG로 변환)
   * **PngDevice** (PDF를 PNG로 변환)
   * **GifDevice** (PDF를 GIF로 변환)
3. PDF를 이미지로 변환하기 위해 **ImageDevice.Process()** 메소드를 호출하세요.

```csharp
public static class ExampleConvertPdfToImage
{
     private static readonly string _dataDir = @"C:\Samples\";
    public static void ConvertPDFusingImageDevice()
    {
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
            imageDevice.Process(pdfDocument.Pages[pageCount], imageStream);
            imageStream.Close();
        }
    }
}
```
{{% alert color="success" %}}
**온라인으로 PDF를 PNG로 변환해보세요**

우리의 무료 애플리케이션 작동 방식의 예를 확인하세요.

Aspose.PDF for .NET에서는 ["PDF to PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png)라는 무료 온라인 애플리케이션을 제공하며, 여기서 기능과 품질을 실험해 볼 수 있습니다.

[![온라인 무료 앱을 사용하여 PDF를 PNG로 변환하는 방법](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

## SaveOptions 클래스를 사용한 PDF 변환

이 문서의 이 부분은 C# 및 SaveOptions 클래스를 사용하여 PDF를 <abbr title="Scalable Vector Graphics">SVG</abbr>로 변환하는 방법을 보여줍니다.

{{% alert color="success" %}}
**온라인으로 PDF를 SVG로 변환해보세요**

Aspose.PDF for .NET에서는 ["PDF to SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg)라는 무료 온라인 애플리케이션을 제공하며, 여기서 기능과 품질을 실험해 볼 수 있습니다.

[![Aspose.PDF 무료 앱을 사용한 PDF에서 SVG로의 변환](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
[![Aspose.PDF Convertion PDF to SVG with Free App](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** 는 2차원 벡터 그래픽을 위한 XML 기반 파일 형식의 사양 모음입니다. 정적이고 동적(상호 작용적이거나 애니메이션) 모두를 포함합니다. SVG 사양은 1999년부터 World Wide Web Consortium (W3C)에 의해 개발 중인 개방형 표준입니다.

SVG 이미지와 그 행동은 XML 텍스트 파일로 정의됩니다. 이는 검색, 색인 생성, 스크립팅이 가능하며 필요한 경우 압축할 수 있음을 의미합니다. XML 파일로서, SVG 이미지는 모든 텍스트 편집기로 생성 및 편집할 수 있지만, Inkscape와 같은 그리기 프로그램으로 만드는 것이 종종 더 편리합니다.

Aspose.PDF for .NET은 SVG 이미지를 PDF 형식으로 변환하는 기능을 지원하며 PDF 파일을 SVG 형식으로 변환할 수 있는 기능도 제공합니다.
Aspose.PDF for .NET은 SVG 이미지를 PDF 형식으로 변환하는 기능을 지원하며 PDF 파일을 SVG 형식으로 변환하는 기능도 제공합니다.

다음 코드 스니펫은 .NET을 사용하여 PDF 파일을 SVG 형식으로 변환하는 단계를 보여줍니다.

<a name="csharp-pdf-to-svg"><strong>단계: C#에서 PDF를 SVG로 변환</strong></a>

1. **Document** 클래스의 객체를 생성합니다.
2. 필요한 설정이 있는 **SvgSaveOptions** 객체를 생성합니다.
3. **Document.Save()** 메소드를 호출하고 **SvgSaveOptions** 객체를 전달하여 PDF 문서를 SVG로 변환합니다.

```csharp
public static void ConvertPDFtoSVG()
{
    // PDF 문서 불러오기
    Document document = new Document(System.IO.Path.Combine(_dataDir, "input.pdf"));
    // SvgSaveOptions 객체 인스턴스화
    SvgSaveOptions saveOptions = new SvgSaveOptions
    {
        // SVG 이미지를 Zip 아카이브로 압축하지 않음
        CompressOutputToZipArchive = false,
        TreatTargetFileNameAsDirectory = true                
    };
            
    // 결과를 SVG 파일로 저장
    document.Save(System.IO.Path.Combine(_dataDir, "PDFToSVG_out.svg"), saveOptions);
}
```

