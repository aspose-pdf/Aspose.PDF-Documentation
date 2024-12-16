---
title: 권한 설정, PDF 암호화 및 복호화
linktitle: PDF 파일 암호화 및 복호화
type: docs
weight: 20
url: /ko/net/set-privileges-encrypt-and-decrypt-pdf-file/
description: 다양한 암호화 유형 및 알고리즘을 사용하여 C#으로 PDF 파일을 암호화합니다. 또한 소유자 비밀번호를 사용하여 PDF 파일을 복호화합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "권한 설정, PDF 암호화 및 복호화",
    "alternativeHeadline": "PDF 파일을 암호화하고 복호화하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, PDF 암호화, PDF 복호화",
    "wordcount": "302",
    "proficiencyLevel":"초급",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "dateModified": "2022-02-04",
    "description": "다양한 암호화 유형 및 알고리즘을 사용하여 C#으로 PDF 파일을 암호화합니다. 또한 소유자 비밀번호를 사용하여 PDF 파일을 복호화합니다."
}
</script>
다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 함께 작동합니다.

## 기존 PDF 파일에 권한 설정

PDF 파일에 권한을 설정하려면 [DocumentPrivilege](https://reference.aspose.com/pdf/net/aspose.pdf.facades/documentprivilege) 클래스의 객체를 생성하고 문서에 적용하고자 하는 권한을 지정하세요. 권한이 정의되면 이 객체를 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) 메소드에 인수로 전달합니다. 다음 코드 조각은 PDF 파일의 권한을 설정하는 방법을 보여줍니다.

```csharp
// 전체 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// 소스 PDF 파일을 로드합니다
using (Document document = new Document(dataDir + "input.pdf"))
{
    // Document Privileges 객체를 인스턴스화합니다.
    // 모든 권한에 대한 제한을 적용합니다.
    DocumentPrivilege documentPrivilege = DocumentPrivilege.ForbidAll;
    // 화면 읽기만 허용합니다.
    documentPrivilege.AllowScreenReaders = true;
    // 사용자와 소유자 비밀번호로 파일을 암호화합니다.
    // 사용자가 사용자 비밀번호로 파일을 볼 때,
    // 화면 읽기 옵션만 활성화됩니다.
    document.Encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
    // 업데이트된 문서를 저장합니다.
    document.Save(dataDir + "SetPrivileges_out.pdf");
}
```
## PDF 파일을 다양한 암호화 유형 및 알고리즘을 사용하여 암호화하기

[문서](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) 메소드를 사용하여 PDF 파일을 암호화할 수 있습니다. 사용자 비밀번호, 소유자 비밀번호, 권한을 [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) 메소드에 전달할 수 있습니다. 그 외에도, [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm) 열거형의 어떤 값이든 전달할 수 있습니다. 이 열거형은 암호화 알고리즘과 키 크기의 다양한 조합을 제공합니다. 원하는 값을 전달할 수 있습니다. 마지막으로, [문서](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체의 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) 메소드를 사용하여 암호화된 PDF 파일을 저장하세요.

>PDF 파일을 암호화할 때 다른 사용자 및 소유자 비밀번호를 지정하십시오.

- **사용자 비밀번호**가 설정되어 있으면 PDF를 열기 위해 제공해야 합니다.
- **사용자 비밀번호**가 설정된 경우, PDF를 열기 위해 제공해야 합니다.
- **소유자 비밀번호**가 설정된 경우, 인쇄, 편집, 추출, 코멘트 추가 등의 권한을 제어합니다. Acrobat/Reader는 권한 설정에 따라 이러한 작업을 금지합니다. 권한을 설정/변경하려면 Acrobat에서 이 비밀번호가 필요합니다.

다음 코드 조각은 PDF 파일을 암호화하는 방법을 보여줍니다.

```csharp
// 완전한 예시와 데이터 파일에 대해서는 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 을 방문하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// 문서 열기
Document document = new Document(dataDir+ "Encrypt.pdf");
// PDF 암호화
document.Encrypt("user", "owner", 0, CryptoAlgorithm.RC4x128);
dataDir = dataDir + "Encrypt_out.pdf";
// 업데이트된 PDF 저장
document.Save(dataDir);
```

## 소유자 비밀번호를 사용하여 PDF 파일 복호화

점점 더 많은 사용자들이 인쇄/복사/공유/정보 추출 등의 행위로부터 문서를 보호하기 위해 암호화된 PDF 파일을 교환하고 있습니다.
사용자들은 문서에 대한 무단 액세스, 예를 들어 PDF 파일 내용의 인쇄/복사/공유/추출을 방지하기 위해 암호화된 PDF 파일을 교환하는 경우가 점점 더 많아지고 있습니다.
이와 관련하여 암호화된 PDF 파일에 대한 접근이 필요한데, 이러한 접근은 인증된 사용자만이 얻을 수 있습니다. 또한 사람들은 인터넷 상에서 PDF 파일을 복호화하는 다양한 솔루션을 찾고 있습니다.

이 문제는 Aspose.PDF 라이브러리를 사용하여 한 번에 해결하는 것이 좋습니다.

PDF 파일을 복호화하려면 먼저 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 생성하고 소유자의 비밀번호를 사용하여 PDF를 열어야 합니다.
PDF 파일을 해독하려면 먼저 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 생성하고 소유자의 비밀번호를 사용하여 PDF를 엽니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// 문서 열기
Document document = new Document(dataDir+ "Decrypt.pdf", "password");
// PDF 해독
document.Decrypt();
dataDir = dataDir + "Decrypt_out.pdf";
// 업데이트된 PDF 저장
document.Save(dataDir);
```

## PDF 파일의 비밀번호 변경

PDF 파일의 비밀번호를 변경하려면 먼저 소유자 비밀번호를 사용하여 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체로 PDF 파일을 열어야 합니다.
PDF 파일의 비밀번호를 변경하려면 먼저 [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) 객체를 사용하여 소유자 비밀번호로 PDF 파일을 열어야 합니다.

>- 사용자 비밀번호가 설정된 경우, PDF를 열기 위해 제공해야 합니다. Acrobat/Reader는 사용자에게 사용자 비밀번호를 입력하라는 메시지를 표시합니다. 올바르지 않으면 문서가 열리지 않습니다.
>- 소유자 비밀번호가 설정된 경우, 인쇄, 편집, 추출, 주석 추가 등의 권한을 제어합니다. Acrobat/Reader는 권한 설정에 따라 이러한 작업을 허용하지 않습니다. 권한을 설정/변경하려면 이 비밀번호가 필요합니다.

다음 코드 조각은 PDF 파일의 비밀번호를 변경하는 방법을 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

// 문서 열기
Document document = new Document(dataDir+ "ChangePassword.pdf", "owner");
// 비밀번호 변경
document.ChangePasswords("owner", "newuser", "newowner");
dataDir = dataDir + "ChangePassword_out.pdf";
// 업데이트된 PDF 저장
document.Save(dataDir);
```
## 방법 - 소스 PDF가 비밀번호로 보호되어 있는지 확인하는 방법

**Aspose.PDF for .NET**은 PDF 문서를 다루는 데 탁월한 기능을 제공합니다. Aspose.PDF 네임스페이스의 Document 클래스를 사용하여 비밀번호로 보호된 PDF 문서를 열 때, Document 생성자에 비밀번호 정보를 인수로 제공해야 하며, 이 정보를 제공하지 않으면 오류 메시지가 생성됩니다. 사실, Document 객체로 PDF 파일을 열려고 할 때, 생성자는 PDF 파일의 내용을 읽으려고 시도하고 올바른 비밀번호가 제공되지 않으면 오류 메시지가 생성됩니다(문서의 무단 접근을 방지하기 위해 발생합니다).

암호화된 PDF 파일을 다룰 때, PDF에 열기 비밀번호와/또는 편집 비밀번호가 있는지 감지하고 싶은 상황에 직면할 수 있습니다.
암호화된 PDF 파일을 다룰 때, PDF에 열기 비밀번호와/또는 편집 비밀번호가 있는지 감지하는 상황에 직면할 수 있습니다.

### PDF 문서 보안에 대한 정보 얻기

PdfFileInfo는 PDF 문서 보안에 대한 정보를 얻기 위한 세 가지 속성을 포함하고 있습니다.

1. 속성 PasswordType은 PasswordType 열거형 값을 반환합니다:
    - PasswordType.None - 문서는 비밀번호로 보호되지 않았습니다
    - PasswordType.User - 문서가 사용자(또는 문서 열기) 비밀번호로 열렸습니다
    - PasswordType.Owner - 문서가 소유자(또는 권한, 편집) 비밀번호로 열렸습니다
    - PasswordType.Inaccessible - 문서는 비밀번호로 보호되지만, 비밀번호가 필요하며 잘못된 비밀번호(또는 비밀번호 없음)가 제공되었습니다.
2. boolean 속성 HasOpenPassword - 입력 파일이 열릴 때 비밀번호가 필요한지 여부를 결정하는 데 사용됩니다.
3. boolean 속성 HasEditPassword - 입력 파일이 내용을 편집하기 위해 비밀번호가 필요한지 여부를 결정하는 데 사용됩니다.

### 배열에서 올바른 비밀번호 결정하기
### 배열에서 올바른 비밀번호 결정하기

때때로 비밀번호 배열에서 올바른 비밀번호를 결정하고 올바른 비밀번호로 문서를 열어야 하는 요구 사항이 있습니다. 다음 코드 스니펫은 비밀번호 배열을 반복하고 문서를 올바른 비밀번호로 시도해 보는 단계를 보여줍니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리의 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// 소스 PDF 파일을 로드합니다.
PdfFileInfo info = new PdfFileInfo();
info.BindPdf(dataDir + "IsPasswordProtected.pdf");
// 소스 PDF가 암호화되었는지 확인합니다.
Console.WriteLine("File is password protected " + info.IsEncrypted);
String[] passwords = new String[5] { "test", "test1", "test2", "test3", "sample" };
for (int passwordcount = 0; passwordcount < passwords.Length; passwordcount++)
{
    try
    {
        Document doc = new Document(dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
        if (doc.Pages.Count > 0)
            Console.WriteLine("Number of Page in document are = " + doc.Pages.Count);
    }
    catch (InvalidPasswordException)
    {
        Console.WriteLine("Password = " + passwords[passwordcount] + "  is not correct");
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
                "contactType": "영업",
                "areaServed": "US",
                "availableLanguage": "영어"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "영업",
                "areaServed": "GB",
                "availableLanguage": "영어"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "영업",
                "areaServed": "AU",
                "availableLanguage": "영어"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": ".NET을 위한 PDF 조작 라이브러리",
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
```

