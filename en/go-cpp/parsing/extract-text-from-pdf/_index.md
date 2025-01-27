---
title: Extract Text from PDF using Go
linktitle: Extract text from PDF
type: docs
weight: 30
url: /go-cpp/extract-text-from-pdf/
description: This article describes various ways to extract text from PDF documents using Aspose.PDF for Go. 
lastmod: "2024-12-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract Text with Aspose.PDF for Go 
Abstract: Aspose.PDF for Go via C++ provides a powerful and efficient way to extract text from PDF documents. The library supports multiple extraction techniques, allowing users to retrieve text from entire documents, specific pages, or predefined areas within a PDF.
SoftwareApplication: go-cpp         
---

## Extract Text From PDF Document

Extracting text from the PDF document is a very common and useful task. PDFs often contain critical information that needs to be accessed, analyzed, or processed for various purposes. Extracting text enables easier reuse in databases, reports, or other documents.

Extracting text makes PDF content searchable, allowing users to locate specific information quickly without manually reviewing the entire document.

In case you want to extract text from PDF document, you can use [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) function.
Please check following code snippet in order to extract text from PDF file using Go via C++.

1. Open a PDF document with the given filename.
1. [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) extracts the text content from the PDF document.
1. Print the extracted text to the console.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"
    import "fmt"

    func main() {
        // Open(filename string) opens a PDF-document with filename
        pdf, err := asposepdf.Open("sample.pdf")
        if err != nil {
            log.Fatal(err)

        }
        // ExtractText() returns PDF-document contents as plain text
        txt, err := pdf.ExtractText()
        if err != nil {
            log.Fatal(err)
        }
        // Print
        fmt.Println("Extracted text:\n", txt)
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```