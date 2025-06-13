---
title: Convert PDF to Word documents in Go
linktitle: Convert PDF to Word
type: docs
weight: 10
url: /go-cpp/convert-pdf-to-doc/
lastmod: "2023-08-04"
description: Learn how to write Go code for conversion PDF to DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tool for Converting PDF to Word with Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ enables the seamless conversion of PDF documents to DOC format while preserving the original text, images, tables, and overall document structure. This feature allows developers to transform static PDFs into editable Word files for further modification and processing. The library provides various customization options to control the conversion output, ensuring high fidelity and accuracy. The documentation includes detailed instructions and sample code to help developers efficiently implement PDF-to-DOC conversion in their applications.
SoftwareApplication: go-cpp     
---

To edit the content of a PDF file in Microsoft Word or other word processors that support DOC and DOCX formats. PDF files are editable, but DOC and DOCX files are more flexible and customizable.

## Convert PDF to DOC

The provided Go code snippet demonstrates how to convert a PDF document into a DOC using the Aspose.PDF library:

1. Open a PDF document.
1. Convert a PDF file to DOC using [SaveDoc](https://reference.aspose.com/pdf/go-cpp/convert/savedoc/) function.
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
      // SaveDoc(filename string) saves previously opened PDF-document as Doc-document with filename
      err = pdf.SaveDoc("sample.doc")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Try to convert PDF to DOC online**

Aspose.PDF for Go presents you online free application ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), where you may try to investigate the functionality and quality it works.

[![Convert PDF to DOC](/cpp/converting/convert-pdf-to-word/pdf_to_doc.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) 
{{% /alert %}}

## Convert PDF to DOCX

Aspose.PDF for Go API lets you read and convert PDF documents to DOCX. DOCX is a well-known format for Microsoft Word documents whose structure was changed from plain binary to a combination of XML and binary files. Docx files can be opened with Word 2007 and lateral versions but not with the earlier versions of MS Word which support DOC file extensions.

The provided Go code snippet demonstrates how to convert a PDF document into a DOCX using the Aspose.PDF library:

1. Open a PDF document.
1. Convert a PDF file to DOCX using [SaveDocX](https://reference.aspose.com/pdf/go-cpp/convert/savedocx/) function.
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
      // SaveDocX(filename string) saves previously opened PDF-document as DocX-document with filename
      err = pdf.SaveDocX("sample.docx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Try to convert PDF to DOCX online**

Aspose.PDF for Go presents you online free application ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Word Free App](/cpp/converting/convert-pdf-to-word/pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}