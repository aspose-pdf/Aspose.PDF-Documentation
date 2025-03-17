---
title: 이미지 및 서명 정보 추출
linktitle: 이미지 및 서명 정보 추출
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ko/net/extract-image-and-signature-information/
description: C#을 사용하여 SignatureField 클래스를 통해 서명 필드에서 이미지를 추출하고 서명 정보를 추출할 수 있습니다.
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
    "abstract": "새로운 Aspose.PDF for .NET 기능은 PDF 서명 필드에서 이미지와 상세 정보를 추출합니다. C#을 사용하여 개발자는 서명 이미지와 인증서 데이터를 검색할 수 있으며, 여기에는 공개 키, 지문 및 발급자 세부정보가 포함되어 PDF 조작 기능을 향상시킵니다. 이는 애플리케이션 내에서 디지털 서명 검증 및 관리를 개선합니다.",
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
    "description": "C#을 사용하여 SignatureField 클래스를 통해 서명 필드에서 이미지를 추출하고 서명 정보를 추출할 수 있습니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## 서명 필드에서 이미지 추출

Aspose.PDF for .NET은 [SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield) 클래스를 사용하여 PDF 파일에 디지털 서명하는 기능을 지원하며, 문서에 서명하는 동안 `SignatureAppearance`에 대한 이미지를 설정할 수도 있습니다. 이제 이 API는 서명 필드와 관련된 이미지뿐만 아니라 서명 정보를 추출하는 기능도 제공합니다.

서명 정보를 추출하기 위해, 우리는 SignatureField 클래스에 [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractimage) 메서드를 도입했습니다. 다음 코드 스니펫을 참조하여 `SignatureField` 객체에서 이미지를 추출하는 단계를 보여줍니다:

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

### 서명 이미지 교체

때때로 PDF 파일 내에 이미 존재하는 서명 필드의 이미지만 교체해야 할 필요가 있을 수 있습니다. 이 요구 사항을 달성하기 위해, 먼저 PDF 파일 내의 양식 필드를 검색하고, 서명 필드를 식별한 다음, 서명 필드의 치수(직사각형 치수)를 가져오고 동일한 치수에 이미지를 스탬프해야 합니다.

## 서명 정보 추출

Aspose.PDF for .NET은 SignatureField 클래스를 사용하여 PDF 파일에 디지털 서명하는 기능을 지원합니다. 현재 우리는 인증서의 유효성을 판단할 수 있지만 전체 인증서를 추출할 수는 없습니다. 추출할 수 있는 정보는 공개 키, 지문, 발급자 등입니다.

서명 정보를 추출하기 위해, 우리는 [ExtractCertificate](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractcertificate) 메서드를 [SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield) 클래스에 도입했습니다. 다음 코드 스니펫을 참조하여 SignatureField 객체에서 인증서를 추출하는 단계를 보여줍니다:

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

문서 서명 알고리즘에 대한 정보를 얻을 수 있습니다.

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

위 예제에 대한 샘플 출력:
```
Sha256
Rsa
Pkcs7
Signature1
```


## 서명의 손상 여부 확인

**SignaturesCompromiseDetector** 클래스를 사용하여 디지털 서명의 손상 여부를 확인할 수 있습니다.
**Check()** 메서드를 호출하여 문서의 서명을 확인합니다.
서명 손상이 감지되지 않으면 메서드는 true를 반환합니다.
메서드가 false를 반환하면 **HasCompromisedSignatures** 속성을 사용하여 손상된 서명이 있는지 확인하고 **CompromisedSignatures** 속성을 통해 손상된 서명 목록을 검색할 수 있습니다.

기존 서명이 전체 문서를 커버하는지 확인하려면 **SignaturesCoverage** 속성을 사용하십시오.
이 속성은 다음 값을 가질 수 있습니다:
- **Undefined** – 서명 중 하나가 명시적으로 손상되었거나 커버리지 확인이 실패한 경우.
- **EntirelySigned** – 서명이 전체 문서를 커버하는 경우.
- **PartiallySigned** – 서명이 전체 문서를 커버하지 않으며 서명되지 않은 내용이 있는 경우.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Check(string pdfFile)
{
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(pdfFile))
    {   
         // Create the compromise detector instance
         var detector = new Aspose.Pdf.SignaturesCompromiseDetector(document);
         CompromiseCheckResult result;
    
         // Check for compromise
         if (detector.Check(out result))
         {
            Console.WriteLine("No signature compromise detected");
            return;
         }
         
         // Get information about compromised signatures
         if (result.HasCompromisedSignatures)
         {
            Console.WriteLine($"Count of compromised signatures: {result.CompromisedSignatures.Count}");
            foreach (var signatureName in result.CompromisedSignatures)
            {
                Console.WriteLine($"Signature name: {signatureName.FullName}");
            }
         }
         
         // Get info about signatures coverage
         Console.WriteLine(result.SignaturesCoverage);   
    }
}
```
{{< /tab >}}
{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Check(string pdfFile)
{
    // Open PDF document
    using var document = new Aspose.Pdf.Document(pdfFile);
    // Create the compromise detector instance
    var detector = new Aspose.Pdf.SignaturesCompromiseDetector(document);

    // Check for compromise
    if (detector.Check(out var result))
    {
        Console.WriteLine("No signature compromise detected");
        return;
    }
         
    // Get information about compromised signatures
    if (result.HasCompromisedSignatures)
    {
        Console.WriteLine($"Count of compromised signatures: {result.CompromisedSignatures.Count}");
        foreach (var signatureName in result.CompromisedSignatures)
        {
            Console.WriteLine($"Signature name: {signatureName.FullName}");
        }
    }
         
    // Get info about signatures coverage
    Console.WriteLine(result.SignaturesCoverage);
}
```
{{< /tab >}}
{{< /tabs >}}


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