---
title: Extract Data from AcroForm using Rust
linktitle: Extract Data from AcroForm
type: docs
weight: 50
url: /rust-cpp/extract-data-from-acroform/
description: Aspose.PDF makes it easy to extract form field data from PDF files. Learn how to extract data from AcroForms and save it into XML, FDF or XFDF format.
lastmod: "2026-02-02"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Extract Data from AcroForm via Rust
Abstract: This article explains how to extract AcroForm data from PDF files using Aspose.PDF for Rust via C++ and export it into widely used data exchange formats - XML, FDF, and XFDF. It demonstrates how to open a PDF document containing interactive form fields and programmatically export form field names and values for reuse outside the original PDF. By providing practical Rust examples for each export format, the article highlights common workflows, including data processing, form submission, system integration, and long-term data storage, helping developers efficiently manage and reuse PDF form data in their applications.
---

## Extract Data to XML from a PDF File

This code snippet shows how to export AcroForm data from a PDF document to an XML file using Aspose.PDF for Rust.
The process involves opening an existing PDF file with form fields, then exporting those fields and their values to an XML document for further processing, storage, or data exchange.

1. Open the PDF document.
1. Call the 'export_xml' method to extract the form field data and save it as an XML file.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XML-document
        pdf.export_xml("sample.xml")?;

        Ok(())
    }
```

## Export Data to FDF from a PDF File

Aspose.PDF for Rust via C++ allows you to export AcroForm data from a PDF document to an FDF file. The Forms Data Format (FDF) file stores form field names and values separately from the PDF, making it useful for data exchange, form submission workflows, and archiving form data without embedding it in the original document.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to FDF-document
        pdf.export_fdf("sample.fdf")?;

        Ok(())
    }
```

## Export Data to XFDF from a PDF File

XFDF (XML Forms Data Format) is an XML-based format that represents form field data separately from the PDF file, making it ideal for data interchange, form submissions, and integration with web-based workflows.
Aspose.PDF for Rust via C++ helps to export AcroForm data from a PDF document to an XFDF file.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XFDF-document
        pdf.export_xfdf("sample.xfdf")?;

        Ok(())
    }
```
