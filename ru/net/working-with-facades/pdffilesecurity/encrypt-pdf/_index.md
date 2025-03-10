---
title: Шифрование PDF файла
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/encrypt-pdf-file/
description: Эта тема объясняет, как зашифровать PDF файл с помощью класса PdfFileSecurity.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Encrypt PDF File",
    "alternativeHeadline": "Secure PDF Encryption with C#",
    "abstract": "Узнайте, как повысить безопасность ваших конфиденциальных документов с помощью новой функции шифрования PDF, используя класс PdfFileSecurity. Эта функциональность позволяет защитить ваши PDF файлы паролем, гарантируя, что только авторизованные пользователи могут получить к ним доступ. Изучите различные типы шифрования и алгоритмы, включая AES с длиной ключа до 256 бит, для надежной защиты при обмене файлами и архивировании.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "273",
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
    "url": "/net/encrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/encrypt-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

Шифрование PDF документа защищает его содержимое от несанкционированного доступа извне, особенно во время обмена файлами или архивирования.

Конфиденциальные PDF документы могут быть зашифрованы и защищены паролем. Только пользователи, знающие пароль, смогут расшифровать, открыть и просмотреть эти документы.

Давайте рассмотрим, как работает шифрование PDF с библиотекой Aspose.PDF.

## Шифрование PDF файла с использованием различных типов шифрования и алгоритмов

Чтобы зашифровать PDF файл, вам нужно создать объект [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) и затем вызвать метод [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). Вы можете передать пароль пользователя, пароль владельца и привилегии в метод [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile). Вам также нужно передать значения KeySize и Algorithm в этот метод.

Просмотрите возможный список таких [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm):

|**Имя члена**|**Значение**|**Описание**|
| :- | :- | :- |
|RC4x40|0|RC4 с длиной ключа 40.|
|RC4x128|1|RC4 с длиной ключа 128.|
|AESx128|2|AES с длиной ключа 128.|
|AESx256|3|AES с длиной ключа 256.|

Следующий фрагмент кода показывает, как зашифровать PDF файл.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EncryptPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "input.pdf");
        // Encrypt file using 256-bit encryption
        fileSecurity.EncryptFile("User_P@ssw0rd", "OwnerP@ssw0rd", Aspose.Pdf.Facades.DocumentPrivilege.Print, Aspose.Pdf.Facades.KeySize.x256,
            Aspose.Pdf.Facades.Algorithm.AES);
        // Save PDF document
        fileSecurity.Save(dataDir + "SampleEncrypted_out.pdf");
    }
}
```