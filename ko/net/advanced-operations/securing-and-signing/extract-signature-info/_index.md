---
title: 이미지 및 서명 정보 추출
linktitle: 이미지 및 서명 정보 추출
type: docs
weight: 30
url: ko/net/extract-image-and-signature-information/
description: 서명 필드에서 이미지를 추출하고 SignatureField 클래스를 사용하여 서명 정보를 추출할 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "이미지 및 서명 정보 추출",
    "alternativeHeadline": "PDF에서 이미지 및 서명 추출 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "PDF, C#, 서명 추출",
    "wordcount": "302",
    "proficiencyLevel":"초보자",
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
    "url": "/net/extract-image-and-signature-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-image-and-signature-information/"
    },
    "dateModified": "2022-02-04",
    "description": "서명 필드에서 이미지를 추출하고 SignatureField 클래스를 사용하여 서명 정보를 추출할 수 있습니다."
}
</script>

다음 코드 스니펫도 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## 서명 필드에서 이미지 추출

Aspose.PDF for .NET은 [SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield) 클래스를 사용하여 PDF 파일에 디지털 서명을 지원하며, 문서에 서명할 때 SignatureAppearance에 이미지를 설정할 수도 있습니다. 이제 이 API는 서명 필드와 관련된 이미지뿐만 아니라 서명 정보를 추출하는 기능도 제공합니다.

서명 정보를 추출하기 위해, SignatureField 클래스에 [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractimage) 메소드를 도입했습니다. 다음 코드 스니펫을 살펴보세요. 이는 SignatureField 객체에서 이미지를 추출하는 단계를 보여줍니다:

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하세요.
// 문서 디렉토리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

string input = dataDir+ @"ExtractingImage.pdf";
using (Document pdfDocument = new Document(input))
{
    foreach (Field field in pdfDocument.Form)
    {
        SignatureField sf = field as SignatureField;
        if (sf != null)
        {
            string outFile = dataDir+ @"output_out.jpg";
            using (Stream imageStream = sf.ExtractImage())
            {
                if (imageStream != null)
                {
                    using (System.Drawing.Image image = Bitmap.FromStream(imageStream))
                    {
                        image.Save(outFile, System.Drawing.Imaging.ImageFormat.Jpeg);
                    }
                }
            }
        }
    }
}
```
### 서명 이미지 교체

때로는 PDF 파일 내에 이미 존재하는 서명 필드의 이미지만 교체해야 할 필요가 있을 수 있습니다. 이 요구 사항을 수행하기 위해, 먼저 PDF 파일 내의 양식 필드를 검색하고, 서명 필드를 식별하고, 서명 필드의 치수(직사각형 치수)를 얻은 다음 동일한 치수 위에 이미지를 찍어야 합니다.

## 서명 정보 추출

Aspose.PDF for .NET은 SignatureField 클래스를 사용하여 PDF 파일에 디지털 서명하는 기능을 지원합니다. 현재, 우리는 인증서의 유효성을 판단할 수 있지만 전체 인증서를 추출할 수는 없습니다. 추출 가능한 정보에는 공개 키, 지문, 발급자 등이 있습니다.

서명 정보를 추출하기 위해, 우리는 [SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield) 클래스에 [ExtractCertificate](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractcertificate) 메소드를 도입하였습니다.
서명 정보를 추출하기 위해 [SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield) 클래스에 [ExtractCertificate](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractcertificate) 메소드를 도입했습니다.

```csharp
// 완전한 예제와 데이터 파일은 https://github.com/aspose-pdf/Aspose.PDF-for-.NET 에서 확인하십시오.
// 문서 디렉터리 경로입니다.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

string input = dataDir + "ExtractSignatureInfo.pdf";
using (Document pdfDocument = new Document(input))
{
    foreach (Field field in pdfDocument.Form)
    {
        SignatureField sf = field as SignatureField;
        if (sf != null)
        {
            Stream cerStream = sf.ExtractCertificate();
            if (cerStream != null)
            {
                using (cerStream)
                {
                    byte[] bytes = new byte[cerStream.Length];
                    using (FileStream fs = new FileStream(dataDir + @"input.cer", FileMode.CreateNew))
                    {
                        cerStream.Read(bytes, 0, bytes.Length);
                        fs.Write(bytes, 0, bytes.Length);
                    }
                }
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
                "contactType": "영업",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "영업",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "영업",
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

