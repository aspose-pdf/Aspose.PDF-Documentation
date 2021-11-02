---
title: Convert DICOM to PDF 
linktitle: Convert DICOM to PDF
type: docs
weight: 250
url: /cpp/convert-dicom-to-pdf/
lastmod: "2021-06-05"
description: Convert medical images saved in DICOM format to a PDF file using Aspose.PDF for C++.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> format is the medical industry standard for the creation, storage, transmission, and visualization of digital medical images and documents of examined patients.

**Aspsoe.PDF for C++** allows you to convert DICOM and SVG images, but for technical reasons to add images you need to specify the type of file to be added to PDF:

1. Create a [String Class](https://apireference.aspose.com/pdf/cpp/class/system.string) for path name and file name.
1. Instantiate [Document](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document) Object.
1. Add a [Page](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.page) to pages collection of document.
1. Aspose.PDF TDicom is added to the Page as a Paragraph.
1. Load and [Save](https://apireference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) the input image file.

The following code snippet shows how to convert DICOM files to PDF  format with Aspose.PDF. You should load DICOM image, place the image on a page in a PDF file and save the output as PDF.

```cpp
void ConvertDICOMtoPDF()
{
 std::clog << "DICOM to PDF convert: Start" << std::endl;

 String _dataDir("C:\\Samples\\Conversion\\");
 String infilename("CR_Anno.dcm");
 String outfilename("PDFWithDicomImage_out.pdf");

 // Instantiate Document Object
 auto document = MakeObject<Document>();

 // Add a page to pages collection of document
 auto page = document->get_Pages()->Add();

 auto image = MakeObject<Aspose::Pdf::Image>();
 image->set_File(_dataDir + infilename);
 image->set_FileType(Aspose::Pdf::ImageFileType::Dicom);

 page->get_Paragraphs()->Add(image);

 // Save output as PDF format
 document->Save(_dataDir + outfilename);
 std::clog << "DICOM to PDF convert: Finish" << std::endl;
}
```
