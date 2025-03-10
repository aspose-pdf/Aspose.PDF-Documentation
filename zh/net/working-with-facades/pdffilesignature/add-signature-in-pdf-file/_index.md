---
title: 在 PDF 文件中添加签名
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/add-signature-in-pdf/
description: 本节解释如何使用 PdfFileSignature 类向 PDF 文件添加签名。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Signature in PDF File",
    "alternativeHeadline": "Add Custom Digital Signatures to PDF Files",
    "abstract": "通过使用 PdfFileSignature 类增强您的 PDF 文档，新增添加数字签名的功能。此功能允许用户应用多种签名类型，包括 PKCS#1、PKCS#7 和 PKCS#7Detached，同时可以使用图像和特定属性自定义签名外观。通过轻松在不同页面上合并多个签名，简化您的文档验证过程。",
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
    "description": "Aspose.PDF 不仅可以执行简单易行的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发者的信息。"
}
</script>

## 在 PDF 文件中添加数字签名

[PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 类允许您在 PDF 文件中添加签名。您需要使用输入和输出 PDF 文件创建 [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 类的对象。您还需要创建一个 [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) 对象，以指定您希望添加签名的位置，并且为了设置外观，您可以使用 [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 对象的 [SignatureAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/signatureappearance) 属性指定图像。Aspose.Pdf.Facades 还提供不同类型的签名，如 PKCS#1、PKCS#7 和 PKCS#7Detached。为了创建特定类型的签名，您需要使用证书文件和密码创建特定类的对象，如 **PKCS1**、**PKCS7** 或 **PKCS7Detached**。

一旦创建了特定签名类型的对象，您可以使用 [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 类的 [Sign](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/sign/index) 方法对 PDF 进行签名，并将特定签名对象传递给该类。您还可以为此方法指定其他属性。最后，您需要使用 [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 类的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) 方法保存签名后的 PDF。以下代码片段向您展示了如何在 PDF 文件中添加签名。

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

以下代码示例展示了用两个签名签署文档的能力。在我们的示例中，我们将第一个签名放在第一页，第二个签名放在第二页。您可以指定所需的页面。

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

对于需要签名的表单或 acroforms 文档，请参见以下示例。
您需要使用输入和输出 PDF 文件创建 [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 类的对象。使用 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilesignature/bindpdf/methods/1) 进行绑定。创建一个签名，并能够添加所需的属性。在我们的示例中，它们是 'Reason' 和 'CustomAppearance'。

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

如果我们的文档有两个字段，签署它的算法与第一个示例类似。

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