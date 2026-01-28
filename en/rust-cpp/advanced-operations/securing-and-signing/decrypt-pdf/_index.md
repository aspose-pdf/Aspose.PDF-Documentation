---
title: Decrypt PDF using Rust
linktitle: Decrypt PDF File
type: docs
weight: 40
url: /rust-cpp/decrypt-pdf/
description: Decrypt PDF File with Aspose.PDF for Rust via C++.
lastmod: "2026-01-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Decrypt PDF File using Owner Password

You can open, decrypt, and save a password-protected PDF document using Aspose.PDF for Rust via C++.
The PDF is opened with the owner password, decrypted to remove all security restrictions, and then saved as a new, unprotected PDF.

1. Use [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) to load a password-protected PDF by supplying the file path and the owner password.
1. Call the [decrypt](https://reference.aspose.com/pdf/rust-cpp/security/decrypt/) method to remove password protection and all associated security restrictions from the document.
1. Save the decrypted PDF using [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a password-protected PDF-document
      let pdf = Document::open_with_password("sample_with_password.pdf", "ownerpass")?;

      // Decrypt PDF-document
      pdf.decrypt()?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_decrypt.pdf")?;

      Ok(())
  }
```