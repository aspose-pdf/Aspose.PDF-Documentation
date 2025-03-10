---
title: 提取图像和签名信息
linktitle: 提取图像和签名信息
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/extract-image-and-signature-information/
description: 您可以使用 C# 的 SignatureField 类从签名字段中提取图像并提取签名信息。
lastmod: "2024-11-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Image and Signature Information",
    "alternativeHeadline": "Extract PDF signature images and certificate details",
    "abstract": "新的 Aspose.PDF for .NET 功能从 PDF 签名字段中提取图像和详细信息。使用 C#，开发人员可以检索签名图像和证书数据，包括公钥、指纹和颁发者详细信息，从而增强 PDF 操作能力。这改善了应用程序中的数字签名验证和管理。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Extract Image, SignatureField class, ExtractImage method, ExtractCertificate method, C#, Aspose.PDF for .NET, PDF Signature, digital signature, signature information",
    "wordcount": "583",
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
    "url": "/net/extract-image-and-signature-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-image-and-signature-information/"
    },
    "dateModified": "2024-11-25",
    "description": "您可以使用 C# 的 SignatureField 类从签名字段中提取图像并提取签名信息。"
}
</script>

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

## 从签名字段提取图像

Aspose.PDF for .NET 支持使用 [SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield) 类对 PDF 文件进行数字签名的功能，并且在签署文档时，您还可以为 `SignatureAppearance` 设置图像。现在，此 API 还提供提取签名信息以及与签名字段关联的图像的能力。

为了提取签名信息，我们已向 SignatureField 类引入了 [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractimage) 方法。请查看以下代码片段，演示从 `SignatureField` 对象提取图像的步骤：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesFromSignatureField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractingImage.pdf"))
    {
        // Searching for signature fields
        foreach (var field in document.Form)
        {
            var sf = field as Aspose.Pdf.Forms.SignatureField;
            if (sf == null)
            {
                continue;
            }

            using (Stream imageStream = sf.ExtractImage())
            {
                if (imageStream != null)
                {
                    continue;
                }

                using (System.Drawing.Image image = System.Drawing.Bitmap.FromStream(imageStream))
                {
                    // Save the image
                    image.Save(dataDir + "output_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);
                }
            }
        }
    }
}
```

### 替换签名图像

有时您可能需要仅替换 PDF 文件中已存在的签名字段的图像。为了实现此要求，首先，我们需要在 PDF 文件中搜索表单字段，识别签名字段，获取签名字段的尺寸（矩形尺寸），然后在相同的尺寸上盖印图像。

## 提取签名信息

Aspose.PDF for .NET 支持使用 SignatureField 类对 PDF 文件进行数字签名的功能。目前，我们还可以确定证书的有效性，但无法提取整个证书。可以提取的信息包括公钥、指纹、颁发者等。

为了提取签名信息，我们已向 [SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield) 类引入了 [ExtractCertificate](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractcertificate) 方法。请查看以下代码片段，演示从 SignatureField 对象提取证书的步骤：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractCertificate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractSignatureInfo.pdf"))
    {
        // Searching for signature fields
        foreach (var field in document.Form)
        {
            var sf = field as Aspose.Pdf.Forms.SignatureField;
            if (sf == null)
            {
                continue;
            }
            // Extract certificate
            Stream cerStream = sf.ExtractCertificate();
            if (cerStream == null)
            {
                continue;
            }
            // Save certificate
            using (cerStream)
            {
                byte[] bytes = new byte[cerStream.Length];
                using (FileStream fs = new FileStream(dataDir + "input.cer", FileMode.CreateNew))
                {
                    cerStream.Read(bytes, 0, bytes.Length);
                    fs.Write(bytes, 0, bytes.Length);
                }
            }
        }
    }
}
```

您可以获取有关文档签名算法的信息。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private void GetSignaturesInfo()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "signed_rsa.pdf"))
    {
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            var sigNames = signature.GetSignatureNames();
            var signaturesInfoList =  signature.GetSignaturesInfo();
            foreach (var sigInfo in signaturesInfoList)
            {
                Console.WriteLine(sigInfo.DigestHashAlgorithm);
                Console.WriteLine(sigInfo.AlgorithmType);
                Console.WriteLine(sigInfo.CryptographicStandard);
                Console.WriteLine(sigInfo.SignatureName);
            }
        }
    }
}
```

上述示例的示例输出：
```
Sha256
Rsa
Pkcs7
Signature1
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