---
title: Convert PDF to Word documents in Go
linktitle: Convert PDF to Word
type: docs
weight: 10
url: /go-cpp/convert-pdf-to-doc/
lastmod: "2026-07-16"
description: Learn how to write Go code to convert PDF documents to DOC and DOCX formats.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tool for Converting PDF to Word with Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ enables the seamless conversion of PDF documents to DOC format while preserving the original text, images, tables, and overall document structure. This feature allows developers to transform static PDFs into editable Word files for further modification and processing. The library provides various customization options to control the conversion output, ensuring high fidelity and accuracy. The documentation includes detailed instructions and sample code to help developers efficiently implement PDF-to-DOC conversion in their applications.
SoftwareApplication: go-cpp
---

Convert PDF files to Word formats when you need to move static document content into editable word-processing workflows. DOC and DOCX outputs are useful for review, reuse, and further content updates in Microsoft Word and other compatible editors.

## Convert PDF to DOC

Use DOC conversion when you need a broadly compatible Word-processing format for editing, review, or export into older document workflows.

The following example shows how to convert a PDF document to DOC with Aspose.PDF for Go via C++.

1. Use the [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) method to load the source PDF file and return a `Document` instance for processing.
1. Call the [SaveDoc](https://reference.aspose.com/pdf/go-cpp/convert/savedoc/) method to convert the opened PDF document and save the result as a DOC file.
1. Use the [Close](https://reference.aspose.com/pdf/go-cpp/core/close/) method after conversion to release the resources associated with the opened PDF document.

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
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
      // SaveDoc(filename string) saves previously opened PDF-document as Doc-document with filename
      err = pdf.SaveDoc("sample.doc")
      if err != nil {
        log.Fatal(err)
      }
    }
```

{{% alert color="success" %}}
**Try to convert PDF to DOC online**

Aspose.PDF for Go presents you online free application ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), where you may try to investigate the functionality and quality it works.

[![Convert PDF to DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) 
{{% /alert %}}

## Convert PDF to DOCX

Aspose.PDF for Go API also lets you convert PDF documents to DOCX. DOCX is the modern Microsoft Word format based on XML packaging and is the preferred option when you need better compatibility with current editing, collaboration, and document-processing tools.

The following example shows how to convert a PDF document to DOCX with Aspose.PDF for Go via C++.

1. Use the [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) method to load the input PDF document from disk.
1. Call the [SaveDocX](https://reference.aspose.com/pdf/go-cpp/convert/savedocx/) method to convert the opened PDF document and save the result as a DOCX file.
1. Use the [Close](https://reference.aspose.com/pdf/go-cpp/core/close/) method when processing is complete to release the PDF resources.

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
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
      // SaveDocX(filename string) saves previously opened PDF-document as DocX-document with filename
      err = pdf.SaveDocX("sample.docx")
      if err != nil {
        log.Fatal(err)
      }
    }
```

{{% alert color="success" %}}
**Try to convert PDF to DOCX online**

Aspose.PDF for Go presents you online free application ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Word Free App](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}
