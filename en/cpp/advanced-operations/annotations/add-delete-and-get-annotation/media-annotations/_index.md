---
title: Media annotations in C++
linktitle: Media annotations
type: docs
weight: 40
url: /cpp/media-annotations/
description: Create and inspect PDF sound, screen, rich media, and 3D annotations and delete rich media annotations using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Embed Sound, Video, and 3D PDF Annotations in C++
Abstract: Create sound, screen, rich media, and 3D annotations with Aspose.PDF for C++. The examples also inspect multimedia annotation types and rectangles and delete rich media annotations, with details about external player assets and viewer support.
---

Use the following examples to create media annotation objects and inspect existing multimedia annotations. Playback and 3D interaction depend on the PDF viewer and its supported features.

The rich media example uses external Adobe SWF player and skin files. Set pathToAdobeApp to their location and supply the MP4 video and poster image in mediaDir. The example preserves the legacy player configuration from the source; creating the PDF does not verify playback.

The snippets retain the example namespaces and include files. They assume the Aspose.PDF for C++ SDK is configured. Functions that open an existing PDF generally use its first page; supply a PDF containing the expected text, annotations, or media resources. Coordinates are taken from the supplied fixtures and should be adjusted for other documents.

## Add a 3D annotation

Create a new PDF containing a 3D model with CAD lighting, solid rendering, and two named views: Top and Left.

1. Create a PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Load modelFile into [PDF3DContent](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/pdf3dcontent/) and create [PDF3DArtwork](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/pdf3dartwork/).
1. Configure lighting and rendering and add two [PDF3DView](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/pdf3dview/) objects using transformation matrices.
1. Create a [PDF3DAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/pdf3dannotation/) on a new page and set its border, default view, flags, and name.
1. Add it with [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Border.h>
#include <system/exceptions.h>
#include <system/io/path.h>
#include <Aspose.PDF.Cpp/DOM/Matrix3D.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationFlags.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/PDF3DAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/PDF3DArtwork.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/PDF3DContent.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/PDF3DLightingScheme.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/PDF3DRenderMode.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/PDF3DView.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/PDF3DViewArray.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Media {

    void Annotation3dAdd(System::String modelFile, System::String outputFile)
    {
        auto document = MakeObject<Document>();
        auto pdf3dContent = MakeObject<PDF3DContent>(modelFile);
        auto pdf3dArtwork = MakeObject<PDF3DArtwork>(document, pdf3dContent);
        pdf3dArtwork->set_LightingScheme(MakeObject<PDF3DLightingScheme>(LightingSchemeType::CAD));
        pdf3dArtwork->set_RenderMode(MakeObject<PDF3DRenderMode>(RenderModeType::Solid));

        auto topMatrix = MakeObject<Matrix3D>(
            1, 0, 0,
            0, -1, 0,
            0, 0, -1,
            0.10271, 0.08184, 0.273836);

        auto frontMatrix = MakeObject<Matrix3D>(
            0, -1, 0,
            0, 0, 1,
            -1, 0, 0,
            0.332652, 0.08184, 0.085273);

        pdf3dArtwork->get_ViewArray()->Add(MakeObject<PDF3DView>(document, topMatrix, 0.188563, u"Top"));
        pdf3dArtwork->get_ViewArray()->Add(MakeObject<PDF3DView>(document, frontMatrix, 0.188563, u"Left"));

        auto page = document->get_Pages()->Add();

        auto pdf3dAnnotation = MakeObject<PDF3DAnnotation>(
            page,
            MakeObject<Rectangle>(100, 500, 300, 700, true),
            pdf3dArtwork);

        pdf3dAnnotation->set_Border(MakeObject<Border>(pdf3dAnnotation));
        pdf3dAnnotation->SetDefaultViewIndex(1);
        pdf3dAnnotation->set_Flags(AnnotationFlags::NoZoom);
        pdf3dAnnotation->set_Name(System::IO::Path::GetFileName(modelFile));

        page->get_Annotations()->Add(pdf3dAnnotation);
        document->Save(outputFile);
    }

} // namespace WorkingWithAnnotations::Media
```

## Get multimedia annotations

Print the type name and rectangle of Screen, Sound, and RichMedia annotations on the first page. This filter does not include 3D annotations.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through [Page::get_Annotations()](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_annotations/).
1. Filter by Screen, Sound, or RichMedia using [AnnotationType](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationtype/).
1. Print each matching [Annotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotation/) type and rectangle.

```cpp
#include <iostream>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Media {

void MultimediaAnnotationsGet(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Screen
            || annotation->get_AnnotationType() == AnnotationType::Sound
            || annotation->get_AnnotationType() == AnnotationType::RichMedia) {
            const char* typeName = annotation->get_AnnotationType() == AnnotationType::Screen ? "Screen"
                : annotation->get_AnnotationType() == AnnotationType::Sound ? "Sound" : "RichMedia";
            std::cout << typeName << " [" << annotation->get_Rect()->ToString() << "]" << std::endl;
        }
    }
}

} // namespace WorkingWithAnnotations::Media
```

## Add a rich media annotation

Create a new page with an MP4 video annotation, a poster, and custom Adobe player and skin streams. Keep the streams alive through Save().

1. Create a PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [RichMediaAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/richmediaannotation/) on a new page.
1. Open the player, skin, poster, and video streams.
1. Set the custom player, Flash variables, skin data, poster, and video content through [RichMediaAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/richmediaannotation/).
1. Set video content and click activation, then call [Update()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/richmediaannotation/update/).
1. Add the annotation with [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <system/io/path.h>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/RichMediaAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Media {

    void RichMediaAnnotationsAdd(System::String mediaDir, System::String outputFile)
    {
        // Supply the Adobe multimedia player and skin files at this location.
        String pathToAdobeApp = u"C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins";
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();
        String videoName = u"file_example_MP4_480_1_5MG.mp4";
        String skinName = u"SkinOverAllNoFullNoCaption.swf";
        auto richMediaAnnotation = MakeObject<RichMediaAnnotation>(page, MakeObject<Rectangle>(100, 500, 300, 600, true));
        auto player = System::IO::File::OpenRead(System::IO::Path::Combine(pathToAdobeApp, u"Players\\Videoplayer.swf"));
        auto skin = System::IO::File::OpenRead(System::IO::Path::Combine(pathToAdobeApp, skinName));
        auto poster = System::IO::File::OpenRead(System::IO::Path::Combine(mediaDir, u"file_example_MP4_480_1_5MG_poster.jpg"));
        auto video = System::IO::File::OpenRead(System::IO::Path::Combine(mediaDir, videoName));
        richMediaAnnotation->set_CustomPlayer(player);
        richMediaAnnotation->set_CustomFlashVariables(u"source=" + videoName + u"&skin=" + skinName);
        richMediaAnnotation->AddCustomData(skinName, skin);
        richMediaAnnotation->SetPoster(poster);
        richMediaAnnotation->SetContent(videoName, video);
        richMediaAnnotation->set_Type(RichMediaAnnotation::ContentType::Video);
        richMediaAnnotation->set_ActivateOn(RichMediaAnnotation::ActivationEvent::Click);
        richMediaAnnotation->Update();
        page->get_Annotations()->Add(richMediaAnnotation);
        document->Save(outputFile);
    }

} // namespace WorkingWithAnnotations::Media
```

## Delete rich media annotations

Collect rich media annotations on the first page, then delete the collected objects. The collection is not modified during enumeration.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through the first page [Annotations](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_annotations/) collection and filter by [AnnotationType](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationtype/).
1. Collect the matching annotations before modifying the collection.
1. Delete each collected annotation with [AnnotationCollection::Delete()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/delete/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <vector>
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Annotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Media {

void RichMediaAnnotationsDelete(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);

    std::vector<SharedPtr<Annotation>> toDelete;
    for (auto& annotation : page->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::RichMedia) {
            toDelete.push_back(annotation);
        }
    }
    for (auto& annotation : toDelete) {
        page->get_Annotations()->Delete(annotation);
    }
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Media
```

## Add a screen annotation

Create a new one-page PDF and attach a screen annotation using the supplied media file path.

1. Create a PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Add a page through [PageCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf/pagecollection/add/).
1. Create a [ScreenAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/screenannotation/) with a rectangle and mediaFile.
1. Add it with [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/ScreenAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Media {

void ScreenAnnotationWithMediaAdd(System::String mediaFile, System::String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto screenAnnotation = MakeObject<ScreenAnnotation>(
            page,
            MakeObject<Rectangle>(170, 190, 470, 380, true),
            mediaFile);

    page->get_Annotations()->Add(screenAnnotation);
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Media
```

## Add a sound annotation

Load file_example_WAV_1MG.wav from the input PDF directory and add a blue sound annotation with a popup on page 1.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Locate the WAV file beside the input PDF.
1. Create a [SoundAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/soundannotation/) and set its title, subject, and color.
1. Attach a [PopupAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/popupannotation/).
1. Add the sound annotation with [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/exceptions.h>
#include <system/io/path.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Point.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Annotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/PopupAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/SoundAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

namespace WorkingWithAnnotationsExamples::Media {

void SoundAnnotationAdd(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);

    auto mediaFile = System::IO::Path::Combine(System::IO::Path::GetDirectoryName(inputFile), u"file_example_WAV_1MG.wav");

    auto soundAnnotation = MakeObject<SoundAnnotation>(
            page,
            MakeObject<Rectangle>(20, 700, 60, 740, true),
            mediaFile);

    soundAnnotation->set_Color(Color::get_Blue());
    soundAnnotation->set_Title(u"John Smith");
    soundAnnotation->set_Subject(u"Sound Annotation demo");

    soundAnnotation->set_Popup(MakeObject<PopupAnnotation>(
            page,
            MakeObject<Rectangle>(20, 700, 60, 740, true)));

    page->get_Annotations()->Add(soundAnnotation);
    document->Save(outputFile);
}

} // namespace WorkingWithAnnotations::Media
```
