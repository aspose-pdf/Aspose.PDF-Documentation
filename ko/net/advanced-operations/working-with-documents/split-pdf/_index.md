---
title: PDF를 프로그래밍적으로 분할하기
linktitle: PDF 파일 분할하기
type: docs
weight: 60
url: ko/net/split-pdf-document/
keywords: 여러 파일로 PDF 분할하기, 별도의 PDF로 PDF 분할하기, split pdf c#
description: 이 주제는 C#을 사용하여 .NET 애플리케이션에서 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/split-document/
    - /net/split-pdf-pages/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF를 프로그래밍적으로 분할하기",
    "alternativeHeadline": ".NET으로 PDF 분할 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, split pdf",
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
    "url": "/net/split-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "이 주제는 C#을 사용하여 .NET 애플리케이션에서 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다."
}
</script>
## 실시간 예제

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter)는 프레젠테이션 분할 기능이 어떻게 작동하는지 조사할 수 있는 온라인 무료 웹 애플리케이션입니다.

[![Aspose PDF 분할](splitter.png)](https://products.aspose.app/pdf/splitter)

이 주제는 .NET 애플리케이션에서 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다. C#을 사용하여 PDF 페이지를 단일 페이지 PDF 파일로 분할하기 위해 다음 단계를 따를 수 있습니다:

1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 컬렉션을 통해 PDF 문서의 페이지를 반복합니다.
1. 반복할 때마다 새 Document 객체를 생성하고 개별 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 객체를 빈 문서에 추가합니다.
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 새 PDF를 저장합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.
다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리에서도 작동합니다.

## C#에서 PDF를 여러 파일 또는 개별 PDF로 분할하기

다음 C# 코드 조각은 PDF 페이지를 개별 PDF 파일로 분할하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// 문서 열기
Document pdfDocument = new Document(dataDir + "SplitToPages.pdf");

int pageCount = 1;

// 모든 페이지를 순회
foreach (Page pdfPage in pdfDocument.Pages)
{
    Document newDocument = new Document();
    newDocument.Pages.Add(pdfPage);
    newDocument.Save(dataDir + "page_" + pageCount + "_out" + ".pdf");
    pageCount++;
}
```

