---
title: 从现有PDF中移除表格
linktitle: 移除表格
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /zh/net/remove-tables-from-existing-pdf/
description: 了解如何使用Aspose.PDF for .NET从PDF文档中移除表格，提高文档的清晰度和结构。
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
    "abstract": "Aspose.PDF for .NET中的移除表格功能允许用户使用TableAbsorber类有效地消除现有PDF文档中的表格对象。此功能通过提供简单的方法来定位和移除表格，从而简化了管理PDF内容的过程，增强了文档编辑能力。",
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
    "description": "Aspose.PDF不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分，适合高级用户和开发人员。"
}
</script>

{{% alert color="primary" %}}

Aspose.PDF for NET提供了在生成PDF文档时插入/创建表格的功能，您也可以在任何现有PDF文档中添加表格对象。然而，您可能需要[操作现有PDF中的表格](https://docs.aspose.com/pdf/net/manipulate-tables-in-existing-pdf/)，在其中更新现有表格单元格的内容。然而，您可能会遇到需要从现有PDF文档中移除表格对象的需求。

{{% /alert %}}

为了移除表格，我们需要使用[TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber)类来获取现有PDF中的表格，然后调用[Remove](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/remove)。

以下代码片段也适用于[Aspose.PDF.Drawing](/pdf/zh/net/drawing/)库。

## 从PDF文档中移除表格

我们在现有的TableAbsorber类中添加了新功能，即Remove()，以便从PDF文档中移除表格。一旦吸收器成功找到页面上的表格，它就能够将其移除。请查看以下代码片段，展示如何从PDF文档中移除表格：

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

## 从PDF文档中移除多个表格

有时，PDF文档可能包含多个表格，您可能会遇到需要从中移除多个表格的需求。为了从PDF文档中移除多个表格，请使用以下代码片段：

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

请注意，移除或替换表格会改变TableList集合。因此，在循环中移除/替换表格时，复制TableList集合是必不可少的。

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