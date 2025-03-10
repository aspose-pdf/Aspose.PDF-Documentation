---
title: PDFをXPSプリンターに印刷する
linktitle: PDFをXPSプリンターに印刷する（ファサード）
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/printing-pdf-to-an-xps-printer-facades/
description: このページでは、PdfViewerクラスを使用してPDFをXPSプリンターに印刷する方法を示します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Printing PDF to an XPS Printer",
    "alternativeHeadline": "Print PDFs Directly to XPS Printers with Ease",
    "abstract": "新機能により、C#のPdfViewerクラスを使用してPDF文書をXPSプリンターに直接印刷することが可能になりました。この機能は、さまざまな印刷設定を構成できるため、印刷プロセスに対する制御が強化され、自動サイズ変更や回転調整を含むことができます。開発者に最適なこの機能は、.NETアプリケーションへのPDF印刷機能の統合を簡素化します。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "print pdf to xps, PdfViewer class, print document settings, C# PDF printing, XPS printer, printer settings, page settings, choose paper tray, soft printer, Aspose.PDF library",
    "wordcount": "458",
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
    "url": "/net/printing-pdf-to-an-xps-printer-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-to-an-xps-printer-facades/"
    },
    "dateModified": "2024-11-25",
    "description": "このページでは、PdfViewerクラスを使用してPDFをXPSプリンターに印刷する方法を示します。"
}
</script>

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

## **C#でPDFをXPSプリンターに印刷する**

[PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer)クラスを使用して、PDFファイルをXPSプリンターまたは他のソフトプリンターに印刷できます。そのためには、PdfViewerクラスのオブジェクトを作成し、[BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2)メソッドを使用してPDFファイルを開きます。さまざまな印刷設定は、[PrinterSettings](https://reference.aspose.com/pdf/net/aspose.pdf.printing/printersettings/)および[PageSettings](https://reference.aspose.com/pdf/net/aspose.pdf.printing/pagesettings/)クラスを使用して設定できます。また、[PrinterName](https://reference.aspose.com/pdf/net/aspose.pdf.printing/printersettings/printername/)プロパティを、インストールされているXPSまたは他のソフトプリンターに設定する必要があります。

最後に、[PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings)メソッドを使用して、PDFをXPSまたは他のソフトプリンターに印刷します。次のコードスニペットは、PDFファイルをXPSプリンターに印刷する方法を示しています。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintToXpsPrinter()
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

        // Set XPS/PDF printer name
        ps.PrinterName = "Microsoft XPS Document Writer";
        // Or set the PDF printer
        // ps.PrinterName = "Adobe PDF";

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
private static void PrintToXpsPrinter()
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

    // Set XPS/PDF printer name
    ps.PrinterName = "Microsoft XPS Document Writer";
    // Or set the PDF printer
    // ps.PrinterName = "Adobe PDF";

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

## PDFページサイズによる用紙ソースの選択
 
24.4リリース以降、印刷ダイアログでPDFページサイズによる用紙ソースの選択が可能になりました。次のコードスニペットは、PDFのページサイズに基づいてプリンタートレイを選択することを可能にします。

この設定は、[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/)ファサードを使用してオンオフできます。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PickTrayByPdfSizeFacade()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create the PdfContentEditor facade
    using (var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor())
    {
        // Bind PDF document
        contentEditor.BindPdf(dataDir + "PrintDocument.pdf");

        // Set the flag to choose a paper tray using the PDF page size
        contentEditor.ChangeViewerPreference(ViewerPreference.PickTrayByPDFSize);

        // Save PDF document
        contentEditor.Save(dataDir + "PickTrayByPdfSizeFacade_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PickTrayByPdfSizeFacade()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create the PdfContentEditor facade
    using var contentEditor = new Aspose.Pdf.Facades.PdfContentEditor();

    // Bind PDF document
    contentEditor.BindPdf(dataDir + "PrintDocument.pdf");

    // Set the flag to choose a paper tray using the PDF page size
    contentEditor.ChangeViewerPreference(ViewerPreference.PickTrayByPDFSize);
    // Save PDF document
    contentEditor.Save(dataDir + "PickTrayByPdfSizeFacade_out.pdf");
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