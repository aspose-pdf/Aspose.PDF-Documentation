---
title: Add PDF backgrounds in C++
linktitle: Add Backgrounds
type: docs
weight: 20
url: /cpp/add-backgrounds/
description: Add image or solid-color backgrounds to the first PDF page and configure image opacity using Aspose.PDF for C++.
lastmod: "2026-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create PDF Background Artifacts in C++
Abstract: Add BackgroundArtifact objects to the first page of an existing PDF. The examples use an image stream, set image opacity to 0.5, or apply a DarkKhaki background color.
---

Use `BackgroundArtifact` to add an image or solid color behind page content. All three examples modify page 1. Keep the image stream alive until the document is saved.

The input PDF must contain at least one page. Configure the Aspose.PDF for C++ SDK and use a writable output path for examples that save a PDF.

## Add a background image

Open the image as a stream and use it as the background of the first page.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Open imageFile as a file stream.
1. Create a [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/backgroundartifact/).
1. Assign the stream with [set_BackgroundImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf/backgroundartifact/set_backgroundimage/).
1. Add the artifact to the first page with [ArtifactCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifactcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Artifacts/Artifact.h>
#include <Aspose.PDF.Cpp/Artifacts/ArtifactCollection.h>

using namespace System;
using namespace Aspose::Pdf;

#include <Aspose.PDF.Cpp/Artifacts/BackgroundArtifact.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>

void AddBackgroundImageToPdf(System::String inputFile, System::String imageFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto imageStream = System::IO::File::OpenRead(imageFile);
    auto artifact = MakeObject<BackgroundArtifact>();
    artifact->set_BackgroundImage(imageStream);
    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);
    document->Save(outputFile);
    imageStream->Close();
}
```

## Set background image opacity

Add the image background with an opacity of 0.5.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Open imageFile as a file stream and create a [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/backgroundartifact/).
1. Set its image with [set_BackgroundImage()](https://reference.aspose.com/pdf/cpp/aspose.pdf/backgroundartifact/set_backgroundimage/).
1. Set opacity to 0.5 with [Artifact::set_Opacity()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/set_opacity/).
1. Add the artifact to the first page with [ArtifactCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifactcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Artifacts/Artifact.h>
#include <Aspose.PDF.Cpp/Artifacts/ArtifactCollection.h>
#include <Aspose.PDF.Cpp/Artifacts/BackgroundArtifact.h>

#include <system/io/file.h>
#include <system/io/file_stream.h>

using namespace System;
using namespace Aspose::Pdf;

void AddBackgroundImageWithOpacityToPdf(System::String inputFile, System::String imageFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto imageStream = System::IO::File::OpenRead(imageFile);
    auto artifact = MakeObject<BackgroundArtifact>();
    artifact->set_BackgroundImage(imageStream);
    artifact->set_Opacity(0.5);
    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);
    document->Save(outputFile);
}
```

## Add a background color

Create a DarkKhaki background using a PDF Color directly.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/aspose.pdf/backgroundartifact/).
1. Set DarkKhaki through [set_BackgroundColor()](https://reference.aspose.com/pdf/cpp/aspose.pdf/backgroundartifact/set_backgroundcolor/) using a [Color](https://reference.aspose.com/pdf/cpp/aspose.pdf/color/).
1. Add the artifact to the first page with [ArtifactCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifactcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Artifacts/Artifact.h>
#include <Aspose.PDF.Cpp/Artifacts/ArtifactCollection.h>
#include <Aspose.PDF.Cpp/Artifacts/BackgroundArtifact.h>
#include <Aspose.PDF.Cpp/Color.h>

using namespace System;
using namespace Aspose::Pdf;

void AddBackgroundColorToPdf(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto artifact = MakeObject<BackgroundArtifact>();
    artifact->set_BackgroundColor(Color::get_DarkKhaki());
    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);
    document->Save(outputFile);
}
```

## Moved inspection and removal guides

<a id="remove-background-artifacts"></a>

See [Remove Backgrounds](/pdf/cpp/remove-backgrounds/) for this operation.

## Related artifact topics

- [Remove Backgrounds](/pdf/cpp/remove-backgrounds/)
- [Work with PDF Artifacts](/pdf/cpp/artifacts/)
