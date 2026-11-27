---
title: Optimize PDF documents in C++
linktitle: Optimize PDF documents
type: docs
weight: 50
url: /cpp/optimize-pdf/
description: Optimize PDF resources, compress images, remove unused data, flatten interactive content, and convert pages to grayscale with Aspose.PDF for C++.
lastmod: "2026-11-26"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Compress PDF Images and Remove Unused Resources in C++
Abstract: Learn how to optimize PDF resources, compress images, and remove unused or duplicate data with Aspose.PDF for C++. Additional examples flatten interactive content and convert pages to grayscale; file-size results depend on the input PDF.
---

Optimize PDF resources, compress images, remove unused data, flatten interactive content, and convert pages to grayscale with Aspose.PDF for C++.

## Report input and output file sizes

The examples that compare file sizes define `PrintOptimizationFileSizes` in their snippets. The sample repository also provides the following standalone helper. Optimization results depend on the PDF; an output file can be the same size or larger.

1. Read the input file size before modifying the PDF.
1. Read the saved output file size.
1. Print both sizes for comparison.

```cpp
#pragma once

#include <cstdint>
#include <system/console.h>
#include <system/io/file_info.h>
#include <system/string.h>

inline void PrintOptimizationFileSizes(int64_t originalSize, System::String outputFile)
{

    auto output = System::MakeObject<System::IO::FileInfo>(outputFile);
    System::Console::WriteLine(
        u"Original file size: {0}. Reduced file size: {1}",
        originalSize, output->get_Length());
}
```

## Optimize for web viewing

Web optimization is distinct from reducing resources and does not guarantee a smaller file.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Call [Optimize()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/optimize/) to organize the PDF for web access.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).
1. Print the input and output sizes using PrintOptimizationFileSizes().

Source example: `optimize-document-01.cpp`.

```cpp
#include <Aspose.PDF.Cpp/Document.h>

using namespace System;
using namespace Aspose::Pdf;

#include <system/io/file_info.h>
#include <system/console.h>

inline static void PrintOptimizationFileSizes(int64_t originalSize, System::String outputFile)
{

    auto output = System::MakeObject<System::IO::FileInfo>(outputFile);
    System::Console::WriteLine(
        u"Original file size: {0}. Reduced file size: {1}",
        originalSize, output->get_Length());
}


void OptimizePdf(String inputFile, String outputFile)
{
    const auto originalSize = System::MakeObject<System::IO::FileInfo>(inputFile)->get_Length();
    auto document = MakeObject<Document>(inputFile);
    document->Optimize();
    document->Save(outputFile);
    PrintOptimizationFileSizes(originalSize, outputFile);
}
```

## Optimize resources with default settings

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Call [OptimizeResources()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/optimizeresources/) using its default settings.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).
1. Print the input and output sizes.

```cpp
#include <Aspose.PDF.Cpp/Document.h>

#include <system/io/file_info.h>
#include <system/console.h>


using namespace System;
using namespace Aspose::Pdf;

inline void PrintOptimizationFileSizes(int64_t originalSize, System::String outputFile)
{

    auto output = System::MakeObject<System::IO::FileInfo>(outputFile);
    System::Console::WriteLine(
        u"Original file size: {0}. Reduced file size: {1}",
        originalSize, output->get_Length());
}

void ReduceSizePdf(String inputFile, String outputFile)
{
    const auto originalSize = System::MakeObject<System::IO::FileInfo>(inputFile)->get_Length();
    auto document = MakeObject<Document>(inputFile);
    document->OptimizeResources();
    document->Save(outputFile);
    PrintOptimizationFileSizes(originalSize, outputFile);
}
```

## Compress images

Image compression can reduce visual quality. Review the output before choosing a quality setting.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [OptimizationOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.optimization/optimizationoptions/).
1. Enable CompressImages and set ImageQuality to 50 through [ImageCompressionOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.optimization/imagecompressionoptions/).
1. Call [OptimizeResources()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/optimizeresources/) with the options.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).
1. Print the input and output sizes.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Optimization/OptimizationOptions.h>
#include <Aspose.PDF.Cpp/Optimization/ImageCompressionOptions.h>
#include <system/io/file_info.h>
#include <system/console.h>

using namespace System;
using namespace Aspose::Pdf;

inline static void PrintOptimizationFileSizes(int64_t originalSize, System::String outputFile)
{

    auto output = System::MakeObject<System::IO::FileInfo>(outputFile);
    System::Console::WriteLine(
        u"Original file size: {0}. Reduced file size: {1}",
        originalSize, output->get_Length());
}

void ShrinkingOrCompressingAllImages(String inputFile, String outputFile)
{
    const auto originalSize = System::MakeObject<System::IO::FileInfo>(inputFile)->get_Length();
    auto document = MakeObject<Document>(inputFile);
    auto options = MakeObject<Optimization::OptimizationOptions>();
    options->get_ImageCompressionOptions()->set_CompressImages(true);
    options->get_ImageCompressionOptions()->set_ImageQuality(50);
    document->OptimizeResources(options);
    document->Save(outputFile);
    PrintOptimizationFileSizes(originalSize, outputFile);
}
```

## Remove unused objects

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [OptimizationOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.optimization/optimizationoptions/) and enable RemoveUnusedObjects.
1. Call [OptimizeResources()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/optimizeresources/) with the options.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).
1. Print the input and output sizes.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Optimization/OptimizationOptions.h>
#include <system/io/file_info.h>
#include <system/console.h>

using namespace System;
using namespace Aspose::Pdf;

inline static void PrintOptimizationFileSizes(int64_t originalSize, System::String outputFile)
{

    auto output = System::MakeObject<System::IO::FileInfo>(outputFile);
    System::Console::WriteLine(
        u"Original file size: {0}. Reduced file size: {1}",
        originalSize, output->get_Length());
}

void RemovingUnusedObjects(String inputFile, String outputFile)
{
    const auto originalSize = System::MakeObject<System::IO::FileInfo>(inputFile)->get_Length();
    auto document = MakeObject<Document>(inputFile);
    auto options = MakeObject<Optimization::OptimizationOptions>();
    options->set_RemoveUnusedObjects(true);
    document->OptimizeResources(options);
    document->Save(outputFile);
    PrintOptimizationFileSizes(originalSize, outputFile);
}
```

## Remove unused streams

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [OptimizationOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.optimization/optimizationoptions/) and enable RemoveUnusedStreams.
1. Call [OptimizeResources()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/optimizeresources/) with the options.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).
1. Print the input and output sizes.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Optimization/OptimizationOptions.h>

#include <system/io/file_info.h>
#include <system/console.h>

using namespace System;
using namespace Aspose::Pdf;

inline static void PrintOptimizationFileSizes(int64_t originalSize, System::String outputFile)
{

    auto output = System::MakeObject<System::IO::FileInfo>(outputFile);
    System::Console::WriteLine(
        u"Original file size: {0}. Reduced file size: {1}",
        originalSize, output->get_Length());
}

void RemovingUnusedStreams(String inputFile, String outputFile)
{
    const auto originalSize = System::MakeObject<System::IO::FileInfo>(inputFile)->get_Length();
    auto document = MakeObject<Document>(inputFile);
    auto options = MakeObject<Optimization::OptimizationOptions>();
    options->set_RemoveUnusedStreams(true);
    document->OptimizeResources(options);
    document->Save(outputFile);
    PrintOptimizationFileSizes(originalSize, outputFile);
}
```

## Link duplicate streams

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [OptimizationOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.optimization/optimizationoptions/) and enable LinkDuplicateStreams.
1. Call [OptimizeResources()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/optimizeresources/) with the options.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).
1. Print the input and output sizes.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Optimization/OptimizationOptions.h>
#include <system/io/file_info.h>
#include <system/console.h>

using namespace System;
using namespace Aspose::Pdf;

inline static void PrintOptimizationFileSizes(int64_t originalSize, System::String outputFile)
{

    auto output = System::MakeObject<System::IO::FileInfo>(outputFile);
    System::Console::WriteLine(
        u"Original file size: {0}. Reduced file size: {1}",
        originalSize, output->get_Length());
}

void LinkingDuplicateStreams(String inputFile, String outputFile)
{
    const auto originalSize = System::MakeObject<System::IO::FileInfo>(inputFile)->get_Length();
    auto document = MakeObject<Document>(inputFile);
    auto options = MakeObject<Optimization::OptimizationOptions>();
    options->set_LinkDuplicateStreams(true);
    document->OptimizeResources(options);
    document->Save(outputFile);
    PrintOptimizationFileSizes(originalSize, outputFile);
}
```

## Unembed fonts

Removing embedded fonts makes rendering dependent on fonts available to the viewer and can affect appearance.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [OptimizationOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.optimization/optimizationoptions/) and enable UnembedFonts.
1. Call [OptimizeResources()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/optimizeresources/) with the options.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).
1. Print the input and output sizes.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Optimization/OptimizationOptions.h>

#include <system/io/file_info.h>
#include <system/console.h>

using namespace System;
using namespace Aspose::Pdf;

inline static void PrintOptimizationFileSizes(int64_t originalSize, System::String outputFile)
{

    auto output = System::MakeObject<System::IO::FileInfo>(outputFile);
    System::Console::WriteLine(
        u"Original file size: {0}. Reduced file size: {1}",
        originalSize, output->get_Length());
}

void UnembedFonts(String inputFile, String outputFile)
{
    const auto originalSize = System::MakeObject<System::IO::FileInfo>(inputFile)->get_Length();
    auto document = MakeObject<Document>(inputFile);
    auto options = MakeObject<Optimization::OptimizationOptions>();
    options->set_UnembedFonts(true);
    document->OptimizeResources(options);
    document->Save(outputFile);
    PrintOptimizationFileSizes(originalSize, outputFile);
}
```

## Flatten annotations

Reverse iteration accounts for annotations being removed during flattening.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through every [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/).
1. Traverse the annotations in reverse order and call [Flatten()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotation/) on each one.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Annotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>

#include <system/io/file_info.h>
#include <system/console.h>

using namespace System;
using namespace Aspose::Pdf;

inline static void PrintOptimizationFileSizes(int64_t originalSize, System::String outputFile)
{

    auto output = System::MakeObject<System::IO::FileInfo>(outputFile);
    System::Console::WriteLine(
        u"Original file size: {0}. Reduced file size: {1}",
        originalSize, output->get_Length());
}

void FlattenAnnotations(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto page : document->get_Pages()) {
        auto annotations = page->get_Annotations();
        // Flatten removes annotations, so visit the collection in reverse.
        for (int index = annotations->get_Count(); index >= 1; --index) {
            annotations->idx_get(index)->Flatten();
        }
    }
    document->Save(outputFile);
}
```

## Flatten form fields

Flattened fields no longer provide interactive form entry.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the document form and take a snapshot of its fields.
1. Call [Flatten()](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/field/) on each field in the snapshot.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).
1. Print the input and output sizes.

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Field.h>
#include <system/array.h>

using namespace System;
using namespace Aspose::Pdf;

#include <system/io/file_info.h>
#include <system/console.h>

inline static void PrintOptimizationFileSizes(int64_t originalSize, System::String outputFile)
{

    auto output = System::MakeObject<System::IO::FileInfo>(outputFile);
    System::Console::WriteLine(
        u"Original file size: {0}. Reduced file size: {1}",
        originalSize, output->get_Length());
}

void FlattenForms(String inputFile, String outputFile)
{
    const auto originalSize = System::MakeObject<System::IO::FileInfo>(inputFile)->get_Length();
    auto document = MakeObject<Document>(inputFile);
    auto form = document->get_Form();
    if (form != nullptr) {
        // Snapshot the fields before Flatten changes the form collection.
        auto fields = form->get_Fields();
        for (auto& field : fields) {
            field->Flatten();
        }
    }
    document->Save(outputFile);
    PrintOptimizationFileSizes(originalSize, outputFile);
}
```

## Convert pages to grayscale

Grayscale conversion changes page colors; file-size reduction depends on the input.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through each [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) and call [MakeGrayscale()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/).
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;

void ConvertPdfFromRgbColorspaceToGrayscale(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto& page : document->get_Pages()) {
        page->MakeGrayscale();
    }
    document->Save(outputFile);
}
```

## Use Flate image encoding

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [OptimizationOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.optimization/optimizationoptions/).
1. Set the [ImageCompressionOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.optimization/imagecompressionoptions/) Encoding property to ImageEncoding::Flate.
1. Call [OptimizeResources()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/optimizeresources/) with the options.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/)

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Optimization/OptimizationOptions.h>
#include <Aspose.PDF.Cpp/Optimization/ImageCompressionOptions.h>
#include <Aspose.PDF.Cpp/Optimization/ImageEncoding.h>

using namespace System;
using namespace Aspose::Pdf;

void UsingFlatedecodeCompression(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto options = MakeObject<Optimization::OptimizationOptions>();
    options->get_ImageCompressionOptions()->set_Encoding(Optimization::ImageEncoding::Flate);
    document->OptimizeResources(options);
    document->Save(outputFile);
}
```
