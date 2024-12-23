---
title: Aspose PDF License
linktitle: Licensing and limitations
type: docs
weight: 90
url: /go-cpp/licensing/
description: Aspose. PDF for Go invites its customers to get a Classic License. As well as use a limited license to better explore the product.
lastmod: "2024-12-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---


## Limitation of an evaluation version

We want our customers to test our components thoroughly before buying so the evaluation version allows you to use it as you would normally.

- **Documents created with an evaluation watermark.** The evaluation version of Aspose.PDF for Go provides full product functionality, but all pages in the generated files are watermarked with the text "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2024 Aspose Pty Ltd." at the top.

- **Limit the number of pages that can be processed.**
In the evaluation version, you can only process the first four pages of a document.

>If you want to test Aspose.PDF for Go without the evaluation version limitations, you can also request a 30-day Temporary License. Please refer to [How to get a Temporary License?](https://purchase.aspose.com/temporary-license)

## Classic license

Applying a license to enable full functionality of the Aspose.PDF library using a license file (Aspose.PDF.GoViaCPP.lic).

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
        // SetLicense(filename string) licenses with filename
        err = pdf.SetLicense("Aspose.PDF.GoViaCPP.lic")
        if err != nil {
            log.Fatal(err)
        }
        // Working with PDF-document
        // ...
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
