---
title: Obtenir les autorisations avec Go
linktitle: Obtenir les autorisations
type: docs
weight: 60
url: /fr/go-cpp/get-permissions/
description: Lire et afficher les autorisations d'accès d'un document PDF protégé par mot de passe avec Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Obtenir les autorisations d'un document PDF protégé par mot de passe

Cet exemple montre comment récupérer, interpréter et afficher les autorisations d'accès d'un document PDF protégé par mot de passe en Go en utilisant Aspose.PDF for Go via C++.
Le PDF est ouvert avec le mot de passe propriétaire, ses indicateurs d'autorisation sont lus, et chaque autorisation activée est convertie en une description lisible par l'homme avant d'être affichée dans la console.

1. Définir les correspondances des noms d'autorisations.
1. Convertir les indicateurs d'autorisation en texte lisible.
1. Utiliser [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) avec le mot de passe propriétaire pour accéder aux informations de sécurité du document.
1. Assurez-vous de nettoyer correctement les ressources.
1. Appel [GetPermissions](https://reference.aspose.com/pdf/go-cpp/security/getpermissions/) pour obtenir le bitflag d'autorisation actuel assigné au PDF.
1. Afficher les autorisations.

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