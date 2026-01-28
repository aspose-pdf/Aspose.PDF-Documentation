---
title: Extract Text from PDF using Rust
linktitle: Extract text from PDF
type: docs
weight: 30
url: /rust-cpp/extract-text-from-pdf/
description: This article describes various ways to extract text from PDF documents using Aspose.PDF for Rust. 
lastmod: "2025-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extract Text with Aspose.PDF for Rust 
Abstract: Aspose.PDF for Rust via C++ provides a powerful and efficient way to extract text from PDF documents. The library supports multiple extraction techniques, allowing users to retrieve text from entire documents, specific pages, or predefined areas within a PDF.
SoftwareApplication: rust-cpp         
---

## Extract Text From PDF Document

Extracting text from the PDF document is a very common and useful task. PDFs often contain critical information that needs to be accessed, analyzed, or processed for various purposes. Extracting text enables easier reuse in databases, reports, or other documents.

Extracting text makes PDF content searchable, allowing users to locate specific information quickly without manually reviewing the entire document.

In case you want to extract text from PDF document, you can use [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) function.
Please check following code snippet in order to extract text from PDF file using Rust.

1. Open a PDF document with the given filename.
1. [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) extracts the text content from the PDF document.
1. Print the extracted text to the console.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Return the PDF-document contents as plain text
        let txt = pdf.extract_text()?;

        // Print extracted text
        println!("Extracted text:\n{}", txt);

        Ok(())
    }
```