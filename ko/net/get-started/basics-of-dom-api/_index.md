---
title: Aspose.PDF DOM API의 기초
linktitle: DOM API의 기초
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 130
url: /ko/net/basics-of-dom-api/
description: Aspose.PDF for .NET은 객체 측면에서 PDF 문서의 구조를 나타내기 위해 DOM의 아이디어를 사용합니다.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Basics of Aspose.PDF DOM API",
    "alternativeHeadline": "Enhanced PDF Manipulation with Aspose.PDF DOM API in C#",
    "abstract": "새로운 Aspose.PDF for .NET DOM API는 PDF 문서의 구조를 계층적 트리로 표현하여 조작할 수 있는 강력한 객체 지향 접근 방식을 제공합니다. 이 기능은 개발자가 직관적인 프로그래밍 인터페이스를 통해 문서 조작에 대한 유연성과 제어를 향상시키면서 PDF 요소에 쉽게 접근하고 업데이트하며 내보낼 수 있도록 합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "891",
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
    "url": "/net/basics-of-dom-api/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/basics-of-dom-api/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## DOM API 소개

문서 객체 모델(DOM)은 구조화된 문서를 객체 지향 모델로 표현하는 형태입니다. DOM은 플랫폼 및 언어 중립적인 방식으로 구조화된 문서를 표현하기 위한 공식 월드 와이드 웹 컨소시엄(W3C) 표준입니다.

간단히 말해, DOM은 문서의 구조를 나타내는 객체의 트리입니다. Aspose.PDF for .NET은 객체 측면에서 PDF 문서의 구조를 나타내기 위해 DOM의 아이디어를 사용합니다. 그러나 DOM의 요소와 같은 측면은 사용 중인 프로그래밍 언어의 구문 내에서 조작됩니다. DOM의 공용 인터페이스는 애플리케이션 프로그래밍 인터페이스(API)에서 지정됩니다.

### PDF 문서 소개

휴대용 문서 형식(PDF)은 문서 교환을 위한 개방형 표준입니다. PDF 문서는 텍스트와 이진 데이터의 조합입니다. 텍스트 편집기에서 열면 문서의 구조와 내용을 정의하는 원시 객체를 볼 수 있습니다.

PDF 파일의 논리적 구조는 계층적이며, 뷰어 애플리케이션이 문서의 페이지와 내용을 그리는 순서를 결정합니다. PDF는 객체, 파일 구조, 문서 구조 및 콘텐츠 스트림의 네 가지 구성 요소로 구성됩니다.

### PDF 문서 구조

PDF 파일의 구조가 계층적이므로 Aspose.PDF for .NET도 동일한 방식으로 요소에 접근합니다. 다음 계층 구조는 PDF 문서가 논리적으로 어떻게 구성되어 있는지와 Aspose.PDF for .NET DOM API가 이를 어떻게 구성하는지를 보여줍니다.

![PDF 문서 구조](../images/structure.png)

### PDF 문서 요소 접근

Document 객체는 객체 모델의 루트 수준에 있습니다. Aspose.PDF for .NET DOM API를 사용하면 Document 객체를 생성한 다음 계층 내의 모든 다른 객체에 접근할 수 있습니다. Pages와 같은 컬렉션이나 Page와 같은 개별 요소에 접근할 수 있습니다. DOM API는 PDF 문서를 조작하기 위한 단일 진입 및 종료 지점을 제공합니다:

- PDF 문서 열기.
- DOM 스타일로 PDF 문서 구조 접근.
- PDF 문서의 데이터 업데이트.
- PDF 문서 유효성 검사.
- PDF 문서를 다양한 형식으로 내보내기.
- 마지막으로 업데이트된 PDF 문서 저장.

## 새로운 Aspose.PDF for .NET API 사용 방법

이 주제에서는 새로운 Aspose.PDF for .NET API를 설명하고 빠르고 쉽게 시작할 수 있도록 안내합니다. 특정 기능 사용에 대한 세부 사항은 이 기사에 포함되지 않음을 유의하십시오.

Aspose.PDF for .NET은 두 부분으로 구성됩니다:

- Aspose.PDF for .NET DOM API.
- Aspose.Pdf.Facades (구 Aspose.PDF.Kit for .NET).

각 영역에 대한 세부 사항은 아래에서 확인할 수 있습니다.

### Aspose.PDF for .NET DOM API

Aspose.PDF for .NET DOM API는 PDF 문서 구조에 해당하며, 파일 및 문서 수준뿐만 아니라 객체 수준에서도 PDF 문서 작업을 도와줍니다. 우리는 개발자가 PDF 문서의 모든 요소와 객체에 접근할 수 있는 더 많은 유연성을 제공했습니다. Aspose.PDF DOM API의 클래스를 사용하면 문서 요소 및 형식에 프로그래밍적으로 접근할 수 있습니다. 이 새로운 DOM API는 아래와 같은 다양한 네임스페이스로 구성됩니다:

### Aspose.PDF

이 네임스페이스는 PDF 문서를 열고 저장할 수 있는 Document 클래스를 제공합니다. License 클래스도 이 네임스페이스의 일부입니다. 또한 Page, PageCollection, FileSpecification, EmbeddedFileCollection, OutlineItemCollection 및 OutlineCollection과 같은 PDF 페이지, 첨부 파일 및 북마크와 관련된 클래스를 제공합니다.

#### Aspose.Text

이 네임스페이스는 텍스트 및 그 다양한 측면을 작업하는 데 도움이 되는 클래스를 제공합니다. 예를 들어 Font, FontCollection, FontRepository, FontStyles, TextAbsorber, TextFragment, TextFragmentAbsorber, TextFragmentCollection, TextFragmentState, TextSegment 및 TextSegmentCollection 등이 있습니다.

#### Aspose.Text.TextOptions

이 네임스페이스는 텍스트 검색, 편집 또는 교체를 위한 다양한 옵션을 설정할 수 있는 클래스를 제공합니다. 예를 들어 TextEditOptions, TextReplaceOptions 및 TextSearchOptions 등이 있습니다.

#### Aspose.InteractiveFeatures

이 네임스페이스는 PDF 문서의 인터랙티브 기능을 작업하는 데 도움이 되는 클래스를 포함합니다. 예를 들어 문서 작업 및 기타 작업과 관련된 클래스가 포함되어 있습니다. 이 네임스페이스에는 GoToAction, GoToRemoteAction 및 GoToURIAction과 같은 클래스가 포함되어 있습니다.

#### Aspose.InteractiveFeatures.Annotations

주석은 PDF 문서의 인터랙티브 기능의 일부입니다. 우리는 주석을 위한 네임스페이스를 전용했습니다. 이 네임스페이스에는 Annotation, AnnotationCollection, CircleAnnotation 및 LinkAnnotation과 같은 주석 작업에 도움이 되는 클래스가 포함되어 있습니다.

#### Aspose.InteractiveFeatures.Forms

이 네임스페이스는 PDF 양식 및 양식 필드를 작업하는 데 도움이 되는 클래스를 포함합니다. 예를 들어 Form, Field, TextBoxField 및 OptionCollection 등이 있습니다.

#### Aspose.Pdf.Devices

PDF 문서에 대해 다양한 작업을 수행할 수 있습니다. 예를 들어 PDF 문서를 다양한 이미지 형식으로 변환하는 작업이 있습니다. 그러나 이러한 작업은 Document 객체에 속하지 않으며, 이러한 작업을 위해 Document 클래스를 확장할 수 없습니다. 그래서 우리는 새로운 DOM API에서 Device 개념을 도입했습니다.

#### Aspose.Pdf.Facades

Aspose.PDF for .NET 이전에는 기존 PDF 파일을 조작하기 위해 Aspose.PDF.Kit for .NET이 필요했습니다. 이전 Aspose.PDF.Kit 코드를 실행하려면 Aspose.PDF.Facades 네임스페이스를 사용할 수 있습니다.