---
title: Optimize PDF using Aspose.PDF for Rust via C++ 
linktitle: Optimize PDF File
type: docs
weight: 10
url: /rust-cpp/optimize-pdf/
description: Optimize and compress PDF files using Rust tool.
lastmod: "2025-06-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Optimize and compress PDF files using Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ offers powerful optimization features to reduce the size and improve the performance of PDF documents. The library provides various optimization options, including compressing images, removing unused objects, reducing font sizes, and optimizing content streams. These features help enhance document storage efficiency and ensure faster processing and loading times. The documentation provides step-by-step instructions and code samples to assist developers in implementing PDF optimization effectively within their applications.
SoftwareApplication: rust-cpp      
---

## Optimize PDF Document

Toolkit with Aspose.PDF for Rust via C++ allows you to optimize a PDF document.

This snippet is useful for applications where reducing the size or enhancing the efficiency of PDF files is critical, such as for web uploads, archiving, or sharing over limited bandwidth.

1. The [open](https://reference.aspose.com/pdf/rust-cpp/core/open/) method loads the specified PDF file (sample.pdf) into memory.
1. The [optimize](https://reference.aspose.com/pdf/rust-cpp/organize/optimize/) reduces the file size by performing optimizations like removing unused objects, compressing images, flattening annotations, unembedding fonts, and enabling content reuse. These steps help reduce storage requirements and improve processing speed for the PDF document.
1. The [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) method saves the optimized PDF to a new file.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Optimize PDF-document content
        pdf.optimize()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_optimize.pdf")?;

        Ok(())
    }
```