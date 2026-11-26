---
title: Use FloatingBox for PDF Layout in C++
linktitle: Using FloatingBox
type: docs
weight: 30
url: /cpp/floating-box/
description: Create FloatingBox containers with borders, columns, background colors, offsets, and alignment in PDF documents using C++.
lastmod: "2026-11-23"
sitemap:
    changefreq: monthly
    priority: 0.7
TechArticle: true
AlternativeHeadline: Build floating text containers and column layouts in C++
Abstract: Place text inside FloatingBox containers with Aspose.PDF for C++. Configure borders, column widths and spacing, background colors, absolute positioning, and horizontal and vertical alignment.
---

A FloatingBox groups paragraphs inside a configurable container. Use it for bordered text blocks, column layouts, backgrounds, and positioned page content. Each example below creates a new PDF document.

## Before you begin

Configure a C++ project with Aspose.PDF for C++ and apply your license if available. The snippets are independent functions adapted from the supplied examples: the example-project header and namespace qualification have been removed, while the PDF operations are preserved. Include the headers shown with each function and call it from your application. Helper functions, where needed, are included in the same block.

Pass the destination PDF path as `outputFile`. Most functions create their own text and do not use `inputFile`; exceptions that read text, images, or fonts are described below. Ensure the fonts named by each example are available.

The main APIs used here are [FloatingBox](https://reference.aspose.com/pdf/cpp/aspose.pdf/floatingbox/), [ColumnInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/columninfo/), [BorderInfo](https://reference.aspose.com/pdf/cpp/aspose.pdf/borderinfo/), [TextFragment](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragment/).

## Basic FloatingBox usage

### Create a bordered text container

Create a 400 by 30 point FloatingBox with a dark green border, disable repetition, and add a text fragment before adding the box to page paragraphs.

1. Create a page and a 400-by-30-point [FloatingBox](https://reference.aspose.com/pdf/cpp/aspose.pdf/floatingbox/) with a dark green border.
1. Disable box repetition, add a text fragment to the box, and add the box to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/FloatingBox.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void CreateAndAddFloatingBox(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto box = MakeObject<FloatingBox>(400, 30);
    box->set_Border(MakeObject<BorderInfo>(BorderSide::All, 1.5f, Color::get_DarkGreen()));
    box->set_IsNeedRepeating(false);
    String phrase = String(u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, "
                           u"sollicitudin ac mauris vel, suscipit pellentesque nisi.");
    box->get_Paragraphs()->Add(MakeObject<TextFragment>(phrase));

    page->get_Paragraphs()->Add(box);
    document->Save(outputFile);
}
```

## Multi-column support

### Flow text into three columns

Calculate column widths from the page width, margins, and 10-point gaps. Configure three columns on a repeating FloatingBox and add ten copies of the supplied paragraph.

1. Create a page and calculate column widths from the page width, margins, and 10-point gaps.
1. Configure a repeating [FloatingBox](https://reference.aspose.com/pdf/cpp/aspose.pdf/floatingbox/) with three columns and the calculated widths and spacing.
1. Add ten copies of the paragraph to the box and add the box to the page.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/ColumnInfo.h>
#include <Aspose.PDF.Cpp/Generator/FloatingBox.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void MultiColumnLayout(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    page->get_PageInfo()->set_Margin(MakeObject<MarginInfo>(36, 18, 36, 18));

    int columnCount = 3;
    int spacing = 10;
    double width = page->get_PageInfo()->get_Width() - page->get_PageInfo()->get_Margin()->get_Left() -
                   page->get_PageInfo()->get_Margin()->get_Right() - (columnCount - 1) * spacing;
    double columnWidth = width / 3;

    auto box = MakeObject<FloatingBox>();
    box->set_IsNeedRepeating(true);
    box->get_ColumnInfo()->set_ColumnWidths(String::Format(u"{0} {0} {0}", columnWidth));
    box->get_ColumnInfo()->set_ColumnSpacing(String::Format(u"{0}", spacing));
    box->get_ColumnInfo()->set_ColumnCount(columnCount);

    String phrase = String(u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, "
                           u"sollicitudin ac mauris vel, suscipit pellentesque nisi.");
    for (int i = 0; i < 10; i++)
    {
        box->get_Paragraphs()->Add(MakeObject<TextFragment>(phrase));
    }

    page->get_Paragraphs()->Add(box);
    document->Save(outputFile);
}
```

### Start each paragraph in a column

Use the same three-column setup and set IsFirstParagraphInColumn on each added fragment to force a column start.

1. Create a page and configure a repeating [FloatingBox](https://reference.aspose.com/pdf/cpp/aspose.pdf/floatingbox/) with three columns separated by 10-point gaps.
1. Enable [IsFirstParagraphInColumn](https://reference.aspose.com/pdf/cpp/aspose.pdf/baseparagraph/) on each fragment before adding it to the box.
1. Add the box to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/ColumnInfo.h>
#include <Aspose.PDF.Cpp/Generator/FloatingBox.h>
#include <Aspose.PDF.Cpp/Generator/MarginInfo.h>
#include <Aspose.PDF.Cpp/Generator/PageInfo.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void MultiColumnLayout2(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();
    page->get_PageInfo()->set_Margin(MakeObject<MarginInfo>(36, 18, 36, 18));

    int columnCount = 3;
    int spacing = 10;
    double width = page->get_PageInfo()->get_Width() - page->get_PageInfo()->get_Margin()->get_Left() -
                   page->get_PageInfo()->get_Margin()->get_Right() - (columnCount - 1) * spacing;
    double columnWidth = width / 3;

    auto box = MakeObject<FloatingBox>();
    box->set_IsNeedRepeating(true);
    box->get_ColumnInfo()->set_ColumnWidths(String::Format(u"{0}", columnWidth) + String(u" ") +
                                            String::Format(u"{0}", columnWidth) + String(u" ") +
                                            columnWidth);
    box->get_ColumnInfo()->set_ColumnSpacing(String::Format(u"{0}", spacing));
    box->get_ColumnInfo()->set_ColumnCount(3);

    String phrase = String(u"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, "
                           u"sollicitudin ac mauris vel, suscipit pellentesque nisi.");
    for (int i = 0; i < 10; i++)
    {
        auto text = MakeObject<TextFragment>(phrase);
        text->set_IsFirstParagraphInColumn(true);
        box->get_Paragraphs()->Add(text);
    }

    page->get_Paragraphs()->Add(box);
    document->Save(outputFile);
}
```

## Background and positioning

### Set a background color

Create a 400 by 30 point box with a light green background and repetition disabled.

1. Create a page and a 400-by-30-point [FloatingBox](https://reference.aspose.com/pdf/cpp/aspose.pdf/floatingbox/) with a light green background.
1. Disable repetition, add text to the box, and add the box to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/FloatingBox.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void BackgroundSupport(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto box = MakeObject<FloatingBox>(400, 30);
    box->set_BackgroundColor(Color::get_LightGreen());
    box->set_IsNeedRepeating(false);
    box->get_Paragraphs()->Add(MakeObject<TextFragment>(String(u"text example")));

    page->get_Paragraphs()->Add(box);
    document->Save(outputFile);
}
```

### Position a box with offsets

Set Top to 45 and Left to 15, choose Absolute positioning, and add the bordered box between two regular text fragments.

1. Create a bordered [FloatingBox](https://reference.aspose.com/pdf/cpp/aspose.pdf/floatingbox/) and add a text fragment to it.
1. Set `Top` to 45, `Left` to 15, and the positioning mode to `Absolute`.
1. Insert the box between two text fragments in the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/FloatingBox.h>
#include <Aspose.PDF.Cpp/Generator/ParagraphPositioningMode.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void OffsetSupport(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto box = MakeObject<FloatingBox>(400, 30);
    box->set_Top(45);
    box->set_Left(15);
    box->set_PositioningMode(ParagraphPositioningMode::Absolute);
    box->set_Border(MakeObject<BorderInfo>(BorderSide::All, 1.5f, Color::get_DarkGreen()));
    box->get_Paragraphs()->Add(MakeObject<TextFragment>(String(u"text example 1")));

    page->get_Paragraphs()->Add(MakeObject<TextFragment>(String(u"text example 2")));
    page->get_Paragraphs()->Add(box);
    page->get_Paragraphs()->Add(MakeObject<TextFragment>(String(u"text example 3")));

    document->Save(outputFile);
}
```

### Align floating containers

Create three bordered 100 by 100 point boxes aligned to the right. Compare bottom, center, and top vertical alignment.

1. Create a [page](https://reference.aspose.com/pdf/cpp/aspose.pdf/page/) and three bordered 100-by-100-point boxes with text.
1. Right-align the boxes and set the vertical alignments to bottom, center, and top, respectively.
1. Add all three boxes to the page paragraphs.
1. Save the PDF to `outputFile` with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <system/string.h>

#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>
#include <Aspose.PDF.Cpp/Generator/FloatingBox.h>
#include <Aspose.PDF.Cpp/Generator/Paragraphs.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/VerticalAlignment.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AlignTextToFloat(String inputFile, String outputFile)
{
    auto document = MakeObject<Document>();
    auto page = document->get_Pages()->Add();

    auto floatBox = MakeObject<FloatingBox>(100, 100);
    floatBox->set_VerticalAlignment(VerticalAlignment::Bottom);
    floatBox->set_HorizontalAlignment(HorizontalAlignment::Right);
    floatBox->get_Paragraphs()->Add(MakeObject<TextFragment>(String(u"FloatingBox_bottom")));
    floatBox->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Blue()));
    page->get_Paragraphs()->Add(floatBox);

    auto floatBox2 = MakeObject<FloatingBox>(100, 100);
    floatBox2->set_VerticalAlignment(VerticalAlignment::Center);
    floatBox2->set_HorizontalAlignment(HorizontalAlignment::Right);
    floatBox2->get_Paragraphs()->Add(MakeObject<TextFragment>(String(u"FloatingBox_center")));
    floatBox2->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Blue()));
    page->get_Paragraphs()->Add(floatBox2);

    auto floatBox3 = MakeObject<FloatingBox>(100, 100);
    floatBox3->set_VerticalAlignment(VerticalAlignment::Top);
    floatBox3->set_HorizontalAlignment(HorizontalAlignment::Right);
    floatBox3->get_Paragraphs()->Add(MakeObject<TextFragment>(String(u"FloatingBox_top")));
    floatBox3->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Blue()));
    page->get_Paragraphs()->Add(floatBox3);

    document->Save(outputFile);
}
```

## Related text topics

- [Working with text](/pdf/cpp/working-with-text/)
- [Add Text to PDF in C++](/pdf/cpp/add-text-to-pdf-file/)
- [Add Tooltips to PDF Text in C++](/pdf/cpp/pdf-tooltip/)
- [Replace Text in PDF with C++](/pdf/cpp/replace-text-in-pdf/)
- [Rotate PDF Text in C++](/pdf/cpp/rotate-text-inside-pdf/)
- [Search and Extract PDF Text in C++](/pdf/cpp/search-and-get-text-from-pdf/)
- [Format PDF Text in C++](/pdf/cpp/text-formatting-inside-pdf/)

For additional types and members, see the [Aspose.PDF for C++ API reference](https://reference.aspose.com/pdf/cpp/).
