---
title: 기존 PDF에서 테이블 제거
linktitle: 테이블 제거
type: docs
weight: 50
url: ko/python-net/remove-tables-from-existing-pdf/
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "기존 PDF에서 테이블 제거",
    "alternativeHeadline": "PDF에서 테이블 삭제 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, python, 테이블 제거, 테이블 삭제",
    "wordcount": "302",
    "proficiencyLevel":"초급",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2023-02-04",
    "description": ""
}
</script>


{{% alert color="primary" %}}

Aspose.PDF for Python via .NET은 PDF 문서를 처음부터 생성할 때 테이블을 삽입/생성하는 기능을 제공하며, 기존의 PDF 문서에 테이블 객체를 추가할 수도 있습니다. 그러나 기존 테이블 셀의 내용을 업데이트해야 하는 [기존 PDF의 테이블 조작](https://docs.aspose.com/pdf/python-net/manipulate-tables-in-existing-pdf/)이 필요할 수 있습니다. 그러나 기존 PDF 문서에서 테이블 객체를 제거해야 하는 요구 사항에 직면할 수 있습니다.

{{% /alert %}}

테이블을 제거하기 위해서는 [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) 클래스를 사용하여 기존 PDF의 테이블을 확보한 다음 [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods)를 호출해야 합니다.

## PDF 문서에서 테이블 제거

새로운 기능을 추가했습니다. 즉,
 [remove()](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods)를 사용하여 PDF 문서에서 테이블을 제거하기 위해 기존 [TableAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/) 클래스에 추가합니다. 흡수기가 페이지에서 테이블을 성공적으로 찾으면 이를 제거할 수 있게 됩니다. PDF 문서에서 테이블을 제거하는 방법을 보여주는 다음 코드 스니펫을 확인하십시오:

```python

    import aspose.pdf as ap

    # 기존 PDF 문서 로드
    pdf_document = ap.Document(input_file)
    # 테이블을 찾기 위한 TableAbsorber 객체 생성
    absorber = ap.text.TableAbsorber()
    # 첫 번째 페이지를 흡수기로 방문
    absorber.visit(pdf_document.pages[1])
    # 페이지에서 첫 번째 테이블 가져오기
    table = absorber.table_list[0]
    # 테이블 제거
    absorber.remove(table)
    # PDF 저장
    pdf_document.save(output_file)
```

## PDF 문서에서 여러 테이블 제거

때때로 PDF 문서에는 하나 이상의 테이블이 포함될 수 있으며, 여러 테이블을 제거해야 할 수도 있습니다. 여러 테이블을 PDF 문서에서 제거하려면 다음 코드 스니펫을 사용하십시오:

```python

    import aspose.pdf as ap

    # 기존 PDF 문서 로드
    pdf_document = ap.Document(input_file)
    # 테이블을 찾기 위한 TableAbsorber 객체 생성
    absorber = ap.text.TableAbsorber()
    # 흡수기와 함께 두 번째 페이지 방문
    absorber.visit(pdf_document.pages[1])
    # 테이블 컬렉션의 복사본 가져오기
    tables = absorber.table_list
    # 컬렉션의 복사본을 반복하며 테이블 제거
    for table in tables:
        absorber.remove(table)
    # 문서 저장
    pdf_document.save(output_file)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>