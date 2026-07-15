---
title: Получить разрешения с использованием Go
linktitle: Получить разрешения
type: docs
weight: 60
url: /ru/go-cpp/get-permissions/
description: Считать и отобразить разрешения доступа к защищённому паролем PDF‑документу с помощью Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Получить разрешения защищённого паролем PDF‑документа

Этот пример демонстрирует, как извлечь, интерпретировать и отобразить разрешения доступа из защищённого паролем PDF‑документа в Go с использованием Aspose.PDF for Go via C++.
PDF открывается с паролем владельца, его флаги разрешений читаются, и каждое включённое разрешение преобразуется в человекочитаемое описание перед выводом в консоль.

1. Определите сопоставления имён разрешений.
1. Преобразуйте флаги разрешений в читаемый текст.
1. Используйте [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) с паролем владельца, чтобы получить доступ к информации о защите документа.
1. Обеспечьте корректную очистку ресурсов.
1. Вызовите [GetPermissions](https://reference.aspose.com/pdf/go-cpp/security/getpermissions/) для получения текущего битового флага разрешений, назначенного PDF.
1. Отобразите разрешения.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import (
        "fmt"
        "log"
        "strings"
    )

    var permissionNames = map[asposepdf.Permissions]string{
        asposepdf.PrintDocument:                  "Allow printing",
        asposepdf.ModifyContent:                  "Allow modifying content (except forms/annotations)",
        asposepdf.ExtractContent:                 "Allow copying/extracting text and graphics",
        asposepdf.ModifyTextAnnotations:          "Allow adding/modifying text annotations",
        asposepdf.FillForm:                       "Allow filling interactive forms",
        asposepdf.ExtractContentWithDisabilities: "Allow content extraction for accessibility",
        asposepdf.AssembleDocument:               "Allow inserting/rotating/deleting pages or changing structure",
        asposepdf.PrintingQuality:                "Allow high-quality / faithful printing",
    }

    func PermissionsToString(p asposepdf.Permissions) string {
        var result []string
        for flag, name := range permissionNames {
            if p&flag != 0 {
                result = append(result, name)
            }
        }
        if len(result) == 0 {
            return "None"
        }
        return strings.Join(result, ", ")
    }

    func main() {
        // OpenWithPassword(filename string, password string) opens a password-protected PDF-document
        pdf, err := asposepdf.OpenWithPassword("sample_with_permissions.pdf", "ownerpass")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
        // GetPermissions() gets current permissions of PDF-document
        permissions, err := pdf.GetPermissions()
        if err != nil {
            log.Fatal(err)
        }
        // Print permissions
        fmt.Println("Permissions:", PermissionsToString(permissions))
    }
```
