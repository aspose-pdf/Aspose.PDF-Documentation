---
title: Basic text extraction in C++
linktitle: Basic Text Extraction
type: docs
weight: 10
url: /cpp/basic-text-extraction/
description: Extract text from all pages, the first page, or detected paragraphs using Aspose.PDF for C++.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract PDF Document, Page, and Paragraph Text in C++
Abstract: Learn how to extract text from all PDF pages or a selected page using TextAbsorber in Aspose.PDF for C++. Use ParagraphAbsorber to inspect detected paragraphs and collect their text.
---

Extract text from all pages, the first page, or detected paragraphs using Aspose.PDF for C++.

## Extract text from all pages

Collect document text into one output file.

1. Open the input PDF as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Create a [TextAbsorber](https://reference.aspose.com/pdf/cpp/aspose.pdf.text/textabsorber/).
1. Pass the absorber to the page collection's Accept() method.
1. Read the absorber's Text property.
1. Write the extracted text to the output file.

```cpp

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TextAbsorber.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ExtractTextFromAllThePages(System::String path_infile, System::String path_outfile) {


    // Open document
    auto document = MakeObject<Document>(path_infile);

    // Create TextAbsorber object to extract text
    auto textAbsorber = MakeObject<TextAbsorber>();
    // Accept the absorber for all the pages
    document->get_Pages()->Accept(textAbsorber);
    // Get the extracted text
    auto extractedText = textAbsorber->get_Text();

    System::IO::File::WriteAllText(path_outfile, extractedText);
}
```

