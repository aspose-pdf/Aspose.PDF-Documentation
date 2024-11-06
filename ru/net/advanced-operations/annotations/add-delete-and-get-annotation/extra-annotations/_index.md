---
title: Дополнительные аннотации на C#
linktitle: Дополнительные аннотации
type: docs
weight: 60
url: ru/net/extra-annotations/
description: Этот раздел описывает, как добавлять, получать и удалять дополнительные виды аннотаций из вашего PDF-документа.
lastmod: "2023-09-12"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Дополнительные аннотации на C#",
    "alternativeHeadline": "Как добавить дополнительные аннотации в PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "создание документов PDF",
    "keywords": "pdf, c#, ссылочная аннотация, аннотация курсора",
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
                "contactType": "продажи",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
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
    "dateModified": "2022-02-04",
    "description": "Этот раздел описывает, как добавлять, получать и удалять дополнительные виды аннотаций из вашего PDF-документа."
}
</script>
## Как добавить аннотацию Caret в существующий PDF-файл

Аннотация Caret - это символ, указывающий на редактирование текста. Аннотация Caret также является разметочной аннотацией, поэтому класс Caret наследуется от класса Markup и также предоставляет функции для получения или установки свойств аннотации Caret и сброса потока внешнего вида аннотации Caret.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

Шаги, с помощью которых мы создаем аннотацию Caret:

1. Загрузите PDF-файл - новый [Документ](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Создайте новую [Аннотацию Caret](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/caretannotation) и установите параметры Caret (новый Rectangle, title, Subject, Flags, color, width, StartingStyle и EndingStyle). Эта аннотация используется для указания вставки текста.
1. Создайте новую [StrikeOutAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/strikeoutannotation) и установите параметры (новый Rectangle, title, color, новые QuadPoints и новые points, Subject, InReplyTo, ReplyType).
1. После мы можем добавить аннотации на страницу.

Следующий пример кода показывает, как добавить аннотацию Caret в файл PDF:

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleCaretAnnotation
    {
        // Путь к директории с документами.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddCaretAnnotation()
        {
            // Загрузка файла PDF
            Document document = new Document(System.IO.Path.Combine(_dataDir, "sample.pdf"));
            // Эта аннотация используется для указания вставки текста
            var caretAnnotation1 = new CaretAnnotation(document.Pages[1], new Rectangle(299.988, 713.664, 308.708, 720.769))
            {
                Title = "Пользователь Aspose",
                Subject = "Вставленный текст 1",
                Flags = AnnotationFlags.Print,
                Color = Color.Blue
            };
            // Эта аннотация используется для указания замены текста
            var caretAnnotation2 = new CaretAnnotation(document.Pages[1], new Rectangle(361.246, 727.908, 370.081, 735.107))
            {
                Flags = AnnotationFlags.Print,
                Subject = "Вставленный текст 2",
                Title = "Пользователь Aspose",
                Color = Color.Blue
            };

            var strikeOutAnnotation = new StrikeOutAnnotation(document.Pages[1],
                new Rectangle(318.407, 727.826, 368.916, 740.098))
            {
                Color = Color.Blue,
                QuadPoints = new[] {
                new Point(321.66, 739.416),
                new Point(365.664, 739.416),
                new Point(321.66, 728.508),
                new Point(365.664, 728.508)
            },
                Subject = "Зачеркнуто",
                InReplyTo = caretAnnotation2,
                ReplyType = ReplyType.Group
            };

            document.Pages[1].Annotations.Add(caretAnnotation1);
            document.Pages[1].Annotations.Add(caretAnnotation2);
            document.Pages[1].Annotations.Add(strikeOutAnnotation);

            document.Save(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
        }
```
### Получение аннотации каретки

Пожалуйста, используйте следующий фрагмент кода для получения аннотации каретки в документе PDF

```csharp
public static void GetCaretAnnotation()
{
    // Загрузка файла PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
    var caretAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Caret)
        .Cast<CaretAnnotation>();
    foreach (var ca in caretAnnotations)
    {
        Console.WriteLine($"{ca.Rect}");
    }
}
```

### Удаление аннотации каретки

Следующий фрагмент кода показывает, как удалить аннотацию каретки из файла PDF.

```csharp
public static void DeleteCaretAnnotation()
{
    // Загрузка файла PDF
    Document document = new Document(System.IO.Path.Combine(_dataDir, "sample_caret.pdf"));
    var caretAnnotations = document.Pages[1].Annotations
        .Where(a => a.AnnotationType == AnnotationType.Caret)
        .Cast<CaretAnnotation>();

    foreach (var ca in caretAnnotations)
    {
        document.Pages[1].Annotations.Delete(ca);
    }
    document.Save(System.IO.Path.Combine(_dataDir, "sample_caret_del.pdf"));
}
```
## Закрытие определенной области страницы с помощью аннотации Redaction Annotation в Aspose.PDF для .NET

Aspose.PDF для .NET поддерживает возможность добавления и манипулирования аннотациями в существующем PDF-файле. Недавно некоторые наши клиенты выразили потребность в закрытии (удалении текста, изображений и т. д. элементов из) определенной области страницы PDF-документа. Для выполнения этого требования предоставляется класс под названием RedactionAnnotation, который можно использовать для закрытия определенных областей страницы или для манипулирования существующими RedactionAnnotations и их закрытием (т.е. сглаживание аннотации и удаление текста под ней).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

// Открыть документ
Document doc = new Document(dataDir + "input.pdf");

// Создать экземпляр RedactionAnnotation для конкретной области страницы
RedactionAnnotation annot = new RedactionAnnotation(doc.Pages[1], new Aspose.Pdf.Rectangle(200, 500, 300, 600));
annot.FillColor = Aspose.Pdf.Color.Green;
annot.BorderColor = Aspose.Pdf.Color.Yellow;
annot.Color = Aspose.Pdf.Color.Blue;
// Текст, который будет напечатан на аннотации закрытия
annot.OverlayText = "REDACTED";
annot.TextAlignment = Aspose.Pdf.HorizontalAlignment.Center;
// Повтор текста закрытия на аннотации
annot.Repeat = true;
// Добавить аннотацию в коллекцию аннотаций первой страницы
doc.Pages[1].Annotations.Add(annot);
// Сглаживание аннотации и закрытие содержимого страницы (т.е. удаление текста и изображения
// Под закрытой аннотацией)
annot.Redact();
dataDir = dataDir + "RedactPage_out.pdf";
doc.Save(dataDir);
```
### Подход с использованием фасадов

Пространство имен Aspose.PDF.Facades также имеет класс с именем [PdfAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor), который предоставляет возможность управлять существующими аннотациями в файле PDF. Этот класс содержит метод с именем [RedactArea(..)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/redactarea), который позволяет удалять определенные области страницы.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

Aspose.Pdf.Facades.PdfAnnotationEditor редактор = new Aspose.Pdf.Facades.PdfAnnotationEditor();
// Закрасить определенную область страницы
редактор.RedactArea(1, new Aspose.Pdf.Rectangle(100, 100, 20, 70), System.Drawing.Color.White);
редактор.BindPdf(dataDir + "input.pdf");
редактор.Save(dataDir + "FacadesApproach_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для библиотеки .NET",
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
                "contactType": "продажи",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
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
    "applicationCategory": "Библиотека для манипуляции PDF для .NET",
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
```

