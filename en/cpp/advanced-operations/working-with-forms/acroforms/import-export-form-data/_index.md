---
title: Import and export PDF form data in C++
linktitle: Import and Export Form Data
type: docs
weight: 40
url: /cpp/import-export-form-data/
description: Export and import PDF form data in FDF, XFDF, and XML formats using Aspose.PDF for C++.
lastmod: "2026-10-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Exchange AcroForm Data through FDF, XFDF, and XML in C++
Abstract: Learn how to move field data between PDFs and external data files with Aspose.PDF for C++. The examples export three formats and import matching data files before saving the updated PDF.
---

## Export form data to FDF

1. Create a [Aspose::Pdf::Facades::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) facade for the input PDF.
1. Create a writable output stream.
1. Call [ExportFdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) on [Aspose::Pdf::Facades::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) with the stream.
1. Close the stream and the facade.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>

using namespace System;

void FormExamples::ExportDataToFdf(String inputFile, String outputFile)
{
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(inputFile);
    auto stream = System::IO::File::Create(outputFile);
    form->ExportFdf(stream);
    stream->Close();
    form->Close();
}
```

## Export form data to XFDF

1. Create a [Aspose::Pdf::Facades::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) facade for the input PDF.
1. Create a writable output stream.
1. Call [ExportXfdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) on [Aspose::Pdf::Facades::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) with the stream.
1. Close the stream and the facade.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;

void FormExamples::ExportDataToXfdf(String inputFile, String outputFile)
{
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(inputFile);
    auto stream = System::IO::File::Create(outputFile);
    form->ExportXfdf(stream);
    stream->Close();
    form->Close();
}
```

## Export form data to XML

1. Create a [Aspose::Pdf::Facades::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) facade for the input PDF.
1. Create a writable output stream.
1. Call [ExportXml()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) on [Aspose::Pdf::Facades::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) with the stream.
1. Close the stream and the facade.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;

void FormExamples::ExportDataToXml(String inputFile, String outputFile)
{
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(inputFile);
    auto stream = System::IO::File::Create(outputFile);
    form->ExportXml(stream);
    stream->Close();
    form->Close();
}
```

## Import form data from FDF

The data file is resolved relative to outputFile, not inputFile.

1. Create a [Aspose::Pdf::Facades::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) facade for the input PDF.
1. Open StudentInfoFormElectronic.fdf from the output PDF directory.
1. Call [ImportFdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) on [Aspose::Pdf::Facades::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) with the stream.
1. Save the modified PDF to outputFile.
1. Close the input stream and the facade.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;

void FormExamples::ImportDataFromFdf(String inputFile, String outputFile)
{
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(inputFile);
    auto stream = System::IO::File::OpenRead(System::IO::Path::Combine(
        System::IO::Path::GetDirectoryName(outputFile), u"StudentInfoFormElectronic.fdf"));
    form->ImportFdf(stream);
    form->Save(outputFile);
    stream->Close();
    form->Close();
}
```

## Import form data from XFDF

The data file is resolved relative to outputFile, not inputFile.

1. Create a [Aspose::Pdf::Facades::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) facade for the input PDF.
1. Open StudentInfoFormElectronic.xfdf from the output PDF directory.
1. Call [ImportXfdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) on [Aspose::Pdf::Facades::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) with the stream.
1. Save the modified PDF to outputFile.
1. Close the input stream and the facade.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;

void FormExamples::ImportDataFromXfdf(String inputFile, String outputFile)
{
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(inputFile);
    auto stream = System::IO::File::OpenRead(System::IO::Path::Combine(
        System::IO::Path::GetDirectoryName(outputFile), u"StudentInfoFormElectronic.xfdf"));
    form->ImportXfdf(stream);
    form->Save(outputFile);
    stream->Close();
    form->Close();
}
```

## Import form data from XML

The XML example closes the stream and facade after success and when a System::Exception is caught, then rethrows the exception.

1. Create a [Aspose::Pdf::Facades::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) facade for the input PDF.
1. Open StudentInfoFormElectronic.xml from the output PDF directory.
1. Call [ImportXml()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) on [Aspose::Pdf::Facades::Form](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/form/) with the stream.
1. Save the modified PDF to outputFile.
1. Close the input stream and the facade.

```cpp
#include <Aspose.PDF.Cpp/Facades/Form.h>
#include <system/io/file.h>
#include <system/io/path.h>

using namespace System;
using namespace Aspose::Pdf;

void FormExamples::ImportDataFromXml(String inputFile, String outputFile)
{
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(inputFile);
    auto stream = System::IO::File::OpenRead(System::IO::Path::Combine(
        System::IO::Path::GetDirectoryName(outputFile), u"StudentInfoFormElectronic.xml"));

    const auto cleanup = [&]() {
        stream->Close();
        form->Close();
    };

    try {
        form->ImportXml(stream);
        form->Save(outputFile);
    }
    catch (const System::Exception&) {
        cleanup();
        throw;
    }

    cleanup();
}
```
