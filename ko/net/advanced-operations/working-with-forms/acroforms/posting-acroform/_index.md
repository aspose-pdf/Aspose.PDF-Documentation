---
title: 아크로폼 데이터 게시
linktitle: AcroForm 게시
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ko/net/posting-acroform-data/
description: Aspose.Pdf.Facades 네임스페이스를 사용하여 양식 데이터를 XML 파일로 가져오고 내보낼 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Posting AcroForm Data",
    "alternativeHeadline": "Post AcroForm Data",
    "abstract": "Aspose.PDF for .NET에서 AcroForm 데이터를 게시할 수 있는 강력한 새로운 기능을 소개합니다. 이 기능은 개발자가 AcroForms를 생성하고 편집할 수 있을 뿐만 아니라 양식 데이터를 XML 파일로 원활하게 가져오고 내보낼 수 있도록 하여 애플리케이션 내에서 데이터 처리 및 저장 기능을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Posting AcroForm Data, Import and Export Form Data, Aspose.PDF for .NET, AcroForm Fields, Submit Button, External Web Page Integration, Form Data Posting, XML File Handling, FieldType.Text, Database Saving",
    "wordcount": "400",
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
    "url": "/net/posting-acroform-data/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/posting-acroform-data/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.Pdf.Facades 네임스페이스를 사용하여 양식 데이터를 XML 파일로 가져오고 내보낼 수 있습니다."
}
</script>

{{% alert color="primary" %}}

AcroForm은 PDF 문서의 중요한 유형입니다. [Aspose.Pdf.Facades 네임스페이스](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace)를 사용하여 AcroForm을 생성하고 편집할 수 있을 뿐만 아니라 양식 데이터를 XML 파일로 가져오고 내보낼 수 있습니다. Aspose.PDF for .NET의 Aspose.Pdf.Facades 네임스페이스는 AcroForm의 또 다른 기능을 구현할 수 있게 해주며, 이를 통해 AcroForm 데이터를 외부 웹 페이지에 게시할 수 있습니다. 이 웹 페이지는 게시된 변수를 읽고 이 데이터를 추가 처리에 사용합니다. 이 기능은 PDF 파일에 데이터를 단순히 보관하는 것이 아니라 서버로 전송하고 데이터베이스에 저장하는 등의 경우에 유용합니다.

{{% /alert %}}

## 구현 세부사항

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 작동합니다.

이 기사에서는 [Aspose.Pdf.Facades 네임스페이스](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace)를 사용하여 AcroForm을 생성하려고 했습니다. 또한 제출 버튼을 추가하고 그 대상 URL을 설정했습니다. 다음 코드 스니펫은 양식을 생성한 후 웹 페이지에서 게시된 데이터를 수신하는 방법을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateAcroFormWithFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create an instance of FormEditor class and bind input and output pdf files
    using (var editor = new Aspose.Pdf.Facades.FormEditor(dataDir + "input.pdf", dataDir + "output.pdf"))
    {
        // Create AcroForm fields - I have created only two fields for simplicity
        editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "firstname", 1, 100, 600, 200, 625);
        editor.AddField(Aspose.Pdf.Facades.FieldType.Text, "lastname", 1, 100, 550, 200, 575);

        // Add a submit button and set target URL
        editor.AddSubmitBtn("submitbutton", 1, "Submit", "http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

        // Save PDF document
        editor.Save();
    }
}
```

{{% alert color="primary" %}}

다음 코드 스니펫은 대상 웹 페이지에서 게시된 값을 수신하는 방법을 보여줍니다. 이 예제에서는 Show.a spx라는 페이지를 사용했으며, 페이지 로드 메서드에 간단한 한 줄 코드를 추가했습니다.

{{% /alert %}}

```csharp
// Show the posted values on the target web page
Response.Write("Hello " + Request.Form.Get("firstname") + " " + Request.Form.Get("lastname"));
```

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