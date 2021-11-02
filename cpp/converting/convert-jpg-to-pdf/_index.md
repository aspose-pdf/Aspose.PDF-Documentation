---
title: Convert JPG to PDF 
linktitle: Convert JPG to PDF
type: docs
weight: 190
url: /cpp/convert-jpg-to-pdf/
lastmod: "2021-10-01"
description: Learn how to easily convert a JPG images to PDF file. Also, you can convert an image to PDF with the same height and width of the page.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

No need to wonder how to convert JPG to PDF, because **Aspose.PDF for C++** library has best decision.

You can very easy convert a JPG images to PDF with Aspose.PDF for C++ by following steps:

1. Create a [String Class](https://apireference.aspose.com/pdf/cpp/class/system.string) for path name and file name.
1. An instance of a new Document object is created.
1. Add a new Page to this [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. A new Aspose::Pdf::Image is created.
1. The Aspose.PDF Image object is initialized using the input file.
1. Aspose.PDF Image is added to the Page as a Paragraph.
1. Load and save the input image file.

The code snippet below shows how to convert JPG Image to PDF using C++:

```cpp
void ConvertJPEGtoPDF() {

 std::clog << "JPEG to PDF convert: Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for input file name
 String infilename("sample.jpg");

 // String for input file name
 String outfilename("ImageToPDF-JPEG.pdf");

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
 std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```

Then you can see how to convert an image to PDF with the **same height and width of the page**. We will be getting the image dimensions and accordingly set the page dimensions of PDF document with the below steps:

1. Load input image file
1. Get the height and width of the image
1. Set height, width, and margins of a page
1. Save the output PDF file

Following code snippet shows how to convert an Image to PDF with same page height and width using C++:

```cpp
void ConvertJPGtoPDF_fitsize() {

 std::clog << "JPEG to PDF convert: Start" << std::endl;
 // String for path name
 String _dataDir("C:\\Samples\\Conversion\\");

 // String for input file name
 String infilename("sample.jpg");

 // String for input file name
 String outfilename("ImageToPDF-JPG.pdf");

 // Open document
 auto document = MakeObject<Document>();

 // Add empty page in empty document
 auto page = document->get_Pages()->Add();
 auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
 auto bitMap = MakeObject<System::Drawing::Bitmap>(fileStream);


 auto image = MakeObject<Aspose::Pdf::Image>();
 image->set_File(_dataDir + infilename);

 // Add image on a page
 page->get_Paragraphs()->Add(image);

 // Set page dimensions and margins
 page->get_PageInfo()->set_Height(bitMap->get_Height());
 page->get_PageInfo()->set_Width(bitMap->get_Width());
 page->get_PageInfo()->get_Margin()->set_Bottom(0);
 page->get_PageInfo()->get_Margin()->set_Top(0);
 page->get_PageInfo()->get_Margin()->set_Right(0);
 page->get_PageInfo()->get_Margin()->set_Left(0);
 page->get_Paragraphs()->Add(image);

 // Save output document
 document->Save(_dataDir + outfilename);
 std::clog << "JPEG to PDF convert: Finish" << std::endl;
}
```
