---
title: 주석 작업하기
linktitle: PDF의 주석
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 160
url: /ko/net/annotations/
description: Aspose.PDF를 사용하여 .NET에서 PDF 파일의 주석 작업 방법을 배우고, 주석, 강조 표시 및 기타 주석을 추가하는 방법을 포함합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Annotations",
    "alternativeHeadline": "Enhance PDFs with Comprehensive Annotation Capabilities",
    "abstract": "Aspose.PDF 라이브러리의 강력한 주석 기능으로 PDF 문서를 향상시키세요. 이 기능을 통해 사용자는 강조 표시, 메모 및 도형을 포함한 다양한 주석 유형을 쉽게 추가, 편집 및 삭제할 수 있으며, PDF 뷰어와의 완벽한 호환성을 유지합니다. 주석을 원활하게 관리하고 XFDF 및 FDF 형식으로 데이터를 가져오고 내보내는 방법을 알아보세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF Annotations, Aspose.PDF, annotations, XFDF format, FDF format, edit annotations, add annotations, delete annotations, PDF manipulation, interactive features",
    "wordcount": "294",
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
    "url": "/net/annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

PDF 페이지 내의 콘텐츠는 편집하기 어렵지만, PDF 사양은 페이지 콘텐츠를 변경하지 않고 PDF 페이지에 추가할 수 있는 완전한 객체 세트를 정의합니다.

이 객체들은 주석이라고 하며, 그 목적은 페이지 콘텐츠를 표시하는 것부터 양식과 같은 인터랙티브 기능을 구현하는 것까지 다양합니다.

PDF 뷰어는 일반적으로 텍스트 강조, 메모, 선 또는 도형과 같은 다양한 주석 유형의 생성 및 편집을 허용합니다. 생성할 수 있는 주석 유형에 관계없이 PDF 사양을 준수하는 PDF 뷰어는 모든 주석 유형의 렌더링을 지원해야 합니다.

주석은 PDF 파일의 중요한 부분입니다. Aspose.PDF for .NET을 사용하여 새 주석을 추가하고, 기존 주석을 편집하고, 주석을 삭제하는 등의 작업을 수행할 수 있습니다. 이 섹션에서는 다음 주제를 다룹니다:

다음 작업을 수행할 수 있습니다:

- [주석 개요](/pdf/net/overview-of-annotations/) - PDF 사양에 정의된 주석 유형과 Aspose.PDF가 지원하는 내용을 배웁니다.
- [주석 추가, 삭제 및 가져오기](/pdf/net/add-delete-and-get-annotation/) - 이 섹션에서는 허용된 모든 유형의 주석 작업 방법을 설명합니다.
- [XFDF 형식으로 주석 가져오기 및 내보내기](/pdf/net/import-export-xfdf/) - Aspose.PDF 라이브러리는 XFDF 파일로 주석 데이터를 가져오고 내보내는 방법을 제공합니다.
- [FDF 형식 주석을 PDF로 가져오기](/pdf/net/import-fdf/) - Aspose.PDF 라이브러리는 FDF 형식 주석을 PDF 파일로 가져오는 방법을 제공합니다.

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