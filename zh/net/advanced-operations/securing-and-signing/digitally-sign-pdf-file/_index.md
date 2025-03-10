---
title: 在 C# 中添加数字签名或数字签名 PDF
linktitle: 数字签名 PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/digitally-sign-pdf-file/
description: 使用 C# 或 VB.NET 数字签名 PDF 文档。使用 C# 或 VB.NET 验证或验证数字签名的 PDF。
lastmod: "2025-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add digital signature or digitally sign PDF in C#",
    "alternativeHeadline": "Working with digitally sign PDF",
    "abstract": "Aspose.PDF for .NET 引入了使用 C# 或 VB.NET 数字签名 PDF 文档的强大功能，增强了文档的完整性和安全性。用户可以实现各种签名类型，包括非分离和分离签名，支持 PKCS7 和 ECDSA，允许根据特定的加密标准定制签名过程。此功能不仅验证文档的真实性，还支持时间戳和认证，确保可信的文档处理。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "digital signature, digitally sign PDF, C#, PDF signing, PKCS12 certificate, verify PDF signature, ECDSA signing, timestamp server, custom hash signing, Aspose.PDF for .NET",
    "wordcount": "2020",
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
    "url": "/net/digitally-sign-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/digitally-sign-pdf-file/"
    },
    "dateModified": "2025-02-07",
    "description": "使用 C# 或 VB.NET 数字签名 PDF 文档。使用 C# 或 VB.NET 验证或验证数字签名的 PDF。"
}
</script>

Aspose.PDF for .NET 支持使用 SignatureField 类数字签名 PDF 文件。您还可以使用 PKCS12 证书对 PDF 文件进行认证。类似于 [在 Adobe Acrobat 中添加签名和安全性](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6)。

使用签名签署 PDF 文档时，您基本上确认其内容“原样”。因此，之后进行的任何其他更改都会使签名失效，从而您会知道文档是否被更改。而认证文档则首先允许您指定用户可以对文档进行的更改，而不会使认证失效。

换句话说，文档仍然被认为保持其完整性，接收者仍然可以信任该文档。有关更多详细信息，请访问认证和签署 PDF。一般来说，认证文档可以与对 .NET 可执行文件的代码签名进行比较。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## Aspose.PDF for .NET 签名功能

我们可以使用以下类和方法进行 PDF 签名

- 类 [DocMDPSignature](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpsignature)。
- 枚举 [DocMDPAccessPermissions](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpaccesspermissions)。
- 属性 [IsCertified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/iscertified) 在 [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) 类中。

要基于 PKCS12 证书（文件扩展名 .p12, pfx）创建数字签名，您应该创建 `PdfFileSignature` 类的实例，将文档对象传递给它。
接下来，您应该通过创建其中一个类的对象来指定所需的数字签名方法：

- PKCS1。
- PKCS7。
- PKCS7Detached。

_您只能为 `PKCS7Detached` 设置摘要算法。对于 `PKCS1` 和 `PKCS7`，摘要算法始终设置为 SHA-1。_

接下来，您需要在 `PdfFileSignature.Sign()` 方法中使用接收到的签名算法对象。
数字签名将在文档保存后设置。

## 使用数字签名签署 PDF

下面的示例创建了一个带有 SHA-1 摘要算法的 PKCS7 非分离签名。
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7(dataDir + "rsa_cert.pfx", "12345");
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}
```

下面的示例创建了一个带有 SHA-256 摘要算法的 PKCS7Detached 格式的分离签名。密钥算法取决于证书密钥。支持 DSA、RSA、ECDSA。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignDocument(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object using the opened document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 detached object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(pfxFilePath, password, Aspose.Pdf.DigestHashAlgorithm.Sha256);
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200),pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}
```

您可以使用 PdfFileSignature.VerifySignature() 方法验证签名。
之前，使用 `GetSignNames()` 方法获取签名名称。从版本 25.02 开始，应使用 `GetSignatureNames()` 方法，该方法返回 `SignatureName` 的列表。
`SignatureName` 防止在验证具有相同名称的签名时发生冲突。
应使用接受 `SignatureName` 类型而不是字符串签名名称的方法。

_注意，__PdfFileSignature.VerifySigned()__ 方法已弃用。_

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Verify()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "signed_rsa.pdf"))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {         
            // Get a list of signature names in the document
            var sigNames = signature.GetSignatureNames();

            // Loop through all signature names to verify each one
            foreach (var sigName in sigNames)
            {
                // Verify that the signature with the given name is valid
                if (!signature.VerifySignature(sigName))
                {
                    throw new Exception("Not verified");
                }
            }
        }
    }
}
```

## 向数字签名添加时间戳

### 如何使用时间戳数字签署 PDF

Aspose.PDF for .NET 支持使用时间戳服务器或 Web 服务数字签署 PDF。

为了实现此要求，Aspose.PDF 命名空间中添加了 [TimestampSettings](https://reference.aspose.com/pdf/net/aspose.pdf/timestampsettings) 类。请查看以下代码片段，该代码获取时间戳并将其添加到 PDF 文档中：

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithTimeStampServer(string pfxFilePath, string password)
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            var pkcs = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);
            // Create TimestampSettings settings
            var timestampSettings = new Aspose.Pdf.TimestampSettings("https://freetsa.org/tsr", string.Empty); // User/Password can be omitted
            pkcs.TimestampSettings = timestampSettings;
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(100, 100, 200, 100);
            // Create any of the three signature types
            signature.Sign(1, "Signature Reason", "Contact", "Location", true, rect, pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySignWithTimeStamp_out.pdf");
        }
    }
}
```

## 使用 base64 格式的 X509Certificate2 签署 PDF

此代码使用外部证书对 PDF 进行签名，可能与服务器交互以检索签名哈希并将签名嵌入 PDF 文档中。

签署 PDF 的步骤：

1. 创建 PdfFileSignature 的实例。
1. 定义自定义签名哈希。
1. 加载证书。
1. 签署数据。
1. 绑定并签署 PDF。
1. 保存已签名的 PDF。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithBase64Certificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    var base64Str = "Certificate in base64 format";
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        var sign = new Aspose.Pdf.Forms.ExternalSignature(base64Str, false);// without Private Key
        sign.ShowProperties = false;
        // Create a delegate to external sign
        Aspose.Pdf.Forms.SignHash customSignHash = delegate (byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
        {
            // Simulated Server Part (This will probably just be sending data and receiving a response)
            var signerCert = new X509Certificate2(pfxFilePath, password, X509KeyStorageFlags.Exportable);// must have Private Key
            var rsaCSP = new RSACryptoServiceProvider();
            var xmlString = signerCert.PrivateKey.ToXmlString(true);
            rsaCSP.FromXmlString(xmlString);
            byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
            return signedData;
        };
        sign.CustomSignHash = customSignHash;
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "input.pdf");
        // Sign the file
        pdfSign.Sign(1, "second approval", "second_user@example.com", "Australia", false,
            new System.Drawing.Rectangle(200, 200, 200, 100),
            sign);
        // Save PDF document
        pdfSign.Save(dataDir + "SignWithBase64Certificate_out.pdf");
    }
}
```

## 使用 HASH 签名函数签署 PDF

使用自定义哈希签名函数，签名机构可以实施超出标准签名方法的特定加密标准或内部安全政策，从而确保文档的完整性。
这种方法有助于验证自签名以来文档未被更改，并提供具有可验证的签名者身份证明的具有法律约束力的数字签名，使用 PFX 证书。

此代码片段演示了使用带有自定义哈希签名函数的 PFX（PKCS#12）证书在 C# 中数字签署 PDF 文档。

让我们更仔细地看看 DPF 签名过程：

1. 定义文件路径和证书信息：

- inputPdf: 需要签名的输入 PDF 文档的路径。
- inputP12: 用于签名的 .p12（PFX）证书文件的路径。
- inputPfxPassword: PFX 证书的密码。
- outputPdf: 签名 PDF 将保存的路径。

2. 签名过程：

- 创建一个 `PdfFileSignature` 对象并绑定到输入 PDF。
- 使用 PFX 证书及其密码初始化 `PKCS7` 对象。将 'CustomSignHash' 方法分配为自定义哈希签名函数。
- 调用 `Sign` 方法，指定页码（在此情况下为 1）、签名详细信息（原因、内容、位置）以及签名的位置（坐标为 (0, 0, 500, 500) 的矩形）。
- 然后将签名的 PDF 保存到指定的输出路径。

3. 自定义哈希签名：

- `CustomSignHash` 方法接受一个字节数组 signableHash（要签名的哈希）。
- 它加载相同的 PFX 证书并检索其私钥。
- 使用 `RSACryptoServiceProvider` 和 SHA-1 算法对哈希进行签名。
- 返回签名数据（字节数组），以便应用于 PDF 签名。

摘要算法可以在 PKCS7Detached 构造函数中指定。可以在 CustomSignHash 委托中调用第三方服务。CustomSignHash 中使用的签名算法必须与传递给 PKCS7/PKCS7Detached 的证书中的密钥算法匹配。

下面的示例创建了一个带有 RSA 算法和 SHA-1 摘要算法的非分离签名。
如果您使用 PKCS7Detached 而不是 PKCS7，您可以使用 ECDCA 并设置所需的摘要算法。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithCertificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {   
        // Bind PDF document
        sign.BindPdf(dataDir + "input.pdf");
        // Create PKCS#7 object to sign
        var pkcs7 = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);// You can use PKCS7Detached with digest algorithm argument
        // Set the delegate to external sign
        pkcs7.CustomSignHash = CustomSignHash;
        // Sign the file
        sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);
        // Save PDF document
        sign.Save(dataDir + "SignWithCertificate_out.pdf");
    }

    // Custom hash signing function to generate a digital signature
    byte[] CustomSignHash(byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
    {
        var inputP12 = "111.p12";
        var inputPfxPassword = "123456";
        X509Certificate2 signerCert = new X509Certificate2(inputP12, inputPfxPassword, X509KeyStorageFlags.Exportable);
        RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
        var xmlString = signerCert.PrivateKey.ToXmlString(true);
        rsaCSP.FromXmlString(xmlString);
        byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
        return signedData;
    }
}
```

要创建签名，需要对未来数字签名的长度进行初步估计。
如果您使用 SignHash 创建数字签名，您可能会发现委托在文档保存过程中被调用两次。
如果由于某种原因您无法承受两次调用，例如在调用期间发生 PIN 码请求，您可以对 PKCS1、PKCS7、PKCS7Detached 和 ExternalSignature 类使用 `AvoidEstimatingSignatureLength` 选项。
设置此选项通过将固定值设置为预期长度 - `DefaultSignatureLength` 来避免签名长度估计步骤。DefaultSignatureLength 属性的默认值为 3000 字节。
AvoidEstimatingSignatureLength 选项仅在 CustomSignHash 属性中设置 SignHash 委托时有效。
如果结果签名长度超过 DefaultSignatureLength 属性指定的预期长度，您将收到 `SignatureLengthMismatchException`，指示实际长度。
您可以根据自己的判断调整 DefaultSignatureLength 参数的值。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithCertificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {   
        // Bind PDF document
        sign.BindPdf(dataDir + "input.pdf");
        // Create PKCS#7 object to sign
        var pkcs7 = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);// You can use PKCS7Detached with digest algorithm argument
        // Set the delegate to external sign
        pkcs7.CustomSignHash = CustomSignHash;
        // Set an option to avoiding twice SignHash calling.
        pkcs7.AvoidEstimatingSignatureLength = true;
        // Sign the file
        sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);
        // Save PDF document
        sign.Save(dataDir + "SignWithCertificate_out.pdf");
    }

    // Custom hash signing function to generate a digital signature
    byte[] CustomSignHash(byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
    {
        var inputP12 = "111.p12";
        var inputPfxPassword = "123456";
        X509Certificate2 signerCert = new X509Certificate2(inputP12, inputPfxPassword, X509KeyStorageFlags.Exportable);
        RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
        var xmlString = signerCert.PrivateKey.ToXmlString(true);
        rsaCSP.FromXmlString(xmlString);
        byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
        return signedData;
    }
}
```

## 使用 ECDSA 签署 PDF 文档

使用 ECDSA（椭圆曲线数字签名算法）签署 PDF 文档涉及利用椭圆曲线密码学生成数字签名。这提供了高安全性和效率，特别是在移动和资源受限的环境中。这种方法确保您的 PDF 文档以椭圆曲线密码学的安全优势进行数字签名。

Aspose.PDF 支持基于 ECDSA 的数字签名创建和验证。
以下椭圆曲线支持数字签名的创建和验证：

- P-192(secp192r1)。
- P-256(secp256r1)。
- P-384(secp384r1)。
- P-521(secp521r1)。
- brainpoolP192r1。
- brainpoolP256r1。
- brainpoolP384r1。
- brainpoolP512r1。

默认摘要算法是 SHA2，长度取决于 ECDSA 密钥大小。
您可以在 `PKCS7Detached` 构造函数中指定摘要算法。

可以使用以下摘要算法签署 ECDSA 数字签名：SHA-256、SHA-384、SHA3–512、SHA3–256、SHA3–384、SHA3–512。
可以验证以下摘要算法的 ECDSA 数字签名：SHA-256、SHA-384、SHA3–512、SHA3–256、SHA3–384、SHA3–512。

您可以通过在 OpenSSL 中创建 PFX(output.pfx) 证书来检查签名和验证。

```bash
openssl ecparam -genkey -name brainpoolP512r1 -out private.key
openssl ec -in private.key -pubout -out public.pem
openssl req -new -x509 -days 365 -key private.key -out certificate.crt -subj "/C=PL/ST=Silesia/L=Katowice/O=My2 Organization/CN=example2.com"
openssl pkcs12 -export -out output.pfx -inkey private.key -in certificate.crt
```

在 Aspose.PDF 中可用于签名和验证的曲线名称（可以使用命令 'openssl ecparam -list_curves' 获取 OpenSSL 中的曲线列表）：prime256v1、secp384r1、secp521r1、brainpoolP256r1、brainpoolP384r1、brainpoolP512r1。

要使用 ECDSA 签署 PDF 文档，C# 中的一般步骤如下：

1. 您需要一个 PFX 或 P12 格式的 ECDSA 证书。这些证书包含签名所需的公钥和私钥。
1. 使用 Aspose.PDF 库，您将文档绑定到签名处理程序。
1. 使用 ECDSA 私钥对文档内容的哈希进行签名。
1. 将生成的签名与签名原因、位置和联系信息等元数据一起放入 PDF 文件中。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void VerifyEcda()
{
   // The path to the documents directory
   var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

   // Open PDF document
   using (var document = new Aspose.Pdf.Document(dataDir + "signed_ecdsa.pdf"))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Check if the document contains any digital signatures
            if (!signature.ContainsSignature())
            {
                throw new Exception("Not contains signature");
            }

            // Get a list of signature names in the document
            var sigNames = signature.GetSignatureNames();

            // Loop through all signature names to verify each one
            foreach (var sigName in sigNames)
            {
                // Verify that the signature with the given name is valid
                if (!signature.VerifySignature(sigName))
                {
                    throw new Exception("Not verified");
                }
            }
        }
    }
}

private static void SignEcdsa(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures(); 

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create an instance of PdfFileSignature to sign the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create a PKCS7Detached object using the provided certificate and password
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(cert, "12345", Aspose.Pdf.DigestHashAlgorithm.Sha256);

            // Sign the first page of the document, setting the signature's appearance at the specified location
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);

            // Save PDF document
            signature.Save(dataDir + "SignEcdsa_out.pdf");
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