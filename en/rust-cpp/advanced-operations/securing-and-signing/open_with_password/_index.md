---
title: Open a password-protected PDF using Rust
linktitle: Open a password-protected PDF
type: docs
weight: 70
url: /rust-cpp/open-password-protected-pdf/
description: Open a password-protected PDF File with Aspose.PDF for Rust via C++.
lastmod: "2026-01-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Open a password-protected PDF document

Open a password-protected PDF document with Aspose.PDF for Rust via C++. The document is opened with the owner's password, which grants full access and allows further operations such as reading metadata, modifying content, changing permissions, or removing encryption.

1. Open the protected PDF document with [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) and provide the file path along with the owner password to unlock the document.
1. Work with the opened document.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a password-protected PDF-document
        let _pdf = Document::open_with_password("sample_with_password.pdf", "ownerpass")?;

        // working...

        Ok(())
    }
```