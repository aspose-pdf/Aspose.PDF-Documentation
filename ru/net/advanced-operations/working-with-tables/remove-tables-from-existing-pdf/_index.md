---
title: Удаление таблиц из существующего PDF
linktitle: Удаление таблиц
type: docs
weight: 50
url: /ru/net/remove-tables-from-existing-pdf/
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Удаление таблиц из существующего PDF",
    "alternativeHeadline": "Как удалить таблицы из PDF",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация PDF документов",
    "keywords": "pdf, c#, удаление таблицы, удалить таблицы",
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
    "url": "/net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
{{% alert color="primary" %}}

Aspose.PDF для NET предоставляет возможности вставки/создания таблицы в документе PDF во время его создания с нуля или вы также можете добавить объект таблицы в любой существующий документ PDF. Однако у вас может возникнуть потребность в [Манипулировании таблицами в существующем PDF](https://docs.aspose.com/pdf/net/manipulate-tables-in-existing-pdf/), где вы можете обновлять содержимое существующих ячеек таблицы. Также может возникнуть потребность в удалении объектов таблиц из существующего документа PDF.

{{% /alert %}}

Для удаления таблиц необходимо использовать класс [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber), чтобы получить доступ к таблицам в существующем PDF, а затем вызвать [Remove](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/remove).

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Удаление таблицы из документа PDF

Мы добавили новую функцию, а именно
Мы добавили новую функцию, а именно:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Загрузить существующий документ PDF
Document pdfDocument = new Document(dataDir + "Table_input.pdf");

// Создать объект TableAbsorber для поиска таблиц
TableAbsorber absorber = new TableAbsorber();

// Посетить первую страницу с помощью absorber
absorber.Visit(pdfDocument.Pages[1]);

// Получить первую таблицу на странице
AbsorbedTable table = absorber.TableList[0];

// Удалить таблицу
absorber.Remove(table);

// Сохранить PDF
pdfDocument.Save(dataDir + "Table_out.pdf");
```

## Удаление нескольких таблиц из документа PDF

Иногда в документе PDF может содержаться более одной таблицы, и у вас может возникнуть необходимость удалить несколько таблиц из него. Для удаления нескольких таблиц из документа PDF, пожалуйста, используйте следующий фрагмент кода:

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к каталогу документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// Загрузить существующий документ PDF
Document pdfDocument = new Document(dataDir + "Table_input2.pdf");

// Создать объект TableAbsorber для поиска таблиц
TableAbsorber absorber = new TableAbsorber();

// Посетить вторую страницу с помощью absorber
absorber.Visit(pdfDocument.Pages[1]);

// Получить копию коллекции таблиц
AbsorbedTable[] tables = new AbsorbedTable[absorber.TableList.Count];
absorber.TableList.CopyTo(tables, 0);

// Пройтись по копии коллекции и удалить таблицы
foreach (AbsorbedTable table in tables)
    absorber.Remove(table);

// Сохранить документ
pdfDocument.Save(dataDir + "Table2_out.pdf");
```
{{% alert color="primary" %}}

Пожалуйста, учитывайте, что удаление или замена таблицы изменяет коллекцию TableList. Поэтому, в случае удаления/замены таблиц в цикле, копирование коллекции TableList является обязательным.

{{% /alert %}}

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
    "applicationCategory": "Библиотека для манипуляции с PDF для .NET",
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

