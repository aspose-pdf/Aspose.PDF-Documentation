---
title: Edit PDF page properties in C++
linktitle: PdfPageEditor Class
type: docs
weight: 120
url: /cpp/pdfpageeditor-class/
description: Change page sizes, rotation, alignment, transitions, position, and zoom and inspect page boxes using Aspose.PDF for C++.
lastmod: "2026-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Change PDF Page Geometry and Presentation in C++
Abstract: Use PdfPageEditor to configure page size, rotation, zoom, and presentation settings. The examples also read page boxes and generate a page-property report.
---

Use [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/) to change page sizes, rotation, alignment, transitions, position, and zoom and inspect page boxes.

ProcessPages limits selected edits to specific pages. The per-page rotation sample requires at least three pages. Presentation transitions depend on the viewer displaying the output.

The snippets are independent example functions with their SDK includes and example namespaces. Configure the Aspose.PDF for C++ SDK, supply the input resources referenced by the sample, and choose writable output paths. The examples retain the source field names, page indexes, coordinates, and options.

## PdfPageEditor workflows

- [Change PDF page size](#change-pdf-page-size)
- [Edit PDF pages](#edit-pdf-pages)
- [Get PDF page properties](#get-pdf-page-properties)
- [Set individual page rotations](#set-individual-page-rotations)
- [Rotate selected pages](#rotate-selected-pages)
- [Set PDF page properties](#set-pdf-page-properties)

## Change PDF page size

Select page 1 and change its size to Letter.

1. Create [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set process pages through [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/) using the example values.
1. Set page size through [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/) using the example values.
1. Save the resulting PDF with [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfPageEditor.h>
#include <Aspose.PDF.Cpp/PageSize.h>
#include <system/array.h>
#include <system/string.h>

namespace Facades::Examples::PDF_PageEditor
{
	using namespace System;
	using namespace Aspose::Pdf;
	using Aspose::Pdf::Facades::PdfPageEditor;

	void ChangePdfPageSize(String inputFile, String outputFile)
	{
		auto editor = MakeObject<PdfPageEditor>();
		editor->BindPdf(inputFile);

		editor->set_ProcessPages(MakeArray<int>({ 1 }));
		editor->set_PageSize(PageSize::get_PageLetter());

		editor->Save(outputFile);
	}
} // namespace Facades::Examples::PDF_PageEditor
```

## Edit PDF pages

Configure page 1 with Ledger size, right alignment, 90-degree rotation, zoom 1, and presentation timing settings.

1. Create [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set process pages through [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/) using the example values.
1. Set horizontal alignment through [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/) using the example values.
1. Set transition type through [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/) using the example values.
1. Set transition duration through [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/) using the example values.
1. Set display duration through [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/) using the example values.
1. Set page size through [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/) using the example values.
1. Set rotation through [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/) using the example values.
1. Set zoom through [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/) using the example values.
1. Read the page rotation with [PdfPageEditor::GetPageRotation()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/getpagerotation/).
1. Read the page count with [PdfPageEditor::GetPages()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/getpages/).
1. Save the resulting PDF with [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/)::`Save()`.
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfPageEditor.h>
#include <Aspose.PDF.Cpp/HorizontalAlignment.h>
#include <Aspose.PDF.Cpp/PageSize.h>
#include <iostream>
#include <system/array.h>
#include <system/string.h>

namespace Facades::Examples::PDF_PageEditor
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfPageEditor;

void EditPdfPages(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfPageEditor>();
    editor->BindPdf(inputFile);

    editor->set_ProcessPages(MakeArray<int>({1}));
    editor->set_HorizontalAlignment(HorizontalAlignment::Right);
    editor->set_TransitionType(2);
    editor->set_TransitionDuration(5);
    editor->set_DisplayDuration(5);
    editor->set_PageSize(PageSize::get_PageLedger());
    editor->set_Rotation(90);
    editor->set_Zoom(1.0f);
    std::cout << editor->GetPageRotation(1) << std::endl;
    std::cout << editor->GetPages() << std::endl;

    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_PageEditor
```

## Get PDF page properties

Write page 1 rotation, total pages, and trim, art, bleed, crop, and media boxes to a text report.

1. Create [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read the page rotation with [PdfPageEditor::GetPageRotation()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/getpagerotation/).
1. Read the page count with [PdfPageEditor::GetPages()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/getpages/).
1. Read page boxes with [PdfPageEditor::GetPageBoxSize()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/getpageboxsize/).
1. Write the collected values to the output text file.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfPageEditor.h>
#include <drawing/rectangle.h>
#include <iostream>
#include <string>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_PageEditor
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfPageEditor;

void GetPdfPageProperties(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfPageEditor>();
    editor->BindPdf(inputFile);
    String report =
        String::Format(u"Page 1 Rotation: {0}\nTotal Pages: {1}\n", editor->GetPageRotation(1), editor->GetPages());
    for (const auto &box : {u"trim", u"art", u"bleed", u"crop", u"media"})
        report += String(box) + u": " + editor->GetPageBoxSize(1, box).ToString() + u"\n";
    std::cout << report << std::endl;
    System::IO::File::WriteAllText(outputFile, report);
}
} // namespace Facades::Examples::PDF_PageEditor
```

## Set individual page rotations

Assign rotations of 90, 180, and 270 degrees to pages 1, 2, and 3.

1. Create [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set page rotations through [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/) using the example values.
1. Save the resulting PDF with [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfPageEditor.h>
#include <system/collections/dictionary.h>
#include <system/string.h>

namespace Facades::Examples::PDF_PageEditor
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfPageEditor;

void RotatePages1(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfPageEditor>();
    editor->BindPdf(inputFile);

    auto rotations = MakeObject<System::Collections::Generic::Dictionary<int, int>>();
    rotations->Add(1, 90);
    rotations->Add(2, 180);
    rotations->Add(3, 270);
    editor->set_PageRotations(rotations);

    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_PageEditor
```

## Rotate selected pages

Rotate pages 1 and 3 by 90 degrees.

1. Create [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Set process pages through [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/) using the example values.
1. Set rotation through [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/) using the example values.
1. Save the resulting PDF with [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfPageEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace Facades::Examples::PDF_PageEditor
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfPageEditor;

void RotatePages2(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfPageEditor>();
    editor->BindPdf(inputFile);

    editor->set_ProcessPages(MakeArray<int>({1, 3}));
    editor->set_Rotation(90);

    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_PageEditor
```

## Set PDF page properties

Move page content by (100, 100) and set zoom to 2.

1. Create [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Move page content with [PdfPageEditor::MovePosition()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/moveposition/).
1. Set zoom through [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/) using the example values.
1. Save the resulting PDF with [PdfPageEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfpageeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfPageEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_PageEditor
{
using namespace System;
using namespace Aspose::Pdf;
using Aspose::Pdf::Facades::PdfPageEditor;

void SetPdfPageProperties(String inputFile, String outputFile)
{
    auto editor = MakeObject<PdfPageEditor>();
    editor->BindPdf(inputFile);

    editor->MovePosition(100, 100);
    editor->set_Zoom(2.0f);

    editor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_PageEditor
```
