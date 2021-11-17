---
title: Create PDF C++
linktitle: Create PDF Document
type: docs
weight: 10
url: /cpp/create-pdf-document/
description: Create and format the PDF Document with Aspose.PDF for C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

We are always looking for a way to generate PDF documents and work with them in C++ projects more exactly, accurately, and effectively. Having easy-to-use functions from a library allows us to track more of the work, and less on the time-heavy details of trying to generate PDFs, whether in C++.

## Generate PDF

Aspose.PDF for C++ API lets you create and read PDF files using C++. The API can be used in a variety of C++ applications including WinForms, and several others. In this article, we are going to show how to use Aspose.PDF for C++ API to easily generate and read PDF files in C++ applications.

### How to Create PDF File using C++ language

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

## Create a searchable PDF document

Aspose.PDF for C ++ allows you to create PDFs from scratch and manipulate existing ones.
When you add text elements to a PDF, the resulting PDF is searchable. However, if we convert an image containing text to a PDF file, the content inside the PDF is not searchable. However, as a workaround, we can use OCR on the resulting file to make it searchable. Therefore first you need to install Tesseract-OCR on your system, and you will have a tesseract console application.

Following is complete code to accomplish this requirement:

```cpp
void CreateSearchableDocument() {
private const string _dataDir = "..\\..\\..\\..\\Samples";

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

static String CallBackGetHocr(System::Drawing::Image img)
{
    String tmpFile = System::IO::Path::GetTempFileName();
    try
    {
        System.Drawing.Bitmap bmp = new System.Drawing.Bitmap(img);

        bmp.Save(tmpFile, System.Drawing.Imaging.ImageFormat.Bmp);
        string inputFile = string.Concat('"', tmpFile, '"');
        string outputFile = string.Concat('"', tmpFile, '"');
        string arguments = string.Concat(inputFile, " ", outputFile, " -l eng hocr");
        string tesseractProcessName = @"C:\Program Files\Tesseract-OCR\Tesseract.exe";

        System.Diagnostics.ProcessStartInfo psi =
           new System.Diagnostics.ProcessStartInfo(tesseractProcessName, arguments)
        {
            UseShellExecute = true,
                CreateNoWindow = true,
                WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden,
                WorkingDirectory = System.IO.Path.GetDirectoryName(tesseractProcessName)
        };

        System.Diagnostics.Process p = new System.Diagnostics.Process
        {
            StartInfo = psi
        };
        p.Start();
        p.WaitForExit();

        System.IO.StreamReader streamReader = new System.IO.StreamReader(tmpFile + ".hocr");
        string text = streamReader.ReadToEnd();
        streamReader.Close();

        return text;
    }
    finally
    {
        if (System.IO.File.Exists(tmpFile))
            System.IO.File.Delete(tmpFile);
       if (System.IO.File.Exists(tmpFile + ".hocr"))
            System.IO.File.Delete(tmpFile + ".hocr");
   }
}
```
