---
title: Manage PDF backgrounds in C++
linktitle: Adding backgrounds
type: docs
weight: 20
url: /cpp/add-backgrounds/
description: Add image backgrounds, set background opacity or color, and remove background artifacts from PDF files using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create and Remove PDF Background Artifacts in C++
Abstract: Use BackgroundArtifact to add an image or a solid color to a PDF page with Aspose.PDF for C++. The examples also set image opacity and remove background pagination artifacts from the first page.
---

Use BackgroundArtifact to add an image or a solid color to the first PDF page. Image examples accept an imageFile path and keep the image stream alive until the document is saved.

The input PDF must contain at least one page. Configure the Aspose.PDF for C++ SDK before using these functions.

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

## Remove background artifacts

Remove first-page artifacts whose type is Pagination and subtype is Background. The reverse iteration avoids skipping items after deletion.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Get the first page [Artifacts](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_artifacts/) collection.
1. Iterate backward from [ArtifactCollection::get_Count()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifactcollection/get_count/) to index 1.
1. Check [Artifact::get_Type()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/get_type/) for Pagination and [get_Subtype()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifact/get_subtype/) for Background.
1. Delete matches with [ArtifactCollection::Delete()](https://reference.aspose.com/pdf/cpp/aspose.pdf/artifactcollection/delete/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Artifacts/Artifact.h>
#include <Aspose.PDF.Cpp/Artifacts/ArtifactCollection.h>

using namespace System;
using namespace Aspose::Pdf;


void RemoveBackground(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto artifacts = document->get_Pages()->idx_get(1)->get_Artifacts();
    for (int i = artifacts->get_Count(); i >= 1; --i) {
        auto artifact = artifacts->idx_get(i);
        if (artifact->get_Type() == Artifact::ArtifactType::Pagination &&
            artifact->get_Subtype() == Artifact::ArtifactSubtype::Background) {
            artifacts->Delete(artifact);
        }
    }
    document->Save(outputFile);
}
```
