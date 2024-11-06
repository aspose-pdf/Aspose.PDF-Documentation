---
title: .NET Framework에서 PDF 인쇄
linktitle: .NET Framework에서 PDF 인쇄
type: docs
weight: 10
url: ko/net/printing-pdf-in-net-framework/
keywords: "print pdf file c#, c# print pdf"
description: C#을 사용하여 프린터 및 페이지 설정으로 기본 프린터에 PDF 파일을 인쇄할 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": ".NET Framework에서 PDF 인쇄",
    "alternativeHeadline": ".NET Framework에서 PDF 인쇄 방법",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 문서 생성",
    "keywords": "pdf, c#, .NET Framework에서의 pdf",
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
    "url": "/net/printing-pdf-in-net-framework/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-in-net-framework/"
    },
    "dateModified": "2022-02-04",
    "description": "C#을 사용하여 프린터 및 페이지 설정으로 기본 프린터에 PDF 파일을 인쇄할 수 있습니다."
}
</script>
다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리에서도 작동합니다.

## **C#에서 PDF 파일 인쇄 - 기본 프린터를 사용하여 프린터 및 페이지 설정으로 PDF 파일 인쇄**

이 문서는 C#에서 기본 프린터를 사용하여 프린터 및 페이지 설정으로 PDF 파일을 인쇄하는 방법을 설명합니다.

[PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) 클래스를 사용하면 기본 프린터에 PDF 파일을 인쇄할 수 있습니다. PdfViewer 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2) 메서드를 사용하여 PDF를 엽니다. 다른 인쇄 설정을 지정하려면 `PageSettings` 및 `PrinterSettings` 클래스를 사용합니다. 마지막으로 [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) 메서드를 호출하여 기본 프린터에 PDF를 인쇄합니다. 다음 코드 스니펫은 프린터 및 페이지 설정을 사용하여 기본 프린터에 PDF를 인쇄하는 방법을 보여줍니다.

```csharp
public static void SimplePrint()
{
    // PdfViewer 객체 생성
    PdfViewer viewer = new PdfViewer();

    // 입력 PDF 파일 열기
    viewer.BindPdf(System.IO.Path.Combine(_dataDir, "input.pdf"));

    // 인쇄 속성 설정
    viewer.AutoResize = true;         // 크기 조정하여 파일 인쇄
    viewer.AutoRotate = true;         // 회전 조정하여 파일 인쇄
    viewer.PrintPageDialog = false;   // 인쇄 시 페이지 번호 대화 상자 생성 안 함

    // 프린터 및 페이지 설정 및 PrintDocument 객체 생성
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
    System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

    // 프린터 이름 설정
    ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

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
인쇄 대화 상자를 표시하려면 다음 코드 스니펫을 사용해 보세요:

```csharp
System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
{
    // 문서 인쇄 코드는 여기에 입력하세요
    // 프린터 및 페이지 설정을 사용하여 문서 인쇄
    viewer.PrintDocumentWithSettings(pgs, ps);
}
```

