---
title: Working with Portfolio in PDF
linktitle: Portfolio
type: docs
weight: 40
url: /cpp/portfolio/
description: Create a PDF Portfolio with Aspose.PDF for C++. You should use a Microsoft Excel File, a Word document, and an image file to create a PDF Portfolio.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## How to Create a PDF Portfolio

Aspose.PDF allows creating PDF Portfolio documents using the [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) class. Add a file into a Document.Collection object after getting it with the [FileSpecification](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) class. When the files have been added, use the Document class' Save method to save the portfolio document.

The following example uses a Microsoft Excel File, a Word document and an image file to create a PDF Portfolio.

The code below results in the following portfolio.

### A PDF Portfolio created with Aspose.PDF

![A PDF Portfolio created with Aspose.PDF for C++](working-with-pdf-portfolio_1.jpg)

```cpp
void WorkingWithAttachments::CreatePortfolio()
{
    String _dataDir("C:\\Samples\\");

    // Instantiate Document Object
    auto pdfDocument = MakeObject<Document>();

    // Instantiate document Collection object
    pdfDocument->set_Collection(MakeObject<Collection>());

    // Get Files to add to Portfolio
    auto excel = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.xlsx");
    auto word = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.docx");
    auto image = MakeObject<FileSpecification>(_dataDir + u"sample.jpg");

    // Provide description of the files
    excel->set_Description(u"Excel File");
    word->set_Description(u"Word File");
    image->set_Description(u"Image File");

    // Add files to document collection
    pdfDocument->get_Collection()->Add(excel);
    pdfDocument->get_Collection()->Add(word);
    pdfDocument->get_Collection()->Add(image);

    // Save Portfolio document
    pdfDocument->Save(_dataDir + u"PDFPortfolio.pdf");
}
```

## Extract files from PDF Portfolio

PDF Portfolios allow you to bring together content from a variety of sources (for example, PDF, Word, Excel, JPEG files) into one unified container. The original files retain their individual identities but are assembled into a PDF Portfolio file. Users can open, read, edit, and format each component file independently of the other component files.

Aspose.PDF allows the creation of PDF Portfolio documents using [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) class. It also offers the capability to extract files from PDF portfolio.

The following code snippet shows you the steps to extract files from PDF portfolio.

```cpp
void WorkingWithAttachments::ExtractPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // Open a document
    auto pdfDocument = MakeObject <Document>(_dataDir + u"PDFPortfolio.pdf");
    // Get collection of embedded files
    auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

    // Iterate through individual file of Portfolio
    for (auto fileSpecification : embeddedFiles) {
    auto initialStream = fileSpecification->get_Contents();
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
    auto filename = System::IO::Path::GetFileName(fileSpecification->get_Name());
    // Save the extracted file to some location
    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"_out_" + filename);
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    // Close the stream object
    fileStream->Close();
    }
}
```

![Extract files from PDF Portfolio](working-with-pdf-portfolio_2.jpg)

## Remove Files from PDF Portfolio

In order to delete/remove files from PDF portfolio, try using the following code lines.

```cpp
void WorkingWithAttachments::RemoveFilesFromPDFPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // Load source PDF Portfolio
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PDFPortfolio.pdf");
    pdfDocument->get_Collection()->Delete();
    pdfDocument->Save(_dataDir + u"No_PortFolio_out.pdf");
}
```
