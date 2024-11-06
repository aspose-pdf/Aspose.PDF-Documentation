---
title: JavaScript를 다루는 방법
type: docs
url: ko/net/working-with-javascript/
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "JavaScript를 다루는 방법",
    "alternativeHeadline": "PDF에서 JavaScript를 다루는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, pdf 내의 javascript",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
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
    "url": "/net/working-with-javascript/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-javascript/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>

## 자바스크립트 추가하기 (DOM)

### Acrobat 자바스크립트란 무엇인가요?

Acrobat 자바스크립트는 ISO-16262의 자바스크립트 버전 1.5의 핵심을 기반으로 한 언어로, 이전에는 ECMAScript로 알려져 있으며 Netscape Communications에서 개발한 객체 지향 스크립팅 언어입니다. 자바스크립트는 웹 기반 응용 프로그램에서 서버에서 클라이언트로 웹 페이지 처리를 옮기기 위해 만들어졌습니다. Acrobat 자바스크립트는 자바스크립트 언어에 새로운 객체와 그에 따른 메소드 및 속성의 형태로 확장을 구현합니다. 이 Acrobat 특화 객체들은 개발자가 문서 보안을 관리하고, 데이터베이스와 통신하며, 파일 첨부를 다루고, PDF 파일을 상호 작용적이고 웹 활성화된 양식처럼 동작하게 조작할 수 있게 해줍니다. Acrobat 특화 객체들은 핵심 자바스크립트 위에 추가되므로, 여전히 표준 클래스인 Math, String, Date, Array, RegExp에 접근할 수 있습니다.

### Acrobat 자바스크립트와 HTML (웹) 자바스크립트의 비교

PDF 문서는 Acrobat 소프트웨어 내부와 웹 브라우저에서 모두 표시될 수 있어 매우 다양하게 사용됩니다.
PDF 문서는 Acrobat 소프트웨어뿐만 아니라 웹 브라우저 내에서도 표시될 수 있어 매우 다양하게 사용됩니다.

- Acrobat 자바스크립트는 HTML 페이지 내의 객체에 접근할 수 없습니다. 마찬가지로, HTML 자바스크립트는 PDF 파일 내의 객체에 접근할 수 없습니다.
- HTML 자바스크립트는 Window와 같은 객체를 조작할 수 있습니다. Acrobat 자바스크립트는 이 특정 객체에 접근할 수 없지만 PDF 특정 객체를 조작할 수 있습니다.

[Aspose.PDF for .NET](/pdf/net/)을 사용하여 문서와 페이지 수준에서 자바스크립트를 추가할 수 있습니다. 자바스크립트를 추가하는 방법:

### 문서 또는 페이지 액션에 자바스크립트 추가

1. 원하는 자바스크립트 구문을 생성자 인수로 사용하여 JavascriptAction 객체를 선언하고 인스턴스화합니다.
1. JavascriptAction 객체를 PDF 문서 또는 페이지의 원하는 액션에 할당합니다.

아래 예제는 특정 문서에 OpenAction을 적용합니다.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Working-Document-AddJavaScriptToPage-AddJavaScriptToPage.cs" >}}

### **문서 수준에 자바스크립트 추가/제거**
### **문서 레벨에 자바스크립트 추가/제거하기**

문서 클래스에 JavaScript라는 새 속성이 추가되었습니다. 이 속성은 JavaScript 컬렉션 유형을 가지고 있으며 키로 JavaScript 시나리오에 접근할 수 있습니다. 이 속성은 문서 레벨 JavaScript를 추가하는 데 사용됩니다. JavaScript 컬렉션에는 다음과 같은 속성과 메서드가 있습니다:

- string this(string key) – 이름으로 JavaScript를 가져오거나 설정합니다.
- IList Keys – JavaScript 컬렉션에 있는 기존 키 목록을 제공합니다.
- bool Remove(string key) – 키로 JavaScript를 제거합니다.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Working-Document-AddRemoveJavascriptToDoc-AddRemoveJavascriptToDoc.cs" >}}

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


