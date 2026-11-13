---
title: What's new
linktitle: What's new
type: docs
weight: 10
url: /cpp/whatsnew/
description: Review selected Aspose.PDF for C++ release highlights, including new conversion formats, image handling, forms, and runtime improvements.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: false
AlternativeHeadline: Aspose.PDF for C++ Release Highlights
Abstract: Explore selected C++ release updates from 21.4 through the source page's 25.3 section. Examples demonstrate conversion and image workflows; the release notes provide the complete change history.
---

This page summarizes selected updates from the published C++ What's New page. For newer releases and complete fixes, see the [Aspose.PDF for C++ release notes](https://releases.aspose.com/pdf/cpp/release-notes/).

## What's new in Aspose.PDF 25.3

The source's 25.3 section announces Markdown export, available since 25.2. Use [SaveFormat::Markdown](https://reference.aspose.com/pdf/cpp/aspose.pdf/saveformat/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/SaveFormat.h>

void ExportMarkdown(System::String input, System::String output)
{
    auto pdf = System::MakeObject<Aspose::Pdf::Document>(input);
    pdf->Save(output, Aspose::Pdf::SaveFormat::Markdown);
}
```

## What's new in Aspose.PDF 24.11

DJVU input became available through [DjvuLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/djvuloadoptions/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/DjvuLoadOptions.h>

void ImportDjvu(System::String input, System::String output)
{
    auto settings = System::MakeObject<Aspose::Pdf::DjvuLoadOptions>();
    auto pdf = System::MakeObject<Aspose::Pdf::Document>(input, settings);
    pdf->Save(output);
}
```

## What's new in Aspose.PDF 24.10

CDR input became available through [CdrLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/cdrloadoptions/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/CdrLoadOptions.h>

void ImportCdr(System::String input, System::String output)
{
    auto settings = System::MakeObject<Aspose::Pdf::CdrLoadOptions>();
    auto pdf = System::MakeObject<Aspose::Pdf::Document>(input, settings);
    pdf->Save(output);
}
```

## What's new in Aspose.PDF 24.8

SVG placement through [Page::AddImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/addimage/) was added.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

void PlaceSvg(System::String image, System::String output)
{
    auto pdf = System::MakeObject<Aspose::Pdf::Document>();
    auto sheet = pdf->get_Pages()->Add();
    sheet->AddImage(image, System::MakeObject<Aspose::Pdf::Rectangle>(100, 100, 400, 400));
    pdf->Save(output);
}
```

## What's new in Aspose.PDF 24.4

SVG loading was corrected. See [SVG conversion examples](/pdf/cpp/convert-images-format-to-pdf/#convert-svg-to-pdf).

## What's new in Aspose.PDF 24.3

PDF-to-TIFF conversion was introduced. The source configures [TiffDevice](https://reference.aspose.com/pdf/cpp/aspose.pdf.devices/tiffdevice/) to skip blank pages and use 8-bit color.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Devices/TiffDevice.h>
#include <Aspose.PDF.Cpp/Devices/TiffSettings.h>
#include <Aspose.PDF.Cpp/Devices/ColorDepth.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>

void ExportTiff(System::String input, System::String output)
{
    auto pdf = System::MakeObject<Aspose::Pdf::Document>(input);
    auto renderer = System::MakeObject<Aspose::Pdf::Devices::TiffDevice>();
    renderer->get_Settings()->set_SkipBlankPages(true);
    renderer->get_Settings()->set_Depth(Aspose::Pdf::Devices::ColorDepth::Format8bpp);
    auto stream = System::IO::File::Create(output);
    renderer->Process(pdf, 1, pdf->get_Pages()->get_Count(), stream);
    stream->Close();
}
```

## What's new in Aspose.PDF 24.2

JPX decoding performance and recovery of malformed document structures were improved.

## What's new in Aspose.PDF 23.7

EPUB export and PCL loading were added. EPUB uses [SaveFormat::Epub](https://reference.aspose.com/pdf/cpp/aspose.pdf/saveformat/); PCL uses [PclLoadOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/pclloadoptions/).

## What's new in Aspose.PDF 23.1

DICOM image support was added. See the [DICOM example](/pdf/cpp/convert-images-format-to-pdf/#convert-dicom-to-pdf).

## What's new in Aspose.PDF 22.11

The first public macOS edition was released.

## What's new in Aspose.PDF 22.5

XFA form support was introduced. See [XFA Forms](/pdf/cpp/xfa-forms/).

## What's new in Aspose.PDF 22.4

The codebase incorporated Aspose.PDF for .NET and Aspose.Imaging 22.4, with thumbnail, region-constructor, and monochrome-image updates.

## What's new in Aspose.PDF 22.3

Additional overloads accepted ArrayView parameters.

## What's new in Aspose.PDF 22.1

Updates included a CoreFX-based System::Xml implementation, double-conversion 3.1.7, and signed DLLs.

## What's new in Aspose.PDF 21.10

SVG-to-PDF conversion became available. See [basic and advanced SVG conversion](/pdf/cpp/convert-images-format-to-pdf/#convert-svg-to-pdf).

## What's new in Aspose.PDF 21.4

HTML export became available through [SaveFormat::Html](https://reference.aspose.com/pdf/cpp/aspose.pdf/saveformat/).
