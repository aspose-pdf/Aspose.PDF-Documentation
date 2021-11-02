---
title: Convert PNG to PDF 
linktitle: Convert PNG to PDF
type: docs
weight: 200
url: /cpp/convert-png-to-pdf/
lastmod: "2021-06-05"
description: This article shows how to convert PNG to PDF with Aspose.PDF library in your C++ applications. You can convert PNG images to PDF format using simple steps.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for C++** support feature to convert PNG images to PDF format. Check the next code snippet for realizing you task.

<abbr title="Portable Network Graphics">PNG</abbr> refers to a type of raster image file format that use loseless compression, that makes it popular among its users.

You can convert PNG to PDF image using the below steps:

1. Create a [String Class](https://apireference.aspose.com/pdf/cpp/class/system.string) for path name and file name.
1. An instance of a new Document object is created.
1. Add a new Page to this [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. A new Aspose.Pdf PNG is created.
1. The Aspose.PDF PNG object is initialized using the input file.
1. Aspose.PDF PNG is added to the Page as a Paragraph.
1. Load and save the input image file.

Moreover, the code snippet below shows how to convert PNG to PDF with C# in your C++ applications:

```cpp
void ConvertPNGtoPDF() {

 std::clog << "PNG to PDF convert: Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for input file name
 String infilename("sample.png");

 // String for input file name
 String outfilename("ImageToPDF-PNG.pdf");

 // Open document
 auto document = MakeObject<Document>();

 // Add empty page in empty document
 auto page = document->get_Pages()->Add();
 auto image = MakeObject<Aspose::Pdf::Image>();
 image->set_File(_dataDir + infilename);

 // Add image on a page
 page->get_Paragraphs()->Add(image);

 // Save output document
 document->Save(_dataDir + outfilename);
 std::clog << "PNG to PDF convert: Finish" << std::endl;
}
```
