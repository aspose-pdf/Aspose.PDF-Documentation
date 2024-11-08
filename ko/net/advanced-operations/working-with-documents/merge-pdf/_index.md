---
title: C#을 사용하여 PDF 병합 방법
linktitle: PDF 파일 병합
type: docs
weight: 50
url: /ko/net/merge-pdf-documents/
keywords: "merge multiple pdf into single pdf c#, combine multiple pdf into one c#, merge multiple pdf into one c#"
description: 이 페이지는 C# 또는 VB.NET을 사용하여 PDF 문서를 단일 PDF 파일로 병합하는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#을 사용하여 PDF 병합 방법",
    "alternativeHeadline": "PDF 문서 결합",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 조작",
    "keywords": "pdf, c#, merge pdf, concatenate, combine pdf",
    "wordcount": "212",
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
    "url": "https://docs.aspose.com/pdf/net/merge-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://docs.aspose.com/pdf/net/merge-pdf-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "이 페이지는 C# 또는 VB.NET을 사용하여 PDF 문서를 단일 PDF 파일로 병합하는 방법을 설명합니다."
}
</script>

## C#에서 여러 PDF를 단일 PDF로 병합 또는 결합

C#에서 PDF를 병합하는 것은 3rd 파티 라이브러리를 사용하지 않고는 간단하지 않습니다.
이 글은 Aspose.PDF for .NET을 사용하여 여러 PDF 파일을 단일 PDF 문서로 병합하는 방법을 보여줍니다. 예제는 C#으로 작성되었지만, API는 VB.NET과 같은 다른 .NET 프로그래밍 언어에서도 사용할 수 있습니다. PDF 파일은 첫 번째 파일이 다른 문서의 끝에 연결되도록 병합됩니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

## C# 및 DOM을 사용하여 PDF 파일 병합

두 PDF 파일을 연결하려면:

1. 입력 PDF 파일이 각각 포함된 두 개의 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 생성합니다.
1. 다른 PDF 파일을 추가하고자 하는 Document 객체에 대해 [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) 컬렉션의 Add 메서드를 호출합니다.
1.
1. 마지막으로 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 출력 PDF 파일을 저장하세요.

다음 코드 조각은 PDF 파일을 연결하는 방법을 보여줍니다.

```csharp
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

// 첫 번째 문서 열기
Document pdfDocument1 = new Document(dataDir + "Concat1.pdf");
// 두 번째 문서 열기
Document pdfDocument2 = new Document(dataDir + "Concat2.pdf");

// 두 번째 문서의 페이지를 첫 번째 문서에 추가
pdfDocument1.Pages.Add(pdfDocument2.Pages);

dataDir = dataDir + "ConcatenatePdfFiles_out.pdf";
// 연결된 출력 파일 저장
pdfDocument1.Save(dataDir);
```

## 실시간 예제

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger)는 프레젠테이션 병합 기능이 작동하는 방식을 조사할 수 있는 온라인 무료 웹 애플리케이션입니다.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)

## 참고하세요

- [DOM을 사용한 PDF 분할](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [DOM을 사용하여 PDF 분할](https://docs.aspose.com/pdf/net/split-pdf-document/)
- [Facades를 사용하여 PDF 문서 연결](https://docs.aspose.com/pdf/net/concatenate-pdf-documents/)
- [Facades를 사용하여 PDF 분할](https://docs.aspose.com/pdf/net/split-pdf-pages/)

