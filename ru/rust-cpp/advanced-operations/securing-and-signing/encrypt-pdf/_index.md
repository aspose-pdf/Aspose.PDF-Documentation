---
title:  Зашифровать PDF с помощью Rust
linktitle: Зашифровать файл PDF
type: docs
weight: 10
url: /ru/rust-cpp/encrypt-pdf/
description: Зашифровать файл PDF с помощью Aspose.PDF for Rust через C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Зашифровать файл PDF, используя пользовательский или пароль владельца

Для простого и безопасного шифрования документов вы можете использовать Aspose.PDF for Rust через C++.

- **user_password**, если задан, — это то, что нужно предоставить, чтобы открыть PDF. Acrobat/Reader попросит пользователя ввести пользовательский пароль. Если он неверен, документ не откроется.
- Пароль **owner_password**, если установлен, управляет разрешениями, такими как печать, редактирование, извлечение, комментирование и т.д. Acrobat/Reader будет запрещать эти действия в соответствии с настройками разрешений. Acrobat потребует этот пароль, если вы хотите установить/изменить разрешения.

PDF защищён как пользовательским, так и паролем владельца, определёнными разрешениями доступа и шифрованием AES-128 в соответствии со стандартом PDF 2.0. После шифрования документ сохраняется на диск, обеспечивая контролируемый доступ и безопасную работу с файлом PDF.

1. Создайте новый PDF‑документ.
1. Зашифруйте PDF‑документ с помощью [зашифровать](https://reference.aspose.com/pdf/rust-cpp/security/encrypt/) метод.
1. Укажите пароль пользователя, чтобы ограничить открытие документа.
1. Укажите пароль владельца для управления разрешениями.
1. Определите разрешённые действия, используя битовый флаг разрешений.
1. Выберите AES-128 в качестве алгоритма шифрования.
1. Включите шифрование PDF 2.0 для соответствия современным требованиям безопасности.
1. Сохраните зашифрованный PDF, используя [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/). 

```rs

  use asposepdf::{CryptoAlgorithm, Document, Permissions};

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Create a new PDF-document
      let pdf = Document::new()?;

      // Encrypt PDF-document
      pdf.encrypt(
          "userpass",  // User password
          "ownerpass", // Owner password
          Permissions::PRINT_DOCUMENT | Permissions::MODIFY_CONTENT | Permissions::FILL_FORM, // Permissions bitflag
          CryptoAlgorithm::AESx128, // Encryption algorithm
          true,                     // Use PDF 2.0 encryption
      )?;

      // Save the encrypted PDF-document
      pdf.save_as("sample_with_password.pdf")?;

      Ok(())
  }
```