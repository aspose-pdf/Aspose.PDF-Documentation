---
title: Work with PDF layers in C++
linktitle: Work with PDF layers
type: docs
weight: 70
url: /cpp/working-with-layers/
description: Inspect the supplied layer-creation example and lock, export, flatten, or merge layers on the first PDF page with Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Lock, Export, Flatten, and Merge PDF Layers in C++
Abstract: Learn how to inspect and manage layers on the first PDF page with Aspose.PDF for C++. The examples demonstrate locking, exporting, flattening, and merging layers, along with a layer-creation example.
---

Inspect the supplied layer-creation example and lock, export, flatten, or merge layers on the first PDF page with Aspose.PDF for C++.

## Lock the first layer

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Check that page 1 and its layers exist.
1. Select the first [Layer](https://reference.aspose.com/pdf/cpp/aspose.pdf/layer/) at index 0 and call [Lock()](https://reference.aspose.com/pdf/cpp/aspose.pdf/layer/).
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/console.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Layers/Layer.h>

using namespace System;
using namespace Aspose::Pdf;

void LockLayer(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    if (document->get_Pages()->get_Count() == 0) {
        Console::WriteLine(u"No pages found in the document.");
        return;
    }
    auto page = document->get_Pages()->idx_get(1);
    auto layers = page->get_Layers();
    if (layers == nullptr || layers->get_Count() == 0) {
        Console::WriteLine(u"No layers found in the document.");
        return;
    }

    layers->idx_get(0)->Lock();
    document->Save(outputFile);
    Console::WriteLine(u"Layer locked successfully. File saved at {0}", outputFile);
}
```

## Export layers to separate files

Only layers on the first page are exported. When no extension is supplied, the example uses .pdf.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Check that page 1 and its layers exist.
1. Build numbered output names from the supplied output path.
1. Call [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/layer/) on each [Layer](https://reference.aspose.com/pdf/cpp/aspose.pdf/layer/) using its output filename.

```cpp

#include <system/console.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Layers/Layer.h>

using namespace System;
using namespace Aspose::Pdf;

void ExtractLayers(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    if (document->get_Pages()->get_Count() == 0) {
        Console::WriteLine(u"No layers found in the document.");
        return;
    }
    auto page = document->get_Pages()->idx_get(1);
    auto layers = page->get_Layers();
    if (layers == nullptr || layers->get_Count() == 0) {
        Console::WriteLine(u"No layers found in the document.");
        return;
    }

    const auto directory = System::IO::Path::GetDirectoryName(outputFile);
    const auto root = System::IO::Path::GetFileNameWithoutExtension(outputFile);
    auto extension = System::IO::Path::GetExtension(outputFile);
    if (extension.IsEmpty()) {
        extension = u".pdf";
    }
    int index = 1;
    for (auto layer : layers) {
        auto layerOutputFile = System::IO::Path::Combine(directory,
            String::Format(u"{0}{1}{2}", root, index, extension));
        layer->Save(layerOutputFile);
        Console::WriteLine(u"Layer {0} saved to {1}", index++, layerOutputFile);
    }
}
```

## Export the first layer to a stream

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Check that page 1 and its layers exist.
1. Create a writable file stream.
1. Call [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/layer/) on the first [Layer](https://reference.aspose.com/pdf/cpp/aspose.pdf/layer/) with the stream.
1. Close the stream.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Layers/Layer.h>

using namespace System;
using namespace Aspose::Pdf;

void ExtractLayersStream(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    if (document->get_Pages()->get_Count() == 0) {
        Console::WriteLine(u"No layers found in the document.");
        return;
    }
    auto page = document->get_Pages()->idx_get(1);
    auto layers = page->get_Layers();
    if (layers == nullptr || layers->get_Count() == 0) {
        Console::WriteLine(u"No layers found in the document.");
        return;
    }

    auto stream = MakeObject<System::IO::FileStream>(
        outputFile, System::IO::FileMode::Create, System::IO::FileAccess::Write);
    layers->idx_get(0)->Save(stream);
    stream->Close();
    Console::WriteLine(u"Layer extracted to stream: {0}", outputFile);
}
```

## Flatten layers on the first page

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Check that page 1 and its layers exist.
1. Copy the layer collection to an array.
1. Call [Flatten(true)](https://reference.aspose.com/pdf/cpp/aspose.pdf/layer/) on every [Layer](https://reference.aspose.com/pdf/cpp/aspose.pdf/layer/) in the snapshot.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Layers/Layer.h>

using namespace System;
using namespace Aspose::Pdf;

void FlattenLayers(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    if (document->get_Pages()->get_Count() == 0) {
        Console::WriteLine(u"No layers found in the document.");
        return;
    }
    auto page = document->get_Pages()->idx_get(1);
    auto layers = page->get_Layers();
    if (layers == nullptr || layers->get_Count() == 0) {
        Console::WriteLine(u"No layers found in the document.");
        return;
    }

    // Copy the layer list because flattening can change the page's layers.
    auto snapshot = layers->ToArray();
    for (auto layer : snapshot) {
        layer->Flatten(true);
    }
    document->Save(outputFile);
    Console::WriteLine(u"Layers flattened successfully. File saved at {0}", outputFile);
}
```

## Merge layers on the first page

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Check that page 1 and its layers exist.
1. Call [MergeLayers()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) on the [Page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) with the name LayerNew.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Layers/Layer.h>

using namespace System;
using namespace Aspose::Pdf;

void MergeLayers(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    if (document->get_Pages()->get_Count() == 0) {
        Console::WriteLine(u"No layers found in the document.");
        return;
    }
    auto page = document->get_Pages()->idx_get(1);
    auto layers = page->get_Layers();
    if (layers == nullptr || layers->get_Count() == 0) {
        Console::WriteLine(u"No layers found in the document.");
        return;
    }

    page->MergeLayers(u"LayerNew");
    document->Save(outputFile);
    Console::WriteLine(u"Layers merged successfully. File saved at {0}", outputFile);
}
```
