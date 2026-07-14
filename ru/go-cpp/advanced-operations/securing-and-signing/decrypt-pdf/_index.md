---
title: Расшифровать PDF с помощью Go
linktitle: Расшифровать PDF-файл
type: docs
weight: 40
url: /ru/go-cpp/decrypt-pdf/
description: Расшифровать PDF-файл с помощью Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Расшифровать PDF-файл используя пароль владельца

Вы можете открыть, расшифровать и сохранить защищённый паролем PDF‑документ с помощью Aspose.PDF for Go via C++. PDF‑файл открывается с паролем владельца, расшифровывается для снятия всех ограничений безопасности и затем сохраняется как новый, незащищённый документ.

1. Вызовите [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) и укажите имя файла вместе с паролем владельца для доступа к зашифрованному PDF.
1. Вызовите [Decrypt](https://reference.aspose.com/pdf/go-cpp/security/decrypt/) метод для снятия защиты паролем и всех связанных с ней ограничений безопасности из документа.
1. Сохраните расшифрованный PDF, используя [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // OpenWithPassword(filename string, password string) opens a password-protected PDF-document
        pdf, err := asposepdf.OpenWithPassword("sample_with_password.pdf", "ownerpass")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
        // Decrypt() decrypts PDF-document
        err = pdf.Decrypt()
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_without_password.pdf")
        if err != nil {
            log.Fatal(err)
        }
    }
```