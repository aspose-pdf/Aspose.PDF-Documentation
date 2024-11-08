---
title: Пример Hello World на языке C#
linktitle: Пример Hello World
type: docs
weight: 40
url: /ru/net/hello-world-example/
description: Этот пример демонстрирует, как создать простой PDF документ с текстом Hello World с использованием Aspose.PDF
aliases:
    - /net/hello-world/
lastmod: "2022-02-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Пример Hello World на языке C#",
    "alternativeHeadline": "Пример Aspose.PDF на C#",
    "author": {
        "@type": "Person",
        "givenName": "Андрий",
        "familyName": "Андруховский",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, c#, генерация документов",
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
                "areaServed": "США",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "английский"
            }
        ]
    },
    "url": "http://docs.aspose.com/pdf/net/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/net/hello-world-example/"
    },
    "dateModified": "2022-02-04",
    "description": "Этот пример демонстрирует, как создать простой PDF документ с текстом Hello World с использованием Aspose.PDF",
    "articleBody": "Пример \"Hello World\" традиционно используется для демонстрации возможностей языка программирования или программного обеспечения с помощью простого примера использования.\nAspose.PDF для .NET - это функционально насыщенное PDF API, которое позволяет разработчикам встраивать возможности создания, управления и конвертации PDF документов в их .NET приложения. Оно поддерживает работу с многими популярными форматами файлов, включая PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX и форматы изображений. В этой статье мы создаем PDF документ, содержащий текст \"Hello World!\". После установки Aspose.PDF для .NET в вашей среде, вы можете выполнить приведенный ниже пример кода, чтобы увидеть, как работает API Aspose.PDF.\nНиже приведен фрагмент кода, который следует этим шагам:\n1. Создать объект Document\n2. Добавить страницу к объекту документа\n3. Создать TextFragment\n4. Добавить TextFragment в коллекцию Paragraph страницы\n5. Сохранить результирующий PDF документ\nНиже приведен код программы Hello World для демонстрации работы API Aspose.PDF для .NET."
}
</script>
Пример "Hello World" традиционно используется для демонстрации особенностей языка программирования или программного обеспечения на простом примере.

Aspose.PDF для .NET - это функционально насыщенный API для работы с PDF, который позволяет разработчикам встраивать возможности создания, манипуляции и конвертации PDF-документов в их .NET приложения. Он поддерживает работу с множеством популярных форматов файлов, включая PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX и форматы изображений. В этой статье мы создаем PDF-документ, содержащий текст "Hello World!". После установки Aspose.PDF для .NET в вашей среде, вы можете выполнить приведенный ниже пример кода, чтобы увидеть, как работает API Aspose.PDF.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Приведенный ниже фрагмент кода следует этим шагам:

1. Создать объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Добавить [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) к объекту документа
1.
1.
1. Добавьте TextFragment в коллекцию [Paragraph](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) страницы
1. [Сохраните](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) результирующий PDF документ

Следующий фрагмент кода является программой "Hello World", демонстрирующей работу API Aspose.PDF для .NET.

```csharp
namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
        public static void HelloWorld()
        {
            // Инициализация объекта документа
            Document document = new Document();
            // Добавление страницы
            Page page = document.Pages.Add();
            // Добавление текста на новую страницу
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
            // Сохранение обновленного PDF
            var outputFileName = System.IO.Path.Combine(_dataDir, "HelloWorld_out.pdf");
            document.Save( outputFileName );
        }
    }
}
```
