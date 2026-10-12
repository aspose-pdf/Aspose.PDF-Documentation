---
title: Extract table data from PDF in C++
linktitle: Extract Data from Table
type: docs
weight: 40
url: /cpp/extract-data-from-table-in-pdf/
description: Read detected PDF tables, filter them by a marked region, or convert the document to Excel with Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Read PDF Tables and Export to Excel in C++
Abstract: Learn how to traverse tables, rows, and cells detected by TableAbsorber in Aspose.PDF for C++. The examples also filter tables by a square annotation region and export a PDF document to Excel.
---

Read detected PDF tables, filter them by a marked region, or convert the document to Excel with Aspose.PDF for C++.

## Read detected tables

Print text from tables detected on every page.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Iterate through the pages.
1. Create a [TableAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/tableabsorber/) and visit each page.
1. Traverse detected tables, rows, cells, fragments, and segments.
1. Join cell and fragment text using separators and print each row.

Source example: `table-01.cpp`.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/Resources.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextSegment.h>
#include <Aspose.PDF.Cpp/Text/TextSegmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedTable.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedRow.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedCell.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ExtractTablesFromPdf(System::String inputFile) {
    auto document = MakeObject<Document>(inputFile);
    for (auto& page : document->get_Pages()) {
        auto absorber = MakeObject<TableAbsorber>();
        absorber->Visit(page);

        for (auto& table : absorber->get_TableList()) {
            System::Console::WriteLine(u"Table");
            for (auto& row : table->get_RowList()) {
                auto rowText = MakeObject<System::Text::StringBuilder>();
                for (auto& cell : row->get_CellList()) {
                    if (rowText->get_Length() > 0) {
                        rowText->Append(u"|");
                    }
                    auto cellText = MakeObject<System::Text::StringBuilder>();
                    for (auto& fragment : cell->get_TextFragments()) {
                        auto fragmentText = MakeObject<System::Text::StringBuilder>();
                        for (auto& segment : fragment->get_Segments()) {
                            fragmentText->Append(segment->get_Text());
                        }
                        if (cellText->get_Length() > 0) {
                            cellText->Append(u"|");
                        }
                        cellText->Append(fragmentText);
                    }
                    rowText->Append(cellText);
                }
                System::Console::WriteLine(rowText);
            }
        }
    }
}
```

## Read tables inside a square annotation

Use the first square annotation on page 1 as a region filter.

The boundary checks use strict inequalities; tables touching the annotation boundary are excluded.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Find the first Square annotation on page 1.
1. Return if no square annotation is found.
1. Visit the page with [TableAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/tableabsorber/).
1. Compare each detected table rectangle with the annotation rectangle.
1. Print rows only for tables strictly contained inside the annotation.

Source example: `table-02.cpp`.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationCollection.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/AnnotationType.h>
#include <Aspose.PDF.Cpp/InteractiveFeatures/Annotations/Annotation.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextSegment.h>
#include <Aspose.PDF.Cpp/Text/TextSegmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedTable.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedRow.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedCell.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void ExtractTableFromSpecificArea(System::String inputFile) {
    auto document = MakeObject<Document>(inputFile);
    auto page = document->get_Pages()->idx_get(1);

    SharedPtr<Annotation> squareAnnotation = nullptr;
    for (auto& annotation : page->get_Annotations()) {
        if (annotation->get_AnnotationType() == AnnotationType::Square) {
            squareAnnotation = annotation;
            break;
        }
    }

    if (squareAnnotation == nullptr) {
        System::Console::WriteLine(u"No square annotation found.");
        return;
    }

    auto absorber = MakeObject<TableAbsorber>();
    absorber->Visit(page);

    for (auto& table : absorber->get_TableList()) {
        auto tableRect = table->get_Rectangle();
        auto annotationRect = squareAnnotation->get_Rect();

        bool isInRegion = annotationRect->get_LLX() < tableRect->get_LLX()
            && annotationRect->get_LLY() < tableRect->get_LLY()
            && annotationRect->get_URX() > tableRect->get_URX()
            && annotationRect->get_URY() > tableRect->get_URY();

        if (isInRegion) {
            for (auto& row : table->get_RowList()) {
                auto rowText = MakeObject<System::Text::StringBuilder>();
                for (auto& cell : row->get_CellList()) {
                    if (rowText->get_Length() > 0) {
                        rowText->Append(u"|");
                    }
                    auto cellText = MakeObject<System::Text::StringBuilder>();
                    for (auto& fragment : cell->get_TextFragments()) {
                        auto fragmentText = MakeObject<System::Text::StringBuilder>();
                        for (auto& segment : fragment->get_Segments()) {
                            fragmentText->Append(segment->get_Text());
                        }
                        if (cellText->get_Length() > 0) {
                            cellText->Append(u"|");
                        }
                        cellText->Append(fragmentText);
                    }
                    rowText->Append(cellText);
                }
                System::Console::WriteLine(rowText);
            }
        }
    }
}
```

## Export a PDF to Excel

Save document content as XLSX using Excel conversion options.

This converts the document to Excel; it does not export a selected TableAbsorber result.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf/excelsaveoptions/) and set Format to XLSX.
1. Pass the output path and save options to [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

Source example: `table-03.cpp`.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/ExcelSaveOptions.h>

using namespace Aspose::Pdf;

void ExportTablesToExcel(System::String inputFile, System::String outputFile) {
    auto document = MakeObject<Document>(inputFile);
    auto excelSave = MakeObject<ExcelSaveOptions>();
    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::XLSX);
    document->Save(outputFile, excelSave);
}
```
