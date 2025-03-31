---
title: C#에서 디지털 서명 추가 또는 PDF 디지털 서명
linktitle: PDF 디지털 서명
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/digitally-sign-pdf-file/
description: C# 또는 VB.NET을 사용하여 PDF 문서에 디지털 서명합니다. C# 또는 VB.NET을 사용하여 디지털 서명된 PDF를 검증하거나 유효성을 검사합니다.
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
    "abstract": "Aspose.PDF for .NET은 C# 또는 VB.NET을 사용하여 PDF 문서에 디지털 서명하는 강력한 기능을 소개하여 문서의 무결성과 보안을 향상시킵니다. 사용자는 PKCS7 및 ECDSA를 지원하는 비분리 및 분리 서명을 포함한 다양한 서명 유형을 구현할 수 있으며, 특정 암호화 표준에 맞춘 사용자 정의 서명 프로세스를 허용합니다. 이 기능은 문서의 진위를 검증할 뿐만 아니라 타임스탬프 및 인증을 가능하게 하여 신뢰할 수 있는 문서 처리를 보장합니다.",
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
    "description": "C# 또는 VB.NET을 사용하여 PDF 문서에 디지털 서명합니다. C# 또는 VB.NET을 사용하여 디지털 서명된 PDF를 검증하거나 유효성을 검사합니다."
}
</script>

Aspose.PDF for .NET은 SignatureField 클래스를 사용하여 PDF 파일에 디지털 서명하는 기능을 지원합니다. PKCS12 인증서를 사용하여 PDF 파일을 인증할 수도 있습니다. [Adobe Acrobat에서 서명 및 보안 추가하기](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6)와 유사한 것입니다.

서명을 사용하여 PDF 문서에 서명할 때, 기본적으로 그 내용을 "있는 그대로" 확인하는 것입니다. 따라서 이후에 이루어진 다른 변경 사항은 서명을 무효화하며, 문서가 변경되었는지 알 수 있습니다. 반면, 문서를 인증하면 사용자가 인증을 무효화하지 않고 문서에 대해 수행할 수 있는 변경 사항을 지정할 수 있습니다.

즉, 문서는 여전히 무결성을 유지하는 것으로 간주되며 수신자는 문서를 신뢰할 수 있습니다. 자세한 내용은 PDF 인증 및 서명 방문하십시오. 일반적으로 문서를 인증하는 것은 .NET 실행 파일의 코드 서명과 비교할 수 있습니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## Aspose.PDF for .NET 서명 기능

PDF 서명을 위해 다음 클래스 및 메서드를 사용할 수 있습니다.

- 클래스 [DocMDPSignature](https://reference.aspose.com/pdf/ko/net/aspose.pdf.forms/docmdpsignature).
- 열거형 [DocMDPAccessPermissions](https://reference.aspose.com/pdf/ko/net/aspose.pdf.forms/docmdpaccesspermissions).
- [PdfFileSignature](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilesignature) 클래스의 [IsCertified](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilesignature/properties/iscertified) 속성.

PKCS12 인증서(.p12, .pfx 파일 확장자)를 기반으로 디지털 서명을 생성하려면 `PdfFileSignature` 클래스의 인스턴스를 생성하고 문서 객체를 전달해야 합니다.
다음으로, 다음 클래스 중 하나의 객체를 생성하여 원하는 디지털 서명 방법을 지정해야 합니다:

- PKCS1.
- PKCS7.
- PKCS7Detached.

_해시 알고리즘은 `PKCS7Detached`에 대해서만 설정할 수 있습니다. `PKCS1` 및 `PKCS7`의 경우 해시 알고리즘은 항상 SHA-1로 설정됩니다._

다음으로, 수신한 서명 알고리즘 객체를 `PdfFileSignature.Sign()` 메서드에서 사용해야 합니다.
디지털 서명은 문서가 저장된 후 설정됩니다.

## 디지털 서명으로 PDF 서명하기

아래 예제는 SHA-1 해시 알고리즘을 사용하여 PKCS7 비분리 서명을 생성합니다.
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

아래 예제는 SHA-256 해시 알고리즘을 사용하여 PKCS7Detached 형식으로 분리 서명을 생성합니다. 키 알고리즘은 인증서 키에 따라 다릅니다. DSA, RSA, ECDSA가 지원됩니다.

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

PdfFileSignature.VerifySignature() 메서드를 사용하여 서명을 검증할 수 있습니다.
이전에는 `GetSignNames()` 메서드를 사용하여 서명 이름을 가져왔습니다. 버전 25.02부터는 `GetSignatureNames()` 메서드를 사용해야 하며, 이는 `SignatureName` 목록을 반환합니다.
`SignatureName`은 동일한 이름의 서명을 검증할 때 충돌을 방지합니다.
문자열 서명 이름 대신 `SignatureName` 유형을 수용하는 메서드를 사용해야 합니다.

_참고: __PdfFileSignature.VerifySigned()__ 메서드는 더 이상 사용되지 않습니다._

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

## 디지털 서명에 타임스탬프 추가하기

### 타임스탬프와 함께 PDF에 디지털 서명하는 방법

Aspose.PDF for .NET은 타임스탬프 서버 또는 웹 서비스를 사용하여 PDF에 디지털 서명하는 것을 지원합니다.

이 요구 사항을 충족하기 위해 [TimestampSettings](https://reference.aspose.com/pdf/ko/net/aspose.pdf/timestampsettings) 클래스가 Aspose.PDF 네임스페이스에 추가되었습니다. 타임스탬프를 얻고 PDF 문서에 추가하는 다음 코드 스니펫을 살펴보십시오:

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

## base64 형식의 X509Certificate2로 PDF 서명하기

이 코드는 외부 인증서를 사용하여 PDF에 서명하며, 서명된 해시를 검색하고 PDF 문서에 서명을 삽입하기 위해 서버와 상호 작용할 수 있습니다.

PDF 서명 단계:

1. PdfFileSignature의 인스턴스를 생성합니다.
1. 사용자 정의 서명 해시를 정의합니다.
1. 인증서를 로드합니다.
1. 데이터를 서명합니다.
1. PDF를 바인딩하고 서명합니다.
1. 서명된 PDF를 저장합니다.

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

## 해시 서명 기능으로 PDF 서명하기

사용자 정의 해시 서명 기능을 사용하여 서명 권한자는 표준 서명 방법을 넘어서는 특정 암호화 표준 또는 내부 보안 정책을 구현할 수 있으며, 문서의 무결성을 보장합니다.
이 접근 방식은 서명이 적용된 이후 문서가 변경되지 않았음을 검증하는 데 도움이 되며, PFX 인증서를 사용하여 서명자의 신원을 검증할 수 있는 법적 구속력이 있는 디지털 서명을 제공합니다.

이 코드 스니펫은 C#에서 사용자 정의 해시 서명 기능을 사용하여 PFX (PKCS#12) 인증서를 사용하여 PDF 문서에 디지털 서명하는 방법을 보여줍니다.

PDF 서명 프로세스를 자세히 살펴보겠습니다:

1. 파일 경로 및 인증서 정보를 정의합니다:

- inputPdf: 서명해야 하는 입력 PDF 문서의 경로입니다.
- inputP12: 서명에 사용되는 .p12 (PFX) 인증서 파일의 경로입니다.
- inputPfxPassword: PFX 인증서의 비밀번호입니다.
- outputPdf: 서명된 PDF가 저장될 경로입니다.

2. 서명 프로세스:

- `PdfFileSignature` 객체가 생성되어 입력 PDF에 바인딩됩니다.
- PFX 인증서와 그 비밀번호를 사용하여 `PKCS7` 객체가 초기화됩니다. 'CustomSignHash' 메서드가 사용자 정의 해시 서명 기능으로 할당됩니다.
- `Sign` 메서드가 호출되어 페이지 번호(이 경우 1), 서명 세부정보(이유, 내용, 위치) 및 서명의 위치(좌표 (0, 0, 500, 500)의 사각형)를 지정합니다.
- 서명된 PDF는 지정된 출력 경로에 저장됩니다.

3. 사용자 정의 해시 서명:

- `CustomSignHash` 메서드는 서명할 해시(signableHash)인 바이트 배열을 수용합니다.
- 동일한 PFX 인증서를 로드하고 개인 키를 검색합니다.
- 개인 키를 사용하여 `RSACryptoServiceProvider` 및 SHA-1 알고리즘을 사용하여 해시에 서명합니다.
- 서명된 데이터(바이트 배열)가 PDF 서명에 적용되도록 반환됩니다.

해시 알고리즘은 PKCS7Detached 생성자에서 지정할 수 있습니다. 사용자 정의 해시 서명 대리자에서 타사 서비스를 호출할 수 있습니다. CustomSignHash에서 사용되는 서명 알고리즘은 PKCS7/PKCS7Detached에 전달된 인증서의 키 알고리즘과 일치해야 합니다.

아래 예제는 RSA 알고리즘과 SHA-1 해시 알고리즘을 사용하여 비분리 서명을 생성합니다.
PKCS7 대신 PKCS7Detached를 사용하면 ECDCA를 사용할 수 있으며 원하는 해시 알고리즘을 설정할 수 있습니다.

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

서명을 생성하려면 미래의 디지털 서명의 길이에 대한 예비 추정이 필요합니다.
SignHash를 사용하여 디지털 서명을 생성하는 경우 문서 저장 프로세스 중에 대리자가 두 번 호출되는 것을 발견할 수 있습니다.
어떤 이유로 두 번 호출할 수 없는 경우, 예를 들어 호출 중에 PIN 코드 요청이 발생하는 경우, PKCS1, PKCS7, PKCS7Detached 및 ExternalSignature 클래스에 대해 `AvoidEstimatingSignatureLength` 옵션을 사용할 수 있습니다.
이 옵션을 설정하면 예상 길이로 고정 값을 설정하여 서명 길이 추정 단계를 피할 수 있습니다 - `DefaultSignatureLength`. DefaultSignatureLength 속성의 기본값은 3000 바이트입니다.
AvoidEstimatingSignatureLength 옵션은 CustomSignHash 속성에 SignHash 대리자가 설정된 경우에만 작동합니다.
결과 서명 길이가 DefaultSignatureLength 속성에 의해 지정된 예상 길이를 초과하면 실제 길이를 나타내는 `SignatureLengthMismatchException`이 발생합니다.
DefaultSignatureLength 매개변수의 값을 자유롭게 조정할 수 있습니다.

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

## ECDSA를 사용한 PDF 문서 서명하기

ECDSA (타원 곡선 디지털 서명 알고리즘)를 사용하여 PDF 문서에 서명하는 것은 타원 곡선 암호화를 활용하여 디지털 서명을 생성하는 것을 포함합니다. 이는 특히 모바일 및 자원이 제한된 환경에서 높은 보안성과 효율성을 제공합니다. 이 접근 방식은 PDF 문서가 타원 곡선 암호화의 보안 이점을 가지고 디지털 서명되도록 보장합니다.

Aspose.PDF는 ECDSA 기반 디지털 서명 생성 및 검증을 지원합니다.
디지털 서명 생성 및 검증을 위해 지원되는 타원 곡선은 다음과 같습니다:

- P-192(secp192r1).
- P-256(secp256r1).
- P-384(secp384r1).
- P-521(secp521r1).
- brainpoolP192r1.
- brainpoolP256r1.
- brainpoolP384r1.
- brainpoolP512r1.

기본 해시 알고리즘은 ECDSA 키 크기에 따라 길이가 달라지는 SHA2입니다.
PKCS7Detached 생성자에서 해시 알고리즘을 지정할 수 있습니다.

다음 해시 알고리즘으로 ECDSA 디지털 서명을 서명할 수 있습니다: SHA-256, SHA-384, SHA3–512, SHA3–256, SHA3–384, SHA3–512.
다음 해시 알고리즘으로 ECDSA 디지털 서명을 검증할 수 있습니다: SHA-256, SHA-384, SHA3–512, SHA3–256, SHA3–384, SHA3–512.

OpenSSL에서 PFX(output.pfx) 인증서를 생성하여 서명 및 검증을 확인할 수 있습니다.

```bash
openssl ecparam -genkey -name brainpoolP512r1 -out private.key
openssl ec -in private.key -pubout -out public.pem
openssl req -new -x509 -days 365 -key private.key -out certificate.crt -subj "/C=PL/ST=Silesia/L=Katowice/O=My2 Organization/CN=example2.com"
openssl pkcs12 -export -out output.pfx -inkey private.key -in certificate.crt
```

Aspose.PDF에서 서명 및 검증을 위한 사용 가능한 곡선 이름(OpenSSL에서 곡선 목록은 'openssl ecparam -list_curves' 명령으로 얻을 수 있음): prime256v1, secp384r1, secp521r1, brainpoolP256r1, brainpoolP384r1, brainpoolP512r1.

ECDSA를 사용하여 PDF 문서에 서명하려면 C#에서 일반적인 단계는 다음과 같습니다:

1. PFX 또는 P12 형식의 ECDSA 인증서가 필요합니다. 이 인증서에는 서명에 필요한 공개 키와 개인 키가 모두 포함되어 있습니다.
1. Aspose.PDF 라이브러리를 사용하여 문서를 서명 처리기에 바인딩합니다.
1. ECDSA 개인 키를 사용하여 문서 내용의 해시에 서명합니다.
1. 서명된 메타데이터(서명 이유, 위치 및 연락처 세부정보 등)와 함께 PDF 파일 내에 생성된 서명을 배치합니다.

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