---
title: 更新 PDF 中的链接
linktitle: 更新链接
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/update-links/
description: 以编程方式更新 PDF 中的链接。本指南介绍如何在 C# 语言中更新 PDF 中的链接。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Update Links in PDF",
    "alternativeHeadline": "Programmatically Modify PDF Links Using C#",
    "abstract": "新的 PDF 中更新链接功能允许用户以编程方式修改 PDF 文档中的超链接。此功能使用户能够将链接指向特定页面、外部网页地址或其他 PDF 文件，从而增强数字文档的互动性和可用性。通过简化链接管理过程，此功能非常适合希望优化其 PDF 应用程序的开发人员。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Update links in PDF, C#, LinkAnnotation, GoToAction, XYZExplicitDestination, GoToURIAction, update hyperlink, PDF manipulation",
    "wordcount": "797",
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
    "url": "/net/update-links/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/update-links/"
    },
    "dateModified": "2024-11-25",
    "description": "以编程方式更新 PDF 中的链接。本指南介绍如何在 C# 语言中更新 PDF 中的链接。"
}
</script>

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## 更新 PDF 文件中的链接

如在《在 PDF 文件中添加超链接》中所讨论的， [LinkAnnotation](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/linkannotation) 类使得在 PDF 文件中添加链接成为可能。还有一个类似的类用于获取 PDF 文件中的现有链接。如果您需要更新现有链接，请使用此类。要更新现有链接：

1. 加载 PDF 文件。
1. 转到 PDF 文件中的特定页面。
1. 使用 [GoToAction](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/gotoaction) 对象的 Destination 属性指定链接目标。
1. 使用 [XYZExplicitDestination](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/xyzexplicitdestination) 构造函数指定目标页面。

### 将链接目标设置为同一文档中的页面

以下代码片段演示如何在 PDF 文件中更新链接并将其目标设置为文档的第二页。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf"))
    {
        // Get the first link annotation from first page of document
        var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];

        // Modification link: change link destination
        var goToAction = (Aspose.Pdf.Annotations.GoToAction)linkAnnot.Action;

        // Specify the destination for link object
        // The first parameter is document object, second is destination page number.
        // The 5ht argument is zoom factor when displaying the respective page. When using 2, the page will be displayed in 200% zoom
        goToAction.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 1, 2, 2);

        // Save PDF document
        document.Save(dataDir + "UpdateLinks_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf");

    // Get the first link annotation from first page of document
    var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];

    // Modification link: change link destination
    var goToAction = (Aspose.Pdf.Annotations.GoToAction)linkAnnot.Action;

    // Specify the destination for link object
    // The first parameter is document object, second is destination page number.
    // The 5ht argument is zoom factor when displaying the respective page. When using 2, the page will be displayed in 200% zoom
    goToAction.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(1, 1, 2, 2);

    // Save PDF document
    document.Save(dataDir + "UpdateLinks_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### 将链接目标设置为网页地址

要更新超链接以指向网页地址，请实例化 [GoToURIAction](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/gotouriaction) 对象并将其传递给 LinkAnnotation 的 Action 属性。以下代码片段演示如何在 PDF 文件中更新链接并将其目标设置为网页地址。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf"))
    {
        // Get the first link annotation from first page of document
        var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];

        // Modification link: change link action and set target as web address
        linkAnnot.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");

        // Save PDF document
        document.Save(dataDir + "SetDestinationLink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf");

    // Get the first link annotation from first page of document
    var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];

    // Modification link: change link action and set target as web address
    linkAnnot.Action = new Aspose.Pdf.Annotations.GoToURIAction("www.aspose.com");

    // Save PDF document
    document.Save(dataDir + "SetDestinationLink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### 将链接目标设置为另一个 PDF 文件

以下代码片段演示如何在 PDF 文件中更新链接并将其目标设置为另一个 PDF 文件。

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf"))
    {
        var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];
        var goToR = (Aspose.Pdf.Annotations.GoToRemoteAction)linkAnnot.Action;

        // Next line update destination, do not update file
        goToR.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(2, 0, 0, 1.5);

        // Next line update file
        goToR.File = new Aspose.Pdf.FileSpecification(dataDir + "input.pdf");

        // Save PDF document
        document.Save(dataDir + "SetTargetLink_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf");

    var linkAnnot = (Aspose.Pdf.Annotations.LinkAnnotation)document.Pages[1].Annotations[1];
    var goToR = (Aspose.Pdf.Annotations.GoToRemoteAction)linkAnnot.Action;

    // Next line update destination, do not update file
    goToR.Destination = new Aspose.Pdf.Annotations.XYZExplicitDestination(2, 0, 0, 1.5);

    // Next line update file
    goToR.File = new Aspose.Pdf.FileSpecification(dataDir + "input.pdf");

    // Save PDF document
    document.Save(dataDir + "SetTargetLink_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### 更新 LinkAnnotation 文本颜色

链接注释不包含文本。相反，文本放置在注释下方页面的内容中。因此，要更改文本的颜色，请替换页面文本的颜色，而不是尝试更改注释的颜色。以下代码片段演示如何在 PDF 文件中更新链接注释的颜色。

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf"))
    {
        foreach (var annotation in document.Pages[1].Annotations)
        {
            if (annotation is Aspose.Pdf.Annotations.LinkAnnotation)
            {
                // Search the text under the annotation
                var ta = new Aspose.Pdf.Text.TextFragmentAbsorber();
                var rect = annotation.Rect;
                rect.LLX -= 10;
                rect.LLY -= 10;
                rect.URX += 10;
                rect.URY += 10;
                ta.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(rect);
                ta.Visit(document.Pages[1]);

                // Change color of the text.
                foreach (var textFragment in ta.TextFragments)
                {
                    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "UpdateLinkTextColor_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UpdateLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "UpdateLinks.pdf");

    foreach (var annotation in document.Pages[1].Annotations)
    {
        if (annotation is Aspose.Pdf.Annotations.LinkAnnotation)
        {
            // Search the text under the annotation
            var ta = new Aspose.Pdf.Text.TextFragmentAbsorber();
            var rect = annotation.Rect;
            rect.LLX -= 10;
            rect.LLY -= 10;
            rect.URX += 10;
            rect.URY += 10;
            ta.TextSearchOptions = new Aspose.Pdf.Text.TextSearchOptions(rect);
            ta.Visit(document.Pages[1]);

            // Change color of the text.
            foreach (var textFragment in ta.TextFragments)
            {
                textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
            }
        }
    }

    // Save PDF document
    document.Save(dataDir + "UpdateLinkTextColor_out.pdf");
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