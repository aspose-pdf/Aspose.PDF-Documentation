---
title: PDF를 Microsoft Word 문서로 변환하기 (.NET)
linktitle: PDF를 Word로 변환하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: C# 코드를 사용하여 Aspose.PDF for .NET와 함께 PDF를 Microsoft Word 형식으로 변환하는 방법과 PDF를 DOC(DOCX)로 변환하는 기능을 조정하는 방법을 알아보세요.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert PDF to Microsoft Word Documents in .NET",
    "alternativeHeadline": "Seamlessly Convert PDFs to Word Documents with C#",
    "abstract": "Aspose.PDF for .NET는 C#을 사용하여 PDF 파일을 Microsoft Word 형식(DOC 및 DOCX)으로 변환하는 강력한 기능을 소개합니다. 이 기능은 문서 편집을 향상시킬 뿐만 아니라 텍스트 인식 및 형식 지정에 대한 유연한 옵션을 제공하여 원본 PDF와 결과 Word 문서 간의 높은 충실도를 보장합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1114",
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
    "url": "/net/convert-pdf-to-word/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-pdf-to-word/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 개요

이 기사에서는 **C#을 사용하여 PDF를 Microsoft Word 문서로 변환하는 방법**에 대해 설명합니다. 다음 주제를 다룹니다.

- [PDF를 DOC로 변환하기](#csharp-pdf-to-doc)
- [PDF를 DOCX로 변환하기](#csharp-pdf-to-docx)

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 함께 작동합니다.

## PDF를 DOC 및 DOCX로 변환하기

가장 인기 있는 기능 중 하나는 PDF를 Microsoft Word DOC 포맷으로 변환하는 기능으로, 콘텐츠 관리를 보다 쉽게 만들어 줍니다. **Aspose.PDF for .NET**을(를) 사용하면 PDF 파일을 DOC 및 DOCX 형식으로 빠르고 효율적으로 변환할 수 있습니다.

## PDF를 DOC (Microsoft Word 97-2003) 파일로 변환하기

PDF 파일을 손쉽게 DOC 형식으로 변환하고 완벽한 제어를 할 수 있습니다. Aspose.PDF for .NET은(는) 유연하며 다양한 변환을 지원합니다. 예를 들어, PDF 문서의 페이지를 이미지로 변환하는 기능은 매우 인기 있는 기능입니다.

많은 고객들이 PDF를 DOC로 변환하는 기능을 요청해 왔습니다: PDF 파일을 Microsoft Word 문서로 변환하는 것입니다. 이는 PDF 파일은 쉽게 편집할 수 없지만 Word 문서는 편집할 수 있기 때문입니다. 일부 회사는 사용자들이 PDF로 시작된 파일의 텍스트, 표 및 이미지를 조작할 수 있기를 원합니다.

모든 것을 간단하고 이해하기 쉽게 만드는 전통을 이어가며, Aspose.PDF for .NET은 소스 PDF 파일을 두 줄의 코드로 DOC 파일로 변환할 수 있게 해줍니다. 이 기능을 구현하기 위해 SaveFormat이라는 열거형이 도입되었으며, 그 값인 .Doc을 사용하면 소스 파일을 Microsoft Word 형식으로 저장할 수 있습니다.

다음 C# 코드 스니펫은 PDF 파일을 DOC 형식으로 변환하는 예를 보여줍니다.

<a name="csharp-pdf-to-doc" id="csharp-pdf-to-doc"><strong>PDF를 DOC로 변환하기</strong></a>

1. 소스 PDF 문서를 사용하여 [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/) 객체의 인스턴스를 생성합니다.
2. **Document.Save()** 메서드를 호출하여 **SaveFormat.Doc** 형식으로 저장합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    usnig (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Save the file into MS document format
        document.Save(dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);
    }
}
```

### DocSaveOptions 클래스를 사용하는 방법

[`DocSaveOptions`](https://reference.aspose.com/pdf/ko/net/aspose.pdf/docsaveoptions) 클래스는 PDF 파일을 DOC 형식으로 변환하는 기능을 향상시키는 다양한 속성을 제공합니다. 이러한 속성 중 Mode는 PDF 콘텐츠의 인식 모드를 지정할 수 있게 해줍니다. 이 속성에는 RecognitionMode 열거형의 값을 선택할 수 있습니다. 각각의 값은 특정한 장점과 한계를 가지고 있습니다:

- [`Textbox`](https://reference.aspose.com/pdf/ko/net/aspose.pdf.docsaveoptions/recognitionmode) 모드는 빠르며 PDF 파일의 원본 모양을 보존하는 데 좋지만, 결과 문서의 편집 가능성은 제한적일 수 있습니다. 원본 PDF에 있는 시각적으로 그룹화된 모든 텍스트 블록이 출력 문서에서 텍스트 상자로 변환됩니다. 이로 인해 출력 문서가 원본과 최대한 유사하게 보이지만, 완전히 텍스트 상자로 구성되어 있어 Microsoft Word에서 편집하기가 상당히 어렵습니다.
- [`Flow`](https://reference.aspose.com/pdf/ko/net/aspose.pdf.docsaveoptions/recognitionmode) 모드는 전체 인식 모드로, 엔진이 그룹화 및 다단계 분석을 수행하여 작성자의 의도에 맞게 원본 문서를 복원하면서 쉽게 편집 가능한 문서를 생성합니다. 단점은 출력 문서가 원본과 다르게 보일 수 있다는 점입니다.

[`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/ko/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) 속성은 텍스트 요소들 간의 상대적 간격을 조절하는 데 사용할 수 있습니다. 이는 거리가 글꼴 크기에 의해 정규화된다는 의미입니다. 더 큰 글꼴은 음절 사이에 더 큰 간격을 가질 수 있으며 여전히 하나의 단위로 간주될 수 있습니다. 글꼴 크기의 백분율로 지정되며, 예를 들어 1은 100%를 의미합니다. 즉, 12pt 크기의 두 문자가 12pt 간격으로 배치되면 서로 근접한 것으로 간주됩니다.
- [`RecognitionBullets`](https://reference.aspose.com/pdf/ko/net/aspose.pdf/docsaveoptions/properties/recognizebullets)은 변환 중에 글머리표 인식을 활성화하는 데 사용됩니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWordDocAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDF-to-DOC.pdf"))
    {
        var saveOptions = new Aspose.Pdf.DocSaveOptions
        {
            // Set format to save MS document
            Format = Aspose.Pdf.DocSaveOptions.DocFormat.Doc,
            // Set the recognition mode as Flow
            Mode = Aspose.Pdf.DocSaveOptions.RecognitionMode.Flow,
            // Set the Horizontal proximity as 2.5
            RelativeHorizontalProximity = 2.5f,
            // Enable the value to recognize bullets during the conversion process
            RecognizeBullets = true
        };
        // Save the file into MS document with save options
        document.Save(dataDir + "PDFtoDOC_out.doc", saveOptions);
    }
}
```

{{% alert color="success" %}}
**온라인에서 PDF를 DOC로 변환해보세요**

Aspose.PDF for .NET은(는) 온라인 무료 애플리케이션 ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)를 제공하여 기능과 품질을 확인해 볼 수 있습니다.

[![PDF를 DOC로 변환하기](/pdf/ko/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## PDF를 DOCX (Microsoft Word 2007-2024) 파일로 변환하기

Aspose.PDF for .NET API를 사용하면 C# 및 모든 .NET 언어를 사용하여 PDF 문서를 DOCX로 읽고 변환할 수 있습니다. DOCX는 Microsoft Word 문서에 널리 알려진 형식으로, 구조가 순수 이진 형식에서 XML과 이진 파일의 조합으로 변경되었습니다. Docx 파일은 Word 2007 이상 버전에서 열 수 있지만, DOC 파일 확장자를 지원하는 이전 버전의 MS Word에서는 열 수 없습니다.

다음 C# 코드 스니펫은 PDF 파일을 DOCX 형식으로 변환하는 예를 보여줍니다.

<a name="csharp-pdf-to-docx" id="csharp-pdf-to-docx"><strong>PDF를 DOCX로 변환하기</strong></a>

1. 소스 PDF 문서를 사용하여 [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/) 객체의 인스턴스를 생성합니다.
2. **Document.Save()** 메서드를 호출하여 **SaveFormat.DocX** 형식으로 저장합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord_DOCX_Format()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Save the file into MS document format
        document.Save(dataDir + "PDFtoDOC_out.docx", SaveFormat.DocX);
    }
}
```

### 향상된 모드로 PDF를 DOCX로 변환하기

PDF를 DOCX로 변환할 때 더 나은 결과를 얻기 위해 `EnhancedFlow` 모드를 사용할 수 있습니다.
Flow 모드와 EnhancedFlow 모드의 주요 차이점은 테이블(테두리가 있거나 없는)이 배경의 이미지와 함께 있는 텍스트가 아닌 실제 테이블로 인식된다는 것입니다.
또한 번호 매기기 목록 및 기타 여러 소소한 요소들이 인식됩니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPDFtoWord_Advanced_DOCX_Format()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "PDFToDOC.pdf"))
    {
        // Instantiate DocSaveOptions object
        DocSaveOptions saveOptions = new Aspose.Pdf.DocSaveOptions
        {
            // Set format to save MS document
            Format = Aspose.Pdf.DocSaveOptions.DocFormat.DocX,
            // Set the recognition mode as EnhancedFlow
            Mode = Aspose.Pdf.DocSaveOptions.RecognitionMode.EnhancedFlow
        };

        // Save the file into MS document format
        document.Save(dataDir + "PDFToDOC_out.docx", saveOptions);
    }
}
```

{{% alert color="warning" %}}
**온라인에서 PDF를 DOCX로 변환해보세요**

Aspose.PDF for .NET은(는) 온라인 무료 애플리케이션 ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)를 제공하여 기능과 품질을 확인해 볼 수 있습니다.

[![Aspose.PDF를 사용한 PDF를 Word로 변환하는 무료 앱](/pdf/ko/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}