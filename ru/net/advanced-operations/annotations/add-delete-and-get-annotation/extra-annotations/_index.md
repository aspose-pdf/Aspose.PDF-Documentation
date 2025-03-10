---
title: Дополнительные аннотации с использованием C#
linktitle: Дополнительные аннотации
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ru/net/extra-annotations/
description: Узнайте, как добавлять дополнительные аннотации в PDF-файлы в .NET с использованием Aspose.PDF для интерактивных функций документа.
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extra Annotations using C#",
    "alternativeHeadline": "Enhance PDF Annotations with C#",
    "abstract": "Представляем функцию дополнительных аннотаций в C#, которая позволяет разработчикам без труда добавлять, извлекать и удалять различные аннотации из PDF-документов. Эта мощная функциональность улучшает взаимодействие с PDF, позволяя точно редактировать текст и манипулировать документами, включая возможность эффективно добавлять аннотации курсора и редактирования. Оптимизируйте работу с PDF с помощью этих продвинутых возможностей, разработанных для интуитивного управления документами.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Extra Annotations, Caret Annotation, PDF document manipulation, Aspose.PDF for .NET, Redaction Annotation, Markup annotation, Delete Caret Annotation, Get Caret Annotation, StrikeOutAnnotation, PdfAnnotationEditor",
    "wordcount": "929",
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
    "url": "/net/extra-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extra-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "В этом разделе описывается, как добавлять, получать и удалять дополнительные виды аннотаций из вашего PDF-документа."
}
</script>

## Как добавить аннотацию курсора в существующий PDF-файл

Аннотация курсора — это символ, который указывает на редактирование текста. Аннотация курсора также является аннотацией разметки, поэтому класс Caret наследуется от класса Markup и также предоставляет функции для получения или установки свойств аннотации курсора и сброса потока внешнего вида аннотации курсора.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Шаги, с помощью которых мы создаем аннотацию курсора:

1. Загрузите PDF-файл - новый [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Создайте новую [аннотацию курсора](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) и установите параметры курсора (новый Rectangle, title, Subject, Flags, color, width, StartingStyle и EndingStyle). Эта аннотация используется для указания вставки текста.
1. Создайте новую [аннотацию курсора](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) и установите параметры курсора (новый Rectangle, title, Subject, Flags, color, width, StartingStyle и EndingStyle). Эта аннотация используется для указания замены текста.
1. Создайте новую [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) и установите параметры (новый Rectangle, title, color, новые QuadPoints и новые points, Subject, InReplyTo, ReplyType).
1. После этого мы можем добавить аннотации на страницу.

Следующий фрагмент кода показывает, как добавить аннотацию курсора в PDF-файл:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCaretAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample.pdf"))
    {
        // Create Caret Annotation for text insertion
        var caretAnnotation1 = new Aspose.Pdf.Annotations.CaretAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(299.988, 713.664, 308.708, 720.769))
        {
            Title = "Aspose User",
            Subject = "Inserted text 1",
            Flags = Aspose.Pdf.Annotations.AnnotationFlags.Print,
            Color = Aspose.Pdf.Color.Blue
        };

        // Create Caret Annotation for text replacement
        var caretAnnotation2 = new Aspose.Pdf.Annotations.CaretAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(361.246, 727.908, 370.081, 735.107))
        {
            Flags = Aspose.Pdf.Annotations.AnnotationFlags.Print,
            Subject = "Inserted text 2",
            Title = "Aspose User",
            Color = Aspose.Pdf.Color.Blue
        };

        // Create StrikeOut Annotation
        var strikeOutAnnotation = new Aspose.Pdf.Annotations.StrikeOutAnnotation(document.Pages[1],
            new Rectangle(318.407, 727.826, 368.916, 740.098))
        {
            Color = Aspose.Pdf.Color.Blue,
            QuadPoints = new[] {
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
            },
            Subject = "Cross-out",
            InReplyTo = caretAnnotation2,
            ReplyType = Aspose.Pdf.Annotations.ReplyType.Group
        };

        document.Pages[1].Annotations.Add(caretAnnotation1);
        document.Pages[1].Annotations.Add(caretAnnotation2);
        document.Pages[1].Annotations.Add(strikeOutAnnotation);

        // Save PDF document
        document.Save(dataDir + "AddCaretAnnotations_out.pdf");
    }
}
```

### Получить аннотацию курсора

Пожалуйста, попробуйте использовать следующий фрагмент кода, чтобы получить аннотацию курсора в PDF-документе:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetCaretAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_caret.pdf"))
    {
        // Get Caret annotations from the first page
        var caretAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Caret)
            .Cast<Aspose.Pdf.Annotations.CaretAnnotation>();

        // Iterate through the annotations and print their details
        foreach (var ca in caretAnnotations)
        {
            Console.WriteLine($"{ca.Rect}");
        }
    }
}
```

### Удалить аннотацию курсора

Следующий фрагмент кода показывает, как удалить аннотацию курсора из PDF-файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteCaretAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "sample_caret.pdf"))
    {
        // Get Caret annotations from the first page
        var caretAnnotations = document.Pages[1].Annotations
            .Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Caret)
            .Cast<Aspose.Pdf.Annotations.CaretAnnotation>();

        // Delete each Caret annotation
        foreach (var ca in caretAnnotations)
        {
            document.Pages[1].Annotations.Delete(ca);
        }

        // Save PDF document after deleting annotations
        document.Save(dataDir + "DeleteCaretAnnotation_out.pdf");
    }
}
```

## Закрыть определенную область страницы с помощью аннотации редактирования, используя Aspose.PDF for .NET

Aspose.PDF for .NET поддерживает функцию добавления, а также манипуляции аннотациями в существующем PDF-файле. Недавно некоторые из наших клиентов разместили запрос на редактирование (удаление текста, изображения и т. д. элементов) определенной области страницы PDF-документа. Чтобы выполнить это требование, предоставлен класс под названием RedactionAnnotation, который можно использовать для редактирования определенных областей страницы или для манипуляции существующими RedactionAnnotations и их редактирования (т.е. сглаживания аннотации и удаления текста под ней).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RedactPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create RedactionAnnotation instance for a specific page region
        var annot = new Aspose.Pdf.Annotations.RedactionAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(200, 500, 300, 600));
        annot.FillColor = Aspose.Pdf.Color.Green;
        annot.BorderColor = Aspose.Pdf.Color.Yellow;
        annot.Color = Aspose.Pdf.Color.Blue;

        // Text to be printed on the redact annotation
        annot.OverlayText = "REDACTED";
        annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;

        // Repeat Overlay text over the redact Annotation
        annot.Repeat = true;

        // Add annotation to the annotations collection of the first page
        document.Pages[1].Annotations.Add(annot);

        // Flattens annotation and redacts page contents (i.e., removes text and image under the redacted annotation)
        annot.Redact();

        // Save the result document
        document.Save(dataDir + "RedactPage_out.pdf");
    }
}
```

### Подход фасадов

Пространство имен Aspose.Pdf.Facades также имеет класс под названием [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor), который предоставляет возможность манипулировать существующими аннотациями внутри PDF-файла. Этот класс содержит метод под названием [RedactArea(..)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/redactarea), который предоставляет возможность удалять определенные области страницы.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RedactPageWithFacadesApproach()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create an instance of PdfAnnotationEditor
    using (var editor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Redact a specific page region
        editor.RedactArea(1, new Aspose.Pdf.Rectangle(100, 100, 20, 70), System.Drawing.Color.White);

        // Bind PDF document
        editor.BindPdf(dataDir + "input.pdf");

        // Save the result document
        editor.Save(dataDir + "FacadesApproach_out.pdf");
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