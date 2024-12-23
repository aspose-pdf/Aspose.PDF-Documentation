---
title: Convert PDF to Excel in Go
linktitle: Convert PDF to Excel
type: docs
weight: 20
url: /go-cpp/convert-pdf-to-xlsx/
lastmod: "2024-12-01"
description: Aspose.PDF for Go allows you to convert PDF to XLSX format.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

**Aspose.PDF for Go** support the feature of converting PDF files to Excel format.

## Convert PDF to XLSX

Excel provides advanced tools for sorting, filtering, and analyzing data, making it easier to perform tasks like trend analysis or financial modeling, which are difficult with static PDF files. Manually copying data from PDFs into Excel is time-consuming and error-prone. Conversion automates this process, saving significant time for large datasets.

Aspose.PDF for Go uses [SaveXlsX](https://reference.aspose.com/pdf/go-cpp/convert/savexlsx/) to convert the downloaded PDF file into an Excel spreadsheet and save it.

1. Import Required Packages.
1. Open a PDF File.
1. Convert the PDF to XLSX using [SaveXlsX](https://reference.aspose.com/pdf/go-cpp/convert/savexlsx/).
1. Close the PDF Document.

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
    // SaveXlsX(filename string) saves previously opened PDF-document as XlsX-document with filename
    err = pdf.SaveXlsX("sample.xlsx")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```

{{% alert color="success" %}}
**Try to convert PDF to Excel online**

Aspose.PDF for Go presents you online free application ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}