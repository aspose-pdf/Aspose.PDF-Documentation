---
title: Rotate PDF Pages with Go via C++ 
linktitle: Rotate PDF Pages
type: docs
weight: 50
url: /go-cpp/rotate-pages/
description: This topic describes how to rotate the page orientation in an existing PDF file programmatically with Go via C++ 
lastmod: "2024-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

This section describes how to change the page orientation from landscape to portrait and vice versa in an existing PDF file using Go via C++.

Rotating pages ensures proper alignment for printing or displaying PDFs in professional settings

1. Open the PDF Document.
1. Rotate PDF Pages. The [PageRotate](https://reference.aspose.com/pdf/go-cpp/organize/rotate/) function applies a specific rotation (in this case, 180 degrees) to a given page.
1. Save Changes to a New File. The [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) function creates a new PDF file to preserve the original while storing the updated version.

In this example, you rotate a specific page in a PDF document:

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
    // PageRotate(num int32, rotation int32) rotates page
    err = pdf.PageRotate(1, asposepdf.RotationOn180)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_page1_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```

You also have the option to rotate all PDF pages in your document:

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
    // Rotate(rotation int32) rotates PDF-document
    err = pdf.Rotate(asposepdf.RotationOn270)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```