---
title: Adding Header and Footer to PDF using Rust
linktitle: Adding Header and Footer to PDF
type: docs
weight: 90
url: /rust-cpp/add-headers-and-footers-of-pdf-file/
description: 
lastmod: "2026-02-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to add Header and Footer to PDF using Rust
Abstract: This article demonstrates how to add text headers and footers to PDF documents using the asposepdf Rust library. It explains how to open an existing PDF, insert consistent text into the header or footer of every page, and save the modified document as a new file. The examples showcase a simple, error-safe workflow that can be used for tasks such as adding page numbers, titles, or branding programmatically in Rust applications.
SoftwareApplication: rust-cpp 
---

## Adding Headers and Footers as Text Fragments

### Add text in Footer of a PDF-document

Our tool lets you open an existing PDF, add a text footer to all pages, and save the modified PDF as a new file using the asposepdf Rust library. It handles errors gracefully with Rust’s Result type.

1. Open an existing PDF document.
1. Add text to the footer with [add_text_footer](https://reference.aspose.com/pdf/rust-cpp/organize/add_text_footer/).
1. Save the modified PDF.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add text in Footer of a PDF-document
        pdf.add_text_footer("FOOTER")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_text_footer.pdf")?;

        Ok(())
    }
```

### Add text in Header of a PDF-document

This code snippet demonstrates how to open an existing PDF file, add a text header to all pages, and save the modified document as a new file using the asposepdf library. It provides a simple, automated way to insert consistent headers into PDFs.

1. Open an existing PDF.
1. Add text to the Header with helps [add_text_header](https://reference.aspose.com/pdf/rust-cpp/organize/add_text_header/).
1. Save the modified PDF.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add text in Header of a PDF-document
        pdf.add_text_header("HEADER")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_text_header.pdf")?;

        Ok(())
    }
```