---
title: Adding Page Number to PDF with Rust
linktitle: Adding Page Number
type: docs
weight: 10
url: /rust-cpp/add-page-number/
description: This article demonstrates how to add page numbers to an existing PDF document using Aspose.PDF for Rust via C++.
lastmod: "2026-02-23"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adding Page Numbers
Abstract: Aspose.PDF for Rust via C++ enables developers to enhance existing PDF documents with automatic page numbering in just a few lines of code. This example demonstrates how to open a PDF file, insert page numbers across all pages, and save the updated document as a new file. Automating pagination ensures consistent document structure and is particularly useful for reports, contracts, manuals, and other multi-page outputs prepared for distribution or printing.
SoftwareApplication: rust-cpp    
---

Aspose.PDF for Rust via C++ provides built-in functionality to modify PDF documents programmatically. In this example, the application opens an existing PDF file, applies automatic page numbering to every page, and saves the modified document under a new name.

This approach is useful when generating finalized documents for distribution, printing, or archival purposes. The process requires only a few lines of code and does not alter the original file unless explicitly overwritten.

Page numbering is a common requirement for reports, invoices, contracts, manuals, and other multi-page documents. The [add_page_num()](https://reference.aspose.com/pdf/rust-cpp/organize/add_page_num/) method automatically inserts page numbers into all pages of the document, ensuring consistent pagination across the file.

After adding page numbers, the updated document is saved as a new PDF file.

1. Open the existing PDF document.
1. Add page numbers with [add_page_num()](https://reference.aspose.com/pdf/rust-cpp/organize/add_page_num/) method.
1. Save the updated document.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add page number to a PDF-document
        pdf.add_page_num()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_page_num.pdf")?;

        Ok(())
    }
```