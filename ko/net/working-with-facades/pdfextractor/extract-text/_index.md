---
title: PDF 파일에서 텍스트 추출
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/extract-text/
description: 이 섹션에서는 PdfExtractor 클래스를 사용하여 PDF에서 텍스트를 추출하는 방법을 설명합니다.
lastmod: "2021-06-05"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text from PDF File",
    "alternativeHeadline": "Effortless Text Extraction from PDF Files",
    "abstract": "PdfExtractor 클래스는 여러 방법을 통해 PDF 파일에서 효율적으로 텍스트를 추출할 수 있게 해주며, 사용자가 텍스트, 이미지 및 첨부 파일을 쉽게 검색할 수 있도록 합니다. ExtractText, GetText 및 GetNextPageText와 같은 메서드를 활용함으로써 개발자는 개별 페이지 또는 전체 문서에서 텍스트 콘텐츠를 원활하게 추출하고 저장할 수 있어 PDF 조작 작업을 간소화합니다. 유연한 추출 모드가 제공되어 출력 형식에 대한 제어를 강화하며, PDF 데이터를 다루는 모든 사람에게 필수 도구가 됩니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "441",
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
    "url": "/net/extract-text/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

이 기사에서는 PDF 파일에서 텍스트를 추출하는 세부 사항을 살펴보겠습니다. 이러한 모든 추출 기능은 [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 클래스에서 한 곳에서 제공됩니다. 이러한 기능을 코드에서 사용하는 방법을 살펴보겠습니다.

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 클래스는 세 가지 유형의 추출 기능을 제공합니다. 이 세 가지 범주는 텍스트, 이미지 및 첨부 파일입니다. 이 세 가지 범주 각각에서 추출을 수행하기 위해 PdfExtractor는 최종 출력을 제공하기 위해 함께 작동하는 다양한 메서드를 제공합니다.

예를 들어, 텍스트를 추출하려면 [ExtractText, GetText, HasNextPageText 및 GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/index)와 같은 세 가지 메서드를 사용할 수 있습니다. 이제 텍스트 추출을 시작하려면 먼저 [ExtractText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extracttext/index) 메서드를 호출해야 합니다. 이 메서드는 PDF 파일에서 텍스트를 추출하여 메모리에 저장합니다. 그 후, [GetText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/gettext/index) 메서드는 이 추출된 텍스트를 가져와 지정된 위치의 파일에 저장합니다. [HasNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextpagetext) 메서드는 각 페이지를 반복하며 다음 페이지에 텍스트가 있는지 확인하는 데 도움을 줍니다. 텍스트가 포함되어 있으면 [GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getnextpagetext/index) 메서드는 개별 페이지의 텍스트를 파일에 저장하는 데 도움을 줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    bool wholeText = true;
    // Create an object of the PdfExtractor class
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "sample.pdf");

        // ExtractText
        pdfExtractor.ExtractText();

        if (!wholeText)
        {
            pdfExtractor.GetText(dataDir + "sample.txt");
        }
        else
        {
            // Extract the text into separate files
            int pageNumber = 1;
            while (pdfExtractor.HasNextPageText())
            {
                pdfExtractor.GetNextPageText($"{dataDir}\\sample{pageNumber:D3}.txt");
                pageNumber++;
            }
        }
    }
}
```

텍스트 추출 모드를 추출하려면 다음 코드를 사용하십시오:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextExtractonMode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    bool wholeText = true;
    // Create an object of the PdfExtractor class
    using (var pdfExtractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        pdfExtractor.BindPdf(dataDir + "ExtractTextExtractonMode.pdf");

        // ExtractText
        // pdfExtractor.ExtractTextMode = 0; // pure mode
        pdfExtractor.ExtractTextMode = 1; // raw mode
        pdfExtractor.ExtractText();

        if (!wholeText)
        {
            pdfExtractor.GetText(dataDir + "ExtractTextExtractonMode_out.txt");
        }
        else
        {
            // Extract the text into separate files
            int pageNumber = 1;
            while (pdfExtractor.HasNextPageText())
            {
                pdfExtractor.GetNextPageText($"{dataDir}\\sample{pageNumber:D3}.txt");
                pageNumber++;
            }
        }
    }
}
```