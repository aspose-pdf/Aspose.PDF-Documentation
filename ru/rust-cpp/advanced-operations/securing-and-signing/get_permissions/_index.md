---
title: Получить разрешения с помощью Rust
linktitle: Получить разрешения
type: docs
weight: 60
url: /ru/rust-cpp/get-permissions/
description: Прочитать и отобразить разрешения доступа к защищенному паролем PDF-документу с помощью Aspose.PDF for Rust через C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Получить разрешения защищенного паролем PDF-документа

В этом разделе объясняется, как в Rust прочитать и отобразить разрешения доступа к защищенному паролем PDF-документу.
PDF открывается с паролем владельца, который предоставляет полный доступ к настройкам безопасности документа. Затем текущие назначенные разрешения извлекаются и выводятся в консоль.

1. Откройте защищённый PDF‑документ.
1. Вызов [get_permissions](https://reference.aspose.com/pdf/rust-cpp/security/get_permissions/) чтобы получить флаги разрешений, определяющие, какие операции разрешены.
1. Выведите полученные разрешения в консоль.

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