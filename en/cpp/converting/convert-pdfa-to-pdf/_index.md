---
title: Convert PDF/A to standard PDF in C++
linktitle: Convert PDF/A to PDF
type: docs
weight: 120
url: /cpp/convert-pdfa-to-pdf/
description: Remove PDF/A compliance information and save a standard PDF document in C++ using Aspose.PDF.
lastmod: "2026-10-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Use Aspose.PDF for C++ to remove PDF/A compliance information from an existing PDF/A document and save the result as a regular PDF. The following example uses the Document API rather than a format-specific load option.

## Remove PDF/A compliance information

Open a PDF/A document and remove its PDF/A compliance information before saving.

This operation removes PDF/A compliance information. It does not convert the document to another archival PDF standard.

The following example is based on `pdf_a-to-pdf.cpp`.

1. Open the input PDF/A file as a [Document](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/).
1. Call [RemovePdfaCompliance()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/removepdfacompliance/).
1. Save the output file with [Save()](https://reference.aspose.com/pdf/cpp/aspose.pdf/document/save/).

```cpp
#include <Aspose.PDF.Cpp/Document.h>

using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void ConvertPDFAtoPDF(String path_infile, String path_outfile)
{
    auto document = MakeObject<Document>(path_infile);
    // Remove PDF/A compliance information
    document->RemovePdfaCompliance();
    // Save updated document
    document->Save(path_outfile);
}
```
