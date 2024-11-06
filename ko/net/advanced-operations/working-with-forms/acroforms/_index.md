---
title: AcroForms 작업하기
linktitle: AcroForms
type: docs
weight: 10
url: ko/net/acroforms/
description: Aspose.PDF for .NET을 사용하면 처음부터 양식을 생성하고, PDF 문서의 양식 필드를 채우고, 양식에서 데이터를 추출하는 등의 작업을 수행할 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "AcroForms 작업하기",
    "alternativeHeadline": "PDF에서 AcroForms 사용 옵션",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, pdf에서 acroforms",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 문서 팀",
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
    "url": "/net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/acroforms/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET을 사용하면 처음부터 양식을 생성하고, PDF 문서의 양식 필드를 채우고, 양식에서 데이터를 추출하는 등의 작업을 수행할 수 있습니다."
}
</script>
## AcroForms의 기본 사항

**AcroForms**는 원래의 PDF 양식 기술입니다. AcroForms는 페이지 지향 양식입니다. 1998년에 처음 도입되었습니다. Forms Data Format 또는 FDF 및 XML Forms Data Format 또는 xFDF에서 입력을 받습니다. 타사 공급업체가 AcroForms를 지원합니다. Adobe가 AcroForms를 도입했을 때, 그들은 이를 “Adobe Acrobat Pro/Standard로 작성된 PDF 양식이며, 특별한 유형의 정적 또는 동적 XFA 양식이 아닙니다.”라고 언급했습니다. Acroforms는 휴대가 가능하며 모든 플랫폼에서 작동합니다.

AcroForms를 사용하여 PDF 양식 문서에 추가 페이지를 추가할 수 있습니다. 템플릿 개념 덕분에 여러 데이터베이스 레코드로 양식을 채우는 것을 지원하기 위해 AcroForms를 사용할 수 있습니다.

PDF 1.7은 데이터와 PDF 양식을 통합하기 위한 두 가지 다른 방법을 지원합니다.

*AcroForms(또한 Acrobat 양식으로 알려짐)*, PDF 1.2 형식 사양에 도입되고 포함되었습니다.

*Adobe XML Forms Architecture (XFA) 양식*, PDF 1.5 형식 사양에서 선택적 기능으로 도입되었습니다 (XFA 사양은 PDF 사양에 포함되지 않으며, 참조만 됩니다).
*Adobe XML Forms Architecture (XFA) 양식*은 PDF 1.5 형식 사양에서 선택적 기능으로 도입되었습니다 (XFA 사양은 PDF 사양에 포함되어 있지 않으며, 참조만 합니다).

**Acroforms**와 **XFA** 양식을 이해하기 위해서는 기본부터 이해해야 합니다. 우선 두 가지 모두 사용할 수 있는 PDF 양식입니다. Acroforms는 1998년에 만들어진 오래된 것으로, 여전히 클래식 PDF 양식으로 언급됩니다. XFA 양식은 2003년에 등장한 웹페이지를 PDF로 저장할 수 있는 양식입니다. PDF가 XFA 양식을 수용하기 시작하기 전까지는 다소 시간이 걸렸습니다.

AcroForms는 XFA에 없는 기능을 가지고 있으며, 반대로 XFA는 AcroForms에 없는 몇 가지 기능을 가지고 있습니다. 예를 들면:

- AcroForms는 "템플릿"의 개념을 지원하여, 여러 데이터베이스 레코드로 양식을 채우기 위해 PDF 양식 문서에 추가 페이지를 추가할 수 있습니다.
- XFA는 문서 재배치 개념을 지원하여 데이터를 수용하기 위해 필요한 경우 필드 크기를 조정할 수 있습니다.

Java 라이브러리의 기능에 대해 자세히 알아보려면 다음 기사를 참조하세요:
Java 라이브러리의 기능을 자세히 학습하려면 다음 기사를 참조하십시오:

- [Create AcroForm](/pdf/net/create-form) - C#을 사용하여 처음부터 양식을 만듭니다.
- [Fill AcroForm](/pdf/net/fill-form) - PDF 문서의 양식 필드를 채웁니다.
- [Extract AcroForm](/pdf/net/extract-form) - PDF 문서의 모든 또는 개별 필드에서 값을 가져옵니다.
- [Modifing AcroForm](/pdf/net/modifing-form) - FieldLimit를 가져오거나 설정하고, 양식 필드 글꼴을 설정하는 등의 작업을 합니다.
- [Posting AcroForm Data](/pdf/net/posting-acroform-data/) - 양식 데이터를 XML 파일로 가져오고 내보냅니다.
- [Import and Export Data](/pdf/net/import-and-export-data/) - Form Class를 사용하여 데이터를 가져오고 내보냅니다.

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

