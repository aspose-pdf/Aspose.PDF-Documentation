---
title: PDF 페이지를 프로그래밍 방식으로 이동 C#
linktitle: PDF 페이지 이동
type: docs
weight: 20
url: /net/move-pages/
description: Aspose.PDF for .NET을 사용하여 원하는 위치나 PDF 파일의 끝에 페이지를 이동해보세요.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 페이지를 프로그래밍 방식으로 이동 C#",
    "alternativeHeadline": ".NET을 사용한 PDF 페이지 이동 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, pdf 페이지 이동",
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
    "url": "/net/move-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF for .NET을 사용하여 원하는 위치나 PDF 파일의 끝에 페이지를 이동해보세요."
}
</script>
## PDF 문서에서 다른 문서로 페이지 이동하기

이 주제는 C#을 사용하여 한 PDF 문서에서 다른 문서 끝으로 페이지를 이동하는 방법에 대해 설명합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리에서도 작동합니다.

페이지를 이동하려면 다음을 수행해야 합니다:

1. 소스 PDF 파일을 가진 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스 객체를 생성합니다.
1. 목적지 PDF 파일을 가진 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스 객체를 생성합니다.
1. [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 컬렉션에서 페이지를 가져옵니다.
1. 목적지 문서에 페이지를 [추가](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1)합니다.
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메소드를 사용하여 출력 PDF를 저장합니다.
1. 원본 문서에서 페이지를 [삭제](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1)합니다.
1.

다음 코드 스니펫은 한 페이지를 이동하는 방법을 보여줍니다.

```csharp
var srcFileName = "<파일 이름 입력>";
var dstFileName = "<파일 이름 입력>";
var srcDocument = new Document(srcFileName);
var dstDocument = new Document();
var page = srcDocument.Pages[2];
dstDocument.Pages.Add(page);
// 출력 파일 저장
dstDocument.Save(srcFileName);
srcDocument.Pages.Delete(2);
srcDocument.Save(dstFileName);
```

## 한 PDF 문서에서 다른 PDF 문서로 여러 페이지 이동하기

1. 소스 PDF 파일로 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스 객체를 생성합니다.
1. 목적지 PDF 파일로 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 클래스 객체를 생성합니다.
1. 이동할 페이지 번호를 포함한 배열을 정의합니다.
1. 배열을 통해 반복 실행:
    1. [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 컬렉션에서 페이지를 가져옵니다.
    1.
1. 출력 PDF를 [저장](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 저장하세요.
1. 배열을 사용하여 원본 문서에서 [삭제](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/2) 페이지를 삭제하세요.
1. 원본 PDF를 [저장](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 저장하세요.

다음 코드 스니펫은 한 PDF 문서에서 다른 PDF 문서로 여러 페이지를 이동하는 방법을 보여줍니다.

```csharp
var srcFileName = "<파일 이름 입력>";
var dstFileName = "<파일 이름 입력>";
var srcDocument = new Aspose.Pdf.Document(srcFileName);
var dstDocument = new Aspose.Pdf.Document();
var pages = new []{ 1, 3 };
foreach (var pageIndex in pages)
{
    var page = srcDocument.Pages[pageIndex];
    dstDocument.Pages.Add(page);
}                       
// 출력 파일 저장
dstDocument.Save(dstFileName);
srcDocument.Pages.Delete(pages);
srcDocument.Save(srcFileName);
```

## 현재 PDF 문서에서 새 위치로 페이지 이동

1.
1. [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 컬렉션에서 페이지를 가져옵니다.
1. 예를 들어 끝에 페이지를 새 위치에 [추가](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/add/methods/1)합니다.
1. 이전 위치에서 페이지를 [삭제](https://reference.aspose.com/pdf/net/aspose.pdf.pagecollection/delete/methods/1)합니다.
1. [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메소드를 사용하여 출력 PDF를 저장합니다.

```csharp
var srcFileName = "<enter file name>";
var dstFileName = "<enter file name>";
var srcDocument = new Aspose.Pdf.Document(srcFileName);

var page = srcDocument.Pages[2];
srcDocument.Pages.Add(page);
srcDocument.Pages.Delete(2);          

// Save output file
srcDocument.Save(dstFileName);
```

