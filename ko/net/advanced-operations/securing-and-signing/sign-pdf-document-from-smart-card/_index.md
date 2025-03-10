---
title: PDF에 스마트 카드 서명 추가하는 방법
linktitle: 스마트 카드로 PDF 서명하기
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/sign-pdf-document-from-smart-card/
description: Aspose.PDF for .NET은 서명 필드를 사용하여 스마트 카드에서 PDF 문서에 서명할 수 있게 해줍니다.
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
    "abstract": "Aspose.PDF for .NET은 이제 스마트 카드를 사용하여 원활한 PDF 서명을 가능하게 하여 사용자가 저장된 디지털 인증서로 문서를 인증할 수 있도록 디지털 보안을 강화합니다. 이 기능은 서명 필드와 고급 서명 옵션을 모두 지원하여 PDF 거래의 준수 및 무결성을 보장합니다.",
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
    "description": "Aspose.PDF for .NET은 서명 필드를 사용하여 스마트 카드에서 PDF 문서에 서명할 수 있게 해줍니다."
}
</script>

Aspose.PDF for .NET은 키 저장소 위치에서 디지털 서명을 추가하는 기능을 제공합니다. 시스템에 연결된 인증서 저장소, 스마트 카드 또는 [PIV 카드](https://whatis.techtarget.com/definition/personal-identity-verification-PIV-card)에서 제공된 인증서를 수락하여 서명을 적용할 수 있습니다.

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

스마트 카드에서 PDF 문서에 서명하기 위한 코드 스니펫은 다음과 같습니다:

## 서명 필드를 사용하여 스마트 카드로 서명하기

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

## PDF 파일 서명을 사용하여 스마트 카드로 서명하기

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

외부 서명 서비스에 대해 ExternalSignature 클래스를 사용할 수 있습니다. ExternalSignature는 PKCS7 및 PKCS7 분리 서명을 생성합니다.
원하는 해시 알고리즘을 ExternalSignature 생성자에 전달할 수 있습니다. 비분리 서명은 SHA1만 사용할 수 있습니다.
해시 알고리즘을 명시적으로 지정하지 않으면 자동으로 선택됩니다. 비분리 서명의 경우 SHA1이 사용되며, 분리 서명의 경우 RSA 키에 대해 SHA-256이 사용됩니다. ECDSA 키의 경우 해시 크기는 키 크기에 따라 다릅니다.

ExternalSignature 생성자는 키 인증서도 수락합니다(이것은 Base64 형식일 수 있습니다). 개인 키가 포함된 인증서와 공개 키만 포함된 인증서를 전달할 수 있습니다. 두 경우 모두 서명은 CustomSignHash 대리자 코드에서 외부적으로 수행되지만, 외부 알고리즘은 전달된 인증서의 키에 해당하는 서명을 생성해야 합니다. 인증서는 서명된 문서를 올바르게 생성하는 데 필요합니다. ECDSA 서명은 SHA-1을 지원하지 않습니다.

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

서명을 생성하려면 미래의 디지털 서명의 길이에 대한 사전 추정이 필요합니다.
SignHash를 사용하여 디지털 서명을 생성하는 경우 문서 저장 과정에서 대리자가 두 번 호출된다는 것을 알 수 있습니다.
어떤 이유로 두 번 호출할 수 없는 경우, 예를 들어 호출 중에 PIN 코드 요청이 발생하는 경우, PKCS1, PKCS7, PKCS7Detached 및 ExternalSignature 클래스에 대해 __AvoidEstimatingSignatureLength__ 옵션을 사용할 수 있습니다.
이 옵션을 설정하면 예상 길이로 고정 값을 설정하여 서명 길이 추정 단계를 피할 수 있습니다 - __DefaultSignatureLength__. DefaultSignatureLength 속성의 기본값은 3000 바이트입니다.
AvoidEstimatingSignatureLength 옵션은 CustomSignHash 속성에 SignHash 대리자가 설정된 경우에만 작동합니다.
결과 서명 길이가 DefaultSignatureLength 속성에 의해 지정된 예상 길이를 초과하면 실제 길이를 나타내는 __SignatureLengthMismatchException__이 발생합니다.
DefaultSignatureLength 매개변수의 값을 자유롭게 조정할 수 있습니다.

__ExternalSignature__의 경우 CustomSignHash를 사용하지 않더라도 AvoidEstimatingSignatureLength 옵션을 사용할 수 있습니다.

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