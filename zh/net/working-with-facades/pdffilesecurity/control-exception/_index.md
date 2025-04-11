---
title: 控制异常 PDF 文件
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /zh/net/control-exception/
description: 了解如何处理 PDF 处理中的异常，并在使用 Aspose.PDF 在 .NET 中处理 PDF 时确保顺利操作。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Control Exception PDF File",
    "alternativeHeadline": "Manage PDF Exception Handling with New Security Control",
    "abstract": "PdfFileSecurity 类中的控制异常功能允许您通过切换 AllowExceptions 属性来管理解密 PDF 文件时的错误处理。用户可以选择接收布尔结果以判断解密是否成功，或利用 try-catch 块进行全面的异常管理，从而增强对 PDF 安全操作的灵活性和控制。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "224",
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
    "url": "/net/control-exception/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/control-exception/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

[PdfFileSecurity](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilesecurity) 类允许您控制异常。为此，您需要将 [AllowExceptions](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) 属性设置为 false 或 true。如果您将操作设置为 false，则 [DecryptFile](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilesecurity/methods/decryptfile) 的结果将根据密码的正确性返回 true 或 false。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ControlExceptionPDFFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
        // Disallow exceptions
        fileSecurity.AllowExceptions = false;
        
        // Decrypt PDF document
        if (!fileSecurity.DecryptFile("IncorrectPassword"))
        {
            Console.WriteLine("Something wrong...");
            Console.WriteLine($"Last exception: {fileSecurity.LastException.Message}");
        }
        // Save PDF document
        fileSecurity.Save(dataDir + "SampleDecrtypted_out.pdf");
    }
}
```

如果您将 [AllowExceptions](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilesecurity/properties/allowexceptions) 属性设置为 true，则可以使用 try-catch 操作符获取操作的结果。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ControlExceptionPDFFile2()
{   
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
        // Allow exceptions
        fileSecurity.AllowExceptions = true;
        try
        {
            // Decrypt PDF document
            fileSecurity.DecryptFile("IncorrectPassword");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Something wrong...");
            Console.WriteLine($"Exception: {ex.Message}");
        }
        // Save PDF document
        fileSecurity.Save(dataDir + "SampleDecrtypted_out.pdf");
    }
}
```