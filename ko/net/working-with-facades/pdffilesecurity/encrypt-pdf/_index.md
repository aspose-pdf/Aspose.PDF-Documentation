---
title: PDF 파일 암호화
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/encrypt-pdf-file/
description: 이 주제는 PdfFileSecurity 클래스를 사용하여 PDF 파일을 암호화하는 방법을 설명합니다.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Encrypt PDF File",
    "alternativeHeadline": "Secure PDF Encryption with C#",
    "abstract": "PdfFileSecurity 클래스를 사용하여 민감한 문서의 보안을 강화하는 방법을 알아보세요. 이 기능을 통해 PDF 파일에 비밀번호를 설정하여 권한이 있는 사용자만 접근할 수 있도록 합니다. 파일 공유 및 아카이빙 중 강력한 보호를 위해 최대 256비트의 키 길이를 가진 AES를 포함한 다양한 암호화 유형 및 알고리즘을 탐색하세요.",
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
    "description": "Aspose.PDF는 간단하고 쉬운 작업뿐만 아니라 더 복잡한 목표도 수행할 수 있습니다. 고급 사용자 및 개발자를 위한 다음 섹션을 확인하세요."
}
</script>

PDF 문서를 암호화하면 외부의 무단 접근으로부터 내용을 보호할 수 있으며, 특히 파일 공유나 아카이빙 중에 유용합니다.

기밀 PDF 문서는 암호화되고 비밀번호로 보호될 수 있습니다. 비밀번호를 아는 사용자만 이러한 문서를 복호화하고 열어볼 수 있습니다.

Aspose.PDF 라이브러리를 사용하여 PDF 암호화가 어떻게 작동하는지 살펴보겠습니다.

## 다양한 암호화 유형 및 알고리즘을 사용하여 PDF 파일 암호화

PDF 파일을 암호화하려면 [PdfFileSecurity](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilesecurity) 객체를 생성한 다음 [EncryptFile](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile) 메서드를 호출해야 합니다. [EncryptFile](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdffilesecurity/methods/encryptfile) 메서드에 사용자 비밀번호, 소유자 비밀번호 및 권한을 전달할 수 있습니다. 이 메서드에 KeySize 및 Algorithm 값을 전달해야 합니다.

다음은 가능한 [CryptoAlgorithm](https://reference.aspose.com/pdf/ko/net/aspose.pdf/cryptoalgorithm) 목록입니다:

|**멤버 이름**|**값**|**설명**|
| :- | :- | :- |
|RC4x40|0|키 길이 40의 RC4.|
|RC4x128|1|키 길이 128의 RC4.|
|AESx128|2|키 길이 128의 AES.|
|AESx256|3|키 길이 256의 AES.|

다음 코드 스니펫은 PDF 파일을 암호화하는 방법을 보여줍니다.

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