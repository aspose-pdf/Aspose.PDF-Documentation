---
title: Печать PDF в XPS-принтер
linktitle: Печать PDF в XPS-принтер (Фасады)
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/printing-pdf-to-an-xps-printer-facades/
description: На этой странице показано, как печатать PDF-файлы в XPS-принтере с помощью класса PdfViewer.
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
    "abstract": "Новая функция позволяет бесшовную печать PDF-документов напрямую на принтерах XPS с использованием класса PdfViewer в C#. Эта функциональность поддерживает настройку различных параметров печати, обеспечивая улучшенный контроль над процессом печати, включая автоматическое изменение размера и регулировку поворота. Идеально для разработчиков, эта функция упрощает интеграцию возможностей печати PDF в приложения .NET.",
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
    "description": "Эта страница показывает, как печатать PDF на принтере XPS с помощью класса PdfViewer."
}
</script>

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## **Печать PDF в XPS-принтер в C#**

Вы можете напечатать PDF-файл на XPS-принтере или другом программном принтере, используя класс [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). Для этого создайте объект класса PdfViewer и откройте PDF-файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2). Вы можете установить различные параметры печати с помощью классов [PrinterSettings](https://reference.aspose.com/pdf/net/aspose.pdf.printing/printersettings/) и [PageSettings](https://reference.aspose.com/pdf/net/aspose.pdf.printing/pagesettings/). Вам также необходимо установить свойство [PrinterName](https://reference.aspose.com/pdf/net/aspose.pdf.printing/printersettings/printername/) на XPS или другой программный принтер, который у вас установлен.

Наконец, используйте метод [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings), чтобы напечатать PDF на XPS или другом программном принтере. Следующий фрагмент кода показывает, как напечатать PDF-файл на XPS-принтере.

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

## Выбор источника бумаги по размеру страницы PDF

Начиная с версии 24.4, в диалоговом окне печати можно выбрать источник бумаги по размеру страницы PDF. Следующий фрагмент кода позволяет выбирать лоток принтера на основе размера страницы PDF.

Эту настройку можно включить и отключить с помощью фасада [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/).

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

<!-- 9597812767 -->
<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "Программное приложение",
    "название": "Библиотека Aspose.PDF for .NET",
    "изображение": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "издательство": {
        "@type": "Организация",
        "название": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "логотип": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
        "контактные точки": [
            {
                "@type": "Контактная точка",
                "телефон": "+1 903 306 1676",
                "тип
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