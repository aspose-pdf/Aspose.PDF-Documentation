---
title: 如何将智能卡签名添加到PDF
linktitle: 使用智能卡进行PDF签名
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /zh/net/sign-pdf-document-from-smart-card/
description: Aspose.PDF for .NET允许您使用签名字段从智能卡签署PDF文档。
lastmod: "2024-11-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to add Smart Card signature to PDF",
    "alternativeHeadline": "Add Smart Card Signatures to PDF Documents Easily",
    "abstract": "Aspose.PDF for .NET现在支持使用智能卡无缝签署PDF，增强数字安全性，允许用户使用其存储的数字证书对文档进行身份验证。此功能支持签名字段和高级签名选项，确保PDF交易的合规性和完整性。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Smart Card signature, PDF signing, Aspose.PDF for .NET, digital signatures, external signing service, PKCS7 signature, certificate selection, hash algorithm, signature field, signing PDF documents",
    "wordcount": "755",
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
    "url": "/net/sign-pdf-document-from-smart-card/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/sign-pdf-document-from-smart-card/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET允许您使用签名字段从智能卡签署PDF文档。"
}
</script>

Aspose.PDF for .NET提供从密钥存储位置添加数字签名的功能。您可以通过接受证书存储、智能卡或在运行时连接到系统的[PIV卡](https://whatis.techtarget.com/definition/personal-identity-verification-PIV-card)提供的证书来应用签名。

以下代码片段也适用于[Aspose.PDF.Drawing](/pdf/net/drawing/)库。

以下是从智能卡签署PDF文档的代码片段：

## 使用签名字段进行智能卡签名

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetSignatureInfo()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open a document stream
    using (var fs = new FileStream(dataDir + "blank.pdf", FileMode.Open, FileAccess.ReadWrite))
    {
        // Open PDF document from stream
        using (var document = new Aspose.Pdf.Document(fs))
        {
            // Create a signature field
            var field1 = new Aspose.Pdf.Forms.SignatureField(document.Pages[1], new Aspose.Pdf.Rectangle(100, 400, 10, 10));

            // Sign with certificate selection in the windows certificate store
            var store = new X509Store(StoreLocation.CurrentUser);
            store.Open(OpenFlags.ReadOnly);
            
            // Manually chose the certificate in the store
            var sel = X509Certificate2UI.SelectFromCollection(store.Certificates, null, null, X509SelectionFlag.SingleSelection);

            // Set an external signature settings
            var externalSignature = new Aspose.Pdf.Forms.ExternalSignature(sel[0])
            {
                Authority = "Me",
                Reason = "Reason",
                ContactInfo = "Contact"
            };
            // Set a name of signature field
            field1.PartialName = "sig1";
            // Add the signature field to the document
            document.Form.Add(field1, 1);
            // Sign the document
            field1.Sign(externalSignature);
            // Save PDF document
            document.Save(dataDir + "externalSignature1_out.pdf");
        }
    }
}

private static void VerifyExternalSignature()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "externalSignature1.pdf"))
    {
        using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            var sigNames = pdfSign.GetSignatureNames();
            for (int index = 0; index <= sigNames.Count - 1; index++)
            {
                if (!pdfSign.VerifySignature(sigNames[index]))
                {
                    throw new Exception("Not verified");
                }
            }
        }
    }
}
```

## 使用PDF文件签名进行智能卡签名

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private void SignWithSmartCard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "blank.pdf"))
    {
        using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
        {   
            // Bind PDF document
            pdfSign.BindPdf(document);

            // Sign with certificate selection in the windows certificate store
            var store = new X509Store(StoreLocation.CurrentUser);
            store.Open(OpenFlags.ReadOnly);
            // Manually chose the certificate in the store
            var sel = X509Certificate2UI.SelectFromCollection(store.Certificates, null, null, X509SelectionFlag.SingleSelection);
            
            // Set an external signature settings
            var externalSignature = new Aspose.Pdf.Forms.ExternalSignature(sel[0]);
            pdfSign.SignatureAppearance = dataDir + "demo.png";
            // Sign the document
            pdfSign.Sign(1, "Reason", "Contact", "Location", true, new System.Drawing.Rectangle(100, 100, 200, 200), externalSignature);
            // Save PDF document
            pdfSign.Save(dataDir + "externalSignature2_out.pdf");
        }
    }
}

private static void VerifyExternalSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "externalSignature1.pdf"))
    {
        using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            var sigNames = pdfSign.GetSignatureNames();
            for (int index = 0; index <= sigNames.Count - 1; index++)
            {
                if (!pdfSign.VerifySignature(sigNames[index]))
                {
                    throw new Exception("Not verified");
                }
            }
        }
    }
}
```

您可以使用ExternalSignature类进行外部签名服务。ExternalSignature创建PKCS7和PKCS7分离签名。
您可以将所需的哈希算法传递给ExternalSignature构造函数。请注意，非分离签名只能使用SHA1。
如果您没有明确指定哈希算法，它将自动选择。对于非分离签名，将使用SHA1；对于分离签名，将为RSA密钥使用SHA-256。对于ECDSA密钥，哈希大小取决于密钥大小。

ExternalSignature构造函数还接受一个密钥证书（可以是Base64格式）。您可以传递一个包含私钥的证书和一个仅包含公钥的证书。在任何情况下，签名将在CustomSignHash委托代码中外部执行，但外部算法必须创建与传递证书的密钥相对应的签名。证书用于正确生成签名文档。ECDSA签名不支持SHA-1。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithExternalService()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "blank.pdf"))
    {
        using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
        {
            // Bind PDF document
            sign.BindPdf(document);

            // Get public certificate
            X509Certificate2 signerCert = GetPublicCertificate();

            // Set a certificate and a digest algorithm
            var signature = new Aspose.Pdf.Forms.ExternalSignature(signerCert, Aspose.Pdf.DigestHashAlgorithm.Sha256);

            // Define a delegate to external sign
            Aspose.Pdf.Forms.SignHash customSignHash = delegate(byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
            {
                return CallExternalSignatureService(signableHash, digestHashAlgorithm);
            };
            // Set a sign hash
            signature.CustomSignHash = customSignHash;
            sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), signature);
            // Save PDF document
            sign.Save(dataDir + "ExternalSignature_out.pdf");
        }
    }
}

private static X509Certificate2 GetPublicCertificate()
{
    // Your code to get a public certificate. The certificate can be supplied by a third-party service or a smart card
}

private static byte[] CallExternalSignatureService(byte[] hash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
{
    // Call a third-party service that provides a digital signature service
    // The method must return signed data
    // The digestHashAlgorithm argument points to the digest algorithm that was applied to the data to produce the value of the hash argument
}
```

要创建签名，需要对未来数字签名的长度进行初步估计。
如果您使用SignHash创建数字签名，您可能会发现委托在文档保存过程中被调用两次。
如果由于某种原因您无法承受两次调用，例如在调用期间发生PIN码请求，您可以对PKCS1、PKCS7、PKCS7Detached和ExternalSignature类使用__AvoidEstimatingSignatureLength__选项。
设置此选项通过将固定值作为预期长度 - __DefaultSignatureLength__ 来避免签名长度估计步骤。DefaultSignatureLength属性的默认值为3000字节。
AvoidEstimatingSignatureLength选项仅在CustomSignHash属性中设置SignHash委托时有效。
如果结果签名长度超过DefaultSignatureLength属性指定的预期长度，您将收到__SignatureLengthMismatchException__，指示实际长度。
您可以根据自己的需要调整DefaultSignatureLength参数的值。

对于__ExternalSignature__，即使未使用CustomSignHash，也可以使用AvoidEstimatingSignatureLength选项。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithExternalService()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "blank.pdf"))
    {
        using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
        {
            // Bind PDF document
            sign.BindPdf(document);

            // Get public certificate
            X509Certificate2 signerCert = GetPublicCertificate();

            // Set a certificate and a digest algorithm
            var signature = new Aspose.Pdf.Forms.ExternalSignature(signerCert, Aspose.Pdf.DigestHashAlgorithm.Sha256);

            // Define a delegate to external sign
            Aspose.Pdf.Forms.SignHash customSignHash = delegate(byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
            {
                return CallExternalSignatureService(signableHash, digestHashAlgorithm);
            };
            // Set a sign hash
            signature.CustomSignHash = customSignHash;

            // Set an option to avoiding twice SignHash calling.
            signature.AvoidEstimatingSignatureLength = true;
            signature.DefaultSignatureLength = 3500;

            sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), signature);
            // Save PDF document
            sign.Save(dataDir + "ExternalSignature_out.pdf");
        }
    }
}

private static X509Certificate2 GetPublicCertificate()
{
    // Your code to get a public certificate. The certificate can be supplied by a third-party service or a smart card
}

private static byte[] CallExternalSignatureService(byte[] hash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
{
    // Call a third-party service that provides a digital signature service
    // The method must return signed data
    // The digestHashAlgorithm argument points to the digest algorithm that was applied to the data to produce the value of the hash argument
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