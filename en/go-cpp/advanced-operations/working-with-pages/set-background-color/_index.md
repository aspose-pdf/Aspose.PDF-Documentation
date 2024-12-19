---
title: Set the background color for PDF with Go via C++
linktitle: Set background color 
type: docs
weight: 80
url: /go-cpp/set-background-color/
description: Set background color for the your PDF file with Go via C++. 
lastmod: "2024-12-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

1. The provided code snippet demonstrates how to set a background color for a PDF file using the Aspose.PDF library in Go.

1. The [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) method loads the specified PDF file into memory, allowing further manipulations, such as modifying its appearance or content.
1. The [SetBackground](https://reference.aspose.com/pdf/go-cpp/organize/setbackground/) method applies a new background color to the PDF document. The RGB values allow users to customize the document's visual style.
1. The [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) method saves the updated PDF under a new name.

This code is ideal for applications that need to automate PDF customizations, such as creating branded reports, adding watermarks, or enhancing visual consistency across multiple documents.

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
      // SetBackground(r, g, b int32) sets PDF-document background color
      err = pdf.SetBackground(200, 100, 101)
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_SetBackground.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```