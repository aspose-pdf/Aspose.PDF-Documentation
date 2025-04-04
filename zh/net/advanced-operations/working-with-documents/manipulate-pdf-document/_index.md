---
title: 在 C# 中操作 PDF 文档
linktitle: 操作 PDF 文档
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /zh/net/manipulate-pdf-document/
description: 本文包含有关如何验证 PDF 文档是否符合 PDF A 标准、如何处理目录、如何设置 PDF 到期日期等信息。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipulate PDF Document in C#",
    "alternativeHeadline": "Enhanced PDF Manipulation Features in C# Library",
    "abstract": "发现使用 C# 操作 PDF 文档的强大功能，包括对 PDF/A 标准的验证、创建和自定义目录的能力，以及设置文档到期日期。此功能不仅增强了文档管理，还确保符合行业标准，使其成为寻求强大 PDF 处理解决方案的开发人员的必备工具。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "manipulate PDF, C#, validate PDF/A, TOC, set PDF expiry date, flatten fillable PDF, Aspose.PDF, PDF generation progress, customize page numbers, PDF encryption",
    "wordcount": "2170",
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
    "url": "/net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "本文包含有关如何验证 PDF 文档是否符合 PDF A 标准、如何处理目录、如何设置 PDF 到期日期等信息。"
}
</script>

## **在 C# 中操作 PDF 文档**

## 验证 PDF 文档是否符合 PDF A 标准 (A 1A 和 A 1B)

要验证 PDF 文档是否符合 PDF/A-1a 或 PDF/A-1b 兼容性，请使用 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document) 类的 Validate 方法。此方法允许您指定结果要保存的文件名和所需的验证类型 [PdfFormat](https://reference.aspose.com/pdf/zh/net/aspose.pdf/pdfformat) 枚举：PDF_A_1A 或 PDF_A_1B。

{{% alert color="primary" %}}

输出 XML 格式是自定义的 Aspose 格式。XML 包含一组名为 Problem 的标签；每个标签包含特定问题的详细信息。Problem 标签的 ObjectID 属性表示与此问题相关的特定对象的 ID。Clause 属性表示 PDF 规范中的相应规则。

{{% /alert %}}

以下代码片段还可以与 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库一起使用。

以下代码片段演示了如何验证 PDF 文档是否符合 PDF/A-1A。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidateToPdfA1aStandard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ValidatePDFAStandard.pdf"))
    {
        // Validate PDF for PDF/A-1a
        document.Validate(dataDir + "validation-result-A1A.xml", Aspose.Pdf.PdfFormat.PDF_A_1A);
    }
}
```

以下代码片段演示了如何验证 PDF 文档是否符合 PDF/A-1b。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ValidateToPdfA1bStandard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ValidatePDFAStandard.pdf"))
    {
        // Validate PDF for PDF/A-1b
        document.Validate(dataDir + "validation-result-A1B.xml", Aspose.Pdf.PdfFormat.PDF_A_1B);
    }
}
```

{{% alert color="primary" %}}

Aspose.PDF for .NET 可用于确定加载的文档是否为有效 PDF，以及 [它是否被加密](https://docs.aspose.com/pdf/net/set-privileges-encrypt-and-decrypt-pdf-file/)。为了进一步扩展 Document 类的功能，添加了 *IsPdfaCompliant* 属性以确定输入文件是否符合 PDF/A 标准，并引入了名为 *PdfaFormat* 的属性以识别 PDF/A 格式。

{{% /alert %}}

## 处理目录

### 向现有 PDF 添加目录

Aspose.PDF API 允许您在创建 PDF 时或向现有文件添加目录。Aspose.Pdf.Generator 命名空间中的 ListSection 类允许您在从头创建 PDF 时创建目录。要添加目录的元素（即标题），请使用 Aspose.Pdf.Generator.Heading 类。

要向现有 PDF 文件添加目录，请使用 Aspose.PDF 命名空间中的 Heading 类。Aspose.Pdf 命名空间可以创建新 PDF 也可以操作现有 PDF 文件。以下代码片段演示了如何在现有 PDF 文件中创建目录。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTOCToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddTOC.pdf"))
    {
        // Get access to the first page of PDF file
        var tocPage = document.Pages.Insert(1);

        // Create an object to represent TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 20;
        title.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Set the title for TOC
        tocInfo.Title = title;
        tocPage.TocInfo = tocInfo;

        // Create string objects which will be used as TOC elements
        string[] titles = { "First page", "Second page", "Third page", "Fourth page" };

        for (int i = 0; i < 2; i++)
        {
            // Create Heading object
            var heading = new Aspose.Pdf.Heading(1);
            var segment = new Aspose.Pdf.Text.TextSegment();
            heading.TocPage = tocPage;
            heading.Segments.Add(segment);

            // Specify the destination page for the heading object
            heading.DestinationPage = document.Pages[i + 2];

            // Destination page
            heading.Top = document.Pages[i + 2].Rect.Height;

            // Destination coordinate
            segment.Text = titles[i];

            // Add heading to the page containing TOC
            tocPage.Paragraphs.Add(heading);
        }

        // Save PDF document
        document.Save(dataDir + "TOC_out.pdf");
    }
}
```

### 为不同的目录级别设置不同的 TabLeaderType

Aspose.PDF 还允许为不同的目录级别设置不同的 TabLeaderType。您需要将 FormatArray 的 LineDash 属性设置为 TabLeaderType 枚举的适当值，如下所示。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTocWithCustomFormatting()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a TOC page
        var tocPage = document.Pages.Add();

        // Create TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();

        // Set LeaderType
        tocInfo.LineDash = Aspose.Pdf.Text.TabLeaderType.Solid;

        // Set the title for TOC
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 30;
        tocInfo.Title = title;

        // Add the TOC section to the document
        tocPage.TocInfo = tocInfo;

        // Define the format of the four levels list by setting the left margins
        // and text format settings of each level
        tocInfo.FormatArrayLength = 4;

        // Level 1
        tocInfo.FormatArray[0].Margin.Left = 0;
        tocInfo.FormatArray[0].Margin.Right = 30;
        tocInfo.FormatArray[0].LineDash = Aspose.Pdf.Text.TabLeaderType.Dot;
        tocInfo.FormatArray[0].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold | Aspose.Pdf.Text.FontStyles.Italic;

        // Level 2
        tocInfo.FormatArray[1].Margin.Left = 10;
        tocInfo.FormatArray[1].Margin.Right = 30;
        tocInfo.FormatArray[1].LineDash = Aspose.Pdf.Text.TabLeaderType.None;
        tocInfo.FormatArray[1].TextState.FontSize = 10;

        // Level 3
        tocInfo.FormatArray[2].Margin.Left = 20;
        tocInfo.FormatArray[2].Margin.Right = 30;
        tocInfo.FormatArray[2].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Level 4
        tocInfo.FormatArray[3].LineDash = Aspose.Pdf.Text.TabLeaderType.Solid;
        tocInfo.FormatArray[3].Margin.Left = 30;
        tocInfo.FormatArray[3].Margin.Right = 30;
        tocInfo.FormatArray[3].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Create a section in the Pdf document
        var page = document.Pages.Add();

        // Add four headings in the section
        for (int level = 1; level <= 4; level++)
        {
            var heading = new Aspose.Pdf.Heading(level);
            var segment = new Aspose.Pdf.Text.TextSegment();
            heading.Segments.Add(segment);
            heading.IsAutoSequence = true;
            heading.TocPage = tocPage;
            segment.Text = "Sample Heading " + level;
            heading.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial Unicode MS");

            // Add the heading into Table Of Contents.
            heading.IsInList = true;
            page.Paragraphs.Add(heading);
        }

        // Save PDF document
        document.Save(dataDir + "TOC_out.pdf");
    }
}
```

### 在目录中隐藏页码

如果您不想在目录中显示页码，可以将 [TOCInfo](https://reference.aspose.com/pdf/zh/net/aspose.pdf/tocinfo) 类的 [IsShowPageNumbers](https://reference.aspose.com/pdf/zh/net/aspose.pdf/tocinfo/properties/isshowpagenumbers) 属性设置为 false。请查看以下代码片段以在目录中隐藏页码：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateTocWithHiddenPageNumbers()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add a TOC page
        var tocPage = document.Pages.Add();

        // Create TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();

        // Set the title for TOC
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 20;
        title.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;
        tocInfo.Title = title;

        // Add the TOC section to the document
        tocPage.TocInfo = tocInfo;

        // Hide page numbers in TOC
        tocInfo.IsShowPageNumbers = false;

        // Define the format of the four levels list by setting the left margins and
        // text format settings of each level
        tocInfo.FormatArrayLength = 4;

        // Level 1
        tocInfo.FormatArray[0].Margin.Right = 0;
        tocInfo.FormatArray[0].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold | Aspose.Pdf.Text.FontStyles.Italic;

        // Level 2
        tocInfo.FormatArray[1].Margin.Left = 30;
        tocInfo.FormatArray[1].TextState.Underline = true;
        tocInfo.FormatArray[1].TextState.FontSize = 10;

        // Level 3
        tocInfo.FormatArray[2].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Level 4
        tocInfo.FormatArray[3].TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Create a section in the Pdf document
        var page = document.Pages.Add();

        // Add four headings in the section
        for (int level = 1; level <= 4; level++)
        {
            var heading = new Aspose.Pdf.Heading(level);
            var segment = new Aspose.Pdf.Text.TextSegment();
            heading.TocPage = tocPage;
            heading.Segments.Add(segment);
            heading.IsAutoSequence = true;
            segment.Text = "this is heading of level " + level;
            heading.IsInList = true;
            page.Paragraphs.Add(heading);
        }

        // Save PDF document
        document.Save(dataDir + "TOC_out.pdf");
    }
}
```

### 在添加目录时自定义页码

在向 PDF 文档添加目录时，自定义目录中的页码是很常见的。例如，我们可能需要在页码前添加一些前缀，如 P1、P2、P3 等。在这种情况下，Aspose.PDF for .NET 提供了 TocInfo 类的 PageNumbersPrefix 属性，可以用来自定义页码，如以下代码示例所示。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomizePageNumbersAddingToC()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CustomizePageNumbersAddingToC.pdf"))
    {
        // Get access to first page of PDF file
        Page tocPage = document.Pages.Insert(1);

        // Create object to represent TOC information
        var tocInfo = new Aspose.Pdf.TocInfo();
        var title = new Aspose.Pdf.Text.TextFragment("Table Of Contents");
        title.TextState.FontSize = 20;
        title.TextState.FontStyle = Aspose.Pdf.Text.FontStyles.Bold;

        // Set the title for TOC
        tocInfo.Title = title;
        tocInfo.PageNumbersPrefix = "P";
        tocPage.TocInfo = tocInfo;

        // Loop through the pages to create TOC entries
        for (int i = 1; i < document.Pages.Count; i++)
        {
            // Create Heading object
            var heading2 = new Aspose.Pdf.Heading(1);
            var segment2 = new Aspose.Pdf.Text.TextSegment();
            heading2.TocPage = tocPage;
            heading2.Segments.Add(segment2);

            // Specify the destination page for heading object
            heading2.DestinationPage = document.Pages[i + 1];

            // Destination page
            heading2.Top = document.Pages[i + 1].Rect.Height;

            // Destination coordinate
            segment2.Text = "Page " + i.ToString();

            // Add heading to page containing TOC
            tocPage.Paragraphs.Add(heading2);
        }

        // Save PDF document
        document.Save(dataDir + "CustomizePageNumbersAddingToC_out.pdf");
    }
}
```

## 如何设置 PDF 到期日期

我们对 PDF 文件应用访问权限，以便某一特定用户组可以访问 PDF 文档的特定功能/对象。为了限制 PDF 文件的访问，我们通常会应用加密，并且可能需要设置 PDF 文件的到期日期，以便访问/查看文档的用户能够获得有关 PDF 文件到期的有效提示。

为了实现上述要求，我们可以使用 *JavascriptAction* 对象。请查看以下代码片段。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Add text fragment to paragraphs collection of page object
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World..."));

        // Create JavaScript object to set PDF expiry date
        var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(
            "var year=2017;" +
            "var month=5;" +
            "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" +
            "expiry = new Date(year, month);" +
            "if (today.getTime() > expiry.getTime())" +
            "app.alert('The file is expired. You need a new one.');"
        );

        // Set JavaScript as PDF open action
        document.OpenAction = javaScript;

        // Save PDF Document
        document.Save(dataDir + "SetExpiryDate_out.pdf");
    }
}
```

## 确定 PDF 文件生成进度

客户要求我们添加一个功能，允许开发人员确定 PDF 文件生成的进度。以下是对此请求的响应。

[DocSaveOptions](https://reference.aspose.com/pdf/zh/net/aspose.pdf/docsaveoptions) 类的 [CustomerProgressHandler](https://reference.aspose.com/pdf/zh/net/aspose.pdf/docsaveoptions/fields/customprogresshandler) 字段允许您确定 PDF 生成的进度。处理程序具有以下类型：

- DocSaveOptions.ConversionProgessEventHandler。
- DocSaveOptions.ProgressEventHandlerInfo。
- DocSaveOptions.ProgressEventType。

以下代码片段演示了如何使用 CustomerProgressHandler。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DetermineProgress()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddTOC.pdf"))
    {
        // Create DocSaveOptions instance and set custom progress handler
        var saveOptions = new Aspose.Pdf.DocSaveOptions();
        saveOptions.CustomProgressHandler = new Aspose.Pdf.UnifiedSaveOptions.ConversionProgressEventHandler(ShowProgressOnConsole);

        // Save PDF Document
        document.Save(dataDir + "DetermineProgress_out.pdf", saveOptions);
    }
}

// Method to handle progress and display it on the console
private static void ShowProgressOnConsole(Aspose.Pdf.UnifiedSaveOptions.ProgressEventHandlerInfo eventInfo)
{
    switch (eventInfo.EventType)
    {
        case Aspose.Pdf.ProgressEventType.TotalProgress:
            Console.WriteLine(String.Format("{0}  - Conversion progress : {1}% .", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString()));
            break;
        case Aspose.Pdf.ProgressEventType.SourcePageAnalysed:
            Console.WriteLine(String.Format("{0}  - Source page {1} of {2} analyzed.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case Aspose.Pdf.ProgressEventType.ResultPageCreated:
            Console.WriteLine(String.Format("{0}  - Result page's {1} of {2} layout created.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        case Aspose.Pdf.ProgressEventType.ResultPageSaved:
            Console.WriteLine(String.Format("{0}  - Result page {1} of {2} exported.", DateTime.Now.ToLongTimeString(), eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
            break;
        default:
            break;
    }
}
```

## 扁平化可填写 PDF

PDF 文档通常包含带有交互式可填写小部件（如单选按钮、复选框、文本框、列表等）的表单。为了使其在各种应用程序中不可编辑，我们需要扁平化 PDF 文件。
Aspose.PDF 提供了在 C# 中扁平化 PDF 的功能，只需几行代码：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Flatten Fillable PDF
        if (document.Form.Fields.Count() > 0)
        {
            foreach (var item in document.Form.Fields)
            {
                item.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "FlattenForms_out.pdf");
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