---
title: Работа с метаданными PDF файла | C#
linktitle: Метаданные PDF файла
type: docs
weight: 140
url: /ru/net/pdf-file-metadata/
description: Этот раздел объясняет, как получить информацию о PDF файле, как получить XMP метаданные из PDF файла, установить информацию о PDF файле.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Работа с метаданными PDF файла | C#",
    "alternativeHeadline": "Как получить метаданные PDF файла",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация pdf документов",
    "keywords": "pdf, c#, метаданные pdf файла",
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
    "url": "/net/pdf-file-metadata/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-file-metadata/"
    },
    "dateModified": "2022-02-04",
    "description": "Этот раздел объясняет, как получить информацию о PDF файле, как получить XMP метаданные из PDF файла, установить информацию о PDF файле."
}
</script>
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Получение информации о файле PDF

Для получения информации о конкретном файле PDF, вам сначала нужно получить объект [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo), используя свойство [Info](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/info) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). После получения объекта [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo), вы можете получить значения отдельных свойств. Следующий фрагмент кода показывает, как получить информацию о файле PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Открыть документ
Document pdfDocument = new Document(dataDir + "GetFileInfo.pdf");
// Получить информацию о документе
DocumentInfo docInfo = pdfDocument.Info;
// Показать информацию о документе
Console.WriteLine("Автор: {0}", docInfo.Author);
Console.WriteLine("Дата создания: {0}", docInfo.CreationDate);
Console.WriteLine("Ключевые слова: {0}", docInfo.Keywords);
Console.WriteLine("Дата изменения: {0}", docInfo.ModDate);
Console.WriteLine("Тема: {0}", docInfo.Subject);
Console.WriteLine("Название: {0}", docInfo.Title);
```
## Установка информации о файле PDF

Aspose.PDF для .NET позволяет устанавливать специфическую информацию для PDF, такую как автор, дата создания, тема и название. Для установки этой информации:

1. Создайте объект [DocumentInfo](https://reference.aspose.com/pdf/net/aspose.pdf/documentinfo).
1. Установите значения свойств.
1. Сохраните обновленный документ, используя метод Save класса Document.

{{% alert color="primary" %}}

Обратите внимание, что вы не можете устанавливать значения для полей *Application* и *Producer*, так как против этих полей будут отображаться Aspose Ltd. и Aspose.PDF для .NET x.x.x.

{{% /alert %}}

Следующий фрагмент кода показывает, как установить информацию о файле PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Открыть документ
Document pdfDocument = new Document(dataDir + "SetFileInfo.pdf");

// Указать информацию о документе
DocumentInfo docInfo = new DocumentInfo(pdfDocument);

docInfo.Author = "Aspose";
docInfo.CreationDate = DateTime.Now;
docInfo.Keywords = "Aspose.Pdf, DOM, API";
docInfo.ModDate = DateTime.Now;
docInfo.Subject = "Информация о PDF";
docInfo.Title = "Установка информации о документе PDF";

dataDir = dataDir + "SetFileInfo_out.pdf";
// Сохранить выходной документ
pdfDocument.Save(dataDir);
```
## Получение метаданных XMP из PDF-файла

Aspose.PDF позволяет получить доступ к метаданным XMP PDF-файла. Чтобы получить метаданные PDF-файла:

1. Создайте объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) и откройте входной PDF-файл.
1. Получите метаданные файла с помощью свойства [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata).

Следующий фрагмент кода показывает, как получить метаданные из PDF-файла.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Открыть документ
Document pdfDocument = new Document(dataDir + "GetXMPMetadata.pdf");

// Получить свойства
Console.WriteLine(pdfDocument.Metadata["xmp:CreateDate"]);
Console.WriteLine(pdfDocument.Metadata["xmp:Nickname"]);
Console.WriteLine(pdfDocument.Metadata["xmp:CustomProperty"]);
```

## Установка метаданных XMP в PDF-файле

Aspose.PDF позволяет устанавливать метаданные в PDF-файле.
Aspose.PDF позволяет устанавливать метаданные в файле PDF.

1. Создайте объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Установите значения метаданных с помощью свойства [Metadata](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/metadata).
1. Сохраните обновленный документ с помощью метода [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Следующий фрагмент кода показывает, как установить метаданные в файле PDF.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Открыть документ
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");

// Установить свойства
pdfDocument.Metadata["xmp:CreateDate"] = DateTime.Now;
pdfDocument.Metadata["xmp:Nickname"] = "Nickname";
pdfDocument.Metadata["xmp:CustomProperty"] = "Custom Value";

dataDir = dataDir + "SetXMPMetadata_out.pdf";
// Сохранить документ
pdfDocument.Save(dataDir);
```
## Вставка метаданных с префиксом

Некоторым разработчикам необходимо создать новое пространство имен метаданных с префиксом. Следующий фрагмент кода показывает, как вставить метаданные с префиксом.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Открыть документ
Document pdfDocument = new Document(dataDir + "SetXMPMetadata.pdf");
pdfDocument.Metadata.RegisterNamespaceUri("xmp", "http:// Ns.adobe.com/xap/1.0/"); // Префикс Xmlns был удален
pdfDocument.Metadata["xmp:ModifyDate"] = DateTime.Now;

dataDir = dataDir + "SetPrefixMetadata_out.pdf";
// Сохранить документ
pdfDocument.Save(dataDir);
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

