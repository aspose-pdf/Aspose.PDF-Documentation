---
title:  Cifrar PDF usando Go
linktitle: Cifrar archivo PDF
type: docs
weight: 10
url: /es/go-cpp/encrypt-pdf/
description: Cifrar archivo PDF con Aspose.PDF for Go a través de C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Cifrar archivo PDF usando usando contraseña de usuario o de propietario

Para cifrar documentos de forma fácil y segura, puedes usar Aspose.PDF for Go a través de C++.

- El **userPassword**, si está establecido, es lo que necesitas proporcionar para abrir un PDF. Acrobat/Reader le pedirá al usuario que introduzca la contraseña de usuario. Si no es correcta, el documento no se abrirá.
- El **ownerPassword**, si está establecido, controla los permisos, como imprimir, editar, extraer, comentar, etc. Acrobat/Reader rechazará estas acciones según la configuración de permisos. Acrobat requerirá esta contraseña si deseas establecer/cambiar permisos.

El PDF está protegido con contraseñas de usuario y de propietario, configurado con permisos de acceso específicos y cifrado usando el algoritmo AES-128 con seguridad compatible con PDF 2.0. El documento cifrado se guarda luego en el disco.

1. Crear un nuevo documento PDF.
1. Cifrar el documento PDF con [encrypt](https://reference.aspose.com/pdf/go-cpp/security/encrypt/) método.
1. Especifique una contraseña de usuario para restringir la apertura del documento.
1. Especifique una contraseña de propietario para controlar los permisos.
1. Defina acciones permitidas usando una bandera de bits de permisos.
1. Elija AES-128 como el algoritmo de cifrado.
1. Habilite el cifrado PDF 2.0 para el cumplimiento de seguridad moderno.
1. Guarde el documento protegido usando [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/), escribiéndolo en un archivo nuevo.

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