---
title: Использование аннотаций ссылок в PDF
linktitle: Аннотации ссылок
type: docs
weight: 70
url: ru/net/link-annotations/
description: Aspose.PDF для .NET позволяет добавлять, получать и удалять аннотации ссылок в вашем PDF документе.
lastmod: "2024-07-28"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Использование аннотации ссылок для PDF",
    "alternativeHeadline": "Как добавить аннотацию ссылки в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, аннотация текста",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
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
    "description": "Aspose.PDF для .NET позволяет добавлять, получать и удалять аннотации текста из вашего PDF документа."
}
</script>
## Добавление аннотации ссылки в существующий PDF файл

> Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

Аннотация [Link Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) представляет собой гиперссылку, место назначения в другом месте и документ. Согласно стандарту PDF, аннотация ссылки может использоваться в трех случаях: открытие представления страницы, открытие файла и открытие веб-страницы.

### Использование аннотации ссылки для открытия представления страницы

Для создания аннотации было выполнено несколько дополнительных шагов. Мы использовали 2 TextFragmentAbsorber для поиска фрагментов для демонстрации. Первый предназначен для текста аннотации ссылки, а второй указывает на некоторые места в документе.

```cs
Document document = new Document(System.IO.Path.Combine(_dataDir, "Link Annotation Demo.pdf"));

var page = document.Pages[1];

var regEx = new Regex(@"Link Annotation Demo \d");
TextFragmentAbsorber textFragmentAbsorber1 = new TextFragmentAbsorber(regEx);
textFragmentAbsorber1.Visit(document);

regEx = new Regex(@"Sample text \d");
TextFragmentAbsorber textFragmentAbsorber2 = new TextFragmentAbsorber(regEx);
textFragmentAbsorber2.Visit(document);

var linkFragments = textFragmentAbsorber1.TextFragments;
var sampleTextFragments = textFragmentAbsorber2.TextFragments;

var linkAnnotation1 = new LinkAnnotation(page, linkFragments[1].Rectangle)
{
    Action = new GoToAction(
        new XYZExplicitDestination(
            sampleTextFragments[1].Page,
            sampleTextFragments[1].Rectangle.LLX,
            sampleTextFragments[1].Rectangle.URX, 1.5))
};

page.Annotations.Add(linkAnnotation1);

document.Save("test.pdf");
```
Для создания аннотации мы следовали определённым шагам:

1. Создать `LinkAnnotation` и передать объект страницы и прямоугольник текстового фрагмента, который соответствует аннотации.
1. Установить `Action` как `GoToAction` и передать `XYZExplicitDestination` в качестве желаемого назначения. Мы создали `XYZExplicitDestination` на основе страницы, левых и верхних координат и масштаба.
1. Добавить аннотацию в коллекцию аннотаций страницы.
1. Сохранить документ

### Использование ссылочной аннотации с именованным назначением

При обработке различных документов возникает ситуация, когда вы печатаете и не знаете, куда будет указывать аннотация.
В этом случае вы можете использовать специальное (именованное) назначение, и код будет выглядеть так:

```cs
var destinationName = "Link2";
var linkAnnotation2 = new LinkAnnotation(page, linkFragments[2].Rectangle)
{
    Action = new GoToAction(document, destinationName)
};
```

В другом месте вы можете создать Именованное Назначение.

```cs
document.NamedDestinations.Add(destinationName,
    new XYZExplicitDestination(
        sampleTextFragments[2].Page,
        sampleTextFragments[2].Rectangle.LLX,
        sampleTextFragments[2].Rectangle.URX, 1));
```
### Использование аннотации ссылки для открытия файла

Тот же подход используется при создании аннотации для открытия файла, как и в приведенных выше примерах.

```cs
var linkAnnotation3 = new LinkAnnotation(page, linkFragments[3].Rectangle)
{
    Action = new GoToRemoteAction("another.pdf", 2)
};
```

Разница заключается в том, что мы будем использовать `GoToRemoteAction` вместо `GoToAction`. Конструктор GoToRemoteAction принимает два параметра: имя файла и номер страницы.
Вы также можете использовать другую форму и передать имя файла и некоторое назначение. Очевидно, что такое назначение нужно создать до его использования.

### Использование аннотации ссылки для открытия веб-страницы

Чтобы открыть веб-страницу, просто установите `Action` с объектом `GoToURIAction`.
Вы можете передать гиперссылку в качестве параметра конструктора или любой другой тип URI. Например, вы можете использовать `callto` для реализации действия с вызовом номера телефона.

```cs
var linkAnnotation4 = new LinkAnnotation(page, linkFragments[4].Rectangle)
{
    Action = new GoToURIAction("https://products.aspose.com/pdf/net"),
    // Создать аннотацию ссылки и установить действие для вызова номера телефона
    //Action = new GoToURIAction("callto:678-555-0103")
    Color = Color.Blue
};
```
## Добавление декорированной ссылочной аннотации

Вы можете настроить ссылочную аннотацию с помощью границ. В примере ниже мы создадим синюю пунктирную границу шириной 3pt.

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

Еще один пример показывает, как симулировать стиль браузера и использовать подчеркивание для ссылок.

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

### Получение ссылочных аннотаций

Пожалуйста, попробуйте использовать следующий фрагмент кода для получения LinkAnnotation из PDF документа.

```csharp
class ExampleLinkAnnotations
{
    // Путь к директории документов.
    private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    public static void GetLinkAnnotations()
    {
        // Загрузите PDF файл
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);
        foreach (Aspose.Pdf.Annotations.Annotation annot in linkAnnotations)
        {
            // Вывод URL каждой ссылочной аннотации
            Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
            TextAbsorber absorber = new TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            document.Pages[1].Accept(absorber);
            string extractedText = absorber.Text;
            // Вывод текста, связанного с гиперссылкой
            Console.WriteLine(extractedText);
        }
    }
}
```
### Удаление аннотаций ссылок

Следующий фрагмент кода показывает, как удалить аннотацию ссылки из файла PDF. Для этого нам нужно найти и удалить все аннотации ссылок на 1-й странице. После этого мы сохраняем документ с удаленной аннотацией.

```csharp
class ExampleLinkAnnotations
{
    // Путь к директории с документами.
    private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
    public static void DeleteLinkAnnotations()
    {
        // Загрузить PDF файл
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        // Найти и удалить все аннотации ссылок на 1-й странице
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);

        foreach (var la in linkAnnotations)
            document.Pages[1].Annotations.Delete(la);
        // Сохранить документ с удаленной аннотацией
        document.Save(System.IO.Path.Combine(_dataDir, "SimpleResume_del.pdf"));
    }
}
```
