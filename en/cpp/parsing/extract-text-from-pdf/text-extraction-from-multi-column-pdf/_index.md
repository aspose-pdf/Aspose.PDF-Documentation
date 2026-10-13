---
title: Extract text from multi-column PDFs in C++
linktitle: Text Extraction from Multi-Column PDFs
type: docs
weight: 30
url: /cpp/text-extraction-from-multi-column-pdf/
description: Explore font-size reduction and extraction scale settings for text in multi-column PDF layouts with Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adjust Text Extraction for Multi-Column PDF Layouts in C++
Abstract: Explore font-size reduction and Pure formatting with a scale factor for PDF text extraction in Aspose.PDF for C++. The examples show both approaches, but extraction order must be reviewed for each input document.
---

## Extract text after reducing font sizes

Adjust in-memory text fragment sizes before extracting text from a reloaded document.

This technique changes the intermediate document. Review extraction order for your input; the example does not guarantee correct column ordering.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [TextFragmentAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textfragmentabsorber/) and process all pages.
1. Multiply each fragment font size by reduceRatio.
1. Save the modified document to a memory stream with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).
1. Reload the document from the stream and process it with [TextAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textabsorber/).
1. Write the extracted text to the output file.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentState.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void ExtractTextReduceFont(String inputFile, String outputFile, float reduceRatio)
{
    auto document = MakeObject<Document>(inputFile);
    auto fragmentAbsorber = MakeObject<TextFragmentAbsorber>();
    document->get_Pages()->Accept(fragmentAbsorber);
    for (auto& fragment : fragmentAbsorber->get_TextFragments()) {
        fragment->get_TextState()
            ->set_FontSize((fragment->get_TextState()->get_FontSize() * reduceRatio));
    }

    auto stream = MakeObject<System::IO::MemoryStream>();
    document->Save(stream);
    auto document2 = MakeObject<Document>(stream);
    auto textAbsorber = MakeObject<TextAbsorber>();
    document2->get_Pages()->Accept(textAbsorber);
    System::IO::File::WriteAllText(outputFile, textAbsorber->get_Text());
}
```

## Extract text with a scale factor

Configure Pure text formatting and a scale factor without explicitly editing text fragments.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [TextAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textabsorber/) and [TextExtractionOptions](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textextractionoptions/) with Pure formatting.
1. Set ScaleFactor to reduceRatio and assign the extraction options.
1. Process all pages.
1. Write the extracted text to the output file.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TextOptions/TextExtractionOptions.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ExtractTextScaleFactor(String inputFile, String outputFile, float reduceRatio)
{
    auto document = MakeObject<Document>(inputFile);
    auto textAbsorber = MakeObject<TextAbsorber>();
    auto extractionOptions = MakeObject<TextExtractionOptions>(TextExtractionOptions::TextFormattingMode::Pure);
    extractionOptions->set_ScaleFactor(reduceRatio);
    textAbsorber->set_ExtractionOptions(extractionOptions);
    document->get_Pages()->Accept(textAbsorber);
    System::IO::File::WriteAllText(outputFile, textAbsorber->get_Text());
}
```
