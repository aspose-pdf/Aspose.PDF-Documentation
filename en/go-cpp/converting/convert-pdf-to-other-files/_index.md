---
title: Convert PDF to EPUB, TeX, Text, XPS in Go
linktitle: Convert PDF to other formats
type: docs
weight: 90
url: /go-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-16"
description: This topic shows you how to convert PDF files to formats such as EPUB, LaTeX, Text, and XPS using Go.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Golang tool for Converting PDF to EPUB, TeX, Text, and XPS
Abstract: Aspose.PDF for Go via C++ offers capabilities to convert PDF documents into various file formats, including EPUB, TeX, TXT, XPS, and grayscale PDF output. This functionality allows developers to extract and repurpose PDF content while maintaining layout and content fidelity across different output formats. The documentation includes step-by-step instructions and code samples to help developers integrate PDF-to-file conversion and PDF post-processing into Go applications.
SoftwareApplication: go-cpp
---

## Convert PDF to EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** is a free and open e-book standard from the International Digital Publishing Forum (IDPF). Files use the `.epub` extension, and the format is designed for reflowable content so readers can adapt the text layout to different devices and screen sizes.

The following example shows how to convert a PDF document to EPUB. Use this method when you need to repurpose PDF content for e-book readers, mobile reading applications, or digital publishing workflows.

1. Use the [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) method to load the source PDF file and create a `Document` instance for processing.
1. Call the [SaveEpub](https://reference.aspose.com/pdf/go-cpp/convert/saveepub/) method to convert the opened PDF document to EPUB format and write the result to the target file.
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
      // SaveEpub(filename string) saves previously opened PDF-document as Epub-document with filename
      err = pdf.SaveEpub("sample.epub")
      if err != nil {
        log.Fatal(err)
      }
    }
```

{{% alert color="success" %}}
**Try to convert PDF to EPUB online**

Aspose.PDF for Go presents you online free application ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to EPUB with Free App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Convert PDF to TeX

TeX and LaTeX are text-based formats used in high-quality typesetting systems. Use PDF-to-TeX conversion when you need to move PDF content into publishing or technical documentation workflows that depend on TeX-compatible source files.

The following example shows how to convert a PDF document to TeX format with Aspose.PDF for Go via C++.

1. Use the [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) method to load the input PDF document from disk.
1. Call the [SaveTeX](https://reference.aspose.com/pdf/go-cpp/convert/savetex/) method to convert the opened PDF document and save the exported TeX file.
1. Use the [Close](https://reference.aspose.com/pdf/go-cpp/core/close/) method after processing to release the native PDF resources.

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
      // SaveTeX(filename string) saves previously opened PDF-document as TeX-document with filename
      err = pdf.SaveTeX("sample.tex")
      if err != nil {
        log.Fatal(err)
      }
    }
```

{{% alert color="success" %}}
**Try to convert PDF to LaTeX/TeX online**

Aspose.PDF for Go presents you online free application ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Convert PDF to TXT

Plain text output is useful when you need to extract readable content from a PDF for search indexing, text processing pipelines, data cleanup, or lightweight export scenarios.

The following example shows how to convert a PDF document to TXT format.

1. Use the [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) method to load the source PDF file.
1. Call the [SaveTxt](https://reference.aspose.com/pdf/go-cpp/convert/savetxt/) method to export the opened PDF document as a plain text file.
1. Use the [Close](https://reference.aspose.com/pdf/go-cpp/core/close/) method after conversion to release the `Document` resources.

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
      // SaveTxt(filename string) saves previously opened PDF-document as Txt-document with filename
      err = pdf.SaveTxt("sample.txt")
      if err != nil {
        log.Fatal(err)
      }
    }
```

{{% alert color="success" %}}
**Try to convert PDF to Text online**

Aspose.PDF for Go presents you online free application ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Text with Free App](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convert PDF to XPS

The XPS file type is associated with the XML Paper Specification developed by Microsoft. Use this format when you need a fixed-layout output for Windows-centric document distribution or print-oriented workflows.

The following example shows how to convert a PDF document to <abbr title="XML Paper Specification">XPS</abbr> format with Go.

1. Use the [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) method to load the source PDF document.
1. Call the [SaveXps](https://reference.aspose.com/pdf/go-cpp/convert/savexps/) method to convert the opened PDF file and save it as an XPS document.
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
      // SaveXps(filename string) saves previously opened PDF-document as Xps-document with filename
      err = pdf.SaveXps("sample.xps")
      if err != nil {
        log.Fatal(err)
      }
    }
```

{{% alert color="success" %}}
**Try to convert PDF to XPS online**

Aspose.PDF for Go presents you online free application ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to XPS with Free App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Convert PDF to Grayscale PDF

Grayscale conversion is useful when you need to reduce color complexity for printing, archival storage, monochrome workflows, or output normalization before further document processing.

The following examples show two grayscale workflows. Use [PageGrayscale](https://reference.aspose.com/pdf/go-cpp/organize/pagegrayscale/) when you want to convert only a specific page, or use [Grayscale](https://reference.aspose.com/pdf/go-cpp/organize/grayscale/) when you need to convert the entire document. In both cases, you can write the updated PDF with the [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) method.

1. Use the [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) method to load the source PDF document.
1. Call either [PageGrayscale](https://reference.aspose.com/pdf/go-cpp/organize/pagegrayscale/) for one page or [Grayscale](https://reference.aspose.com/pdf/go-cpp/organize/grayscale/) for the full document, depending on the scope of the conversion you need.
1. Use the [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) method to write the updated grayscale PDF to a new file.
1. Use the [Close](https://reference.aspose.com/pdf/go-cpp/core/close/) method after saving to release the PDF resources.

This example converts a specific page of your PDF to grayscale:

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
      // PageGrayscale(num int32) converts page to black and white
      err = pdf.PageGrayscale(1)
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_page1_Grayscale.pdf")
      if err != nil {
        log.Fatal(err)
      }
    }
```

This example converts the entire PDF document to grayscale:

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
      // Grayscale() converts PDF-document to black and white
      err = pdf.Grayscale()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_Grayscale.pdf")
      if err != nil {
        log.Fatal(err)
      }
    }
```
