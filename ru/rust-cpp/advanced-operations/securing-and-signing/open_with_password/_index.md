---
title: Откройте защищённый паролем PDF с использованием Rust
linktitle: Откройте защищённый паролем PDF
type: docs
weight: 70
url: /ru/rust-cpp/open-password-protected-pdf/
description: Откройте защищённый паролем файл PDF с помощью Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Откройте защищённый паролем PDF‑документ

Откройте защищённый паролем PDF‑документ с помощью Aspose.PDF for Rust via C++. Документ открывается с паролем владельца, который предоставляет полный доступ и позволяет выполнять дальнейшие операции, такие как чтение метаданных, изменение содержимого, изменение разрешений или удаление шифрования.

1. Откройте защищённый PDF‑документ с [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) и укажите путь к файлу вместе с паролем владельца, чтобы разблокировать документ.
1. Работайте с открытым документом.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a password-protected PDF-document
        let _pdf = Document::open_with_password("sample_with_password.pdf", "ownerpass")?;

        // working...

        Ok(())
    }
```