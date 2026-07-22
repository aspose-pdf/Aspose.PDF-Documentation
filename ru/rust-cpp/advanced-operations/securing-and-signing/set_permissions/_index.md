---
title: Установить разрешения для PDF‑документа с использованием Rust
linktitle: Установить разрешения
type: docs
weight: 80
url: /ru/rust-cpp/set_permissions/
description: Установить разрешения для PDF‑документа с помощью Aspose.PDF для Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Установите права доступа для PDF‑документа

Создаётся новый PDF‑документ, защищённый пользовательским и владельцем паролями, при этом явно разрешаются определённые действия — такие как печать, изменение содержимого и заполнение форм. Затем документ сохраняется с применёнными определёнными ограничениями разрешений.

1. Создайте новый PDF‑документ.
1. Вызовите [set_permissions](https://reference.aspose.com/pdf/rust-cpp/security/set_permissions/) для защиты документа.
1. Укажите пароль пользователя для ограничения доступа.
1. Укажите пароль владельца для управления настройками безопасности.
1. Определите разрешённые операции с помощью битового флага разрешений.
1. Сохраните PDF с примененными разрешениями, используя [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

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
