---
title: 기존 PDF에서 테이블 제거
linktitle: 테이블 제거
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /ko/net/remove-tables-from-existing-pdf/
description: Aspose.PDF for .NET을 사용하여 PDF 문서에서 테이블을 제거하는 방법을 이해하고 문서의 명확성과 구조를 개선합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Remove Tables from existing PDF",
    "alternativeHeadline": "Effortlessly Eliminate Tables from Existing PDF Files",
    "abstract": "Aspose.PDF for .NET의 테이블 제거 기능은 사용자가 TableAbsorber 클래스를 사용하여 기존 PDF 문서에서 테이블 객체를 효율적으로 제거할 수 있도록 합니다. 이 기능은 테이블을 찾고 제거하는 간단한 방법을 제공하여 PDF 콘텐츠 관리 프로세스를 단순화하고 문서 편집 기능을 향상시킵니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "494",
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
    "url": "/net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 처리할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하십시오."
}
</script>

{{% alert color="primary" %}}

Aspose.PDF for NET은 PDF 문서가 처음 생성될 때 테이블을 삽입/생성할 수 있는 기능을 제공하며, 기존 PDF 문서에 테이블 객체를 추가할 수도 있습니다. 그러나 기존 PDF에서 [테이블 조작](https://docs.aspose.com/pdf/net/manipulate-tables-in-existing-pdf/)이 필요할 수 있으며, 이 경우 기존 테이블 셀의 내용을 업데이트할 수 있습니다. 그러나 기존 PDF 문서에서 테이블 객체를 제거해야 할 필요가 있을 수 있습니다.

{{% /alert %}}

테이블을 제거하기 위해서는 [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) 클래스를 사용하여 기존 PDF의 테이블을 가져온 다음 [Remove](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/remove) 메서드를 호출해야 합니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## PDF 문서에서 테이블 제거

기존 TableAbsorber 클래스에 테이블을 PDF 문서에서 제거하기 위한 새로운 함수인 Remove()를 추가했습니다. 흡수기가 페이지에서 테이블을 성공적으로 찾으면 이를 제거할 수 있게 됩니다. PDF 문서에서 테이블을 제거하는 방법을 보여주는 다음 코드 스니펫을 확인하십시오:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Table_input.pdf"))
    {
        // Create TableAbsorber object to find tables
        var absorber = new Aspose.Pdf.Text.TableAbsorber();

        // Visit first page with absorber
        absorber.Visit(document.Pages[1]);

        // Get first table on the page
        Aspose.Pdf.Text.AbsorbedTable table = absorber.TableList[0];

        // Remove the table
        absorber.Remove(table);

        // Save PDF document
        document.Save(dataDir + "RemoveTable_out.pdf");
    }
}
```

## PDF 문서에서 여러 테이블 제거

때때로 PDF 문서에는 하나 이상의 테이블이 포함될 수 있으며, 여러 테이블을 제거해야 할 필요가 있을 수 있습니다. PDF 문서에서 여러 테이블을 제거하려면 다음 코드 스니펫을 사용하십시오:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveMultipleTables()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Table_input2.pdf"))
    {
        // Create TableAbsorber object to find tables
        var absorber = new Aspose.Pdf.Text.TableAbsorber();

        // Visit second page with absorber
        absorber.Visit(document.Pages[1]);

        // Get copy of table collection
        Aspose.Pdf.Text.AbsorbedTable[] tables = new Aspose.Pdf.Text.AbsorbedTable[absorber.TableList.Count];
        absorber.TableList.CopyTo(tables, 0);

        // Loop through the copy of collection and removing tables
        foreach (var table in tables)
        {
            absorber.Remove(table);
        }

        // Save PDF document
        document.Save(dataDir + "RemoveMultipleTables_out.pdf");
    }
}
```

{{% alert color="primary" %}}

테이블을 제거하거나 교체하면 TableList 컬렉션이 변경됩니다. 따라서 루프에서 테이블을 제거/교체하는 경우 TableList 컬렉션을 복사하는 것이 필수적입니다.

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