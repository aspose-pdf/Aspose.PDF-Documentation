---
title: C#을 사용하여 디지털 서명 또는 PDF에 디지털 서명 추가
linktitle: PDF에 디지털 서명
type: docs
weight: 10
url: /ko/net/digitally-sign-pdf-file/
description: C# 또는 VB.NET을 사용하여 PDF 문서에 디지털 서명을 하세요. C# 또는 VB.NET을 사용하여 디지털 서명된 PDF를 검증하거나 유효성을 검사하세요.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF에 디지털 서명하는 방법",
    "alternativeHeadline": "PDF에 디지털 서명 작업하기",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, 디지털 서명 pdf",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 문서 팀",
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
    "dateModified": "2022-02-04",
    "description": "C# 또는 VB.NET을 사용하여 PDF 문서에 디지털 서명을 하세요. C# 또는 VB.NET을 사용하여 디지털 서명된 PDF를 검증하거나 유효성을 검사하세요."
}
</script>
Aspose.PDF for .NET은 SignatureField 클래스를 사용하여 PDF 파일에 디지털 서명을 추가하는 기능을 지원합니다. PKCS12-인증서로 PDF 파일을 인증할 수도 있습니다. [Adobe Acrobat에서 서명 및 보안 추가하기](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6)와 유사합니다.

PDF 문서에 서명을 사용할 때 기본적으로 문서의 내용을 "그대로" 확인합니다. 따라서 이후에 이루어진 다른 변경사항은 서명을 무효화하게 되므로 문서가 변경되었는지 알 수 있습니다. 반면, 문서를 먼저 인증하면 사용자가 인증을 무효화하지 않고 문서에 할 수 있는 변경사항을 지정할 수 있습니다.

다시 말해, 문서는 여전히 그 무결성을 유지하는 것으로 간주되며, 수신자는 여전히 문서를 신뢰할 수 있습니다. 자세한 내용은 PDF 인증 및 서명을 참조하십시오. 일반적으로 문서를 인증하는 것은 .NET 실행 파일에 코드 서명하는 것과 비교할 수 있습니다.

다음 코드 스니펫도 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.
다음 코드 조각도 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## Aspose.PDF for .NET 서명 기능

다음 클래스와 메서드를 사용하여 PDF 서명을 할 수 있습니다.

- 클래스 [DocMDPSignature](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpsignature)
- 열거형 [DocMDPAccessPermissions](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpaccesspermissions)
- 클래스 [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature)의 속성 [IsCertified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/iscertified)

## 디지털 서명을 이용한 PDF 서명

```csharp
public static void SignDocument()
{
    string inFile = System.IO.Path.Combine(_dataDir,"DigitallySign.pdf");
    string outFile = System.IO.Path.Combine(_dataDir,"DigitallySign_out.pdf");
    using (Document document = new Document(inFile))
    {
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            PKCS7 pkcs = new PKCS7(@"C:\Keys\test.pfx", "Pa$$w0rd2020"); // PKCS7/PKCS7Detached 객체 사용
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200),pkcs);
            // 출력 PDF 파일 저장
            signature.Save(outFile);
        }
    }
}
```
## 디지털 서명에 타임스탬프 추가

### PDF에 타임스탬프를 포함하여 디지털 서명하는 방법

Aspose.PDF for .NET은 타임스탬프 서버나 웹 서비스를 이용하여 PDF에 디지털 서명을 지원합니다.

이 요구 사항을 달성하기 위해, Aspose.PDF 네임스페이스에 [TimestampSettings](https://reference.aspose.com/pdf/net/aspose.pdf/timestampsettings) 클래스가 추가되었습니다. 다음 코드 스니펫을 확인해 주세요. 이 코드는 타임스탬프를 가져와 PDF 문서에 추가합니다:

```csharp
public static void SignWithTimeStampServer()
{
    using (Document document = new Document(System.IO.Path.Combine(_dataDir,"SimpleResume.pdf")))
    {
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            PKCS7 pkcs = new PKCS7(@"C:\Keys\test.pfx", "Start2020");
            TimestampSettings timestampSettings = new TimestampSettings("https://freetsa.org/tsr", string.Empty); // 사용자/비밀번호는 생략 가능
            pkcs.TimestampSettings = timestampSettings;
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(100, 100, 200, 100);
            // 세 가지 서명 유형 중 하나 생성
            signature.Sign(1, "서명 이유", "연락처", "위치", true, rect, pkcs);
            // 출력 PDF 파일 저장
            signature.Save(System.IO.Path.Combine(_dataDir, "DigitallySignWithTimeStamp_out.pdf"));
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
                "contactType": "판매",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "판매",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "판매",
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
    "applicationCategory": ".NET용 PDF 조작 라이브러리",
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

