---
title: 다양한 이미지 형식을 .NET에서 PDF로 변환하기
linktitle: 이미지를 PDF로 변환하기
type: docs
weight: 60
url: /net/convert-images-format-to-pdf/
lastmod: "2021-11-01"
description: BMP, CGM, JPEG, DICOM, PNG, TIFF, EMF, SVG와 같은 다양한 이미지 형식을 C# .NET을 사용하여 PDF로 변환합니다.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## 개요

이 글은 C#을 사용하여 다양한 이미지 형식을 PDF로 변환하는 방법에 대해 설명합니다. 이 주제들을 다룹니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 작동합니다.

_형식_: **BMP**
- [C# BMP를 PDF로 변환](#csharp-bmp-to-pdf)
- [C# BMP를 PDF로 변환하기](#csharp-bmp-to-pdf)
- [C# BMP 이미지를 PDF로 변환하는 방법](#csharp-bmp-to-pdf)

_형식_: **CGM**
- [C# CGM을 PDF로 변환](#csharp-cgm-to-pdf)
- [C# CGM을 PDF로 변환하기](#csharp-cgm-to-pdf)
- [C# CGM 이미지를 PDF로 변환하는 방법](#csharp-cgm-to-pdf)

_형식_: **DICOM**
- [C# DICOM을 PDF로 변환](#csharp-dicom-to-pdf)
- [C# DICOM을 PDF로 변환하기](#csharp-dicom-to-pdf)
- [C# DICOM 이미지를 PDF로 변환하는 방법](#csharp-dicom-to-pdf)
- [C# DICOM 이미지를 PDF로 변환하는 방법](#csharp-dicom-to-pdf)

_포맷_: **EMF**
- [C# EMF를 PDF로 변환](#csharp-emf-to-pdf)
- [C# EMF를 PDF로 변환](#csharp-emf-to-pdf)
- [C# EMF 이미지를 PDF로 변환하는 방법](#csharp-emf-to-pdf)

_포맷_: **GIF**
- [C# GIF를 PDF로 변환](#csharp-gif-to-pdf)
- [C# GIF를 PDF로 변환](#csharp-gif-to-pdf)
- [C# GIF 이미지를 PDF로 변환하는 방법](#csharp-gif-to-pdf)

_포맷_: **JPG**
- [C# JPG를 PDF로 변환](#csharp-jpg-to-pdf)
- [C# JPG를 PDF로 변환](#csharp-jpg-to-pdf)
- [C# JPG 이미지를 PDF로 변환하는 방법](#csharp-jpg-to-pdf)

_포맷_: **PNG**
- [C# PNG를 PDF로 변환](#csharp-png-to-pdf)
- [C# PNG를 PDF로 변환](#csharp-png-to-pdf)
- [C# PNG 이미지를 PDF로 변환하는 방법](#csharp-png-to-pdf)

_포맷_: **SVG**
- [C# SVG를 PDF로 변환](#csharp-svg-to-pdf)
- [C# SVG를 PDF로 변환](#csharp-svg-to-pdf)
- [C# SVG 이미지를 PDF로 변환하는 방법](#csharp-svg-to-pdf)

_포맷_: **TIFF**
- [C# TIFF를 PDF로 변환](#csharp-tiff-to-pdf)
- [C# TIFF를 PDF로 변환](#csharp-tiff-to-pdf)
- [C# TIFF 이미지를 PDF로 변환하는 방법](#csharp-tiff-to-pdf)
- [C# TIFF 이미지를 PDF로 변환하는 방법](#csharp-tiff-to-pdf)

다른 주제들도 이 글에서 다룹니다.
- [참조](#see-also)


## C# 이미지를 PDF로 변환

**Aspose.PDF for .NET**은 다양한 형식의 이미지를 PDF 파일로 변환할 수 있습니다. 저희 라이브러리는 BMP, CGM, DICOM, EMF, JPG, PNG, SVG, TIFF 형식과 같은 가장 인기 있는 이미지 형식을 변환하기 위한 코드 스니펫을 제공합니다.

## BMP를 PDF로 변환

**Aspose.PDF for .NET** 라이브러리를 사용하여 BMP 파일을 PDF 문서로 변환하세요.

<abbr title="Bitmap Image File">BMP</abbr> 이미지는 확장자가 있는 파일입니다. BMP는 비트맵 디지털 이미지를 저장하는 데 사용되는 비트맵 이미지 파일을 나타냅니다. 이 이미지들은 그래픽 어댑터와 독립적이며, 장치 독립 비트맵(DIB) 파일 형식이라고도 불립니다.
Aspose.PDF for .NET API를 사용하여 BMP를 PDF 파일로 변환할 수 있습니다. 따라서 BMP 이미지를 변환하기 위해 다음 단계를 따르세요:

<a name="csharp-bmp-to-pdf" id="csharp-bmp-to-pdf"><strong>단계: C#에서 BMP를 PDF로 변환</strong></a>

1.
1.
2. 입력 **BMP** 이미지를 로드합니다.
3. 마지막으로 출력 PDF 파일을 저장합니다.

다음 코드 스니펫은 BMP를 PDF로 변환하는 방법을 보여주고 C#을 사용한 이 단계를 따릅니다:

```csharp
//비어 있는 PDF 문서 초기화
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // 샘플 BMP 이미지 파일을 로드합니다
    image.File = dataDir + "Sample.bmp";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // 출력 PDF 문서를 저장합니다
    pdfDocument.Save(dataDir + "BMPtoPDF.pdf");
}
```

{{% alert color="success" %}}
**BMP를 PDF로 온라인 변환 시도하기**

Aspose는 기능과 품질을 조사할 수 있는 무료 온라인 애플리케이션 ["BMP to PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)를 제공합니다.

[![Aspose.PDF 변환 BMP를 PDF로 사용하는 무료 앱](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## CGM을 PDF로 변환

<abbr title="Computer Graphics Metafile">CGM</abbr>은 CAD(컴퓨터 지원 설계) 및 프레젠테이션 그래픽 응용 프로그램에서 일반적으로 사용되는 컴퓨터 그래픽 메타파일 형식을 위한 파일 확장자입니다.
<abbr title="컴퓨터 그래픽스 메타파일">CGM</abbr>은 주로 CAD(컴퓨터 지원 설계) 및 프레젠테이션 그래픽 응용 프로그램에서 사용되는 컴퓨터 그래픽스 메타파일 형식의 파일 확장자입니다.

다음 코드 스니펫은 CGM 파일을 PDF 형식으로 변환하는 방법을 보여줍니다.

<a name="csharp-cgm-to-pdf" id="csharp-cgm-to-pdf"><strong>단계: C#에서 CGM을 PDF로 변환</strong></a>

1. [CgmLoadOptions](https://reference.aspose.com/pdf/net/aspose.pdf/cgmloadoptions) 클래스의 인스턴스를 생성합니다.
2. 원본 파일명과 옵션을 명시하여 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스의 인스턴스를 생성합니다.
3. 원하는 파일 이름으로 문서를 저장합니다.

```csharp
public static void ConvertCGMtoPDF()
{
    CgmLoadOptions option = new CgmLoadOptions();
    Document pdfDocument= new Document(_dataDir+"corvette.cgm", option);
    pdfDocument.Save(_dataDir+"CGMtoPDF.pdf");
}
```

## DICOM을 PDF로 변환

<abbr title="의료 영상 및 통신 표준">DICOM</abbr> 형식은 검사된 환자의 디지털 의료 이미지 및 문서의 생성, 저장, 전송, 시각화를 위한 의료 산업 표준입니다.
<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> 형식은 검진받은 환자의 디지털 의료 이미지 및 문서의 생성, 저장, 전송 및 시각화를 위한 의료 산업 표준입니다.

**Aspsoe.PDF for .NET**은 DICOM 및 SVG 이미지를 변환할 수 있지만, 기술적인 이유로 이미지를 추가할 때 PDF에 추가할 파일의 유형을 지정해야 합니다:

<a name="csharp-dicom-to-pdf" id="csharp-dicom-to-pdf"><strong>단계: C#에서 DICOM을 PDF로 변환</strong></a>

1. Image 클래스의 객체를 생성합니다.
2. 이미지를 페이지의 Paragraphs 컬렉션에 추가합니다.
3. [FileType](https://reference.aspose.com/pdf/net/aspose.pdf/image/properties/filetype) 속성을 지정합니다.
4. 파일의 경로 또는 소스를 지정합니다.
    - 하드 드라이브의 위치에 이미지가 있는 경우, Image.File 속성을 사용하여 경로 위치를 지정합니다.
    - 이미지가 MemoryStream에 배치된 경우, 이미지를 포함하는 객체를 Image.ImageStream 속성에 전달합니다.

다음 코드 스니펫은 Aspose.PDF를 사용하여 DICOM 파일을 PDF 형식으로 변환하는 방법을 보여줍니다.
다음 코드 조각은 Aspose.PDF를 사용하여 DICOM 파일을 PDF 형식으로 변환하는 방법을 보여줍니다.

```csharp
private const string _dataDir = "..\\..\\..\\..\\Samples";
// Image 클래스를 사용하여 DICOM 이미지를 PDF로 변환
public static void ConvertDICOMtoPDF()
{
    // 문서 객체 인스턴스화
    Document pdfDocument = new Document();

    // 문서의 페이지 컬렉션에 페이지 추가
    Page page = pdfDocument.Pages.Add();

    Image image = new Image
    {
        FileType = ImageFileType.Dicom,
        File = System.IO.Path.Combine(_dataDir,"bmode.dcm")
    };
    pdfDocument.Pages[1].Paragraphs.Add(image);
    // 출력을 PDF 형식으로 저장
    pdfDocument.Save(System.IO.Path.Combine(_dataDir,"PDFWithDicomImage_out.pdf"));
}
```

{{% alert color="success" %}}
**온라인에서 DICOM을 PDF로 변환해보세요**

Aspose는 무료 온라인 애플리케이션 ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)를 제공합니다. 여기에서 기능과 품질을 조사해볼 수 있습니다.

[![Aspose.PDF 변환 DICOM을 PDF로 사용하는 무료 앱](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)

[![Aspose.PDF 변환 DICOM을 PDF로 무료 앱 사용](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## EMF를 PDF로 변환

<abbr title="Enhanced metafile format">EMF</abbr>EMF는 그래픽 이미지를 장치 독립적으로 저장합니다. EMF의 메타파일은 시간 순서대로 다양한 길이의 레코드로 구성되어 있으며, 파싱 후 모든 출력 장치에서 저장된 이미지를 렌더링할 수 있습니다. 또한, 아래 단계를 사용하여 EMF를 PDF 이미지로 변환할 수 있습니다:

<a name="csharp-emf-to-pdf" id="csharp-emf-to-pdf"><strong>단계: C#에서 EMF를 PDF로 변환</strong></a>

1. 먼저, [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스 객체를 초기화합니다.
2. **EMF** 이미지 파일을 로드합니다.
3. 로드된 EMF 이미지를 페이지에 추가합니다.
4. PDF 문서를 저장합니다.

또한, 다음 코드 스니펫은 C#을 사용하여 .NET 코드 스니펫에서 EMF를 PDF로 변환하는 방법을 보여줍니다:

```csharp
// 새 PDF 문서 초기화
var doc = new Document();

// 입력 EMF 이미지 파일의 경로 지정
var imageFile = dataDir + "drawing.emf";
var page = doc.Pages.Add();
string file = imageFile;
FileStream filestream = new FileStream(file, FileMode.Open, FileAccess.Read);
BinaryReader reader = new BinaryReader(filestream);
long numBytes = new FileInfo(file).Length;
byte[] bytearray = reader.ReadBytes((int)numBytes);
Stream stream = new MemoryStream(bytearray);
var b = new Bitmap(stream);

// 페이지 치수 속성 지정
page.PageInfo.Margin.Bottom = 0;
page.PageInfo.Margin.Top = 0;
page.PageInfo.Margin.Left = 0;
page.PageInfo.Margin.Right = 0;
page.PageInfo.Width = b.Width;
page.PageInfo.Height = b.Height;
var image = new Aspose.Pdf.Image();
image.File = imageFile;
page.Paragraphs.Add(image);

// 출력 PDF 문서 저장
doc.Save(dataDir + "EMFtoPDF.pdf");
```
{{% alert color="success" %}}
**온라인으로 EMF를 PDF로 변환해보세요**

Aspose에서 무료 온라인 애플리케이션 ["EMF에서 PDF로"](https://products.aspose.app/pdf/conversion/emf-to-pdf/)를 제공합니다. 여기서 기능과 품질을 탐구해 볼 수 있습니다.

[![Aspose.PDF 무료 앱을 사용하여 EMF에서 PDF로 변환](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## GIF를 PDF로 변환

**Aspose.PDF for .NET** 라이브러리를 사용하여 GIF 파일을 PDF 문서로 변환합니다.

<abbr title="Graphics Interchange Format">GIF</abbr>는 압축된 데이터를 256색 이하의 형식으로 품질 손실 없이 저장할 수 있습니다. 하드웨어 독립적인 GIF 형식은 네트워크를 통한 비트맵 이미지 전송을 위해 CompuServe가 1987년 (GIF87a)에 개발했습니다.
Aspose.PDF for .NET API를 사용하여 GIF를 PDF 파일로 변환할 수 있습니다. 다음 단계에 따라 GIF 이미지를 변환할 수 있습니다:

<a name="csharp-gif-to-pdf" id="csharp-gif-to-pdf"><strong>단계: C#에서 GIF를 PDF로 변환</strong></a>

1.
1.
2. 입력 **GIF** 이미지를 로드합니다.
3. 마침내 출력 PDF 파일을 저장합니다.

다음 코드 스니펫은 BMP를 PDF로 변환하는 방법을 보여주며 C#을 사용한 이 단계를 따릅니다:

```csharp
//PDF 문서 초기화
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // 샘플 GIF 이미지 파일 로드
    image.File = dataDir + "Sample.gif";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // 출력 PDF 문서 저장
    pdfDocument.Save(dataDir + "GIFtoPDF.pdf");
}
```

{{% alert color="success" %}}
**온라인에서 GIF를 PDF로 변환해보세요**

Aspose에서는 기능과 품질을 조사해볼 수 있는 무료 온라인 애플리케이션 ["GIF to PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/)를 제공합니다.

[![Aspose.PDF Convertion GIF to PDF using Free App](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## JPG를 PDF로 변환

JPG를 PDF로 변환하는 방법을 궁금해할 필요가 없습니다. 왜냐하면 **Apose.PDF for .NET** 라이브러리가 최고의 결정을 제공하기 때문입니다.
JPG를 PDF로 변환하는 방법을 궁금해할 필요가 없습니다. 왜냐하면 **Apose.PDF for .NET** 라이브러리가 최고의 해결책을 가지고 있기 때문입니다.

다음 단계를 따라 Aspose.PDF for .NET을 사용하여 JPG 이미지를 PDF로 쉽게 변환할 수 있습니다:

<a name="csharp-jpg-to-pdf" id="csharp-jpg-to-pdf"><strong>단계: C#에서 JPG를 PDF로 변환</strong></a>

1. [Document](https://reference.aspose.com/page/net/aspose.page/document) 클래스의 객체를 초기화합니다.
2. PDF 문서에 새 페이지를 추가합니다.
3. **JPG** 이미지를 불러와서 문단에 추가합니다.
4. 출력 PDF를 저장합니다.

아래 코드 스니펫은 C#을 사용하여 JPG 이미지를 PDF로 변환하는 방법을 보여줍니다:

```csharp
// 입력 JPG 파일 로드
String path = dataDir + "Aspose.jpg";

// 새 PDF 문서 초기화
Document doc = new Document();

// 빈 문서에 빈 페이지 추가
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// 페이지에 이미지 추가
page.Paragraphs.Add(image);

// 출력 PDF 파일 저장
doc.Save(dataDir + "ImagetoPDF.pdf");
```

그런 다음 **페이지의 같은 높이와 너비**를 가진 PDF로 이미지를 변환하는 방법을 볼 수 있습니다.
그럼 **페이지와 동일한 높이와 너비로 이미지를 PDF로 변환**하는 방법을 알 수 있습니다.

1. 입력 이미지 파일을 불러옵니다.
1. 이미지의 높이와 너비를 가져옵니다.
1. 페이지의 높이, 너비 및 여백을 설정합니다.
1. 출력 PDF 파일을 저장합니다.

다음 코드 스니펫은 C#을 사용하여 페이지 높이와 너비가 동일한 이미지를 PDF로 변환하는 방법을 보여줍니다:

```csharp
// 입력 JPG 이미지 파일을 불러옵니다
String path = dataDir + "Aspose.jpg";
System.Drawing.Image srcImage = System.Drawing.Image.FromFile(path);

// 입력 이미지의 높이를 읽습니다
int h = srcImage.Height;

// 입력 이미지의 너비를 읽습니다
int w = srcImage.Width;

// 새 PDF 문서를 초기화합니다
Document doc = new Document();

// 빈 페이지를 추가합니다
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// 페이지 크기와 여백을 설정합니다
page.PageInfo.Height = (h);
page.PageInfo.Width = (w);
page.PageInfo.Margin.Bottom = (0);
page.PageInfo.Margin.Top = (0);
page.PageInfo.Margin.Right = (0);
page.PageInfo.Margin.Left = (0);
page.Paragraphs.Add(image);

// 출력 PDF 파일을 저장합니다
doc.Save(dataDir + "ImagetoPDF_HeightWidth.pdf");
```
{{% alert color="success" %}}
**JPG를 PDF로 온라인 변환해 보세요**

Aspose에서 ["JPG to PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)라는 무료 온라인 애플리케이션을 제공합니다. 여기서 기능과 품질을 탐색해 볼 수 있습니다.

[![Aspose.PDF를 사용한 JPG에서 PDF로의 무료 앱 변환](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## PNG를 PDF로 변환

**Aspose.PDF for .NET**은 PNG 이미지를 PDF 형식으로 변환하는 기능을 지원합니다. 다음 코드 스니펫을 확인하여 작업을 실현하세요.

<abbr title="Portable Network Graphics">PNG</abbr>는 손실 없는 압축을 사용하는 래스터 이미지 파일 형식을 나타냅니다. 이로 인해 사용자에게 인기가 있습니다.

아래 단계를 사용하여 PNG를 PDF 이미지로 변환할 수 있습니다:

<a name="csharp-png-to-pdf" id="csharp-png-to-pdf"><strong>단계: C#에서 PNG를 PDF로 변환</strong></a>

1. 입력 **PNG** 이미지를 로드합니다.
2. 높이와 너비 값을 읽습니다.
3.
페이지 차원 설정.
출력 파일 저장.

아래 코드 스니펫은 C#을 사용하여 .NET 애플리케이션에서 PNG를 PDF로 변환하는 방법을 보여줍니다:

```csharp
// 입력 PNG 파일 로드
String path = dataDir + "Aspose.png";
System.Drawing.Image srcImage = System.Drawing.Image.FromFile(path);
int h = srcImage.Height;
int w = srcImage.Width;

// 새 문서 초기화
Document doc = new Document();
Page page = doc.Pages.Add();
Aspose.Pdf.Image image = new Aspose.Pdf.Image();
image.File = (path);

// 페이지 차원 설정
page.PageInfo.Height = (h);
page.PageInfo.Width = (w);
page.PageInfo.Margin.Bottom = (0);
page.PageInfo.Margin.Top = (0);
page.PageInfo.Margin.Right = (0);
page.PageInfo.Margin.Left = (0);
page.Paragraphs.Add(image);

// 출력 PDF 저장
doc.Save(dataDir + "ImagetoPDF.pdf");
```

{{% alert color="success" %}}
**온라인으로 PNG를 PDF로 변환해 보세요**

Aspose는 기능과 품질을 조사해 볼 수 있는 무료 온라인 애플리케이션 ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/)를 제공합니다.
**Aspose.PDF for .NET**에서는 SVG 이미지를 PDF 형식으로 변환하는 방법과 원본 <abbr title="Scalable Vector Graphics">SVG</abbr> 파일의 크기를 얻는 방법을 설명합니다.

스케일러블 벡터 그래픽(SVG)은 정적 및 동적(대화형 또는 애니메이션)의 2차원 벡터 그래픽을 위한 XML 기반 파일 형식의 사양 가족입니다. SVG 사양은 1999년부터 World Wide Web Consortium (W3C)에 의해 개발되고 있는 개방형 표준입니다.

SVG 이미지와 그 행동은 XML 텍스트 파일에서 정의됩니다.
SVG 이미지와 그 행동은 XML 텍스트 파일에서 정의됩니다.

{{% alert color="success" %}}
**온라인에서 SVG 형식을 PDF로 변환해 보세요**

Aspose.PDF for .NET은 무료 온라인 애플리케이션 ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf)를 제공합니다. 여기에서 기능과 품질을 조사해 볼 수 있습니다.

[![Aspose.PDF Convertion SVG to PDF with Free App](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

SVG 파일을 PDF로 변환하려면 [`LoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/loadoptions) 객체를 초기화하는 데 사용되는 [SvgLoadOptions](https://reference.aspose.com/net/pdf/aspose.pdf/svgloadoptions)라는 클래스를 사용하세요. 나중에 이 객체는 Document 객체 초기화 중에 인수로 전달되며 PDF 렌더링 엔진이 소스 문서의 입력 형식을 결정하는 데 도움이 됩니다.

<a name="csharp-svg-to-pdf" id="csharp-svg-to-pdf"><strong>단계: C#에서 SVG를 PDF로 변환</strong></a>

1.
1.
2. [`Document`](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스의 인스턴스를 소스 파일명과 옵션으로 생성하세요.
3. 원하는 파일 이름으로 문서를 저장하세요.

다음 코드 조각은 Aspose.PDF for .NET을 사용하여 SVG 파일을 PDF 형식으로 변환하는 과정을 보여줍니다.

```csharp
public static void ConvertSVGtoPDF()
{
    SvgLoadOptions option = new SvgLoadOptions();
    Document pdfDocument= new Document(_dataDir + "car.svg", option);
    pdfDocument.Save(_dataDir + "svgtest.pdf");
}
```

## SVG 차원 가져오기

소스 SVG 파일의 차원을 가져올 수도 있습니다. 이 정보는 출력 PDF의 전체 페이지를 SVG가 차지하게 하고 싶을 때 유용할 수 있습니다. ScgLoadOption 클래스의 AdjustPageSize 속성이 이 요구사항을 충족합니다. 이 속성의 기본값은 false입니다. 값이 true로 설정되면, 출력 PDF는 소스 SVG와 동일한 크기(차원)를 가지게 됩니다.

다음 코드 조각은 소스 SVG 파일의 차원을 가져오고 PDF 파일을 생성하는 과정을 보여줍니다.
다음 코드 조각은 소스 SVG 파일의 크기를 가져오고 PDF 파일을 생성하는 과정을 보여줍니다.

```csharp
public static void ConvertSVGtoPDF_Advanced()
{
    // 완전한 예제와 데이터 파일을 보려면 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 로 이동하십시오.
    // 문서 디렉토리 경로입니다.
    string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    var loadopt = new SvgLoadOptions();
    loadopt.AdjustPageSize = true;
    var svgDoc = new Document(dataDir + "GetSVGDimensions.svg", loadopt);
    svgDoc.Pages[1].PageInfo.Margin.Top = 0;
    svgDoc.Pages[1].PageInfo.Margin.Left = 0;
    svgDoc.Pages[1].PageInfo.Margin.Bottom = 0;
    svgDoc.Pages[1].PageInfo.Margin.Right = 0;
    svgDoc.Save(dataDir + "GetSVGDimensions_out.pdf");
}
```

### SVG 지원 기능

<table>
    <thead>
        <tr>
            <th>
                <p>SVG 태그</p>
            </th>
            <th>
                <p>샘플 사용</p>
            </th>
        </tr>
    </thead>
    <tbody>

<tbody>
    <tr>
        <td>
            <p>원</p>
        </td>
        <td>
            <code><pre>&lt;circle id="r2" cx="10" cy="10" r="10" stroke="blue" stroke-width="2"&gt;</pre></code>
        </td>
    </tr>
    <tr>
        <td>
            <p>정의</p>
        </td>
        <td>
            <code>&lt;defs&gt;&nbsp; <br> &lt;rect id="r1" width="15" height="15"
                stroke="blue" stroke-width="2" /&gt;&nbsp; <br> &lt;circle id="r2"
                cx="10" cy="10" r="10" stroke="blue" stroke-width="2"/&gt;&nbsp; <br>
                &lt;circle id="r3" cx="10" cy="10" r="10" stroke="blue" stroke-width="3"/&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br> &lt;use
                x="25" y="40" xlink:href="#r1" fill="red"/&gt;&nbsp; <br> &lt;use
                x="35" y="15" xlink:href="#r2" fill="green"/&gt;&nbsp; <br> &lt;use
                x="58" y="50" xlink:href="#r3" fill="blue"/&gt;</code>
        </td>
    </tr>
```


         </tr>
        <tr>
            <td>
                <p>tref</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text
                    id="ReferencedText"&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    참조된 문자 데이터&nbsp; <br> &nbsp;&nbsp;&nbsp;
                    &lt;/text&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;text x="10" y="100" font-size="15" fill="red" &gt;&nbsp; <br
                        class="atl-forced-newline"> &nbsp;&nbsp;&nbsp; &lt;tref
                    xlink:href="#ReferencedText"/&gt;&nbsp; <br> &lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>use</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text id="Text" x="400"
                    y="200"&nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; font-family="Verdana" font-size="100"
```


font-family="Verdana" font-size="100"
text-anchor="middle" > <br> 
Masked text <br> </text> <br
    class="atl-forced-newline"> <use xlink:href="#Text" fill="blue" /&gt;</p>
</td>
</tr>
<tr>
<td>
    <p>ellipse&nbsp;</p>
</td>
<td>
    <p>&lt;ellipse cx="2.5" cy="1.5" rx="2" ry="1" fill="red" /&gt;</p>
</td>
</tr>
<tr>
<td>
    <p>g&nbsp;</p>
</td>
<td>
    <p>&lt;g fill="none" stroke="dimgray" stroke-width="1.5" &gt; <br>
        &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="-7"
        y1="-7" x2="-3" y2="-3"/&gt; <br> &nbsp;&nbsp;
        &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="7" y1="7" x2="3"
```


<tr>
    <td>
        <p>선</p>
    </td>
    <td>
        <p>&lt;line x1="7" y1="7" x2="3" y2="3"/&gt;&nbsp;<br>&nbsp;&nbsp;&nbsp;
        &lt;line x1="-7" y1="7" x2="-3" y2="3"/&gt;&nbsp;<br>&nbsp;&nbsp;&nbsp;
        &lt;line x1="7" y1="-7" x2="3" y2="-3"/&gt;&nbsp;<br class="atl-forced-newline">&lt;/g&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>이미지</p>
    </td>
    <td>
        <p>&lt;image id="ShadedRelief" x="24" y="4" width="64" height="82" xlink:href="relief.jpg"/&gt;&nbsp;</p>
    </td>
</tr>
<tr>
    <td>
        <p>선</p>
    </td>
    <td>
        <p>&lt;line style="stroke:#eea;stroke-width:8" x1="10" y1="30" x2="260" y2="100"/&gt;&nbsp;</p>
    </td>
</tr>
```

<tr>
    <td>
        <p>선</p>
    </td>
    <td>
        <p>&lt;line style="stroke:#eea;stroke-width:8" x1="10" y1="30" x2="260" y2="100"/&gt;&nbsp;</p>
    </td>
</tr>
<tr>
    <td>
        <p>경로</p>
    </td>
    <td>
        <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
            "/&gt;&nbsp;</p>
    </td>
</tr>
<tr>
    <td>
        <p>스타일</p>
    </td>
    <td>
        <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
            "/&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>다각형</p>
    </td>
    <td>
        <p>&lt;polygon style="stroke:#24a;stroke-width:1.5;fill:#eefefe" points="10,10 180,10 10,250 10,10"
            /&gt;</p>
    </td>
</tr>
<tr>
    <td>
        <p>폴리라인</p>
```

        <tr>
            <td>
                <p>다각선</p>
            </td>
            <td>
                <p>&lt;polyline fill="none" stroke="dimgray" stroke-width="1" points="-3,-6 3,-6 3,1 5,1 0,7 -5,1
                    -3,1 -3,-5"/&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>사각형</p>
            </td>
            <td>
                <p>&lt;rect x="0" y="0" width="400" height="600" stroke="none" fill="aliceblue" /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>SVG</p>
            </td>
            <td>
                <p>&lt;svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="10cm" height="5cm" &gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>텍스트</p>
            </td>
            <td>
                <p>&lt;text font-family="sans-serif" fill="dimgray" font-size="22px" font-weight="bold" x="58"
                    y="30" pointer-events="none"&gt;지도 제목&lt;/text&gt;</p>
            </td>
        </tr>
```
## TIFF를 PDF로 변환

**Aspose.PDF**는 단일 프레임 또는 멀티 프레임 <abbr title="Tag Image File Format">TIFF</abbr> 이미지를 지원하는 파일 형식입니다. 이는 .NET 애플리케이션에서 TIFF 이미지를 PDF로 변환할 수 있음을 의미합니다.

TIFF 또는 TIF, 태그 이미지 파일 형식은 이 파일 형식 표준을 준수하는 다양한 장치에서 사용하기 위해 설계된 래스터 이미지를 나타냅니다.
TIFF 또는 TIF, Tagged Image File Format은 이 파일 형식 표준을 준수하는 다양한 장치에서 사용하기 위한 래스터 이미지를 나타냅니다.

다른 래스터 파일 형식 그래픽처럼 TIFF를 PDF로 변환할 수 있습니다:

<a name="csharp-tiff-to-pdf" id="csharp-tiff-to-pdf"><strong>단계: C#에서 TIFF를 PDF로 변환</strong></a>

1. 새로운 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스 객체를 생성하고 페이지를 추가하세요.
2. 입력 **TIFF** 이미지를 로드하세요.
3. PDF 문서를 저장하세요.

```csharp
빈 PDF 문서 초기화
using (Document pdfDocument = new Document())
{
    pdfDocument.Pages.Add();
    Aspose.Pdf.Image image = new Aspose.Pdf.Image();

    // 샘플 Tiff 이미지 파일 로드
    image.File = dataDir + "sample.tiff";
    pdfDocument.Pages[1].Paragraphs.Add(image);

    // 출력 PDF 문서 저장
    pdfDocument.Save(dataDir + "TIFFtoPDF.pdf");
}
```

다페이지 TIFF 이미지를 다페이지 PDF 문서로 변환하고 일부 매개변수를 제어할 필요가 있는 경우, 예를 들어
다중 페이지 TIFF 이미지를 다중 페이지 PDF 문서로 변환하고 일부 매개변수를 제어해야하는 경우 다음 단계를 따르십시오.

1. Document 클래스의 인스턴스를 생성합니다
1. 입력 TIFF 이미지를 로드합니다
1. 프레임의 FrameDimension을 가져옵니다
1. 각 프레임에 대해 새 페이지를 추가합니다
1. 마지막으로 이미지를 PDF 페이지에 저장합니다

다음 코드 스니펫은 C#을 사용하여 다중 페이지 또는 다중 프레임 TIFF 이미지를 PDF로 변환하는 방법을 보여줍니다:

```csharp
public static void TiffToPDF2()
{
    // 새 Document 초기화
    Document pdf = new Document();

    // TIFF 이미지를 스트림으로 로드
    Bitmap bitmap = new Bitmap(File.OpenRead(_dataDir+"multipage.tif"));
    // 다중 페이지 또는 다중 프레임 TIFF를 PDF로 변환
    FrameDimension dimension = new FrameDimension(bitmap.FrameDimensionsList[0]);
    int frameCount = bitmap.GetFrameCount(dimension);

    // 각 프레임을 반복 처리
    for (int frameIdx = 0; frameIdx <= frameCount - 1; frameIdx++)
    {
        Page page = pdf.Pages.Add();

        bitmap.SelectActiveFrame(dimension, frameIdx);

        MemoryStream currentImage = new MemoryStream();
        bitmap.Save(currentImage, ImageFormat.Tiff);

        Aspose.Pdf.Image imageht = new Aspose.Pdf.Image
        {
            ImageStream = currentImage,
            //다른 옵션 적용
            //ImageScale = 0.5
        };
        page.Paragraphs.Add(imageht);
    }

    // 출력 PDF 파일 저장
    pdf.Save(_dataDir + "TifftoPDF.pdf");
}
```
## 적용 대상

|**플랫폼**|**지원됨**|**코멘트**|
| :- | :- |:- |
|Windows .NET Framework|2.0-4.6| |
|Windows .NET Core |2.0-3.1| |
|.NET 5 Windows| |
|Linux .NET Core|2.0-3.1 | |
|.NET 5 Linux | |

## 참조

이 글은 또한 다음 주제들을 다룹니다. 코드는 위와 같습니다.

형식: **BMP**
- [C# BMP to PDF Code](#csharp-bmp-to-pdf)
- [C# BMP to PDF API](#csharp-bmp-to-pdf)
- [C# BMP to PDF Programmatically](#csharp-bmp-to-pdf)
- [C# BMP to PDF Library](#csharp-bmp-to-pdf)
- [C# Save BMP as PDF](#csharp-bmp-to-pdf)
- [C# Generate PDF from BMP](#csharp-bmp-to-pdf)
- [C# Create PDF from BMP](#csharp-bmp-to-pdf)
- [C# BMP to PDF Converter](#csharp-bmp-to-pdf)

형식: **CGM**
- [C# CGM to PDF Code](#csharp-cgm-to-pdf)
- [C# CGM to PDF API](#csharp-cgm-to-pdf)
- [C# CGM to PDF Programmatically](#csharp-cgm-to-pdf)
- [C# CGM to PDF Library](#csharp-cgm-to-pdf)
- [C# Save CGM as PDF](#csharp-cgm-to-pdf)
- [C# Generate PDF from CGM](#csharp-cgm-to-pdf)
- [C# Create PDF from CGM](#csharp-cgm-to-pdf)
- [C# CGM to PDF Converter](#csharp-cgm-to-pdf)
- [C# CGM to PDF 변환기](#csharp-cgm-to-pdf)

_형식_: **DICOM**
- [C# DICOM에서 PDF 코드로](#csharp-dicom-to-pdf)
- [C# DICOM에서 PDF API로](#csharp-dicom-to-pdf)
- [C# 프로그래밍 방식으로 DICOM에서 PDF로](#csharp-dicom-to-pdf)
- [C# DICOM에서 PDF 라이브러리로](#csharp-dicom-to-pdf)
- [C# DICOM을 PDF로 저장](#csharp-dicom-to-pdf)
- [C# DICOM에서 PDF 생성](#csharp-dicom-to-pdf)
- [C# DICOM에서 PDF 생성](#csharp-dicom-to-pdf)
- [C# DICOM에서 PDF 변환기로](#csharp-dicom-to-pdf)

_형식_: **EMF**
- [C# EMF에서 PDF 코드로](#csharp-emf-to-pdf)
- [C# EMF에서 PDF API로](#csharp-emf-to-pdf)
- [C# 프로그래밍 방식으로 EMF에서 PDF로](#csharp-emf-to-pdf)
- [C# EMF에서 PDF 라이브러리로](#csharp-emf-to-pdf)
- [C# EMF를 PDF로 저장](#csharp-emf-to-pdf)
- [C# EMF에서 PDF 생성](#csharp-emf-to-pdf)
- [C# EMF에서 PDF 생성](#csharp-emf-to-pdf)
- [C# EMF에서 PDF 변환기로](#csharp-emf-to-pdf)
