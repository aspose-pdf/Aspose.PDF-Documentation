---
title: Optimize PDF using Aspose.PDF for Go via C++ 
linktitle: Optimize PDF File
type: docs
weight: 10
url: /go-cpp/optimize-pdf/
description: Optimize and compress PDF files using Go tool.
lastmod: "2024-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Optimize and compress PDF files using Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ offers powerful optimization features to reduce the size and improve the performance of PDF documents. The library provides various optimization options, including compressing images, removing unused objects, reducing font sizes, and optimizing content streams. These features help enhance document storage efficiency and ensure faster processing and loading times. The documentation provides step-by-step instructions and code samples to assist developers in implementing PDF optimization effectively within their applications.
SoftwareApplication: go-cpp      
---

## Optimize PDF Document

Toolkit with Aspose.PDF for Go via C++ allows you to optimize a PDF document.

This snippet is useful for applications where reducing the size or enhancing the efficiency of PDF files is critical, such as for web uploads, archiving, or sharing over limited bandwidth.

1. The [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) method loads the specified PDF file (sample.pdf) into memory.
1. The [Optimize method](https://reference.aspose.com/pdf/go-cpp/organize/optimize/) reduces the file size by performing optimizations like removing unused objects, compressing images, flattening annotations, unembedding fonts, and enabling content reuse. These steps help reduce storage requirements and improve processing speed for the PDF document.
1. The [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) method saves the optimized PDF to a new file.

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
      // Optimize() optimizes PDF-document content
      err = pdf.Optimize()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_Optimize.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```