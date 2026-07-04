---
title: Abrir un PDF protegido con contraseña usando Go
linktitle: Abrir un PDF protegido con contraseña
type: docs
weight: 70
url: /es/go-cpp/open-password-protected-pdf/
description: Abrir un archivo PDF protegido con contraseña con Aspose.PDF for Go vía C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Abrir un documento PDF protegido con contraseña

Este fragmento de código explica cómo abrir un documento PDF protegido con contraseña usando Aspose.PDF for Go vía C++. El documento se abre con la contraseña del propietario, que brinda acceso completo y permite operaciones adicionales como leer metadatos, inspeccionar permisos, descifrar el archivo o modificar el contenido.

1. Abrir el documento PDF protegido.
1. Llamar [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) y proporcione el nombre del archivo junto con la contraseña del propietario para desbloquear el documento.
1. Utilice 'defer pdf.Close()' para liberar todos los recursos asignados una vez que el procesamiento haya finalizado.
1. Después de abrir el documento, puede continuar con tareas adicionales como descifrar el PDF, cambiar los permisos o extraer información.

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