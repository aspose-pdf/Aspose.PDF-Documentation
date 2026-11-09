---
title: Extract PDF links in C++
linktitle: Extract Links
type: docs
weight: 30
url: /cpp/extract-links/
description: Read link annotation locations and extract web destination URIs from the first PDF page using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Read PDF Link Rectangles and Web Destinations in C++
Abstract: Inspect LinkAnnotation objects on the first page with Aspose.PDF for C++. One example prints link locations, while another filters GoToURIAction objects and prints their web destinations.
---

These read-only examples inspect the first page and print results. They do not scan all pages or save a modified PDF.

Configure the Aspose.PDF for C++ SDK and create the output directory before running examples that save a file. The snippets retain the source includes, function parameters, coordinates, and action settings, with the project runner header omitted.

## Read link annotation locations

Inspect page 1 and print each link annotation's page index and rectangle. This example does not extract the visible text of the link.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through the first page [Annotations](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_annotations/).
1. Filter by [AnnotationType](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/annotationtype/) and cast matching objects to [LinkAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/linkannotation/).
1. Print the page index and rectangle from each [LinkAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/linkannotation/).

```cpp
#include <iostream>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Annotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/LinkAnnotation.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;

// Port of links/ExtractExamples.extractLinkAnnotation.
void ExtractLinkAnnotation(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (const auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Link && System::DynamicCast_noexcept<LinkAnnotation>(annotation)) {
            auto linkAnnotation = System::DynamicCast<LinkAnnotation>(annotation);
            std::cout << "Page: " << linkAnnotation->get_PageIndex()
            << ", location: " << linkAnnotation->get_Rect()->ToString() << std::endl;
        }
    }
}
```

## Extract web destinations

Inspect page 1 links and print only those whose action is GoToURIAction, including each URI and page index.

1. Open the input PDF with [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Filter the first page [Annotations](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/get_annotations/) for [LinkAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/linkannotation/) objects.
1. Check and cast the action to [GoToURIAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/gotouriaction/).
1. Print the URI from [get_URI()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/gotouriaction/get_uri/) and the link page index.

```cpp
#include <iostream>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Annotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/LinkAnnotation.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/GoToURIAction.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;

// Port of links/ExtractExamples.extractHyperlinks.
void ExtractHyperlinks(System::String inputFile)
{
    auto document = MakeObject<Document>(inputFile);
    for (const auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Link && System::DynamicCast_noexcept<LinkAnnotation>(annotation)) {
            auto linkAnnotation = System::DynamicCast<LinkAnnotation>(annotation);
            if (System::DynamicCast_noexcept<GoToURIAction>(linkAnnotation->get_Action())) {
                auto action = System::DynamicCast<GoToURIAction>(linkAnnotation->get_Action());
                std::cout << "Page " << linkAnnotation->get_PageIndex() << ", URI:" << action->get_URI() << std::endl;
            }
        }
    }
}
```
