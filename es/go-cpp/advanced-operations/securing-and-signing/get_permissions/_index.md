---
title: Obtener permisos usando Go
linktitle: Obtener permisos
type: docs
weight: 60
url: /es/go-cpp/get-permissions/
description: Leer y mostrar los permisos de acceso de un documento PDF protegido con contraseña con Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Obtener permisos de un documento PDF protegido con contraseña

Este ejemplo muestra cómo recuperar, interpretar y mostrar los permisos de acceso de un documento PDF protegido con contraseña en Go usando Aspose.PDF for Go via C++.
El PDF se abre con la contraseña de propietario, sus indicadores de permiso se leen, y cada permiso habilitado se convierte en una descripción legible por humanos antes de imprimirse en la consola.

1. Definir asignaciones de nombres de permisos.
1. Convertir indicadores de permisos a texto legible.
1. Usar [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) con la contraseña del propietario para obtener acceso a la información de seguridad del documento.
1. Asegurar la limpieza adecuada de recursos.
1. Llamar [GetPermissions](https://reference.aspose.com/pdf/go-cpp/security/getpermissions/) para obtener la bandera de bits de permiso actual asignada al PDF.
1. Mostrar los permisos.

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