---
title: 设置 PDF 权限
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /zh/net/set-privileges/
description: 了解如何在 PDF 文件中修改用户权限，使用 Aspose.PDF 在 .NET 中限制某些操作。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Privileges on PDF",
    "alternativeHeadline": "Set Custom Permissions for PDF Document Security",
    "abstract": "介绍使用 PdfFileSecurity 类在现有 PDF 文件上设置权限的新功能，允许用户指定打印和复制等操作的权限。此外，用户现在可以轻松地从 PDF 文档中删除扩展权限，从而确保对文档修改和安全性的更大控制。此功能简化了 PDF 管理，同时增强了安全合规性。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "436",
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
    "url": "/net/set-privileges/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-privileges/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 在现有 PDF 文件上设置权限

要设置 PDF 文件的权限，请创建一个 [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) 对象并调用 SetPrivilege 方法。您可以使用 DocumentPrivilege 对象指定权限，然后将此对象传递给 SetPrivilege 方法。以下代码片段演示了如何设置 PDF 文件的权限。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrivilege1()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Create DocumentPrivileges object and set needed privileges
    var privilege = Aspose.Pdf.Facades.DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample.pdf");
        // Set privilege
        fileSecurity.SetPrivilege(privilege);
        // Save PDF document
        fileSecurity.Save(dataDir + "SamplePrivileges_out.pdf");
    }
}
```

请参见以下方法并指定密码：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrivilegeWithPassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Create DocumentPrivileges object and set needed privileges
    var privilege = Aspose.Pdf.Facades.DocumentPrivilege.ForbidAll;
    privilege.ChangeAllowLevel = 1;
    privilege.AllowPrint = true;
    privilege.AllowCopy = true;

    using (var fileSecurity = new Aspose.Pdf.Facades.PdfFileSecurity())
    {
        // Bind PDF document
        fileSecurity.BindPdf(dataDir + "sample.pdf");
        // Set privilege and passwords
        fileSecurity.SetPrivilege(string.Empty, "P@ssw0rd", privilege);
        // Save PDF document
        fileSecurity.Save(dataDir + "SamplePrivilegesPassword_out.pdf");
    }
}
```

## 从 PDF 中移除扩展权限功能

PDF 文档支持扩展权限功能，以便最终用户使用 Adobe Acrobat Reader 填写表单字段，然后保存填写后的表单副本。然而，它确保 PDF 文件未被修改，如果对 PDF 的结构进行任何修改，扩展权限功能将丢失。查看此类文档时，会显示错误消息，指出由于文档已被修改，扩展权限已被移除。最近，我们收到了一个要求，从 PDF 文档中移除扩展权限。

要从 PDF 文件中移除扩展权限，PdfFileSignature 类中添加了一个名为 RemoveUsageRights() 的新方法。另一个名为 ContainsUsageRights() 的方法被添加以确定源 PDF 是否包含扩展权限。

{{% alert color="primary" %}}
从 Aspose.PDF for .NET 9.5.0 开始，以下方法的名称已更新。请注意，之前的方法仍在 API 中，但已被标记为过时，并将被移除。因此，建议尝试使用更新的方法。

- IsContainSignature(.) 方法已重命名为 ContainsSignature(..)。
- IsCoversWholeDocument(..) 方法已重命名为 CoversWholeDocument(..)。
{{% /alert %}}

以下代码演示了如何从文档中移除使用权限：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void RemoveExtendedRights()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_SecuritySignatures();
    
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "DigitallySign.pdf");
        if (pdfSign.ContainsUsageRights())
        {
            pdfSign.RemoveUsageRights();
        }
        // Save PDF document
        pdfSign.Document.Save(dataDir + "RemoveRights_out.pdf");
    }
}
```