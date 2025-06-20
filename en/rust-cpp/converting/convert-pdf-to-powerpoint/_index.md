---
title: Convert PDF to PPTX in Rust
linktitle: Convert PDF to PowerPoint
type: docs
weight: 30
url: /rust-cpp/convert-pdf-to-powerpoint/
lastmod: "2025-06-01"
description: Aspose.PDF allows you to convert PDF to PPTX format using Rust.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rust Tool for Converting PDF to PowerPoint
Abstract: Aspose.PDF for Rust via C++ provides a reliable solution for converting PDF documents to PowerPoint (PPTX) format while preserving the original layout, formatting, and content structure. This functionality enables developers to seamlessly transform static PDF files into dynamic, editable presentations. The library offers customization options to control the conversion process, ensuring high-quality output suitable for business and professional use. The documentation provides step-by-step instructions and code samples to help developers efficiently integrate PDF-to-PowerPoint conversion into their applications.
SoftwareApplication: rust-cpp      
---

## Convert PDF to PPTX

The provided Rust code snippet demonstrates how to convert a PDF document into a PPTX using the Aspose.PDF library:

1. Open a PDF document.
1. Convert a PDF file to PPTX using [save_pptx](https://reference.aspose.com/pdf/rust-cpp/convert/save_pptx/) function.

```rust

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as PptX-document
      pdf.save_pptx("sample.pptx")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Try to convert PDF to PowerPoint online**

Aspose.PDF for Rust presents you online free application ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to PPTX with Free App](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}