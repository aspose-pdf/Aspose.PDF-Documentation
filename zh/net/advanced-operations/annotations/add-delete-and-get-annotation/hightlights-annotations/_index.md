---
title: 使用 C# 的 PDF 高亮注释
linktitle: 高亮注释
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/highlights-annotation/
description: 学习如何使用 Aspose.PDF 在 .NET 中为 PDF 文档添加高亮注释，以强调和审阅文本。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF Highlight Annotation using C#",
    "alternativeHeadline": "PDF Annotations with Customizable Highlighting Options",
    "abstract": "新的使用 C# 的 PDF 高亮注释功能允许用户无缝添加和自定义 PDF 文档中的文本标记注释。此功能包括高亮、下划线、删除线和波浪下划线的选项，所有这些都可以编辑颜色、不透明度和元数据，从而增强文档的互动性和清晰度。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "PDF Highlight Annotation, C#, text markup annotation, highlight settings, strikethrough settings, underline settings, add annotation, delete annotation, Aspose.PDF.Drawing, markup annotations",
    "wordcount": "958",
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
    "url": "/net/highlights-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/highlights-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "标记注释在文档的文本中以高亮、下划线、删除线或波浪下划线的形式呈现。"
}
</script>

文本标记注释应以高亮、下划线、删除线或波浪（“波浪状”）下划线的形式出现在文档的文本中。打开时，它们应显示一个弹出窗口，包含相关注释的文本。

PDF 文档中的文本标记注释的属性可以使用 PDF 查看控件提供的属性窗口进行编辑。可以修改文本标记注释的颜色、不透明度、作者和主题。

可以使用 highlightSettings 属性获取或设置高亮注释的设置。highlightSettings 属性用于设置高亮注释的颜色、不透明度、作者、主题、修改日期和锁定状态属性。

也可以使用 strikethroughSettings 属性获取或设置删除线注释的设置。strikethroughSettings 属性用于设置删除线注释的颜色、不透明度、作者、主题、修改日期和锁定状态属性。

下一个功能是使用 underlineSettings 属性获取或设置下划线注释的设置。underlineSettings 属性用于设置下划线注释的颜色、不透明度、作者、主题、修改日期和锁定状态属性。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## 添加文本标记注释

为了向 PDF 文档添加文本标记注释，我们需要执行以下操作：

1. 加载 PDF 文件 - 新建 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document) 对象。
1. 创建注释：
    - [HighlightAnnotation](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/highlightannotation) 并设置参数（标题、颜色）。
    - [StrikeOutAnnotation](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/strikeoutannotation) 并设置参数（标题、颜色）。
    - [SquigglyAnnotation](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/squigglyannotation) 并设置参数（标题、颜色）。
    - [UnderlineAnnotation](https://reference.aspose.com/pdf/zh/net/aspose.pdf.annotations/underlineannotation) 并设置参数（标题、颜色）。
1. 然后我们应该将所有注释添加到页面。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextMarkupAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Create a TextFragmentAbsorber to find the text "PDF"
        var tfa = new Aspose.Pdf.Text.TextFragmentAbsorber("PDF");
        tfa.Visit(document.Pages[1]);

        // Create annotations for the found text fragments
        var highlightAnnotation = new Aspose.Pdf.Annotations.HighlightAnnotation(document.Pages[1], tfa.TextFragments[1].Rectangle)
        {
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.LightGreen
        };

        var strikeOutAnnotation = new Aspose.Pdf.Annotations.StrikeOutAnnotation(document.Pages[1], tfa.TextFragments[2].Rectangle)
        {
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.Blue
        };

        var squigglyAnnotation = new Aspose.Pdf.Annotations.SquigglyAnnotation(document.Pages[1], tfa.TextFragments[3].Rectangle)
        {
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.Red
        };

        var underlineAnnotation = new Aspose.Pdf.Annotations.UnderlineAnnotation(document.Pages[1], tfa.TextFragments[4].Rectangle)
        {
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.Violet
        };

        // Add annotations to the page
        document.Pages[1].Annotations.Add(highlightAnnotation);
        document.Pages[1].Annotations.Add(squigglyAnnotation);
        document.Pages[1].Annotations.Add(strikeOutAnnotation);
        document.Pages[1].Annotations.Add(underlineAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddTextMarkupAnnotations_out.pdf");
    }
}
```

如果您想突出显示多行片段，您应该使用高级示例：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddHighlightAnnotationAdvanced()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
    {
        var page = document.Pages[1];
        var tfa = new TextFragmentAbsorber(@"Adobe\W+Acrobat\W+Reader", new TextSearchOptions(true));
        tfa.Visit(page);
        foreach (var textFragment in tfa.TextFragments)
        {
            var highlightAnnotation = HighLightTextFragment(page, textFragment, Color.Yellow);
            page.Annotations.Add(highlightAnnotation);
        }

        // Save PDF document
        document.Save(dataDir + "AddHighlightAnnotationAdvanced_out.pdf");
    }
}

private static HighlightAnnotation HighLightTextFragment(Page page,
    Aspose.Pdf.Text.TextFragment textFragment, Aspose.Pdf.Color color)
{
    if (textFragment.Segments.Count == 1)
    {
        return new Aspose.Pdf.Annotations.HighlightAnnotation(page, textFragment.Segments[1].Rectangle)
        {
            Title = "Aspose User",
            Color = color,
            Modified = DateTime.Now,
            QuadPoints = new Aspose.Pdf.Point[]
            {
                new Aspose.Pdf.Point(textFragment.Segments[1].Rectangle.LLX, textFragment.Segments[1].Rectangle.URY),
                new Aspose.Pdf.Point(textFragment.Segments[1].Rectangle.URX, textFragment.Segments[1].Rectangle.URY),
                new Aspose.Pdf.Point(textFragment.Segments[1].Rectangle.LLX, textFragment.Segments[1].Rectangle.LLY),
                new Aspose.Pdf.Point(textFragment.Segments[1].Rectangle.URX, textFragment.Segments[1].Rectangle.LLY)
            }
        };
    }

    var offset = 0;
    var quadPoints = new Aspose.Pdf.Point[textFragment.Segments.Count * 4];
    foreach (Aspose.Pdf.Text.TextSegment segment in textFragment.Segments)
    {
        quadPoints[offset + 0] = new Aspose.Pdf.Point(segment.Rectangle.LLX, segment.Rectangle.URY);
        quadPoints[offset + 1] = new Aspose.Pdf.Point(segment.Rectangle.URX, segment.Rectangle.URY);
        quadPoints[offset + 2] = new Aspose.Pdf.Point(segment.Rectangle.LLX, segment.Rectangle.LLY);
        quadPoints[offset + 3] = new Aspose.Pdf.Point(segment.Rectangle.URX, segment.Rectangle.LLY);
        offset += 4;
    }

    var llx = quadPoints.Min(pt => pt.X);
    var lly = quadPoints.Min(pt => pt.Y);
    var urx = quadPoints.Max(pt => pt.X);
    var ury = quadPoints.Max(pt => pt.Y);
    return new Aspose.Pdf.Annotations.HighlightAnnotation(page, new Aspose.Pdf.Rectangle(llx, lly, urx, ury))
    {
        Title = "Aspose User",
        Color = color,
        Modified = DateTime.Now,
        QuadPoints = quadPoints
    };
}

private static void GetHighlightedText()
{
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
    {
        var highlightAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Highlight)
            .Cast<Aspose.Pdf.Annotations.HighlightAnnotation>();
        foreach (var ta in highlightAnnotations)
        {
            Console.WriteLine($"[{ta.GetMarkedText()}]");
        }
    }
}
```

## 获取文本标记注释

请尝试使用以下代码片段从 PDF 文档中获取文本标记注释。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetTextMarkupAnnotation()
{
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
    {
        var textMarkupAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Highlight
            || a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Squiggly)
            .Cast<Aspose.Pdf.Annotations.TextMarkupAnnotation>();
        foreach (var ta in textMarkupAnnotations)
        {
            Console.WriteLine($"[{ta.AnnotationType} {ta.Rect}]");
        }
    }
}
```

## 删除文本标记注释

以下代码片段演示如何从 PDF 文件中删除文本标记注释。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteTextMarkupAnnotation()
{
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_mod.pdf"))
    {
        var textMarkupAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Highlight
            ||a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Squiggly)
            .Cast<Aspose.Pdf.Annotations.TextMarkupAnnotation>();
        foreach (var ta in textMarkupAnnotations)
        {
            document.Pages[1].Annotations.Delete(ta);
        }
        
        // Save PDF document
        document.Save(dataDir + "DeleteTextMarkupAnnotation_out.pdf");
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