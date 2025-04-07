---
title: PDF印刷の操作 - ファサード
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/working-with-pdf-printing-facades/
description: このセクションでは、PdfFileEditorクラスを使用してAspose.PDFファサードでPDFファイルを印刷する方法を説明します。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with PDF printing - Facades",
    "alternativeHeadline": "Enhancing PDF Printing Capabilities with C#",
    "abstract": "Aspose.PDF for .NETファサード機能は、プリンター設定や出力形式に対する制御を強化し、PDF印刷を簡素化します。ユーザーは、デフォルトまたは仮想プリンターに文書をシームレスに印刷し、ページレイアウトを定義し、単面または両面モードで印刷ジョブを管理することができます。また、グレースケールで印刷したり、印刷ダイアログを非表示にするオプションがその多様性を高めています。この機能はPDF文書の印刷ワークフローを大幅に最適化し、効率的な文書管理ソリューションを求める開発者やユーザーに最適です。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "3818",
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
    "url": "/net/working-with-pdf-printing-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-pdf-printing-facades/"
    },
    "dateModified": "2025-04-07",
    "description": "Aspose.PDFは、単純で簡単なタスクだけでなく、より複雑な目標にも対応できます。次のセクションでは、上級ユーザーと開発者向けの情報を確認してください。"
}
</script>

## デフォルトプリンターへのPDFファイルの印刷とページ設定

まず、文書は画像に変換され、その後プリンターで印刷されます。
[PdfViewer](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfviewer)クラスのインスタンスを作成し、PDFファイルをデフォルトプリンターに印刷できるようにし、[BindPdf](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfviewer/bindpdf/)メソッドを使用して文書を開き、必要な設定を変更します。この例ではA4形式、縦向きを使用しています。[PrinterSettings](https://reference.aspose.com/pdf/ja/net/aspose.pdf.printing/printersettings/)では、まず印刷先のプリンター名を設定する必要があります。さもなければ、デフォルトプリンターに印刷されます。次に、必要なコピー数を指定します。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintingPDFFile()
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
private static void PrintingPDFFile()
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

印刷ダイアログを表示するには、次のコードスニペットを使用します：

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintingPDFDisplayPrintDialog()
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
private static void PrintingPDFDisplayPrintDialog()
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

## ソフトプリンターへのPDF印刷

ファイルに印刷するプリンターがあります。それらを使用するには、仮想プリンターの名前を設定し、前の例と同様に設定を行います。

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintingPDFToSoftPrinter()
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
        // Do not convert document pages to images
        viewer.PrintAsImage = false;

        // Create objects for printer and page settings and PrintDocument
        var ps = new Aspose.Pdf.Printing.PrinterSettings();
        var pgs = new Aspose.Pdf.Printing.PageSettings();

        // Set printer name
        ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
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
private static void PrintingPDFToSoftPrinter()
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
    // Do not convert document pages to images
    viewer.PrintAsImage = false;

    // Create objects for printer and page settings and PrintDocument
    var ps = new Aspose.Pdf.Printing.PrinterSettings();
    var pgs = new Aspose.Pdf.Printing.PageSettings();

    // Set printer name
    ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
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

## 印刷ダイアログの非表示

Aspose.PDF for .NETは印刷ダイアログを非表示にすることをサポートしています。これには、[PrintPageDialog](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfviewer/properties/printpagedialog)プロパティを使用します。

次のコードスニペットは、印刷ダイアログを非表示にする方法を示しています。

{{< tabs tabID="4" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintingPDFHidePrintDialog()
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

        // Create objects for printer and page settings
        var ps = new Aspose.Pdf.Printing.PrinterSettings();
        var pgs = new Aspose.Pdf.Printing.PageSettings();

        // Set XPS/PDF printer name
        ps.PrinterName = "OneNote for Windows 10";

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
private static void PrintingPDFHidePrintDialog()
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
    // Do not produce the page number dialog when printin
    viewer.PrintPageDialog = false;

    // Create objects for printer and page settings
    var ps = new Aspose.Pdf.Printing.PrinterSettings();
    var pgs = new Aspose.Pdf.Printing.PageSettings();

    // Set XPS/PDF printer name
    ps.PrinterName = "OneNote for Windows 10";

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

## カラーPDFをグレースケールでXPSファイルに印刷

カラーPDF文書は、[PdfViewer](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfviewer)を使用してグレースケールでXPSプリンターに印刷できます。それを実現するために、プロパティ[PdfViewer.PrintAsGrayscale](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfviewer/printasgrayscale/)を*true*に設定します。次のコードスニペットは、`PdfViewer.PrintAsGrayscale`プロパティの使用法を示しています。

{{< tabs tabID="5" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintingPDFAsGrayscale()
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
        // Print the file as grayscale
        viewer.PrintAsGrayscale = false;

        // Create objects for printer and page settings
        var ps = new Aspose.Pdf.Printing.PrinterSettings();
        var pgs = new Aspose.Pdf.Printing.PageSettings();

        // Set XPS/PDF printer name
        ps.PrinterName = "OneNote for Windows 10";

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
private static void PrintingPDFAsGrayscale()
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
    // Print the file as grayscale
    viewer.PrintAsGrayscale = false;

    // Create objects for printer and page settings
    var ps = new Aspose.Pdf.Printing.PrinterSettings();
    var pgs = new Aspose.Pdf.Printing.PageSettings();

    // Set XPS/PDF printer name
    ps.PrinterName = "OneNote for Windows 10";

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

## PDFからPostScriptへの変換

[PdfViewer](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfviewer)クラスはPDF文書を印刷する機能を提供し、このクラスを使用することでPDFファイルをPostScript形式に変換することもできます。PDFファイルをPostScriptに変換するには、まず任意のPSプリンターをインストールし、`PdfViewer`を使用してファイルに印刷します。

次のコードスニペットは、PDFをPostScript形式に印刷して変換する方法を示しています。

{{< tabs tabID="6" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void PrintingPDFToPostScript()
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
        // Do not convert document pages to images
        viewer.PrintAsImage = false;

        // Create objects for printer and page settings and PrintDocument
        var ps = new Aspose.Pdf.Printing.PrinterSettings();
        var pgs = new Aspose.Pdf.Printing.PageSettings();

        // Set printer name
        ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
        
        // Set output file name and PrintToFile attribute
        ps.PrintFileName = dataDir + "PdfToPostScript_out.ps";
        ps.PrintToFile = true;

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
private static void PrintingPDFToSoftPrinter()
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
    // Do not convert document pages to images
    viewer.PrintAsImage = false;

    // Create objects for printer and page settings and PrintDocument
    var ps = new Aspose.Pdf.Printing.PrinterSettings();
    var pgs = new Aspose.Pdf.Printing.PageSettings();

    // Set printer name
    ps.PrinterName = "HP Universal Printing PS (v7.0.0)";
    
    // Set output file name and PrintToFile attribute
    ps.PrintFileName = dataDir + "PdfToPostScript_out.ps";
    ps.PrintToFile = true;

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

## 印刷ジョブのステータス確認

PDFファイルは、印刷ダイアログを表示せずに物理プリンターやMicrosoft XPS Document Writerに印刷できます。[PdfViewer](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfviewer)クラスを使用します。大きなPDFファイルを印刷する際、プロセスに時間がかかることがあるため、ユーザーは印刷プロセスが完了したか、問題が発生したかを確信できない場合があります。印刷ジョブのステータスを確認するには、[PrintStatus](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfviewer/printstatus/)プロパティを使用します。次のコードスニペットは、PDFファイルをXPSファイルに印刷し、印刷ステータスを取得する方法を示しています。

{{< tabs tabID="7" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
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

        // Set attributes for printing
        // Print the file with adjusted size
        viewer.AutoResize = true;
        // Print the file with adjusted rotation
        viewer.AutoRotate = true;
        // Do not produce the page number dialog when printing
        viewer.PrintPageDialog = false;
        // Do not convert document pages to images
        viewer.PrintAsImage = false;

        // Create Printer Settings object
        var ps = new Aspose.Pdf.Printing.PrinterSettings();
        var pgs = new Aspose.Pdf.Printing.PageSettings();

        // Specify the printer name
        ps.PrinterName = "Microsoft XPS Document Writer";

        // Set output file name and PrintToFile attribute
        ps.PrintFileName = dataDir + "CheckingPrintJobStatus_out.xps";
        ps.PrintToFile = true;

        // Set PageSize (if required)
        pgs.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;
        
        // Set PageMargins (if required)
        pgs.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);
        
        // Print document using printer and page settings
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

    // Set attributes for printing
    // Print the file with adjusted size
    viewer.AutoResize = true;
    // Print the file with adjusted rotation
    viewer.AutoRotate = true;
    // Do not produce the page number dialog when printing
    viewer.PrintPageDialog = false;
    // Do not convert document pages to images
    viewer.PrintAsImage = false;

    // Create Printer Settings object
    var ps = new Aspose.Pdf.Printing.PrinterSettings();
    var pgs = new Aspose.Pdf.Printing.PageSettings();

    // Specify the printer name
    ps.PrinterName = "Microsoft XPS Document Writer";

    // Set output file name and PrintToFile attribute
    ps.PrintFileName = dataDir + "CheckingPrintJobStatus_out.xps";
    ps.PrintToFile = true;

    // Set PageSize (if required)
    pgs.PaperSize = Aspose.Pdf.Printing.PaperSizes.A4;

    // Set PageMargins (if required)
    pgs.Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0);

    // Print document using printer and page settings
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

## 単面および両面モードでのページ印刷

特定の印刷ジョブでは、PDF文書のページを両面または単面モードで印刷できますが、単一の印刷ジョブ内で一部のページを単面、他のページを両面で印刷することはできません。ただし、要件を達成するために、異なるページ範囲とPrintingJobSettingsオブジェクトを使用できます。次のコードスニペットは、PDFファイルの一部のページを単面で印刷し、他のページを両面で印刷する方法を示しています。

{{< tabs tabID="8" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
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

private static void PrintingPagesInSimplexAndDuplexMode()
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
    printingJob1.OutputFile = outputDir + "PrintPageRange_p1-3_out.xps";
    printingJob1.Mode = Aspose.Pdf.Printing.Duplex.Default;

    printingJobs.Add(printingJob1);

    PrintingJobSettings printingJob2 = new PrintingJobSettings();
    printingJob2.FromPage = 4;
    printingJob2.ToPage = 6;
    printingJob2.OutputFile = outputDir + "PrintPageRange_p4-6_out.xps";
    printingJob2.Mode = Aspose.Pdf.Printing.Duplex.Simplex;

    printingJobs.Add(printingJob2);

    PrintingJobSettings printingJob3 = new PrintingJobSettings();
    printingJob3.FromPage = 7;
    printingJob3.ToPage = 7;
    printingJob3.OutputFile = outputDir + "PrintPageRange_p7_out.xps";
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

private static void PrintingPagesInSimplexAndDuplexMode()
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
    printingJob1.OutputFile = outputDir + "PrintPageRange_p1-3_out.xps";
    printingJob1.Mode = Aspose.Pdf.Printing.Duplex.Default;

    printingJobs.Add(printingJob1);

    PrintingJobSettings printingJob2 = new PrintingJobSettings();
    printingJob2.FromPage = 4;
    printingJob2.ToPage = 6;
    printingJob2.OutputFile = outputDir + "PrintPageRange_p4-6_out.xps";
    printingJob2.Mode = Aspose.Pdf.Printing.Duplex.Simplex;

    printingJobs.Add(printingJob2);

    PrintingJobSettings printingJob3 = new PrintingJobSettings();
    printingJob3.FromPage = 7;
    printingJob3.ToPage = 7;
    printingJob3.OutputFile = outputDir + "PrintPageRange_p7_out.xps";
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

## 単一の印刷ジョブで複数のPDF文書を印刷

時には、関連する複数の文書を単一の印刷ジョブとして一緒に印刷する必要があります。これにより、特にリモートネットワークプリンターを使用する場合、これらの文書が他のユーザーの出力と混在しないようにします。Aspose.PDFは、[PdfViewer](https://reference.aspose.com/pdf/ja/net/aspose.pdf.facades/pdfviewer)クラスの静的`PrintDocuments`メソッドを介して、共有プリンター設定で任意の数の文書を単一の印刷ジョブで印刷することをサポートしています。印刷する文書は、ファイルパス、文書ストリーム、または[Document](https://reference.aspose.com/pdf/ja/net/aspose.pdf/document)オブジェクトとして提供できます。

{{% alert color="primary" %}}

複数の文書を印刷する場合、[PrinterSettings.PrintRange](https://reference.aspose.com/pdf/ja/net/aspose.pdf.printing/printersettings/printrange/)プロパティは無視され、すべての文書が完全に印刷されます。

{{% /alert %}}

{{< tabs tabID="9" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
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
    var printDocument = new PrintDocument();
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
    var printDocument = new PrintDocument();
    Aspose.Pdf.Printing.PrinterSettings printerSettings = new Aspose.Pdf.Printing.PrinterSettings
    {
        PrinterName = printDocument.PrinterSettings.PrinterName
    };
    
    Aspose.Pdf.Printing.PageSettings pageSettings = new Aspose.Pdf.Printing.PageSettings
    {
        PaperSize = Aspose.Pdf.Printing.PaperSizes.A4,
        Margins = new Aspose.Pdf.Devices.Margins(0, 0, 0, 0)
    }
    
    // Print multiple documents in a single print job
    Aspose.Pdf.Facades.PdfViewer.PrintDocuments(printerSettings, pageSettings, path1, path2, path3);
}
```
{{< /tab >}}
{{< /tabs >}}