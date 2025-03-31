---
title: 기존 PDF에서 테이블 조작
linktitle: 테이블 조작
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/manipulate-tables-in-existing-pdf/
description: Aspose.PDF for .NET을 사용하여 기존 PDF의 테이블 작업 방법을 배우고 문서 수정의 유연성을 제공합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate Tables in existing PDF",
    "alternativeHeadline": "Enhance Table Editing in Existing PDF Documents",
    "abstract": "Aspose.PDF for .NET은 기존 PDF 테이블을 조작하는 강력한 기능을 소개하여 사용자가 테이블 내용을 쉽게 검색, 구문 분석 및 수정할 수 있도록 합니다. 새로운 TableAbsorber 클래스는 PDF 문서 내에서 테이블을 동적으로 업데이트하고 교체할 수 있게 하여 PDF에서 표 형식 데이터를 관리하는 프로세스를 간소화합니다. PDF 편집 및 데이터 통합 작업을 최적화하기 위해 이 혁신적인 기능을 탐색하십시오.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

## 기존 PDF에서 테이블 조작

Aspose.PDF for .NET이 지원하는 초기 기능 중 하나는 테이블 작업 기능이며, 이는 처음부터 생성된 PDF 파일이나 기존 PDF 파일에 테이블을 추가하는 데 큰 지원을 제공합니다. 또한 데이터베이스 내용을 기반으로 동적 테이블을 생성하기 위해 테이블을 데이터베이스(DOM)와 통합할 수 있는 기능도 제공합니다. 이번 새로운 릴리스에서는 PDF 문서 페이지에 이미 존재하는 간단한 테이블을 검색하고 구문 분석하는 새로운 기능을 구현했습니다. **Aspose.PDF.Text.TableAbsorber**라는 새로운 클래스가 이러한 기능을 제공합니다. TableAbsorber의 사용법은 기존 TextFragmentAbsorber 클래스와 매우 유사합니다. 다음 코드 스니펫은 특정 테이블 셀의 내용을 업데이트하는 단계를 보여줍니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 작동합니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ManipulateTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create TableAbsorber object to find tables
        var absorber = new Aspose.Pdf.Text.TableAbsorber();

        // Visit first page with absorber
        absorber.Visit(document.Pages[1]);

        // Get access to first table on page, their first cell and text fragments in it
        Aspose.Pdf.Text.TextFragment fragment = absorber.TableList[0].RowList[0].CellList[0].TextFragments[1];

        // Change text of the first text fragment in the cell
        fragment.Text = "hi world";

        // Save PDF document
        document.Save(dataDir + "ManipulateTable_out.pdf");
    }
}
```

## PDF 문서에서 오래된 테이블을 새 테이블로 교체

특정 테이블을 찾아 원하는 테이블로 교체해야 하는 경우, [TableAbsorber](https://reference.aspose.com/pdf/ko/net/aspose.pdf.text/tableabsorber) 클래스의 Replace() 메서드를 사용하여 이를 수행할 수 있습니다. 다음 예제는 PDF 문서 내에서 테이블을 교체하는 기능을 보여줍니다.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Table_input2.pdf"))
    {
        // Create TableAbsorber object to find tables
        var absorber = new Aspose.Pdf.Text.TableAbsorber();

        // Visit first page with absorber
        absorber.Visit(document.Pages[1]);

        // Get first table on the page
        Aspose.Pdf.Text.AbsorbedTable table = absorber.TableList[0];

        // Create new table
        var newTable = new Aspose.Pdf.Table();
        newTable.ColumnWidths = "100 100 100";
        newTable.DefaultCellBorder = new Aspose.Pdf.BorderInfo(BorderSide.All, 1F);

        Row row = newTable.Rows.Add();
        row.Cells.Add("Col 1");
        row.Cells.Add("Col 2");
        row.Cells.Add("Col 3");

        // Replace the table with new one
        absorber.Replace(document.Pages[1], table, newTable);

        // Save PDF document
        document.Save(dataDir + "ReplaceTable_out.pdf");
    }
}
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