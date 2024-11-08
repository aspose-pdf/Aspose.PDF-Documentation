---
title: C#에서 PDF 페이지 다루기
linktitle: 페이지 작업
type: docs
weight: 20
url: /ko/net/working-with-pages/
description: 페이지 추가, 헤더 및 푸터 추가, 워터마크 추가 방법은 이 섹션에서 알 수 있습니다. Aspose.PDF for .NET가 이 주제에 대한 모든 세부 사항을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
aliases:
    - /net/working-with-stamps-and-watermarks/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "C#에서 PDF 페이지 다루기",
    "alternativeHeadline": "PDF 페이지 작업 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, pdf 페이지, pdf 페이지 추가, 페이지 번호 추가, 페이지 회전, 페이지 삭제",
    "wordcount": "302",
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
    "url": "/net/working-with-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "페이지 추가, 헤더 및 푸터 추가, 워터마크 추가 방법은 이 섹션에서 알 수 있습니다. Aspose.PDF for .NET가 이 주제에 대한 모든 세부 사항을 설명합니다."
}
</script>

**Aspose.PDF for .NET** 은 파일의 어느 위치에나 페이지를 삽입하거나 PDF 파일 끝에 페이지를 추가할 수 있습니다. 이 섹션에서는 Acrobat Reader 없이 PDF에 페이지를 추가하는 방법을 보여줍니다.
PDF 파일의 헤더와 푸터에 텍스트 또는 이미지를 추가하고 Aspose의 C# 라이브러리를 사용하여 문서에서 다른 헤더를 선택할 수 있습니다.
또한 C#을 사용하여 PDF 문서에서 페이지를 프로그래밍 방식으로 자르십시오.

이 섹션에서는 Artifact 클래스를 사용하여 PDF 파일에 워터마크를 추가하는 방법을 배웁니다. 이 작업을 위한 프로그래밍 샘플을 확인하십시오.
PageNumberStamp 클래스를 사용하여 페이지 번호를 추가하십시오. 문서에 스탬프를 추가하려면 ImageStamp 및 TextStamp 클래스를 사용하십시오. **Aspose.PDF for .NET**을 사용하여 PDF 파일에서 배경 이미지를 생성하기 위해 워터마크를 추가하십시오.

다음을 수행할 수 있습니다:

- [페이지 추가](/pdf/ko/net/add-pages/) - 원하는 위치에 페이지를 추가하거나 PDF 파일 끝에 페이지를 추가하고 문서에서 페이지를 삭제합니다.
- [페이지 이동](/pdf/ko/net/move-pages/) - 한 문서에서 다른 문서로 페이지를 이동합니다.
- [페이지 이동](/pdf/ko/net/move-pages/) - 한 문서에서 다른 문서로 페이지를 이동합니다.
- [페이지 삭제](/pdf/ko/net/delete-pages/) - PageCollection 컬렉션을 사용하여 PDF 파일에서 페이지를 삭제합니다.
- [페이지 크기 변경](/pdf/ko/net/change-page-size/) - Aspose.PDF 라이브러리를 사용하여 코드 스니펫으로 PDF 페이지 크기를 변경할 수 있습니다.
- [페이지 회전](/pdf/ko/net/rotate-pages/) - 기존 PDF 파일의 페이지 방향을 변경할 수 있습니다.
- [페이지 분할](/pdf/ko/net/split-document/) - PDF 파일을 하나 또는 여러 PDF로 분할할 수 있습니다.
- [헤더 및/또는 풋터 추가](/pdf/ko/net/add-headers-and-footers-of-pdf-file/) - PDF 파일의 헤더와 풋터에 텍스트나 이미지를 추가합니다.
- [페이지 자르기](/pdf/ko/net/crop-pages/) - 다양한 페이지 속성을 가진 PDF 문서에서 프로그래밍 방식으로 페이지를 자를 수 있습니다.
- [워터마크 추가](/pdf/ko/net/add-watermarks/) - Artifact Class를 사용하여 PDF 파일에 워터마크를 추가합니다.
- [PDF 파일에 페이지 번호 추가](/pdf/ko/net/add-page-number/) - PageNumberStamp 클래스를 사용하여 PDF 파일에 페이지 번호를 추가할 수 있습니다.
- [PDF 파일에 페이지 번호 추가](/pdf/ko/net/add-page-number/) - PageNumberStamp 클래스를 사용하면 PDF 파일에 페이지 번호를 추가할 수 있습니다.
- [배경 추가](/pdf/ko/net/add-backgrounds/) - 배경 이미지를 사용하여 워터마크를 추가할 수 있습니다.
- [스탬핑](/pdf/ko/net/stamping/) - ImageStamp 클래스를 사용하여 PDF 파일에 이미지 스탬프를 추가하고 TextStamp 클래스를 사용하여 텍스트를 추가할 수 있습니다.

