---
title: 使用 C# 创建标记 PDF
linktitle: 创建标记 PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/create-tagged-pdf/
description: 本文解释了如何使用 Aspose.PDF for .NET 以编程方式为标记 PDF 文档创建结构元素。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create Tagged PDF using C#",
    "alternativeHeadline": "Programmatically create tagged PDFs using C#",
    "abstract": "使用 C# 和 Aspose.PDF 以编程方式创建标记 PDF 文档，确保符合 PDF/UA 标准。此功能支持创建具有标题和段落等元素的结构化 PDF 文档，支持嵌套结构和可访问性的文本样式。该库还包括验证，以确认符合 PDF/UA 标准。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Tagged PDF, C#, Aspose.PDF, PDF/UA, Structure Elements, ITaggedContent, AppendChild,  StructureTextState",
    "wordcount": "1163",
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
    "url": "/net/create-tagged-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-tagged-pdf/"
    },
    "dateModified": "2022-11-25",
    "description": "本文解释了如何使用 Aspose.PDF for .NET 以编程方式为标记 PDF 文档创建结构元素。"
}
</script>

创建标记 PDF 意味着向文档添加（或创建）某些元素，以使文档能够根据 PDF/UA 要求进行验证。这些元素通常称为结构元素。

以下代码片段还可以与 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库一起使用。

## 创建标记 PDF（简单场景）

为了在标记 PDF 文档中创建结构元素，Aspose.PDF 提供了使用 [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent) 接口创建结构元素的方法。以下代码片段显示了如何创建包含 2 个元素：标题和段落的标记 PDF。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTaggedPdfDocument01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get Content for work with TaggedPdf
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;
        var rootElement = taggedContent.RootElement;

        // Set Title and Language for Document
        taggedContent.SetTitle("Tagged Pdf Document");
        taggedContent.SetLanguage("en-US");

        Aspose.Pdf.LogicalStructure.HeaderElement mainHeader = taggedContent.CreateHeaderElement();
        mainHeader.SetText("Main Header");

        Aspose.Pdf.LogicalStructure.ParagraphElement paragraphElement = taggedContent.CreateParagraphElement();
        paragraphElement.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " +
            "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. " +
            "Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet" +
            "nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus." +
            "Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat" +
            "sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper" +
            "pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus" +
            "ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus," +
            "ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");

        rootElement.AppendChild(mainHeader);
        rootElement.AppendChild(paragraphElement);

        // Save Tagged PDF document
        document.Save(dataDir + "TaggedPdfDocument_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTaggedPdfDocument01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using var document = new Aspose.Pdf.Document();

    // Get Content for work with TaggedPdf
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;
    var rootElement = taggedContent.RootElement;

    // Set Title and Language for Document
    taggedContent.SetTitle("Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    Aspose.Pdf.LogicalStructure.HeaderElement mainHeader = taggedContent.CreateHeaderElement();
    mainHeader.SetText("Main Header");

    Aspose.Pdf.LogicalStructure.ParagraphElement paragraphElement = taggedContent.CreateParagraphElement();
    paragraphElement.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. " +
        "Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. " +
        "Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet" +
        "nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus." +
        "Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat" +
        "sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper" +
        "pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus" +
        "ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus," +
        "ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");

    rootElement.AppendChild(mainHeader);
    rootElement.AppendChild(paragraphElement);

    // Save Tagged PDF Document
    document.Save(dataDir + "TaggedPdfDocument_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

创建后，我们将得到以下文档：

![包含 2 个元素 - 标题和段落的标记 PDF 文档](taggedpdf-01.png)

## 创建带有嵌套元素的标记 PDF（创建结构元素树）

在某些情况下，我们需要创建更复杂的结构，例如在段落中放置引号。为了创建结构元素树，我们应该使用 [AppendChild](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/element/methods/appendchild) 方法。以下代码片段显示了如何创建标记 PDF 文档的结构元素树：

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTaggedPdfDocument02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get Content for work with TaggedPdf
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;
        var rootElement = taggedContent.RootElement;

        // Set Title and Language for Document
        taggedContent.SetTitle("Tagged Pdf Document");
        taggedContent.SetLanguage("en-US");

        Aspose.Pdf.LogicalStructure.HeaderElement header1 = taggedContent.CreateHeaderElement(1);
        header1.SetText("Header Level 1");

        Aspose.Pdf.LogicalStructure.ParagraphElement paragraphWithQuotes = taggedContent.CreateParagraphElement();
        paragraphWithQuotes.StructureTextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Calibri");
        paragraphWithQuotes.StructureTextState.MarginInfo = new Aspose.Pdf.MarginInfo(10, 5, 10, 5);

        Aspose.Pdf.LogicalStructure.SpanElement spanElement1 = taggedContent.CreateSpanElement();
        spanElement1.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");

        Aspose.Pdf.LogicalStructure.QuoteElement quoteElement = taggedContent.CreateQuoteElement();
        quoteElement.SetText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa.");
        quoteElement.StructureTextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold | Aspose.Pdf.Text.FontStyles.Italic;
        Aspose.Pdf.LogicalStructure.SpanElement spanElement2 = taggedContent.CreateSpanElement();
        spanElement2.SetText(" Sed non consectetur elit.");

        paragraphWithQuotes.AppendChild(spanElement1);
        paragraphWithQuotes.AppendChild(quoteElement);
        paragraphWithQuotes.AppendChild(spanElement2);

        rootElement.AppendChild(header1);
        rootElement.AppendChild(paragraphWithQuotes);

        // Save Tagged PDF Document
        document.Save(dataDir + "TaggedPdfDocument_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTaggedPdfDocument02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using var document = new Aspose.Pdf.Document();

    // Get Content for work with TaggedPdf
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;
    var rootElement = taggedContent.RootElement;

    // Set Title and Language for Document
    taggedContent.SetTitle("Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    Aspose.Pdf.LogicalStructure.HeaderElement header1 = taggedContent.CreateHeaderElement(1);
    header1.SetText("Header Level 1");

    Aspose.Pdf.LogicalStructure.ParagraphElement paragraphWithQuotes = taggedContent.CreateParagraphElement();
    paragraphWithQuotes.StructureTextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Calibri");
    paragraphWithQuotes.StructureTextState.MarginInfo = new Aspose.Pdf.MarginInfo(10, 5, 10, 5);

    Aspose.Pdf.LogicalStructure.SpanElement spanElement1 = taggedContent.CreateSpanElement();
    spanElement1.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");

    Aspose.Pdf.LogicalStructure.QuoteElement quoteElement = taggedContent.CreateQuoteElement();
    quoteElement.SetText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa.");
    quoteElement.StructureTextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold | Aspose.Pdf.Text.FontStyles.Italic;
    Aspose.Pdf.LogicalStructure.SpanElement spanElement2 = taggedContent.CreateSpanElement();
    spanElement2.SetText(" Sed non consectetur elit.");

    paragraphWithQuotes.AppendChild(spanElement1);
    paragraphWithQuotes.AppendChild(quoteElement);
    paragraphWithQuotes.AppendChild(spanElement2);

    rootElement.AppendChild(header1);
    rootElement.AppendChild(paragraphWithQuotes);

    // Save Tagged PDF Document
    document.Save(dataDir + "TaggedPdfDocument_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

创建后，我们将得到以下文档：
![带有嵌套元素 - span 和引号的标记 PDF 文档](taggedpdf-02.png)

## 样式文本结构

为了在标记 PDF 文档中样式文本结构，Aspose.PDF 提供了 [Font](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/font)、[FontSize](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/fontsize)、[FontStyle](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/fontstyle) 和 [ForegroundColor](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate/properties/foregroundcolor) 属性的 [StructureTextState](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structuretextstate) 类。以下代码片段显示了如何在标记 PDF 文档中样式文本结构：

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddStyle()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get Content for work with TaggedPdf
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        // Set Title and Language for Document
        taggedContent.SetTitle("Tagged Pdf Document");
        taggedContent.SetLanguage("en-US");

        Aspose.Pdf.LogicalStructure.ParagraphElement p = taggedContent.CreateParagraphElement();
        taggedContent.RootElement.AppendChild(p);

        p.StructureTextState.FontSize = 18F;
        p.StructureTextState.ForegroundColor = Aspose.Pdf.Color.Red;
        p.StructureTextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;

        p.SetText("Red italic text.");

        // Save Tagged Pdf Document
        document.Save(dataDir + "StyleTextStructure_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddStyle()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using var document = new Aspose.Pdf.Document();

    // Get Content for work with TaggedPdf
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

    // Set Title and Language for Document
    taggedContent.SetTitle("Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    Aspose.Pdf.LogicalStructure.ParagraphElement p = taggedContent.CreateParagraphElement();
    taggedContent.RootElement.AppendChild(p);

    p.StructureTextState.FontSize = 18F;
    p.StructureTextState.ForegroundColor = Aspose.Pdf.Color.Red;
    p.StructureTextState.FontStyle = Aspose.Pdf.Text.FontStyles.Italic;

    p.SetText("Red italic text.");

    // Save Tagged Pdf Document
    document.Save(dataDir + "StyleTextStructure_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 说明结构元素

为了在标记 PDF 文档中说明结构元素，Aspose.PDF 提供了 [IllustrationElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/illustrationelement) 类。以下代码片段显示了如何在标记 PDF 文档中说明结构元素：

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IllustrateStructureElements()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using (var document = new Aspose.Pdf.Document())
    {
        // Get Content for work with TaggedPdf
        Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

        // Set Title and Language for Document
        taggedContent.SetTitle("Tagged Pdf Document");
        taggedContent.SetLanguage("en-US");

        Aspose.Pdf.LogicalStructure.IllustrationElement figure1 = taggedContent.CreateFigureElement();
        taggedContent.RootElement.AppendChild(figure1);
        figure1.AlternativeText = "Figure One";
        figure1.Title = "Image 1";
        figure1.SetTag("Fig1");
        figure1.SetImage(dataDir + "image.png");

        // Save Tagged Pdf Document
        document.Save(dataDir + "IllustrationStructureElements_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void IllustrateStructureElements()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF Document
    using var document = new Aspose.Pdf.Document();

    // Get Content for work with TaggedPdf
    Aspose.Pdf.Tagged.ITaggedContent taggedContent = document.TaggedContent;

    // Set Title and Language for Document
    taggedContent.SetTitle("Tagged Pdf Document");
    taggedContent.SetLanguage("en-US");

    Aspose.Pdf.LogicalStructure.IllustrationElement figure1 = taggedContent.CreateFigureElement();
    taggedContent.RootElement.AppendChild(figure1);
    figure1.AlternativeText = "Figure One";
    figure1.Title = "Image 1";
    figure1.SetTag("Fig1");
    figure1.SetImage(dataDir + "image.png");

    // Save Tagged Pdf Document
    document.Save(dataDir + "IllustrationStructureElements_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 验证标记 PDF

Aspose.PDF for .NET 提供了验证 PDF/UA 标记 PDF 文档的能力。PDF/UA 标准的验证支持：

- 检查 XObjects。
- 检查操作。
- 检查可选内容。
- 检查嵌入文件。
- 检查 Acroform 字段（验证自然语言、替代名称和数字签名）。
- 检查 XFA 表单字段。
- 检查安全设置。
- 检查导航。
- 检查注释。

以下代码片段显示了如何验证标记 PDF 文档。相应的问题将显示在 XML 日志报告中。

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidateTaggedPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StructureElements.pdf"))
    {
        bool isValid = document.Validate(dataDir + "StructureElements_log.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidateTaggedPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "StructureElements.pdf");

    bool isValid = document.Validate(dataDir + "StructureElements_log.xml", Aspose.Pdf.PdfFormat.PDF_UA_1);
}
```
{{< /tab >}}
{{< /tabs >}}

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