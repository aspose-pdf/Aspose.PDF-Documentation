---
title: C#를 사용하여 PDF 생성하는 방법
linktitle: PDF 문서 생성
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/create-pdf-document/
description: Aspose.PDF for .NET로 PDF 문서를 생성하고 형식을 지정합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Create PDF using C#",
    "alternativeHeadline": "Create and Format PDFs Effortlessly with C#",
    "abstract": "Aspose.PDF for .NET의 새로운 기능은 개발자가 C#을 사용하여 PDF 문서를 손쉽게 생성하고 형식을 지정할 수 있도록 합니다. 이 직관적인 API를 사용하면 사용자는 검색 가능한 PDF를 생성하고 접근성을 위한 태그가 있는 콘텐츠를 조작하며 다양한 .NET 애플리케이션에 PDF 생성을 원활하게 통합하여 생산성을 높이고 워크플로를 간소화할 수 있습니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF creation, C# PDF generation, Aspose.PDF for .NET, searchable PDF, accessible PDF, Document class, TextFragment, PDF document manipulation, .NET applications, BDC operations",
    "wordcount": "871",
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
    "url": "/net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET로 PDF 문서를 생성하고 형식을 지정합니다."
}
</script>

우리는 항상 C# 프로젝트에서 PDF 문서를 생성하고 작업하는 더 정확하고 효과적인 방법을 찾고 있습니다. 라이브러리의 사용하기 쉬운 기능을 통해 우리는 작업의 많은 부분을 추적할 수 있으며, PDF를 생성하는 데 소요되는 시간과 세부 사항에 덜 집중할 수 있습니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## C# 언어를 사용하여 PDF 문서 생성(또는 생성)

Aspose.PDF for .NET API를 사용하면 C# 및 VB.NET을 사용하여 PDF 파일을 생성하고 읽을 수 있습니다. 이 API는 WinForms, ASP.NET 및 여러 다른 .NET 애플리케이션에서 사용할 수 있습니다. 이 기사에서는 Aspose.PDF for .NET API를 사용하여 .NET 애플리케이션에서 PDF 파일을 쉽게 생성하고 읽는 방법을 보여줍니다.

### 간단한 PDF 파일 생성 방법

C#을 사용하여 PDF 파일을 생성하려면 다음 단계를 사용할 수 있습니다.

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스의 객체를 생성합니다.
1. Document 객체의 [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) 컬렉션에 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체를 추가합니다.
1. 페이지의 [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) 컬렉션에 [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment)를 추가합니다.
1. 결과 PDF 문서를 저장합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateHelloWorldDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Add text to new page
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
        // Save PDF document
        document.Save(dataDir + "HelloWorld_out.pdf");
    }
}
```

### 검색 가능한 PDF 문서 생성 방법

Aspose.PDF for .NET는 기존 PDF 문서를 생성하고 조작하는 기능을 제공합니다. PDF 파일 내에 텍스트 요소를 추가할 때 결과 PDF는 검색 가능합니다. 그러나 텍스트가 포함된 이미지를 PDF 파일로 변환하는 경우 PDF 내의 내용은 검색할 수 없습니다. 그러나 해결 방법으로 결과 파일에 OCR을 사용할 수 있어 검색 가능하게 만들 수 있습니다.

아래에 명시된 이 논리는 PDF 이미지의 텍스트를 인식합니다. 인식을 위해 외부 OCR 지원 HOCR 표준을 사용할 수 있습니다. 테스트 목적으로 무료 Google Tesseract OCR을 사용했습니다. 따라서 먼저 시스템에 Tesseract-OCR을 설치해야 하며, Tesseract 콘솔 애플리케이션이 필요합니다.

다음은 이 요구 사항을 충족하기 위한 전체 코드입니다:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateSearchableDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SearchableDocument.pdf"))
    {
        document.Convert(CallBackGetHocr);

        // Save PDF document
        document.Save(dataDir + "SearchableDocument_out.pdf");
    }
}

private static string CallBackGetHocr(System.Drawing.Image img)
{
    var tmpFile = Path.GetTempFileName();
    try
    {
        using (var bmp = new System.Drawing.Bitmap(img))
        {
            bmp.Save(tmpFile, System.Drawing.Imaging.ImageFormat.Bmp);
        }

        var inputFile = string.Concat('"', tmpFile, '"');
        var outputFile = string.Concat('"', tmpFile, '"');
        var arguments = string.Concat(inputFile, " ", outputFile, " -l eng hocr");
        var tesseractProcessName = RunExamples.GetTesseractExePath();

        var psi = new System.Diagnostics.ProcessStartInfo(tesseractProcessName, arguments)
        {
            UseShellExecute = true,
            CreateNoWindow = true,
            WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden,
            WorkingDirectory = Path.GetDirectoryName(tesseractProcessName)
        };

        var p = new System.Diagnostics.Process
        {
            StartInfo = psi
        };
        p.Start();
        p.WaitForExit();

        using (var streamReader = new StreamReader(tmpFile + ".hocr"))
        {
            string text = streamReader.ReadToEnd();
            return text;
        }
    }
    finally
    {
        if (File.Exists(tmpFile))
        {
            File.Delete(tmpFile);
        }
        if (File.Exists(tmpFile + ".hocr"))
        {
            File.Delete(tmpFile + ".hocr");
        }
    }
}
```

### 저수준 기능을 사용하여 접근 가능한 PDF 생성 방법

이 코드 스니펫은 PDF 문서와 그 태그가 있는 콘텐츠를 처리하기 위해 Aspose.PDF 라이브러리를 사용합니다.

예제는 PDF의 첫 번째 페이지의 태그가 있는 콘텐츠에 새 span 요소를 생성하고 모든 BDC 요소를 찾아 span과 연결합니다. 수정된 문서는 저장됩니다.

BDCProperties 객체를 사용하여 mcid, lang 및 확장 텍스트를 지정하는 bdc 문을 생성할 수 있습니다:

```cs
var bdc = new Aspose.Pdf.Operators.BDC("P", new Aspose.Pdf.Facades.BDCProperties(1, "de", "Hallo, welt!"));
```

구조 트리를 생성한 후, 요소 객체의 Tag 메서드를 사용하여 BDC 연산자를 구조의 지정된 요소에 바인딩할 수 있습니다:

```cs
Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
span.Tag(bdc);
```

접근 가능한 PDF를 생성하는 단계:

1. PDF 문서를 로드합니다.
1. 태그가 있는 콘텐츠에 접근합니다.
1. Span 요소를 생성합니다.
1. Span을 루트 요소에 추가합니다.
1. 페이지 내용을 반복합니다.
1. BDC 요소를 확인하고 태그를 지정합니다.
1. 수정된 문서를 저장합니다.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAnAccessibleDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "tourguidev2_gb_tags.pdf"))
    {
        // Access tagged content
        Aspose.Pdf.Tagged.ITaggedContent content = document.TaggedContent;
        // Create a span element
        Aspose.Pdf.LogicalStructure.SpanElement span = content.CreateSpanElement();
        // Append span to root element
        content.RootElement.AppendChild(span);
        // Iterate over page contents
        foreach (var op in document.Pages[1].Contents)
        {
            var bdc = op as Aspose.Pdf.Operators.BDC;
            if (bdc != null)
            {
                span.Tag(bdc);
            }
        }
        // Save PDF document
        document.Save(dataDir + "AccessibleDocument_out.pdf");
    }
}
```

이 코드는 문서의 태그가 있는 콘텐츠 내에 span 요소를 생성하고 첫 번째 페이지의 특정 콘텐츠(BDC 작업)를 이 span으로 태그 지정하여 PDF를 수정합니다. 수정된 PDF는 새 파일로 저장됩니다.

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>