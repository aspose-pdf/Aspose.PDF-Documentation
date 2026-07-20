---
title: Extraire des données d'AcroForm à l'aide de Rust
linktitle: Extraire des données d'AcroForm
type: docs
weight: 50
url: /fr/rust-cpp/extract-data-from-acroform/
description: Aspose.PDF facilite l'extraction des données de champs de formulaire à partir de fichiers PDF. Apprenez comment extraire des données d'AcroForms et les enregistrer au format XML, FDF ou XFDF.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment extraire des données d'AcroForm via Rust
Abstract: Cet article explique comment extraire les données AcroForm de fichiers PDF en utilisant Aspose.PDF for Rust via C++ et les exporter vers des formats d'échange de données largement utilisés - XML, FDF et XFDF. Il montre comment ouvrir un document PDF contenant des champs de formulaire interactifs et exporter programmatique les noms et valeurs des champs de formulaire pour les réutiliser en dehors du PDF d'origine. En fournissant des exemples pratiques en Rust pour chaque format d'exportation, l'article met en évidence les flux de travail courants, y compris le traitement des données, la soumission de formulaires, l'intégration système et le stockage de données à long terme, aidant les développeurs à gérer et réutiliser efficacement les données de formulaire PDF dans leurs applications.
---

## Exporter des données vers XML depuis un fichier PDF

Cet extrait de code montre comment exporter les données AcroForm d'un document PDF vers un fichier XML en utilisant Aspose.PDF for Rust.
Le processus consiste à ouvrir un fichier PDF existant contenant des champs de formulaire, puis à exporter ces champs et leurs valeurs vers un document XML pour un traitement ultérieur, un stockage ou un échange de données.

1. Ouvrez le document PDF.
1. Appelez la méthode 'export_xml' pour extraire les données des champs de formulaire et les enregistrer dans un fichier XML.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XML-document
        pdf.export_xml("sample.xml")?;

        Ok(())
    }
```

## Exporter les données vers FDF à partir d'un fichier PDF

Aspose.PDF for Rust via C++ vous permet d'exporter les données AcroForm d'un document PDF vers un fichier FDF. Le fichier Formats de données de formulaire (FDF) stocke les noms et les valeurs des champs de formulaire séparément du PDF, ce qui le rend utile pour l'échange de données, les flux de travail de soumission de formulaires et l'archivage des données de formulaire sans les intégrer dans le document original.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to FDF-document
        pdf.export_fdf("sample.fdf")?;

        Ok(())
    }
```

## Exporter les données vers XFDF depuis un fichier PDF

XFDF (XML Forms Data Format) est un format basé sur XML qui représente les données des champs de formulaire séparément du fichier PDF, ce qui le rend idéal pour l'échange de données, les soumissions de formulaires et l'intégration avec les flux de travail basés sur le web.
Aspose.PDF for Rust via C++ aide à exporter les données AcroForm d'un document PDF vers un fichier XFDF.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XFDF-document
        pdf.export_xfdf("sample.xfdf")?;

        Ok(())
    }
```
