---
title: Convert PDF to PPTX in Go
linktitle: Convert PDF to PowerPoint
type: docs
weight: 30
url: /go-cpp/convert-pdf-to-powerpoint/
lastmod: "2024-11-01"
description: Aspose.PDF allows you to convert PDF to PPTX format using Go via C++.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

{{% alert color="success" %}}
**Try to convert PDF to PowerPoint online**

Aspose.PDF for Go presents you online free application ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

## Convert PDF to PPTX

The provided Go code snippet demonstrates how to convert a PDF document into a PPTX using the Aspose.PDF library:

1. Open a PDF document.
1. Convert a PDF file to PPTX using [SavePptx](https://reference.aspose.com/pdf/go-cpp/convert/savepptx/) function.
1. Close the PDF document and release any allocated resources.

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
      // SavePptX(filename string) saves previously opened PDF-document as PptX-document with filename
      err = pdf.SavePptX("sample.pptx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

