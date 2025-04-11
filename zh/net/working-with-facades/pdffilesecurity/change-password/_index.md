---
title: 更改 PDF 文件的密码
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /zh/net/change-password/
description: 探索如何在 .NET 中修改 PDF 文档的密码，以提高文件安全性，使用 Aspose.PDF。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Change Password of PDF File",
    "alternativeHeadline": "Securely Change PDF Passwords with Ease",
    "abstract": "通过使用 PdfFileSecurity 类轻松增强您的 PDF 安全性。此功能允许用户修改用户和所有者密码，确保有效管理权限的同时，提供对未授权访问的强大保护。通过简单的实现，轻松优化您的文档安全设置。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "250",
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
    "url": "/net/change-password/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/change-password/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 更改 PDF 文件的密码

为了更改 PDF 文件的密码，您需要创建 [PdfFileSecurity](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdffilesecurity) 对象，然后调用 [ChangePassword](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2) 方法。您需要将现有的所有者密码和新的用户及所有者密码传递给 [ChangePassword](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.pdffilesecurity/changepassword/methods/2) 方法。

{{% alert color="primary" %}}

- **用户密码**（如果设置）是您需要提供以打开 PDF 的密码。Acrobat/Reader 会提示用户输入用户密码。如果不正确，文档将无法打开。
- **所有者密码**（如果设置）控制权限，例如打印、编辑、提取、评论等。Acrobat/Reader 将根据权限设置禁止这些操作。如果您想设置/更改权限，Acrobat 将需要此密码。

{{% /alert %}}

以下代码片段向您展示如何更改 PDF 文件的密码。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdfFileInfo = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "sample_encrypted.pdf"))
    {
        // Create PdfFileSecurity object if the document is encrypted
        if (pdfFileInfo.IsEncrypted)    
        {
            using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
            {
                // Bind PDF document
                fileSecurity.BindPdf(dataDir + "sample_encrypted.pdf");
                fileSecurity.ChangePassword("OwnerP@ssw0rd", "Pa$$w0rd1", "Pa$$w0rd2", Aspose.Pdf.Facades.DocumentPrivilege.Print, Aspose.Pdf.Facades.KeySize.x256);
                // Save PDF document
                fileSecurity.Save(dataDir + "sample_encrtypted1.pdf");
            }
        }
    }
}
```