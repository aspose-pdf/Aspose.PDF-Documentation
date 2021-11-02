---
title: Convert TIFF to PDF 
linktitle: Convert TIFF to PDF
type: docs
weight: 210
url: /cpp/convert-tiff-to-pdf/
lastmod: "2021-06-05"
description: Aspose.PDF for C++ allows converting multi-page or multi-frame TIFF images to PDF applications.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF** file format supported, be it a single frame or multi-frame <abbr title="Tag Image File Format">TIFF</abbr> image. It means that you can convert the TIFF image to PDF in your C++ applications.

TIFF or TIF, Tagged Image File Format, represents raster images that are meant for usage on a variety of devices that comply with this file format standard. TIFF image can contain several frames with different images. Aspose.PDF file format is also supported, be it a single frame or multi-frame TIFF image. So you can convert the TIFF image to PDF in your C++ applications. Therefore, we will consider an example of converting multi-page TIFF image to multi-page PDF document with below steps:

1. Create a [String Class](https://apireference.aspose.com/pdf/cpp/class/system.string) for path name and file name.
1. An instance of a new Document object is created.
1. Add a new Page to this [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. A new Aspose.Pdf TIFF is created.
1. The Aspose.PDF TIFF object is initialized using the input file.
1. Aspose.PDF TIFF is added to the Page as a Paragraph.
1. Load and save the input image file.

Moreover, the following code snippet shows how to convert multi-page or multi-frame TIFF image to PDF with C++:

```cpp
void ConvertTIFFtoPDF() {

 std::clog << "TIFF to PDF convert: Start" << std::endl;

 String _dataDir("C:\\Samples\\Conversion\\");
 String infilename("sample.tiff");
 String outfilename("ImageToPDF-TIFF.pdf");

 auto fileStream = System::IO::File::OpenRead(_dataDir + infilename);
 auto myimage = MakeObject<System::Drawing::Bitmap>(fileStream);

 auto document = MakeObject<Document>();
 auto page = document->get_Pages()->Add();

 auto currentImage = MakeObject<System::IO::MemoryStream>();
 myimage->Save(currentImage, System::Drawing::Imaging::ImageFormat::get_Tiff());

 auto imageht = MakeObject<Aspose::Pdf::Image>();
 imageht->set_ImageStream(currentImage);
 page->get_Paragraphs()->Add(imageht);

 document->Save(_dataDir + outfilename);

 std::clog << "TIFF to PDF convert: Finish" << std::endl;
}
```
