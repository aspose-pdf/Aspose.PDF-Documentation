---
title: Aspose.PDF С++ Example
linktitle: Hello World Example
type: docs
weight: 20
url: /cpp/hello-world-example/
description: This page show how use simple programming for create a PDF document containing text - Hello World.
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.6
---

A "Hello World" example is traditionally used to introduce features of a programming language or software with a simple use case.

Aspose.PDF for C++ is a feature rich PDF API that allows the developers to embed PDF document creation, manipulation & conversion capabilities in their C++ applications. It supports working with many popular file formats including PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX and image file formats. In this article, we are creating a PDF document containing text "Hello World!". After installing Aspose.PDF for C++ in your environment, you can execute below code sample to see how Aspose.PDF API works.

Below code snippet follows these steps:

1. Create a [String Class](https://apireference.aspose.com/pdf/cpp/class/system.string) for path name and file name.
1. Instantiate a [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) object. In this step we will create an empty PDF document with some metadata but without pages.
1. Add a [Page](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page) to the document object. So, now our document will have one page.
1. [Save](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa)resultant PDF document

Following code snippet is a Hello World program to exhibit working of Aspose.PDF for C++ API.

```cpp
void ExampleSimple()
{
    // Buffer to hold combined path.
    String outputFileName;

    // String for path name.
    String _dataDir("C:\\Samples\\");

    // String for file name.
    String filename("HelloWorld_out.pdf");

    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    // Add text to new page
    auto text = MakeObject<TextFragment>(u"Hello world!");

    auto paragraphs = page->get_Paragraphs();
    paragraphs->Add(text);

    // Save updated PDF
    outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```
