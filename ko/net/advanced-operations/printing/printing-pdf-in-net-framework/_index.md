---
title: .NET Framework에서 PDF 인쇄
linktitle: .NET Framework에서 PDF 인쇄
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ko/net/printing-pdf-in-net-framework/
description: C#을 사용하여 기본 프린터에 PDF 파일을 인쇄할 수 있습니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Printing PDF in .NET Framework",
    "alternativeHeadline": "Print PDF Files Easily with C# in .NET Framework",
    "abstract": "C#을 사용하여 기본 프린터에 PDF 파일을 원활하게 인쇄할 수 있는 새로운 기능을 소개합니다. 사용자 정의 가능한 프린터 및 페이지 설정을 통해 개발자는 인쇄 옵션을 쉽게 관리하고 PDF 페이지 크기에 따라 출력을 최적화하여 운영 효율성과 사용자 경험을 향상시킬 수 있습니다. 이 기능은 .NET 애플리케이션에 PDF 인쇄 기능을 통합하는 과정을 간소화합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "print pdf, C# print pdf, .NET Framework, PdfViewer class, Printer and Page Settings, PrintDocumentWithSettings, choose paper source, PDF page size, Aspose.PDF, document printing",
    "wordcount": "503",
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
    "url": "/net/printing-pdf-in-net-framework/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-in-net-framework/"
    },
    "dateModified": "2024-11-25",
    "description": "C#을 사용하여 기본 프린터에 PDF 파일을 인쇄할 수 있습니다."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리와 함께 작동합니다.

## **C#에서 PDF 파일 인쇄 - 프린터 및 페이지 설정을 사용하여 기본 프린터에 PDF 파일 인쇄하기**

이 문서에서는 C#에서 프린터 및 페이지 설정을 사용하여 기본 프린터에 PDF 파일을 인쇄하는 방법을 설명합니다.

[PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) 클래스는 PDF 파일을 기본 프린터에 인쇄할 수 있도록 합니다. PdfViewer 객체를 생성하고 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2) 메서드를 사용하여 PDF를 엽니다. 다양한 인쇄 설정을 지정하려면 [PageSettings](https://reference.aspose.com/pdf/net/aspose.pdf.printing/pagesettings/) 및 [PrinterSettings](https://reference.aspose.com/pdf/net/aspose.pdf.printing/printersettings/) 클래스를 사용하십시오. 마지막으로 [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) 메서드를 호출하여 PDF를 기본 프린터에 인쇄합니다. 다음 코드 스니펫은 프린터 및 페이지 설정으로 PDF를 기본 프린터에 인쇄하는 방법을 보여줍니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SimplePrint()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "PrintDocument.pdf");

        // Set attributes for printing
        // Print the file with adjusted size
        viewer.AutoResize = true;
        // Print the file with adjusted rotation
        viewer.AutoRotate = true;
        // Do not produce the page number dialog when printing
        viewer.PrintPageDialog = false;

        // Create objects for printer and page settings and PrintDocument
        var ps = new Aspose.Pdf.Printing.PrinterSettings();
        var pgs = new Aspose.Pdf.Printing.PageSettings();
        var prtdoc = new System.Drawing.Printing.PrintDocument();

        // Set printer name
        ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

        // Set PageSize (if required)
        pgs.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;

        // Set PageMargins (if required)
        pgs.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);

        // Print document using printer and page settings
        viewer.PrintDocumentWithSettings(pgs, ps);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SimplePrint()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Set attributes for printing
    // Print the file with adjusted size
    viewer.AutoResize = true;
    // Print the file with adjusted rotation
    viewer.AutoRotate = true;
    // Do not produce the page number dialog when printing
    viewer.PrintPageDialog = false;

    // Create objects for printer and page settings and PrintDocument
    var ps = new Aspose.Pdf.Printing.PrinterSettings();
    var pgs = new Aspose.Pdf.Printing.PageSettings();
    var prtdoc = new System.Drawing.Printing.PrintDocument();

    // Set printer name
    ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

    // Set PageSize (if required)
    pgs.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;

    // Set PageMargins (if required)
    pgs.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);

    // Print document using printer and page settings
    viewer.PrintDocumentWithSettings(pgs, ps);
}
```
{{< /tab >}}
{{< /tabs >}}

인쇄 대화 상자를 표시하려면 다음 코드 스니펫을 사용해 보십시오:

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintWithPrintDialog()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "PrintDocument.pdf");

        // Set attributes for printing
        // Print the file with adjusted size
        viewer.AutoResize = true;
        // Print the file with adjusted rotation
        viewer.AutoRotate = true;
        // Do not produce the page number dialog when printing
        viewer.PrintPageDialog = false;

        var printDialog = new System.Windows.Forms.PrintDialog();
        if (printDialog.ShowDialog() == DialogResult.OK)
        {
            // Document printing code goes here

            // Convert PrinterSettings and PageSettings to Aspose.PDF counterparts via extension methods
            // provided in the Aspose.Pdf.Printing namespace
            Aspose.Pdf.Printing.PrinterSettings ps = printDialog.PrinterSettings.ToAsposePrinterSettings();
            Aspose.Pdf.Printing.PageSettings pgs = printDialog.PrinterSettings.DefaultPageSettings.ToAsposePageSettings();

            // Print document using printer and page settings
            viewer.PrintDocumentWithSettings(pgs, ps);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintWithPrintDialog()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Set attributes for printing
    // Print the file with adjusted size
    viewer.AutoResize = true;
    // Print the file with adjusted rotation
    viewer.AutoRotate = true;
    // Do not produce the page number dialog when printing
    viewer.PrintPageDialog = false;

    var printDialog = new System.Windows.Forms.PrintDialog();
    if (printDialog.ShowDialog() == DialogResult.OK)
    {
        // Document printing code goes here

        // Convert PrinterSettings and PageSettings to Aspose.PDF counterparts via extension methods
        // provided in the Aspose.Pdf.Printing namespace
        Aspose.Pdf.Printing.PrinterSettings ps = printDialog.PrinterSettings.ToAsposePrinterSettings();
        Aspose.Pdf.Printing.PageSettings pgs = printDialog.PrinterSettings.DefaultPageSettings.ToAsposePageSettings();

        // Print document using printer and page settings
        viewer.PrintDocumentWithSettings(pgs, ps);
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## PDF 페이지 크기로 용지 출처 선택하기
 
24.4 릴리스 이후, 인쇄 대화 상자에서 PDF 페이지 크기로 용지 출처를 선택할 수 있습니다. 다음 코드 스니펫은 PDF의 페이지 크기에 따라 프린터 트레이를 선택할 수 있게 합니다.

이 선호도는 [Document.PickTrayByPdfSize](https://reference.aspose.com/pdf/net/aspose.pdf/document/picktraybypdfsize/) 속성을 사용하여 켜고 끌 수 있습니다.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PickTrayByPdfSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello world!"));

        // Set the flag to choose a paper tray using the PDF page size
        document.PickTrayByPdfSize = true;

        // Save PDF document
        document.Save(dataDir + "PickTrayByPdfSize_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PickTrayByPdfSize()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Add page
    var page = document.Pages.Add();
    page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello world!"));

    // Set the flag to choose a paper tray using the PDF page size
    document.PickTrayByPdfSize = true;

    // Save PDF document
    document.Save(dataDir + "PickTrayByPdfSize_out.pdf");
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