---
title: Establecer permisos para un documento PDF usando Go
linktitle: Establecer permisos
type: docs
weight: 80
url: /es/go-cpp/set_permissions/
description: Establecer permisos para un documento PDF con Aspose.PDF for Go a través de C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Establecer permisos de acceso para un documento PDF

Se crea un nuevo documento PDF y se protege con contraseñas de usuario y propietario, mientras que permisos específicos—como imprimir, modificar contenido y rellenar formularios—se permiten explícitamente. Luego, el documento se guarda con estas restricciones de permisos aplicadas.

1. Crear un nuevo documento PDF.
1. Llama al método [SetPermissions](https://reference.aspose.com/pdf/go-cpp/security/setpermissions/) para proteger el documento.
1. Especifique una contraseña de usuario para restringir el acceso.
1. Especifique una contraseña de propietario para controlar la configuración de seguridad.
1. Defina las operaciones permitidas usando una bandera de bits de permisos.
1. Guardar el PDF con los permisos aplicados usando [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

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