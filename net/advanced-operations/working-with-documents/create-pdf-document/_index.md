---
title: Create PDF C#
linktitle: Create PDF Document
type: docs
weight: 10
url: /net/create-pdf-document/
description: Create and format the PDF Document with Aspose.PDF for .NET.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

We are always looking for a way to generate PDF documents and work with them in C# projects more exactly, accurately, and effectively. Having easy-to-use functions from a library allows us to track more of the work, and less on the time-heavy details of trying to generate PDFs, whether in .NET.

## Generate PDF

Aspose.PDF for .NET API lets you create and read PDF files using C# and VB.NET. The API can be used in a variety of .NET applications including WinForms, ASP.NET, and several others. In this article, we are going to show how to use Aspose.PDF for .NET API to easily generate and read PDF files in .NET applications.

### How to Create PDF File using C# language

To create a PDF file using C#, the following steps can be used.

1. Create an object of [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) class
1. Add a [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) object to the [Pages](https://apireference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) collection of the Document object
1. Add [TextFragment](https://apireference.aspose.com/pdf/net/aspose.pdf.text/textfragment) to [Paragraphs](https://apireference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) collection of the page
1. Save the resultant PDF document

```csharp
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

// Initialize document object
Document document = new Document();
// Add page
Page page = document.Pages.Add();
// Add text to new page
page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
// Save updated PDF
document.Save(dataDir + "HelloWorld_out.pdf");
```

## Create a searchable PDF document

Aspose.PDF for .NET provides the feature to create as well as manipulate existing PDF documents. When adding Text elements inside PDF file, the resultant PDF is searchable. However if we are converting an Image containing text to PDF file, the contents inside PDF are not searchable. However as a workaround, we can use OCR over the resultant file, so that it becomes searchable.

This logic specified below recognizes text for PDF images. For recognition you may use outer OCR supports HOCR standard. For testing purposes, we have used a free Google tesseract OCR. Therefore first you need to install Tesseract-OCR on your system, and you will have tesseract console application.

Following is complete code to accomplish this requirement:

```csharp

using System;

namespace Aspose.Pdf.Examples.Advanced.WorkingWithDocuments
{
    class ExampleCreateDocument
    {
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void CreateSearchableDocuments(string file)
        {
            Aspose.Pdf.Document doc = new Aspose.Pdf.Document(file);
            bool convertResult = false;
            try
            {               
                convertResult = doc.Convert(CallBackGetHocr);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            doc.Save(file);
            doc.Dispose();          
        }

        static string CallBackGetHocr(System.Drawing.Image img)
        {
            string tmpFile = System.IO.Path.GetTempFileName();
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
    }
}
```
