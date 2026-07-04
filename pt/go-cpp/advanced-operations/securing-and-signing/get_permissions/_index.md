---
title: Obter permissões usando Go
linktitle: Obter permissões
type: docs
weight: 60
url: /pt/go-cpp/get-permissions/
description: Ler e exibir as permissões de acesso de um documento PDF protegido por senha com Aspose.PDF for Go via C\u002B\u002B.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Obter permissões de um documento PDF protegido por senha

Este exemplo demonstra como recuperar, interpretar e exibir as permissões de acesso de um documento PDF protegido por senha em Go usando Aspose.PDF for Go via C\u002B\u002B.
O PDF é aberto com a senha do proprietário, suas bandeiras de permissão são lidas e cada permissão habilitada é convertida em uma descrição legível antes de ser impressa no console.

1. Defina mapeamentos de nomes de permissões.
1. Converta sinalizadores de permissão em texto legível.
1. Usar [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) com a senha do proprietário para obter acesso às informações de segurança do documento.
1. Garanta a limpeza adequada dos recursos.
1. Chamar [GetPermissions](https://reference.aspose.com/pdf/go-cpp/security/getpermissions/) para obter o bitflag de permissão atual atribuído ao PDF.
1. Exibir as permissões.

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