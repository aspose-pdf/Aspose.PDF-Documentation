---
title: Convert BMP to PDF 
linktitle: Convert BMP to PDF
type: docs
weight: 220
url: /cpp/convert-bmp-to-pdf/
lastmod: "2021-06-05"
description: You may easily convert BMP bitmap files to PDF used Aspose.PDF. for C++ from the display device.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Convert BMP files to PDF document using **Aspose.PDF for C++** library.

<abbr title="Bitmap Image File">BMP</abbr> images are Files having extension. BMP represent Bitmap Image files that are used to store bitmap digital images. These images are independent of graphics adapter and are also called device independent bitmap (DIB) file format.
You can convert BMP to PDF files with Aspose.PDF for C++ API. Therefore, you can follow the following steps to convert BMP images:

1. Create a [String Class](https://apireference.aspose.com/pdf/cpp/class/system.string) for path name and file name.
1. An instance of a new Document object is created.
1. Add a new [Page](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page) to this [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. A new Aspose.Pdf BMP is created.
1. The Aspose.PDF BMP object is initialized using the input file.
1. Aspose.PDF BMP is added to the Page as a Paragraph.
1. Finally, save the output PDF file

So the following code snippet follows these steps and shows how to convert BMP to PDF using C++:

```cpp
void ConvertBMPtoPDF() {

 std::clog << "BMP to PDF convert: Start" << std::endl;

 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for input file name
 String infilename("sample.bmp");

 // String for input file name
 String outfilename("ImageToPDF-BMP.pdf");

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

 std::clog << "BMP to PDF convert: Finish" << std::endl;
}
```
