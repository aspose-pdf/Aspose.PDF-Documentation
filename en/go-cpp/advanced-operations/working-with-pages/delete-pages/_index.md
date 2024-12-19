---
title: Delete PDF Pages with Go via C++ 
linktitle: Delete PDF Pages
type: docs
weight: 30
url: /go-cpp/delete-pages/
description: You can delete pages from your PDF file using Aspose.PDF for Go via C++.
lastmod: "2024-12-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

You can delete pages from a PDF file using **Aspose.PDF for Go via C++**. The next code snippet demonstrates how to manipulate a PDF document by deleting a specific page. This method is efficient for PDF document manipulation tasks, specifically for removing pages, saving the modified document, and ensuring proper resource management.

1. Opening a PDF File.
1. Deleting a Specific Page with [PageDelete](https://reference.aspose.com/pdf/go-cpp/core/pagedelete/) function.
1. Saving the Document using [Save](https://reference.aspose.com/pdf/go-cpp/core/save/) method.

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
      // PageDelete(num int32) deletes specified page in PDF-document
      err = pdf.PageDelete(1)
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
