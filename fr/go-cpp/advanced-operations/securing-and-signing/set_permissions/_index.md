---
title: Définir les autorisations d'un document PDF avec Go
linktitle: Définir les autorisations
type: docs
weight: 80
url: /fr/go-cpp/set_permissions/
description: Définir les autorisations d'un document PDF avec Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Définir les autorisations d'accès pour un document PDF

Un nouveau document PDF est créé et protégé avec les mots de passe utilisateur et propriétaire, tandis que des autorisations spécifiques—telles que l'impression, la modification du contenu et le remplissage des formulaires—sont explicitement autorisées. Le document est ensuite enregistré avec ces restrictions d'autorisation appliquées.

1. Créer un nouveau document PDF.
1. Appel [SetPermissions](https://reference.aspose.com/pdf/go-cpp/security/setpermissions/) pour protéger le document.
1. Spécifiez un mot de passe utilisateur pour restreindre l'accès.
1. Spécifiez un mot de passe propriétaire pour contrôler les paramètres de sécurité.
1. Définissez les opérations autorisées à l'aide d'un bitflag d'autorisations.
1. Enregistrez le PDF avec les autorisations appliquées en utilisant [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

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