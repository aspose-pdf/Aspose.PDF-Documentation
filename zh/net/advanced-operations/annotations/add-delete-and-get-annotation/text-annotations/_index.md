---
title: 使用文本注释处理PDF
linktitle: 文本注释
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/text-annotation/
description: Aspose.PDF for .NET 允许您从PDF文档中添加、获取和删除文本注释。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using Text Annotation for PDF",
    "alternativeHeadline": "Enhance PDFs with Dynamic Text Annotations",
    "abstract": "Aspose.PDF for .NET 引入了先进的文本注释功能，使用户能够轻松地在PDF文档中添加、检索或删除文本注释。此功能通过允许精确放置和自定义注释来增强PDF编辑过程，从而改善文档交互和可用性。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Text Annotation, PDF document generation, Aspose.PDF for .NET, Add Annotation, Delete Annotation, Free Text Annotation, Popup Annotation, StrikeOutAnnotation, AnnotationCollection, Aspose.PDF library",
    "wordcount": "2636",
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
    "url": "/net/text-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/text-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET 允许您从PDF文档中添加、获取和删除文本注释。"
}
</script>

## 如何将文本注释添加到现有PDF文件

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

文本注释是附加到PDF文档中特定位置的注释。关闭时，注释显示为图标；打开时，应显示一个弹出窗口，其中包含读者选择的字体和大小的注释文本。

注释由特定页面的 [Annotations](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations) 集合包含。该集合仅包含该单独页面的注释；每个页面都有自己的注释集合。

要将注释添加到特定页面，请使用 [Add](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/annotationcollection/methods/add) 方法将其添加到该页面的注释集合中。

1. 首先，创建要添加到PDF的注释。
1. 然后打开输入PDF。
1. 将注释添加到 [Page](https://reference.aspose.com/pdf/zh/net/aspose.pdf/page) 对象的注释集合中。

以下代码片段演示了如何在PDF页面中添加注释。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextAnnotationToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAnnotation.pdf"))
    {
        // Create text annotation
        var textAnnotation = new Aspose.Pdf.Annotations.TextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600));
        textAnnotation.Title = "Sample Annotation Title";
        textAnnotation.Subject = "Sample Subject";
        textAnnotation.SetReviewState(Aspose.Pdf.Annotations.AnnotationState.Accepted);
        textAnnotation.Contents = "Sample contents for the annotation";
        textAnnotation.Open = true;
        textAnnotation.Icon = Aspose.Pdf.Annotations.TextIcon.Key;

        // Set border for the annotation
        var border = new Aspose.Pdf.Annotations.Border(textAnnotation);
        border.Width = 5;
        border.Dash = new Aspose.Pdf.Annotations.Dash(1, 1);
        textAnnotation.Border = border;
        textAnnotation.Rect = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

        // Add annotation to the annotations collection of the page
        document.Pages[1].Annotations.Add(textAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddAnnotation_out.pdf");
    }
}
```

## 如何添加弹出注释

弹出注释在弹出窗口中显示文本以供输入和编辑。它不应单独出现，而是与标记注释（其父注释）相关联，并应用于编辑父注释的文本。

它不应具有自己的外观流或相关操作，并应通过父注释字典中的Popup条目进行标识。

以下代码片段演示了如何在PDF页面中添加 [Popup Annotation](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/popupannotation)，以添加父注释的 [Line annotation](/pdf/zh/net/figures-annotation/#how-to-add-line-annotation-into-existing-pdf-file) 为例。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLineAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Appartments.pdf"))
    {
        // Create Line Annotation
        var lineAnnotation = new Aspose.Pdf.Annotations.LineAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(550, 93, 562, 439),
            new Aspose.Pdf.Point(556, 99), new Aspose.Pdf.Point(556, 443))
        {
            Title = "John Smith",
            Color = Aspose.Pdf.Color.Red,
            Width = 3,
            StartingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            EndingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow,
            Popup = new Aspose.Pdf.Annotations.PopupAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(842, 124, 1021, 266))
        };

        // Add annotation to the page
        document.Pages[1].Annotations.Add(lineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddLineAnnotation_out.pdf");
    }
}
```

## 如何添加（或创建）新的自由文本注释

自由文本注释直接在页面上显示文本。 [PdfContentEditor.CreateFreeText](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfcontenteditor/methods/createfreetext) 方法允许创建这种类型的注释。在以下代码片段中，我们在字符串的第一次出现上方添加自由文本注释。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeTextAnnotationDemo()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "pdf-sample.pdf"))
    {
        var pdfContentEditor = new Aspose.Pdf.Facades.PdfContentEditor(document);

        // Assuming tfa is an instance of TextFragmentAbsorber or similar
        var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber();
        tfa.Visit(document.Pages[1]);

        if (tfa.TextFragments.Count <= 0)
        {
            return;
        }

        // Define the rectangle for the free text annotation
        var rect = new System.Drawing.Rectangle
        {
            X = (int)tfa.TextFragments[1].Rectangle.LLX,
            Y = (int)tfa.TextFragments[1].Rectangle.URY + 5,
            Height = 18,
            Width = 100
        };

        // Create free text annotation
        pdfContentEditor.CreateFreeText(rect, "Free Text Demo", 1); // Last param is the page number

        // Save PDF document
        pdfContentEditor.Save(dataDir + "pdf-sample-0.pdf");
    }
}
```

### 为FreeTextAnnotation设置标注属性

为了更灵活地配置PDF文档中的注释，Aspose.PDF for .NET 提供了 [FreeTextAnnotation](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/freetextannotation) 类的 [Callout](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/freetextannotation/properties/callout) 属性，该属性允许指定标注线的点数组。以下代码片段展示了如何使用此功能：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeTextCalloutAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Create default appearance for the annotation
        var da = new Aspose.Pdf.Annotations.DefaultAppearance();
        da.TextColor = System.Drawing.Color.Red;
        da.FontSize = 10;

        // Create free text annotation with callout
        var fta = new Aspose.Pdf.Annotations.FreeTextAnnotation(page, new Aspose.Pdf.Rectangle(422.25, 645.75, 583.5, 702.75), da);
        fta.Intent = Aspose.Pdf.Annotations.FreeTextIntent.FreeTextCallout;
        fta.EndingStyle = Aspose.Pdf.Annotations.LineEnding.OpenArrow;
        fta.Callout = new Aspose.Pdf.Point[]
        {
            new Aspose.Pdf.Point(428.25, 651.75),
            new Aspose.Pdf.Point(462.75, 681.375),
            new Aspose.Pdf.Point(474, 681.375)
        };

        // Add the annotation to the page
        page.Annotations.Add(fta);

        // Set rich text for the annotation
        fta.RichText = "<body xmlns=\"http://www.w3.org/1999/xhtml\" xmlns:xfa=\"http://www.xfa.org/schema/xfa-data/1.0/\" xfa:APIVersion=\"Acrobat:11.0.23\" xfa:spec=\"2.0.2\"  style=\"color:#FF0000;font-weight:normal;font-style:normal;font-stretch:normal\"><p dir=\"ltr\"><span style=\"font-size:9.0pt;font-family:Helvetica\">This is a sample</span></p></body>";

        // Save PDF document
        document.Save(dataDir + "SetCalloutProperty_out.pdf");
    }
}
```

### 为XFDF文件设置标注属性

如果您使用从XFDF文件导入，请使用标注线名称而不是仅使用Callout。以下代码片段展示了如何使用此功能：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotationsFromXfdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAnnotation.pdf"))
    {
        // Create an XFDF string builder
        var xfdf = new StringBuilder();
        xfdf.AppendLine("<?xml version=\"1.0\" encoding=\"UTF-8\"?><xfdf xmlns=\"http://ns.adobe.com/xfdf/\" xml:space=\"preserve\"><annots>");

        // Call the method to create XFDF content
        CreateXfdf(ref xfdf);

        xfdf.AppendLine("</annots></xfdf>");

        // Import annotations from the XFDF string
        document.ImportAnnotationsFromXfdf(new MemoryStream(Encoding.UTF8.GetBytes(xfdf.ToString())));

        // Save PDF document
        document.Save(dataDir + "SetCalloutPropertyXfdf_out.pdf");
    }
}
```

以下方法用于 CreateXfdf：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateXfdf(ref StringBuilder pXfdf)
{
    pXfdf.Append("<freetext");
    pXfdf.Append(" page=\"0\"");
    pXfdf.Append(" rect=\"422.25,645.75,583.5,702.75\"");
    pXfdf.Append(" intent=\"FreeTextCallout\"");
    pXfdf.Append(" callout-line=\"428.25,651.75,462.75,681.375,474,681.375\"");
    pXfdf.Append(" tail=\"OpenArrow\"");
    pXfdf.AppendLine(">");
    pXfdf.Append("<contents-richtext><body ");
    pXfdf.Append(" style=\"font-size:10.0pt;text-align:left;color:#FF0000;font-weight:normal;font-style:normal;font-family:Helvetica;font-stretch:normal\">");
    pXfdf.Append("<p dir=\"ltr\">This is a sample</p>");
    pXfdf.Append("</body></contents-richtext>");
    pXfdf.AppendLine("<defaultappearance>/Helv 12 Tf 1 0 0 rg</defaultappearance>");
    pXfdf.AppendLine("</freetext>");
}
```

### 使自由文本注释不可见

有时，有必要创建一个在查看文档时不可见但在打印文档时可见的水印。为此，请使用注释标志。以下代码片段展示了如何做到这一点。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddInvisibleAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create a free text annotation
        var annotation = new Aspose.Pdf.Annotations.FreeTextAnnotation(
            document.Pages[1],
            new Aspose.Pdf.Rectangle(50, 600, 250, 650),
            new Aspose.Pdf.Annotations.DefaultAppearance("Helvetica", 16, System.Drawing.Color.Red)
        );

        annotation.Contents = "ABCDEFG";
        annotation.Characteristics.Border = System.Drawing.Color.Red;
        annotation.Flags = Aspose.Pdf.Annotations.AnnotationFlags.Print | Aspose.Pdf.Annotations.AnnotationFlags.NoView;

        // Add the annotation to the page
        document.Pages[1].Annotations.Add(annotation);

        // Save PDF document
        document.Save(dataDir + "InvisibleAnnotation_out.pdf");
    }
}
```

### 设置FreeTextAnnotation的格式

这一部分介绍了如何格式化自由文本注释中的文本。

注释包含在 [Page](https://reference.aspose.com/pdf/zh/net/aspose.pdf/page) 对象的 [AnnotationCollection](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/annotationcollection) 集合中。当将 [FreeTextAnnotation](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/freetextannotation) 添加到PDF文档时，可以使用 [DefaultAppearance](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/defaultappearance/methods/index) 类指定格式信息，例如字体、大小、颜色等。还可以使用 TextStyle 属性指定格式信息。此外，您可以更新PDF文档中任何已存在的FreeTextAnnotation的格式。

[TextStyle](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/textstyle) 类支持处理默认样式条目。该类允许您设置颜色、字体大小和字体名称：

- FontName 属性获取或设置字体名称（字符串）。
- FontSize 属性获取和设置默认文本大小（双精度）。
- System.Drawing.Color 属性获取和设置文本颜色（颜色）。
- TextAlignment 属性获取和设置注释的文本对齐方式（对齐方式）。

以下代码片段展示了如何添加具有特定文本格式的FreeTextAnnotation。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFreeTextAnnotationFormatting.pdf"))
    {
        // Instantiate DefaultAppearance object
        var defaultAppearance = new Aspose.Pdf.Annotations.DefaultAppearance("Arial", 28, System.Drawing.Color.Red);

        // Create annotation
        var freetext = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 400, 400, 600), defaultAppearance);

        // Specify the contents of annotation
        freetext.Contents = "Free Text";

        // Add annotation to annotations collection of page
        document.Pages[1].Annotations.Add(freetext);

        // Save PDF document
        document.Save(dataDir + "SetFreeTextAnnotationFormatting_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddFreeAnnotation(string fontName = "Arial", float fontSize = 28)
{
     // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
	
    using (var document = new Aspose.Pdf.Document(dataDir + "SetFreeTextAnnotationFormatting.pdf"))
    {
        // Set default values
        var textColor = System.Drawing.Color.Red;
        var position = new Aspose.Pdf.Rectangle(200, 400, 400, 600);

        // Instantiate DefaultAppearance object
        Aspose.Pdf.Annotations.DefaultAppearance defaultAppearance = new(fontName, fontSize, textColor);
        // Create annotation
        var freetext = new Aspose.Pdf.Annotations.FreeTextAnnotation(document.Pages[1], position, defaultAppearance)
        {
            // Specify the contents of annotation
            Contents = "Free Text"
        };
        // Add anootation to annotations collection of page
        document.Pages[1].Annotations.Add(freetext);

        // Save PDF document
        document.Save(dataDir + "SetFreeTextAnnotationFormatting_out.pdf");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

{{% alert color="primary" %}}

当您更改自由文本注释的内容或文本样式时，注释的外观会重新生成以反映更改。

{{% /alert %}}

### 使用StrikeOutAnnotation划掉单词

Aspose.PDF for .NET 允许您在PDF文档中添加、删除和更新注释。一个类允许您划掉注释。这在您想要划掉文档中的一个或多个文本片段时非常有用。注释保存在 [Page](https://reference.aspose.com/pdf/zh/net/aspose.pdf/page) 对象的 [AnnotationCollection](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/annotationcollection) 集合中。可以使用名为 [StrikeOutAnnotation](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/strikeoutannotation) 的类将划掉注释添加到PDF文档中。

要划掉特定的TextFragment：

1. 在PDF文件中搜索TextFragment。
1. 获取TextFragment对象的坐标。
1. 使用坐标实例化一个StrikeOutAnnotation对象。

以下代码片段展示了如何搜索特定的TextFragment并将StrikeOutAnnotation添加到该对象。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private void StrikeOutTextInDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "pdf-sample.pdf"))
    {
        // Create TextFragment Absorber instance to search for a particular text fragment
        var textFragmentAbsorber = new Aspose.Pdf.Text.TextFragmentAbsorber("Estoque");

        // Iterate through pages of PDF document
        foreach (var page in document.Pages)
        {
            // Accept the absorber for the current page
            page.Accept(textFragmentAbsorber);
        }

        // Get the collection of absorbed text fragments
        var textFragmentCollection = textFragmentAbsorber.TextFragments;

        // Iterate through the collection of text fragments
        foreach (Aspose.Pdf.Text.TextFragment textFragment in textFragmentCollection)
        {
            // Get rectangular dimensions of the TextFragment object
            var rect = new Aspose.Pdf.Rectangle(
                (float)textFragment.Position.XIndent,
                (float)textFragment.Position.YIndent,
                (float)textFragment.Position.XIndent + (float)textFragment.Rectangle.Width,
                (float)textFragment.Position.YIndent + (float)textFragment.Rectangle.Height);

            // Instantiate StrikeOut Annotation instance
            var strikeOut = new Aspose.Pdf.Annotations.StrikeOutAnnotation(textFragment.Page, rect)
            {
                // Set opacity for annotation
                Opacity = 0.80f,

                // Set the color of annotation
                Color = Aspose.Pdf.Color.Red
            };

            // Set the border for annotation instance
            strikeOut.Border = new Aspose.Pdf.Annotations.Border(strikeOut);

            // Add annotation to the annotations collection of the TextFragment's page
            textFragment.Page.Annotations.Add(strikeOut);
        }

        // Save PDF document
        document.Save(dataDir + "StrikeOutWords_out.pdf");
    }
}
```

## 从PDF文件的页面删除所有注释

[Page](https://reference.aspose.com/pdf/zh/net/aspose.pdf/page) 对象的 [AnnotationCollection](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/annotationcollection) 集合包含该特定页面的所有注释。要从页面中删除所有注释，请调用 AnnotationCollectoin 集合的 *Delete* 方法。

以下代码片段展示了如何从特定页面删除所有注释。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteAllAnnotationsFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAnnotationsFromPage.pdf"))
    {
        // Delete all annotations from the first page
        document.Pages[1].Annotations.Delete();

        // Save PDF document
        document.Save(dataDir + "DeleteAllAnnotationsFromPage_out.pdf");
    }
}
```

## 从PDF文件中删除特定注释

{{% alert color="primary" %}}

您可以在此链接检查Aspose.PDF的质量并在线获取结果：
[products.aspose.app/pdf/annotation](https://products.aspose.app/pdf/annotation)

{{% /alert %}}

Aspose.PDF 允许您从PDF文件中删除特定注释。此主题解释了如何操作。

要从PDF中删除特定注释，请调用 [AnnotationCollection 集合的 Delete 方法](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations.annotationcollection/delete/methods/1)。该集合属于 [Page](https://reference.aspose.com/pdf/zh/net/aspose.pdf/page) 对象。Delete 方法需要您要删除的注释的索引。然后，保存更新后的PDF文件。以下代码片段展示了如何删除特定注释。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteParticularAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteParticularAnnotation.pdf"))
    {
        // Delete a particular annotation by index (e.g., the first annotation on the first page)
        document.Pages[1].Annotations.Delete(1);

        // Save PDF document
        document.Save(dataDir + "DeleteParticularAnnotation_out.pdf");
    }
}
```

## 从PDF文档的页面获取所有注释

Aspose.PDF 允许您从整个文档或给定页面获取注释。要从PDF文档的页面获取所有注释，请循环遍历所需页面资源的 [AnnotationCollection](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/annotationcollection) 集合。以下代码片段展示了如何获取页面的所有注释。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAllAnnotationsFromPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetAllAnnotationsFromPage.pdf"))
    {
        // Loop through all the annotations on the first page
        foreach (Aspose.Pdf.Annotations.MarkupAnnotation annotation in document.Pages[1].Annotations)
        {
            // Get annotation properties
            Console.WriteLine("Title : {0} ", annotation.Title);
            Console.WriteLine("Subject : {0} ", annotation.Subject);
            Console.WriteLine("Contents : {0} ", annotation.Contents);
        }
    }
}
```

请注意，要从整个PDF中获取所有注释，您必须在遍历 AnnotationCollection 类集合之前循环遍历文档的 PageCollection 类集合。您可以在称为 MarkupAnnotation 类的基本注释类型中获取集合中的每个注释，然后显示其属性。

## 从PDF文件中获取特定注释

注释与单独的页面相关联，并存储在 [Page](https://reference.aspose.com/pdf/zh/net/aspose.pdf/page) 对象的 [AnnotationCOllection](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/annotationcollection) 集合中。要获取特定注释，请指定其索引。这将返回一个 [Annotation](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/annotation) 对象，需要将其转换为特定的注释类型，例如 [TextAnnotation](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/textannotation)。以下代码片段展示了如何获取特定注释及其属性。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetParticularAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetParticularAnnotation.pdf"))
    {
        // Get a particular annotation by index (e.g., the first annotation on the first page)
        var textAnnotation = (Aspose.Pdf.Annotations.TextAnnotation)document.Pages[1].Annotations[1];

        // Get annotation properties
        Console.WriteLine("Title : {0} ", textAnnotation.Title);
        Console.WriteLine("Subject : {0} ", textAnnotation.Subject);
        Console.WriteLine("Contents : {0} ", textAnnotation.Contents);
    }
}
```

## 获取注释的资源

Aspose.PDF 允许您从整个文档或给定页面获取注释的资源。以下代码片段展示了如何获取输入PDF文件的注释资源作为 [FileSpecification](https://reference.aspose.com/pdf/zh/net/aspose.pdf/filespecification) 对象。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddAndGetResourceOfAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddAnnotation.pdf"))
    {
        // Create a screen annotation with a SWF file
        var sa = new Aspose.Pdf.Annotations.ScreenAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 400, 300, 600), dataDir + "AddSwfFileAsAnnotation.swf");
        document.Pages[1].Annotations.Add(sa);

        // Save PDF document with the new annotation
        document.Save(dataDir + "GetResourceOfAnnotation_out.pdf");

        // Open the updated document
        var document1 = new Aspose.Pdf.Document(dataDir + "GetResourceOfAnnotation_Out.pdf");

        // Get the action of the annotation
        var action = (document1.Pages[1].Annotations[1] as Aspose.Pdf.Annotations.ScreenAnnotation).Action as Aspose.Pdf.Annotations.RenditionAction;

        // Get the rendition of the rendition action
        var rendition = action.Rendition;

        // Get the media clip
        var clip = (rendition as Aspose.Pdf.Annotations.MediaRendition).MediaClip;
        var data = (clip as Aspose.Pdf.Annotations.MediaClipData).Data;

        // Read the media data
        using (var ms = new MemoryStream())
        {
            byte[] buffer = new byte[1024];
            int read = 0;

            // Data of media are accessible in FileSpecification.Contents
            using (var source = data.Contents)
            {
                while ((read = source.Read(buffer, 0, buffer.Length)) > 0)
                {
                    ms.Write(buffer, 0, read);
                }
            }

            Console.WriteLine(rendition.Name);
            Console.WriteLine(action.RenditionOperation);
        }
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