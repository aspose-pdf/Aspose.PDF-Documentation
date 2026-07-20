---
title: Ajout du numéro de page au PDF avec Rust
linktitle: Ajout du numéro de page
type: docs
weight: 10
url: /fr/rust-cpp/add-page-number/
description: Cet article montre comment ajouter des numéros de page à un document PDF existant en utilisant Aspose.PDF pour Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajout de numéros de page
Abstract: Aspose.PDF for Rust via C++ permet aux développeurs d'améliorer les documents PDF existants avec une numérotation automatique des pages en quelques lignes de code seulement. Cet exemple montre comment ouvrir un fichier PDF, insérer des numéros de page sur toutes les pages et enregistrer le document mis à jour sous un nouveau fichier. L'automatisation de la pagination garantit une structure de document cohérente et est particulièrement utile pour les rapports, les contrats, les manuels et autres productions multi‑pages préparées pour la distribution ou l'impression.
SoftwareApplication: rust-cpp
---

Aspose.PDF for Rust via C++ offre une fonctionnalité intégrée pour modifier les documents PDF de façon programmatique. Dans cet exemple, l'application ouvre un fichier PDF existant, applique une numérotation automatique des pages à chaque page et enregistre le document modifié sous un nouveau nom.

Cette approche est utile lors de la génération de documents finalisés destinés à la distribution, à l'impression ou à des fins d'archivage. Le processus ne nécessite que quelques lignes de code et ne modifie pas le fichier original sauf si celui-ci est explicitement écrasé.

La numérotation des pages est une exigence courante pour les rapports, les factures, les contrats, les manuels et autres documents multipages. Le [add_page_num()](https://reference.aspose.com/pdf/rust-cpp/organize/add_page_num/) La méthode insère automatiquement les numéros de page dans toutes les pages du document, assurant une pagination cohérente dans l'ensemble du fichier.

Après avoir ajouté les numéros de page, le document mis à jour est enregistré sous forme d'un nouveau fichier PDF.

1. Ouvrez le document PDF existant.
1. Ajouter des numéros de page avec [add_page_num()](https://reference.aspose.com/pdf/rust-cpp/organize/add_page_num/) méthode.
1. Enregistrer le document mis à jour.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add page number to a PDF-document
        pdf.add_page_num()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_page_num.pdf")?;

        Ok(())
    }
```