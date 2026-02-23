---
title: Get Permissions using Rust
linktitle: Get Permissions
type: docs
weight: 60
url: /rust-cpp/get-permissions/
description: Read and display the access permissions of a password-protected PDF document with Aspose.PDF for Rust via C++.
lastmod: "2026-01-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Get permissions of a password-protected PDF document

This section explains how to read and display the access permissions of a password-protected PDF document in Rust.
The PDF is opened with the owner password, which grants full access to the document’s security settings. The currently assigned permissions are then retrieved and printed to the console.

1. Open the protected PDF document.
1. Call [get_permissions](https://reference.aspose.com/pdf/rust-cpp/security/get_permissions/) to obtain the permission flags that define which operations are allowed.
1. Print the retrieved permissions to the console.

```rs

    use asposepdf::{Document, Permissions};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a password-protected PDF-document
        let pdf = Document::open_with_password("sample_with_permissions.pdf", "ownerpass")?;

        // Get current permissions of PDF-document
        let permissions: Permissions = pdf.get_permissions()?;

        // Print permissions
        println!("Permissions: {}", permissions);

        Ok(())
    }
```