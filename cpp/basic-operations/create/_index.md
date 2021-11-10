---
title: Create PDF Document using C++
linktitle: Create
type: docs
weight: 10
url: /cpp/create-document/
description: Learn how to create PDF file in Aspose.PDF for C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++**  API lets Cpp application developers to embed PDF documents processing functionality in their applications. It can be used to create and read PDF files without the need of any other software installed on the underlying machine. Aspose.PDF for C++ can be used in a variety of C++ application types such as Desktop, JSP, and JSF applications.

## How to create PDF File using C++

To create a PDF file using C++, the following steps can be used.

1. Instantiate a [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document/) object
1. Add a [Page](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page/) to document object
1. Create a [TextFragment](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) object
1. Add [TextFragment](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) to [Paragraph](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs/) collection of the page
1. Save the resultant PDF document

```cpp
void CreatePDF() {

 // String for path name.
 String _dataDir("C:\\Samples\\");

 // String for file name.
 String filename("sample-new.pdf");

 // Initialize document object
 auto document = MakeObject<Document>();
 // Add page
 auto page = document->get_Pages()->Add();

 // Add text to new page
 auto textFragment = MakeObject<TextFragment>(u"Hello World!");
 page->get_Paragraphs()->Add(textFragment);

 // Save updated PDF
 String outputFileName = _dataDir + filename;

 document->Save(outputFileName);
}
```
