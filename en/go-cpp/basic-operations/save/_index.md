---
title: Save PDF document programmatically
linktitle: Save PDF
type: docs
weight: 30
url: /go-cpp/save-pdf-document/
description: Learn how to save PDF file with Aspose.PDF for Go via C++.
lastmod: "2024-12-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Save PDF document to file system

The example demonstrates the [New](https://reference.aspose.com/pdf/go-cpp/core/new/) method for creating a new PDF document, which is a fundamental feature for generating documents dynamically, such as reports or invoices.

The code is simple and can act as a template for more advanced features like adding text, images, or annotations to the PDF.

This example demonstrates the straightforward use of the Aspose.PDF Go library, showcasing its potential for creating, modifying, and saving documents.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // New creates a new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_New_SaveAs.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
