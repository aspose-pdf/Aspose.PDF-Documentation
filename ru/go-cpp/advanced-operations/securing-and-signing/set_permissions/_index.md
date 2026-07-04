---
title: Установить разрешения для PDF‑документа с использованием Go
linktitle: Установить разрешения
type: docs
weight: 80
url: /ru/go-cpp/set_permissions/
description: Установить разрешения для PDF‑документа с помощью Aspose.PDF for Go через C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Установить разрешения доступа для PDF‑документа

Создаётся новый PDF‑документ, защищённый пользовательским и владельским паролями, при этом конкретные разрешения — такие как печать, изменение содержимого и заполнение форм — явно разрешены. Затем документ сохраняется с применёнными этими ограничениями разрешений.

1. Создайте новый PDF‑документ.
1. Вызовите [SetPermissions](https://reference.aspose.com/pdf/go-cpp/security/setpermissions/) для защиты документа.
1. Укажите пароль пользователя, чтобы ограничить доступ.
1. Укажите пароль владельца, чтобы управлять настройками безопасности.
1. Определите разрешённые операции, используя битовый флаг разрешений.
1. Сохраните PDF с применёнными разрешениями, используя [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

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

        // SetPermissions(userPassword, ownerPassword, permissions) sets permissions for PDF-document
        err = pdf.SetPermissions(
            "userpass",
            "ownerpass",
            asposepdf.PrintDocument|
                asposepdf.ModifyContent|
                asposepdf.FillForm,
        )
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_with_permissions.pdf")
        if err != nil {
            log.Fatal(err)
        }
    }
```
