---
title: Работа с векторной графикой
linktitle: Работа с векторной графикой
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 100
url: /ru/net/working-with-vector-graphics/
description: Эта статья описывает функции работы с инструментом GraphicsAbsorber с использованием C#.
lastmod: "2024-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Vector Graphics",
    "alternativeHeadline": "Enhance PDF Graphics Manipulation with С№",
    "abstract": "Откройте для себя расширенные возможности инструмента GraphicsAbsorber в Aspose.PDF for .NET, позволяя разработчикам бесшовно манипулировать векторной графикой в PDF-документах. Эта функция позволяет точно извлекать, перемещать и удалять графику, а также добавлять их на разные страницы, улучшая ваш рабочий процесс манипуляции PDF с большей гибкостью и контролем.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "889",
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
    "url": "/net/working-with-vector-graphics/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-vector-graphics/"
    },
    "dateModified": "2024-11-26",
    "description": "Этот раздел описывает функции работы с PDF-файлом GraphicsAbsorber с использованием библиотеки C#."
}
</script>

В этой главе мы рассмотрим, как использовать мощный класс `GraphicsAbsorber` для взаимодействия с векторной графикой в PDF-документах. Независимо от того, нужно ли вам переместить, удалить или добавить графику, этот гид покажет вам, как эффективно выполнять эти задачи.

## Введение<a name="introduction"></a>

Векторная графика является важным компонентом многих PDF-документов, используемых для представления изображений, форм и других графических элементов. Aspose.PDF предоставляет класс `GraphicsAbsorber`, который позволяет разработчикам программно получать доступ и манипулировать этой графикой. Используя метод `Visit` класса `GraphicsAbsorber`, вы можете извлекать векторную графику с указанной страницы и выполнять различные операции, такие как перемещение, удаление или копирование их на другие страницы.

## Извлечение графики с помощью `GraphicsAbsorber`<a name="extracting-graphics"></a>

Первый шаг в работе с векторной графикой — извлечение их из PDF-документа. Вот как вы можете это сделать, используя класс `GraphicsAbsorber`:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void UsingGraphicsAbsorber()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open the document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create an instance of GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Select the first page of the document
            var page = document.Pages[1];

            // Use the `Visit` method to extract graphics from the page
            graphicsAbsorber.Visit(page);

            // Display information about the extracted elements
            foreach (var element in graphicsAbsorber.Elements)
            {
                Console.WriteLine($"Page Number: {element.SourcePage.Number}");
                Console.WriteLine($"Position: ({element.Position.X}, {element.Position.Y})");
                Console.WriteLine($"Number of Operators: {element.Operators.Count}");
            }
        }
    }
}
```

1. **Создайте объект документа**: Новый объект `Document` создается с путем к целевому PDF-файлу.
2. **Создайте экземпляр `GraphicsAbsorber`**: Этот класс захватывает все графические элементы с указанной страницы.
3. **Метод Visit**: Метод `Visit` вызывается на первой странице, позволяя `GraphicsAbsorber` поглотить векторную графику.
4. **Итерация по извлеченным элементам**: Код проходит по каждому извлеченному элементу, выводя информацию, такую как номер страницы, позиция и количество операторов рисования.

## Перемещение графики<a name="moving-graphics"></a>

После того как вы извлекли графику, вы можете переместить их на другое место на той же странице. Вот как вы можете это сделать:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void MoveGraphics()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create a GraphicsAbsorber instance 
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Select the first page of the document
            var page = document.Pages[1];

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Temporarily suspend updates to improve performance
            graphicsAbsorber.SuppressUpdate();

            // Loop through each extracted graphic element and shift its position
            foreach (var element in graphicsAbsorber.Elements)
            {
                var position = element.Position;
                // Move graphics by shifting its X and Y coordinates
                element.Position = new Aspose.Pdf.Point(position.X + 150, position.Y - 10);
            }

            // Resume updates and apply changes
            graphicsAbsorber.ResumeUpdate();
        }

        // Save PDF document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

- **SuppressUpdate**: Этот метод временно приостанавливает обновления для повышения производительности при внесении нескольких изменений.
- **ResumeUpdate**: Этот метод возобновляет обновления и применяет изменения, внесенные в позиции графики.
- **Позиционирование элементов**: Позиция каждой графики корректируется путем изменения ее координат `X` и `Y`.

## Удаление графики<a name="removing-graphics"></a>

Существуют сценарии, когда вы можете захотеть удалить определенные графические элементы со страницы. Aspose.PDF предлагает два метода для достижения этого:

### Метод 1: Использование границы прямоугольника

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveGraphicsMethod1()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Define the rectangle where graphics will be removed
            var rectangle = new Aspose.Pdf.Rectangle(70, 248, 170, 252);

            // Temporarily suspend updates for better performance
            graphicsAbsorber.SuppressUpdate();

            // Iterate through the extracted graphic elements and remove elements inside the rectangle
            foreach (var element in graphicsAbsorber.Elements)
            {
                // Check if the graphic's position falls within the rectangle
                if (rectangle.Contains(element.Position))
                {
                    // Remove the graphic element
                    element.Remove();
                }
            }

            // Resume updates and apply changes
            graphicsAbsorber.ResumeUpdate();
        }

        // Save PDF document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

### Метод 2: Использование коллекции удаленных элементов

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveGraphicsMethod2()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first page of the document
            var page = document.Pages[1];

            // Define the rectangle where graphics will be removed
            var rectangle = new Aspose.Pdf.Rectangle(70, 248, 170, 252);

            // Extract graphic elements from the page
            graphicsAbsorber.Visit(page);

            // Create a collection for the removed elements
            var removedElementsCollection = new Aspose.Pdf.Vector.GraphicElementCollection();

            // Add elements within the rectangle to the collection
            foreach (var item in graphicsAbsorber.Elements.Where(el => rectangle.Contains(el.Position)))
            {
                removedElementsCollection.Add(item);
            }

            // Temporarily suppress updates for better performance
            page.Contents.SuppressUpdate();

            // Delete the selected graphic elements
            page.DeleteGraphics(removedElementsCollection);

            // Resume updates and apply changes
            page.Contents.ResumeUpdate();
        }

        // Save PDF document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

- **Граница прямоугольника**: Определите прямоугольную область, чтобы указать, какие графические элементы удалить.
- **Приостановка и возобновление обновлений**: Обеспечьте эффективное удаление без промежуточного рендеринга.

## Добавление графики на другую страницу<a name="adding-graphics"></a>

Графика, поглощенная с одной страницы, может быть добавлена на другую страницу в том же документе. Вот два метода для достижения этого:

### Метод 1: Добавление графики по отдельности

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddToAnotherPageMethod1()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first and second pages
            var page1 = document.Pages[1];
            var page2 = document.Pages[2];

            // Extract graphic elements from the first page
            graphicsAbsorber.Visit(page1);

            // Temporarily suppress updates for better performance
            page2.Contents.SuppressUpdate();

            // Add each graphic element from the first page to the second page
            foreach (var element in graphicsAbsorber.Elements)
            {
                element.AddOnPage(page2); // Add each graphic element to the second page.
            }

            // Resume updates and apply changes
            page2.Contents.ResumeUpdate();
        }

        // Save PDF document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

### Метод 2: Добавление графики как коллекции

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddToAnotherPageMethod2()
{
    // The path to the document directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithVectorGraphics.pdf"))
    {
        // Create GraphicsAbsorber
        using (var graphicsAbsorber = new Aspose.Pdf.Vector.GraphicsAbsorber())
        {
            // Get the first and second pages
            var page1 = document.Pages[1];
            var page2 = document.Pages[2];

            // Extract graphic elements from the first page
            graphicsAbsorber.Visit(page1);

            // Temporarily suppress updates for better performance
            page2.Contents.SuppressUpdate();

            // Add all graphics at once from the first page to the second page
            page2.AddGraphics(graphicsAbsorber.Elements);

            // Resume updates and apply changes
            page2.Contents.ResumeUpdate();
        }

        // Save PDF document
        document.Save(dataDir + "DocumentWithVectorGraphics_out.pdf");
    }
}
```

- **SuppressUpdate и ResumeUpdate**: Эти методы помогают поддерживать производительность при внесении массовых изменений.
- **AddOnPage против AddGraphics**: Используйте `AddOnPage` для индивидуальных добавлений и `AddGraphics` для массовых добавлений.

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