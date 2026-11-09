---
title: Merge, split, and arrange PDF pages in C++
linktitle: PdfFileEditor Class
type: docs
weight: 80
url: /cpp/pdffileeditor-class/
description: Merge, append, insert, delete, extract, split, impose, and resize PDF pages and content using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Process PDF Files and Arrange Pages in C++
Abstract: Use PdfFileEditor for file-based page operations and document imposition. The examples cover merging, splitting, page selection, margins, content resizing, N-up output, and booklets.
---

Use [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/) to merge, append, insert, delete, extract, split, impose, and resize PDF pages and content.

These functions pass file paths directly to PdfFileEditor rather than binding an input PDF. Supply the page counts referenced in each sample. Some examples inspect Boolean results and report failure or throw an exception.

The snippets are independent example functions with their SDK includes and example namespaces. Configure the Aspose.PDF for C++ SDK, supply the input resources referenced by the sample, and choose writable output paths. The examples retain the source field names, page indexes, coordinates, and options.

## Add margins to PDF pages

Apply margins of 36 points on each side of pages 1 and 3.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Apply page margins with [PdfFileEditor::AddMargins()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/addmargins/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace Facades::Examples::PDF_FileEditor
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void AddMarginsToPdfPages(String inputFile, String outputFile)
	{
		auto pdfEditor = MakeObject<PdfFileEditor>();
		pdfEditor->AddMargins(inputFile, outputFile, MakeArray<int32_t>({ 1, 3 }), 36, 36, 36, 36);
	}
} // namespace  Facades::Examples::PDF_FileEditor
```

## Add page breaks in PDF

Insert a page break on page 1 at the position specified by 400.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Insert the page break with [PdfFileEditor::AddPageBreak()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/addpagebreak/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddPageBreaksInPdf(String inputFile, String outputFile)
{
    auto pdfEditor = MakeObject<PdfFileEditor>();
    pdfEditor->AddPageBreak(
        inputFile, outputFile,
        MakeArray<SharedPtr<PdfFileEditor::PageBreak>>({MakeObject<PdfFileEditor::PageBreak>(1, 400)}));
}
} // namespace  Facades::Examples::PDF_FileEditor
```

## Append pages to PDF

Append page 1 from sampleFile to inputFile.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Append pages with [PdfFileEditor::Append()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/append/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AppendPagesToPdf(String inputFile, String sampleFile, String outputFile)
{
    auto pdfEditor = MakeObject<PdfFileEditor>();
    pdfEditor->Append(inputFile, MakeArray<String>({sampleFile}), 1, 1, outputFile);
}
} // namespace  Facades::Examples::PDF_FileEditor
```

## Create N-up PDF document

Create N-up output using a 2 by 2 layout.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Generate N-up output with [PdfFileEditor::MakeNUp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/makenup/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void CreateNupPdfDocument(String inputFile, String outputFile)
{
    auto nupMaker = MakeObject<PdfFileEditor>();
    nupMaker->MakeNUp(inputFile, outputFile, 2, 2);
}
} // namespace  Facades::Examples::PDF_FileEditor
```

## Create PDF booklet

Create booklet output with the default MakeBooklet overload.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Generate booklet output with [PdfFileEditor::MakeBooklet()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/makebooklet/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void CreatePdfBooklet(String inputFile, String outputFile)
{
    auto bookletMaker = MakeObject<PdfFileEditor>();
    bookletMaker->MakeBooklet(inputFile, outputFile);
}
} // namespace  Facades::Examples::PDF_FileEditor
```

## Delete pages from PDF

Delete pages 2 and 4.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Delete the selected pages with [PdfFileEditor::Delete()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/delete/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void DeletePagesFromPdf(String inputFile, String outputFile)
{
    auto pdfEditor = MakeObject<PdfFileEditor>();
    pdfEditor->Delete(inputFile, MakeArray<int32_t>({2, 4}), outputFile);
}
} // namespace  Facades::Examples::PDF_FileEditor
```

## Extract pages from PDF

Extract pages in the order 1, 4, 3.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Extract the selected pages with [PdfFileEditor::Extract()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/extract/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ExtractPagesFromPdf(String inputFile, String outputFile)
{
    auto pdfEditor = MakeObject<PdfFileEditor>();
    pdfEditor->Extract(inputFile, MakeArray<int32_t>({1, 4, 3}), outputFile);
}
} // namespace  Facades::Examples::PDF_FileEditor
```

## Insert pages into PDF

Insert pages 1 and 2 from sampleFile after page 2 of the input document.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Insert source pages with [PdfFileEditor::Insert()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/insert/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void InsertPagesIntoPdf(String inputFile, String sampleFile, String outputFile)
{
    auto pdfEditor = MakeObject<PdfFileEditor>();
    pdfEditor->Insert(inputFile, 2, sampleFile, MakeArray<int32_t>({1, 2}), outputFile);
}
} // namespace  Facades::Examples::PDF_FileEditor
```

## Merge PDF documents

Concatenate firstInputFile and secondInputFile in that order.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Merge the input files with [PdfFileEditor::Concatenate()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/concatenate/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void MergePdfDocuments(String firstInputFile, String secondInputFile, String outputFile)
{
    auto pdfEditor = MakeObject<PdfFileEditor>();
    pdfEditor->Concatenate(MakeArray<String>({firstInputFile, secondInputFile}), outputFile);
}
} // namespace  Facades::Examples::PDF_FileEditor
```

## Resize PDF page contents

Resize content on pages 1 and 3 using dimensions 400 and 750. Throw an error if ResizeContents returns false.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Resize page content with [PdfFileEditor::ResizeContents()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/resizecontents/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <stdexcept>
#include <system/array.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ResizePdfPageContents(String inputFile, String outputFile)
{
    auto pdfEditor = MakeObject<PdfFileEditor>();
    if (!pdfEditor->ResizeContents(inputFile, outputFile, MakeArray<int32_t>({1, 3}), 400, 750))
    {
        throw std::runtime_error("Failed to resize PDF page contents.");
    }
}
} // namespace  Facades::Examples::PDF_FileEditor
```

## Resize content with percentage margins

Resize content on pages 1 and 2 using percentage-based margins of 10 on each side.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Resize page content with [PdfFileEditor::ResizeContents()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/resizecontents/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ResizePdfPageContents2(String inputFile, String outputFile)
{
    auto fileEditor = MakeObject<PdfFileEditor>();

    auto parameters = MakeObject<PdfFileEditor::ContentsResizeParameters>(

        PdfFileEditor::ContentsResizeValue::Percents(10),

        nullptr,

        PdfFileEditor::ContentsResizeValue::Percents(10),

        PdfFileEditor::ContentsResizeValue::Percents(10),

        nullptr,

        PdfFileEditor::ContentsResizeValue::Percents(10));

    fileEditor->ResizeContents(inputFile, outputFile, MakeArray<int32_t>({1, 2}), parameters);
}
} // namespace  Facades::Examples::PDF_FileEditor
```

## Split PDF from beginning

Write the first three pages to a new PDF.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Write the first page range with [PdfFileEditor::SplitFromFirst()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/splitfromfirst/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SplitPdfFromBeginning(String inputFile, String outputFile)
{
    auto pdfFileEditor = MakeObject<PdfFileEditor>();
    pdfFileEditor->SplitFromFirst(inputFile, 3, outputFile);
}
} // namespace  Facades::Examples::PDF_FileEditor
```

## Split PDF into single pages

Split the PDF into individual pages using outputFilePattern.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Write individual page files with [PdfFileEditor::SplitToPages()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/splittopages/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SplitPdfIntoSinglePages(String inputFile, String outputFilePattern)
{
    auto pdfFileEditor = MakeObject<PdfFileEditor>();
    pdfFileEditor->SplitToPages(inputFile, outputFilePattern);
}
} // namespace  Facades::Examples::PDF_FileEditor
```

## Split PDF to end

Write pages from page 2 through the end to a new PDF.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Write the ending page range with [PdfFileEditor::SplitToEnd()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/splittoend/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SplitPdfToEnd(String inputFile, String outputFile)
{
    auto pdfFileEditor = MakeObject<PdfFileEditor>();
    pdfFileEditor->SplitToEnd(inputFile, 2, outputFile);
}
} // namespace  Facades::Examples::PDF_FileEditor
```

## Try create N-up PDF document

Create a 2 by 2 N-up document and print a failure message if MakeNUp returns false.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Generate N-up output with [PdfFileEditor::MakeNUp()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/makenup/).
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <iostream>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void TryCreateNupPdfDocument(String inputFile, String outputFile)
{
    auto nupMaker = MakeObject<PdfFileEditor>();
    if (!nupMaker->MakeNUp(inputFile, outputFile, 2, 2))
    {
        std::cout << "Failed to create N-Up PDF document." << std::endl;
    }
}
} // namespace  Facades::Examples::PDF_FileEditor
```

## Try create PDF booklet

Create a booklet and print a failure message if MakeBooklet returns false.

1. Create [PdfFileEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/).
1. Generate booklet output with [PdfFileEditor::MakeBooklet()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdffileeditor/makebooklet/).
1. Print the results or diagnostic messages shown in the example.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfFileEditor.h>
#include <iostream>
#include <system/string.h>

namespace  Facades::Examples::PDF_FileEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void TryCreatePdfBooklet(String inputFile, String outputFile)
{
    auto bookletMaker = MakeObject<PdfFileEditor>();
    if (!bookletMaker->MakeBooklet(inputFile, outputFile))
    {
        std::cout << "Failed to create booklet." << std::endl;
    }
}
} // namespace  Facades::Examples::PDF_FileEditor
```
