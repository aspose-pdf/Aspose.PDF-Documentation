---
title: PDF 파일에 이미지 또는 텍스트가 포함되어 있는지 확인
linktitle: 텍스트 및 이미지 존재 여부 확인
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/find-whether-pdf-file-contains-images-or-text-only/
description: 이 주제는 PdfExtractor 클래스를 사용하여 PDF 파일에 이미지 또는 텍스트만 포함되어 있는지 확인하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Find whether PDF contains images or text",
    "alternativeHeadline": "Determine PDF Content: Text, Images, or Both",
    "abstract": "PdfExtractor 클래스를 사용하여 PDF 파일에 텍스트, 이미지 또는 둘 다 포함되어 있는지 효율적으로 확인할 수 있는 기능을 발견하십시오. 이 기능은 PDF 콘텐츠 분석 프로세스를 단순화하여 파일 내 텍스트 및 이미지의 존재에 대한 명확한 출력을 제공합니다. 몇 줄의 코드만으로 사용자는 콘텐츠 유형에 따라 PDF 문서를 효과적으로 분류할 수 있습니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "265",
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
    "url": "/net/find-whether-pdf-file-contains-images-or-text-only/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/find-whether-pdf-file-contains-images-or-text-only/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## 배경

PDF 파일은 텍스트와 이미지를 모두 포함할 수 있습니다. 때때로 사용자는 PDF 파일에 텍스트만 포함되어 있는지, 아니면 이미지만 포함되어 있는지를 확인해야 할 수 있습니다. 또한 둘 다 포함되어 있는지 또는 아무것도 포함되어 있지 않은지도 확인할 수 있습니다.

{{% alert color="primary" %}}

다음 코드 스니펫은 이 요구 사항을 충족하는 방법을 보여줍니다.

{{% /alert %}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckIfPdfContainsTextOrImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Instantiate a memoryStream object to hold the extracted text from Document
    using (var ms = new MemoryStream())
    {
        // Create the PdfExtractor
        using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
        {
            // Bind PDF document
            extractor.BindPdf(dataDir + "FilledForm.pdf");
            // Extract text from the input PDF document
            extractor.ExtractText();
            // Save the extracted text to a text file
            extractor.GetText(ms);
            // Check if the MemoryStream length is greater than or equal to 1

            bool containsText = ms.Length >= 1;

            // Extract images from the input PDF document
            extractor.ExtractImage();

            // Calling HasNextImage method in while loop. When images will finish, loop will exit
            bool containsImage = extractor.HasNextImage();

            // Now find out whether this PDF is text only or image only

            if (containsText && !containsImage)
            {
                Console.WriteLine("PDF contains text only");
            }
            else if (!containsText && containsImage)
            {
                Console.WriteLine("PDF contains image only");
            }
            else if (containsText && containsImage)
            {
                Console.WriteLine("PDF contains both text and image");
            }
            else if (!containsText && !containsImage)
            {
                Console.WriteLine("PDF contains neither text or nor image");
            }
        }
    }
}
```