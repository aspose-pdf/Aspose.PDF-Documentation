---
title: WebForms DataGridView를 PDF로 렌더링하기
linktitle: WebForms DataGridView를 PDF로 렌더링하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/render-webforms-datagridview-to-pdf/
description: 이 샘플은 Aspose.PDF 라이브러리를 사용하여 WebForm을 PDF로 렌더링하는 방법을 보여줍니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Render WebForms DataGridView to PDF",
    "alternativeHeadline": "Effortlessly Convert WebForms DataGridView to PDF",
    "abstract": "이 기능은 Aspose.PDF for .NET 라이브러리를 사용하여 WebForms DataGridView를 PDF로 원활하게 변환할 수 있게 해줍니다. 이 기능은 전용 GridView 내보내기 컨트롤을 통합하여 데이터 내보내기 프로세스를 단순화하고, 웹 애플리케이션에서 직접 고품질 PDF 렌더링을 보장합니다. 효율적인 문서 생성 솔루션을 찾는 개발자에게 완벽합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "266",
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
    "url": "/net/render-webforms-datagridview-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/render-webforms-datagridview-to-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

## Aspose.PDF/Aspose.HTML를 사용하여 WebForm을 PDF로 내보내는 방법

### 소개

일반적으로 WebForm을 PDF 문서로 변환하려면 추가 도구가 필요합니다. 이 샘플은 Aspose.PDF 라이브러리를 사용하여 WebForm을 PDF로 렌더링하는 방법을 보여줍니다. Aspose Export GridView To Pdf Control도 이 샘플에 포함되어 있어 _GridView 컨트롤을 PDF 문서로 렌더링하는 방법을 보여줍니다._

## WebForm을 PDF로 렌더링하는 방법

WebForm을 PDF로 렌더링하기 위한 원래 아이디어는 [System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx)에서 상속받은 도우미 클래스를 만들고 Render 메서드를 재정의하는 것입니다.</em></p>

```csharp
void Render(HtmlTextWriter writer)
{
    if (RenderToPDF)
    {
        // render web page for PDF document
    }
    else
    {
        // render web page in browser
        base.Render(writer);
    }
}
```

HTML을 PDF로 렌더링하는 데 사용할 수 있는 두 가지 Aspose 도구가 있습니다:

- Aspose.PDF for .NET.
- Aspose Export GridView 컨트롤 (Aspose.PDF 기반).

## 소스 파일

이 샘플에는 2개의 데모 보고서가 있습니다.

- _Default.aspx_는 Aspose.PDF를 사용하여 PDF로 내보내는 방법을 보여줍니다.
- _Report2.aspx_는 Aspose Export GridView 컨트롤 (Aspose.PDF 기반)을 사용하여 PDF로 내보내는 방법을 보여줍니다.

## 추가 파일

`Helpers\PdfPage.cs` - Aspose.PDF API를 사용하는 방법을 보여주는 도우미 클래스가 포함되어 있습니다.</em>

Aspose.Pdf.GridViewExport 프로젝트는 `Report2.aspx`에서 시연을 위한 확장된 GridView 컨트롤을 포함합니다.