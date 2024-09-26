---
title: 페이지 속성 가져오기 및 설정하기
type: docs
url: /net/get-and-set-page-properties/
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "페이지 속성 가져오기 및 설정하기",
    "alternativeHeadline": "PDF 페이지 속성 가져오기 및 설정하기",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, 페이지 속성 가져오기, 페이지 속성 설정하기",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 문서팀",
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
    "url": "/net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-and-set-page-properties/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
Aspose.PDF for .NET을 사용하면 .NET 애플리케이션에서 PDF 파일의 페이지 속성을 읽고 설정할 수 있습니다. 이 섹션에서는 PDF 파일의 페이지 수를 가져오고, PDF 페이지 속성(예: 색상)에 대한 정보를 가져오고 페이지 속성을 설정하는 방법을 보여줍니다. 제공된 예제는 C#으로 되어 있지만 VB.NET과 같은 다른 .NET 언어를 사용하여 동일한 작업을 수행할 수 있습니다.

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와도 함께 작동합니다.

## PDF 파일의 페이지 수 가져오기

문서를 다룰 때 종종 그 문서가 몇 페이지로 구성되어 있는지 알고 싶어합니다. Aspose.PDF를 사용하면 두 줄의 코드로 이 정보를 얻을 수 있습니다.

PDF 파일의 페이지 수를 얻으려면:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스를 사용하여 PDF 파일을 엽니다.
1. 그런 다음 Document 객체에서 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 컬렉션의 Count 속성을 사용하여 문서의 총 페이지 수를 가져옵니다.

다음 코드 조각은 PDF 파일의 페이지 수를 얻는 방법을 보여줍니다.
다음 코드 조각은 PDF 파일의 페이지 수를 얻는 방법을 보여줍니다.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetNumberofPages-GetNumberofPages.cs" >}}

### 문서를 저장하지 않고 페이지 수 가져오기

때로는 PDF 파일을 실시간으로 생성하고 PDF 파일 생성 중에 (목차 생성 등) 시스템이나 스트림에 파일을 저장하지 않고 PDF 파일의 페이지 수를 얻어야 할 필요성이 생길 수 있습니다. 이러한 요구 사항을 충족하기 위해 Document 클래스에 [ProcessParagraphs](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/processparagraphs) 메서드가 도입되었습니다. 문서를 저장하지 않고 페이지 수를 얻는 단계를 보여주는 다음 코드 조각을 살펴보십시오.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetPageCount-GetPageCount.cs" >}}

## 페이지 속성 가져오기

PDF 파일의 각 페이지에는 너비, 높이, 블리드, 크롭 및 트림박스와 같은 여러 속성이 있습니다.
### **페이지 속성 이해하기: Artbox, BleedBox, CropBox, MediaBox, TrimBox 및 Rect 속성의 차이점**

- **미디어 박스**: 미디어 박스는 가장 큰 페이지 박스입니다. 이는 문서가 PostScript 또는 PDF로 인쇄될 때 선택된 페이지 크기(예: A4, A5, US Letter 등)에 해당합니다. 즉, 미디어 박스는 PDF 문서가 표시되거나 인쇄되는 미디어의 물리적 크기를 결정합니다.
- **블리드 박스**: 문서에 블리드가 있으면 PDF에도 블리드 박스가 있습니다. 블리드는 페이지 가장자리를 넘어 확장되는 색상(또는 아트워크)의 양입니다. 이는 문서가 인쇄되어 크기에 맞게 자를 때("트리밍") 잉크가 페이지 가장자리까지 도달하도록 하기 위해 사용됩니다. 페이지가 트림 표시에서 약간 벗어나 잘릴 경우에도 페이지에 흰색 가장자리가 나타나지 않습니다.
- **트림 박스**: 트림 박스는 인쇄 및 트리밍 후 문서의 최종 크기를 나타냅니다.
- **Trim box**: 트림 박스는 인쇄 및 자르기 후 문서의 최종 크기를 나타냅니다.
- **Art box**: 아트 박스는 문서의 페이지에 있는 실제 내용 주변에 그려진 박스입니다. 이 페이지 박스는 다른 애플리케이션에서 PDF 문서를 가져올 때 사용됩니다.
- **Crop box**: 크롭 박스는 Adobe Acrobat에서 PDF 문서가 표시되는 "페이지" 크기입니다. 일반 보기에서 Adobe Acrobat에서는 크롭 박스의 내용만 표시됩니다.
  이러한 속성의 자세한 설명은 Adobe.Pdf 사양, 특히 10.10.1 페이지 경계를 참조하십시오.
- **Page.Rect**: MediaBox와 DropBox의 교차점(일반적으로 보이는 직사각형)입니다. 아래 그림은 이러한 속성을 보여줍니다.

자세한 내용은 [이 페이지](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)를 방문하십시오.

### **페이지 속성 접근**

[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 클래스는 특정 PDF 페이지와 관련된 모든 속성을 제공합니다.
[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 클래스는 특정 PDF 페이지와 관련된 모든 속성을 제공합니다.

여기서 개별 Page 객체에 인덱스를 사용하여 접근하거나, foreach 루프를 사용하여 컬렉션을 순회하며 모든 페이지를 가져올 수 있습니다. 개별 페이지에 접근하면 그 속성을 가져올 수 있습니다. 다음 코드 스니펫은 페이지 속성을 가져오는 방법을 보여줍니다.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetProperties-GetProperties.cs" >}}

## PDF 파일의 특정 페이지 가져오기

Aspose.PDF는 PDF를 개별 페이지로 [분할](/pdf/net/split-pdf-document/)하고 PDF 파일로 저장할 수 있습니다. PDF 파일에서 지정된 페이지를 가져와 새 PDF로 저장하는 것은 매우 유사한 작업입니다: 원본 문서를 열고, 페이지에 접근하고, 새 문서를 생성하고 페이지를 추가합니다.

[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)은 PDF 파일의 페이지를 보유합니다.
[문서](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection)은 PDF 파일의 페이지를 보유합니다.

1. Pages 속성을 사용하여 페이지 인덱스를 지정하세요.
1. 새 [문서](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 생성하세요.
1. 새 [문서](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체에 [페이지](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체를 추가하세요.
1. [저장](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 출력을 저장하세요.

다음 코드 스니펫은 PDF 파일에서 특정 페이지를 가져와 새 파일로 저장하는 방법을 보여줍니다.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-GetParticularPage-GetParticularPage.cs" >}}

## 페이지 색상 결정

[페이지](https://reference.aspose.com/pdf/net/aspose.pdf/page) 클래스는 PDF 문서의 특정 페이지와 관련된 속성을 제공합니다. 여기에는 페이지가 사용하는 색상 유형 - RGB, 흑백, 회색조 또는 정의되지 않음 - 이 포함됩니다.
[Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 클래스는 PDF 문서의 특정 페이지에 관련된 속성을 제공하며, 페이지가 사용하는 색상 유형 - RGB, 흑백, 회색조 또는 정의되지 않음 -을 포함합니다.

PDF 파일의 모든 페이지는 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 컬렉션에 포함되어 있습니다. ColorType 속성은 페이지의 요소 색상을 지정합니다. 특정 PDF 페이지의 색상 정보를 얻거나 결정하려면 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체의 [ColorType](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/colortype) 속성을 사용하세요.

다음 코드 스니펫은 PDF 파일의 개별 페이지를 순회하며 색상 정보를 얻는 방법을 보여줍니다.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Pages-DeterminePageColor-DeterminePageColor.cs" >}}

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

