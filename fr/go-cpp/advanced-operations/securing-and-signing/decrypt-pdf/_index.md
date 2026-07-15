---
title: Décrypter le PDF avec Go
linktitle: Décrypter le fichier PDF
type: docs
weight: 40
url: /fr/go-cpp/decrypt-pdf/
description: Décrypter le fichier PDF avec Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Décrypter le fichier PDF en utilisant le mot de passe propriétaire

Vous pouvez ouvrir, décrypter et enregistrer un document PDF protégé par mot de passe en utilisant Aspose.PDF for Go via C++. Le fichier PDF est ouvert avec le mot de passe propriétaire, décrypté pour supprimer toutes les restrictions de sécurité, puis enregistré comme un nouveau document non protégé.

1. Appel [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) et fournissez le nom du fichier ainsi que le mot de passe propriétaire pour accéder au PDF chiffré.
1. Appelez le [Decrypt](https://reference.aspose.com/pdf/go-cpp/security/decrypt/) méthode pour supprimer la protection par mot de passe et toutes les restrictions de sécurité associées du document.
1. Enregistrez le PDF déchiffré en utilisant [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

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