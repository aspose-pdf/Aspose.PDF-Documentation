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
    "abstract": "Aspose.PDF for .NET представляет собой мощную функцию, которая позволяет пользователям без труда извлекать и сохранять вложения из PDF-документов. Эта функциональность позволяет извлекать все встроенные файлы или конкретные вложения, улучшая управление документами и доступность для разработчиков, работающих с PDF-файлами. Оптимизируйте свои рабочие процессы с PDF, без усилий обрабатывая вложения с помощью этого инновационного инструмента",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "extract attachments, save attachments, Aspose.PDF for .NET, PDF document, individual attachment, embedded files collection, FileSpecification object, PDF manipulation, document instance, get all attachments",
    "wordcount": "1169",
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
    "dateModified": "2025-04-02",
    "description": "Aspose.PDF for .NET позволяет вам получить все вложения из PDF-документа. Также вы можете получить отдельное вложение из вашего документа."
}
</script>

## Получить все вложения

С помощью Aspose.PDF можно получить все вложения из PDF-документа. Это полезно, когда вы хотите сохранить документы отдельно от PDF или если вам нужно удалить вложения из PDF.

Чтобы получить все вложения из PDF-файла:

1. Пройдите по коллекции [EmbeddedFiles](https://reference.aspose.com/pdf/ru/net/aspose.pdf/embeddedfilecollection) объекта [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document). Коллекция [EmbeddedFiles](https://reference.aspose.com/pdf/ru/net/aspose.pdf/embeddedfilecollection) содержит все вложения. Каждый элемент этой коллекции представляет собой объект [FileSpecification](https://reference.aspose.com/pdf/ru/net/aspose.pdf/filespecification). Каждая итерация цикла foreach по коллекции [EmbeddedFiles](https://reference.aspose.com/pdf/ru/net/aspose.pdf/embeddedfilecollection) возвращает объект [FileSpecification](https://reference.aspose.com/pdf/ru/net/aspose.pdf/filespecification).
1. Как только объект доступен, получите либо все свойства прикрепленного файла, либо сам файл.

Следующие фрагменты кода показывают, как получить все вложения из PDF-документа.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

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
            var fileContent = new byte[fileSpecification.Contents.Length];
            fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);
            using (var fileStream = new FileStream(dataDir + count + "_out" + ".txt", FileMode.Create))
            {
                fileStream.Write(fileContent, 0, fileContent.Length);
            }
            count += 1;
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAllAttachments()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "GetAlltheAttachments.pdf");

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
        var fileContent = new byte[fileSpecification.Contents.Length];
        fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);
        using var fileStream = new FileStream(dataDir + count + "_out" + ".txt", FileMode.Create);
        fileStream.Write(fileContent, 0, fileContent.Length);

        count += 1;
    }
}
```
{{< /tab >}}
{{< /tabs >}}


## Получить отдельное вложение

Чтобы получить отдельное вложение, мы можем указать индекс вложения в объекте `EmbeddedFiles` экземпляра документа. Пожалуйста, попробуйте использовать следующий фрагмент кода.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

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
        var fileContent = new byte[fileSpecification.Contents.Length];
        fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);

        using (var fileStream = new FileStream(dataDir + "test_out" + ".txt", FileMode.Create))
        {
            fileStream.Write(fileContent, 0, fileContent.Length);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetIndividualAttachment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "GetIndividualAttachment.pdf");

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
    var fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);

    using var fileStream = new FileStream(dataDir + "test_out" + ".txt", FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
}
```
{{< /tab >}}
{{< /tabs >}}


## Получить вложения, содержащиеся в объектах FileAttachmentAnnotation

В дополнение к коллекции EmbeddedFiles объекта Document, вложения также могут содержаться в объектах FileAttachmentAnnotation. Ниже приведен код для просмотра количества и деталей таких вложений.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ViewAttachmentsInFileAttachmentAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetAlltheAttachments.pdf"))
    {
        for (int i = 1; i <= document.Pages.Count; i++)
        {
            foreach (Aspose.Pdf.Annotations.Annotation annotation in document.Pages[i].Annotations)
            {
                var fileAttachmentAnnotation = annotation as Aspose.Pdf.Annotations.FileAttachmentAnnotation;
                if (fileAttachmentAnnotation != null)
                {
                    Aspose.Pdf.FileSpecification file = fileAttachmentAnnotation.File;
                    if (file != null && file.Name != null)
                    {
                        Console.WriteLine($"Name: {file.Name} on page {i}");
                    }
                }
            }
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ViewAttachmentsInFileAttachmentAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Attachments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "GetAlltheAttachments.pdf");

    for (int i = 1; i <= document.Pages.Count; i++)
    {
        foreach (Aspose.Pdf.Annotations.Annotation annotation in document.Pages[i].Annotations)
        {
            var fileAttachmentAnnotation = annotation as Aspose.Pdf.Annotations.FileAttachmentAnnotation;
            if (fileAttachmentAnnotation != null)
            {
                Aspose.Pdf.FileSpecification file = fileAttachmentAnnotation.File;
                if (file != null && file.Name != null)
                {
                    Console.WriteLine($"Name: {file.Name} on page {i}");
                }
            }
        }
    }
}
```
{{< /tab >}}
{{< /tabs >}}


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