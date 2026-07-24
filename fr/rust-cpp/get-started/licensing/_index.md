---
title: Licence Aspose PDF
linktitle: Licence et limitations
type: docs
weight: 90
url: /fr/rust-cpp/licensing/
description: Aspose. PDF for Rust invite ses clients à obtenir une Classic License. Ainsi qu’à utiliser une licence limitée pour mieux explorer le produit.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Licence d'Aspose.PDF pour Rust via C++
Abstract: La page de licence d'Aspose.PDF pour Rust via C++ explique les options de licence disponibles pour le produit. Les clients peuvent choisir entre une Classic License, une Metered License ou une licence limitée à des fins d'évaluation. La page met également en évidence les avantages d'obtenir une licence appropriée, tels que le déverrouillage de toutes les fonctionnalités et la suppression des limitations d'évaluation.
SoftwareApplication: rust-cpp
---

## Licence

- Le **code source Rust** est licencié sous la licence MIT.
- La **bibliothèque partagée** (AsposePDFforRust_windows_amd64.dll, libAsposePDFforRust_linux_amd64.so, libAsposePDFforRust_darwin_amd64.dylib, libAsposePDFforRust_darwin_arm64.dylib) est propriétaire et nécessite une licence commerciale. Pour utiliser toutes les fonctionnalités, vous devez obtenir une licence.

## Version d'évaluation

Vous pouvez utiliser **Aspose.PDF for Rust via C++** gratuitement pour l'évaluation. La version d'évaluation offre presque toutes les fonctionnalités du produit avec certaines limitations. La même version d'évaluation devient sous licence lorsque vous achetez une licence et ajoutez quelques lignes de code pour appliquer la licence.

- Si vous souhaitez tester Aspose.PDF for Rust sans les limitations de la version d'évaluation, vous pouvez également demander une licence temporaire de 30 jours. Veuillez vous référer à [Comment obtenir une licence temporaire ?](https://purchase.aspose.com/temporary-license)?

### Limitation d'une version d'évaluation

Nous voulons que nos clients testent nos composants en profondeur avant d'acheter, ainsi la version d'évaluation vous permet de l'utiliser comme vous le feriez normalement.

- **Documents créés avec un filigrane d'évaluation**. La version d'évaluation d'Aspose.PDF for Rust offre toutes les fonctionnalités du produit, mais toutes les pages des fichiers générés sont filigranées avec le texte "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd." en haut.
- **Limiter le nombre de pages pouvant être traitées**. Dans la version d'évaluation, vous ne pouvez traiter que les quatre premières pages d'un document.

### Utilisation en production

Une clé de licence commerciale est requise dans un environnement de production. Veuillez nous contacter pour acheter une licence commerciale.

### Appliquer la licence

Application d'une licence pour activer toutes les fonctionnalités d'Aspose.PDF pour Rust à l'aide d'un fichier de licence (Aspose.PDF.RustViaCPP.lic).

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set license with filename
        pdf.set_license("Aspose.PDF.RustViaCPP.lic")?;

        // Now you can work with the licensed PDF document
        // ...

        Ok(())
    }
```