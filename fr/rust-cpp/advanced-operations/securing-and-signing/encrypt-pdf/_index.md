---
title:  Crypter le PDF avec Rust
linktitle: Crypter le fichier PDF
type: docs
weight: 10
url: /fr/rust-cpp/encrypt-pdf/
description: Crypter le fichier PDF avec Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Crypter le fichier PDF en utilisant le mot de passe utilisateur ou propriétaire

Pour chiffrer facilement et en toute sécurité les documents, vous pouvez utiliser Aspose.PDF for Rust via C++.

- Le **user_password**, s'il est défini, est ce que vous devez fournir pour ouvrir un PDF. Acrobat/Reader demandera à l'utilisateur de saisir le mot de passe utilisateur. S'il n'est pas correct, le document ne s'ouvrira pas.
- Le **owner_password**, s'il est défini, contrôle les autorisations, comme l'impression, la modification, l'extraction, les commentaires, etc. Acrobat/Reader refusera ces actions en fonction des paramètres d'autorisation. Acrobat exigera ce mot de passe si vous souhaitez définir/modifier les autorisations.

Le PDF est protégé par les mots de passe utilisateur et propriétaire, des autorisations d'accès spécifiques, et un chiffrement AES-128 conforme aux normes PDF 2.0. Une fois chiffré, le document est enregistré sur le disque, garantissant un accès contrôlé et une manipulation sécurisée du fichier PDF.

1. Créer un nouveau document PDF.
1. Chiffrer le document PDF avec [chiffrer](https://reference.aspose.com/pdf/rust-cpp/security/encrypt/) méthode.
1. Spécifiez un mot de passe utilisateur pour restreindre l'ouverture du document.
1. Spécifiez un mot de passe propriétaire pour contrôler les autorisations.
1. Définissez les actions autorisées à l'aide d'un drapeau de bits de permissions.
1. Choisissez AES-128 comme algorithme de chiffrement.
1. Activez le chiffrement PDF 2.0 pour la conformité aux exigences de sécurité modernes.
1. Enregistrez le PDF chiffré en utilisant [enregistrer_sous](https://reference.aspose.com/pdf/rust-cpp/core/save_as/). 

```rs

  use asposepdf::{CryptoAlgorithm, Document, Permissions};

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Create a new PDF-document
      let pdf = Document::new()?;

      // Encrypt PDF-document
      pdf.encrypt(
          "userpass",  // User password
          "ownerpass", // Owner password
          Permissions::PRINT_DOCUMENT | Permissions::MODIFY_CONTENT | Permissions::FILL_FORM, // Permissions bitflag
          CryptoAlgorithm::AESx128, // Encryption algorithm
          true,                     // Use PDF 2.0 encryption
      )?;

      // Save the encrypted PDF-document
      pdf.save_as("sample_with_password.pdf")?;

      Ok(())
  }
```