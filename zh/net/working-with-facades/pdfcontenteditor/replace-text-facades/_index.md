---
title: 替换文本 - 外观
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /zh/net/replace-text-facades/
description: 本节解释如何使用 PdfContentEditor 类处理文本 - 外观。
lastmod: "2021-06-24"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Replace Text - Facades",
    "alternativeHeadline": "Effortless Text Replacement in PDF Files",
    "abstract": "PdfContentEditor 类中的替换文本功能允许用户高效地修改现有 PDF 文档中的文本内容。通过使用 BindPdf 和 ReplaceText 等简单方法，用户可以无缝更新文本、调整字体大小，并自定义文本格式，包括粗体和颜色，同时保持原始文档的完整性。此功能增强了 PDF 编辑能力，使动态管理内容变得更加容易。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "550",
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
    "url": "/net/replace-text-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/replace-text-facades/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 在现有 PDF 文件中替换文本

为了在现有 PDF 文件中替换文本，您需要创建一个 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 类的对象，并使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) 方法绑定输入 PDF 文件。之后，您需要调用 [ReplaceText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replacetext/index) 方法。您需要使用 [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) 类的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存更新后的 PDF 文件。以下代码片段向您展示如何在现有 PDF 文件中替换文本。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");
        editor.ReplaceText("Value", "Label");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo01_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor Object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");
    editor.ReplaceText("Value", "Label");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo01_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

查看原始文档中的样子：

![替换文本](replace_text1.png)

并查看替换文本后的结果：

![替换文本结果](replace_text2.png)

在第二个示例中，您将看到除了替换文本外，您还可以增加或减少字体大小：

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");
        editor.ReplaceText("Value", "Label", 12);

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo02_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");
    editor.ReplaceText("Value", "Label", 12);

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo02_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

对于更高级的文本处理功能，我们将使用 [TextState](https://reference.aspose.com/pdf/net/aspose.pdf.text/textstate) 方法。通过此方法，我们可以使文本变为粗体、斜体、彩色等。

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");

        var textState = new Aspose.Pdf.Text.TextState
        {
            ForegroundColor = Aspose.Pdf.Color.Red,
            FontSize = 12,
        };

        editor.ReplaceText("Value", "Label", textState);

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo03_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");

    var textState = new Aspose.Pdf.Text.TextState
    {
        ForegroundColor = Aspose.Pdf.Color.Red,
        FontSize = 12,
    };

    editor.ReplaceText("Value", "Label", textState);

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo03_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

如果您需要替换文档中所有指定的文本，请使用以下代码片段。也就是说，文本的替换将在遇到指定替换的文本时发生，并且还会计算此类替换的数量。

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText04()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");
        int count = 0;

        while (editor.ReplaceText("Value", "Label"))
        {
            count++;
        }

        Console.WriteLine($"{count} occurrences have been replaced.");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo04_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText04()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");
    int count = 0;

    while (editor.ReplaceText("Value", "Label"))
    {
        count++;
    }

    Console.WriteLine($"{count} occurrences have been replaced.");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo04_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

![替换所有文本](replace_text3.png)

以下代码片段展示了如何在文档的特定页面上进行所有文本替换。

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText05()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");
        int count = 0;

        while (editor.ReplaceText("9999", 2, "ABCDE"))
        {
            count++;
        }

        Console.WriteLine($"{count} occurrences have been replaced.");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo05_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText05()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");
    int count = 0;

    while (editor.ReplaceText("9999", 2, "ABCDE"))
    {
        count++;
    }

    Console.WriteLine($"{count} occurrences have been replaced.");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo05_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

在下一个代码片段中，我们将展示如何将给定的数字替换为我们需要的字母。

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText06()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using (var editor = new Aspose.Pdf.Facades.PdfContentEditor
           {
               ReplaceTextStrategy = new Aspose.Pdf.Facades.ReplaceTextStrategy
               {
                   IsRegularExpressionUsed = true,
                   ReplaceScope = Aspose.Pdf.Facades.ReplaceTextStrategy.Scope.ReplaceAll
               }
           })
    {
        // Bind PDF document
        editor.BindPdf(dataDir + "sample.pdf");
        editor.ReplaceText("\\d{4}", "ABCDE");

        // Save PDF document
        editor.Save(dataDir + "PdfContentEditorDemo06_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ReplaceText06()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Instantiate PdfContentEditor object
    using var editor = new Aspose.Pdf.Facades.PdfContentEditor
    {
        ReplaceTextStrategy = new Aspose.Pdf.Facades.ReplaceTextStrategy
        {
            IsRegularExpressionUsed = true,
            ReplaceScope = Aspose.Pdf.Facades.ReplaceTextStrategy.Scope.ReplaceAll
        }
    };

    // Bind PDF document
    editor.BindPdf(dataDir + "sample.pdf");
    editor.ReplaceText("\\d{4}", "ABCDE");

    // Save PDF document
    editor.Save(dataDir + "PdfContentEditorDemo06_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}