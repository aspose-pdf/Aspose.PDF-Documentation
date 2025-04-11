---
title: 在 PDF 文件中使用签名
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /zh/net/working-with-signature-in-a-pdf-file/
description: 本节解释如何使用 PdfFileSignature 类提取签名信息、从签名中提取图像、改变语言等。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Signature in PDF File",
    "alternativeHeadline": "Extract Signature Details and Images from PDFs",
    "abstract": "Aspose.PDF for .NET 中的新功能通过允许用户使用 PdfFileSignature 类提取签名信息和图像来增强 PDF 文档的安全性。此功能还包括自定义数字签名、抑制特定信息（如位置和原因）以及更改签名文本的语言设置，提供了一整套高效管理 PDF 签名的工具。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "878",
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
    "url": "/net/working-with-signature-in-a-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-signature-in-a-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

## 如何提取签名信息

Aspose.PDF for .NET 支持使用 PdfFileSignature 类对 PDF 文件进行数字签名的功能。目前，还可以确定证书的有效性，但我们无法提取整个证书。可以提取的信息包括公钥、指纹和颁发者等。

为了提取签名信息，我们在 PdfFileSignature 类中引入了 ExtractCertificate(..) 方法。请查看以下代码片段，演示如何从 PdfFileSignature 对象中提取证书的步骤：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSignatureInfo()
{ 
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        // Get list of signature names
        var sigNames = pdfFileSignature.GetSignatureNames();
        if (sigNames.Count > 0)
        {
            SignatureName sigName = sigNames[0];            
            // Extract signature certificate
            Stream cerStream = pdfFileSignature.ExtractCertificate(sigName);
            if (cerStream != null)
            {
                using (cerStream)
                {
                    using (FileStream fs = new FileStream(dataDir + "extracted_cert.pfx", FileMode.CreateNew))
                    {
                        cerStream.CopyTo(fs);
                    }
                }
            }
            
        }
    }
}
```

## 从签名字段提取图像 (PdfFileSignature)

Aspose.PDF for .NET 支持使用 PdfFileSignature 类对 PDF 文件进行数字签名，并且在签署文档时，您还可以为 SignatureAppearance 设置图像。现在此 API 还提供提取签名信息以及与签名字段相关的图像的能力。

为了提取签名信息，我们在 PdfFileSignature 类中引入了 ExtractImage(..) 方法。请查看以下代码片段，演示如何从 PdfFileSignature 对象中提取图像的步骤：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSignatureImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var signature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        signature.BindPdf(dataDir + "ExtractingImage.pdf");

        if (signature.ContainsSignature())
        {
            // Get list of signature names
            foreach (string sigName in signature.GetSignatureNames())
            {                
                // Extract signature image
                using (Stream imageStream = signature.ExtractImage(sigName))
                {
                    if (imageStream != null)
                    {
                        imageStream.Position = 0;
                        using (FileStream fs = new FileStream(dataDir + "ExtractImages_out.jpg", FileMode.OpenOrCreate))
                        {
                            imageStream.CopyTo(fs);
                        }
                    }
                }
            }
        }
    }
}
```

## 抑制位置和原因

Aspose.PDF 功能允许灵活配置数字签名实例。[PdfFileSignature](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilesignature) 类提供对 PDF 文件进行签名的能力。签名方法的实现允许对 PDF 进行签名并将特定的签名对象传递给此类。签名方法包含一组属性，用于自定义输出数字签名。如果您需要从结果签名中抑制某些文本属性，可以将它们留空。以下代码片段演示如何从签名块中抑制位置和原因两行：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SupressLocationReason()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
        // Set signature appearance
        pdfFileSignature.SignatureAppearance = dataDir + "aspose-logo.png";

        // Create any of the three signature types
        var signature = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdfFileSignature.Sign(1, string.Empty, "test01@aspose-pdf-demo.local", string.Empty, true, rect, signature);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

## 数字签名的自定义功能

Aspose.PDF for .NET 允许数字签名的自定义功能。[SignatureCustomAppearance](https://reference.aspose.com/pdf/zh/net/aspose.pdf.forms/signaturecustomappearance) 类的签名方法实现了 6 个重载，以便于您的使用。例如，您可以仅通过 SignatureCustomAppearance 类实例及其属性值来配置结果签名。以下代码片段演示如何从 PDF 的输出数字签名中隐藏“数字签名由”标题。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomizationFeaturesForDigitalSign()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);

        // Create any of the three signature types
        var signature = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1
        // Create signature appearance
        var signatureCustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
        {
            FontSize = 6,
            FontFamilyName = "Times New Roman",
            DigitalSignedLabel = "Signed by:"
        };
        // Set signature appearance
        signature.CustomAppearance = signatureCustomAppearance;

        pdfFileSignature.Sign(1, true, rect, signature);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

## 更改数字签名文本中的语言

使用 Aspose.PDF for .NET API，您可以使用以下三种类型的签名之一对 PDF 文件进行签名：

- PKCS#1。
- PKCS#7。
- PKCS#12。

每种提供的签名都包含一组为您的方便而实现的配置属性（本地化、日期时间格式、字体系列等）。[SignatureCustomAppearance](https://reference.aspose.com/pdf/zh/net/aspose.pdf.forms/signaturecustomappearance) 类提供相应的功能。以下代码片段演示如何更改数字签名文本中的语言：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangeLanguageInDigitalSignText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();   
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");
        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);

        // Create any of the three signature types
        var pkcs = new Aspose.Pdf.Forms.PKCS7(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Pruebas Firma",
            ContactInfo = "Contacto Pruebas",
            Location = "Población (Provincia)",
            Date = DateTime.Now
        };
        
        var signatureCustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
        {
            DateSignedAtLabel = "Fecha",
            DigitalSignedLabel = "Digitalmente firmado por",
            ReasonLabel = "Razón",
            LocationLabel = "Localización",
            FontFamilyName = "Arial",
            FontSize = 10d,
            Culture = System.Globalization.CultureInfo.InvariantCulture,
            DateTimeFormat = "yyyy.MM.dd HH:mm:ss"
        };
        // Set signature appearance
        pkcs.CustomAppearance = signatureCustomAppearance;
        // Sign the PDF file
        pdfFileSignature.Sign(1, true, rect, pkcs);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```