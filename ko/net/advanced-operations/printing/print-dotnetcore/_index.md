---
title: .NET Core에서 PDF 파일 인쇄하는 방법
linktitle: .NET Core에서 PDF 인쇄
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ko/net/print-dotnetcore/
description: 이 페이지는 .NET Core에서 PDF 문서를 XPS로 변환하고 로컬 프린터의 큐에 작업으로 추가하는 방법을 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to print PDF file in .NET Core",
    "alternativeHeadline": "Print PDFs as XPS in .NET Core with ease",
    "abstract": ".NET Core에서 PDF 문서를 XPS 형식으로 변환하고 로컬 프린터 대기열에서 인쇄 작업을 효율적으로 관리하는 프로세스를 간소화하는 새로운 기능을 발견하세요. 이 기능은 PDF 페이지 크기에 따라 용지 소스를 보다 세밀하게 제어할 수 있어 맞춤형 인쇄 경험을 보장합니다. 인쇄 대화 상자에서 직접 정밀한 배율 옵션으로 문서 관리를 최적화하세요.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "print PDF, .NET Core, convert PDF to XPS, print queue, Aspose.PDF, paper source by PDF page size, print dialog presets, page scaling, document printing, local printer",
    "wordcount": "1277",
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
    "url": "/net/print-dotnetcore/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/print-dotnetcore/"
    },
    "dateModified": "2025-04-07",
    "description": "이 페이지는 PDF 문서를 XPS로 변환하고 이를 로컬 프린터의 대기열에 작업으로 추가하는 방법을 설명합니다."
}
</script>

다음 코드 조각은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와도 함께 작동합니다.

## **.NET Core에서 Pdf 문서 인쇄하기**

Aspose.PDF 라이브러리를 사용하면 PDF 파일을 XPS로 변환할 수 있습니다. 이 기능은 문서 인쇄를 구성하는 데 유용할 수 있습니다. 기본 프린터를 사용하는 예제를 살펴보겠습니다.

이 예제에서는 PDF 문서를 XPS로 변환하고 로컬 프린터의 큐에 작업으로 추가합니다:

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintWithNetCore()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create the secondary thread and pass the printing method for
    // the constructor's ThreadStart delegate parameter.
    var printingThread = new Thread(() => PrintPDF(dataDir + "PrintDocument.pdf"));

    // Set the thread that will use PrintQueue.AddJob to single threading.
    printingThread.SetApartmentState(ApartmentState.STA);

    // Start the printing thread. The method passed to the Thread
    // constructor will execute.
    printingThread.Start();

    // Wait for the printing thread to finish its work
    printingThread.Join();
}

private static void PrintPDF(string pdfFileName)
{
    // Create print server and print queue.
    var defaultPrintQueue = LocalPrintServer.GetDefaultPrintQueue();

    // Convert PDF to XPS
    using (var document = new Aspose.Pdf.Document(pdfFileName))
    {
        var xpsFileName = pdfFileName.Replace(".pdf", ".xps");
        document.Save(xpsFileName, SaveFormat.Xps);

        // Print the Xps file while providing XPS validation and progress notifications.
        using (PrintSystemJobInfo xpsPrintJob = defaultPrintQueue.AddJob(xpsFileName, xpsFileName, false))
        {
            Console.WriteLine(xpsPrintJob.JobIdentifier);
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintWithNetCore()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create the secondary thread and pass the printing method for
    // the constructor's ThreadStart delegate parameter.
    var printingThread = new Thread(() => PrintPDF(dataDir + "PrintDocument.pdf"));

    // Set the thread that will use PrintQueue.AddJob to single threading.
    printingThread.SetApartmentState(ApartmentState.STA);

    // Start the printing thread. The method passed to the Thread
    // constructor will execute.
    printingThread.Start();

    // Wait for the printing thread to finish its work
    printingThread.Join();
}

private static void PrintPDF(string pdfFileName)
{
    // Create print server and print queue.
    var defaultPrintQueue = LocalPrintServer.GetDefaultPrintQueue();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(pdfFileName);

    // Convert PDF to XPS
    var xpsFileName = pdfFileName.Replace(".pdf", ".xps");
    document.Save(xpsFileName,SaveFormat.Xps);

    // Print the Xps file while providing XPS validation and progress notifications.
    using PrintSystemJobInfo xpsPrintJob = defaultPrintQueue.AddJob(xpsFileName, xpsFileName, false);
    Console.WriteLine(xpsPrintJob.JobIdentifier);
}
```
{{< /tab >}}
{{< /tabs >}}

## PDF 페이지 크기에 따른 용지 소스 선택
 
24.4 릴리스부터는 인쇄 대화 상자에서 PDF 페이지 크기에 따라 용지 소스를 선택할 수 있습니다. 다음 코드 조각은 PDF의 페이지 크기에 따라 프린터 트레이를 선택할 수 있도록 합니다.

이 설정은 [Document.PickTrayByPdfSize](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/picktraybypdfsize/) 속성을 사용하여 켜고 끌 수 있습니다.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
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

## 인쇄 대화 상자 사전 설정 페이지 스케일링

다음 코드 조각은 [PrintScaling](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/printscaling/) 속성이 올바르게 적용되고 PDF에 저장되도록 하는 데 사용됩니다.

[PrintScaling](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/printscaling/) 속성은 `​​Aspose.Pdf.PrintScaling.AppDefault` 또는 `Aspose.Pdf.PrintScaling.None` 값을 가진 [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document/) 클래스에 추가되었습니다.

이 문서에 대한 인쇄 대화 상자가 표시될 때 선택할 페이지 스케일링 옵션입니다. 유효한 값은 페이지 스케일링을 적용하지 않음을 나타내는 `None`과 준수하는 리더의 기본 인쇄 스케일링을 나타내는 `AppDefault`입니다. 이 항목에 인식할 수 없는 값이 있는 경우 `AppDefault`가 사용되어야 합니다. 기본값: `AppDefault`.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintScaling()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        document.Pages.Add();

        // Disable print scaling
        document.PrintScaling = PrintScaling.None;

        // Save PDF document
        document.Save(dataDir + "SetPrintScaling_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrintScaling()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();

    // Add page
    document.Pages.Add();

    // Disable print scaling
    document.PrintScaling = PrintScaling.None;

    // Save PDF document
    document.Save(dataDir + "SetPrintScaling_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 단일 인쇄 작업에서 여러 PDF 문서 인쇄하기

때로는 여러 관련 문서를 단일 인쇄 작업으로 함께 인쇄해야 할 필요가 있습니다. 이렇게 하면 특히 원격 네트워크 프린터를 사용할 때 이러한 문서가 다른 사용자의 출력과 섞이지 않습니다. Aspose.PDF는 [PdfViewer](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfviewer) 클래스의 정적 `PrintDocuments` 메서드를 통해 공유 프린터 설정으로 여러 문서를 단일 인쇄 작업으로 인쇄하는 것을 지원합니다. 인쇄할 문서는 파일 경로, 문서 스트림 또는 [Document](https://reference.aspose.com/pdf/ko/net/aspose.pdf/document) 객체로 제공될 수 있습니다.

{{% alert color="primary" %}}

여러 문서를 인쇄할 때 [PrinterSettings.PrintRange](https://reference.aspose.com/pdf/ko/net/aspose.pdf.printing/printersettings/printrange/) 속성은 무시되며 모든 문서가 전체로 인쇄됩니다.

{{% /alert %}}

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintingMultipleDocumentsInSingleJob()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Paths to documents to be printed
    var path1 = dataDir + "PrintDocument.pdf";
    var path2 = dataDir + "Print-PageRange.pdf";
    var path3 = dataDir + "35925_1_3.xps";
    
    // Set up printer and page settings
    var printDocument = new System.Drawing.Printing.PrintDocument();
    Aspose.Pdf.Printing.PrinterSettings printerSettings = new Aspose.Pdf.Printing.PrinterSettings();
    printerSettings.PrinterName = printDocument.PrinterSettings.PrinterName;
    
    Aspose.Pdf.Printing.PageSettings pageSettings = new Aspose.Pdf.Printing.PageSettings();
    pageSettings.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;
    pageSettings.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);
    
    // Print multiple documents in a single print job
    Aspose.Pdf.Facades.PdfViewer.PrintDocuments(printerSettings, pageSettings, path1, path2, path3);
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintingMultipleDocumentsInSingleJob()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Paths to documents to be printed
    var path1 = dataDir + "PrintDocument.pdf";
    var path2 = dataDir + "Print-PageRange.pdf";
    var path3 = dataDir + "35925_1_3.xps";
    
    // Set up printer and page settings
    var printDocument = new System.Drawing.Printing.PrintDocument();
    Aspose.Pdf.Printing.PrinterSettings printerSettings = new Aspose.Pdf.Printing.PrinterSettings
    {
        PrinterName = printDocument.PrinterSettings.PrinterName
    };
    
    Aspose.Pdf.Printing.PageSettings pageSettings = new Aspose.Pdf.Printing.PageSettings
    {
        PaperSize = Aspose.Pdf.Printing.PaperSizes.A4,
        Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0)
    };
    
    // Print multiple documents in a single print job
    Aspose.Pdf.Facades.PdfViewer.PrintDocuments(printerSettings, pageSettings, path1, path2, path3);
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