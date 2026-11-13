---
title: Create PDF links in C++
linktitle: Create Links
type: docs
weight: 10
url: /cpp/create-links/
description: Create internal page links, remote PDF links, web links, and file launch links using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add PDF Links with Page, URI, and Launch Actions in C++
Abstract: Create LinkAnnotation objects and assign GoToAction, GoToRemoteAction, GoToURIAction, or LaunchAction with Aspose.PDF for C++. The examples place links on the first page and configure colors and selected border styles.
---

Each example creates a link annotation on page 1. The input PDF must contain at least one page. The internal link targets page 4 when available and otherwise the last page; external targets and URLs are preserved from the supplied source.

Configure the Aspose.PDF for C++ SDK and create the output directory before running examples that save a file. The snippets retain the source includes, function parameters, coordinates, and action settings, with the project runner header omitted.

## Create an internal page link

Add a green link on page 1 with a dashed border of width 5. Its destination is page 4 when available, otherwise the last page.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [LinkAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/linkannotation/) on page 1 with the sample rectangle.
1. Configure its [Border](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/border/), [Dash](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/dash/), and color.
1. Assign a [GoToAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/gotoaction/) targeting page 4 or the last available page.
1. Add it with [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Annotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Border.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Dash.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/LinkAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/GoToAction.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;

void CreateLinkAnnotationGoToAction(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);

    auto link = MakeObject<LinkAnnotation>(page, MakeObject<Rectangle>(10, 580, 120, 600, true));
    auto border = MakeObject<Border>(link);
    border->set_Width(5);
    border->set_Dash(MakeObject<Dash>(1, 1));
    link->set_Border(border);
    link->set_Color(Color::get_Green());
    if (document->get_Pages()->get_Count() >= 4) {
        link->set_Action(MakeObject<GoToAction>(document->get_Pages()->idx_get(4)));
    } else {
        link->set_Action(MakeObject<GoToAction>(document->get_Pages()->idx_get(document->get_Pages()->get_Count())));
    }
    page->get_Annotations()->Add(link);
    document->Save(outputFile);
}
```

## Create a remote PDF link

Create a green link whose GoToRemoteAction targets page 1 of the file named by inputFile. The source intentionally reuses the input path as the external target.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [LinkAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/linkannotation/) on page 1.
1. Set its color and assign a [GoToRemoteAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/gotoremoteaction/) using inputFile and page 1.
1. Add it with [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Annotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/LinkAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/GoToRemoteAction.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;

void CreateLinkAnnotationGoToRemoteAction(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);

    auto link = MakeObject<LinkAnnotation>(page, MakeObject<Rectangle>(10, 580, 120, 600, true));
    link->set_Color(Color::get_Green());
    link->set_Action(MakeObject<GoToRemoteAction>(inputFile, 1));
    page->get_Annotations()->Add(link);
    document->Save(outputFile);
}
```

## Create a web link

Add a green link on page 1 targeting https://docs.aspose.com/pdf/cpp/. The source URL is preserved.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [LinkAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/linkannotation/) with the sample rectangle.
1. Assign a [GoToURIAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/gotouriaction/) with the source URL.
1. Add it through [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Annotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/LinkAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/GoToURIAction.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;

void CreateLinkAnnotationGoToUriAction(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);

    auto link = MakeObject<LinkAnnotation>(page, MakeObject<Rectangle>(10, 580, 120, 600, true));
    link->set_Color(Color::get_Green());
    link->set_Action(MakeObject<GoToURIAction>(u"https://docs.aspose.com/pdf/python"));
    page->get_Annotations()->Add(link);
    document->Save(outputFile);
}
```

## Create a file launch link

Add a green dashed link on page 1 using LaunchAction with inputFile as the launch target. Activation depends on the PDF viewer.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [LinkAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/linkannotation/) and configure its [Border](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/border/) and color.
1. Assign a [LaunchAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/launchaction/) with the document and input file path.
1. Add the link with [AnnotationCollection::Add()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationcollection/add/).
1. Save the result with [Document::Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Annotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Border.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Dash.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/LinkAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/LaunchAction.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;

void CreateLinkAnnotationLaunchAction(System::String inputFile, System::String outputFile)
{
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);

    auto link = MakeObject<LinkAnnotation>(page, MakeObject<Rectangle>(10, 580, 120, 600, true));
    auto border = MakeObject<Border>(link);
    border->set_Width(5);
    border->set_Dash(MakeObject<Dash>(1, 1));
    link->set_Border(border);
    link->set_Color(Color::get_Green());
    link->set_Action(MakeObject<LaunchAction>(document, inputFile));
    page->get_Annotations()->Add(link);
    document->Save(outputFile);
}
```
