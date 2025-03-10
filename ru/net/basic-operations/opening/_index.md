---
title: Открытие PDF-документа программным способом
linktitle: Открыть PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/open-pdf-document/
description: Узнайте, как открыть PDF-файл в библиотеке C# Aspose.PDF for .NET. Вы можете открыть существующий PDF-документ, документ из потока и зашифрованный PDF-документ.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Open PDF document programmatically",
    "alternativeHeadline": "Programmatically Open and Access Various PDF Documents with C#",
    "abstract": "Откройте PDF-документы с помощью библиотеки Aspose.PDF для .NET. Эта функция позволяет разработчикам беспрепятственно получать доступ к существующим PDF-файлам, загружать документы из потоков и легко работать с зашифрованными файлами, повышая эффективность рабочего процесса и расширяя возможности работы с PDF в C#.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "238",
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
    "url": "/net/open-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/open-pdf-document/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## Открытие существующего PDF-документа

Существует несколько способов открытия документа. Самый простой — указать имя файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OpenDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "tourguidev2_gb_tags.pdf"))
    {
        Console.WriteLine("Pages " + document.Pages.Count);
    }
}
```

## Открытие существующего PDF-документа из потока

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OpenDocumentStream()
{
    var fileName = "SJPR0033_Folder_Utland_16sid_ENG_web3.pdf";
    var remoteUri = "https://www.sj.se/content/dam/SJ/pdf/Engelska/";
    // Create a new WebClient instance
    var webClient = new System.Net.WebClient();
    // Concatenate the domain with the Web resource filename
    var strWebResource = remoteUri + fileName;
    Console.WriteLine("Downloading File \"{0}\" from \"{1}\" .......\n\n", fileName, strWebResource);

    var stream = new MemoryStream();
    webClient.OpenRead(strWebResource)?.CopyTo(stream);

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(stream))
    {
        Console.WriteLine("Pages " + document.Pages.Count);
    }
}
```

## Открытие зашифрованного PDF-документа

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OpenDocumentWithPassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

    const string password = "Aspose2020";
    try
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "DocSite.pdf", password))
        {
            Console.WriteLine("Pages " + document.Pages.Count);
        }
    }
    catch (Aspose.Pdf.InvalidPasswordException e)
    {
        Console.WriteLine(e);
    }
}
```