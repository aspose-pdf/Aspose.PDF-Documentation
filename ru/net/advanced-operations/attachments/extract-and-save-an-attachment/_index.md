---
title: Извлечение и сохранение вложения
linktitle: Извлечение и сохранение вложения
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/extract-and-save-an-attachment/
description: Aspose.PDF for .NET позволяет вам получить все вложения из PDF-документа. Также вы можете получить отдельное вложение из вашего документа.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract and Save an Attachment",
    "alternativeHeadline": "Extract Attachments from PDF Documents with Ease",
    "abstract": "Aspose.PDF для .NET представляет собой мощную функцию, которая позволяет пользователям легко извлекать и сохранять вложения из PDF-документов. Эта функциональность позволяет получать все встроенные файлы или определённые вложения, улучшая управление документами и доступность для разработчиков, работающих с PDF-файлами. Оптимизируйте свои рабочие процессы с PDF-документами, без труда обрабатывая вложения с помощью этого инновационного инструмента.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "extract attachments, save attachments, Aspose.PDF for .NET, PDF document, individual attachment, embedded files collection, FileSpecification object, PDF manipulation, document instance, get all attachments",
    "wordcount": "604",
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
    "url": "/net/extract-and-save-an-attachment/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-and-save-an-attachment/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF для .NET позволяет получить все вложения из PDF-документа. Также вы можете получить отдельное вложение из вашего документа."
}
</script>

## Получение всех вложений

С Aspose.PDF можно получить все вложения из PDF-документа. Это полезно, когда вы хотите сохранить документы отдельно от PDF или удалить из PDF все вложения.

Чтобы получить все вложения из файла PDF:

1. Пройдитесь по коллекции [EmbeddedFiles](https://reference.aspose.com/pdf/ru/net/aspose.pdf/embeddedfilecollection) объекта [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document). Коллекция [EmbeddedFiles](https://reference.aspose.com/pdf/ru/net/aspose.pdf/embeddedfilecollection) содержит все вложения. Каждая итерация цикла foreach по коллекции [EmbeddedFiles](https://reference.aspose.com/pdf/ru/net/aspose.pdf/embeddedfilecollection) возвращает объект [FileSpecification](https://reference.aspose.com/pdf/ru/net/aspose.pdf/filespecification).
1. Как только объект станет доступен, извлеките либо все свойства прикреплённого файла, либо сам файл.

Следующие фрагменты кода показывают, как получить все вложения из PDF-документа.

Эти фрагменты кода также работают с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAllAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetAlltheAttachments.pdf"))
    {
        // Get embedded files collection
        Aspose.Pdf.EmbeddedFileCollection embeddedFiles = document.EmbeddedFiles;

        // Get count of the embedded files
        Console.WriteLine("Total files : {0}", embeddedFiles.Count);

        int count = 1;

        // Loop through the collection to get all the attachments
        foreach (Aspose.Pdf.FileSpecification fileSpecification in embeddedFiles)
        {
            Console.WriteLine("Name: {0}", fileSpecification.Name);
            Console.WriteLine("Description: {0}",
            fileSpecification.Description);
            Console.WriteLine("Mime Type: {0}", fileSpecification.MIMEType);

            // Check if parameter object contains the parameters
            if (fileSpecification.Params != null)
            {
                Console.WriteLine("CheckSum: {0}",
                fileSpecification.Params.CheckSum);
                Console.WriteLine("Creation Date: {0}",
                fileSpecification.Params.CreationDate);
                Console.WriteLine("Modification Date: {0}",
                fileSpecification.Params.ModDate);
                Console.WriteLine("Size: {0}", fileSpecification.Params.Size);
            }

            // Get the attachment and write to file or stream
            byte[] fileContent = new byte[fileSpecification.Contents.Length];
            fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);
            using (FileStream fileStream = new FileStream(dataDir + count + "_out" + ".txt", FileMode.Create))
            {
                fileStream.Write(fileContent, 0, fileContent.Length);
            }
            count += 1;
        }
    }
}
```

## Получение отдельного вложения

Чтобы получить отдельное вложение, мы можем указать индекс вложения в объекте EmbeddedFiles экземпляра Document. Попробуйте использовать следующий фрагмент кода.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetIndividualAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetIndividualAttachment.pdf"))
    {
        // Get particular embedded file
        Aspose.Pdf.FileSpecification fileSpecification = document.EmbeddedFiles[1];

        // Get the file properties
        Console.WriteLine("Name: {0}", fileSpecification.Name);
        Console.WriteLine("Description: {0}", fileSpecification.Description);
        Console.WriteLine("Mime Type: {0}", fileSpecification.MIMEType);

        // Check if parameter object contains the parameters
        if (fileSpecification.Params != null)
        {
            Console.WriteLine("CheckSum: {0}",
            fileSpecification.Params.CheckSum);
            Console.WriteLine("Creation Date: {0}",
            fileSpecification.Params.CreationDate);
            Console.WriteLine("Modification Date: {0}",
            fileSpecification.Params.ModDate);
            Console.WriteLine("Size: {0}", fileSpecification.Params.Size);
        }

        // Get the attachment and write to file or stream
        byte[] fileContent = new byte[fileSpecification.Contents.Length];
        fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);

        using (FileStream fileStream = new FileStream(dataDir + "test_out" + ".txt", FileMode.Create))
        {
            fileStream.Write(fileContent, 0, fileContent.Length);
        }
    }
}
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