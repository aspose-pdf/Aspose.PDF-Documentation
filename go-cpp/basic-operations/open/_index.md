---
title: Open PDF document programmatically
linktitle: Open PDF
type: docs
weight: 20
url: /go-cpp/open-pdf-document/
description: Learn how to open a PDF file with Aspose.PDF for Go via C++.
lastmod: "2024-12-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Open existing PDF document

The code snippet demonstrates essential operations for working with PDFs using Aspose.PDF for Go. These are opening a file, saving changes, and properly closing resources. This makes it a foundational example for developers handling PDF documents.

The example is straightforward, making it easy to understand and modify. It's ideal for beginners or as a boilerplate for more complex applications.

The ability to open and save PDF documents is a core requirement in many scenarios, such as generating reports, modifying documents, or creating automated workflows.

This example showcases the API's ease of use for simple PDF manipulation, which can be expanded to include advanced features like text extraction, annotation, or form filling.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // Open(filename string) opens a PDF-document with filename
        pdf, err := asposepdf.Open("sample.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Save() saves previously opened PDF-document
        err = pdf.Save()
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
