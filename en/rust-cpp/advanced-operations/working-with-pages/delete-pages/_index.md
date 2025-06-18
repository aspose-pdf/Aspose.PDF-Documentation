---
title: Delete PDF Pages with Rust via C++ 
linktitle: Delete PDF Pages
type: docs
weight: 30
url: /rust-cpp/delete-pages/
description: You can delete pages from your PDF file using Aspose.PDF for Rust via C++.
lastmod: "2025-06-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Delete PDF Pages with Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ offers efficient functionality to delete pages from PDF documents, enabling developers to remove unwanted or unnecessary pages with ease. The library allows for the deletion of single or multiple pages by specifying page numbers or ranges, ensuring precise document modifications. This feature helps streamline PDF files by eliminating redundant content and optimizing document structure. The documentation provides step-by-step instructions and code samples to assist developers in implementing page deletion functionality effectively within their applications.
SoftwareApplication: rust-cpp    
---

You can delete pages from a PDF file using **Aspose.PDF for Rust via C++**. The next code snippet demonstrates how to manipulate a PDF document by deleting a specific page. This method is efficient for PDF document manipulation tasks, specifically for removing pages, saving the modified document, and ensuring proper resource management.

1. Opening a PDF File.
1. Deleting a Specific Page with [page_delete](https://reference.aspose.com/pdf/rust-cpp/core/page_delete/) function.
1. Saving the Document using [save](https://reference.aspose.com/pdf/rust-cpp/core/save/) method.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Delete specified page in PDF-document
        pdf.page_delete(1)?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```
