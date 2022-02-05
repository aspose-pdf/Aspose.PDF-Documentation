---
title: How to Create PDF using C#
linktitle: Create PDF Document
type: docs
weight: 10
url: /net/create-pdf-document/
description: Create and format the PDF Document with Aspose.PDF for .NET.
lastmod: "2021-04-02"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to Create PDF using C#",
    "alternativeHeadline": "Create (or Generate) PDF document using C# language",
    "author": {
        "@type": "Person",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, document generation",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "https://docs.aspose.com/pdf/net/create-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://docs.aspose.com/pdf/net/create-pdf-document/"
    },
    "dateModified": "2022-02-04",
    "description": "Create and format the PDF Document with Aspose.PDF for .NET.",
    "articleBody": "<h1>How to Create PDF using C#</h1><p>We are always looking for a way to generate PDF documents and work with them in C# projects more exactly, accurately, and effectively. Having easy-to-use functions from a library allows us to track more of the work, and less on the time-heavy details of trying to generate PDFs, whether in .NET.</p><h2>Create (or Generate) PDF document using C# language</h2><p>Aspose.PDF for .NET API lets you create and read PDF files using C# and VB.NET. The API can be used in a variety of .NET applications including WinForms, ASP.NET, and several others. In this article, we are going to show how to use Aspose.PDF for .NET API to easily generate and read PDF files in .NET applications.</p><h3>How to Create Simple PDF File</h3><p>To create a PDF file using C#, the following steps can be used.</p><ol> <li>Create an object of Document class</li><li>Add a Page object to the Pages collection of the Document object</li><li>Add TextFragment to Paragraphs collection of the page</li><li>Save the resultant PDF document</li></ol><code> // The path to the documents directory. string dataDir=RunExamples.GetDataDir_AsposePdf_QuickStart(); // Initialize document object Document document=new Document(); // Add page Page page=document.Pages.Add(); // Add text to new page page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment('Hello World!')); // Save updated PDF document.Save(dataDir + 'HelloWorld_out.pdf'); </code><h3>How to Create a Searchable PDF document</h3><p>Aspose.PDF for .NET provides the feature to create as well as manipulate existing PDF documents. When adding Text elements inside PDF file, the resultant PDF is searchable. However if we are converting an Image containing text to PDF file, the contents inside PDF are not searchable. However as a workaround, we can use OCR over the resultant file, so that it becomes searchable.</p><p>This logic specified below recognizes text for PDF images. For recognition you may use outer OCR supports HOCR standard. For testing purposes, we have used a free Google tesseract OCR. Therefore first you need to install Tesseract-OCR on your system, and you will have tesseract console application.</p><p>Following is complete code to accomplish this requirement:</p><code> using System; namespace Aspose.Pdf.Examples.Advanced.WorkingWithDocuments{class ExampleCreateDocument{private const string _dataDir='C:\\Samples'; public static void CreateSearchableDocuments(string file){Aspose.Pdf.Document doc=new Aspose.Pdf.Document(file); bool convertResult=false; try{convertResult=doc.Convert(CallBackGetHocr);}catch (Exception ex){Console.WriteLine(ex.Message);}doc.Save(file); doc.Dispose();}static string CallBackGetHocr(System.Drawing.Image img){string tmpFile=System.IO.Path.GetTempFileName(); try{System.Drawing.Bitmap bmp=new System.Drawing.Bitmap(img); bmp.Save(tmpFile, System.Drawing.Imaging.ImageFormat.Bmp); string inputFile=string.Concat(''', tmpFile, '''); string outputFile=string.Concat(''', tmpFile, '''); string arguments=string.Concat(inputFile, ' ', outputFile, ' -l eng hocr'); string tesseractProcessName=@'C:\Program Files\Tesseract-OCR\Tesseract.exe'; System.Diagnostics.ProcessStartInfo psi=new System.Diagnostics.ProcessStartInfo(tesseractProcessName, arguments){UseShellExecute=true, CreateNoWindow=true, WindowStyle=System.Diagnostics.ProcessWindowStyle.Hidden, WorkingDirectory=System.IO.Path.GetDirectoryName(tesseractProcessName)}; System.Diagnostics.Process p=new System.Diagnostics.Process{StartInfo=psi}; p.Start(); p.WaitForExit(); System.IO.StreamReader streamReader=new System.IO.StreamReader(tmpFile + '.hocr'); string text=streamReader.ReadToEnd(); streamReader.Close(); return text;}finally{if (System.IO.File.Exists(tmpFile)) System.IO.File.Delete(tmpFile); if (System.IO.File.Exists(tmpFile + '.hocr')) System.IO.File.Delete(tmpFile + '.hocr');}}}}</code>"
}
</script>

We are always looking for a way to generate PDF documents and work with them in C# projects more exactly, accurately, and effectively. Having easy-to-use functions from a library allows us to track more of the work, and less on the time-heavy details of trying to generate PDFs, whether in .NET.

## Create (or Generate) PDF document using C# language

Aspose.PDF for .NET API lets you create and read PDF files using C# and VB.NET. The API can be used in a variety of .NET applications including WinForms, ASP.NET, and several others. In this article, we are going to show how to use Aspose.PDF for .NET API to easily generate and read PDF files in .NET applications.

### How to Create Simple PDF File

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

### How to Create a Searchable PDF document

Aspose.PDF for .NET provides the feature to create as well as manipulate existing PDF documents. When adding Text elements inside PDF file, the resultant PDF is searchable. However if we are converting an Image containing text to PDF file, the contents inside PDF are not searchable. However as a workaround, we can use OCR over the resultant file, so that it becomes searchable.

This logic specified below recognizes text for PDF images. For recognition you may use outer OCR supports HOCR standard. For testing purposes, we have used a free Google tesseract OCR. Therefore first you need to install Tesseract-OCR on your system, and you will have tesseract console application.

Following is complete code to accomplish this requirement:

```csharp

using System;

namespace Aspose.Pdf.Examples.Advanced.WorkingWithDocuments
{
    class ExampleCreateDocument
    {
        private const string _dataDir = "C:\\Samples";
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