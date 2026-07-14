---
title: Descifrar PDF usando Go
linktitle: Descifrar archivo PDF
type: docs
weight: 40
url: /es/go-cpp/decrypt-pdf/
description: Descifrar archivo PDF con Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Descifrar archivo PDF usando contraseña del propietario

Puede abrir, descifrar y guardar un documento PDF protegido con contraseña usando Aspose.PDF for Go vía C++. El archivo PDF se abre con la contraseña del propietario, se descifra para eliminar todas las restricciones de seguridad y luego se guarda como un nuevo documento sin protección.

1. Llama al método [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) y proporcione el nombre del archivo junto con la contraseña del propietario para acceder al PDF cifrado.
1. Llama al método [Decrypt](https://reference.aspose.com/pdf/go-cpp/security/decrypt/) método para eliminar la protección con contraseña y todas las restricciones de seguridad asociadas del documento.
1. Guarde el PDF descifrado usando [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

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