---
title: 다중 행 워터마크 추가
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/adding-multi-line-watermark-to-existing-pdf/
description: 이 섹션에서는 FormattedText 클래스를 사용하여 기존 PDF에 다중 행 워터마크를 추가하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding multi line watermark",
    "alternativeHeadline": "Enhance PDFs with Multi-Line Watermarks Easily",
    "abstract": "Aspose.Pdf.Facades 네임스페이스를 사용하여 기존 PDF에 다중 행 워터마크를 추가하는 기능을 소개합니다. 이 새로운 기능은 프로세스를 단순화하여 사용자가 FormattedText 클래스의 새로 구현된 AddNewLineText() 메서드를 사용하여 문서에 여러 줄의 텍스트를 쉽게 통합할 수 있도록 합니다. 맞춤형 다중 행 워터마크로 PDF 프레젠테이션을 손쉽게 향상시키세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "188",
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
    "url": "/net/adding-multi-line-watermark-to-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-multi-line-watermark-to-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

{{% alert color="primary" %}}

많은 사용자들이 다중 행 텍스트로 PDF 문서에 스탬프를 찍고 싶어합니다. 그들은 보통 `\n` 및 `<br>`를 사용하려고 하지만 이러한 유형의 문자는 Aspose.Pdf.Facades 네임스페이스에서 지원되지 않습니다. 따라서 이를 가능하게 하기 위해 Aspose.Pdf.Facades 네임스페이스의 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 클래스에 [AddNewLineText()](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext/methods/addnewlinetext/index)라는 또 다른 메서드를 추가했습니다.

{{% /alert %}}

## 구현 세부사항

기존 PDF에 다중 행 워터마크를 추가하려면 다음 코드 청크를 참조하세요.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampToPdf()
{
    // Instantiate a stamp object
    var logoStamp = new Aspose.Pdf.Facades.Stamp();

    // Instantiate an object of FormattedText class
    var formatText = new Aspose.Pdf.Facades.FormattedText("Hello World!",
        System.Drawing.Color.FromArgb(180, 0, 0), 
        Aspose.Pdf.Facades.FontStyle.TimesItalic,
        Aspose.Pdf.Facades.EncodingType.Winansi, false, 50);

    // Add another line for Stamp
    formatText.AddNewLineText("Good Luck");
    // BindLogo to PDF
    logoStamp.BindLogo(formatText);
}
```