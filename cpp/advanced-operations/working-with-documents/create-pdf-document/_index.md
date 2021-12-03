---
title: Create PDF Document
linktitle: Create PDF
type: docs
weight: 10
url: /cpp/create-pdf-document/
description: This article describes how to Create and format the PDF Document with Aspose.PDF for C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

We are always looking for a way to generate PDF documents and work with them in C++ projects more exactly, accurately, and effectively. Having easy-to-use functions from a library allows us to track more of the work, and less on the time-heavy details of trying to generate PDFs, whether in C++.

## Generate PDF using C++

Aspose.PDF for C++ API lets you create and read PDF files using C++. The API can be used in a variety of C++ applications including WinForms, and several others. In this article, we are going to show how to use Aspose.PDF for C++ API to easily generate and read PDF files in C++ applications.

### How to Create Simple PDF File

To create a PDF file using C++, the following steps can be used.

1. Create an object of [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) class
1. Add a [Page](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page) object to the 'Pages' collection of the Document object
1. Add [TextFragment](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_fragment/) to [Paragraphs](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs) collection of the page
1. Save the resultant PDF document

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CreateDocument() {
    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String outputFileName("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // Add text to new page
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Save updated PDF
    document->Save(_dataDir + outputFileName);
}
```

## Create a Searchable PDF document

Aspose.PDF for C ++ allows you to create PDFs from scratch and manipulate existing ones.
When you add text elements to a PDF, the resulting PDF is searchable. However, if we convert an image containing text to a PDF file, the content inside the PDF is not searchable. However, as a workaround, we can use OCR on the resulting file to make it searchable. Therefore first you need to install Tesseract-OCR on your system, and you will have a tesseract console application.

Following is complete code to accomplish this requirement:

```cpp
void CreateSearchableDocument() {
    // String for path name.
    String _dataDir("C:\\Samples\\");
    // String for file name.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);
    bool convertResult = false;
    try
    {
        convertResult = document->Convert(CallBackGetHocr);
    }
    catch (Exception ex)
    {
        std::cerr << ex->get_Message() << std::endl;
    }
    document->Dispose();
}

static String CallBackGetHocr(System::SharedPtr<System::Drawing::Image> img)
{
    String tmpFile = System::IO::Path::GetTempFileNameSafe();
 
    auto bmp = MakeObject<System::Drawing::Bitmap>(img);

    bmp->Save(tmpFile, System::Drawing::Imaging::ImageFormat::get_Bmp());
    String inputFile = String::Format(u"\"{0}\"", tmpFile);
    String outputFile = String::Format(u"\"{0}\"", tmpFile);
    String arguments = inputFile + u" " + outputFile + u" -l eng hocr";
    String tesseractProcessName = u"C:\\Program Files\\Tesseract-OCR\\Tesseract.exe";

    auto psi = MakeObject<System::Diagnostics::ProcessStartInfo>(tesseractProcessName, arguments);
    psi->set_UseShellExecute(true);
    psi->set_CreateNoWindow(true);
    psi->set_WindowStyle(System::Diagnostics::ProcessWindowStyle::Hidden);
    psi->set_WorkingDirectory(System::IO::Path::GetDirectoryName(tesseractProcessName));

    auto p = MakeObject<System::Diagnostics::Process>(psi);		
    p->Start();
    p->WaitForExit();

    auto streamReader = MakeObject<System::IO::StreamReader>(tmpFile + u".hocr");
    String text = streamReader->ReadToEnd();
    streamReader->Close();

    if (System::IO::File::Exists(tmpFile))
        System::IO::File::Delete(tmpFile);
    if (System::IO::File::Exists(tmpFile + u".hocr"))
        System::IO::File::Delete(tmpFile + u".hocr");

    return text;    
}
```
