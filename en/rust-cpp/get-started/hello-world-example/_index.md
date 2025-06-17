---
title: Example of Hello World using Rust language
linktitle: Hello World Example
type: docs
weight: 40
url: /rust-cpp/hello-world-example/
description: This sample demonstrates how to create a simple PDF document with text Hello World using Aspose.PDF for Rust.
lastmod: "2024-12-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hello World via Aspose.PDF for Rust
Abstract: The Get Started guide for Aspose.PDF for Rust via C++ provides an introduction to working with the library, covering the basic steps to create and manipulate PDF documents. It includes a 'Hello World' example demonstrating how to generate a simple PDF file with text content, helping developers quickly understand the API's core functionality. 
SoftwareApplication: rust-cpp   
---

A "Hello World" example is traditionally used to introduce features of a programming language or software with a simple use case.

**Aspose.PDF for Rust** is a feature-rich PDF API that allows developers to embed PDF document creation, manipulation, and conversion capabilities with Rust. It supports many popular file formats, including PDF, TXT, XLSX, EPUB, TEX, DOC, DOCX, PPTX, image formats etc. In this article, we are creating a PDF document containing the text "Hello World!" After installing Aspose.PDF for Rust in your environment, you can execute the code sample to see how the Aspose.PDF API works.
Below code snippet follows these steps:

1. Create a new PDF document instance.
1. Add a new page to the PDF document using [page_add](https://reference.aspose.com/pdf/rust-cpp/core/page_add/) function.
1. Set the page size using [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/).
1. Add "Hello World!" text to the first page using [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/).
1. Save the repaired PDF document using [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) method.
1. Close the PDF document and release any allocated resources.

Following code snippet is a Hello World program to exhibit working of Aspose.PDF for Rust API.

```rs

    use asposepdf::{Document, PageSize};
    use std::error::Error;

    fn main() -> Result<(), Box<dyn Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Add a new page
        pdf.page_add()?;

        // Set the size of the first page to A4
        pdf.page_set_size(1, PageSize::A4)?;

        // Add "Hello World!" text to the first page
        pdf.page_add_text(1, "Hello World!")?;

        // Save the PDF-document as "hello.pdf"
        pdf.save_as("hello.pdf")?;

        println!("Saved PDF-document: hello.pdf");

        Ok(())
}
```
