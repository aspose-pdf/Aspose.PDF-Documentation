---
title: Add Text to PDF using Rust
linktitle: Add Text to PDF
type: docs
weight: 10
url: /rust-cpp/add-text-to-pdf-file/
description: Learn how to add text to a PDF document in Rust using Aspose.PDF for content enhancement and document editing.
lastmod: "2025-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: Add Text into PDF using Aspose.PDF for Rust
Abstract: The Add Text to PDF File section of the Aspose.PDF for C++ and Rust documentation provides step-by-step instructions on inserting text into PDF documents programmatically. It covers various methods for adding text, including positioning, font customization, color adjustments, and text alignment options. The guide demonstrates how to add text to specific pages and locations within a PDF, ensuring precise content placement. With detailed code examples and explanations, developers can easily integrate text insertion features into their applications for enhanced PDF document management.
SoftwareApplication: rust-cpp      
---

To add text to existing PDF file:

1. Open a PDF file.
1. Add the text to the PDF document with [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/) function.
1. Saves the modifications to the same file.

## Adding Text

The following code snippet shows you how to add text in an existing PDF file.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Add text on page
        pdf.page_add_text(1, "added text")?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```
