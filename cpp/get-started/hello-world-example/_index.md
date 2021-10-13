---
title: Aspose.PDF С# Example
linktitle: Hello World Example
type: docs
weight: 20
url: /net/hello-world-example/
description: This page show how use simple programming for create a PDF document containing text - Hello World.
aliases:
    - /net/hello-world/
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

A "Hello World" example is traditionally used to introduce features of a programming language or software with a simple use case.

Aspose.PDF for .NET is a feature rich PDF API that allows the developers to embed PDF document creation, manipulation & conversion capabilities in their .NET applications. It supports working with many popular file formats including PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX and image file formats. In this article, we are creating a PDF document containing text "Hello World!". After installing Aspose.PDF for .NET in your environment, you can execute below code sample to see how Aspose.PDF API works.

Below code snippet follows these steps:

1. Instantiate a [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object
1. Add a [Page](https://apireference.aspose.com/pdf/net/aspose.pdf/page) to document object
1. Create a [TextFragment](https://apireference.aspose.com/pdf/net/aspose.pdf.text/textfragment) object
1. Add TextFragment to [Paragraph](https://apireference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) collection of the page
1. [Save](https://apireference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) resultant PDF document

Following code snippet is a Hello World program to exhibit working of Aspose.PDF for .NET API.

```csharp
namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
        public static void HelloWorld()
        {
            // Initialize document object
            Document document = new Document();
            // Add page
            Page page = document.Pages.Add();
            // Add text to new page
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Hello World!"));
            // Save updated PDF
            var outputFileName = System.IO.Path.Combine(_dataDir, "HelloWorld_out.pdf");
            document.Save( outputFileName );
        }
    }
}
```
