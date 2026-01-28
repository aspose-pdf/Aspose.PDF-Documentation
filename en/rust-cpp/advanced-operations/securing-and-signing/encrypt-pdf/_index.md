---
title:  Encrypt PDF using Rust
linktitle: Encrypt PDF File
type: docs
weight: 10
url: /rust-cpp/encrypt-pdf/
description: Encrypt PDF File with Aspose.PDF for Rust via C++.
lastmod: "2026-01-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Encrypt PDF File using using User or Owner Password

To easily and securely encrypt documents, you can use Aspose.PDF for Rust via C++.

- The **user_password**, if set, is what you need to provide in order to open a PDF. Acrobat/Reader will prompt a user to enter the user password. If it's not correct, the document will not open.
- The **owner_password**, if set, controls permissions, such as printing, editing, extracting, commenting, etc. Acrobat/Reader will disallow these things based on the permission settings. Acrobat will require this password if you want to set/change permissions.

The PDF is protected with both user and owner passwords, specific access permissions, and AES-128 encryption compliant with PDF 2.0 standards. Once encrypted, the document is saved to disk, ensuring controlled access and secure handling of the PDF file.

1. Create a new PDF document.
1. Encrypt the PDF document with [encrypt](https://reference.aspose.com/pdf/rust-cpp/security/encrypt/) method.
1. Specify a user password to restrict opening the document.
1. Specify an owner password to control permissions.
1. Define allowed actions using a permissions bitmask.
1. Choose AES-128 as the encryption algorithm.
1. Enable PDF 2.0 encryption for modern security compliance.
1. Save the encrypted PDF using [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/). 

```rs

  use asposepdf::{CryptoAlgorithm, Document, Permissions};

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Create a new PDF-document
      let pdf = Document::new()?;

      // Encrypt PDF-document
      pdf.encrypt(
          "userpass",  // User password
          "ownerpass", // Owner password
          Permissions::PRINT_DOCUMENT | Permissions::MODIFY_CONTENT | Permissions::FILL_FORM, // Permissions bitmask
          CryptoAlgorithm::AESx128, // Encryption algorithm
          true,                     // Use PDF 2.0 encryption
      )?;

      // Save the encrypted PDF-document
      pdf.save_as("sample_with_password.pdf")?;

      Ok(())
  }
```