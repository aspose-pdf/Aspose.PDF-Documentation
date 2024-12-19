---
title: Example of Hello World using Go language
linktitle: Hello World Example
type: docs
weight: 40
url: /go-cpp/hello-world-example/
description: This sample demonstrates how to create a simple PDF document with text Hello World using Aspose.PDF for Go.
lastmod: "2024-12-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

A "Hello World" example is traditionally used to introduce features of a programming language or software with a simple use case.

**Aspose.PDF for Go** is a feature-rich PDF API that allows developers to embed PDF document creation, manipulation, and conversion capabilities with Go. It supports many popular file formats, including PDF, TXT, HTML, PCL, XPS, EPUB, TEX, and image file formats. In this article, we are creating a PDF document containing the text "Hello World!" After installing Aspose.PDF for Go in your environment, you can execute the code sample to see how the Aspose.PDF API works.
Below code snippet follows these steps:

1. Create a new PDF document instance.
1. Add a new page to the PDF document using [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/) function.
1. Set the page size using [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/).
1. Add "Hello World!" text to the first page using [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/).
1. Save the repaired PDF document using [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) method.
1. Close the PDF document and release any allocated resources.

Following code snippet is a Hello World program to exhibit working of Aspose.PDF for Go API.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // Create new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
                log.Fatal(err)
        }
        // Add new page
        err = pdf.PageAdd()
        if err != nil {
                log.Fatal(err)
        }
        // Set page size A4
        err = pdf.PageSetSize(1, asposepdf.PageSizeA4)
        if err != nil {
                log.Fatal(err)
        }
        // Add text on first page
        err = pdf.PageAddText(1, "Hello World!")
        if err != nil {
                log.Fatal(err)
        }
        // Save PDF-document with "hello.pdf" name
        err = pdf.SaveAs("hello.pdf")
        if err != nil {
                log.Fatal(err)
        }
        // Release allocated resources
        defer pdf.Close()
    }
```
