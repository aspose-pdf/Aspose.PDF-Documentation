---
title: What's new from C++
linktitle: What's new
type: docs
weight: 10
url: /cpp/whatsnew/
description: In this page introduces the most popular new features in Aspose.PDF for C++ that have been introduced in recent releases.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-22"
---

## What's new in Aspose.PDF 23.7

- The saving of PDF documents into EPUB format has been introduced:

```cpp

    void ConvertPDFtoEPUB()
    {
        std::clog << __func__ << ": Start" << std::endl;
        // String for path name
        String _dataDir("C:\\Samples\\Conversion\\");

        // String for input file name
        String infilename("sample.pdf");
        // String for output file name
        String outfilename("PDFToEPUB_out.epub");

        // Open document
        auto document = MakeObject<Document>(_dataDir + infilename);

        // Save PDF file into EPUB format
        document->Save(_dataDir + outfilename, SaveFormat::Epub);
        std::clog << __func__ << ": Finish" << std::endl;
    }
```

- Loading PCL format files has been implemented:

```cpp

    using namespace System;
    using namespace Aspose::Pdf;

    int main(int argc, char** argv)
    {
        try
        {
            auto lic = MakeObject<Aspose::Pdf::License>();
            lic->SetLicense(u"c:/aspose.pdf/License/Aspose.PDF.C++.lic");

            auto options = System::MakeObject<PclLoadOptions>();
            options->ConversionEngine = Aspose::Pdf::PclLoadOptions::ConversionEngines::NewEngine;
            options->SupressErrors = false;

            auto doc = System::MakeObject<Document>(u"c:/aspose.pdf/PCL/37432.pcl", options);
            doc->Save(u"e:/37432.pdf");
        }
        catch (const System::Exception& error)
        {
            Console::WriteLine(u"Error: {0}", error->get_Message());
            return 1;
        }
        catch (const std::exception& error)
        {
            std::cerr << "Error: " << error.what() << std::endl;
            return 1;
        }

        return 0;
    }
```



## What's new in Aspose.PDF 23.1

From 23.1 the support of Dicom format images was added:

```cpp

    using namespace System;
    using namespace System::IO;
    using namespace Aspose::Pdf;

    int main()
    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();
        auto image = MakeObject<Image>();
        image->set_FileType(ImageFileType::Dicom);
        image->set_ImageStream(MakeObject<FileStream>(u"c:/aspose.pdf/Aspose.Pdf/38067-1.dcm", FileMode::Open, FileAccess::Read));
        page->get_Paragraphs()->Add(image);
        document->Save(u"e:/document.pdf");
    }
```

## What's new in Aspose.PDF 22.11

From 22.11 announced the first Public Release of **Aspose.PDF for C++ macOS**.

We are pleased to announce the first public release of Aspose.PDF for C++ macOS. Aspose.PDF for C++ macOS is a proprietary C++ library that allows developers to create and manipulate PDF documents without using Adobe Acrobat.
Aspose.PDF for C++ macOS allows developers to create forms, add/edit text, manipulate PDF pages, add annotations, process custom fonts, and more.

## What's new in Aspose.PDF 22.7

The Skia version used is updated.

## What's new in Aspose.PDF 22.5

Support of XFA forms in PDF documents was implemented.

## What's new in Aspose.PDF 22.4

The new version of Aspose.PDF for C++ has a codebase of Aspose.PDF for .Net 22.4 and Aspose.Imaging 22.4.

- the System::Drawing::GetThumbnailImage() method was implemented;
- the RegionDataNodeRect constructor was optimized;
- the 1 bit per pixel black-and-white image loading was fixed.

## What's new in Aspose.PDF 22.3

The method overloads were added to numerous classes. These support ArrayView-typed parameters where only ArrayPtr was supported previously.

## What's new in Aspose.PDF 22.1

The new version of Aspose.PDF for C++ has a codebase of Aspose.PDF for .Net 22.1:

- the new implementation for System::Xml was provided. Previously, we had custom implementation which was based on the libxml2 and libxslt libraries. The new version is based on the ported CoreFX code

- the double-conversion library was upgraded to 3.1.7 version

- Dll files are signed with Aspose certificate

## What's new in Aspose.PDF 21.10

### Aspose.PDF for C++ support feature to convert SVG to PDF format

The following code snippet shows the process of converting SVG file into PDF format with Aspose.PDF for C++.

```cpp
void ConvertSVGtoPDF()
{
    std::clog << "SVG to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample.svg");
    String outfilename("ImageToPDF-SVG.pdf");

    auto options = MakeObject<SvgLoadOptions>();
    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << "SVG to PDF convert: Finish" << std::endl;
}
```

Сonsider an example with advanced features:

```cpp
void ConvertSVGtoPDF_Advanced()
{
    std::clog << "SVG to PDF convert: Start" << std::endl;

    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("Sweden-Royal-flag-grand-coa.svg");
    String outfilename("ImageToPDF-SVG.pdf");

    auto options = MakeObject<SvgLoadOptions>();
    options->set_AdjustPageSize(true);
    options->ConversionEngine = SvgLoadOptions::ConversionEngines::NewEngine;

    try {
    auto document = MakeObject<Document>(_dataDir + infilename, options);
    document->Save(_dataDir + outfilename);
    }
    catch (System::Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }

    std::clog << "SVG to PDF convert: Finish" << std::endl;
}
```

## What's new in Aspose.PDF 21.4

### Saving PDF documents to HTML format has been implemented

Aspose.PDF for C++ support the features to convert a PDF file into HTML.

```cpp
#include "Aspose.PDF.Cpp/Document.h"
#include "Aspose.PDF.Cpp/SaveFormat.h"

using namespace System;
using namespace Aspose::Pdf;

int main()
{
    auto doc = MakeObject<Document>(u"e:\\sample.pdf");
    doc->Save(u"e:\\sample.html", SaveFormat::Html);
}
```
