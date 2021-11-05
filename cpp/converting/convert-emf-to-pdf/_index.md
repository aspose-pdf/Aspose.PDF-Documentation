---
title: Convert EMF to PDF 
linktitle: Convert EMF to PDF
type: docs
weight: 230
url: /cpp/convert-emf-to-pdf/
lastmod: "2021-06-05"
description: Both bitmap as well as vector graphics can be files having an EMF extension. Convert EMF to PDF file simply with C++.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Enhanced metafile format">EMF</abbr>EMF stores graphical images device-independently. Metafiles of EMF comprises of variable-length records in chronological order that can render the stored image after parsing on any output device. Furthermore, you can convert EMF to PDF image using the below steps:

1. Create a [String Class](https://apireference.aspose.com/pdf/cpp/class/system.string) for path name and file name.
1. An instance of a new Document object is created.
1. Add a new Page to this [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. A new Aspose.Pdf TIFF is created.
1. The Aspose.PDF TIFF object is initialized using the input file.
1. Aspose.PDF TIFF is added to the Page as a Paragraph.
1. Load and [Save](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) the input image file.

Moreover, the following code snippet shows how to convert an EMF to PDF with C++ in your code snippet:

```cpp
void ConvertEMFtoPDF() {
 std::clog << "EMF to PDF convert: Start" << std::endl;

 String _dataDir("C:\\Samples\\Conversion\\");
 String infilename("sample.emf");
 String outfilename("ImageToPDF_emf.pdf");

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

 std::clog << "EMF to PDF convert: Finish" << std::endl;
}
```
