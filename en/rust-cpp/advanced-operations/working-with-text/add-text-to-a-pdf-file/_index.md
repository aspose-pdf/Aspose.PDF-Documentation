---
title: Add Text to PDF using Go
linktitle: Add Text to PDF
type: docs
weight: 10
url: /go-cpp/add-text-to-pdf-file/
description: Learn how to add text to a PDF document in Go using Aspose.PDF for content enhancement and document editing.
lastmod: "2024-12-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: Add Text into PDF using Aspose.PDF for Go
Abstract: The Add Text to PDF File section of the Aspose.PDF for C++ and Go documentation provides step-by-step instructions on inserting text into PDF documents programmatically. It covers various methods for adding text, including positioning, font customization, color adjustments, and text alignment options. The guide demonstrates how to add text to specific pages and locations within a PDF, ensuring precise content placement. With detailed code examples and explanations, developers can easily integrate text insertion features into their applications for enhanced PDF document management.
SoftwareApplication: go-cpp      
---

To add text to existing PDF file:

1. Open a PDF file.
1. Add the text to the PDF document with [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/) function.
1. Saves the modifications to the same file.

## Adding Text

The following code snippet shows you how to add text in an existing PDF file.

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
        // PageAddText(num int32, addText string) adds text on page
        err = pdf.PageAddText(1, "added text")
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
