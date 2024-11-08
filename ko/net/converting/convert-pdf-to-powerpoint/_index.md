---
title: .NET에서 PDF를 PowerPoint로 변환
linktitle: PDF를 PowerPoint로 변환
type: docs
weight: 30
url: /ko/net/convert-pdf-to-powerpoint/
lastmod: "2021-11-01"
description: Aspose.PDF를 사용하면 .NET을 사용하여 PDF를 PPT (PowerPoint) 형식으로 변환할 수 있습니다. PDF를 PPTX로 변환하는 방법 중 하나는 슬라이드를 이미지로 사용하는 것입니다.
lastmod: "2021-10-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## 개요

이 기사는 **C#을 사용하여 PDF를 PowerPoint로 변환하는 방법**을 설명합니다. 다음 주제를 다룹니다.

_형식_: **PPTX**
- [C# PDF를 PPTX로](#csharp-pdf-to-pptx)
- [C# PDF를 PPTX로 변환](#csharp-pdf-to-pptx)
- [C# PDF 파일을 PPTX로 변환하는 방법](#csharp-pdf-to-pptx)

_형식_: **PowerPoint**
- [C# PDF를 PowerPoint로](#csharp-pdf-to-powerpoint)
- [C# PDF를 PowerPoint로 변환](#csharp-pdf-to-powerpoint)
- [C# PDF 파일을 PowerPoint로 변환하는 방법](#csharp-pdf-to-powerpoint)

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 사용할 수도 있습니다.

## C# PDF를 PowerPoint 및 PPTX로 변환
## C# PDF에서 PowerPoint 및 PPTX 변환

**Aspose.PDF for .NET**을 사용하면 PDF에서 PPTX로의 변환 진행 상황을 추적할 수 있습니다.

우리는 Aspose.Slides라는 API를 가지고 있으며, 이 API는 PPT/PPTX 프레젠테이션을 생성하고 조작하는 기능을 제공합니다. 이 API는 또한 PPT/PPTX 파일을 PDF 형식으로 변환하는 기능을 제공합니다. 최근 많은 고객들로부터 PDF를 PPTX 형식으로 변환하는 기능을 지원해 줄 것을 요청받았습니다. Aspose.PDF for .NET 10.3.0의 출시를 시작으로 PDF 문서를 PPTX 형식으로 변환하는 기능을 도입했습니다. 이 변환 과정에서 PDF 파일의 개별 페이지는 PPTX 파일의 별도 슬라이드로 변환됩니다.

PDF에서 <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>로의 변환 중에는 텍스트가 텍스트로 렌더링되어 선택하거나 업데이트할 수 있습니다.
PDF에서 <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>로 변환하는 동안 텍스트는 선택/업데이트할 수 있는 텍스트로 렌더링됩니다.

## C# 및 Aspose.PDF .NET을 사용한 간단한 PDF에서 PowerPoint로의 변환

PDF를 PPTX로 변환하기 위해 Aspose.PDF for .NET은 다음 코드 단계를 사용할 것을 권장합니다.

<a name="csharp-pdf-to-powerpoint"><strong>단계: C#에서 PDF를 PowerPoint로 변환</strong></a> | <a name="csharp-pdf-to-pptx"><strong>단계: C#에서 PDF를 PPTX로 변환</strong></a>

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스의 인스턴스 생성
2. [PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) 클래스의 인스턴스 생성
3. **Document** 객체의 **Save** 메서드를 사용하여 PDF를 PPTX로 저장하세요.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// PDF 문서를 로드합니다.
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// PptxSaveOptions 인스턴스를 생성합니다.
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();
// 출력을 PPTX 형식으로 저장합니다.
doc.Save(dataDir + "PDFToPPT_out.pptx", pptx_save);
```
## PDF를 PPTX로 변환하여 슬라이드를 이미지로 사용

{{% alert color="success" %}}
**PDF를 PowerPoint 온라인으로 변환해 보세요**

Aspose.PDF for .NET은 무료 온라인 애플리케이션 ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx)를 제공합니다. 여기서 기능성과 품질을 살펴볼 수 있습니다.

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

검색 가능한 PDF를 선택 가능한 텍스트 대신 이미지로 PPTX로 변환해야 하는 경우, Aspose.PDF는 [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) 클래스를 통해 이 기능을 제공합니다. 이를 위해 다음 코드 샘플에서 보여주는 것처럼 [PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) 클래스의 [SlidesAsImages](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/slidesasimages) 속성을 'true'로 설정하세요.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인할 수 있습니다.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// PDF 문서를 로드합니다.
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// PptxSaveOptions 인스턴스를 생성합니다.
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();
// 출력을 PPTX 형식으로 저장합니다.
pptx_save.SlidesAsImages = true;
doc.Save(dataDir + "PDFToPPT_out_.pptx", pptx_save);
```
## PPTX 변환의 진행 상세

Aspose.PDF for .NET은 PDF에서 PPTX로의 변환 진행 상황을 추적할 수 있게 해줍니다. [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions) 클래스는 변환 과정의 진행 상황을 추적하기 위해 사용자 정의 메소드를 지정할 수 있는 [CustomProgressHandler](https://reference.aspose.com/pdf/net/aspose.pdf/pptxsaveoptions/properties/customprogresshandler) 속성을 제공합니다. 다음 코드 샘플에서 보여주는 것처럼 말이죠.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
// PDF 문서를 로드합니다
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// PptxSaveOptions 인스턴스를 생성합니다
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();

//사용자 정의 진행 상태 처리기를 지정합니다
pptx_save.CustomProgressHandler = ShowProgressOnConsole;
// 출력을 PPTX 포맷으로 저장합니다
doc.Save(dataDir + "PDFToPPTWithProgressTracking_out_.pptx", pptx_save);
```
다음은 진행률 변환을 표시하기 위한 사용자 정의 방법입니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
switch (eventInfo.EventType)
{
    case ProgressEventType.TotalProgress:
        Console.WriteLine(String.Format("{0}  - 변환 진행률 : {1}% .", DateTime.Now.TimeOfDay, eventInfo.Value.ToString()));
        break;
    case ProgressEventType.ResultPageCreated:
        Console.WriteLine(String.Format("{0}  - 결과 페이지의 {1} 중 {2} 레이아웃이 생성되었습니다.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.ResultPageSaved:
        Console.WriteLine(String.Format("{0}  - 결과 페이지 {1} 중 {2}가 내보내졌습니다.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.SourcePageAnalysed:
        Console.WriteLine(String.Format("{0}  - 소스 페이지 {1} 중 {2}가 분석되었습니다.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));

        break;
    default:
        break;
}
```
## 참조하십시오

이 문서는 다음 주제도 다룹니다. 코드는 위와 동일합니다.

_형식_: **PowerPoint**
- [C# PDF를 PowerPoint 코드로](#csharp-pdf-to-powerpoint)
- [C# PDF를 PowerPoint API로](#csharp-pdf-to-powerpoint)
- [C# PDF를 프로그래밍 방식으로 PowerPoint로](#csharp-pdf-to-powerpoint)
- [C# PDF를 PowerPoint 라이브러리로](#csharp-pdf-to-powerpoint)
- [C# PDF를 PowerPoint로 저장](#csharp-pdf-to-powerpoint)
- [C# PDF에서 PowerPoint 생성](#csharp-pdf-to-powerpoint)
- [C# PDF에서 PowerPoint 만들기](#csharp-pdf-to-powerpoint)
- [C# PDF를 PowerPoint 변환기로](#csharp-pdf-to-powerpoint)

_형식_: **PPTX**
- [C# PDF를 PPTX 코드로](#csharp-pdf-to-pptx)
- [C# PDF를 PPTX API로](#csharp-pdf-to-pptx)
- [C# PDF를 프로그래밍 방식으로 PPTX로](#csharp-pdf-to-pptx)
- [C# PDF를 PPTX 라이브러리로](#csharp-pdf-to-pptx)
- [C# PDF를 PPTX로 저장](#csharp-pdf-to-pptx)
- [C# PDF에서 PPTX 생성](#csharp-pdf-to-pptx)
- [C# PDF에서 PPTX 만들기](#csharp-pdf-to-pptx)
- [C# PDF를 PPTX 변환기로](#csharp-pdf-to-pptx)
