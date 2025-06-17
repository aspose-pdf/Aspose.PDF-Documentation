---
title: Optimize PDF Resources using Rust via C++ 
linktitle: Optimize PDF Resources
type: docs
weight: 15
url: /rust-cpp/optimize-pdf-resources/
description: Optimize Resources of PDF files using Rust tool.
lastmod: "2025-06-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Optimize PDF Resources using Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ provides advanced capabilities to optimize PDF resources, enhancing document efficiency and reducing file size. The library allows developers to optimize fonts, images, and metadata by removing redundant data and compressing resources without compromising document quality. These optimization techniques improve document performance, making PDFs more suitable for sharing and storage. The documentation offers detailed guidance and code samples to help developers effectively implement resource optimization in their applications.
SoftwareApplication: rust-cpp     
---

## Optimize PDF Resources

Optimize resources in the document:

  1. Resources that are not used on the document pages are removed.
  1. Equal resources are joined into a single object.
  1. Unused objects are deleted.

Optimization may include compressing images, removing unused objects, and optimizing fonts for reduced file size and improved performance. Any error during this operation is logged and terminates the program.  
 
1. The [open](https://reference.aspose.com/pdf/rust-cpp/core/open/) method loads the specified PDF file (sample.pdf) into memory.
1. Optimizes the resources within the PDF for efficiency using [optimize_resource](https://reference.aspose.com/pdf/rust-cpp/organize/optimize_resource/) method.
1. The [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) method saves the optimized PDF to a new file.

The following code snippet shows how to optimize a PDF document.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document named "sample.pdf"
      let pdf = Document::open("sample.pdf")?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_open.pdf")?;

      Ok(())
  }
```