---
title: AcroForms 작업하기
linktitle: 아크로폼
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/acroforms/
description: Aspose.PDF for .NET을 사용하여 처음부터 양식을 만들고, PDF 문서의 양식 필드를 채우고, 양식에서 데이터를 추출하는 등의 작업을 수행할 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with AcroForms",
    "alternativeHeadline": "Enhance PDF forms with flexible AcroForms functionality",
    "abstract": "Aspose.PDF for .NET은 AcroForms 작업을 위한 향상된 기능을 도입하여 사용자가 처음부터 양식을 효율적으로 만들고, PDF 필드를 채우고, 데이터를 원활하게 추출할 수 있도록 합니다. 이 강력한 기능은 여러 데이터베이스 레코드를 통합할 수 있도록 지원하여 동적 양식 관리와 간소화된 사용자 경험을 제공합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "AcroForms, PDF forms technology, create a form, fill form fields, extract data, database records, Templates, modify AcroForms, posting AcroForm data, import and export data",
    "wordcount": "484",
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
    "url": "/net/acroforms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/acroforms/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## AcroForms의 기본

**AcroForms**는 원래 PDF 양식 기술입니다. AcroForms는 페이지 지향 양식입니다. 1998년에 처음 도입되었습니다. 이들은 Forms Data Format 또는 FDF 및 XML Forms Data Format 또는 xFDF 형식의 입력을 수용합니다. 제3자 공급업체가 AcroForms를 지원합니다. Adobe가 AcroForms를 도입했을 때, 그들은 이를 "Adobe Acrobat Pro/Standard로 작성된 PDF 양식이며 특별한 정적 또는 동적 XFA 양식이 아니다"라고 언급했습니다. AcroForms는 휴대 가능하며 모든 플랫폼에서 작동합니다.

AcroForms를 사용하여 PDF 양식 문서에 추가 페이지를 추가할 수 있습니다. 템플릿 개념 덕분에 AcroForms를 사용하여 여러 데이터베이스 레코드로 양식을 채울 수 있습니다.

PDF 1.7은 데이터와 PDF 양식을 통합하는 두 가지 방법을 지원합니다.

*AcroForms(아크로뱃 양식으로도 알려짐)*은 PDF 1.2 형식 사양에 도입되어 포함되었습니다.

*Adobe XML Forms Architecture(XFA) 양식*은 PDF 1.5 형식 사양에 선택적 기능으로 도입되었습니다( XFA 사양은 PDF 사양에 포함되지 않으며, 단지 참조만 됩니다).

**Acroforms**와 **XFA** 양식을 이해하기 위해서는 먼저 기본을 이해해야 합니다. 우선, 두 가지 모두 사용할 수 있는 PDF 양식입니다. Acroforms는 1998년에 만들어진 오래된 양식으로 여전히 클래식 PDF 양식으로 언급됩니다. XFA 양식은 PDF로 저장할 수 있는 웹페이지이며, 2003년에 등장했습니다. PDF가 XFA 양식을 수용하기 시작하기까지는 시간이 걸렸습니다.

AcroForms는 XFA에서 찾을 수 없는 기능을 가지고 있으며, 반대로 XFA는 AcroForms에서 찾을 수 없는 일부 기능을 가지고 있습니다. 예를 들어:

- AcroForms는 "템플릿" 개념을 지원하여 PDF 양식 문서에 추가 페이지를 추가하여 여러 데이터베이스 레코드로 양식을 채울 수 있도록 합니다.
- XFA는 데이터 수용을 위해 필요에 따라 필드 크기를 조정할 수 있는 문서 재흐름 개념을 지원합니다.

Java 라이브러리의 기능에 대한 더 자세한 학습은 다음 기사를 참조하십시오:

- [AcroForm 만들기](/pdf/net/create-form) - C#로 처음부터 양식 만들기.
- [AcroForm 채우기](/pdf/net/fill-form) - PDF 문서의 양식 필드 채우기.
- [AcroForm 추출하기](/pdf/net/extract-form) - PDF 문서의 모든 필드 또는 개별 필드에서 값 가져오기.
- [AcroForm 수정하기](/pdf/net/modifing-form) - FieldLimit 가져오기 또는 설정, 양식 필드 글꼴 설정 등.
- [AcroForm 데이터 게시하기](/pdf/net/posting-acroform-data/) - 양식 데이터를 XML 파일로 가져오고 내보내기.
- [데이터 가져오기 및 내보내기](/pdf/net/import-and-export-data/) - Form Class를 사용하여 데이터 가져오기 및 내보내기.
- [PDF에서 양식 제거하기](/pdf/net/remove-form/) - 하위 유형/형식에 따라 텍스트 제거, 모든 양식 삭제.
- [JSON으로 데이터 가져오기 및 내보내기](/pdf/net/import-export-json/) - JSON으로 데이터 가져오기 및 내보내기.

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