---
title: .NET에서 PDF를 HTML로 변환
linktitle: PDF를 HTML 형식으로 변환
type: docs
weight: 50
url: /net/convert-pdf-to-html/
lastmod: "2021-11-01"
description: 이 주제는 Aspose.PDF C# 라이브러리를 사용하여 PDF 파일을 HTML 형식으로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 개요

이 글은 **C#을 사용하여 PDF를 HTML로 변환하는 방법**을 설명합니다. 다음 주제를 다룹니다.

_형식_: **HTML**
- [C# PDF를 HTML로](#csharp-pdf-to-html)
- [C# PDF를 HTML로 변환](#csharp-pdf-to-html)
- [C# PDF 파일을 HTML로 변환하는 방법](#csharp-pdf-to-html)

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 함께 작동합니다.

## PDF를 HTML로 변환

**Aspose.PDF for .NET**은 다양한 파일 형식을 PDF 문서로 변환하고 PDF 파일을 다양한 출력 형식으로 변환하는 많은 기능을 제공합니다.
**Aspose.PDF for .NET**은 다양한 파일 포맷을 PDF 문서로 변환하고 PDF 파일을 다양한 출력 포맷으로 변환하는 많은 기능을 제공합니다.

**Aspose.PDF for .NET**은 PDF 파일을 HTML로 변환하는 기능을 지원합니다. Aspose.PDF 라이브러리를 사용하여 수행할 수 있는 주요 작업은 다음과 같이 나열됩니다:

- PDF를 HTML로 변환;
- 여러 페이지 HTML로 출력 분할;
- SVG 파일 저장을 위한 폴더 지정;
- 변환 중 SVG 이미지 압축;
- 이미지 폴더 지정;
- 본문 내용만 있는 후속 파일 생성;
- 투명 텍스트 렌더링;
- PDF 문서 레이어 렌더링.

{{% alert color="success" %}}
**온라인에서 PDF를 HTML로 변환해 보세요**

Aspose.PDF for .NET은 기능성과 품질을 조사해 볼 수 있는 무료 온라인 애플리케이션 ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html)을 제공합니다.

[![Aspose.PDF 무료 앱으로 PDF를 HTML로 변환](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

Aspose.PDF for .NET은 소스 PDF 파일을 HTML로 변환하기 위한 두 줄 코드를 제공합니다.
Aspose.PDF for .NET은 소스 PDF 파일을 HTML로 변환하기 위한 두 줄 코드를 제공합니다.

<a name="csharp-pdf-to-html"><strong>단계: C#에서 PDF를 HTML로 변환</strong></a>

1. 소스 PDF 문서로 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) 객체의 인스턴스를 생성합니다.
2. **Document.Save()** 메소드를 호출하여 **SaveFormat.Html** 형식으로 저장합니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// 소스 PDF 문서를 엽니다
Document pdfDocument = new Document(dataDir + "PDFToHTML.pdf");

// 파일을 MS 문서 형식으로 저장합니다
pdfDocument.Save(dataDir + "output_out.html", SaveFormat.Html);
```

### 멀티 페이지 HTML로 출력 분할

여러 페이지를 포함하는 큰 PDF 파일을 HTML 형식으로 변환할 때, 출력은 단일 HTML 페이지로 나타납니다.
여러 페이지의 큰 PDF 파일을 HTML 형식으로 변환할 때 출력은 단일 HTML 페이지로 표시됩니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// 소스 PDF 문서 열기
Document pdfDocument = new Document(dataDir + "PDFToHTML.pdf");

// HTML SaveOptions 객체 인스턴스화
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// 출력을 여러 페이지로 분할하도록 지정
htmlOptions.SplitIntoPages = true;

// 문서 저장
pdfDocument.Save(@"MultiPageHTML_out.html", htmlOptions);
```

### SVG 파일 저장 폴더 지정

PDF를 HTML로 변환하는 동안 SVG 이미지가 저장될 폴더를 지정할 수 있습니다.
PDF에서 HTML로 변환하는 동안 SVG 이미지를 저장할 폴더를 지정할 수 있습니다.

```csharp
// PDF 파일 로드
Document doc = new Document(dataDir + "PDFToHTML.pdf");

// HTML 저장 옵션 객체 생성
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// PDF에서 HTML로 변환하는 동안 SVG 이미지가 저장되는 폴더 지정
newOptions.SpecialFolderForSvgImages = dataDir;

// 출력 파일 저장
doc.Save(dataDir + "SaveSVGFiles_out.html", newOptions);
```

### 변환 중 SVG 이미지 압축

PDF에서 HTML로 변환하는 동안 SVG 이미지를 압축하려면 다음 코드를 사용해 보세요:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요
// 테스트된 기능이 있는 HtmlSaveOption 생성
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// SVG 이미지가 있을 경우 압축
newOptions.CompressSvgGraphicsIfAny = true;
```

### 이미지 폴더 지정

PDF에서 HTML로 변환하는 동안 이미지를 저장할 폴더도 지정할 수 있습니다:
PDF에서 HTML로 변환하는 동안 이미지가 저장될 폴더를 지정할 수도 있습니다:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET에서 확인하세요.
// 테스트된 기능을 가진 HtmlSaveOption 생성
HtmlSaveOptions newOptions = new HtmlSaveOptions();

// 이미지를 저장할 별도의 폴더 지정
newOptions.SpecialFolderForAllImages = dataDir;
```

### 본문 내용만 있는 후속 파일 생성

최근 PDF 파일을 HTML로 변환하고 사용자가 각 페이지의 `<body>` 태그 내용만 얻을 수 있는 기능을 도입해달라는 요청이 있었습니다. 이렇게 하면 CSS, `<html>`, `<head>` 세부 정보가 포함된 하나의 파일과 다른 파일에는 `<body>` 내용만 있는 페이지가 생성됩니다.

이 요구 사항을 충족하기 위해 HtmlSaveOptions 클래스에 HtmlMarkupGenerationMode라는 새 속성이 도입되었습니다.

다음 간단한 코드 스니펫을 사용하면 출력 HTML을 페이지로 분할할 수 있습니다.
다음 간단한 코드 스니펫을 사용하여 출력 HTML을 페이지로 분할할 수 있습니다.

```csharp
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
           
HtmlSaveOptions options = new HtmlSaveOptions();
// 이 설정은 테스트되었습니다
options.HtmlMarkupGenerationMode = HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent;
options.SplitIntoPages = true;

doc.Save(dataDir + "CreateSubsequentFiles_out.html", options);
```

### 투명 텍스트 렌더링

원본/입력 PDF 파일에 전경 이미지에 의해 가려진 투명 텍스트가 포함된 경우 텍스트 렌더링 문제가 발생할 수 있습니다. 이러한 시나리오를 처리하기 위해 SaveShadowedTextsAsTransparentTexts 및 SaveTransparentTexts 속성을 사용할 수 있습니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();
htmlOptions.SaveShadowedTextsAsTransparentTexts = true;
htmlOptions.SaveTransparentTexts = true;
doc.Save(dataDir + "TransparentTextRendering_out.html", htmlOptions);
```
### PDF 문서 레이어 렌더링

PDF 문서 레이어를 PDF에서 HTML 변환 중 별도의 레이어 타입 요소로 렌더링할 수 있습니다:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

Document doc = new Document(dataDir + "PDFToHTML.pdf");
// HTML SaveOptions 객체를 인스턴스화
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// 출력 HTML에서 PDF 문서 레이어를 별도로 렌더링하도록 지정
htmlOptions.ConvertMarkedContentToLayers = true;

// 문서 저장
doc.Save(dataDir + "LayersRendering_out.html", htmlOptions);
```

## 참고

이 문서는 위와 같은 코드로 다음 주제도 다룹니다.

_형식_: **HTML**
- [C# PDF를 HTML로 코드](#csharp-pdf-to-html)
- [C# PDF를 HTML로 API](#csharp-pdf-to-html)
- [C# PDF를 HTML로 프로그래밍적으로](#csharp-pdf-to-html)
- [C# PDF를 HTML로 라이브러리](#csharp-pdf-to-html)
- [C# PDF를 HTML로 저장](#csharp-pdf-to-html)
- [C# PDF를 HTML로 저장](#csharp-pdf-to-html)
- [C# PDF에서 HTML 생성](#csharp-pdf-to-html)
- [C# PDF에서 HTML 만들기](#csharp-pdf-to-html)
- [C# PDF를 HTML로 변환](#csharp-pdf-to-html)
