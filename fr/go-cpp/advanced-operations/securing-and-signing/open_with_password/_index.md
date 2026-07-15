---
title: Ouvrir un PDF protégé par mot de passe avec Go
linktitle: Ouvrir un PDF protégé par mot de passe
type: docs
weight: 70
url: /fr/go-cpp/open-password-protected-pdf/
description: Ouvrir un fichier PDF protégé par mot de passe avec Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ouvrir un document PDF protégé par mot de passe

Cet extrait de code explique comment ouvrir un document PDF protégé par mot de passe en utilisant Aspose.PDF for Go via C++. Le document est ouvert avec le mot de passe propriétaire, qui offre un accès complet et permet d'autres opérations telles que la lecture des métadonnées, l'inspection des permissions, le déchiffrement du fichier ou la modification du contenu.

1. Ouvrir le document PDF protégé.
1. Appeler [OpenWithPassword](https://reference.aspose.com/pdf/go-cpp/security/openwithpassword/) et fournissez le nom du fichier ainsi que le mot de passe du propriétaire pour déverrouiller le document.
1. Utilisez 'defer pdf.Close()' pour libérer toutes les ressources allouées une fois le traitement terminé.
1. Après avoir ouvert le document, vous pouvez poursuivre avec des tâches supplémentaires telles que le déchiffrement du PDF, la modification des autorisations ou l'extraction d'informations.

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