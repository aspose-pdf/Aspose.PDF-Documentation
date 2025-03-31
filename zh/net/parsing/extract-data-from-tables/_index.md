---
title: 使用 C# 从 PDF 中提取表格数据
linktitle: 提取表格数据
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /zh/net/extract-data-from-table-in-pdf/
description: 学习如何使用 Aspose.PDF for .NET 在 C# 中从 PDF 中提取表格数据
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Data from Table in PDF with C#",
    "alternativeHeadline": "Effortlessly Extract Tables from PDFs Using C#",
    "abstract": "发现使用 Aspose.PDF for .NET 在 C# 中从 PDF 文档中提取表格数据的强大能力。此功能通过允许用户无缝访问单个单元格并将提取的数据存储为 CSV 和 Excel 等格式，简化了检索和处理表格的过程，提高了数据的可访问性和可用性。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "695",
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
    "url": "/net/extract-data-from-table-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-data-from-table-in-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 以编程方式从 PDF 中提取表格

从 PDF 中提取表格并不是一项简单的任务，因为表格可以以多种方式创建。

Aspose.PDF for .NET 提供了一种工具，使检索表格变得简单。要提取表格数据，您应执行以下步骤：

1. 打开文档 - 实例化一个 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document) 对象。
1. 创建一个 [TableAbsorber](https://reference.aspose.com/pdf/zh/net/aspose.pdf.text/tableabsorber) 对象。
1. 决定要分析哪些页面，并将 [Visit](https://reference.aspose.com/pdf/zh/net/aspose.pdf.text/tableabsorber/methods/visit) 应用到所需页面。表格数据将被扫描，结果将存储在 [TableList](https://reference.aspose.com/pdf/zh/net/aspose.pdf.text/tableabsorber/properties/tablelist) 中。
1. `TableList` 是一个 [AbsorbedTable](https://reference.aspose.com/pdf/zh/net/aspose.pdf.text/absorbedtable) 的列表。要获取数据，请遍历 `TableList` 并处理 [RowList](https://reference.aspose.com/pdf/zh/net/aspose.pdf.text/absorbedtable/properties/rowlist) 和 [CellList](https://reference.aspose.com/pdf/zh/net/aspose.pdf.text/absorbedrow/properties/celllist)。
1. 每个 [AbsorbedCell](https://reference.aspose.com/pdf/zh/net/aspose.pdf.text/absorbedcell) 包含 [TextFragments](https://reference.aspose.com/pdf/zh/net/aspose.pdf.text/absorbedcell/properties/textfragments) 集合。您可以根据自己的需要处理它。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

以下示例显示了如何从所有页面提取表格：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {                    
        foreach (var page in document.Pages)
        {
            Aspose.Pdf.TableAbsorber absorber = new Aspose.Pdf.TableAbsorber();
            absorber.Visit(page);
            foreach (var table in absorber.TableList)
            {
                Console.WriteLine("Table");
                foreach (var row in table.RowList)
                {
                    foreach (var cell in row.CellList)
                    {                                 
                        foreach (var fragment in cell.TextFragments)
                        {
                            var sb = new StringBuilder();
                            foreach (var seg in fragment.Segments)
                            {
                                sb.Append(seg.Text);
                            }
                            Console.Write($"{sb.ToString()}|");
                        }                           
                    }
                    Console.WriteLine();
                }
            }
        }
    }
}
```

## 从 PDF 页面特定区域提取表格

每个吸收的表格都有 [Rectangle](https://reference.aspose.com/pdf/zh/net/aspose.pdf.text/absorbedtable/properties/rectangle) 属性，描述表格在页面上的位置。

如果您需要提取位于特定区域的表格，您必须使用特定坐标。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

以下示例显示了如何提取带有方形注释的表格：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractMarkedTable()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    { 
        var page = document.Pages[1];
        var squareAnnotation =
            page.Annotations.FirstOrDefault(ann => ann.AnnotationType == Annotations.AnnotationType.Square)
            as Aspose.Pdf.Annotations.SquareAnnotation;


        var absorber = new Aspose.Pdf.Text.TableAbsorber();
        absorber.Visit(page);

        foreach (var table in absorber.TableList)
        {
            var isInRegion = (squareAnnotation.Rect.LLX < table.Rectangle.LLX) &&
            (squareAnnotation.Rect.LLY < table.Rectangle.LLY) &&
            (squareAnnotation.Rect.URX > table.Rectangle.URX) &&
            (squareAnnotation.Rect.URY > table.Rectangle.URY);

            if (isInRegion)
            {
                foreach (var row in table.RowList)
                {
                    foreach (var cell in row.CellList)
                    {
                        foreach (var fragment in cell.TextFragments)
                        {
                            var sb = new StringBuilder();
                            foreach (var seg in fragment.Segments)
                            {
                                sb.Append(seg.Text);
                            }
                            var text = sb.ToString();
                            Console.Write($"{text}|");
                        }
                    }
                    Console.WriteLine();
                }
            }
        }
    }
}
```

## 从 PDF 中提取表格数据并将其存储在 CSV 文件中

以下示例显示了如何提取表格并将其存储为 CSV 文件。
要查看如何将 PDF 转换为 Excel 电子表格，请参阅 [将 PDF 转换为 Excel](/pdf/zh/net/convert-pdf-to-excel/) 文章。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTableSaveExcel()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate ExcelSave Option object
        Aspose.Pdf.ExcelSaveOptions excelSave = new Aspose.Pdf.ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };

        // Save the output in XLS format
        document.Save(dataDir + "ExtractTableSaveXLS_out.xlsx", excelSave);
    }
}
```