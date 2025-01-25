---
title: Convert PDF to EPUB, TeX, Text, XPS in Go
linktitle: Convert PDF to other formats 
type: docs
weight: 90
url: /go-cpp/convert-pdf-to-other-files/
lastmod: "2024-11-01"
description: This topic shows you how to convert PDF file to other file formats like EPUB, LaTeX, Text, XPS etc using Go.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Tool for Converting PDF to EPUB, TeX, Text, and XPS
Abstract: Aspose.PDF for Go via C++ offers powerful capabilities to convert PDF documents into various file formats, including DOCX, PPTX, HTML, EPUB, SVG, and more. This functionality allows developers to extract and repurpose PDF content seamlessly while maintaining formatting, structure, and quality across different output formats. The library provides flexible options to customize the conversion process according to specific requirements. The documentation includes comprehensive guidelines and code samples to assist developers in efficiently implementing PDF-to-file conversion within their applications. 
SoftwareApplication: go-cpp     
---

## Convert PDF to EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** is a free and open e-book standard from the International Digital Publishing Forum (IDPF). Files have the extension .epub.
EPUB is designed for reflowable content, meaning that an EPUB reader can optimize text for a particular display device. EPUB also supports fixed-layout content. The format is intended as a single format that publishers and conversion houses can use in-house, as well as for distribution and sale. It supersedes the Open eBook standard.

The provided Go code snippet demonstrates how to convert a PDF document into a EPUB using the Aspose.PDF library:

1. Open a PDF document.
1. Convert a PDF file to EPUB using [SaveEpub]() function.
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
      // SaveEpub(filename string) saves previously opened PDF-document as Epub-document with filename
      err = pdf.SaveEpub("sample.epub")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Try to convert PDF to EPUB online**

Aspose.PDF for Go presents you online free application ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to EPUB with Free App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Convert PDF to TeX

**Aspose.PDF for Go** support converting PDF to TeX.
The LaTeX file format is a text file format with the special markup and used in TeX-based document preparation system for high-quality typesetting.

The provided Go code snippet demonstrates how to convert a PDF document into a TeX using the Aspose.PDF library:

1. Open a PDF document.
1. Convert a PDF file to TeX using [SaveTeX](https://reference.aspose.com/pdf/go-cpp/convert/savetex/) function.
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
      // SaveTeX(filename string) saves previously opened PDF-document as TeX-document with filename
      err = pdf.SaveTeX("sample.tex")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Try to convert PDF to LaTeX/TeX online**

Aspose.PDF for Go presents you online free application ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Convert PDF to TXT

The provided Go code snippet demonstrates how to convert a PDF document into a TXT using the Aspose.PDF library:

1. Open a PDF document.
1. Convert a PDF file to TXT using [SaveTxt](https://reference.aspose.com/pdf/go-cpp/convert/savetxt/) function.
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
      // SaveTxt(filename string) saves previously opened PDF-document as Txt-document with filename
      err = pdf.SaveTxt("sample.txt")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Try to convert Convert PDF to Text online**

Aspose.PDF for Go presents you online free application ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Text with Free App](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convert PDF to XPS

The XPS file type is primarily associated with the XML Paper Specification by Microsoft Corporation. The XML Paper Specification (XPS), formerly codenamed Metro and subsuming the Next Generation Print Path (NGPP) marketing concept, is Microsoft's initiative to integrate document creation and viewing into the Windows operating system.

**Aspose.PDF for Go** gives a possibility to convert PDF files to <abbr title="XML Paper Specification">XPS</abbr> format. Let try to use the presented code snippet for converting PDF files to XPS format with Go.

The provided Go code snippet demonstrates how to convert a PDF document into a XPS using the Aspose.PDF library:

1. Open a PDF document.
1. Convert a PDF file to XPS using [SaveXps](https://reference.aspose.com/pdf/go-cpp/convert/savexps/) function.
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
      // SaveXps(filename string) saves previously opened PDF-document as Xps-document with filename
      err = pdf.SaveXps("sample.xps")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Try to convert PDF to XPS online**

Aspose.PDF for Go presents you online free application ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to XPS with Free App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Convert PDF to Grayscale PDF

The provided Go code snippet demonstrates how to convert the first page of a PDF document into a Grayscale PDF using the Aspose.PDF library:

1. Open a PDF document.
1. Convert a PDF Page to Grayscale PDF using [PageGrayscale](https://reference.aspose.com/pdf/go-cpp/organize/pagegrayscale/) function.
1. Close the PDF document and release any allocated resources.

This example converts a specific page of your PDF to Grayscale:

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
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

This example will convert the entire PDF document to Grayscale:

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
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```