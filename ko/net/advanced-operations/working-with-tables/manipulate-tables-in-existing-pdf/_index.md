---
title: 기존 PDF에서 테이블 조작
linktitle: 테이블 조작
type: docs
weight: 40
url: /ko/net/manipulate-tables-in-existing-pdf/
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "기존 PDF에서 테이블 조작",
    "alternativeHeadline": "기존 PDF에서 테이블 내용 업데이트 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, 테이블 조작",
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
    "url": "/net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script
## 기존 PDF에서 테이블 조작하기

Aspose.PDF for .NET이 지원하는 가장 초기 기능 중 하나는 테이블 작업 기능이며, 처음부터 생성되거나 기존 PDF 파일에서 테이블을 추가하는 데 큰 지원을 제공합니다. 또한 데이터베이스 내용을 기반으로 동적 테이블을 생성하기 위해 데이터베이스(DOM)와 테이블을 통합할 수 있는 기능도 제공합니다. 이 새로운 릴리스에서, 우리는 PDF 문서의 페이지에 이미 존재하는 간단한 테이블을 검색하고 파싱하는 새로운 기능을 구현했습니다. **Aspose.PDF.Text.TableAbsorber**라는 새로운 클래스가 이러한 기능을 제공합니다. TableAbsorber의 사용법은 기존 TextFragmentAbsorber 클래스와 매우 유사합니다. 다음 코드 스니펫은 특정 테이블 셀의 내용을 업데이트하는 단계를 보여줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리로의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// 기존 PDF 파일을 로드합니다.
Document pdfDocument = new Document(dataDir + "input.pdf");
// 테이블을 찾기 위한 TableAbsorber 객체를 생성합니다.
TableAbsorber absorber = new TableAbsorber();

// absorber로 첫 페이지를 방문합니다.
absorber.Visit(pdfDocument.Pages[1]);

// 페이지의 첫 테이블에 접근하여 그 첫 셀과 그 안의 텍스트 조각들을 가져옵니다.
TextFragment fragment = absorber.TableList[0].RowList[0].CellList[0].TextFragments[1];

// 셀의 첫 텍스트 조각의 텍스트를 변경합니다.
fragment.Text = "hi world";
dataDir = dataDir + "ManipulateTable_out.pdf";
pdfDocument.Save(dataDir);
```
## PDF 문서에서 오래된 테이블을 새 테이블로 교체하기

특정 테이블을 찾아 원하는 테이블로 교체해야하는 경우, [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) 클래스의 Replace() 메소드를 사용할 수 있습니다. 다음 예제는 PDF 문서 내부의 테이블을 교체하는 기능을 보여줍니다:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인해주세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// 기존 PDF 문서를 로드합니다
Document pdfDocument = new Document(dataDir + @"Table_input2.pdf");

// 테이블을 찾기 위한 TableAbsorber 객체를 생성합니다
TableAbsorber absorber = new TableAbsorber();

// absorber와 함께 첫 페이지를 방문합니다
absorber.Visit(pdfDocument.Pages[1]);

// 페이지에서 첫 번째 테이블을 가져옵니다
AbsorbedTable table = absorber.TableList[0];

// 새 테이블을 생성합니다
Table newTable = new Table();
newTable.ColumnWidths = "100 100 100";
newTable.DefaultCellBorder = new BorderInfo(BorderSide.All, 1F);

Row row = newTable.Rows.Add();
row.Cells.Add("Col 1");
row.Cells.Add("Col 2");
row.Cells.Add("Col 3");

// 새 테이블로 기존 테이블을 교체합니다
absorber.Replace(pdfDocument.Pages[1], table, newTable);

// 문서를 저장합니다
pdfDocument.Save(dataDir + "TableReplaced_out.pdf");
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
                "contactType": "영업",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "영업",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "영업",
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
    "applicationCategory": ".NET을 위한 PDF 조작 라이브러리",
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
```

