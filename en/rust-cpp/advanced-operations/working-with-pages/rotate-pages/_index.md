---
title: Rotate PDF Pages with Rust via C++ 
linktitle: Rotate PDF Pages
type: docs
weight: 50
url: /rust-cpp/rotate-pages/
description: This topic describes how to rotate the page orientation in an existing PDF file programmatically with Rust via C++ 
lastmod: "2025-06-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rotate PDF Pages with Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ provides robust functionality to rotate pages in PDF documents, allowing developers to modify page orientation as needed. The library supports rotating pages by 90, 180, or 270 degrees, enabling quick and efficient adjustments to document layout. This feature is useful for correcting misoriented pages or altering the document’s presentation. The documentation includes step-by-step instructions and code samples to help developers seamlessly integrate page rotation capabilities into their applications.
SoftwareApplication: rust-cpp    
---

This section describes how to change the page orientation from landscape to portrait and vice versa in an existing PDF file using Rust via C++.

Rotating pages ensures proper alignment for printing or displaying PDFs in professional settings

1. Open the PDF Document.
1. Rotate PDF Pages. The [rotate](https://reference.aspose.com/pdf/rust-cpp/organize/rotate/) function applies a specific rotation (in this case, 180 degrees) to a given page.
1. Save Changes to a New File. The [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) function creates a new PDF file to preserve the original while storing the updated version.

In this example, you rotate a specific page in a PDF document:

```rs

    use asposepdf::{Document, Rotation};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Rotate PDF-document
        pdf.rotate(Rotation::On270)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_rotate.pdf")?;

        Ok(())
    }
```