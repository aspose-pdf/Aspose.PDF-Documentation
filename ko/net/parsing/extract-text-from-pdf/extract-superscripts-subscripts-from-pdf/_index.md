---
title: PDF에서 SuperScripts 및 SubScripts 텍스트 추출
linktitle: SuperScripts 및 SubScripts 추출
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/extract-superscripts-subscripts-from-pdf/
description: 이 문서에서는 C#에서 Aspose.PDF를 사용하여 PDF에서 SuperScripts 및 SubScripts 텍스트를 추출하는 다양한 방법을 설명합니다.
lastmod: "2022-10-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract SuperScripts and SubScripts text from PDF",
    "alternativeHeadline": "Extract SuperScripts and SubScripts from PDF Documents",
    "abstract": "Aspose.PDF for .NET 라이브러리를 사용하여 PDF 문서에서 SuperScripts 및 SubScripts 텍스트를 추출하는 새로운 기능은 사용자가 기술 문서에서 발견되는 특수 텍스트 형식을 정확하게 검색할 수 있도록 합니다. 이 향상된 기능은 개발자에게 이러한 텍스트 요소를 쉽게 조작할 수 있는 도구를 제공하여 수학적 표현식 및 화학 사양을 처리하는 과정을 단순화합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "323",
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
    "url": "/net/extract-superscripts-subscripts-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-superscripts-subscripts-from-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## SuperScripts 및 SubScripts 텍스트 추출

PDF 문서에서 텍스트를 추출하는 것은 일반적인 일입니다. 그러나 추출된 텍스트에서 기술 문서 및 기사에 일반적인 **SuperScripts 및 SubScripts**가 표시되지 않을 수 있습니다. SubScript 또는 SuperScript는 일반 텍스트 줄 아래 또는 위에 배치된 문자, 숫자 또는 글자입니다. 일반적으로 나머지 텍스트보다 작습니다.

**SubScripts 및 SuperScripts**는 주로 수식, 수학적 표현 및 화학 화합물의 사양에 사용됩니다. 같은 텍스트 구절에 여러 개가 있을 때 이를 편집하는 것은 어렵습니다.
최신 릴리스 중 하나에서 **Aspose.PDF for .NET** 라이브러리는 PDF에서 SuperScripts 및 SubScripts 텍스트를 추출하는 기능을 추가했습니다.

**TextFragmentAbsorber** 클래스를 사용하면 찾은 텍스트로 모든 작업을 수행할 수 있습니다. 즉, 전체 텍스트를 간단히 사용할 수 있습니다. 다음 코드 스니펫을 시도해 보십시오:

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSuperScriptsAndSubScripts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SuperScriptExample.pdf"))
    {
        // Create an absorber
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(dataDir + "SuperScriptExample_out.txt"))
        {
            // Write the extracted text in text file
            writer.WriteLine(absorber.Text);
        }
    }
}
```

또는 **TextFragments**를 개별적으로 사용하여 좌표나 크기로 정렬하는 등 다양한 조작을 수행할 수 있습니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSuperScriptsAndSubScriptsWithTextFragments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SuperScriptExample.pdf"))
    {
        // Create an absorber
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        document.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(dataDir + "SuperScriptExample_out.txt"))
        {
            foreach (var textFragment in absorber.TextFragments)
            {
                // Write the extracted text in text file
                writer.Write(textFragment.Text);
            }

        }
    }
}
```