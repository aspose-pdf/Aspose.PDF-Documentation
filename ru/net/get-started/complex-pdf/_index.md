---
title: Создание сложного PDF
linktitle: Создание сложного PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ru/net/complex-pdf-example/
description: Aspose.PDF для NET позволяет создавать более сложные документы, которые содержат изображения, текстовые фрагменты и таблицы в одном документе.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating a complex PDF",
    "alternativeHeadline": "Create Complex PDFs with Images, Text, and Tables in C#",
    "abstract": "Aspose.PDF for .NET представляет мощную функцию для создания сложных PDF, позволяя разработчикам бесшовно интегрировать изображения, текстовые фрагменты и таблицы в один документ. Эта функциональность использует подход на основе DOM, позволяя детальную настройку и контроль макета при генерации PDF, что делает его идеальным для эффективного создания документов профессионального уровня.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "632",
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
    "url": "/net/complex-pdf-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/complex-pdf-example/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

Пример [Hello, World](/pdf/net/hello-world-example/) показал простые шаги для создания PDF-документа с использованием C# и Aspose.PDF. В этой статье мы рассмотрим создание более сложного документа с C# и Aspose.PDF for .NET. В качестве примера мы возьмем документ от вымышленной компании, которая предоставляет услуги пассажирских паромов. 
Наш документ будет содержать изображение, два текстовых фрагмента (заголовок и абзац) и таблицу. Для создания такого документа мы будем использовать подход на основе DOM. Вы можете прочитать больше в разделе [Основы DOM API](/pdf/net/basics-of-dom-api/).

Если мы создаем документ с нуля, нам нужно следовать определенным шагам:

1. Создайте объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). На этом этапе мы создадим пустой PDF-документ с некоторыми метаданными, но без страниц.
1. Добавьте [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) в объект документа. Теперь у нашего документа будет одна страница.
1. Добавьте [Image](https://reference.aspose.com/pdf/net/aspose.pdf/image/methods/index) на страницу.
1. Создайте [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) для заголовка. Для заголовка мы будем использовать шрифт Arial размером 24pt и центрированное выравнивание.
1. Добавьте заголовок в [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) страницы.
1. Создайте [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) для описания. Для описания мы будем использовать шрифт Arial размером 24pt и центрированное выравнивание.
1. Добавьте (описание) в абзацы страницы.
1. Создайте таблицу, добавьте свойства таблицы.
1. Добавьте (таблицу) в [Paragraphs](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) страницы.
1. Сохраните документ "Complex.pdf".

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreatingComplexPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Add image
        page.AddImage(dataDir + "logo.png", new Aspose.Pdf.Rectangle(20, 730, 120, 830));

        // Add Header
        var header = new Aspose.Pdf.Text.TextFragment("New ferry routes in Fall 2020");
        header.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
        header.TextState.FontSize = 24;
        header.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
        header.Position = new Aspose.Pdf.Text.Position(130, 720);
        page.Paragraphs.Add(header);

        // Add description
        var descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.";
        var description = new Aspose.Pdf.Text.TextFragment(descriptionText);
        description.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Times New Roman");
        description.TextState.FontSize = 14;
        description.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Left;
        page.Paragraphs.Add(description);

        // Add table
        var table = new Aspose.Pdf.Table
        {
            ColumnWidths = "200",
            Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 1f, Aspose.Pdf.Color.DarkSlateGray),
            DefaultCellBorder = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.Box, 0.5f, Aspose.Pdf.Color.Black),
            DefaultCellPadding = new Aspose.Pdf.MarginInfo(4.5, 4.5, 4.5, 4.5),
            Margin =
            {
                Bottom = 10
            },
            DefaultCellTextState =
            {
                Font =  Aspose.Pdf.Text.FontRepository.FindFont("Helvetica")
            }
        };

        var headerRow = table.Rows.Add();
        headerRow.Cells.Add("Departs City");
        headerRow.Cells.Add("Departs Island");
        foreach (Aspose.Pdf.Cell headerRowCell in headerRow.Cells)
        {
            headerRowCell.BackgroundColor = Aspose.Pdf.Color.Gray;
            headerRowCell.DefaultCellTextState.ForegroundColor = Aspose.Pdf.Color.WhiteSmoke;
        }

        var time = new TimeSpan(6, 0, 0);
        var incTime = new TimeSpan(0, 30, 0);
        for (int i = 0; i < 10; i++)
        {
            var dataRow = table.Rows.Add();
            dataRow.Cells.Add(time.ToString(@"hh\:mm"));
            time = time.Add(incTime);
            dataRow.Cells.Add(time.ToString(@"hh\:mm"));
        }

        page.Paragraphs.Add(table);
        // Save PDF document
        document.Save(dataDir + "Complex_out.pdf");
    }
}
```