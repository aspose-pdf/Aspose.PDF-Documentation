---
title: 从 PDF 中提取文本 C#
linktitle: 从 PDF 中提取文本
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/extract-text-from-all-pdf/
description: 本文描述了使用 Aspose.PDF 在 C# 中从 PDF 文档提取文本的各种方法。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Text from PDF C#",
    "alternativeHeadline": "Effortlessly Extract Text from PDFs in C#",
    "abstract": "发现 Aspose.PDF for .NET 中强大的新功能，使开发人员能够轻松从 PDF 文档中提取文本。此功能支持从所有页面或特定区域提取，适应多列布局，甚至只需几行代码即可检索高亮文本。通过这个多功能工具增强您的文档处理能力并简化内容提取。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "2005",
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
    "url": "/net/extract-text-from-all-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-text-from-all-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单易行的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 从 PDF 文档的所有页面提取文本

从 PDF 文档中提取文本是一个常见的需求。在这个例子中，您将看到 Aspose.PDF for .NET 如何允许从 PDF 文档的所有页面提取文本。您需要创建一个 **TextAbsorber** 类的对象。之后，使用 **Document** 类打开 PDF 并调用 **Pages** 集合的 **Accept** 方法。**TextAbsorber** 类从文档中吸收文本并在 **Text** 属性中返回。以下代码片段向您展示了如何从 PDF 文档的所有页面提取文本。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextAbsorber object to extract text
        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();

        // Accept the absorber for all the pages
        document.Pages.Accept(textAbsorber);

        // Get the extracted text
        string extractedText = textAbsorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

在 Document 对象的特定页面上调用 **Accept** 方法。索引是需要提取文本的特定页面编号。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        // Create TextAbsorber object to extract text
        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();

        // Accept the absorber for a particular page
        document.Pages[1].Accept(textAbsorber);

        // Get the extracted text
        string extractedText = textAbsorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text_out.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

## 使用文本设备从页面提取文本

您可以使用 **TextDevice** 类从 PDF 文件中提取文本。TextDevice 在其实现中使用 TextAbsorber，因此，它们实际上做的是同样的事情，但 TextDevice 只是实现了统一的“设备”方法来从页面提取任何内容，如 ImageDevice、PageDevice 等。TextAbsorber 可以从页面、整个 PDF 或 XForm 中提取文本，这个 TextAbsorber 更加通用。

### 从所有页面提取文本

以下步骤和代码片段向您展示了如何使用文本设备从 PDF 中提取文本。

1. 创建一个指定输入 PDF 文件的 Document 类对象。
1. 创建一个 TextDevice 类的对象。
1. 使用 TextExtractOptions 类的对象来指定提取选项。
1. 使用 TextDevice 类的 Process 方法将内容转换为文本。
1. 将文本保存到输出文件。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromPagesWithTextDevice()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    var builder = new System.Text.StringBuilder();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {
        // String to hold extracted text
        string extractedText = "";

        foreach (var page in document.Pages)
        {
            using (MemoryStream textStream = new MemoryStream())
            {
                // Create text device
                var textDevice = new Aspose.Pdf.Devices.TextDevice();

                // Set text extraction options - set text extraction mode (Raw or Pure)
                var textExtOptions = new Aspose.Pdf.Text.TextExtractionOptions(Aspose.Pdf.Text.TextExtractionOptions.TextFormattingMode.Pure);
                textDevice.ExtractionOptions = textExtOptions;

                // Convert a particular page and save text to the stream
                textDevice.Process(page, textStream);
                // Convert a particular page and save text to the stream
                textDevice.Process(document.Pages[1], textStream);

                // Get text from memory stream
                extractedText = System.Text.Encoding.Unicode.GetString(textStream.ToArray());
            }
            builder.Append(extractedText);
        }
    }

    // Save the extracted text in text file
    File.WriteAllText(dataDir + "input_Text_Extracted_out.txt", builder.ToString());
}
```

## 从特定页面区域提取文本

**TextAbsorber** 类提供了从 PDF 文档的特定页面或所有页面提取文本的能力。该类在 **Text** 属性中返回提取的文本。然而，如果我们需要从特定页面区域提取文本，可以使用 **TextSearchOptions** 的 **Rectangle** 属性。Rectangle 属性接受一个 Rectangle 对象作为值，使用此属性，我们可以指定需要提取文本的页面区域。

调用页面的 **Accept** 方法以提取文本。创建 **Document** 和 **TextAbsorber** 类的对象。在 **Document** 对象的单个页面上调用 **Accept** 方法，作为 **Page** 索引。**Index** 是需要提取文本的特定页面编号。您可以从 **TextAbsorber** 类的 **Text** 属性中获取文本。以下代码片段向您展示了如何从单个页面提取文本。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextFromParticularPageRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextAll.pdf"))
    {
        // Create TextAbsorber object to extract text
        var absorber = new Aspose.Pdf.Text.TextAbsorber();
        absorber.TextSearchOptions.LimitToPageBounds = true;
        absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

        // Accept the absorber for first page
        document.Pages[1].Accept(absorber);

        // Get the extracted text
        string extractedText = absorber.Text;

        // Create a writer and open the file
        using (TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt"))
        {
            // Write a line of text to the file
            tw.WriteLine(extractedText);
        }
    }
}
```

## 基于列提取文本

PDF 文件可能包含文本、图像、注释、附件、图表等元素，而 Aspose.PDF for .NET 提供了添加和操作所有这些元素的功能。该 API 在 PDF 文档中添加和提取文本时表现出色，我们可能会遇到一个场景，其中 PDF 文档包含多个列（多列）PDF 文档，我们需要在保持相同布局的情况下提取页面内容，那么 Aspose.PDF for .NET 是实现此需求的正确选择。一种方法是减少 PDF 文档中内容的字体大小，然后执行文本提取。以下代码片段展示了减少文本大小的步骤，然后尝试从 PDF 文档中提取文本。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractTextBasedOnColumns()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    var extractedText = string.Empty;
    // Open PDF document
    using (var sourceDocument = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
        sourceDocument.Pages.Accept(textFragmentAbsorber);
        Aspose.Pdf.Text.TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
        foreach (Aspose.Pdf.Text.TextFragment textFragment in textFragmentCollection)
        {
            // Need to reduce font size at least for 70%
            textFragment.TextState.FontSize = textFragment.TextState.FontSize * 0.7f;
        }
        using (Stream sourceStream = new MemoryStream())
        {
            sourceDocument.Save(sourceStream);
            using (var destDocument = new Aspose.Pdf.Document(sourceStream))
            {
                var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();
                destDocument.Pages.Accept(textAbsorber);
                extractedText = textAbsorber.Text;
                textAbsorber.Visit(destDocument);
            }
        }

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "ExtractColumnsText_out.txt", extractedText);
    }
}
```

### 第二种方法 - 使用 ScaleFactor

在这个新版本中，我们还对 TextAbsorber 和内部文本格式化机制进行了多项改进。因此，现在在使用“纯”模式进行文本提取时，您可以指定 ScaleFactor 选项，这可以作为从多列 PDF 文档中提取文本的另一种方法，除了上述方法。此缩放因子可以设置为调整在文本提取过程中用于内部文本格式化机制的网格。指定 ScaleFactor 值在 1 和 0.1 之间（包括 0.1）具有与字体缩小相同的效果。

指定 ScaleFactor 值在 0.1 和 -0.1 之间被视为零值，但它使算法在提取文本时自动计算所需的缩放因子。计算基于页面上最流行字体的平均字形宽度，但我们不能保证提取的文本中没有列字符串到达下一个列的开始。请注意，如果未指定 ScaleFactor 值，将使用默认值 1.0。这意味着不会进行缩放。如果指定的 ScaleFactor 值大于 10 或小于 -0.1，将使用默认值 1.0。

我们建议在处理大量 PDF 文件以提取文本内容时使用自动缩放（ScaleFactor = 0）。或者手动设置冗余的网格宽度缩小（约 ScaleFactor = 0.5）。但是，您必须确定是否需要对具体文档进行缩放。如果您为不需要缩放的文档设置冗余的网格宽度缩小，提取的文本内容将保持完全适当。请查看以下代码片段。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExctractTextWithScaleFactor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractTextPage.pdf"))
    {

        var textAbsorber = new Aspose.Pdf.Text.TextAbsorber();
        textAbsorber.ExtractionOptions = new Aspose.Pdf.Text.TextExtractionOptions(Aspose.Pdf.Text.TextExtractionOptions.TextFormattingMode.Pure);
        // Setting scale factor to 0.5 is enough to split columns in the majority of documents
        // Setting of zero allows to algorithm choose scale factor automatically
        textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
        document.Pages.Accept(textAbsorber);
        var extractedText = textAbsorber.Text;

        // Save the extracted text in text file
        File.WriteAllText(dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
    }
}
```

{{% alert color="primary" %}}

请注意，新 ScaleFactor 与旧的手动字体缩小系数之间没有直接对应关系。然而，默认算法考虑了由于某些内部原因而已经减少的字体大小的值。例如，将字体大小从 10 减少到 7 的效果与设置缩放因子为 5/8 (= 0.625) 相同。

{{% /alert %}}

## 从 PDF 文档中提取高亮文本

在从 PDF 文档提取文本的各种场景中，您可能会遇到仅提取 PDF 文档中高亮文本的需求。为了实现此功能，我们在 API 中添加了 TextMarkupAnnotation.GetMarkedText() 和 TextMarkupAnnotation.GetMarkedTextFragments() 方法。您可以通过过滤 TextMarkupAnnotation 并使用上述方法从 PDF 文档中提取高亮文本。以下代码片段展示了如何从 PDF 文档中提取高亮文本。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractHighlightedTextFromDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractHighlightedText.pdf"))
    {
        // Loop through all the annotations
        foreach (Aspose.Pdf.Annotations.Annotation annotation in document.Pages[1].Annotations)
        {
            // Filter TextMarkupAnnotation
            if (annotation is Aspose.Pdf.Annotations.TextMarkupAnnotation)
            {
                var highlightedAnnotation = annotation as Aspose.Pdf.Annotations.TextMarkupAnnotation;
                // Retrieve highlighted text fragments
                Aspose.Pdf.Text.TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
                foreach (Aspose.Pdf.Text.TextFragment textFragment in collection)
                {
                    // Display highlighted text
                    Console.WriteLine(textFragment.Text);
                }
            }
        }
    }
}
```

## 从 XML 访问文本片段和段落元素

有时在处理从 XML 生成的 PDF 文档时，我们需要访问 TextFragment 或 TextSegment 项。Aspose.PDF for .NET 通过名称提供对这些项的访问。下面的代码片段展示了如何使用此功能。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessTextFragmentAndSegmentElementsFromXML()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.BindXml(dataDir + "40014.xml");

        // Get page
        var page = (Aspose.Pdf.Page)document.GetObjectById("mainSection");

        // Get elements by Id
        var segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("boldHtml");
        segment = (Aspose.Pdf.Text.TextSegment)document.GetObjectById("strongHtml");

        // Save PDF document
        document.Save(dataDir + "DocumentFromXML_out.pdf");
    }
}
```