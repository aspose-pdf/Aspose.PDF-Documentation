---
title: 기존 PDF에서 테이블 제거
linktitle: 테이블 제거
type: docs
weight: 50
url: /ko/net/remove-tables-from-existing-pdf/
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "기존 PDF에서 테이블 제거",
    "alternativeHeadline": "PDF에서 테이블 삭제하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, 테이블 제거, 테이블 삭제",
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
                "contactType": "판매",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "판매",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "판매",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
{{% alert color="primary" %}}

Aspose.PDF for NET은 PDF 문서를 처음부터 생성하거나 기존 PDF 문서에 테이블 객체를 추가하면서 테이블을 삽입/생성할 수 있는 기능을 제공합니다. 그러나 기존 테이블 셀의 내용을 업데이트할 수 있는 [기존 PDF에서 테이블 조작하기](https://docs.aspose.com/pdf/net/manipulate-tables-in-existing-pdf/)에 대한 요구 사항이 있을 수 있습니다. 또한 기존 PDF 문서에서 테이블 객체를 제거해야 할 수도 있습니다.

{{% /alert %}}

테이블을 제거하려면 [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) 클래스를 사용하여 기존 PDF에서 테이블을 찾은 다음 [Remove](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/remove)를 호출해야 합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 함께 작동합니다.

## PDF 문서에서 테이블 제거

새로운 함수를 추가했습니다.
새로운 함수를 추가했습니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// 기존 PDF 문서를 로드합니다.
Document pdfDocument = new Document(dataDir + "Table_input.pdf");

// 테이블을 찾기 위해 TableAbsorber 객체를 생성합니다.
TableAbsorber absorber = new TableAbsorber();

// absorber를 사용하여 첫 번째 페이지를 방문합니다.
absorber.Visit(pdfDocument.Pages[1]);

// 페이지에서 첫 번째 테이블을 가져옵니다.
AbsorbedTable table = absorber.TableList[0];

// 테이블을 제거합니다.
absorber.Remove(table);

// PDF를 저장합니다.
pdfDocument.Save(dataDir + "Table_out.pdf");
```

## PDF 문서에서 여러 테이블 제거

가끔 PDF 문서에 여러 테이블이 포함되어 있을 수 있으며, 이러한 테이블들을 제거할 필요가 있을 수 있습니다. PDF 문서에서 여러 테이블을 제거하려면 다음 코드 스니펫을 사용하십시오:

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// 기존 PDF 문서를 로드합니다.
Document pdfDocument = new Document(dataDir + "Table_input2.pdf");

// 테이블을 찾기 위해 TableAbsorber 객체를 생성합니다.
TableAbsorber absorber = new TableAbsorber();

// absorber를 사용하여 두 번째 페이지를 방문합니다.
absorber.Visit(pdfDocument.Pages[1]);

// 테이블 컬렉션의 복사본을 가져옵니다.
AbsorbedTable[] tables = new AbsorbedTable[absorber.TableList.Count];
absorber.TableList.CopyTo(tables, 0);

// 컬렉션의 복사본을 반복하면서 테이블을 제거합니다.
foreach (AbsorbedTable table in tables)
    absorber.Remove(table);

// 문서를 저장합니다.
pdfDocument.Save(dataDir + "Table2_out.pdf");
```
{{% alert color="primary" %}}

테이블을 제거하거나 교체할 경우 TableList 컬렉션이 변경됨을 유의하십시오. 따라서 루프에서 테이블을 제거/교체하는 경우 TableList 컬렉션을 복사하는 것이 필수적입니다.

{{% /alert %}}

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


