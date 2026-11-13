---
title: Remove PDF/UA compliance information in C++
linktitle: Convert PDF/UA to PDF
type: docs
weight: 130
url: /cpp/convert-pdfua-to-pdf/
description: Remove PDF/UA compliance information from an existing document and save the result.
lastmod: "2026-11-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Export PDF/UA to PDF Using C++
Abstract: Open a PDF/UA document, remove its compliance information, and save it as PDF. This operation does not itself remove all document tags.
---

Remove PDF/UA compliance information from an existing document and save the result.

Configure the Aspose.PDF for C++ SDK before running these functions. Pass an existing input file and a writable destination path; create any required output directories first. Each function is an independent example, and its options do not carry over to other examples.

## Remove PDF/UA compliance information

Call RemovePdfUaCompliance() before saving. Removing compliance information does not itself remove all document tags.

1. Open the input PDF/UA document.
1. Call [Document::RemovePdfUaCompliance()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/removepdfuacompliance/).
1. Save the result as PDF.

```cpp
#include <Aspose.PDF.Cpp/Document.h>

namespace ConvertingExamples
{
using namespace System;
using namespace Aspose::Pdf;

void ConvertPdfUaToPdf(String inputFile, String outputFile)
{
	auto document = MakeObject<Document>(inputFile);
	document->RemovePdfUaCompliance();
	document->Save(outputFile);
}
}
```

## Related conversion guides

- [PDF Conversion](/pdf/cpp/converting/)

