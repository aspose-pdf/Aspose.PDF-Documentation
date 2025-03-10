---
title: 使用 C# 的 PDF 工具提示
linktitle: PDF 工具提示
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/pdf-tooltip/
description: 学习如何使用 C# 和 Aspose.PDF 为 PDF 中的文本片段添加工具提示
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Tooltip using C#",
    "alternativeHeadline": "Add Interactive Tooltips to PDF Text in C#",
    "abstract": "使用 C# 的新 PDF 工具提示功能增强您的 PDF 文档。此功能允许您无缝地为 PDF 文件中的文本片段添加工具提示，在用户将鼠标悬停时提供额外信息。利用隐形按钮和隐藏文本块，使用 Aspose.PDF 创建动态和交互式的阅读体验。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1072",
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
    "url": "/net/pdf-tooltip/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-tooltip/"
    },
    "dateModified": "2024-11-26",
    "description": "学习如何使用 C# 和 Aspose.PDF 为 PDF 中的文本片段添加工具提示"
}
</script>

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

## 通过添加隐形按钮为搜索文本添加工具提示

通常需要为 PDF 文档中的短语或特定单词添加一些详细信息作为工具提示，以便在用户将鼠标光标悬停在文本上时弹出。Aspose.PDF for .NET 提供此功能，通过在搜索文本上添加隐形按钮来创建工具提示。以下代码片段将向您展示如何实现此功能：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTooltipToSearchedText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add().Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Move the mouse cursor here to display a tooltip"));
        document.Pages[1].Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Move the mouse cursor here to display a very long tooltip"));
        // Save PDF document
        document.Save(dataDir + "Tooltip_out.pdf");
    }

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Tooltip_out.pdf"))
    {
        // Create TextAbsorber object to find all the phrases matching the regular expression
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Move the mouse cursor here to display a tooltip");
        // Accept the absorber for the document pages
        document.Pages.Accept(absorber);
        // Get the extracted text fragments
        var textFragments = absorber.TextFragments;

        // Loop through the fragments
        foreach (var fragment in textFragments)
        {
            // Create invisible button on text fragment position
            var field = new Aspose.Pdf.Forms.ButtonField(fragment.Page, fragment.Rectangle);
            // AlternateName value will be displayed as tooltip by a viewer application
            field.AlternateName = "Tooltip for text.";
            // Add button field to the document
            document.Form.Add(field);
        }

        absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Move the mouse cursor here to display a very long tooltip");
        document.Pages.Accept(absorber);
        textFragments = absorber.TextFragments;

        foreach (var fragment in textFragments)
        {
            var field = new Aspose.Pdf.Forms.ButtonField(fragment.Page, fragment.Rectangle);
            // Set very long text
            field.AlternateName = "Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                                    " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                                    " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                                    " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                                    " Duis aute irure dolor in reprehenderit in voluptate velit" +
                                    " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                                    " occaecat cupidatat non proident, sunt in culpa qui officia" +
                                    " deserunt mollit anim id est laborum.";
            document.Form.Add(field);
        }

        // Save PDF document
        document.Save(dataDir + "Tooltip_out.pdf");
    }
}
```

{{% alert color="primary" %}}

关于工具提示的长度，工具提示文本作为 PDF 字符串类型包含在 PDF 文档中，位于内容流之外。对于 PDF 文件中的此类字符串没有有效的限制（请参见 PDF 参考附录 C.）。然而，符合标准的阅读器（例如 Adobe Acrobat）在特定处理器和特定操作环境下确实有这样的限制。请参考您的 PDF 阅读器应用程序文档。

{{% /alert %}}

## 创建隐藏文本块并在鼠标悬停时显示

在 Aspose.PDF 中，隐藏操作的功能实现了在某些隐形按钮上鼠标进入/退出时显示/隐藏文本框字段（或任何其他类型的注释）。为此，使用 Aspose.Pdf.Annotations.HideAction 类将隐藏/显示的操作分配给文本块。请使用以下代码片段在鼠标进入/退出时显示/隐藏文本块。

请注意，文档中的 PDF 操作在符合标准的阅读器（例如 Adobe Reader）中运行良好，但对其他 PDF 阅读器（例如网页浏览器插件）没有保证。我们进行了简要调查并发现：

- PDF 文档中所有隐藏操作的实现都在 Internet Explorer v.11.0 中运行良好。
- 所有隐藏操作的实现也在 Opera v.12.14 中运行，但我们发现文档首次打开时有一些响应延迟。
- 仅使用接受字段名称的 HideAction 构造函数的实现可以在 Google Chrome v.61.0 浏览文档时正常工作；如果在 Google Chrome 中浏览很重要，请使用相应的构造函数：

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateHiddenTextBlock()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add paragraph with text
        document.Pages.Add().Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Move the mouse cursor here to display floating text"));
        // Save PDF document
        document.Save(dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf");
    }

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf"))
    {
        // Create TextAbsorber object to find all the phrases matching the regular expression
        var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Move the mouse cursor here to display floating text");
        // Accept the absorber for the document pages
        document.Pages.Accept(absorber);
        // Get the first extracted text fragment
        var textFragments = absorber.TextFragments;
        var fragment = textFragments[1];

        // Create hidden text field for floating text in the specified rectangle of the page
        var floatingField = new Aspose.Pdf.Forms.TextBoxField(fragment.Page, new Aspose.Pdf.Rectangle(100, 700, 220, 740));
        // Set text to be displayed as field value
        floatingField.Value = "This is the \"floating text field\".";
        // We recommend to make field 'readonly' for this scenario
        floatingField.ReadOnly = true;
        // Set 'hidden' flag to make field invisible on document opening
        floatingField.Flags |= Aspose.Pdf.Annotations.AnnotationFlags.Hidden;

        // Setting a unique field name isn't necessary but allowed
        floatingField.PartialName = "FloatingField_1";

        // Setting characteristics of field appearance isn't necessary but makes it better
        floatingField.DefaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance("Helv", 10, System.Drawing.Color.Blue);
        floatingField.Characteristics.Background = System.Drawing.Color.LightBlue;
        floatingField.Characteristics.Border = System.Drawing.Color.DarkBlue;
        floatingField.Border = new Aspose.Pdf.Annotations.Border(floatingField);
        floatingField.Border.Width = 1;
        floatingField.Multiline = true;

        // Add text field to the document
        document.Form.Add(floatingField);

        // Create invisible button on text fragment position
        var buttonField = new Aspose.Pdf.Forms.ButtonField(fragment.Page, fragment.Rectangle);
        // Create new hide action for specified field (annotation) and invisibility flag
        // (You also may reffer floating field by the name if you specified it above)
        // Add actions on mouse enter/exit at the invisible button field
        buttonField.Actions.OnEnter = new Aspose.Pdf.Annotations.HideAction(floatingField, false);
        buttonField.Actions.OnExit = new Aspose.Pdf.Annotations.HideAction(floatingField);

        // Add button field to the document
        document.Form.Add(buttonField);

        // Save PDF document
        document.Save(dataDir + "CreateHiddenTextBlock_out.pdf");
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