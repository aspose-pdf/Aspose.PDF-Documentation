---
title: Extract annotation and special text in C++
linktitle: Annotations and Special Text
type: docs
weight: 40
url: /cpp/annotation-and-special-text/
description: Read highlighted text, stamp appearance text, and superscript or subscript flags from PDFs with Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Read highlighted text, stamp appearance text, and superscript or subscript flags from PDFs with Aspose.PDF for C++.

## Extract highlighted text

Read text marked by highlight annotations on page 1.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through the first page annotations.
1. Select Highlight annotations and cast them to [HighlightAnnotation](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/highlightannotation/).
1. Call [GetMarkedText()](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/highlightannotation/) and print the result.

Source example: `annotation.cpp`.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/HighlightAnnotation.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;

void ExtractHighlightedText(String inputFile) {
    auto document = MakeObject<Document>(inputFile);
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Highlight) {
            auto highlightAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::HighlightAnnotation>(annotation);
            System::Console::WriteLine(highlightAnnotation->GetMarkedText());
        }
    }
}
```

## Extract stamp appearance text

Read text from the normal appearance of stamp annotations on page 1.

This requires a suitable normal appearance containing extractable text; it does not perform OCR on image-only stamps.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through the first page annotations and select stamps.
1. Create a [TextAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textabsorber/).
1. Get the normal appearance entry N and cast it to an XForm.
1. Visit the appearance with the absorber and print its text.

Source example: `annotation-02.cpp`.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AppearanceDictionary.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/StampAnnotation.h>
#include <Aspose.PDF.Cpp/Text/TextAbsorber.h>
#include <Aspose.PDF.Cpp/XForm.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

void ExtractStampText(String inputFile) {
    auto document = MakeObject<Document>(inputFile);
    for (auto& annotation : document->get_Pages()->idx_get(1)->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Stamp) {
            auto textAbsorber = MakeObject<TextAbsorber>();
            auto ap = annotation->get_Appearance()->idx_get(u"N");
            textAbsorber->Visit(System::DynamicCast<XForm>(ap));
            System::Console::WriteLine(textAbsorber->get_Text());
        }
    }
}
```

## Extract page text including special text

Extract text fragments from a selected page and save their combined text.

Despite the function name ExtractSuperSubText, this example extracts all page text; it does not filter for superscript or subscript.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/).
1. Select pageNumber and call Accept() with the absorber.
1. Write the extracted text to the output file.

Source example: `annotation-03.cpp`.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>


using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

void ExtractSuperSubText(String inputFile, String outputFile, int pageNumber) {
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>();
    document->get_Pages()->idx_get(pageNumber)->Accept(absorber);
    System::IO::File::WriteAllText(outputFile, absorber->get_Text());
}
```

## Inspect superscript and subscript flags

Report text and formatting flags for every fragment on a selected page.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Process pageNumber with a [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/).
1. Iterate through the extracted fragments.
1. Read each fragment text and the Superscript and Subscript flags from its text state.
1. Write the details to the output file.

Source example: `annotation-04.cpp`.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextState.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Annotations;
using namespace Aspose::Pdf::Text;

void ExtractSuperSubDetails(String inputFile, String outputFile, int pageNumber) {
    auto document = MakeObject<Document>(inputFile);
    auto absorber = MakeObject<TextFragmentAbsorber>();
    document->get_Pages()->idx_get(pageNumber)->Accept(absorber);
    auto details = MakeObject<System::Text::StringBuilder>();
    for (auto& fragment : absorber->get_TextFragments()) {
        details->Append(u"Text: '")->Append(fragment->get_Text())
            ->Append(u"' | Superscript: ")->Append(fragment->get_TextState()->get_Superscript())
            ->Append(u" | Subscript: ")->Append(fragment->get_TextState()->get_Subscript())
            ->Append(System::Environment::get_NewLine());
    }
    System::IO::File::WriteAllText(outputFile, details->ToString());
}
```
