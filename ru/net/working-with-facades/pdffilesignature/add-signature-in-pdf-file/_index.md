---
title: Добавить подпись в PDF файл
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/add-signature-in-pdf/
description: Этот раздел объясняет, как добавить подпись в PDF файл с помощью класса PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Signature in PDF File",
    "alternativeHeadline": "Add Custom Digital Signatures to PDF Files",
    "abstract": "Улучшите свои PDF документы с новой возможностью добавления цифровых подписей с помощью класса PdfFileSignature. Эта функция позволяет пользователям применять различные типы подписей, включая PKCS#1, PKCS#7 и PKCS#7Detached, при этом настраивая внешний вид подписи с помощью изображений и конкретных атрибутов. Упрощайте процесс проверки документов, включая несколько подписей на разных страницах с легкостью.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "838",
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
    "url": "/net/add-signature-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-signature-in-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Добавить цифровую подпись в PDF файл

[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) класс позволяет вам добавлять подпись в PDF файл. Вам нужно создать объект класса [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) с использованием входных и выходных PDF файлов. Вам также нужно создать объект [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle), в который вы хотите добавить подпись, и для настройки внешнего вида вы можете указать изображение, используя свойство [SignatureAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/signatureappearance) объекта [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). Aspose.Pdf.Facades также предоставляет различные виды подписей, такие как PKCS#1, PKCS#7 и PKCS#7Detached. Чтобы создать подпись конкретного типа, вам нужно создать объект определенного класса, такого как **PKCS1**, **PKCS7** или **PKCS7Detached**, используя файл сертификата и пароль.

После создания объекта конкретного типа подписи вы можете использовать метод [Sign](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/sign/index) класса [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) для подписания PDF и передать конкретный объект подписи в этот класс. Вы также можете указать другие атрибуты для этого метода. Наконец, вам нужно сохранить подписанный PDF, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) класса [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). Следующий фрагмент кода показывает, как добавить подпись в PDF файл.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPdfFileSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
    
        // Set signature appearance
        pdFileSignature.SignatureAppearance = dataDir + "aspose-logo.png";

        // Create any of the three signature types
        var signature = new PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdFileSignature.Sign(1, "I'm document author", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect, signature);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

Следующий пример кода демонстрирует возможность подписания документа с двумя подписями. В нашем примере мы ставим первую подпись на первой странице, а вторую на второй странице. Вы можете указать страницы, которые вам нужны.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTwoSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for 1st signature location
        System.Drawing.Rectangle rect1 = new System.Drawing.Rectangle(10, 10, 300, 50);

        // Create 1st signature object
        var signature1 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdFileSignature.Sign(1, "I'm document author", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect1, signature1);
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");

        // Sign with 2nd signature
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "DigitallySign_out.pdf");

        // Create a rectangle for 2nd signature location
        System.Drawing.Rectangle rect2 = new System.Drawing.Rectangle(10, 10, 300, 50);

        // Create 2nd signature object
        var signature2 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdFileSignature.Sign(2, "I'm document reviewer", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect2, signature2);

        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign2_out.pdf");
    }
}
```

Для документа с формами или акроформами, который необходимо подписать, смотрите следующий пример. Вам нужно создать объект класса [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) с использованием входных и выходных PDF файлов. Используйте [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesignature/bindpdf/methods/1) для связывания. Создайте подпись с возможностью добавления необходимых свойств. В нашем примере это 'Причина' и 'ПользовательскийВид'.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPdfFileSignatureField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "input.pdf");

        // Create any of the three signature types
        var signature = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Sign as Author",
            CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
            {
                FontSize = 6,
                FontFamilyName = "Calibri"
            }
        }; // PKCS#1
        
        pdFileSignature.Sign("Signature1", signature);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

Если в нашем документе есть два поля, алгоритм его подписания аналогичен первому примеру.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPdfFileSignatureField2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");

        // Create any of the three signature types
        var signature1 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Sign as Author",
            CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
            {
                FontSize = 6
            }
        }; // PKCS#1
        pdFileSignature.Sign("Signature1", signature1);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "DigitallySign_out.pdf");

        // Create any of the three signature types
        var signature2 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Sign as Reviwer",
            CustomAppearance = new SignatureCustomAppearance
            {
                FontSize = 6
            }
        }; // PKCS#1
        
        pdFileSignature.Sign("Signature2", signature2);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign2_out.pdf");
    }
}
```