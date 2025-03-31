---
title: PDF를 PostScript로 변환
linktitle: PDF를 PostScript로 변환
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /ko/net/pdf-to-postscript-conversion/
description: PDF를 PostScript로 변환하는 솔루션이 있습니다. 이 작업에는 인쇄 및 PdfViewer 클래스를 사용하세요.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "PDF to PostScript conversion",
    "alternativeHeadline": "Effortlessly Convert PDF Files to PostScript Format",
    "abstract": "새로운 PDF를 PostScript로 변환하는 기능은 C#의 PdfViewer 클래스를 사용하여 PDF 문서를 PostScript 형식으로 원활하게 변환할 수 있습니다. 이 기능은 PS 프린터에 직접 파일 출력을 가능하게 하여 다양한 인쇄 환경에서 PDF 파일을 관리하고 활용하기 쉽게 합니다.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf to postscript, PDF to PostScript conversion, PdfViewer class, printing PDF documents, convert PDF files, C# PDF printing, print job status, PrinterJobName property, Aspose.PDF library, PS printer installation",
    "wordcount": "1224",
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
    "url": "/net/pdf-to-postscript-conversion/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-to-postscript-conversion/"
    },
    "dateModified": "2024-11-25",
    "description": "PDF를 PostScript로 변환하는 솔루션이 있습니다. 이 작업에는 인쇄 및 PdfViewer 클래스를 사용하세요."
}
</script>

다음 코드 스니펫은 [Aspose.PDF.Drawing](/pdf/ko/net/drawing/) 라이브러리와 함께 작동합니다.

## **C#에서 PDF를 PostScript로 변환하기**

[PdfViewer](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfviewer/) 클래스는 PDF 문서를 인쇄할 수 있는 기능을 제공하며, 이 클래스를 사용하여 PDF 파일을 PostScript 형식으로 변환할 수도 있습니다. PDF 파일을 PostScript로 변환하려면 먼저 PS 프린터를 설치하고 PdfViewer의 도움으로 파일로 인쇄하면 됩니다. PS 프린터를 설치하려면 프린터 공급업체에서 제공하는 지침을 참조하세요. 다음 코드 스니펫은 PDF를 PostScript 형식으로 인쇄하고 변환하는 방법을 보여줍니다.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintToPostscriptFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "PrintDocument.pdf");

        // Set PrinterSettings and PageSettings
        var printerSettings = new Aspose.Pdf.Printing.PrinterSettings();
        printerSettings.Copies = 1;

        // Set PS printer, one can find this driver in the list of preinstalled printer drivers in Windows
        printerSettings.PrinterName = "HP LaserJet 2300 Series PS";

        // Set output file name and PrintToFile attribute
        printerSettings.PrintFileName = dataDir + "PdfToPostScript_out.ps";
        printerSettings.PrintToFile = true;
        
        // Disable print page dialog
        viewer.PrintPageDialog = false;
        
        // Pass printer settings object to the method
        viewer.PrintDocumentWithSettings(printerSettings);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintToPostscriptFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Set PrinterSettings and PageSettings
    var printerSettings = new Aspose.Pdf.Printing.PrinterSettings();
    printerSettings.Copies = 1;

    // Set PS printer, one can find this driver in the list of preinstalled printer drivers in Windows
    printerSettings.PrinterName = "HP LaserJet 2300 Series PS";

    // Set output file name and PrintToFile attribute
    printerSettings.PrintFileName = dataDir + "PdfToPostScript_out.ps";
    printerSettings.PrintToFile = true;
        
    // Disable print page dialog
    viewer.PrintPageDialog = false;
        
    // Pass printer settings object to the method
    viewer.PrintDocumentWithSettings(printerSettings);
}
```
{{< /tab >}}
{{< /tabs >}}

## 인쇄 작업 상태 확인

PDF 파일은 물리적 프린터뿐만 아니라 Microsoft XPS Document Writer에도 인쇄할 수 있으며, [PdfViewer](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfviewer/) 클래스를 사용하여 인쇄 대화 상자를 표시하지 않고도 가능합니다. 큰 PDF 파일을 인쇄할 때는 프로세스가 오랜 시간이 걸릴 수 있으므로 사용자는 인쇄 프로세스가 완료되었는지 또는 문제가 발생했는지 확신하지 못할 수 있습니다. 인쇄 작업의 상태를 확인하려면 [PrintStatus](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfviewer/printstatus/) 속성을 사용하세요. 다음 코드 스니펫은 PDF 파일을 XPS 파일로 인쇄하고 인쇄 상태를 가져오는 방법을 보여줍니다.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckingPrintJobStatus()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Instantiate PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "PrintDocument.pdf");

        // Print the file with adjusted size
        viewer.AutoResize = true;

        // Hide printing dialog
        viewer.PrintPageDialog = false;

        // Create Printer Settings object
        var ps = new Aspose.Pdf.Printing.PrinterSettings();
        var pgs = new Aspose.Pdf.Printing.PageSettings();

        // Specify the printer name
        ps.PrinterName = "Microsoft XPS Document Writer";

        // Resultant Printout name
        ps.PrintFileName = dataDir + "CheckingPrintJobStatus_out.xps";

        // Print the output to file
        ps.PrintToFile = true;

        // Set a range of pages to print
        ps.FromPage = 1;
        ps.ToPage = 2;
        ps.PrintRange = Aspose.Pdf.Printing.PrintRange.SomePages;

        // Specify the page size of printout
        pgs.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;
        ps.DefaultPageSettings.PaperSize = pgs.PaperSize;

        // Specify page margins
        pgs.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);

        // Print the document with settings specified above
        viewer.PrintDocumentWithSettings(pgs, ps);

        // Check the print status
        if (viewer.PrintStatus != null)
        {
            // An exception was thrown
            if (viewer.PrintStatus is Exception ex)
            {
                // Get exception message
                Console.WriteLine(ex.Message);
            }
        }
        else
        {
            // No errors were found. Printing job has completed successfully
            Console.WriteLine("Printing completed without any issue.");
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckingPrintJobStatus()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Instantiate PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Print the file with adjusted size
    viewer.AutoResize = true;

    // Hide printing dialog
    viewer.PrintPageDialog = false;

    // Create Printer Settings object
    var ps = new Aspose.Pdf.Printing.PrinterSettings();
    var pgs = new Aspose.Pdf.Printing.PageSettings();

    // Specify the printer name
    ps.PrinterName = "Microsoft XPS Document Writer";

    // Resultant Printout name
    ps.PrintFileName = dataDir + "CheckingPrintJobStatus_out.xps";

    // Print the output to file
    ps.PrintToFile = true;

    // Set a range of pages to print
    ps.FromPage = 1;
    ps.ToPage = 2;
    ps.PrintRange = Aspose.Pdf.Printing.PrintRange.SomePages;

    // Specify the page size of printout
    pgs.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;
    ps.DefaultPageSettings.PaperSize = pgs.PaperSize;

    // Specify page margins
    pgs.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);

    // Print the document with settings specified above
    viewer.PrintDocumentWithSettings(pgs, ps);

    // Check the print status
    if (viewer.PrintStatus != null)
    {
        // An exception was thrown
        if (viewer.PrintStatus is Exception ex)
        {
            // Get exception message
            Console.WriteLine(ex.Message);
        }
    }
    else
    {
        // No errors were found. Printing job has completed successfully
        Console.WriteLine("Printing completed without any issue.");
    }
}
```
{{< /tab >}}
{{< /tabs >}}

## 인쇄 작업 소유자 이름 가져오기/설정하기

때때로 인쇄 작업 소유자 이름(즉, 웹 페이지에서 인쇄 버튼을 누른 실제 사용자)을 가져오거나 설정해야 할 필요가 있습니다. 이 정보는 PDF 파일을 인쇄할 때 필요합니다. 이 요구 사항을 충족하기 위해 [PrinterJobName](https://reference.aspose.com/pdf/ko/net/aspose.pdf.facades/pdfviewer/printerjobname/) 속성이 사용됩니다.

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrinterJobName()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "PrintDocument.pdf");

        // Specify the name of Print job
        viewer.PrinterJobName = GetCurrentUserCredentials();

        // Fill the necessary settings and print the documents, as shown in examples in this section
    }
}

private static string GetCurrentUserCredentials()
{
    // The implementation depends on type of running application (ASP.NET, Windows forms, etc.)
    var userCredentials = string.Empty;
    return userCredentials;
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetPrinterJobName()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Specify the name of Print job
    viewer.PrinterJobName = GetCurrentUserCredentials();

    // Fill the necessary settings and print the documents, as shown in examples in this section
}

private static string GetCurrentUserCredentials()
{
    // The implementation depends on type of running application (ASP.NET, Windows forms, etc.)
    var userCredentials = string.Empty;
    return userCredentials;
}
```
{{< /tab >}}
{{< /tabs >}}

## 임시 사용자 사용하기

인쇄 작업 소유자 이름을 가져오는 또 다른 방법은 임시 사용자(다른 사용자 컨텍스트에서 인쇄 루틴 실행)를 사용하는 것이며, 사용자는 SetJob 루틴을 사용하여 소유자 이름을 직접 변경할 수 있습니다.

보안 고려 사항으로 인해 Aspose.PDF 인쇄 API를 사용하여 소유자 값을 설정할 수 있는 가능성은 없습니다. PrinterJobName 속성은 스풀러 인쇄 애플리케이션에서 문서 이름 열 값을 설정하는 데 사용될 수 있습니다. 위에서 공유한 코드 스니펫은 사용자가 문서 이름 열에 사용자 이름을 추가하는 방법을 보여줍니다(예: UserName\documentName 구문 사용). 그러나 소유자 열의 설정은 사용자가 다음과 같은 방법으로 직접 구현할 수 있습니다:

1) 임시 사용자. 소유자 열 값은 인쇄 코드를 실행하는 사용자의 값을 포함하므로, 다른 사용자 컨텍스트 내에서 Aspose.PDF 인쇄 API를 호출할 수 있는 방법이 있습니다. 예를 들어, 여기에서 설명된 솔루션을 참조하세요. [이 임시 사용자 클래스](https://www.codeproject.com/articles/10090/a-small-csharp-class-for-impersonating-a-user)를 사용하면 사용자가 목표를 달성할 수 있습니다:

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintWithImpersonation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "PrintDocument.pdf");

        // Do not produce the page number dialog when printing
        viewer.PrintPageDialog = false;

        // Impersonate another user
        using (new Impersonator("OwnerUserName", "SomeDomain", "OwnerUserPassword"))
        {
            // Set PrinterSettings
            var ps = new Aspose.Pdf.Printing.PrinterSettings();

            // Set the name of the printer
            ps.PrinterName = "Microsoft XPS Document Writer";

            // Pass printer settings object to the method
            viewer.PrintDocumentWithSettings(ps); // OwnerUserName is a value of Owner column in spooler app
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintWithImpersonation()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    // Create PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "PrintDocument.pdf");

    // Do not produce the page number dialog when printing
    viewer.PrintPageDialog = false;

    // Impersonate another user
    using var impersonator = new Impersonator("OwnerUserName", "SomeDomain", "OwnerUserPassword");

    // Set PrinterSettings
    var ps = new Aspose.Pdf.Printing.PrinterSettings();

    // Set the name of the printer
    ps.PrinterName = "Microsoft XPS Document Writer";

    // Pass printer settings object to the method
    viewer.PrintDocumentWithSettings(ps); // OwnerUserName is a value of Owner column in spooler app
}
```
{{< /tab >}}
{{< /tabs >}}

2) 스풀러 API 및 SetJob 루틴 사용하기

다음 코드 스니펫은 PDF 파일의 일부 페이지를 단면 인쇄하고 일부 페이지를 양면 인쇄하는 방법을 보여줍니다.

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
struct PrintingJobSettings
{
    public int ToPage { get; set; }
    public int FromPage { get; set; }
    public string OutputFile { get; set; }
    public Aspose.Pdf.Printing.Duplex Mode { get; set; }
}

private static void PrintUsingSpoolerApi()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    int printingJobIndex = 0;
    string outputDir = dataDir;
    var printingJobs = new List<PrintingJobSettings>();

    // Create multiple printing jobs to print different page ranges with different duplex settings
    var printingJob1 = new PrintingJobSettings();
    printingJob1.FromPage = 1;
    printingJob1.ToPage = 3;
    printingJob1.OutputFile = outputDir + "PrintUsingSpoolerApi_p1-3_out.xps";
    printingJob1.Mode = Aspose.Pdf.Printing.Duplex.Default;

    printingJobs.Add(printingJob1);

    PrintingJobSettings printingJob2 = new PrintingJobSettings();
    printingJob2.FromPage = 4;
    printingJob2.ToPage = 6;
    printingJob2.OutputFile = outputDir + "PrintUsingSpoolerApi_p4-6_out.xps";
    printingJob2.Mode = Aspose.Pdf.Printing.Duplex.Simplex;

    printingJobs.Add(printingJob2);

    PrintingJobSettings printingJob3 = new PrintingJobSettings();
    printingJob3.FromPage = 7;
    printingJob3.ToPage = 7;
    printingJob3.OutputFile = outputDir + "PrintUsingSpoolerApi_p7_out.xps";
    printingJob3.Mode = Aspose.Pdf.Printing.Duplex.Default;

    printingJobs.Add(printingJob3);

    // Create PdfViewer object
    using (var viewer = new Aspose.Pdf.Facades.PdfViewer())
    {
        // Bind PDF document
        viewer.BindPdf(dataDir + "Print-PageRange.pdf");

        // Set attributes for printing
        // Print the file with adjusted size
        viewer.AutoResize = true;
        // Print the file with adjusted rotation
        viewer.AutoRotate = true;
        // Do not produce the page number dialog when printing
        viewer.PrintPageDialog = false;

        // Create objects for printer and page settings
        var ps = new Aspose.Pdf.Printing.PrinterSettings();
        var pgs = new Aspose.Pdf.Printing.PageSettings();

        // Set printer name
        ps.PrinterName = "Microsoft XPS Document Writer";

        // Set output file name and PrintToFile attribute
        ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
        ps.PrintToFile = true;

        // Set parameters for the first print job
        ps.FromPage = printingJobs[printingJobIndex].FromPage;
        ps.ToPage = printingJobs[printingJobIndex].ToPage;
        ps.Duplex = printingJobs[printingJobIndex].Mode;
        ps.PrintRange = Aspose.Pdf.Printing.PrintRange.SomePages;

        // Set paper size and margins
        pgs.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;
        ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
        pgs.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);

        // Chain other print jobs at the end of the finished job
        viewer.EndPrint += (sender, args) =>
        {
            if (++printingJobIndex < printingJobs.Count)
            {
                // Set the next print job parameters
                ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
                ps.FromPage = printingJobs[printingJobIndex].FromPage;
                ps.ToPage = printingJobs[printingJobIndex].ToPage;
                ps.Duplex = printingJobs[printingJobIndex].Mode;

                // Run the next print job
                viewer.PrintDocumentWithSettings(pgs, ps);
            }
        };

        // Run the first print job
        viewer.PrintDocumentWithSettings(pgs, ps);
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

struct PrintingJobSettings
{
    public int ToPage { get; set; }
    public int FromPage { get; set; }
    public string OutputFile { get; set; }
    public Aspose.Pdf.Printing.Duplex Mode { get; set; }
}

private static void PrintUsingSpoolerApi()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Printing();

    int printingJobIndex = 0;
    var printingJobs = new List<PrintingJobSettings>();

    // Create multiple printing jobs to print different page ranges with different duplex settings
    var printingJob1 = new PrintingJobSettings();
    printingJob1.FromPage = 1;
    printingJob1.ToPage = 3;
    printingJob1.OutputFile = dataDir + "PrintUsingSpoolerApi_p1-3_out.xps";
    printingJob1.Mode = Aspose.Pdf.Printing.Duplex.Default;

    printingJobs.Add(printingJob1);

    PrintingJobSettings printingJob2 = new PrintingJobSettings();
    printingJob2.FromPage = 4;
    printingJob2.ToPage = 6;
    printingJob2.OutputFile = dataDir + "PrintUsingSpoolerApi_p4-6_out.xps";
    printingJob2.Mode = Aspose.Pdf.Printing.Duplex.Simplex;

    printingJobs.Add(printingJob2);

    PrintingJobSettings printingJob3 = new PrintingJobSettings();
    printingJob3.FromPage = 7;
    printingJob3.ToPage = 7;
    printingJob3.OutputFile = dataDir + "PrintUsingSpoolerApi_p7_out.xps";
    printingJob3.Mode = Aspose.Pdf.Printing.Duplex.Default;

    printingJobs.Add(printingJob3);

    // Create PdfViewer object
    using var viewer = new Aspose.Pdf.Facades.PdfViewer();

    // Bind PDF document
    viewer.BindPdf(dataDir + "Print-PageRange.pdf");

    // Set attributes for printing
    // Print the file with adjusted size
    viewer.AutoResize = true;
    // Print the file with adjusted rotation
    viewer.AutoRotate = true;
    // Do not produce the page number dialog when printing
    viewer.PrintPageDialog = false;

    // Create objects for printer and page settings
    var ps = new Aspose.Pdf.Printing.PrinterSettings();
    var pgs = new Aspose.Pdf.Printing.PageSettings();

    // Set printer name
    ps.PrinterName = "Microsoft XPS Document Writer";

    // Set output file name and PrintToFile attribute
    ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
    ps.PrintToFile = true;

    // Set parameters for the first print job
    ps.FromPage = printingJobs[printingJobIndex].FromPage;
    ps.ToPage = printingJobs[printingJobIndex].ToPage;
    ps.Duplex = printingJobs[printingJobIndex].Mode;
    ps.PrintRange = Aspose.Pdf.Printing.PrintRange.SomePages;

    // Set paper size and margins
    pgs.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;
    ps.DefaultPageSettings.PaperSize = pgs.PaperSize;
    pgs.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);

    // Chain other print jobs at the end of the finished job
    viewer.EndPrint += (sender, args) =>
    {
        if (++printingJobIndex < printingJobs.Count)
        {
            // Set the next print job parameters
            ps.PrintFileName = Path.GetFullPath(printingJobs[printingJobIndex].OutputFile);
            ps.FromPage = printingJobs[printingJobIndex].FromPage;
            ps.ToPage = printingJobs[printingJobIndex].ToPage;
            ps.Duplex = printingJobs[printingJobIndex].Mode;

            // Run the next print job
            viewer.PrintDocumentWithSettings(pgs, ps);
        }
    };

    // Run the first print job
    viewer.PrintDocumentWithSettings(pgs, ps);
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