---
title: 加密 PDF 文件
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/encrypt-pdf-file/
description: 本主题解释如何使用 PdfFileSecurity 类加密 PDF 文件。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Encrypt PDF File",
    "alternativeHeadline": "Secure PDF Encryption with C#",
    "abstract": "了解如何使用 PdfFileSecurity 类通过新的 PDF 加密功能增强敏感文档的安全性。此功能允许您为 PDF 文件设置密码保护，确保只有授权用户才能访问它们。探索各种加密类型和算法，包括 AES，密钥长度可达 256 位，以在文件共享和归档期间提供强大的保护。",
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
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

加密 PDF 文档可以保护其内容不被未经授权的外部访问，特别是在文件共享或归档期间。

机密 PDF 文档可以被加密并设置密码保护。只有知道密码的用户才能解密、打开和查看这些文档。

让我们看看 Aspose.PDF 库中的 PDF 加密是如何工作的。

## 使用不同的加密类型和算法加密 PDF 文件

为了加密 PDF 文件，您需要创建 [PdfFileSecurity](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity) 对象，然后调用 [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile) 方法。您可以将用户密码、所有者密码和权限传递给 [EncryptFile](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile) 方法。您还需要将 KeySize 和 Algorithm 值传递给此方法。

查看可能的 [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm) 列表：

|**成员名称**|**值**|**描述**|
| :- | :- | :- |
|RC4x40|0|密钥长度为 40 的 RC4。|
|RC4x128|1|密钥长度为 128 的 RC4。|
|AESx128|2|密钥长度为 128 的 AES。|
|AESx256|3|密钥长度为 256 的 AES。|

以下代码片段演示了如何加密 PDF 文件。

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