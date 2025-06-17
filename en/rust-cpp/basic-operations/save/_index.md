---
title: Save PDF document programmatically
linktitle: Save PDF
type: docs
weight: 30
url: /rust-cpp/save-pdf-document/
description: Learn how to save PDF file with Aspose.PDF for Rust via C++.
lastmod: "2025-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Save PDF document with Aspose.PDF for Rust via C++
Abstract: Aspose.PDF for Rust via C++ offers comprehensive functionality to save PDF documents in various formats and locations with high efficiency and flexibility. The library allows developers to save PDFs to file systems, and memory streams, or output them in alternative formats such as DOCX, XLSX, and images. It provides options to customize saving parameters, optimize file size, and ensure data integrity. The documentation includes detailed instructions and code samples to help developers efficiently implement PDF-saving capabilities in their applications.
SoftwareApplication: rust-cpp       
---

## Save PDF document to file system

The example demonstrates the [new](https://reference.aspose.com/pdf/rust-cpp/core/new/) method for creating a new PDF document, which is a fundamental feature for generating documents dynamically, such as reports or invoices.

The code is simple and can act as a template for more advanced features like adding text, images, or annotations to the PDF.

This example demonstrates the straightforward use of the Aspose.PDF Rust library, showcasing its potential for creating, modifying, and saving documents.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_new.pdf")?;

        Ok(())
    }
```
