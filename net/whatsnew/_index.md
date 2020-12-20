---
title: What's new
type: docs
weight: 10
url: /net/whatsnew/
description: In this page introduces the most popular new features in Aspose.PDF for .NET that have been introduced in recent releases.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## What's new in Aspose.PDF 20.11

Aspose.PDF v20.11 added support for ZUGFeRD format.

```csharp
Document doc = new Document();
doc.Pages.Add();
string fileName = "zugferd-invoice.xml";
FileSpecification fs = new FileSpecification(fileName);
doc.EmbeddedFiles.Add(fs);
fs.Description = "ZUGFeRD";
doc.Convert(new MemoryStream(), PdfFormat.ZUGFeRD, ConvertErrorAction.Delete);
doc.Save("invoice.pdf");
```

Also in this release, Aspose.PDF introduced PDF to XML and XML to PDF conversion.

### Conversion PDF to XML

```csharp
//save document as PDFXML
Document doc = new Document("source.pdf");
doc.Save("pdf.xml", SaveFormat.PdfXml);
```

### Conversion XML to PDF
The following code snippet shows the process of converting a PDF file to XML (MobiXML) format.

```csharp
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();            
// Load source PDF file
Document doc = new Document(dataDir + "input.pdf");
// Save output in XML format
doc.Save(dataDir + "PDFToXML_out.xml", SaveFormat.MobiXml);
```

## What's new in Aspose.PDF 20.7

### Conversion PDF to Excel CSV

Aspose.PDF v20.7 Aspose.PDF supports conversion to CSV format.
You should use ExcelSaveOptions while document saving to perform the conversion.

The following snippet shows how you would save data into CSV file.

```csharp
ExcelSaveOptions options = new ExcelSaveOptions();
options.ConversionEngine = ExcelSaveOptions.ConversionEngines.NewEngine;
options.Format = ExcelSaveOptions.ExcelFormat.CSV;

Document pdfDocument = new Document("Currencies.pdf");
pdfDocument.Save("Currencies.csv", options);  
```

## What's new in Aspose.PDF  20.3

### Progress Detail of PPTX Conversion

Aspose.PDF v20.3 lets you track the progress of PDF to PPTX conversion.

The Aspose.Pdf.PptxSaveOptions class provides CustomProgressHandler property that can be specified to a custom method for tracking the progress of conversion as shown in the following code sample.

```csharp
// Load PDF document
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "input.pdf");
// Instantiate PptxSaveOptions instance
Aspose.Pdf.PptxSaveOptions pptx_save = new Aspose.Pdf.PptxSaveOptions();

//Specify Custom Progress Handler
pptx_save.CustomProgressHandler = ShowProgressOnConsole;
// Save the output in PPTX format
doc.Save(dataDir + "PDFToPPTWithProgressTracking_out_.pptx", pptx_save);
```

Following is the custom method for displaying progress conversion.

```csharp
switch (eventInfo.EventType)
{
    case ProgressEventType.TotalProgress:
        Console.WriteLine(String.Format("{0}  - Conversion progress : {1}% .", DateTime.Now.TimeOfDay, eventInfo.Value.ToString()));
        break;
    case ProgressEventType.ResultPageCreated:
        Console.WriteLine(String.Format("{0}  - Result page's {1} of {2} layout created.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.ResultPageSaved:
        Console.WriteLine(String.Format("{0}  - Result page {1} of {2} exported.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;
    case ProgressEventType.SourcePageAnalysed:
        Console.WriteLine(String.Format("{0}  - Source page {1} of {2} analyzed.", DateTime.Now.TimeOfDay, eventInfo.Value.ToString(), eventInfo.MaxValue.ToString()));
        break;

    default:
        break;
}
```
