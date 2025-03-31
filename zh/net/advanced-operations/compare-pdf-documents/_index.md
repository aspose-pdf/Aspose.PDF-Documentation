---
title: 比较 PDF 文档
linktitle: 比较 PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 130
url: /zh/net/compare-pdf-documents/
description: 自 24.7 版本发布以来，可以通过注释标记和并排输出比较 PDF 文档内容
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Compare PDF documents",
    "alternativeHeadline": "Enhanced PDF Document Comparison with Visual Highlights",
    "abstract": "Aspose.PDF for .NET 中的新 PDF 比较功能允许用户高效识别两个 PDF 文档之间的差异，可以按特定页面或整个内容进行比较。通过并排输出和可自定义的选项，如额外的变更标记和各种比较模式，这个强大的工具通过使修订易于跟踪和审查来增强协作",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Compare PDF documents, PDF comparison, Aspose.PDF for .NET, comparing specific pages, comparing entire documents, graphical PDF comparer, side-by-side comparison, change markers, document accuracy, ImagesDifference",
    "wordcount": "1180",
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
    "url": "/net/compare-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/compare-pdf-documents/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

请注意，所有比较工具均可在 [Aspose.PDF.Drawing](https://docs.aspose.com/pdf/net/drawing/) 库中使用。

## 比较 PDF 文档的方法

在处理 PDF 文档时，有时需要比较两个文档的内容以识别差异。Aspose.PDF for .NET 库提供了一个强大的工具集来实现这一目的。在本文中，我们将探讨如何使用几个简单的代码片段比较 PDF 文档。

Aspose.PDF 中的比较功能允许您逐页比较两个 PDF 文档。您可以选择比较特定页面或整个文档。生成的比较文档突出显示差异，使识别两个文件之间的更改变得更加容易。

以下是使用 Aspose.PDF for .NET 库比较 PDF 文档的可能方法列表：

1. **比较特定页面** - 比较两个 PDF 文档的第一页。

1. **比较整个文档** - 比较两个 PDF 文档的整个内容。

1. **图形比较 PDF 文档**：

- 使用 GetDifference 方法比较 PDF - 标记更改的单独图像。

- 使用 CompareDocumentsToPdf 方法比较 PDF - 标记更改的 PDF 文档图像。

## 比较特定页面

第一个代码片段演示了如何比较两个 PDF 文档的第一页。

步骤：

1. 文档初始化。
代码首先使用各自的文件路径（documentPath1 和 documentPath2）初始化两个 PDF 文档。路径目前指定为空字符串，但在实际操作中，您需要将其替换为实际的文件路径。

2. 比较过程。

- 页面选择 - 比较仅限于每个文档的第一页（'Pages[1]'）。
- 比较选项：

'AdditionalChangeMarks = true' - 此选项确保显示额外的变更标记。这些标记突出显示可能存在于其他页面上的差异，即使它们不在当前正在比较的页面上。

'ComparisonMode = ComparisonMode.IgnoreSpaces' - 此模式告诉比较器忽略文本中的空格，仅关注单词内的更改。

3. 生成的比较文档突出显示两个页面之间的差异，并保存到 'resultPdfPath' 指定的文件路径中。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingSpecificPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingSpecificPages2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], dataDir + "ComparingSpecificPages_out.pdf", new Aspose.Pdf.Comparison.SideBySideComparisonOptions
            {
                AdditionalChangeMarks = true,
                ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
            });
        }
    }
}
```

## 比较整个文档

第二个代码片段扩展了范围，以比较两个 PDF 文档的整个内容。

步骤：

1. 文档初始化。
与第一个示例一样，两个 PDF 文档使用其文件路径进行初始化。

2. 比较过程。

- 整个文档比较 - 与第一个代码片段不同，此代码比较两个文档的整个内容。

- 比较选项 - 选项与第一个代码片段相同，确保忽略空格，并显示额外的变更标记。

3. 比较结果突出显示两个文档所有页面之间的差异，并保存在 'resultPdfPath' 指定的文件中。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparingEntireDocuments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparingEntireDocuments2.pdf"))
        {
            // Compare
            Aspose.Pdf.Comparison.SideBySidePdfComparer.Compare(
                document1,
                document2,
                dataDir + "ComparingEntireDocuments_out.pdf",
                new Aspose.Pdf.Comparison.SideBySideComparisonOptions
                {
                    AdditionalChangeMarks = true,
                    ComparisonMode = Aspose.Pdf.Comparison.ComparisonMode.IgnoreSpaces
                });
        }
    }
}
```

这些代码片段生成的比较结果是 PDF 文档，您可以在 Adobe Acrobat 等查看器中打开。如果您在 Adobe Acrobat 中使用双页视图，您将看到并排显示的更改：

- 删除 - 这些在左侧页面上标记。
- 插入 - 这些在右侧页面上标记。

通过将 'AdditionalChangeMarks' 设置为 'true'，您还可以看到可能发生在其他页面上的更改标记，即使这些更改不在当前查看的页面上。

**Aspose.PDF for .NET** 提供了强大的工具来比较 PDF 文档，无论您需要比较特定页面还是整个文档。通过使用 'AdditionalChangeMarks' 和不同的 'ComparisonMode 设置'，您可以根据特定需求定制比较过程。生成的文档提供了清晰的并排更改视图，使跟踪修订和确保文档准确性变得更加容易。

## 使用 GraphicalPdfComparer 比较 PDF 文档

在协作处理文档时，尤其是在专业环境中，您通常会得到同一文件的多个版本。

您可以使用 [GraphicalPdfComparer](https://reference.aspose.com/pdf/zh/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/) 类来比较 PDF 文档和页面。该类适合比较页面图形内容中的更改。

使用 Aspose.PDF for .NET，可以比较文档和页面，并将比较结果输出到 PDF 文档或图像文件。

您可以设置以下类属性：

- 分辨率 - 输出图像的 DPI 单位分辨率，以及在比较过程中生成的图像。
- 颜色 - 更改标记的颜色。
- 阈值 - 变化阈值（以百分比表示）。默认值为零。设置非零值可以让您忽略对您来说不重要的图形更改。

该类具有一个方法，允许您以适合进一步处理的形式获取页面图像差异：**ImagesDifference GetDifference(Page page1, Page page2)**。

此方法返回一个 [ImagesDifference](https://reference.aspose.com/pdf/zh/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/) 类的对象，该对象包含正在比较的第一页的图像和差异数组。差异数组和原始图像具有 **RGB24bpp** 像素格式。

ImagesDifference 允许您生成不同的图像，并通过将差异数组添加到原始图像来获取正在比较的第二页的图像。为此，请使用 **ImagesDifference.GetDestinationImage 和 ImagesDifference.DifferenceToImage** 方法。

### 使用 GetDifference 方法比较 PDF

提供的代码定义了一个方法 [GetDifference](https://reference.aspose.com/pdf/zh/net/aspose.pdf.comparison.graphicalcomparison/imagesdifference/#methods)，该方法比较两个 PDF 文档并生成它们之间差异的视觉表示。

此方法比较两个 PDF 文件的第一页，并生成两个 PNG 图像：

- 一张图像（diffPngFilePath）以红色突出显示页面之间的差异。
- 另一张图像（destPngFilePath）是目标（第二）PDF 页面的视觉表示。

此过程对于直观比较文档的两个版本之间的更改或差异非常有用。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithGetDifferenceMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithGetDifferenceMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithGetDifferenceMethod2.pdf"))
        {
            // Create comparer 
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer();
            // Compare
            using (var imagesDifference = comparer.GetDifference(document1.Pages[1], document2.Pages[1]))
            {
                using (var diffImg = imagesDifference.DifferenceToImage(Aspose.Pdf.Color.Red, Aspose.Pdf.Color.White))
                {
                    diffImg.Save(dataDir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png");
                }
                using (var destImg = imagesDifference.GetDestinationImage())
                {
                    destImg.Save(dataDir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png");
                }
            }
        }
    }
}
```

### 使用 CompareDocumentsToPdf 方法比较 PDF

提供的代码片段使用了 [CompareDocumentsToPdf](https://reference.aspose.com/pdf/zh/net/aspose.pdf.comparison.graphicalcomparison/graphicalpdfcomparer/comparedocumentstopdf/) 方法，该方法比较两个文档并生成比较结果的 PDF 报告。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ComparePDFWithCompareDocumentsToPdfMethod()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentCompare();

    // Open PDF documents
    using (var document1 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf"))
    {
        using (var document2 = new Aspose.Pdf.Document(dataDir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf"))
        {
            // Create comparer
            var comparer = new Aspose.Pdf.Comparison.GraphicalPdfComparer()
            {
                Threshold = 3.0,
                Color = Aspose.Pdf.Color.Blue,
                Resolution = new Aspose.Pdf.Devices.Resolution(300)
            };
            // Compare
            comparer.CompareDocumentsToPdf(document1, document2, dataDir + "compareDocumentsToPdf_out.pdf");
        }
    }
}
```