---
title: Манипулирование таблицами в существующих PDF
linktitle: Манипулирование таблицами
type: docs
weight: 40
url: /ru/net/manipulate-tables-in-existing-pdf/
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Манипулирование таблицами в существующих PDF",
    "alternativeHeadline": "Как обновить содержимое таблиц в существующем PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, манипулирование таблицами",
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
    "url": "/net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>

## Манипулирование таблицами в существующих PDF

Одной из самых ранних функций, поддерживаемых Aspose.PDF для .NET, является возможность работы с таблицами, и она обеспечивает отличную поддержку добавления таблиц в создаваемые с нуля или любые существующие PDF-файлы. Вы также получаете возможность интеграции таблицы с базой данных (DOM) для создания динамических таблиц на основе содержимого базы данных. В этом новом выпуске мы реализовали новую функцию поиска и анализа простых таблиц, которые уже существуют на странице документа PDF. Новый класс под названием **Aspose.PDF.Text.TableAbsorber** предоставляет эти возможности. Использование TableAbsorber очень похоже на существующий класс TextFragmentAbsorber. Следующий фрагмент кода показывает шаги по обновлению содержимого в конкретной ячейке таблицы.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Загрузить существующий PDF-файл
Document pdfDocument = new Document(dataDir + "input.pdf");
// Создать объект TableAbsorber для поиска таблиц
TableAbsorber absorber = new TableAbsorber();

// Посетить первую страницу с absorber
absorber.Visit(pdfDocument.Pages[1]);

// Получить доступ к первой таблице на странице, их первой ячейке и текстовым фрагментам в ней
TextFragment fragment = absorber.TableList[0].RowList[0].CellList[0].TextFragments[1];

// Изменить текст первого текстового фрагмента в ячейке
fragment.Text = "привет мир";
dataDir = dataDir + "ManipulateTable_out.pdf";
pdfDocument.Save(dataDir);
```
## Замените старую таблицу на новую в документе PDF

Если вам нужно найти определенную таблицу и заменить ее желаемой, вы можете использовать метод Replace() класса [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) для этого. Следующий пример демонстрирует функциональность замены таблицы внутри документа PDF:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Загрузить существующий документ PDF
Document pdfDocument = new Document(dataDir + @"Table_input2.pdf");

// Создать объект TableAbsorber для поиска таблиц
TableAbsorber absorber = new TableAbsorber();

// Посетить первую страницу с absorber
absorber.Visit(pdfDocument.Pages[1]);

// Получить первую таблицу на странице
AbsorbedTable table = absorber.TableList[0];

// Создать новую таблицу
Table newTable = new Table();
newTable.ColumnWidths = "100 100 100";
newTable.DefaultCellBorder = new BorderInfo(BorderSide.All, 1F);

Row row = newTable.Rows.Add();
row.Cells.Add("Col 1");
row.Cells.Add("Col 2");
row.Cells.Add("Col 3");

// Заменить таблицу на новую
absorber.Replace(pdfDocument.Pages[1], table, newTable);

// Сохранить документ
pdfDocument.Save(dataDir + "TableReplaced_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Библиотека Aspose.PDF для .NET",
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

