---
title: PDF 到 PostScript 转换
linktitle: PDF 到 PostScript 转换
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /zh/net/pdf-to-postscript-conversion/
description: 我们有一个 PDF 到 PostScript 转换的解决方案。使用打印和 PdfViewer 类来完成此任务。
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
    "abstract": "新的 PDF 到 PostScript 转换功能允许使用 C# 中的 PdfViewer 类无缝地将 PDF 文档转换为 PostScript 格式。此功能通过使文件直接输出到 PS 打印机来增强您的打印工作流程，使在各种打印环境中管理和利用 PDF 文件变得更加容易。",
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
    "description": "我们有一个 PDF 到 PostScript 转换的解决方案。使用打印和 PdfViewer 类来完成此任务。"
}
</script>

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## **C# 中的 PDF 到 Postscript**

[PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/) 类提供打印 PDF 文档的能力，并且借助此类，我们还可以将 PDF 文件转换为 PostScript 格式。要将 PDF 文件转换为 PostScript，首先安装任何 PS 打印机，然后借助 PdfViewer 打印到文件。有关安装 PS 打印机的说明，请参考您的打印机供应商提供的说明。以下代码片段向您展示如何打印并将 PDF 转换为 PostScript 格式。

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

## 检查打印作业状态

PDF 文件可以打印到物理打印机，也可以打印到 Microsoft XPS Document Writer，而无需显示打印对话框，使用 [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/) 类。当打印大型 PDF 文件时，过程可能需要很长时间，因此用户可能不确定打印过程是否完成或遇到问题。要确定打印作业的状态，请使用 [PrintStatus](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/printstatus/) 属性。以下代码片段向您展示如何将 PDF 文件打印到 XPS 文件并获取打印状态。

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

## 获取/设置打印作业所有者名称

有时需要获取或设置打印作业所有者名称（即，实际在网页上按下打印按钮的用户）。在打印 PDF 文件时需要此信息。为了实现此要求，使用属性 [PrinterJobName](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/printerjobname/)。

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

## 使用 impersonation

获取打印作业所有者名称的另一种方法是使用 impersonation（在另一个用户上下文中运行打印例程），或者用户可以通过使用 SetJob 例程直接更改所有者名称。

请注意，由于安全考虑，无法使用 Aspose.PDF 打印 API 设置所有者值。属性 PrinterJobName 可用于在后台打印应用程序中设置文档名称列的值。上面共享的代码片段仅显示用户如何将用户名加入文档名称列（例如使用语法 UserName\documentName）。但是，所有者列的设置可以通过用户直接以以下方式实现：

1) Impersonation。由于所有者列的值包含运行打印代码的用户的值，因此可以在另一个用户上下文中调用 Aspose.PDF 打印 API。例如，请查看此处描述的解决方案。使用 [这个 Impersonator 类](https://www.codeproject.com/articles/10090/a-small-csharp-class-for-impersonating-a-user)，用户可以实现目标：

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

2) 使用 Spooler API 和 SetJob 例程

以下代码片段展示了如何在单面模式下打印 PDF 文件的某些页面，以及在双面模式下打印某些页面。

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