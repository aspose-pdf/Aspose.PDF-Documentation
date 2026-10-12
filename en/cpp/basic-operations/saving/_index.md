---
title: Save PDF document programmatically
linktitle: Save PDF
type: docs
weight: 30
url: /cpp/save-pdf-document/
description: Save PDF documents in C++ to files or streams and convert documents to PDF/A-3u using Aspose.PDF.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Save PDFs to Files or Streams and Convert to PDF/A in C++
Abstract: Learn how to save PDF document changes to a file or stream with Aspose.PDF for C++. A separate example converts and saves a document as PDF/A-3u.
---

Use [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) to persist changes to a PDF.

## Save a PDF to a file

The example from `save-document-01.cpp` adds an empty page and saves the modified document to the output path.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Add an empty page with [PageCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Save the modified document to the output path with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
void SaveDocument(String path_infile, String path_outfile)
{
    auto document = MakeObject<Document>(path_infile);
    document->get_Pages()->Add();
    document->Save(path_outfile);
}
```

## Save a PDF to a stream

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Add an empty page with [PageCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Open a writable file stream with [System::IO::File::OpenWrite()](https://reference.aspose.com/pdf/cpp/system.io/file/).
1. Pass the stream to [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/io/file.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void SaveDocumentStream(String path_infile, String path_outfile)
{
    auto document = MakeObject<Document>(path_infile);
    document->get_Pages()->Add();

    auto fileStream = System::IO::File::OpenWrite(path_outfile);
    document->Save(fileStream);
}
```

## Convert and save as PDF/A-3u

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [PdfFormatConversionOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/pdfformatconversionoptions/) with [PdfFormat::PDF_A_3U](https://reference.aspose.com/pdf/cpp/aspose.pdf/pdfformat/).
1. Convert the document with [Convert()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/convert/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/IO/ConvertStrategies/PdfFormat.h>
#include <Aspose.PDF.Cpp/PdfFormatConversionOptions.h>

using namespace System;
using namespace Aspose::Pdf;

void SaveDocumentAsPdfA(String path_infile, String path_outfile)
{
    auto document = MakeObject<Document>(path_infile);
    auto options = MakeObject<PdfFormatConversionOptions>(Aspose::Pdf::PdfFormat::PDF_A_3U);
    document->Convert(options);
    document->Save(path_outfile);
}
```
