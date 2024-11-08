---
title: PDF에서 썸네일 이미지 생성
linktitle: PDF에서 썸네일 이미지 생성
type: docs
weight: 110
url: /ko/net/generate-thumbnail-images-from-pdf-documents/
description: 이 섹션에서는 PDF 문서에서 썸네일 이미지를 생성하는 방법을 설명합니다
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF에서 썸네일 이미지 생성",
    "alternativeHeadline": "PDF 파일에서 썸네일 이미지를 생성하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF 문서 생성",
    "keywords": "pdf, c#, 썸네일 이미지 생성",
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
    "url": "/net/generate-thumbnail-images-from-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/generate-thumbnail-images-from-pdf-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "이 섹션에서는 PDF 문서에서 썸네일 이미지를 생성하는 방법을 설명합니다"
}
</script>

{{% alert color="primary" %}}

Adobe Acrobat SDK는 Acrobat 기술과 상호 작용하는 소프트웨어를 개발하는 데 도움을 주는 도구 모음입니다. 이 SDK에는 헤더 파일, 타입 라이브러리, 간단한 유틸리티, 샘플 코드 및 문서가 포함되어 있습니다.

Acrobat SDK를 사용하여 다음과 같은 방법으로 Acrobat 및 Adobe Reader와 통합하는 소프트웨어를 개발할 수 있습니다:

- **JavaScript** — Acrobat 또는 Adobe Reader의 기능을 확장하기 위해 개별 PDF 문서나 외부에서 스크립트를 작성합니다.
- **플러그인** — Acrobat 또는 Adobe Reader의 기능을 확장하는 동적으로 연결된 플러그인을 생성합니다.
- **애플리케이션 간 통신** — 애플리케이션 간 통신(IAC)을 사용하여 별도의 애플리케이션 프로세스를 작성하여 Acrobat 기능을 제어합니다. Microsoft® Windows®에서는 DDE 및 OLE를 지원하며, Mac OS®에서는 Apple 이벤트/AppleScript를 지원합니다. IAC는 UNIX®에서는 사용할 수 없습니다.

Aspose.PDF for .NET은 Adobe Acrobat 자동화에 대한 의존성을 없애면서 동일한 기능을 많이 제공합니다.
Aspose.PDF for .NET은 Adobe Acrobat Automation에 대한 의존도를 해소할 수 있는 많은 기능을 제공합니다.

{{% /alert %}}

## Acrobat 상호 응용 프로그램 통신 API를 사용한 응용 프로그램 개발

Acrobat API를 두 가지 구별되는 계층이 있는 것으로 생각하세요. Acrobat 상호 응용 프로그램 통신(IAC) 객체를 사용합니다:

- Acrobat 응용 프로그램(AV) 계층. AV 계층은 문서가 어떻게 보여지는지를 제어할 수 있습니다. 예를 들어, 문서 객체의 뷰는 Acrobat과 관련된 계층에 있습니다.
- 이동 가능 문서(PD) 계층. PD 계층은 문서 내의 정보에 접근을 제공합니다, 예를 들어 페이지 같은. PD 계층에서는 PDF 문서의 기본 조작을 수행할 수 있습니다, 예를 들어 페이지를 삭제, 이동 또는 교체하거나 주석 속성을 변경하는 것도 가능합니다. 또한 PDF 페이지를 인쇄하고, 텍스트를 선택하고, 조작된 텍스트에 접근하며, 썸네일을 생성하거나 삭제할 수도 있습니다.

우리의 의도는 PDF 페이지를 썸네일 이미지로 변환하는 것이므로, 우리는 IAC에 더 집중하고 있습니다.
PDF 페이지를 썸네일 이미지로 변환하는 것이 목표이므로 IAC에 더 집중하고 있습니다.

### Acrobat 접근 방식

각 문서의 썸네일 이미지를 생성하기 위해 Adobe Acrobat 7.0 SDK와 Microsoft .NET 2.0 프레임워크를 사용했습니다.

[Acrobat SDK](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/)는 Adobe Acrobat의 정식 버전과 함께 사용하면 객체의 COM 라이브러리를 제공합니다(무료 Adobe Reader는 COM 인터페이스를 제공하지 않습니다). 이 COM 객체를 COM Interop을 통해 사용하여 PDF 문서를 로드하고 첫 페이지를 가져와 클립보드에 해당 페이지를 렌더링합니다. 그런 다음 .NET 프레임워크를 사용하여 이를 비트맵으로 복사하고 이미지를 확대 및 결합하여 결과를 GIF 또는 PNG 파일로 저장합니다.

Adobe Acrobat이 설치되면 regedit.exe를 사용하여 HKEY_CLASSES_ROOT 아래에서 AcroExch.PDDoc이라는 항목을 찾습니다.

**레지스트리에 보이는 AcroExch.PDDDoc 항목**

![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)
![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-CreateThumbnailImagesUsingAdobe-CreateThumbnailImagesUsingAdobe.cs" >}}

## Aspose.PDF for .NET 접근 방법

Aspose.PDF for .NET은 PDF 문서를 다루는 데 광범위한 지원을 제공합니다. 또한 PDF 문서의 페이지를 다양한 이미지 형식으로 변환하는 기능을 지원합니다. 위에 설명된 기능은 Aspose.PDF for .NET을 사용하여 쉽게 달성할 수 있습니다.

Aspose.PDF의 독특한 이점은 다음과 같습니다:

- 시스템에 Adobe Acrobat이 설치되어 있지 않아도 PDF 파일을 작업할 수 있습니다.
- Acrobat Automation과 비교했을 때 Aspose.PDF for .NET 사용이 간단하고 이해하기 쉽습니다.

PDF 페이지를 JPEG로 변환해야 하는 경우, [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) 네임스페이스는 PDF 페이지를 JPEG 이미지로 렌더링하는 [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice)라는 클래스를 제공합니다.
PDF 페이지를 JPEG 이미지로 변환해야 하는 경우, [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) 네임스페이스는 PDF 페이지를 JPEG 이미지로 렌더링하는 [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice)라는 클래스를 제공합니다.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-CreateThumbnailImages-CreateThumbnailImages.cs" >}}

{{% alert color="primary" %}}

- [PDF 문서에서 썸네일 이미지 생성](https://www.codeproject.com/Articles/5887/Generate-Thumbnail-Images-from-PDF-Documents)에 대해 CodeProject에 감사합니다.
- [Acrobat SDK 참조](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/documentation.html)에 대해 Acrobat에 감사합니다.

{{% /alert %}}

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

