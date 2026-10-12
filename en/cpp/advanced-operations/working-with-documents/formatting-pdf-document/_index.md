---
title: Format PDF documents in C++
linktitle: Format PDF documents
type: docs
weight: 20
url: /cpp/formatting-pdf-document/
description: Inspect and configure PDF viewer preferences, font embedding, font subsets, and opening zoom with Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Configure PDF Viewer Preferences, Fonts, and Opening Zoom in C++
Abstract: Learn how to read and configure PDF viewer preferences with Aspose.PDF for C++. The examples also cover font embedding, font subsets, default fonts, and document opening zoom.
---

Inspect and configure PDF viewer preferences, font embedding, font subsets, and opening zoom with Aspose.PDF for C++.

## Read viewer preferences

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Read the window, direction, page layout, and page mode properties from [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Print the property values.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/DOM/PageMode.h>
#include <Aspose.PDF.Cpp/PageLayout.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace System::Diagnostics;

void GetDocumentWindow(String inputFile) {
    auto document = MakeObject<Document>(inputFile);
    System::Console::WriteLine(u"CenterWindow: {0}", document->get_CenterWindow());
    System::Console::WriteLine(u"Direction: {0}", document->get_Direction());
    System::Console::WriteLine(u"DisplayDocTitle: {0}", document->get_DisplayDocTitle());
    System::Console::WriteLine(u"FitWindow: {0}", document->get_FitWindow());
    System::Console::WriteLine(u"HideMenuBar: {0}", document->get_HideMenubar());
    System::Console::WriteLine(u"HideToolBar: {0}", document->get_HideToolBar());
    System::Console::WriteLine(u"HideWindowUI: {0}", document->get_HideWindowUI());
    System::Console::WriteLine(u"NonFullScreenPageMode: {0}", document->get_NonFullScreenPageMode());
    System::Console::WriteLine(u"PageLayout: {0}", document->get_PageLayout());
    System::Console::WriteLine(u"PageMode: {0}", document->get_PageMode());
}
```

## Set viewer preferences

PDF viewers decide how to apply these display preferences.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Set the window and interface preferences on [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Select right-to-left direction, TwoColumnLeft layout, and UseThumbs page mode.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/DOM/PageMode.h>
#include <Aspose.PDF.Cpp/PageLayout.h>
#include <Aspose.PDF.Cpp/Direction.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace System::Diagnostics;

void SetDocumentWindow(String inputFile, String outputFile) {
    auto document = MakeObject<Document>(inputFile);
    document->set_CenterWindow(true);
    document->set_Direction(Direction::R2L);
    document->set_DisplayDocTitle(true);
    document->set_FitWindow(true);
    document->set_HideMenubar(true);
    document->set_HideToolBar(true);
    document->set_HideWindowUI(true);
    document->set_NonFullScreenPageMode(PageMode::UseOC);
    document->set_PageLayout(PageLayout::TwoColumnLeft);
    document->set_PageMode(PageMode::UseThumbs);
    document->Save(outputFile);
}
```

## Embed fonts in an existing PDF

Make the necessary fonts available in the execution environment.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Enable EmbedStandardFonts on [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through page font resources and set IsEmbedded on each unembedded [Font](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/font/).
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace System::Diagnostics;

void EmbeddedFonts(String inputFile, String outputFile) {
    auto document = MakeObject<Document>(inputFile);
    document->set_EmbedStandardFonts(true);
    for (auto& page : document->get_Pages()) {
        for (auto& pageFont : page->get_Resources()->get_Fonts()) {
            if (!pageFont->get_IsEmbedded()) {
                pageFont->set_IsEmbedded(true);
            }
        }
    }
    document->Save(outputFile);
}
```

## Embed a font in a new PDF

1. Create a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) and add a page.
1. Find Arial with [FontRepository](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/fontrepository/) and set IsEmbedded on the [Font](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/font/).
1. Assign the font to a text state and apply it to a text segment.
1. Add the segment to a [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/) and add the fragment to the page.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextSegment.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontRepository.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace System::Diagnostics;

void EmbeddedFontsInNewDocument(String outputFile) {
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    auto fragment = MakeObject<TextFragment>(u"");
    auto segment = MakeObject<TextSegment>(u" This is a sample text using Custom font.");
    auto textState = MakeObject<TextState>();
    auto font = FontRepository::FindFont(u"Arial");
    font->set_IsEmbedded(true);
    textState->set_Font(font);
    segment->set_TextState(textState);
    fragment->get_Segments()->Add(segment);
    page->get_Paragraphs()->Add(fragment);
    document->Save(outputFile);
}
```

## Set a default font for saving

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [PdfSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/pdfsaveoptions/) and set DefaultFontName to Arial.
1. Call [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/) with the output path and the save options.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PdfSaveOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace System::Diagnostics;

void SetDefaultFont(String inputFile, String outputFile) {
    auto document = MakeObject<Document>(inputFile);
    auto saveOptions = MakeObject<PdfSaveOptions>();
    saveOptions->set_DefaultFontName(u"Arial");
    document->Save(outputFile, saveOptions);
}
```

## List document fonts

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Retrieve all fonts through the document font utilities.
1. Read FontName from each [Font](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/font/) and print it.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace System::Diagnostics;

void GetAllFonts(String inputFile) {
    auto document = MakeObject<Document>(inputFile);
    for (auto& font : document->get_FontUtilities()->GetAllFonts()) {
        System::Console::WriteLine(font->get_FontName());
    }
}
```

## Subset embedded fonts

The alternative SubsetAllFonts call remains commented out in the source.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Call SubsetFonts() through the document font utilities with SubsetEmbeddedFontsOnly.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontCollection.h>
#include <Aspose.PDF.Cpp/CommonData/Text/Fonts/Utilities/FontSubsetStrategy.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace System::Diagnostics;

void ImproveFontsEmbedding(String inputFile, String outputFile) {
    auto document = MakeObject<Document>(inputFile);
    //document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetAllFonts);
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetEmbeddedFontsOnly);
    document->Save(outputFile);

}
```

## Set the opening zoom

The example sets a 50% opening zoom and replaces the existing open action.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Check that the document has at least one page.
1. Create an [XYZExplicitDestination](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/xyzexplicitdestination/) for page 1 with zoom 0.5.
1. Wrap the destination in a [GoToAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/gotoaction/) and assign it as the document OpenAction.
1. Save the result with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontCollection.h>
#include <Aspose.PDF.Cpp/CommonData/Text/Fonts/Utilities/FontSubsetStrategy.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/GoToAction.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/XYZExplicitDestination.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void SetZoomFactor(String inputFile, String outputFile) {
    auto document = MakeObject<Document>(inputFile);
    if (document->get_Pages()->get_Count() == 0) {
        throw System::InvalidOperationException(u"Cannot set an opening page on an empty document.");
    }
    auto action = MakeObject<GoToAction>(MakeObject<XYZExplicitDestination>(1, 0.0, 0.0, 0.5));
    document->set_OpenAction(action);
    document->Save(outputFile);
}
```

## Read the opening zoom

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Cast OpenAction to [GoToAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/gotoaction/).
1. Cast its destination to [XYZExplicitDestination](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/xyzexplicitdestination/).
1. Print Zoom when available, or print that zoom is not set.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/Text/Font.h>
#include <Aspose.PDF.Cpp/Text/FontCollection.h>
#include <Aspose.PDF.Cpp/CommonData/Text/Fonts/Utilities/FontSubsetStrategy.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/GoToAction.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/XYZExplicitDestination.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void GetZoomFactor(String inputFile) {
    auto document = MakeObject<Document>(inputFile);
    auto action = System::DynamicCast<GoToAction>(document->get_OpenAction());
    if (action == nullptr) {
        System::Console::WriteLine(u"Zoom: not set");
        return;
    }
    if (action != nullptr) {
        auto destination = System::DynamicCast<XYZExplicitDestination>(action->get_Destination());
        if (destination != nullptr) {
            System::Console::WriteLine(u"Zoom: {0}", destination->get_Zoom());
        }
        else {
            System::Console::WriteLine(u"Zoom: not set");
        }
    }
}
```
