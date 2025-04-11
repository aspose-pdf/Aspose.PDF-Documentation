---
title: Аннотация выделения PDF с использованием C#
linktitle: Аннотация выделения
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/highlights-annotation/
description: Узнайте, как добавить аннотацию выделения в PDF-документы в .NET с использованием Aspose.PDF для акцента на тексте и его рецензирования.
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
    "abstract": "Новая функция аннотации выделения PDF с использованием C# позволяет пользователям без труда добавлять и настраивать аннотации разметки текста в своих PDF-документах. Эта функциональность включает параметры для выделений, подчеркиваний, зачеркиваний и зубчатых подчеркиваний, все из которых можно редактировать по цвету, непрозрачности и метаданным, что улучшает интерактивность и ясность документа.",
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
    "description": "Аннотации разметки представлены в тексте как выделения, подчеркивания, зачеркивания или зубчатые подчеркивания в тексте документа."
}
</script>

Аннотации разметки текста будут отображаться как выделения, подчеркивания, зачеркивания или зубчатые (“извивающиеся”) подчеркивания в тексте документа. При открытии они будут отображать всплывающее окно с текстом связанной заметки.

Свойства аннотаций разметки текста в PDF-документе можно редактировать с помощью окна свойств, предоставленного в элементе управления просмотра PDF. Цвет, непрозрачность, автор и тема аннотации разметки текста могут быть изменены.

Можно получить или установить параметры аннотаций выделения, используя свойство highlightSettings. Свойство highlightSettings используется для установки свойств цвета, непрозрачности, автора, темы, modifiedDate и isLocked аннотаций выделения.

Также можно получить или установить параметры аннотаций зачеркивания, используя свойство strikethroughSettings. Свойство strikethroughSettings используется для установки свойств цвета, непрозрачности, автора, темы, modifiedDate и isLocked аннотаций зачеркивания.

Следующая функция — это возможность получить или установить параметры аннотаций подчеркивания, используя свойство underlineSettings. Свойство underlineSettings используется для установки свойств цвета, непрозрачности, автора, темы, modifiedDate и isLocked аннотаций подчеркивания.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Добавить аннотацию разметки текста

Чтобы добавить аннотацию разметки текста в PDF-документ, необходимо выполнить следующие действия:

1. Загрузить PDF-файл - новый [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document) объект.
1. Создать аннотации:
    - [HighlightAnnotation](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/highlightannotation) и установить параметры (название, цвет).
    - [StrikeOutAnnotation](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/strikeoutannotation) и установить параметры (название, цвет).
    - [SquigglyAnnotation](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/squigglyannotation) и установить параметры (название, цвет).
    - [UnderlineAnnotation](https://reference.aspose.com/pdf/ru/net/aspose.pdf.annotations/underlineannotation) и установить параметры (название, цвет).
1. После этого необходимо добавить все аннотации на страницу.

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

Если вы хотите выделить многострочный фрагмент, вам следует использовать расширенный пример:

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

## Получить аннотацию разметки текста

Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы получить аннотацию разметки текста из PDF-документа.

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

## Удалить аннотацию разметки текста

Следующий фрагмент кода показывает, как удалить аннотацию разметки текста из PDF-файла.

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