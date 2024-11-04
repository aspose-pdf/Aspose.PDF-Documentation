---
title: PDF 문서에 첨부 파일 추가
linktitle: PDF 문서에 첨부 파일 추가
type: docs
weight: 10
url: /net/add-attachment-to-pdf-document/
description: 이 페이지는 Aspose.PDF for .NET 라이브러리를 사용하여 PDF 파일에 첨부 파일을 추가하는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/adding-to-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF 문서에 첨부 파일 추가",
    "alternativeHeadline": "PDF에 첨부 파일 추가하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, pdf에서의 첨부 파일",
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
    "url": "/net/add-attachment-to-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-attachment-to-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "이 페이지는 Aspose.PDF for .NET 라이브러리를 사용하여 PDF 파일에 첨부 파일을 추가하는 방법을 설명합니다."
}
</script>

첨부 파일에는 다양한 정보가 포함될 수 있으며, 다양한 파일 유형이 있을 수 있습니다. 이 문서는 PDF 파일에 첨부 파일을 추가하는 방법을 설명합니다.

다음 코드 스니펫은 새로운 그래픽 [Aspose.Drawing](/pdf/net/drawing/) 인터페이스에서도 작동합니다.

1. 새 C# 프로젝트를 생성합니다.
1. Aspose.PDF DLL에 대한 참조를 추가합니다.
1. [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 생성합니다.
1. 추가하는 파일과 파일 설명이 포함된 [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) 객체를 생성합니다.
1. [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification) 객체를 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) 컬렉션에 추가 메소드를 사용하여 추가합니다.

[EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) 컬렉션에는 PDF 파일의 모든 첨부 파일이 포함되어 있습니다.
[EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) 컬렉션은 PDF 파일의 모든 첨부 파일을 포함하고 있습니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해 주세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// 문서 열기
Document pdfDocument = new Document(dataDir + "AddAttachment.pdf");

// 첨부 파일로 추가될 새 파일 설정
FileSpecification fileSpecification = new FileSpecification(dataDir + "test.txt", "샘플 텍스트 파일");

// 문서의 첨부 파일 컬렉션에 첨부 파일 추가
pdfDocument.EmbeddedFiles.Add(fileSpecification);

// 업데이트된 문서 저장
pdfDocument.Save(dataDir + "AddllAnnotations_out.pdf");
```

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

