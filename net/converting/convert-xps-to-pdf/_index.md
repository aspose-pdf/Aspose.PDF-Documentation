---
title: Convert XPS to PDF
type: docs
weight: 190
url: /net/convert-xps-to-pdf/
---
# Convert XPS to PDF

The XPS file type is primarily associated with the XML Paper Specification by Microsoft Corporation. The XML Paper Specification (XPS), formerly codenamed Metro and subsuming the Next Generation Print Path (NGPP) marketing concept, is Microsoft's initiative to integrate document creation and viewing into its Windows operating system.

{{% alert color="primary" %}}

The file format is basically a zipped XML file which is primarily used for distribution and storage. It's very difficult to edit and mostly implemented by Microsoft.

{{% /alert %}}

In order to convert XPS to PDF with Aspose.PDF for .NET, we have introduced a class named XpsLoadOptions which is used to initialize a LoadOptions object. Later, this object is passed as an argument during the Document object initialization and it helps the PDF rendering engine to determine the source document's input format.

{{% alert color="primary" %}}

In both XP and Windows 7, you should find an XPS Printer pre-installed if you look in the Control Panel and then Printers. To create these files you can use that printer for the output device. In Windows 7, you should be able to just double-click the file to open it in a XPS viewer. You may also download XPS viewer from Microsoft's website.

{{% /alert %}}

The following code snippet shows the process of converting XPS file into PDF format.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

// Instantiate LoadOption object using XPS load option
Aspose.Pdf.LoadOptions options = new XpsLoadOptions();

// Create document object
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "XPSToPDF.xps", options);

// Save the resultant PDF document
document.Save(dataDir + "XPSToPDF_out.pdf");
```
