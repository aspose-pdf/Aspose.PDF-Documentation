---
title: Portfolio
type: docs
weight: 10
url: /net/portfolio/
---
# How to Create a PDF Portfolio
Aspose.PDF allows creating PDF Portfolio documents using the [Document](https://apireference.aspose.com/net/pdf/aspose.pdf/document) class. Add a file into a Document.Collection object after getting it with the [FileSpecification](https://apireference.aspose.com/net/pdf/aspose.pdf/filespecification) class. When the files have been added, use the Document class' Save method to save the portfolio document.

The following example uses a Microsoft Excel File, a Word document and an image file to create a PDF Portfolio.

The code below results in the following portfolio.

**A PDF Portfolio created with Aspose.PDF** 

![todo:image_alt_text](working-with-pdf-portfolio_1.jpg)

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Load source PDF Portfolio
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
// Get collection of embedded files
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;
// Itterate through individual file of Portfolio
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    // Get the attachment and write to file or stream
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);
    string filename = Path.GetFileName(fileSpecification.Name);
    // Save the extracted file to some location
    FileStream fileStream = new FileStream(dataDir + "_out" + filename, FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    // Close the stream object
    fileStream.Close();
}
```

## Extract files from PDF Portfolio
PDF Portfolios allow you to bring together content from a variety of sources (for example, PDF, Word, Excel, JPEG files) into one unified container. The original files retain their individual identities but are assembled into a PDF Portfolio file. Users can open, read, edit, and format each component file independently of the other component files.

Aspose.PDF allows the creation of PDF Portfolio documents using [Document](https://apireference.aspose.com/net/pdf/aspose.pdf/document) class. It also offers the capability to extract files from PDF portfolio.

The following code snippet shows you the steps to extract files from PDF portfolio.

![todo:image_alt_text](working-with-pdf-portfolio_2.jpg)

## Remove Files from PDF Portfolio
In order to delete/remove files from PDF portfolio, try using the following code lines.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// Load source PDF Portfolio
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
pdfDocument.Collection.Delete();
pdfDocument.Save(dataDir + "No_PortFolio_out.pdf");
```
