---
title: Откройте PDF, защищённый паролем, с использованием Go
linktitle: Откройте PDF, защищённый паролем
type: docs
weight: 70
url: /ru/go-cpp/open-password-protected-pdf/
description: Откройте PDF‑файл, защищённый паролем, с помощью Aspose.PDF for Go через C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Откройте PDF‑документ, защищённый паролем

Этот фрагмент кода объясняет, как открыть PDF‑документ, защищённый паролем, с помощью Aspose.PDF for Go через C++. Документ открывается с паролем владельца, который предоставляет полный доступ и позволяет выполнять дальнейшие операции, такие как чтение метаданных, проверка прав, расшифровка файла или изменение содержимого.

1. Откройте защищённый PDF‑документ.
1. Вызов [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) и укажите имя файла вместе с паролем владельца, чтобы разблокировать документ.
1. Используйте 'defer pdf.Close()', чтобы освободить все выделенные ресурсы после завершения обработки.
1. После открытия документа вы можете продолжить выполнение дополнительных задач, таких как расшифровка PDF, изменение разрешений или извлечение информации.

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
        // working...
    }
```