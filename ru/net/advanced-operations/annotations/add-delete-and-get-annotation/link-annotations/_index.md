---
title: Использование аннотаций ссылок в PDF
linktitle: Аннотации ссылок
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ru/net/link-annotations/
description: Aspose.PDF for .NET позволяет добавлять, получать и удалять аннотации ссылок из вашего PDF-документа.
lastmod: "2024-07-28"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using Link Annotation for PDF",
    "alternativeHeadline": "How to add Link Annotation in PDF",
    "abstract": "Aspose.PDF для .NET предоставляет надёжные возможности для управления аннотированными ссылками в PDF-документах, позволяя пользователям легко добавлять, извлекать и удалять гиперссылки. Эта функция повышает интерактивность документа, позволяя ссылкам открывать определённые страницы, внешние файлы или веб-URL-адреса, причём всё это настраивается с различными стилями и действиями. Откройте для себя новые возможности навигации по PDF-файлам и взаимодействия с пользователями благодаря этой мощной функции аннотаций.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, text annotation",
    "wordcount": "302",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/link-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/link-annotation/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF для .NET позволяет добавлять, получать и удалять текстовые аннотации из вашего PDF-документа."
}
</script>

## Добавление аннотации ссылки в существующий PDF-файл

> Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

[Аннотация ссылки](/reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) представляет собой гиперссылку, пункт назначения в другом месте и документ. Согласно стандарту PDF, аннотацию ссылок можно использовать в трёх случаях: просмотр страницы, открытие файла и просмотр веб-страницы.

### Использование аннотации ссылок для просмотра страницы

Для создания аннотации были выполнены несколько дополнительных шагов. Мы использовали 2 TextFragmentAbsorbers для поиска фрагментов для демонстрации. Первый предназначен для текста аннотации ссылки, а второй указывает на некоторые места в документе.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddLinkAnnotation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Link Annotation Demo.pdf"))
    {
        // Get first page
        var page = document.Pages[1];

        // Define regular expressions for text fragments
        var regEx1 = new Regex(@"Link Annotation Demo \d");
        var regEx2 = new Regex(@"Sample text \d");

        // Create TextFragmentAbsorber for the first regular expression
        var textFragmentAbsorber1 = new Aspose.Pdf.Text.TextFragmentAbsorber(regEx1);
        textFragmentAbsorber1.Visit(document);

        // Create TextFragmentAbsorber for the second regular expression
        var textFragmentAbsorber2 = new Aspose.Pdf.Text.TextFragmentAbsorber(regEx2);
        textFragmentAbsorber2.Visit(document);

        // Get the text fragments for both absorbers
        var linkFragments = textFragmentAbsorber1.TextFragments;
        var sampleTextFragments = textFragmentAbsorber2.TextFragments;

        // Create a LinkAnnotation
        var linkAnnotation1 = new Aspose.Pdf.Annotations.LinkAnnotation(page, linkFragments[1].Rectangle)
        {
            Action = new Aspose.Pdf.Annotations.GoToAction(
                new Aspose.Pdf.Annotations.XYZExplicitDestination(
                    sampleTextFragments[1].Page,
                    sampleTextFragments[1].Rectangle.LLX,
                    sampleTextFragments[1].Rectangle.URX, 1.5))
        };

        // Add the link annotation to the page
        page.Annotations.Add(linkAnnotation1);

        // Save PDF document
        document.Save(dataDir + "AddLinkAnnotation_out.pdf");
    }
}
```

Чтобы создать аннотацию, мы выполнили следующие шаги:

1. Создайте `LinkAnnotation` и передайте объект страницы и прямоугольник текстового фрагмента, который соответствует аннотации.
1. Установите `Action` как `GoToAction` и передайте `XYZExplicitDestination` в качестве желаемого пункта назначения. Мы создали `XYZExplicitDestination`, основываясь на странице, левых и верхних координатах и масштабе.
1. Добавьте аннотацию в коллекцию аннотаций страницы.
1. Сохраните документ.

### Использование аннотации ссылок с именованным пунктом назначения

При обработке различных документов возникает ситуация, когда вы печатаете и не знаете, куда будет указывать аннотация. В этом случае вы можете использовать специальный (именованный) пункт назначения, и код будет выглядеть следующим образом:

```cs
var destinationName = "Link2";
var linkAnnotation2 = new LinkAnnotation(page, linkFragments[2].Rectangle)
{
    Action = new GoToAction(document, destinationName)
};
```

В другом месте вы можете создать именованный пункт назначения.

```cs
document.NamedDestinations.Add(destinationName,
    new XYZExplicitDestination(
        sampleTextFragments[2].Page,
        sampleTextFragments[2].Rectangle.LLX,
        sampleTextFragments[2].Rectangle.URX, 1));
```

### Использование аннотации ссылок для открытия файла

Тот же подход используется при создании аннотации для открытия файла, как в примерах выше.

```cs
var linkAnnotation3 = new LinkAnnotation(page, linkFragments[3].Rectangle)
{
    Action = new GoToRemoteAction("another.pdf", 2)
};
```

Разница заключается в том, что мы будем использовать `GoToRemoteAction` вместо `GoToAction`. Конструктор GoToRemoteAction получает два параметра: имя файла и номер страницы. Вы также можете использовать другую форму и передать имя файла и некоторый пункт назначения. Очевидно, вам нужно создать такой пункт назначения, прежде чем его использовать.

### Использование аннотации ссылок для открытия веб-страницы

Чтобы открыть веб-страницу, просто установите `Action` с объектом `GoToURIAction`. Вы можете передать гиперссылку в качестве параметра конструктора или любой другой тип URI. Например, вы можете использовать `callto` для выполнения действия с вызовом номера телефона.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),
    // Create Link Annotation and set the action to call a phone number
    //Action = new GoToURIAction("callto:678-555-0103")
    Color = Color.Blue
};
```

## Добавление оформленной аннотации ссылки

Вы можете настроить аннотацию ссылки с помощью границ. В приведённом ниже примере мы создадим синюю пунктирную границу шириной 3pt.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),    
    Color = Color.Blue
};

linkAnnotation4.Border = new Border(linkAnnotation4)
{
    Style = BorderStyle.Dashed,
    Dash = new Dash(5, 5),
    Width = 3
};
```

Ещё один пример показывает, как имитировать стиль браузера и использовать подчёркивание для ссылок.

```cs
var linkAnnotation5 = new LinkAnnotation(page, linkFragments[5].Rectangle)
{
    Color = Color.Blue
};
linkAnnotation5.Border = new Border(linkAnnotation5)
{
    Style = BorderStyle.Underline,
    Width = 3
};
```

### Получение аннотаций ссылок

Попробуйте использовать следующий фрагмент кода для получения LinkAnnotation из PDF-документа.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetLinkAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume_mod.pdf"))
    {
        // Get all Link annotations from the first page
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Link);

        // Iterate through each Link annotation
        foreach (Aspose.Pdf.Annotations.Annotation annot in linkAnnotations)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as Aspose.Pdf.Annotations.LinkAnnotation).Action as Aspose.Pdf.Annotations.GoToURIAction).URI);

            // Create a TextAbsorber to extract text within the annotation's rectangle
            var absorber = new Aspose.Pdf.Text.TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;

            // Accept the absorber for the first page
            document.Pages[1].Accept(absorber);

            // Extract and print the text associated with the hyperlink
            string extractedText = absorber.Text;
            Console.WriteLine(extractedText);
        }
    }
}
```

### Удаление аннотаций ссылок

Следующий фрагмент кода показывает, как удалить аннотацию ссылки из PDF-файла. Для этого нам нужно найти и удалить все аннотации ссылок на первой странице. После этого мы сохраним документ с удалённой аннотацией.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeleteLinkAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume_mod.pdf"))
    {
        // Find and delete all link annotations on the 1st page
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == Aspose.Pdf.Annotations.AnnotationType.Link);

        foreach (var la in linkAnnotations)
        {
            document.Pages[1].Annotations.Delete(la);
        }

        // Save PDF document
        document.Save(dataDir + "DeleteLinkAnnotations_out.pdf");
    }
}
```