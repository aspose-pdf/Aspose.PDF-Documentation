---
title: Extract fonts from PDF
type: docs
weight: 30
url: /net/extract-fonts-from-pdf/
---
# Extract fonts from PDF

In case you want to get all fonts from a PDF document, you can use FontUtilities.GetAllFonts() method provided in Document class. Please check following code snippet in order to get all fonts from an existing PDF document:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```
