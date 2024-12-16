---
title: PDF를 XPS 프린터로 인쇄하기
linktitle: PDF를 XPS 프린터로 인쇄하기 (Facades)
type: docs
weight: 20
url: /ko/net/printing-pdf-to-an-xps-printer-facades/
description: 이 페이지는 PdfViewer 클래스를 사용하여 PDF를 XPS 프린터로 인쇄하는 방법을 보여줍니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF를 XPS 프린터로 인쇄하기",
    "alternativeHeadline": "PDF를 XPS 프린터로 인쇄하는 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, pdf to an XPS 프린터",
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
    "url": "/net/printing-pdf-to-an-xps-printer-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-to-an-xps-printer-facades/"
    },
    "dateModified": "2022-02-04",
    "description": "이 페이지는 PdfViewer 클래스를 사용하여 PDF를 XPS 프린터로 인쇄하는 방법을 보여줍니다."
}
</script>
다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리에서도 작동합니다.

## **C#에서 XPS 프린터로 PDF 인쇄하기**

[PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) 클래스를 사용하여 XPS 프린터나 다른 소프트 프린터로 PDF 파일을 인쇄할 수 있습니다. 이를 위해 PdfViewer 클래스의 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2) 메소드를 사용하여 PDF 파일을 엽니다. PrinterSettings 및 PageSettings 클래스를 사용하여 다양한 인쇄 설정을 설정할 수 있습니다. 또한 설치한 XPS 또는 다른 소프트 프린터의 PrinterName 속성을 설정해야 합니다.

마지막으로, [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) 메소드를 사용하여 PDF를 XPS 또는 다른 소프트 프린터로 인쇄합니다. 다음 코드 조각은 PDF 파일을 XPS 프린터로 인쇄하는 방법을 보여줍니다.

```csharp
public static void PrintToXpsPrinter()
{
    // PdfViewer 객체 생성
    PdfViewer viewer = new PdfViewer();

    // 입력 PDF 파일 열기
    viewer.BindPdf(_dataDir + "input.pdf");

    // 인쇄를 위한 속성 설정
    viewer.AutoResize = true;         // 크기 조정하여 파일 인쇄
    viewer.AutoRotate = true;         // 회전 조정하여 파일 인쇄
    viewer.PrintPageDialog = false;   // 인쇄 시 페이지 번호 대화 상자 생성하지 않음

    // 프린터 및 페이지 설정 및 PrintDocument 객체 생성
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // XPS/PDF 프린터 이름 설정
    ps.PrinterName = "Microsoft XPS Document Writer";
    // 또는 PDF 프린터 설정
    // Ps.PrinterName = "Adobe PDF";

    // 필요한 경우 PageSize 설정
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

    // 필요한 경우 PageMargins 설정
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // 프린터 및 페이지 설정을 사용하여 문서 인쇄
    viewer.PrintDocumentWithSettings(pgs, ps);

    // 인쇄 후 PDF 파일 닫기
    viewer.Close();
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
                "areaServed": "미국",
                "availableLanguage": "영어"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "영업",
                "areaServed": "영국",
                "availableLanguage": "영어"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "영업",
                "areaServed": "호주",
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

