---
title: Posting AcroForm Data
linktitle: Posting AcroForm
type: docs
weight: 50
url: /ko/net/posting-acroform-data/
description: Aspose.Pdf.Facades 네임스페이스를 이용하여 Aspose.PDF for .NET에서 XML 파일로 폼 데이터를 가져오고 내보낼 수 있습니다.
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
    "alternativeHeadline": "Import and Export form data to XML file",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, posting acroform data",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "dateModified": "2022-02-04",
    "description": "Aspose.Pdf.Facades 네임스페이스를 이용하여 Aspose.PDF for .NET에서 XML 파일로 폼 데이터를 가져오고 내보낼 수 있습니다."
}
</script>
{{% alert color="primary" %}}

AcroForm은 PDF 문서의 중요한 유형입니다. [Aspose.Pdf.Facades 네임스페이스](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace)를 사용하여 AcroForm을 생성하고 편집할 수 있을 뿐만 아니라, 양식 데이터를 XML 파일로 가져오고 내보낼 수도 있습니다. Aspose.PDF for .NET의 Aspose.Pdf.Facades 네임스페이스를 사용하면 외부 웹 페이지에 AcroForm 데이터를 게시하는 AcroForm의 다른 기능을 구현할 수 있습니다. 그런 다음 이 웹 페이지는 게시 변수를 읽고 이 데이터를 추가 처리에 사용합니다. 이 기능은 PDF 파일에 데이터를 유지하고 싶지 않고 서버로 보내 데이터베이스 등에 저장하고 싶은 경우 유용합니다.

{{% /alert %}}

## 구현 세부 사항

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 작동합니다.

이 글에서는 [Aspose.Pdf.Facades 네임스페이스](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace)를 사용하여 AcroForm을 생성하는 방법을 시도했습니다.
이 문서에서는 [Aspose.Pdf.Facades 네임스페이스](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace)를 사용하여 AcroForm을 생성하려고 시도하였습니다.

```csharp
// FormEditor 클래스의 인스턴스를 생성하고 입력 및 출력 pdf 파일을 바인딩합니다.
Aspose.Pdf.Facades.FormEditor editor = new Aspose.Pdf.Facades.FormEditor("input.pdf","output.pdf");

// AcroForm 필드를 생성합니다 - 간단히 두 개의 필드만 생성하였습니다.
editor.AddField(Aspose.PDF.Facades.FieldType.Text, "firstname", 1, 100, 600, 200, 625);
editor.AddField(Aspose.PDF.Facades.FieldType.Text, "lastname", 1, 100, 550, 200, 575);

// 제출 버튼을 추가하고 대상 URL을 설정합니다.
editor.AddSubmitBtn("submitbutton", 1, "Submit", "http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

// 출력 pdf 파일을 저장합니다.
editor.Save();
```

{{% alert color="primary" %}}

다음 코드 스니펫은 대상 웹 페이지에서 게시된 값을 받는 방법을 보여줍니다.
다음 코드 조각은 대상 웹 페이지에서 게시된 값을 받는 방법을 보여줍니다.
{{% /alert %}}

```csharp
// 대상 웹 페이지에서 게시된 값을 표시합니다.
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
    "applicationCategory": "PDF 조작 라이브러리 for .NET",
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


