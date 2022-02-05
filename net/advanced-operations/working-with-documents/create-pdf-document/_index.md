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
    "articleBody": "<div class="td-content"><h1>How to Create PDF using C#</h1></div><p>We are always looking for a way to generate PDF documents and work with them in C# projects more exactly, accurately, and effectively. Having easy-to-use functions from a library allows us to track more of the work, and less on the time-heavy details of trying to generate PDFs, whether in .NET.</p><h2 id="create-or-generate-pdf-document-using-c-language">Create (or Generate) PDF document using C# language<a aria-hidden="true" class="anchor" href="#create-or-generate-pdf-document-using-c-language" style="visibility: hidden;"> <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="24" height="24" viewBox="0 0 24 24"><path d="M0 0h24v24H0z" fill="none"></path><path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"></path></svg></a></h2><p>Aspose.PDF for .NET API lets you create and read PDF files using C# and VB.NET. The API can be used in a variety of .NET applications including WinForms, ASP.NET, and several others. In this article, we are going to show how to use Aspose.PDF for .NET API to easily generate and read PDF files in .NET applications.</p><h3 id="how-to-create-simple-pdf-file">How to Create Simple PDF File<a aria-hidden="true" class="anchor" href="#how-to-create-simple-pdf-file" style="visibility: hidden;"> <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="24" height="24" viewBox="0 0 24 24"><path d="M0 0h24v24H0z" fill="none"></path><path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"></path></svg></a></h3><p>To create a PDF file using C#, the following steps can be used.</p><ol><li>Create an object of <a href="https://apireference.aspose.com/pdf/net/aspose.pdf/document">Document</a> class</li><li>Add a <a href="https://apireference.aspose.com/pdf/net/aspose.pdf/page">Page</a> object to the <a href="https://apireference.aspose.com/pdf/net/aspose.pdf/document/properties/pages">Pages</a> collection of the Document object</li><li>Add <a href="https://apireference.aspose.com/pdf/net/aspose.pdf.text/textfragment">TextFragment</a> to <a href="https://apireference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs">Paragraphs</a> collection of the page</li><li>Save the resultant PDF document</li></ol><div class="highlight"><pre tabindex="0" style="background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4"><button class="btn btn-dark float-right" type="button" style="font-size: 1em !important;">Copy</button><code class="language-csharp" data-lang="csharp"><span style="color:#8f5902;font-style:italic">// The path to the documents directory.</span><span style="color:#8f5902;font-style:italic"></span><span style="color:#204a87;font-weight:700">string</span> <span style="color:#000">dataDir</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#000">RunExamples</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">GetDataDir_AsposePdf_QuickStart</span><span style="color:#000;font-weight:700">();</span><span style="color:#8f5902;font-style:italic">// Initialize document object</span><span style="color:#8f5902;font-style:italic"></span><span style="color:#000">Document</span> <span style="color:#000">document</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#204a87;font-weight:700">new</span> <span style="color:#000">Document</span><span style="color:#000;font-weight:700">();</span><span style="color:#8f5902;font-style:italic">// Add page</span><span style="color:#8f5902;font-style:italic"></span><span style="color:#000">Page</span> <span style="color:#000">page</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#000">document</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Pages</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Add</span><span style="color:#000;font-weight:700">();</span><span style="color:#8f5902;font-style:italic">// Add text to new page</span><span style="color:#8f5902;font-style:italic"></span><span style="color:#000">page</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Paragraphs</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Add</span><span style="color:#000;font-weight:700">(</span><span style="color:#204a87;font-weight:700">new</span> <span style="color:#000">Aspose</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Pdf</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Text</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">TextFragment</span><span style="color:#000;font-weight:700">(</span><span style="color:#4e9a06">"Hello World!"</span><span style="color:#000;font-weight:700">));</span><span style="color:#8f5902;font-style:italic">// Save updated PDF</span><span style="color:#8f5902;font-style:italic"></span><span style="color:#000">document</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Save</span><span style="color:#000;font-weight:700">(</span><span style="color:#000">dataDir</span> <span style="color:#000;font-weight:700">+</span> <span style="color:#4e9a06">"HelloWorld_out.pdf"</span><span style="color:#000;font-weight:700">);</span></code></pre></div><h3 id="how-to-create-a-searchable-pdf-document">How to Create a Searchable PDF document<a aria-hidden="true" class="anchor" href="#how-to-create-a-searchable-pdf-document" style="visibility: hidden;"> <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="24" height="24" viewBox="0 0 24 24"><path d="M0 0h24v24H0z" fill="none"></path><path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"></path></svg></a></h3><p>Aspose.PDF for .NET provides the feature to create as well as manipulate existing PDF documents. When adding Text elements inside PDF file, the resultant PDF is searchable. However if we are converting an Image containing text to PDF file, the contents inside PDF are not searchable. However as a workaround, we can use OCR over the resultant file, so that it becomes searchable.</p><p>This logic specified below recognizes text for PDF images. For recognition you may use outer OCR supports HOCR standard. For testing purposes, we have used a free Google tesseract OCR. Therefore first you need to install Tesseract-OCR on your system, and you will have tesseract console application.</p><p>Following is complete code to accomplish this requirement:</p><div class="highlight"><pre tabindex="0" style="background-color:#f8f8f8;-moz-tab-size:4;-o-tab-size:4;tab-size:4"><button class="btn btn-dark float-right" type="button" style="font-size: 1em !important;">Copy</button><code class="language-csharp" data-lang="csharp"><span style="color:#204a87;font-weight:700">using</span> <span style="color:#000">System</span><span style="color:#000;font-weight:700">;</span><span style="color:#204a87;font-weight:700">namespace</span> <span style="color:#000">Aspose.Pdf.Examples.Advanced.WorkingWithDocuments</span><span style="color:#000;font-weight:700">{</span> <span style="color:#204a87;font-weight:700">class</span> <span style="color:#000">ExampleCreateDocument</span> <span style="color:#000;font-weight:700">{</span> <span style="color:#204a87;font-weight:700">private</span> <span style="color:#204a87;font-weight:700">const</span> <span style="color:#204a87;font-weight:700">string</span> <span style="color:#0000cf;font-weight:700">_d</span><span style="color:#000">ataDir</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#4e9a06">"C:\\Samples"</span><span style="color:#000;font-weight:700">;</span> <span style="color:#204a87;font-weight:700">public</span> <span style="color:#204a87;font-weight:700">static</span> <span style="color:#204a87;font-weight:700">void</span> <span style="color:#000">CreateSearchableDocuments</span><span style="color:#000;font-weight:700">(</span><span style="color:#204a87;font-weight:700">string</span> <span style="color:#000">file</span><span style="color:#000;font-weight:700">)</span> <span style="color:#000;font-weight:700">{</span> <span style="color:#000">Aspose</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Pdf</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Document</span> <span style="color:#000">doc</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#204a87;font-weight:700">new</span> <span style="color:#000">Aspose</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Pdf</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Document</span><span style="color:#000;font-weight:700">(</span><span style="color:#000">file</span><span style="color:#000;font-weight:700">);</span> <span style="color:#204a87;font-weight:700">bool</span> <span style="color:#000">convertResult</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#204a87;font-weight:700">false</span><span style="color:#000;font-weight:700">;</span> <span style="color:#204a87;font-weight:700">try</span> <span style="color:#000;font-weight:700">{</span> <span style="color:#000">convertResult</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#000">doc</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Convert</span><span style="color:#000;font-weight:700">(</span><span style="color:#000">CallBackGetHocr</span><span style="color:#000;font-weight:700">);</span> <span style="color:#000;font-weight:700">}</span> <span style="color:#204a87;font-weight:700">catch</span> <span style="color:#000;font-weight:700">(</span><span style="color:#000">Exception</span> <span style="color:#000">ex</span><span style="color:#000;font-weight:700">)</span> <span style="color:#000;font-weight:700">{</span> <span style="color:#000">Console</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">WriteLine</span><span style="color:#000;font-weight:700">(</span><span style="color:#000">ex</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Message</span><span style="color:#000;font-weight:700">);</span> <span style="color:#000;font-weight:700">}</span> <span style="color:#000">doc</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Save</span><span style="color:#000;font-weight:700">(</span><span style="color:#000">file</span><span style="color:#000;font-weight:700">);</span> <span style="color:#000">doc</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Dispose</span><span style="color:#000;font-weight:700">();</span> <span style="color:#000;font-weight:700">}</span> <span style="color:#204a87;font-weight:700">static</span> <span style="color:#204a87;font-weight:700">string</span> <span style="color:#000">CallBackGetHocr</span><span style="color:#000;font-weight:700">(</span><span style="color:#000">System</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Drawing</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Image</span> <span style="color:#000">img</span><span style="color:#000;font-weight:700">)</span> <span style="color:#000;font-weight:700">{</span> <span style="color:#204a87;font-weight:700">string</span> <span style="color:#000">tmpFile</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#000">System</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">IO</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Path</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">GetTempFileName</span><span style="color:#000;font-weight:700">();</span> <span style="color:#204a87;font-weight:700">try</span> <span style="color:#000;font-weight:700">{</span> <span style="color:#000">System</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Drawing</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Bitmap</span> <span style="color:#000">bmp</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#204a87;font-weight:700">new</span> <span style="color:#000">System</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Drawing</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Bitmap</span><span style="color:#000;font-weight:700">(</span><span style="color:#000">img</span><span style="color:#000;font-weight:700">);</span> <span style="color:#000">bmp</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Save</span><span style="color:#000;font-weight:700">(</span><span style="color:#000">tmpFile</span><span style="color:#000;font-weight:700">,</span> <span style="color:#000">System</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Drawing</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Imaging</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">ImageFormat</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Bmp</span><span style="color:#000;font-weight:700">);</span> <span style="color:#204a87;font-weight:700">string</span> <span style="color:#000">inputFile</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#204a87;font-weight:700">string</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Concat</span><span style="color:#000;font-weight:700">(</span><span style="color:#4e9a06">'"'</span><span style="color:#000;font-weight:700">,</span> <span style="color:#000">tmpFile</span><span style="color:#000;font-weight:700">,</span> <span style="color:#4e9a06">'"'</span><span style="color:#000;font-weight:700">);</span> <span style="color:#204a87;font-weight:700">string</span> <span style="color:#000">outputFile</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#204a87;font-weight:700">string</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Concat</span><span style="color:#000;font-weight:700">(</span><span style="color:#4e9a06">'"'</span><span style="color:#000;font-weight:700">,</span> <span style="color:#000">tmpFile</span><span style="color:#000;font-weight:700">,</span> <span style="color:#4e9a06">'"'</span><span style="color:#000;font-weight:700">);</span> <span style="color:#204a87;font-weight:700">string</span> <span style="color:#000">arguments</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#204a87;font-weight:700">string</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Concat</span><span style="color:#000;font-weight:700">(</span><span style="color:#000">inputFile</span><span style="color:#000;font-weight:700">,</span> <span style="color:#4e9a06">" "</span><span style="color:#000;font-weight:700">,</span> <span style="color:#000">outputFile</span><span style="color:#000;font-weight:700">,</span> <span style="color:#4e9a06">" -l eng hocr"</span><span style="color:#000;font-weight:700">);</span> <span style="color:#204a87;font-weight:700">string</span> <span style="color:#000">tesseractProcessName</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#4e9a06">@"C:\Program Files\Tesseract-OCR\Tesseract.exe"</span><span style="color:#000;font-weight:700">;</span> <span style="color:#000">System</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Diagnostics</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">ProcessStartInfo</span> <span style="color:#000">psi</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#204a87;font-weight:700">new</span> <span style="color:#000">System</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Diagnostics</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">ProcessStartInfo</span><span style="color:#000;font-weight:700">(</span><span style="color:#000">tesseractProcessName</span><span style="color:#000;font-weight:700">,</span> <span style="color:#000">arguments</span><span style="color:#000;font-weight:700">)</span> <span style="color:#000;font-weight:700">{</span> <span style="color:#000">UseShellExecute</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#204a87;font-weight:700">true</span><span style="color:#000;font-weight:700">,</span> <span style="color:#000">CreateNoWindow</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#204a87;font-weight:700">true</span><span style="color:#000;font-weight:700">,</span> <span style="color:#000">WindowStyle</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#000">System</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Diagnostics</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">ProcessWindowStyle</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Hidden</span><span style="color:#000;font-weight:700">,</span> <span style="color:#000">WorkingDirectory</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#000">System</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">IO</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Path</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">GetDirectoryName</span><span style="color:#000;font-weight:700">(</span><span style="color:#000">tesseractProcessName</span><span style="color:#000;font-weight:700">)</span> <span style="color:#000;font-weight:700">};</span> <span style="color:#000">System</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Diagnostics</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Process</span> <span style="color:#000">p</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#204a87;font-weight:700">new</span> <span style="color:#000">System</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Diagnostics</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Process</span> <span style="color:#000;font-weight:700">{</span> <span style="color:#000">StartInfo</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#000">psi</span> <span style="color:#000;font-weight:700">};</span> <span style="color:#000">p</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Start</span><span style="color:#000;font-weight:700">();</span> <span style="color:#000">p</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">WaitForExit</span><span style="color:#000;font-weight:700">();</span> <span style="color:#000">System</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">IO</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">StreamReader</span> <span style="color:#000">streamReader</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#204a87;font-weight:700">new</span> <span style="color:#000">System</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">IO</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">StreamReader</span><span style="color:#000;font-weight:700">(</span><span style="color:#000">tmpFile</span> <span style="color:#000;font-weight:700">+</span> <span style="color:#4e9a06">".hocr"</span><span style="color:#000;font-weight:700">);</span> <span style="color:#204a87;font-weight:700">string</span> <span style="color:#000">text</span> <span style="color:#000;font-weight:700">=</span> <span style="color:#000">streamReader</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">ReadToEnd</span><span style="color:#000;font-weight:700">();</span> <span style="color:#000">streamReader</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Close</span><span style="color:#000;font-weight:700">();</span> <span style="color:#204a87;font-weight:700">return</span> <span style="color:#000">text</span><span style="color:#000;font-weight:700">;</span> <span style="color:#000;font-weight:700">}</span> <span style="color:#204a87;font-weight:700">finally</span> <span style="color:#000;font-weight:700">{</span> <span style="color:#204a87;font-weight:700">if</span> <span style="color:#000;font-weight:700">(</span><span style="color:#000">System</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">IO</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">File</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Exists</span><span style="color:#000;font-weight:700">(</span><span style="color:#000">tmpFile</span><span style="color:#000;font-weight:700">))</span> <span style="color:#000">System</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">IO</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">File</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Delete</span><span style="color:#000;font-weight:700">(</span><span style="color:#000">tmpFile</span><span style="color:#000;font-weight:700">);</span> <span style="color:#204a87;font-weight:700">if</span> <span style="color:#000;font-weight:700">(</span><span style="color:#000">System</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">IO</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">File</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Exists</span><span style="color:#000;font-weight:700">(</span><span style="color:#000">tmpFile</span> <span style="color:#000;font-weight:700">+</span> <span style="color:#4e9a06">".hocr"</span><span style="color:#000;font-weight:700">))</span> <span style="color:#000">System</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">IO</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">File</span><span style="color:#000;font-weight:700">.</span><span style="color:#000">Delete</span><span style="color:#000;font-weight:700">(</span><span style="color:#000">tmpFile</span> <span style="color:#000;font-weight:700">+</span> <span style="color:#4e9a06">".hocr"</span><span style="color:#000;font-weight:700">);</span> <span style="color:#000;font-weight:700">}</span> <span style="color:#000;font-weight:700">}</span> <span style="color:#000;font-weight:700">}</span><span style="color:#000;font-weight:700">}</span></code></pre></div>"
}
</script>

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
