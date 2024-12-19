---
title: Get and Set Page Properties
type: docs
url: /go-cpp/get-and-set-page-properties/
description: Learn how to get and set page properties for PDF documents using Aspose.PDF for Go, allowing for customized document formatting.
lastmod: "2024-12-13"
---


Aspose.PDF for Go lets you read and set properties of pages in a PDF file. This section shows how to get the number of pages in a PDF file, get information about PDF page properties such as color and set page properties.

## Get Number of Pages in a PDF File

When working with documents, you often want to know how many pages they contain. With Aspose.PDF this takes no more than two lines of code.

**Aspose.PDF for Go via C++** allows you to count Pages with [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) function.

The next code snippet is designed to open a PDF document, retrieve its page count, and then print the result.

The [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) method is called to get the total number of pages in the PDF document. This is useful for tasks that need to know the length of the document, such as when extracting specific pages or performing operations across all pages. This method is a straightforward way to query the document’s structure.

To get the number of pages in a PDF file:

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
      // PageCount() returns page count in PDF-document
      count, err := pdf.PageCount()
      if err != nil {
        log.Fatal(err)
      }
      // Print
      fmt.Println("Count:", count)
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

## Set Page Size

In this example the method pdf.PageSetSize() changes the size of the first page of the PDF document. The PageSizeA1 constant ensures that the first page is set to the A1 paper size. This is useful when converting documents to a standardized format or ensuring that specific content fits correctly on pages.

1. Opening the PDF Document with [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) method.
1. Setting the Page Size with [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/) function.
1. Saving the Document using [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) method.

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
        // PageSetSize(num int32, pageSize int32) sets size of page
        err = pdf.PageSetSize(1, asposepdf.PageSizeA1)
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_page1_SetSize_A1.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```