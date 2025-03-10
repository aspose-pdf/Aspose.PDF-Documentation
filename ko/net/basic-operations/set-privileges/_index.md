---
title: 권한 설정, PDF 암호화 및 복호화
linktitle: PDF 파일 암호화 및 복호화
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /ko/net/set-privileges-encrypt-and-decrypt-pdf-file/
description: 다양한 암호화 유형 및 알고리즘을 사용하여 C#으로 PDF 파일을 암호화합니다. 또한 소유자 비밀번호를 사용하여 PDF 파일을 복호화합니다.
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
    "abstract": "이 새로운 기능은 사용자가 다양한 암호화 유형 및 알고리즘을 사용하여 C#으로 PDF 파일을 효율적으로 암호화하고 복호화할 수 있도록 합니다. 사용자 및 소유자 비밀번호를 활용하여 문서 접근 및 권한에 대한 강력한 제어를 제공하며, PDF 콘텐츠의 기밀성과 무결성을 보장하면서 개발자의 보안 관리 작업을 간소화합니다.",
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
    "description": "다양한 암호화 유형 및 알고리즘을 사용하여 C#으로 PDF 파일을 암호화합니다. 또한 소유자 비밀번호를 사용하여 PDF 파일을 복호화합니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## 기존 PDF 파일에 권한 설정

PDF 파일에 권한을 설정하려면 [DocumentPrivilege](https://reference.aspose.com/pdf/net/aspose.pdf.facades/documentprivilege) 클래스의 객체를 생성하고 문서에 적용할 권한을 지정합니다. 권한이 정의되면 이 객체를 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) 메서드의 인수로 전달합니다. 다음 코드 스니펫은 PDF 파일의 권한을 설정하는 방법을 보여줍니다.

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

## 다양한 암호화 유형 및 알고리즘을 사용하여 PDF 파일 암호화

[Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) 메서드를 사용하여 PDF 파일을 암호화할 수 있습니다. 사용자 비밀번호, 소유자 비밀번호 및 권한을 [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) 메서드에 전달할 수 있습니다. 또한 [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm) 열거형의 값을 전달할 수 있습니다. 이 열거형은 다양한 암호화 알고리즘 및 키 크기의 조합을 제공합니다. 원하는 값을 전달할 수 있습니다. 마지막으로 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 암호화된 PDF 파일을 저장합니다.

>PDF 파일을 암호화할 때는 서로 다른 사용자 및 소유자 비밀번호를 지정하십시오.

- **사용자 비밀번호**가 설정된 경우, PDF를 열기 위해 제공해야 하는 비밀번호입니다. Acrobat/Reader는 사용자에게 사용자 비밀번호를 입력하라는 메시지를 표시합니다. 비밀번호가 올바르지 않으면 문서가 열리지 않습니다.
- **소유자 비밀번호**가 설정된 경우, 인쇄, 편집, 추출, 주석 달기 등의 권한을 제어합니다. Acrobat/Reader는 권한 설정에 따라 이러한 작업을 허용하지 않습니다. 권한을 설정/변경하려면 이 비밀번호가 필요합니다.

다음 코드 스니펫은 PDF 파일을 암호화하는 방법을 보여줍니다.

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

## 소유자 비밀번호를 사용하여 PDF 파일 복호화

점점 더 많은 사용자가 문서에 대한 무단 접근을 방지하기 위해 암호화된 PDF 파일을 교환하고 있습니다. 오늘날 PDF 파일을 암호화하는 가장 좋은 선택은 콘텐츠의 기밀성과 무결성을 유지하기 때문입니다. 이와 관련하여, 암호화된 PDF 파일에 접근할 필요가 있으며, 이러한 접근은 인증된 사용자만 얻을 수 있습니다. 또한 사람들은 인터넷에서 PDF 파일을 복호화하기 위한 다양한 솔루션을 찾고 있습니다.

Aspose.PDF 라이브러리를 사용하여 이 문제를 한 번에 해결하는 것이 좋습니다.

PDF 파일을 복호화하려면 먼저 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 생성하고 소유자 비밀번호를 사용하여 PDF를 엽니다. 그 후, [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [Decrypt](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/decrypt) 메서드를 호출해야 합니다. 마지막으로 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다. 다음 코드 스니펫은 PDF 파일을 복호화하는 방법을 보여줍니다.

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

## PDF 파일의 비밀번호 변경

PDF 파일의 비밀번호를 변경하려면 먼저 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 사용하여 소유자 비밀번호로 PDF 파일을 열어야 합니다. 그 후, [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [ChangePasswords](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/changepasswords) 메서드를 호출해야 합니다. 이 메서드에 현재 소유자 비밀번호와 새로운 사용자 비밀번호 및 새로운 소유자 비밀번호를 전달해야 합니다. 마지막으로 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메서드를 사용하여 업데이트된 PDF 파일을 저장합니다.

>- 사용자 비밀번호가 설정된 경우, PDF를 열기 위해 제공해야 하는 비밀번호입니다. Acrobat/Reader는 사용자에게 사용자 비밀번호를 입력하라는 메시지를 표시합니다. 비밀번호가 올바르지 않으면 문서가 열리지 않습니다.
>- 소유자 비밀번호가 설정된 경우, 인쇄, 편집, 추출, 주석 달기 등의 권한을 제어합니다. Acrobat/Reader는 권한 설정에 따라 이러한 작업을 허용하지 않습니다. 권한을 설정/변경하려면 이 비밀번호가 필요합니다.

다음 코드 스니펫은 PDF 파일의 비밀번호를 변경하는 방법을 보여줍니다.

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

## 방법 - 소스 PDF가 비밀번호로 보호되는지 확인하기

**Aspose.PDF for .NET**은 PDF 문서를 처리하는 뛰어난 기능을 제공합니다. Aspose.PDF 네임스페이스의 Document 클래스를 사용하여 비밀번호로 보호된 PDF 문서를 열 때, Document 생성자에 비밀번호 정보를 인수로 제공해야 하며, 이 정보가 제공되지 않으면 오류 메시지가 생성됩니다. 실제로 Document 객체로 PDF 파일을 열려고 할 때, 생성자는 PDF 파일의 내용을 읽으려고 시도하며, 올바른 비밀번호가 제공되지 않으면 오류 메시지가 생성됩니다(이는 문서의 무단 접근을 방지하기 위해 발생합니다).

암호화된 PDF 파일을 처리할 때, PDF에 열기 비밀번호 및/또는 편집 비밀번호가 있는지 감지하려는 시나리오에 직면할 수 있습니다. 때때로 비밀번호 정보 없이 열 수 있는 문서가 있지만, 파일의 내용을 편집하기 위해서는 정보가 필요합니다. 따라서 위의 요구 사항을 충족하기 위해 Aspose.PDF.Facades에 있는 PdfFileInfo 클래스는 필요한 정보를 결정하는 데 도움이 되는 속성을 제공합니다.

### PDF 문서 보안 정보 가져오기

PdfFileInfo는 PDF 문서 보안에 대한 정보를 가져오기 위해 세 가지 속성을 포함합니다.

1. PasswordType 속성은 PasswordType 열거형 값을 반환합니다:
    - PasswordType.None - 문서가 비밀번호로 보호되지 않음.
    - PasswordType.User - 문서가 사용자(또는 문서 열기) 비밀번호로 열림.
    - PasswordType.Owner - 문서가 소유자(또는 권한, 편집) 비밀번호로 열림.
    - PasswordType.Inaccessible - 문서가 비밀번호로 보호되지만 열기 위해 비밀번호가 필요하며, 잘못된 비밀번호(또는 비밀번호 없음)가 제공됨.
2. boolean 속성 HasOpenPassword - 입력 파일을 열 때 비밀번호가 필요한지 여부를 결정하는 데 사용됩니다.
3. boolean 속성 HasEditPassword - 입력 파일의 내용을 편집하기 위해 비밀번호가 필요한지 여부를 결정하는 데 사용됩니다.

### 배열에서 올바른 비밀번호 결정하기

때때로 비밀번호 배열에서 올바른 비밀번호를 결정하고 올바른 비밀번호로 문서를 여는 요구 사항이 있습니다. 다음 코드 스니펫은 비밀번호 배열을 반복하고 올바른 비밀번호로 문서를 여는 단계를 보여줍니다.

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