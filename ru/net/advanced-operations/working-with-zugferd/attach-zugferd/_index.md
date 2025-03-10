---
title: Создание PDF-документа, соответствующего стандарту PDF/3-A, и прикрепление счёта ZUGFeRD на C#
linktitle: Прикрепление ZUGFeRD к PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/attach-zugferd/
description: Узнайте, как создать PDF-документ с использованием ZUGFeRD на Aspose.PDF for .NET
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating PDF/3-A compliant PDF and attaching ZUGFeRD invoice in C#",
    "alternativeHeadline": "Attach ZUGFeRD Invoices to PDF in C#",
    "abstract": "Откройте для себя новую функциональность, которая позволяет разработчикам создавать PDF-документы, соответствующие стандарту PDF/A-3B, и легко прикреплять счета ZUGFeRD с помощью C#. Эта функция упрощает процесс встраивания метаданных счёта в PDF-файлы, обеспечивая долгосрочное хранение документов и соответствие стандартам электронного выставления счетов",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "429",
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
    "url": "/net/attach-zugferd/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/attach-zugferd/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и лёгкие задачи, но и справляться с более сложными целями. Ознакомьтесь со следующим разделом для опытных пользователей и разработчиков."
}
</script>

## Прикрепление ZUGFeRD к PDF

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

Мы рекомендуем выполнить следующие шаги для прикрепления ZUGFeRD к PDF:

* Определите переменную пути, указывающую на папку, в которой находятся входной и выходной PDF-файлы.
* Создайте объект документа, загрузив существующий PDF-файл (например, «ZUGFeRD-test.pdf») из пути.
* Создайте объект [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification/) указав путь и описание другого файла с именем «factur-x.xml», который содержит метаданные счёта, соответствующие стандарту ZUGFeRD.
* Добавьте свойства к объекту спецификации файла, такие как описание, тип MIME и отношение AF. Отношение AF указывает, как встроенный файл связан с PDF-документом. В этом случае оно установлено на «Альтернативный», что означает, что встроенный файл является альтернативным представлением содержимого PDF.
* Добавьте объект спецификации файла в коллекцию встроенных файлов документа. Имя файла должно соответствовать стандарту ZUGFeRD, например, «factur-x.xml».
* Преобразуйте документ в формат PDF/A-3B, подмножество PDF, обеспечивающее долгосрочное сохранение электронных документов. PDF/A-3B позволяет встраивать файлы любого формата в PDF-документы.
* Сохраните преобразованный документ как новый PDF-файл (например, «ZUGFeRD-res.pdf»).

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AttachZUGFeRD()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ZUGFeRD-testInput.pdf"))
    {
        // Setup new file to be added as attachment
        var description = "Invoice metadata conforming to ZUGFeRD standard";
        var fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "ZUGFeRD-testXmlInput.xml", description)
        {
            Description = "Zugferd",
            MIMEType = "text/xml",
            Name = "factur-x.xml"
        };
        // Add attachment to document's attachment collection
        document.EmbeddedFiles.Add(fileSpecification);
        document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.ZUGFeRD, Aspose.Pdf.ConvertErrorAction.Delete);
        // Save PDF document
        document.Save(dataDir + "AttachZUGFeRD_out.pdf");
    }
}
```

Метод convert принимает поток, формат PDF и действие при ошибке преобразования в качестве параметров. Параметр потока можно использовать для сохранения журнала преобразования. Параметр действия при ошибке преобразования определяет, что делать, если во время преобразования возникают какие-либо ошибки. В этом случае для него установлено значение «Удалить», что означает удаление из документа любых элементов, не соответствующих формату PDF/A-3B.