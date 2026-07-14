---
title:  Зашифровать PDF с помощью Go
linktitle: Зашифровать PDF‑файл
type: docs
weight: 10
url: /ru/go-cpp/encrypt-pdf/
description: Зашифровать PDF‑файл с помощью Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Зашифровать PDF‑файл, используя using пароль пользователя или владельца

Чтобы легко и надёжно зашифровать документы, вы можете использовать Aspose.PDF for Go via C++.

- **userPassword**, если установлен, — это то, что вам нужно предоставить для открытия PDF. Acrobat/Reader предложит пользователю ввести пароль пользователя. Если он неверный, документ не откроется.
- **ownerPassword**- устанавливается для контроля разрешений, такие как печать, редактирование, извлечение, комментирование и т.д. Acrobat/Reader будет запрещать эти действия в зависимости от настроек разрешений. Acrobat потребует этот пароль, если вы хотите установить/изменить разрешения.

PDF защищён пользовательским и владельским паролями, настроенными с определёнными разрешениями доступа, и зашифрован с использованием алгоритма AES-128 с безопасностью, совместимой с PDF 2.0–compatible security. Зашифрованный документ затем сохраняется на диск.

1. Создайте новый PDF‑документ.
1. Зашифруйте PDF‑документ с помощью метода [encrypt](https://reference.aspose.com/pdf/go-cpp/security/encrypt/).
1. Укажите пароль пользователя, чтобы ограничить открытие документа.
1. Укажите пароль владельца для управления разрешениями.
1. Определите разрешённые действия, используя битовый флаг разрешений.
1. Выберите AES-128 в качестве алгоритма шифрования.
1. Включите шифрование PDF 2.0 для обеспечения современной безопасности.
1. Сохраните защищённый документ, используя [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/), записывая его в новый файл.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // New creates a new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
        // Encrypt(userPassword, ownerPassword, permissions, cryptoAlgorithm, usePdf20) encrypts PDF-document
        err = pdf.Encrypt(
            "userpass",
            "ownerpass",
            asposepdf.PrintDocument|asposepdf.ModifyContent|asposepdf.FillForm,
            asposepdf.AESx128,
            true,
        )
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_with_password.pdf")
        if err != nil {
            log.Fatal(err)
        }
    }
```
