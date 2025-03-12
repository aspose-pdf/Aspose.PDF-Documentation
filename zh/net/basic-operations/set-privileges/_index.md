---
title: 设置权限，加密和解密 PDF
linktitle: 加密和解密 PDF 文件
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /zh/net/set-privileges-encrypt-and-decrypt-pdf-file/
description: 使用不同的加密类型和算法通过 C# 加密 PDF 文件。同时，使用所有者密码解密 PDF 文件。
lastmod: "2024-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Set Privileges, Encrypt and Decrypt PDF",
    "alternativeHeadline": "Set PDF Privileges and Secure with Encryption with C#",
    "abstract": "新功能允许用户使用 C# 高效地加密和解密 PDF 文件，支持多种加密类型和算法。通过利用用户和所有者密码，它提供了对文档访问和权限的强大控制，确保 PDF 内容的机密性和完整性，同时简化了开发人员的安全管理。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1586",
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
    "url": "/net/set-privileges-encrypt-and-decrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-privileges-encrypt-and-decrypt-pdf-file/"
    },
    "dateModified": "2024-11-26",
    "description": "使用不同的加密类型和算法通过 C# 加密 PDF 文件。同时，使用所有者密码解密 PDF 文件。"
}
</script>

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## 在现有 PDF 文件上设置权限

要在 PDF 文件上设置权限，请创建 [DocumentPrivilege](https://reference.aspose.com/pdf/net/aspose.pdf.facades/documentprivilege) 类的对象，并指定要应用于文档的权限。一旦定义了权限，将此对象作为参数传递给 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 对象的 [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) 方法。以下代码片段演示了如何设置 PDF 文件的权限。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrivilegesOnExistingPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Instantiate Document Privileges object
        // Apply restrictions on all privileges
        var documentPrivilege = Aspose.Pdf.Facades.DocumentPrivilege.ForbidAll;
        // Only allow screen reading
        documentPrivilege.AllowScreenReaders = true;
        // Encrypt the file with User and Owner password
        // Need to set the password, so that once the user views the file with user password
        // Only screen reading option is enabled
        document.Encrypt("user", "owner", documentPrivilege, Aspose.Pdf.CryptoAlgorithm.AESx128, false);
        // Save PDF document
        document.Save(dataDir + "SetPrivileges_out.pdf");
    }
}
```

## 使用不同的加密类型和算法加密 PDF 文件

您可以使用 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 对象的 [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) 方法来加密 PDF 文件。您可以将用户密码、所有者密码和权限传递给 [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) 方法。此外，您可以传递 [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm) 枚举的任何值。该枚举提供了不同的加密算法和密钥大小的组合。您可以传递您选择的值。最后，使用 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 对象的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 方法保存加密的 PDF 文件。

>在加密 PDF 文件时，请指定不同的用户和所有者密码。

- **用户密码**，如果设置，则是您打开 PDF 所需提供的密码。Acrobat/Reader 将提示用户输入用户密码。如果不正确，文档将无法打开。
- **所有者密码**，如果设置，则控制权限，例如打印、编辑、提取、评论等。Acrobat/Reader 将根据权限设置禁止这些操作。如果您想设置/更改权限，Acrobat 将要求输入此密码。

以下代码片段演示了如何加密 PDF 文件。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void EncryptPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Encrypt.pdf"))
    {
        // Encrypt PDF
        document.Encrypt("user", "owner", 0, Aspose.Pdf.CryptoAlgorithm.RC4x128);
        // Save PDF document
        document.Save(dataDir + "Encrypt_out.pdf");
    }
}
```

## 使用所有者密码解密 PDF 文件

越来越多的用户正在交换加密的 PDF 文件，以防止未经授权访问文档，例如打印/复制/共享/提取 PDF 文件内容的信息。今天，这是加密 PDF 文件的最佳选择，因为它保持内容的机密性和完整性。
在这方面，需要访问加密的 PDF 文件，因为这种访问只能由授权用户获得。此外，人们正在寻找各种解决方案来解密 PDF 文件。

最好通过使用 Aspose.PDF 库一次性解决此问题。

要解密 PDF 文件，您首先需要创建 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 对象，并使用所有者密码打开 PDF。之后，您需要调用 [Decrypt](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/decrypt) 方法。最后，使用 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 对象的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 方法保存更新后的 PDF 文件。以下代码片段演示了如何解密 PDF 文件。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DecryptPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document with password
    using (var document = new Aspose.Pdf.Document(dataDir + "Decrypt.pdf", "password"))
    {
        // Decrypt PDF
        document.Decrypt();
        // Save PDF document
        document.Save(dataDir + "Decrypt_out.pdf");
    }
}
```

## 更改 PDF 文件的密码

如果您想更改 PDF 文件的密码，您首先需要使用所有者密码打开 PDF 文件，并使用 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 对象。之后，您需要调用 [ChangePasswords](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/changepasswords) 方法。您需要将当前所有者密码与新用户密码和新所有者密码一起传递给此方法。最后，使用 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 对象的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 方法保存更新后的 PDF 文件。

>- 用户密码，如果设置，则是您打开 PDF 所需提供的密码。Acrobat/Reader 将提示用户输入用户密码。如果不正确，文档将无法打开。
>- 所有者密码，如果设置，则控制权限，例如打印、编辑、提取、评论等。Acrobat/Reader 将根据权限设置禁止这些操作。如果您想设置/更改权限，Acrobat 将要求输入此密码。

以下代码片段演示了如何更改 PDF 文件的密码。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangePassword()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document with password
    using (var document = new Aspose.Pdf.Document(dataDir + "ChangePassword.pdf", "owner"))
    {
        // Change password
        document.ChangePasswords("owner", "newuser", "newowner");
        // Save PDF document
        document.Save(dataDir + "ChangePassword_out.pdf");
    }
}
```

## 如何确定源 PDF 是否受密码保护

**Aspose.PDF for .NET** 提供了处理 PDF 文档的强大功能。当使用 Aspose.PDF 命名空间的 Document 类打开受密码保护的 PDF 文档时，我们需要将密码信息作为参数提供给 Document 构造函数，如果未提供此信息，则会生成错误消息。实际上，当尝试使用 Document 对象打开 PDF 文件时，构造函数会尝试读取 PDF 文件的内容，如果未提供正确的密码，则会生成错误消息（这是为了防止未经授权访问文档）。

在处理加密的 PDF 文件时，您可能会遇到需要检测 PDF 是否具有打开密码和/或编辑密码的情况。有时，有些文档在打开时不需要密码信息，但在编辑文件内容时需要信息。因此，为了满足上述要求，Aspose.PDF.Facades 下的 PdfFileInfo 类提供了可以帮助确定所需信息的属性。

### 获取 PDF 文档安全性的信息

PdfFileInfo 包含三个属性以获取 PDF 文档安全性的信息。

1. 属性 PasswordType 返回 PasswordType 枚举值：
    - PasswordType.None - 文档未受密码保护。
    - PasswordType.User - 文档是使用用户（或文档打开）密码打开的。
    - PasswordType.Owner - 文档是使用所有者（或权限、编辑）密码打开的。
    - PasswordType.Inaccessible - 文档受密码保护，但需要密码才能打开，同时提供了无效密码（或没有密码）。
2. 布尔属性 HasOpenPassword - 用于确定输入文件在打开时是否需要密码。
3. 布尔属性 HasEditPassword - 用于确定输入文件在编辑其内容时是否需要密码。

### 从数组中确定正确的密码

有时需要从密码数组中确定正确的密码，并使用正确的密码打开文档。以下代码片段演示了遍历密码数组并尝试使用正确的密码打开文档的步骤。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DetermineCorrectPasswordFromArray()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var info = new  Aspose.Pdf.Facades.PdfFileInfo())
    {
        // Bind PDF document
        info.BindPdf(dataDir + "IsPasswordProtected.pdf");
        // Determine if the source PDF is encrypted
        Console.WriteLine("File is password protected " + info.IsEncrypted);
    
        String[] passwords = new String[5] { "test", "test1", "test2", "test3", "sample" };
    
        for (int passwordcount = 0; passwordcount < passwords.Length; passwordcount++)
        {
            try
            {
                using (var document = new Aspose.Pdf.Document(dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]))
                {
                    if (document.Pages.Count > 0)
                    {
                        Console.WriteLine("Number of Page in document are = " + document.Pages.Count);
                    }
                }
            }
            catch (Aspose.Pdf.InvalidPasswordException)
            {
                Console.WriteLine("Password = " + passwords[passwordcount] + "  is not correct");
            }
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>