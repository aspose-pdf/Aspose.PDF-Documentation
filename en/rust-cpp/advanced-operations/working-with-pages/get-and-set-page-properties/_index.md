---
title: Get and Set Page Properties
type: docs
url: /rust-cpp/get-and-set-page-properties/
description: Learn how to get and set page properties for PDF documents using Aspose.PDF for Rust, allowing for customized document formatting.
lastmod: "2025-06-13"
TechArticle: true
AlternativeHeadline: Get and Set Page Properties with Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ provides comprehensive features to get and set page properties in PDF documents, allowing developers to access and modify various page attributes such as size, rotation, margins, and metadata. These capabilities enable precise control over the document layout and appearance to meet specific application requirements. The library ensures seamless customization and optimization of PDF pages. The documentation offers detailed guidance and code samples to help developers efficiently retrieve and update page properties within their applications.
SoftwareApplication: rust-cpp 
---


Aspose.PDF for Rust lets you read and set properties of pages in a PDF file. This section shows how to get the number of pages in a PDF file, get information about PDF page properties such as color and set page properties.

## Get Number of Pages in a PDF File

When working with documents, you often want to know how many pages they contain. With Aspose.PDF this takes no more than two lines of code.

**Aspose.PDF for Rust via C++** allows you to count Pages with [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) function.

The next code snippet is designed to open a PDF document, retrieve its page count, and then print the result.

The [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) method is called to get the total number of pages in the PDF document. This is useful for tasks that need to know the length of the document, such as when extracting specific pages or performing operations across all pages. This method is a straightforward way to query the document’s structure.

To get the number of pages in a PDF file:

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document from file
      let pdf = Document::open("sample.pdf")?;

      // Return page count in PDF-document
      let count = pdf.page_count()?;

      // Print the page count
      println!("Count: {}", count);

      Ok(())
  }
```

## Set Page Size

In this example the method pdf.PageSetSize() changes the size of the first page of the PDF document. The PageSizeA1 constant ensures that the first page is set to the A1 paper size. This is useful when converting documents to a standardized format or ensuring that specific content fits correctly on pages.

1. Opening the PDF Document with [open](https://reference.aspose.com/pdf/rust-cpp/core/open/) method.
1. Setting the Page Size with [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/) function.
1. Saving the Document using [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) method.

```rs

    use asposepdf::{Document, PageSize};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set the size of a page in the PDF-document
        pdf.page_set_size(1, PageSize::A1)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_page1_set_size_A1.pdf")?;

        Ok(())
    }
```