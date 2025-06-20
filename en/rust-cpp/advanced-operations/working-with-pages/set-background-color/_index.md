---
title: Set the background color for PDF with Rust via C++
linktitle: Set background color 
type: docs
weight: 80
url: /rust-cpp/set-background-color/
description: Set background color for the your PDF file with Rust via C++. 
lastmod: "2025-06-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Set the background color for PDF with Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ offers functionality to set the background color of PDF pages, allowing developers to customize the appearance of documents. This feature enables the application of solid colors to the entire page background, enhancing the document's visual presentation. Developers can easily specify color values using standard color models such as RGB or CMYK. The documentation provides detailed instructions and code samples to help developers implement background color customization effectively within their C++ applications.
SoftwareApplication: rust-cpp     
---

1. The provided code snippet demonstrates how to set a background color for a PDF file using the Aspose.PDF library in Rust.
1. The [open](https://reference.aspose.com/pdf/rust-cpp/core/open/) method loads the specified PDF file into memory, allowing further manipulations, such as modifying its appearance or content.
1. The [set_background](https://reference.aspose.com/pdf/rust-cpp/organize/set_background/) method applies a new background color to the PDF document. The RGB values allow users to customize the document's visual style.
1. The [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) method saves the updated PDF under a new name.

This code is ideal for applications that need to automate PDF customizations, such as creating branded reports, adding watermarks, or enhancing visual consistency across multiple documents.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Set PDF-document background color using RGB values
      pdf.set_background(200, 100, 101)?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_set_background.pdf")?;

      Ok(())
  }
```