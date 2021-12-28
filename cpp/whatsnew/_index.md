---
title: What's new
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
