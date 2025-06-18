---
title: Open PDF document programmatically
linktitle: Open PDF
type: docs
weight: 20
url: /rust-cpp/open-pdf-document/
description: Learn how to open a PDF file with Aspose.PDF for Rust via C++.
lastmod: "2025-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Open PDF document with Aspose.PDF for Rust via C++
Abstract: Aspose.PDF for Rust via C++ provides powerful functionality to open and load PDF documents programmatically, allowing developers to access and manipulate PDF content with ease. The library supports opening PDF files from various sources, such as file paths and memory streams, while ensuring efficient processing and resource management. It offers features to inspect document properties, extract text and images, and perform other operations on loaded PDFs. The documentation includes detailed instructions and code samples to help developers integrate PDF opening capabilities into their applications seamlessly.
SoftwareApplication: rust-cpp      
---

## Open existing PDF document

The code snippet demonstrates essential operations for working with PDFs using Aspose.PDF for Rust. These are opening a file, saving changes, and properly closing resources. This makes it a foundational example for developers handling PDF documents.

The example is straightforward, making it easy to understand and modify. It's ideal for beginners or as a boilerplate for more complex applications.

The ability to open and save PDF documents is a core requirement in many scenarios, such as generating reports, modifying documents, or creating automated workflows.

This example showcases the API's ease of use for simple PDF manipulation, which can be expanded to include advanced features like text extraction, annotation, or form filling.

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
