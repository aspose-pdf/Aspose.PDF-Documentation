---
title: Извлечение и сохранение вложения
linktitle: Извлечение и сохранение вложения
type: docs
weight: 20
url: ru/net/extract-and-save-an-attachment/
description: Aspose.PDF для .NET позволяет получить все вложения из документа PDF. Также вы можете получить отдельное вложение из вашего документа.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Извлечение и сохранение вложения",
    "alternativeHeadline": "Как извлечь и сохранить вложения",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голубь",
        "givenName": "Анастасия",
        "familyName": "Голубь",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, сохранение вложений, извлечение вложений",
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
    "url": "/net/extract-and-save-an-attachment/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-and-save-an-attachment/"
    },
    "dateModified": "2022-02-04",
    "description": "Aspose.PDF для .NET позволяет получить все вложения из документа PDF. Также вы можете получить отдельное вложение из вашего документа."
}
</script>
## Получение всех вложений

С помощью Aspose.PDF можно получить все вложения из документа PDF. Это полезно, когда вы хотите сохранить документы отдельно от PDF или если вам нужно удалить вложения из PDF.

Для получения всех вложений из файла PDF:

1. Пройдите через коллекцию [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). Коллекция [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) содержит все вложения. Каждый элемент этой коллекции представляет объект [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification). Каждая итерация цикла foreach по коллекции [EmbeddedFiles](https://reference.aspose.com/pdf/net/aspose.pdf/embeddedfilecollection) возвращает объект [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification).
1.

Следующие примеры кода показывают, как получить все вложения из документа PDF.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите по ссылке https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории документов.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// Открыть документ
Document pdfDocument = new Document(dataDir + "GetAlltheAttachments.pdf");

// Получить коллекцию встроенных файлов
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;

// Получить количество встроенных файлов
Console.WriteLine("Всего файлов: {0}", embeddedFiles.Count);

int count = 1;

// Пройти по коллекции, чтобы получить все вложения
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    Console.WriteLine("Имя: {0}", fileSpecification.Name);
    Console.WriteLine("Описание: {0}",
    fileSpecification.Description);
    Console.WriteLine("MIME-тип: {0}", fileSpecification.MIMEType);

    // Проверить, содержит ли объект параметры
    if (fileSpecification.Params != null)
    {
        Console.WriteLine("Контрольная сумма: {0}",
        fileSpecification.Params.CheckSum);
        Console.WriteLine("Дата создания: {0}",
        fileSpecification.Params.CreationDate);
        Console.WriteLine("Дата изменения: {0}",
        fileSpecification.Params.ModDate);
        Console.WriteLine("Размер: {0}", fileSpecification.Params.Size);
    }

    // Получить вложение и записать в файл или поток
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0,
    fileContent.Length);
    FileStream fileStream = new FileStream(dataDir + count + "_out" + ".txt",
    FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    fileStream.Close();
    count+=1;
}
```
## Получение отдельного вложения

Для получения отдельного вложения мы можем указать индекс вложения в объекте `EmbeddedFiles` экземпляра документа. Пожалуйста, используйте следующий фрагмент кода.

```csharp
// Для полных примеров и файлов данных, пожалуйста, перейдите на https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// Путь к директории с документами.
string dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

// Открыть документ
Document pdfDocument = new Document(dataDir + "GetIndividualAttachment.pdf");

// Получить конкретный встроенный файл
FileSpecification fileSpecification = pdfDocument.EmbeddedFiles[1];

// Получить свойства файла
Console.WriteLine("Имя: {0}", fileSpecification.Name);
Console.WriteLine("Описание: {0}", fileSpecification.Description);
Console.WriteLine("MIME тип: {0}", fileSpecification.MIMEType);

// Проверить, содержит ли объект параметры
if (fileSpecification.Params != null)
{
    Console.WriteLine("Контрольная сумма: {0}",
    fileSpecification.Params.CheckSum);
    Console.WriteLine("Дата создания: {0}",
    fileSpecification.Params.CreationDate);
    Console.WriteLine("Дата изменения: {0}",
    fileSpecification.Params.ModDate);
    Console.WriteLine("Размер: {0}", fileSpecification.Params.Size);
}

// Получить вложение и записать в файл или поток
byte[] fileContent = new byte[fileSpecification.Contents.Length];
fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);

FileStream fileStream = new FileStream(dataDir + "test_out" + ".txt", FileMode.Create);
fileStream.Write(fileContent, 0, fileContent.Length);
fileStream.Close();
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF для .NET библиотеки",
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
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "AU",
                "availableLanguage": "английский"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для работы с PDF для .NET",
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

