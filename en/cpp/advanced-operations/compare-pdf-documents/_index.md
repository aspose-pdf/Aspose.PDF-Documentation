---
title: Compare PDF documents in C++
linktitle: Compare PDF
type: docs
weight: 130
url: /cpp/compare-pdf-documents/
description: Compare PDF pages and entire documents in C++ with side-by-side PDF output, graphical reports, and PNG difference images.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Find PDF Page and Document Differences in C++
Abstract: Learn how to compare selected pages or entire PDF documents with Aspose.PDF for C++. Use side-by-side comparisons, graphical PDF reports, and PNG images to review differences.
---

Aspose.PDF for C++ provides APIs to compare selected PDF pages or entire documents. Use [SideBySidePdfComparer](https://reference.aspose.com/pdf/cpp/aspose.pdf.comparison/sidebysidepdfcomparer/) for marked page pairs and [GraphicalPdfComparer](https://reference.aspose.com/pdf/cpp/aspose.pdf.comparison/graphicalpdfcomparer/) for image-based differences and graphical PDF reports.

The following examples accept input and output file paths. Configure your project to include and link Aspose.PDF for C++ and create output directories before running the functions.

## Compare pages and export difference images

Export the graphical differences between the first page of each input PDF as a PNG image. The example also saves a reconstructed destination image.

1. Open both input PDFs as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) objects.
1. Create a [GraphicalPdfComparer](https://reference.aspose.com/pdf/cpp/aspose.pdf.comparison/graphicalpdfcomparer/) and select page 1 from each document.
1. Call [GetDifference()](https://reference.aspose.com/pdf/cpp/aspose.pdf.comparison/graphicalpdfcomparer/) to obtain an [ImagesDifference](https://reference.aspose.com/pdf/cpp/aspose.pdf.comparison/) object.
1. Generate a difference image with DifferenceToImage(), using red for changes and white for the background.
1. Save the difference image as PNG.
1. Retrieve the destination image with GetDestinationImage() and save it as PNG.
1. Release the comparison result with Dispose().

```cpp

#include <iostream>
#include <drawing/bitmap.h>
#include <drawing/imaging/image_format.h>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Comparison/GraphicalComparison/GraphicalPdfComparer.h>
#include <Aspose.PDF.Cpp/Comparison/GraphicalComparison/ImagesDifference.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Comparison;

void ComparePdfWithGetDifferenceMethod(System::String inputFile1, System::String inputFile2,
    System::String diffOutputFile, System::String destinationOutputFile)
{
    auto document1 = MakeObject<Document>(inputFile1);
    auto document2 = MakeObject<Document>(inputFile2);
    auto comparer = MakeObject<GraphicalPdfComparer>();
    auto imagesDifference = comparer->GetDifference(document1->get_Pages()->idx_get(1),
        document2->get_Pages()->idx_get(1));

    auto differenceImage = imagesDifference->DifferenceToImage(Color::get_Red(), Color::get_White());
    differenceImage->Save(diffOutputFile, System::Drawing::Imaging::ImageFormat::get_Png());
    auto destinationImage = imagesDifference->GetDestinationImage();
    destinationImage->Save(destinationOutputFile, System::Drawing::Imaging::ImageFormat::get_Png());
    imagesDifference->Dispose();

    std::cout << "Difference images saved to " << diffOutputFile << " and " << destinationOutputFile << std::endl;
}
```

## Compare specific pages side by side

Compare the first page of each PDF and save the marked pages in an output PDF. Both input documents must contain at least one page.

Page collection indices start at 1. Change the selected indices to compare another pair of pages. Open the output in two-page view to inspect the pair side by side.

1. Open both input PDFs as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) objects.
1. Create [SideBySideComparisonOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.comparison/).
1. Enable additional change marks and set [ComparisonMode](https://reference.aspose.com/pdf/cpp/aspose.pdf.comparison/) to IgnoreSpaces.
1. Select page 1 from each document.
1. Pass the selected pages, output path, and options to [SideBySidePdfComparer::Compare()](https://reference.aspose.com/pdf/cpp/aspose.pdf.comparison/sidebysidepdfcomparer/compare/).

```cpp

#include <iostream>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Comparison/SideBySideComparison/SideBySideComparisonOptions.h>
#include <Aspose.PDF.Cpp/Comparison/SideBySideComparison/SideBySidePdfComparer.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Comparison;

void ComparingSpecificPages(System::String inputFile1, System::String inputFile2, System::String outputFile)
{
    auto document1 = MakeObject<Document>(inputFile1);
    auto document2 = MakeObject<Document>(inputFile2);
    auto options = MakeObject<SideBySideComparisonOptions>();
    options->set_AdditionalChangeMarks(true);
    options->set_ComparisonMode(ComparisonMode::IgnoreSpaces);

    SideBySidePdfComparer::Compare(document1->get_Pages()->idx_get(1),
        document2->get_Pages()->idx_get(1), outputFile, options);

    std::cout << "Specific pages comparison saved to " << outputFile << std::endl;
}
```

## Compare full PDF documents graphically

Generate a PDF report that highlights graphical differences between two documents. Configure the comparison sensitivity, highlight color, and rendering resolution before creating the report.

1. Open both input PDFs as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) objects.
1. Create a [GraphicalPdfComparer](https://reference.aspose.com/pdf/cpp/aspose.pdf.comparison/graphicalpdfcomparer/).
1. Set the comparison threshold to 3.0 percent and the highlight color to blue.
1. Set a resolution of 300 dpi with [Resolution](https://reference.aspose.com/pdf/cpp/aspose.pdf.devices/resolution/).
1. Call [CompareDocumentsToPdf()](https://reference.aspose.com/pdf/cpp/aspose.pdf.comparison/graphicalpdfcomparer/) with both documents and the output file path.

```cpp

#include <iostream>
#include <Aspose.PDF.Cpp/Color.h>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Devices/Resolution.h>
#include <Aspose.PDF.Cpp/Comparison/GraphicalComparison/GraphicalPdfComparer.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Comparison;

void ComparePdfWithCompareDocumentsToPdfMethod(System::String inputFile1, System::String inputFile2,
    System::String outputFile)
{
    auto document1 = MakeObject<Document>(inputFile1);
    auto document2 = MakeObject<Document>(inputFile2);
    auto comparer = MakeObject<GraphicalPdfComparer>();
    comparer->set_Threshold(3.0);
    comparer->set_Color(Color::get_Blue());
    comparer->set_Resolution(MakeObject<Devices::Resolution>(300));
    comparer->CompareDocumentsToPdf(document1, document2, outputFile);

    std::cout << "Graphical comparison saved to " << outputFile << std::endl;
}
```

## Compare entire documents side by side

Compare two PDF files page by page and save the marked results in a single PDF. The output alternates pages from the first and second document.

1. Open both input PDFs as [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/) objects.
1. Create [SideBySideComparisonOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.comparison/).
1. Enable additional change marks and set [ComparisonMode](https://reference.aspose.com/pdf/cpp/aspose.pdf.comparison/) to IgnoreSpaces.
1. Pass both documents, the output path, and the options to [SideBySidePdfComparer::Compare()](https://reference.aspose.com/pdf/cpp/aspose.pdf.comparison/sidebysidepdfcomparer/compare/).
1. Open the resulting PDF in two-page view to review corresponding pages side by side.

```cpp

#include <iostream>
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Comparison/SideBySideComparison/SideBySideComparisonOptions.h>
#include <Aspose.PDF.Cpp/Comparison/SideBySideComparison/SideBySidePdfComparer.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Comparison;

void ComparingEntireDocuments(System::String inputFile1, System::String inputFile2, System::String outputFile)
{
    auto document1 = MakeObject<Document>(inputFile1);
    auto document2 = MakeObject<Document>(inputFile2);
    auto options = MakeObject<SideBySideComparisonOptions>();
    options->set_AdditionalChangeMarks(true);
    options->set_ComparisonMode(ComparisonMode::IgnoreSpaces);

    SideBySidePdfComparer::Compare(document1, document2, outputFile, options);

    std::cout << "Entire document comparison saved to " << outputFile << std::endl;
}
```
