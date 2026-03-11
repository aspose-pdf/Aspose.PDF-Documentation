---
title: Add watermark to PDF using Rust
linktitle: Add watermark
type: docs
weight: 80
url: /rust-cpp/add-watermarks/
description: This example demonstrates how to add a customizable text watermark to a PDF document using Aspose.PDF for Rust via C++.
lastmod: "2026-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Add Text Watermark 
Abstract: Aspose.PDF for Rust via C++ provides a flexible way to add text watermarks to PDF documents. This example demonstrates how to insert a customizable watermark by specifying text content, font, size, color, position, rotation angle, layering behavior, and transparency. Watermarks are commonly used for branding, confidentiality labels, draft markings, or document protection.
SoftwareApplication: rust-cpp       
---

The [add_watermark](https://reference.aspose.com/pdf/rust-cpp/organize/add_watermark/) method allows developers to programmatically apply a text watermark to an existing PDF document. The watermark can be fully customized, including:

- Watermark text
- Font family
- Font size
- Text color (HEX format)
- X and Y position coordinates
- Rotation angle
- Foreground or background placement
- Opacity (transparency level)

In this example, the application opens an existing PDF file, applies a semi-transparent rotated watermark, and saves the modified document under a new file name.

This functionality is particularly useful for marking documents as Draft, Confidential, Sample, or for adding branding elements before distribution.

1. Open the existing PDF document.
1. Call the add_watermark method and configure the watermark properties.
1. Save the updated document.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add watermark to PDF-document
        pdf.add_watermark(
            "WATERMARK",
            "Arial",
            16.0,
            "#010101",
            100,
            100,
            45,
            true,
            0.5,
        )?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_watermark.pdf")?;

        Ok(())
    }
```