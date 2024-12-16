---
title: Add Pages to PDF Document
linktitle: Add Pages
type: docs
weight: 10
url: /go-cpp/add-pages/
description: Explore how to add pages to an existing PDF in Go with Aspose.PDF for enhancing and expanding your documents.
lastmod: "2024-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Page in a PDF File

The provided Go code snippet demonstrates how to perform the Add Page at the end of the PDF operation using the Aspose.PDF library. 

1. The [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) function allows the program to load an existing PDF file (sample.pdf) for manipulation. This is essential for any PDF-related operations, such as editing, adding content, or reading data.
1. The [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/) method is used to insert a new blank page into the existing PDF document. This is useful for extending a document or preparing it for additional content.
1. The [Save](https://reference.aspose.com/pdf/go-cpp/core/save/) method ensures that modifications to the PDF are written back to the file. This step is crucial for persisting the changes, such as the addition of new pages.
1. The [Close](https://reference.aspose.com/pdf/go-cpp/core/close/) method is called using defer to release any resources allocated during the PDF operations. This is important for preventing memory leaks and ensuring efficient resource usage.

This snippet is a concise and efficient example of how to use the Aspose.PDF Go library for basic PDF manipulation tasks.

Aspose.PDF for Go lets you insert a page to a PDF document at any location in the file as well as add pages to the end of a PDF file.

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
        // PageAdd() adds new page in PDF-document
        err = pdf.PageAdd()
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

## Insert Page in a PDF File

The [PageInsert](https://reference.aspose.com/pdf/go-cpp/core/pageinsert/) method inserts a new page at the specified position. This feature is useful when you need to insert additional pages into an existing document, for example, adding a new section or content to a report or presentation.

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
        // PageInsert(num int32) inserts new page at the specified position in PDF-document
        err = pdf.PageInsert(1)
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