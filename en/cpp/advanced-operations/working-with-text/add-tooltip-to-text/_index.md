---
title: Add Tooltips to PDF Text in C++
linktitle: PDF Tooltip
type: docs
weight: 20
url: /cpp/pdf-tooltip/
description: Add tooltips to searched PDF text and show a hidden text field on hover using C++ form fields and actions.
lastmod: "2026-11-26"
sitemap:
    changefreq: monthly
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create PDF text tooltips and hover fields in C++
Abstract: Use text search results to position interactive form fields over PDF text. The examples set button tooltips and attach show and hide actions to a read-only text field.
---

Create PDF text tooltips with form fields positioned over matching text. These examples generate a one-page PDF, save and reopen it to obtain text bounds, and then add the interactive fields. Tooltip and hover behavior depends on the PDF viewer supporting form fields and actions.

## Before you begin

Configure a C++ project with Aspose.PDF for C++ and apply your license if available. The snippets are independent functions adapted from the supplied examples: the example-project header and namespace qualification have been removed, while the PDF operations are preserved. Include the headers shown with each function and call it from your application. Helper functions, where needed, are included in the same block.

Pass the destination PDF path as `outputFile`. Most functions create their own text and do not use `inputFile`; exceptions that read text, images, or fonts are described below. Ensure the fonts named by each example are available.

The main APIs used here are [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/), [ButtonField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/buttonfield/), [TextBoxField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/textboxfield/), [HideAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/hideaction/).

## Text tooltips

### Add tooltips to searched text

Search the generated text on all pages and create ButtonField objects over the matching rectangles. Set AlternateName to the short or long tooltip text and add the fields to page 1, which is the only page created by this example.

1. Create and save a one-page PDF containing the phrases to search.
1. Reopen the PDF and use [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/) to find both phrases across the document.
1. Create a [ButtonField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/buttonfield/) over each match, set its `AlternateName` to the tooltip text, and add the fields to page 1.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/ButtonField.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Forms;

void AddToolTipToSearchedText(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    document->get_Pages()->Add()->get_Paragraphs()->Add(
        MakeObject<TextFragment>(String(u"Move the mouse cursor here to display a tooltip")));
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(
        MakeObject<TextFragment>(String(u"Move the mouse cursor here to display a very long tooltip")));
    document->Save(outputFile);
    document->Dispose();

    document = MakeObject<Document>(outputFile);
    auto absorber =
        MakeObject<TextFragmentAbsorber>(String(u"Move the mouse cursor here to display a tooltip"));
    document->get_Pages()->Accept(absorber);

    for (auto fragment : absorber->get_TextFragments())
    {
        auto field = MakeObject<ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        field->set_AlternateName(String(u"Tooltip for text."));
        document->get_Form()->Add(field, 1);
    }

    absorber = MakeObject<TextFragmentAbsorber>(
        String(u"Move the mouse cursor here to display a very long tooltip"));
    document->get_Pages()->Accept(absorber);

    for (auto fragment : absorber->get_TextFragments())
    {
        auto field = MakeObject<ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
        field->set_AlternateName(String(u"Lorem ipsum dolor sit amet, consectetur adipiscing elit,") +
                                 String(u" sed do eiusmod tempor incididunt ut labore et dolore magna") +
                                 String(u" aliqua. Ut enim ad minim veniam, quis nostrud exercitation") +
                                 String(u" ullamco laboris nisi ut aliquip ex ea commodo consequat.") +
                                 String(u" Duis aute irure dolor in reprehenderit in voluptate velit") +
                                 String(u" esse cillum dolore eu fugiat nulla pariatur. Excepteur sint") +
                                 String(u" occaecat cupidatat non proident, sunt in culpa qui officia") +
                                 String(u" deserunt mollit anim id est laborum."));
        document->get_Form()->Add(field, 1);
    }

    document->Save(outputFile);
    document->Dispose();
}
```

### Show a hidden text block on hover

Search for the generated phrase and use its first match as the trigger rectangle. Add a hidden, read-only TextBoxField on page 1 at (100, 700, 220, 740), then attach HideAction objects to the button OnEnter and OnExit events to show and hide the field.

1. Create and save a one-page PDF containing the trigger phrase.
1. Reopen the PDF, search for the phrase with [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/), and use the first match as the trigger rectangle.
1. Add a hidden, read-only [TextBoxField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/textboxfield/) to page 1 and place a [ButtonField](https://reference.aspose.com/pdf/cpp/aspose.pdf.forms/buttonfield/) over the match.
1. Attach [HideAction](https://reference.aspose.com/pdf/cpp/aspose.pdf.annotations/hideaction/) objects to the button’s `OnEnter` and `OnExit` events to show and hide the text box.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <stdexcept>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationActionCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationFlags.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Border.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Characteristics.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/DefaultAppearance.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/ButtonField.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/Form.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Forms/TextBoxField.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/HideAction.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Rectangle.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <drawing/color.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;
using Aspose::Pdf::Color;

void CreateHiddenTextBlock(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    document->get_Pages()->Add()->get_Paragraphs()->Add(
        MakeObject<TextFragment>(String(u"Move the mouse cursor here to display floating text")));
    document->Save(outputFile);

    document->Dispose();

    document = MakeObject<Document>(outputFile);
    auto absorber =
        MakeObject<TextFragmentAbsorber>(String(u"Move the mouse cursor here to display floating text"));
    document->get_Pages()->Accept(absorber);
    if (absorber->get_TextFragments()->get_Count() == 0)
        throw std::runtime_error("No matching text fragments found");
    auto fragment = absorber->get_TextFragments()->idx_get(1);

    auto floatingField = MakeObject<TextBoxField>(
        fragment->get_Page(), MakeObject<Aspose::Pdf::Rectangle>(100.0, 700.0, 220.0, 740.0, false));
    floatingField->set_Value(String(u"This is the \"floating text field\"."));
    floatingField->set_ReadOnly(true);
    floatingField->set_Flags(floatingField->get_Flags() | AnnotationFlags::Hidden);
    floatingField->set_PartialName(String(u"FloatingField_1"));
    floatingField->set_DefaultAppearance(
        MakeObject<DefaultAppearance>(String(u"Helv"), 10, System::Drawing::Color::get_Blue()));
    floatingField->get_Characteristics()->set_Background(System::Drawing::Color::get_Cyan());
    floatingField->get_Characteristics()->set_Border(System::Drawing::Color::get_Blue());
    floatingField->set_Border(MakeObject<Border>(floatingField));
    floatingField->get_Border()->set_Width(1);
    floatingField->set_Multiline(true);

    document->get_Form()->Add(floatingField, 1);

    auto buttonField = MakeObject<ButtonField>(fragment->get_Page(), fragment->get_Rectangle());
    buttonField->get_Actions()->set_OnEnter(MakeObject<HideAction>(floatingField, false));
    buttonField->get_Actions()->set_OnExit(MakeObject<HideAction>(floatingField));

    document->get_Form()->Add(buttonField, 1);
    document->Save(outputFile);
    document->Dispose();
}
```

## Related text topics

- [Working with text](/pdf/cpp/working-with-text/)
- [Add Text to PDF in C++](/pdf/cpp/add-text-to-pdf-file/)
- [Use FloatingBox for PDF Layout in C++](/pdf/cpp/floating-box/)
- [Replace Text in PDF with C++](/pdf/cpp/replace-text-in-pdf/)
- [Rotate PDF Text in C++](/pdf/cpp/rotate-text-inside-pdf/)
- [Search and Extract PDF Text in C++](/pdf/cpp/search-and-get-text-from-pdf/)
- [Format PDF Text in C++](/pdf/cpp/text-formatting-inside-pdf/)

For additional types and members, see the [Aspose.PDF for C++ API reference](https://reference.aspose.com/pdf/cpp/).
