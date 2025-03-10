---
title: OneClick PDF 문서 생성기 사용하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/using-oneclick-pdf-document-generator/
description: Microsoft Dynamics에서 Aspose.PDF OneClick PDF 문서 생성기를 사용하는 방법을 배우세요.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using OneClick PDF Document Generator",
    "alternativeHeadline": "Streamlined PDF Generation in Microsoft Dynamics",
    "abstract": "Aspose.PDF OneClick PDF 문서 생성기를 사용하여 Microsoft Dynamics에서 원활한 문서 생성을 잠금 해제하세요. 이 혁신적인 기능을 통해 사용자는 CRM 내에서 직접 사용자 정의 가능한 PDF 템플릿을 만들고, 단일 클릭으로 문서를 효율적으로 생성하며, 양식에 OneClick 버튼을 쉽게 통합하여 간소화된 접근을 제공합니다. 이 강력한 도구로 데이터 관리 능력을 향상시키고 생산성을 개선하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "313",
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
    "url": "/net/using-oneclick-pdf-document-generator/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/using-oneclick-pdf-document-generator/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 단순하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## 템플릿 만들기 및 CRM에 추가하기

- 워드를 열고 템플릿을 만듭니다.
- CRM에서 오는 데이터에 대한 MailMerge 필드를 삽입합니다.

![MailMerge 필드 삽입](using-oneclick-pdf-document-generator_1.png)

- 필드 이름이 CRM 필드와 정확히 일치하는지 확인합니다.
- 템플릿은 개별 엔티티와 함께 사용하기 위해 특정합니다.

![데모 템플릿](using-oneclick-pdf-document-generator_2.png)

- 템플릿이 생성되면 CRM에서 OneClick PDF 구성 엔티티를 열고 새 레코드를 만듭니다.
- 템플릿의 이름을 지정하고, 템플릿이 정의된 엔티티를 선택하고, 생성된 문서를 첨부합니다.

![템플릿 선택](using-oneclick-pdf-document-generator_3.png)

## 리본 버튼에서 문서 생성하기

- 문서를 생성할 레코드를 엽니다. (해당 엔티티에 대한 구성에 템플릿이 이미 첨부되어 있는지 확인하세요)
- 리본에서 OneClick PDF 버튼을 클릭합니다.

![OneClick PDF 클릭](using-oneclick-pdf-document-generator_4.png)

- 팝업에서: 템플릿, 파일 이름 및 작업을 선택하고 생성 버튼을 클릭합니다.
- 선택에 따라 다운로드된 파일 또는 노트를 확인합니다.

## OneClick 버튼 구성 및 사용하기

- 양식에서 OneClick 버튼을 직접 사용하려면 양식 사용자 지정을 엽니다.
- OneClick 버튼을 추가할 위치에 WebResource를 삽입합니다.
- Webresource에서 OpenButtonPage를 선택하고 이름을 지정합니다.
- 다음 샘플에서 데이터 필드에 버튼을 구성합니다.

![WebResource 속성](using-oneclick-pdf-document-generator_5.png)

- 각 버튼에 대해 별도의 줄을 사용하고 다음 구문을 사용합니다:
  - 구문: 템플릿 이름 |<작업: 다운로드/노트>|출력 파일 이름
  - 예: 데모|다운로드|내 다운로드된 파일
- 사용자 지정을 저장하고 게시합니다.
- 버튼이 양식에 표시됩니다.

![양식에 버튼이 표시됩니다](using-oneclick-pdf-document-generator_6.png)