---
title: 在 PDF 中使用操作
linktitle: 操作
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/actions/
description: 本节解释如何使用 C# 程序化地向文档和表单字段添加操作。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Actions in PDF",
    "alternativeHeadline": "Programmatic Actions in PDF with C#",
    "abstract": "Aspose.PDF for .NET 中的新功能允许开发人员以编程方式向 PDF 添加操作，从而增强文档的交互性。用户可以实现超链接以在文档内或外部 URL 之间导航，以及操作文档打开操作以控制 PDF 打开时的显示方式。这一强大的功能简化了 C# 应用程序的文档创建和交互。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "C#, PDF actions, hyperlink creation, LinkAnnotation, LocalHyperlink, FreeTextAnnotation, document open action, XYZExplicitDestination, Aspose.PDF, PDF manipulation",
    "wordcount": "2007",
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
    "url": "/net/actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/actions/"
    },
    "dateModified": "2024-11-25",
    "description": "本节解释如何使用 C# 程序化地向文档和表单字段添加操作。"
}
</script>

以下代码片段还可以与 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库一起使用。

## 在 PDF 文件中添加超链接

可以向 PDF 文件添加超链接，以便允许读者导航到 PDF 的另一部分或外部内容。

为了向 PDF 文档添加网页超链接：

1. 创建一个 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 类对象。
1. 获取要添加链接的 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 类。
1. 使用 Page 和 [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) 对象创建一个 [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 对象。矩形对象用于指定链接应添加到页面上的位置。
1. 将 Action 属性设置为指定远程 URI 位置的 [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) 对象。
1. 要显示超链接文本，请在与 [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 对象放置位置相似的位置添加文本字符串。
1. 要添加自由文本：

- 实例化一个 [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) 对象。它也接受 Page 和 Rectangle 对象作为参数，因此可以提供与 LinkAnnotation 构造函数中指定的相同值。
- 使用 [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) 对象的 Contents 属性，指定应在输出 PDF 中显示的字符串。
- 可选地，将 [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 和 FreeTextAnnotation 对象的边框宽度设置为 0，以便它们不出现在 PDF 文档中。
- 一旦定义了 [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 和 [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) 对象，将这些链接添加到 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 对象的 Annotations 集合中。
- 最后，使用 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 对象的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存更新后的 PDF。

以下代码片段演示了如何向 PDF 文件添加超链接。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddHyperlink.pdf"))
    {
        // Get page
        var page = document.Pages[1];
        // Create Link annotation object
        var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
        // Create border object for LinkAnnotation
        var border = new Aspose.Pdf.Annotations.Border(link);
        // Set the border width value as 0
        border.Width = 0;
        // Set the border for LinkAnnotation
        link.Border = border;
        // Specify the link type as remote URI
        link.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");
        // Add link annotation to annotations collection of first page of PDF file
        page.Annotations.Add(link);

        // Create Free Text annotation
        var textAnnotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new Aspose.Pdf.Annotations.DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
        // String to be added as Free text
        textAnnotation.Contents = "Link to Aspose website";
        // Set the border for Free Text Annotation
        textAnnotation.Border = border;
        // Add FreeText annotation to annotations collection of first page of Document
        document.Pages[1].Annotations.Add(textAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddHyperlink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "AddHyperlink.pdf");
    // Get page
    var page = document.Pages[1];
    // Create Link annotation object
    var link = new Aspose.Pdf.Annotations.LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
    // Create border object for LinkAnnotation
    var border = new Aspose.Pdf.Annotations.Border(link);
    // Set the border width value as 0
    border.Width = 0;
    // Set the border for LinkAnnotation
    link.Border = border;
    // Specify the link type as remote URI
    link.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");
    // Add link annotation to annotations collection of first page of PDF file
    page.Annotations.Add(link);

    // Create Free Text annotation
    var textAnnotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new Aspose.Pdf.Annotations.DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
    // String to be added as Free text
    textAnnotation.Contents = "Link to Aspose website";
    // Set the border for Free Text Annotation
    textAnnotation.Border = border;
    // Add FreeText annotation to annotations collection of first page of Document
    document.Pages[1].Annotations.Add(textAnnotation);

    // Save PDF document
    document.Save(dataDir + "AddHyperlink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 创建指向同一 PDF 中页面的超链接

Aspose.PDF for .NET 为 PDF 创建和操作提供了一个很好的功能。它还提供了向 PDF 页面添加链接的功能，链接可以指向另一个 PDF 文件中的页面、网页 URL、启动应用程序的链接，甚至指向同一 PDF 文件中的页面。为了添加本地超链接（指向同一 PDF 文件中的页面），在 Aspose.PDF 命名空间中添加了一个名为 [LocalHyperlink](https://reference.aspose.com/pdf/net/aspose.pdf/localhyperlink) 的类，该类具有一个名为 TargetPageNumber 的属性，用于指定超链接的目标/目的页面。

为了添加本地超链接，我们需要创建一个 TextFragment，以便链接可以与 TextFragment 关联。[TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) 类具有一个名为 Hyperlink 的属性，用于关联 LocalHyperlink 实例。以下代码片段展示了实现此要求的步骤。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create Text Fragment instance
        var text = new Aspose.Pdf.Text.TextFragment("link page number test to page 7");
        // Create local hyperlink instance
        var link = new Aspose.Pdf.LocalHyperlink();
        // Set target page for link instance
        link.TargetPageNumber = 7;
        // Set TextFragment hyperlink
        text.Hyperlink = link;
        // Add text to paragraphs collection of Page
        page.Paragraphs.Add(text);
        // Create new TextFragment instance
        text = new Aspose.Pdf.Text.TextFragment("link page number test to page 1");
        // TextFragment should be added over new page
        text.IsInNewPage = true;
        // Create another local hyperlink instance
        link = new Aspose.Pdf.LocalHyperlink();
        // Set Target page for second hyperlink
        link.TargetPageNumber = 1;
        // Set link for second TextFragment
        text.Hyperlink = link;
        // Add text to paragraphs collection of page object
        page.Paragraphs.Add(text);

        // Save PDF document
        document.Save(dataDir + "CreateLocalHyperlink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    // Add page
    var page = document.Pages.Add();
    // Create Text Fragment instance
    var text = new Aspose.Pdf.Text.TextFragment("link page number test to page 7");
    // Create local hyperlink instance
    var link = new Aspose.Pdf.LocalHyperlink();
    // Set target page for link instance
    link.TargetPageNumber = 7;
    // Set TextFragment hyperlink
    text.Hyperlink = link;
    // Add text to paragraphs collection of Page
    page.Paragraphs.Add(text);
    // Create new TextFragment instance
    text = new Aspose.Pdf.Text.TextFragment("link page number test to page 1");
    // TextFragment should be added over new page
    text.IsInNewPage = true;
    // Create another local hyperlink instance
    link = new Aspose.Pdf.LocalHyperlink();
    // Set Target page for second hyperlink
    link.TargetPageNumber = 1;
    // Set link for second TextFragment
    text.Hyperlink = link;
    // Add text to paragraphs collection of page object
    page.Paragraphs.Add(text);

    // Save PDF document
    document.Save(dataDir + "CreateLocalHyperlink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 获取 PDF 超链接目标 (URL)

链接在 PDF 文件中表示为注释，可以添加、更新或删除。Aspose.PDF for .NET 还支持获取 PDF 文件中超链接的目标 (URL)。

要获取链接的 URL：

1. 创建一个 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 对象。
1. 获取要提取链接的 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page)。
1. 使用 [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) 类从指定页面提取所有 [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) 对象。
1. 将 [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) 对象传递给 [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) 对象的 Accept 方法。
1. 使用 [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) 对象的 Selected 属性将所有选定的链接注释提取到 IList 对象中。
1. 最后，提取 LinkAnnotation Action 作为 GoToURIAction。

以下代码片段展示了如何从 PDF 文件中获取超链接目标 (URL)。

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Traverse through all the page of PDF
        foreach (var page in document.Pages)
        {
            // Get the link annotations from particular page
            var selector = new Aspose.Pdf.Annotations.AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

            page.Accept(selector);

            // Create list holding all the links
            var list = selector.Selected;

            // Iterate through individual item inside list
            foreach (var a in list)
            {
                // Print the destination URL
                Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
            }
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetHyperlink()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Traverse through all the page of PDF
    foreach (var page in document.Pages)
    {
        // Get the link annotations from particular page
        var selector = new Aspose.Pdf.Annotations.AnnotationSelector(new Aspose.Pdf.Annotations.LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

        page.Accept(selector);

        // Create list holding all the links
        var list = selector.Selected;

        // Iterate through individual item inside list
        foreach (var a in list)
        {
            // Print the destination URL
            Console.WriteLine("\nDestination: " + (a.Action as Aspose.Pdf.Annotations.GoToURIAction).URI + "\n");
        }
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## 获取超链接文本

超链接有两个部分：文档中显示的文本和目标 URL。在某些情况下，我们需要的是文本而不是 URL。

PDF 文件中的文本和注释/操作由不同的实体表示。页面上的文本只是一个单词和字符的集合，而注释则带来一些交互性，例如超链接所固有的交互性。

要查找 URL 内容，您需要同时处理注释和文本。[Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotation) 对象本身没有文本，而是位于页面上的文本下方。因此，要获取文本，注释提供了 URL 的边界，而文本对象提供了 URL 内容。请参见以下代码片段。

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShowLinkAnnotationText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Iterate through each page of PDF
        foreach (var page in document.Pages)
        {
            // Show link annotation
            ShowLinkAnnotations(page);
        }
    }
}

private static void ShowLinkAnnotations(Aspose.Pdf.Page page)
{
    foreach (var annot in page.Annotations)
    {
        if (annot is Aspose.Pdf.Annotations.LinkAnnotation)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            page.Accept(absorber);
            string extractedText = absorber.Text;
            // Print the text associated with hyperlink
            Console.WriteLine(extractedText);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShowLinkAnnotationText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Iterate through each page of PDF
    foreach (var page in document.Pages)
    {
        // Show link annotation
        ShowLinkAnnotations(page);
    }
}

private static void ShowLinkAnnotations(Aspose.Pdf.Page page)
{
    foreach (var annot in page.Annotations)
    {
        if (annot is Aspose.Pdf.Annotations.LinkAnnotation)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            page.Accept(absorber);
            string extractedText = absorber.Text;
            // Print the text associated with hyperlink
            Console.WriteLine(extractedText);
        }
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## 从 PDF 文件中移除文档打开操作

[如何在查看文档时指定 PDF 页面](#how-to-specify-pdf-page-when-viewing-document) 解释了如何告诉文档在不同于第一页的页面上打开。当连接多个文档时，如果一个或多个文档设置了 GoTo 操作，您可能希望移除它们。例如，如果合并两个文档，而第二个文档具有将您带到第二页的 GoTo 操作，则输出文档将在第二个文档的第二页打开，而不是合并文档的第一页。为了避免这种行为，请移除打开操作命令。

要移除打开操作：

1. 将 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 对象的 [OpenAction](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/openaction) 属性设置为 null。
1. 使用 Document 对象的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) 方法保存更新后的 PDF。

以下代码片段展示了如何从 PDF 文件中移除文档打开操作。

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveOpenAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "RemoveOpenAction.pdf"))
    {
        // Remove document open action
        document.OpenAction = null;

        // Save PDF document
        document.Save(dataDir + "RemoveOpenAction_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveOpenAction()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "RemoveOpenAction.pdf");

    // Remove document open action
    document.OpenAction = null;

    // Save PDF document
    document.Save(dataDir + "RemoveOpenAction_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 如何在查看文档时指定 PDF 页面 {#how-to-specify-pdf-page-when-viewing-document}

在 PDF 查看器（如 Adobe Reader）中查看 PDF 文件时，文件通常在第一页打开。然而，可以设置文件在不同的页面上打开。

[XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) 类允许您指定要打开的 PDF 文件中的页面。当将 GoToAction 对象值传递给 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 类的 OpenAction 属性时，文档将在与 XYZExplicitDestination 对象指定的页面上打开。以下代码片段展示了如何指定页面作为文档打开操作。

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SpecifyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SpecifyPageWhenViewing.pdf"))
    {
        // Get the instance of second page of document
        var page2 = document.Pages[2];
        // Create the variable to set the zoom factor of target page
        double zoom = 1;
        // Create GoToAction instance
        var action = new Aspose.Pdf.Annotations.GoToAction(document.Pages[2]);
        // Go to 2 page
        action.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
        // Set the document open action
        document.OpenAction = action;
        // Save PDF document
        document.Save(dataDir + "Goto2page_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SpecifyPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "SpecifyPageWhenViewing.pdf");
    // Get the instance of second page of document
    var page2 = document.Pages[2];
    // Create the variable to set the zoom factor of target page
    double zoom = 1;
    // Create GoToAction instance
    var action = new Aspose.Pdf.Annotations.GoToAction(document.Pages[2]);
    // Go to 2 page
    action.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
    // Set the document open action
    document.OpenAction = action;
    // Save PDF document
    document.Save(dataDir + "Goto2page_out.pdf");
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