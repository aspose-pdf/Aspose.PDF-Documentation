---
title:  Crypter le PDF avec Go
linktitle: Crypter le fichier PDF
type: docs
weight: 10
url: /fr/go-cpp/encrypt-pdf/
description: Crypter le fichier PDF avec Aspose.PDF pour Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Crypter le fichier PDF en utilisant en utilisant le mot de passe Utilisateur ou Propriétaire

Pour crypter les documents facilement et en toute sécurité, vous pouvez utiliser Aspose.PDF pour Go via C++.

- Le **userPassword**, s'il est défini, est ce que vous devez fournir pour ouvrir un PDF. Acrobat/Reader demandera à l'utilisateur de saisir le mot de passe utilisateur. S'il n'est pas correct, le document ne s'ouvrira pas.
- Le **ownerPassword**, s'il est défini, contrôle les autorisations, telles que l'impression, la modification, l'extraction, les commentaires, etc. Acrobat/Reader refusera ces actions en fonction des paramètres d'autorisation. Acrobat exigera ce mot de passe si vous souhaitez définir/modifier les autorisations.

Le PDF est protégé par des mots de passe utilisateur et propriétaire, configuré avec des autorisations d'accès spécifiques, et chiffré à l'aide de l'algorithme AES-128 avec une sécurité compatible PDF 2.0. Le document chiffré est ensuite enregistré sur le disque.

1. Créer un nouveau document PDF.
1. Chiffrer le document PDF avec [chiffrer](https://reference.aspose.com/pdf/go-cpp/security/encrypt/) méthode.
1. Spécifiez un mot de passe utilisateur pour restreindre l'ouverture du document.
1. Spécifiez un mot de passe propriétaire pour contrôler les autorisations.
1. Définissez les actions autorisées à l'aide d'un drapeau de bits de permissions.
1. Choisissez AES-128 comme algorithme de chiffrement.
1. Activez le chiffrement PDF 2.0 pour une conformité de sécurité moderne.
1. Enregistrez le document sécurisé en utilisant [EnregistrerSous](https://reference.aspose.com/pdf/go-cpp/core/saveas/), en l'écrivant dans un nouveau fichier.

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