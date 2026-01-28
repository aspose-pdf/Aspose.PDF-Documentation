---
title: Set permissions for a PDF document using Rust
linktitle: Set permissions
type: docs
weight: 80
url: /rust-cpp/set_permissions/
description: Set permissions for a PDF document with Aspose.PDF for Rust via C++.
lastmod: "2026-01-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Set access permissions for a PDF document

A new PDF document is created and protected with user and owner passwords, while specific actions—such as printing, modifying content, and filling forms—are explicitly allowed. The document is then saved with the defined permission restrictions applied.

1. Create a new PDF document.
1. Call [set_permissions](https://reference.aspose.com/pdf/rust-cpp/security/set_permissions/) to protect the document.
1. Specify a user password to restrict access.
1. Specify an owner password to control security settings.
1. Define allowed operations using a permissions bitflag.
1. Save the PDF with permissions applied using [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

```rs

    use asposepdf::{Document, Permissions};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Set permissions for PDF-document.
        pdf.set_permissions(
            "userpass",  // User password
            "ownerpass", // Owner password
            Permissions::PRINT_DOCUMENT | Permissions::MODIFY_CONTENT | Permissions::FILL_FORM, // Permissions bitflag
        )?;

        // Save the PDF-document with the updated permissions
        pdf.save_as("sample_with_permissions.pdf")?;

        Ok(())
    }
```