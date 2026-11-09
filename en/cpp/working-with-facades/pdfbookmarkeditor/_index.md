---
title: Manage PDF bookmarks in C++
linktitle: PdfBookmarkEditor Class
type: docs
weight: 40
url: /cpp/pdfbookmarkeditor-class/
description: Create bookmark hierarchies and page bookmarks, inspect and update titles, delete bookmarks, and exchange bookmark XML using Aspose.PDF for C++.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create and Exchange PDF Bookmarks in C++
Abstract: Use PdfBookmarkEditor to add page bookmarks and parent-child hierarchies. Additional examples inspect bookmarks, update titles, delete entries, and import or export XML.
---

Use [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/) to create bookmark hierarchies and page bookmarks, inspect and update titles, delete bookmarks, and exchange bookmark XML.

Use input PDFs with the page numbers and bookmark titles referenced by each example. The page-list example demonstrates a single title/page pair even though its function name refers to a range.

The snippets are independent example functions with their SDK includes and example namespaces. Configure the Aspose.PDF for C++ SDK, supply the input resources referenced by the sample, and choose writable output paths. The examples retain the source field names, page indexes, coordinates, and options.

## Add bookmark in an existing PDF file

Create New Bookmark targeting page 1.

1. Create [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create bookmarks with [PdfBookmarkEditor::CreateBookmarks()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/createbookmarks/).
1. Save the resulting PDF with [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/Bookmark.h>
#include <Aspose.PDF.Cpp/Facades/PdfBookmarkEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_BookmarkEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddBookmarkInAnExistingPdfFile(String inputFile, String outputFile)
{
    auto bookmark = MakeObject<Bookmark>();
    bookmark->set_PageNumber(1);
    bookmark->set_Title(u"New Bookmark");

    auto bookmarkEditor = MakeObject<PdfBookmarkEditor>();

    bookmarkEditor->BindPdf(inputFile);

    bookmarkEditor->CreateBookmarks(bookmark);

    bookmarkEditor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_BookmarkEditor
```

## Add child bookmark in an existing PDF file

Create a Parent bookmark with First Child and Second Child targeting pages 1 and 2.

1. Create [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create bookmarks with [PdfBookmarkEditor::CreateBookmarks()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/createbookmarks/).
1. Save the resulting PDF with [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/Bookmark.h>
#include <Aspose.PDF.Cpp/Facades/Bookmarks.h>
#include <Aspose.PDF.Cpp/Facades/PdfBookmarkEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_BookmarkEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void AddChildBookmarkInAnExistingPdfFile(String inputFile, String outputFile)
{
    auto bookmarks = MakeObject<Bookmarks>();
    auto childBookmark1 = MakeObject<Bookmark>();
    childBookmark1->set_PageNumber(1);
    childBookmark1->set_Title(u"First Child");
    auto childBookmark2 = MakeObject<Bookmark>();
    childBookmark2->set_PageNumber(2);
    childBookmark2->set_Title(u"Second Child");
    bookmarks->Add(childBookmark1);
    bookmarks->Add(childBookmark2);
    auto bookmark = MakeObject<Bookmark>();
    bookmark->set_Action(u"GoTo");
    bookmark->set_PageNumber(1);
    bookmark->set_Title(u"Parent");
    bookmark->set_ChildItems(bookmarks);

    auto bookmarkEditor = MakeObject<PdfBookmarkEditor>();

    bookmarkEditor->BindPdf(inputFile);

    bookmarkEditor->CreateBookmarks(bookmark);

    bookmarkEditor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_BookmarkEditor
```

## Create bookmark of a particular page

Create Bookmark Name targeting page 2.

1. Create [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create page bookmarks with [PdfBookmarkEditor::CreateBookmarkOfPage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/createbookmarkofpage/).
1. Save the resulting PDF with [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfBookmarkEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_BookmarkEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void CreateBookmarkOfAParticularPage(String inputFile, String outputFile)
{
    auto bookmarkEditor = MakeObject<PdfBookmarkEditor>();

    bookmarkEditor->BindPdf(inputFile);

    bookmarkEditor->CreateBookmarkOfPage(u"Bookmark Name", 2);

    bookmarkEditor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_BookmarkEditor
```

## Create bookmarks of a range of pages

Pass an array containing the title First and an array containing page 1 to CreateBookmarkOfPage().

1. Create [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create page bookmarks with [PdfBookmarkEditor::CreateBookmarkOfPage()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/createbookmarkofpage/).
1. Save the resulting PDF with [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfBookmarkEditor.h>
#include <system/array.h>
#include <system/string.h>

namespace Facades::Examples::PDF_BookmarkEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void CreateBookmarksOfARangeOfPages(String inputFile, String outputFile)
{
    auto bookmarkEditor = MakeObject<PdfBookmarkEditor>();

    bookmarkEditor->BindPdf(inputFile);

    auto bookmarkList = MakeArray<String>({u"First"});

    auto pageList = MakeArray<int32_t>({1});

    bookmarkEditor->CreateBookmarkOfPage(bookmarkList, pageList);

    bookmarkEditor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_BookmarkEditor
```

## Create bookmarks of all pages with properties

Create page bookmarks with green text and both style flags enabled.

1. Create [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create bookmarks with [PdfBookmarkEditor::CreateBookmarks()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/createbookmarks/).
1. Save the resulting PDF with [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Facades/PdfBookmarkEditor.h>
#include <drawing/color.h>
#include <system/string.h>

namespace Facades::Examples::PDF_BookmarkEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
using DrawingColor = System::Drawing::Color;

void CreateBookmarksOfAllPagesWithProperties(String inputFile, String outputFile)
{
    auto bookmarkEditor = MakeObject<PdfBookmarkEditor>();

    bookmarkEditor->BindPdf(inputFile);

    bookmarkEditor->CreateBookmarks(DrawingColor::get_Green(), true, true);

    bookmarkEditor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_BookmarkEditor
```

## Create bookmarks of all pages

Create bookmarks for all document pages.

1. Create [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Create bookmarks with [PdfBookmarkEditor::CreateBookmarks()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/createbookmarks/).
1. Save the resulting PDF with [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfBookmarkEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_BookmarkEditor
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void CreateBookmarksOfAllPages(String inputFile, String outputFile)
	{
		auto bookmarkEditor = MakeObject<PdfBookmarkEditor>();

		bookmarkEditor->BindPdf(inputFile);

		bookmarkEditor->CreateBookmarks();

		bookmarkEditor->Save(outputFile);
	}
} // namespace Facades::Examples::PDF_BookmarkEditor
```

## Delete all bookmarks

Delete every bookmark in the document.

1. Create [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Delete bookmarks with [PdfBookmarkEditor::DeleteBookmarks()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/deletebookmarks/).
1. Save the resulting PDF with [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfBookmarkEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_BookmarkEditor
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void DeleteAllBookmarks(String inputFile, String outputFile)
	{
		auto bookmarkEditor = MakeObject<PdfBookmarkEditor>();

		bookmarkEditor->BindPdf(inputFile);

		bookmarkEditor->DeleteBookmarks();

		bookmarkEditor->Save(outputFile);
	}
} // namespace Facades::Examples::PDF_BookmarkEditor
```

## Delete particular bookmark

Delete bookmarks matching the title Page2.

1. Create [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Delete bookmarks with [PdfBookmarkEditor::DeleteBookmarks()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/deletebookmarks/).
1. Save the resulting PDF with [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfBookmarkEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_BookmarkEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void DeleteParticularBookmark(String inputFile, String outputFile)
{
    auto bookmarkEditor = MakeObject<PdfBookmarkEditor>();

    bookmarkEditor->BindPdf(inputFile);

    bookmarkEditor->DeleteBookmarks(u"Page2");

    bookmarkEditor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_BookmarkEditor
```

## Export bookmarks to XML

Export bookmarks to an XML output file.

1. Create [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Export the bookmark XML with [PdfBookmarkEditor::ExportBookmarksToXML()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/exportbookmarkstoxml/).

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfBookmarkEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_BookmarkEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ExportBookmarksToXML(String inputFile, String outputFile)
{
    auto bookmarkEditor = MakeObject<PdfBookmarkEditor>();

    bookmarkEditor->BindPdf(inputFile);

    bookmarkEditor->ExportBookmarksToXML(outputFile);
}
} // namespace Facades::Examples::PDF_BookmarkEditor
```

## Get bookmarks from document

Extract bookmarks and write each title, page number, and action to a text report.

1. Create [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Read bookmarks with [PdfBookmarkEditor::ExtractBookmarks()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/extractbookmarks/).
1. Write the collected values to the output text file.

```cpp
#include <Aspose.PDF.Cpp/Facades/Bookmark.h>
#include <Aspose.PDF.Cpp/Facades/Bookmarks.h>
#include <Aspose.PDF.Cpp/Facades/PdfBookmarkEditor.h>
#include <string>
#include <system/io/file.h>
#include <system/io/file_stream.h>
#include <system/string.h>

namespace Facades::Examples::PDF_BookmarkEditor
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void GetBookmarksFromDocument(String inputFile, String outputFile)
	{
		auto editor = MakeObject<PdfBookmarkEditor>();
		editor->BindPdf(inputFile);
		String report;
		for (auto bookmark : editor->ExtractBookmarks())
		{
			report += u"Title: " + bookmark->get_Title() + u"\nPage Number: " +
				String::FromUtf8(std::to_string(bookmark->get_PageNumber())) + u"\nBookmark Action: " +
				bookmark->get_Action() + u"\n";
		}
		System::IO::File::WriteAllText(outputFile, report);
	}
} // namespace Facades::Examples::PDF_BookmarkEditor
```

## Import bookmarks from XML

Import bookmark data from the supplied XML file and save the PDF.

1. Create [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Import bookmark XML with [PdfBookmarkEditor::ImportBookmarksWithXML()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/importbookmarkswithxml/).
1. Save the resulting PDF with [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfBookmarkEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_BookmarkEditor
{
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void ImportBookmarksFromXML(String inputFile, String outputFile)
{
    auto bookmarkEditor = MakeObject<PdfBookmarkEditor>();

    bookmarkEditor->BindPdf(inputFile);

    auto xmlFile = inputFile.Replace(u".pdf", u".xml");

    bookmarkEditor->ImportBookmarksWithXML(xmlFile);

    bookmarkEditor->Save(outputFile);
}
} // namespace Facades::Examples::PDF_BookmarkEditor
```

## Update existing bookmark

Update an existing bookmark title using ModifyBookmarks().

1. Create [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/).
1. Bind the PDF input with [Facade::BindPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/facade/bindpdf/).
1. Change the bookmark title with [PdfBookmarkEditor::ModifyBookmarks()](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/modifybookmarks/).
1. Save the resulting PDF with [PdfBookmarkEditor](https://reference.aspose.com/pdf/cpp/aspose.pdf.facades/pdfbookmarkeditor/)::`Save()`.

```cpp
#include <Aspose.PDF.Cpp/Facades/PdfBookmarkEditor.h>
#include <system/string.h>

namespace Facades::Examples::PDF_BookmarkEditor
{
	using namespace System;
	using namespace Aspose::Pdf;
	using namespace Aspose::Pdf::Facades;

	void UpdateExistingBookmark(String inputFile, String outputFile)
	{
		auto bookmarkEditor = MakeObject<PdfBookmarkEditor>();

		bookmarkEditor->BindPdf(inputFile);

		bookmarkEditor->ModifyBookmarks(u"New Bookmark", u"New Title");

		bookmarkEditor->Save(outputFile);
	}
} // namespace Facades::Examples::PDF_BookmarkEditor
```
