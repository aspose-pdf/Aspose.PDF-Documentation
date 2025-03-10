---
title: Дешифровка PDF файла
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/decrypt-pdf-file/
description: Изучите методы дешифровки PDF файлов с защитой паролем в .NET, обеспечивая доступ к содержимому документа с помощью Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Decrypt PDF File",
    "alternativeHeadline": "Unlock Encrypted PDFs with Ease Using PdfFileSecurity",
    "abstract": "Легко разблокируйте ваши PDF документы с помощью новой функции Дешифровка PDF файла, используя класс PdfFileSecurity. Эта функциональность позволяет пользователям удалять защиту паролем из зашифрованных PDF, обеспечивая беспрепятственный доступ и манипуляцию документом. Испытайте простой подход к управлению документами, используя мощный метод DecryptFile для безопасной работы с PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "235",
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
    "url": "/net/decrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/decrypt-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

PDF документ, зашифрованный паролем или сертификатом, должен быть разблокирован перед выполнением другой операции с ним. Если вы попытаетесь выполнить операцию с зашифрованным PDF документом, будет выброшено исключение. После разблокировки зашифрованного PDF вы можете выполнить одну или несколько операций с ним.

## Дешифровка PDF файла с использованием пароля владельца

{{% alert color="primary" %}}
Попробуйте онлайн <br>
Вы можете попробовать разблокировать документ с помощью Aspose.PDF и получить результаты онлайн по этой ссылке:
[products.aspose.app/pdf/unlock](https://products.aspose.app/pdf/unlock)

{{% /alert %}}

Чтобы дешифровать PDF файл, вам нужно создать объект [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) и затем вызвать метод [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile). Вам также нужно передать пароль владельца в метод [DecryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile). Следующий фрагмент кода показывает, как дешифровать PDF файл.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecryptPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample_encrypted.pdf"))
    {
        if (pdfFileInfo.IsEncrypted)
        {
            using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
            {
                // Bind PDF document
                fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
                // Decrypt PDF document
                fileSecurity.DecryptFile("P@ssw0rd");
                // Save PDF document
                fileSecurity.Save(dataDir + "SampleDecrtypted_out.pdf");
            }
        }
    }
}
```