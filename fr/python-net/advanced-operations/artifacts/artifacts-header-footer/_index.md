---
title: Gérer les en-têtes et pieds de page PDF avec Python
linktitle: Gérer les en-têtes et pieds de page PDF
type: docs
weight: 70
url: /fr/python-net/artifacts-header-footer/
description: Apprenez comment gérer les en-têtes et pieds de page dans les documents PDF avec Python et Aspose.PDF.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment ajouter, personnaliser et supprimer les en-têtes et pieds de page PDF avec Python
Abstract: La gestion des en-têtes et pieds de page est une exigence courante lors du travail avec des documents PDF dans les flux de travail d'entreprise, d'édition et d'automatisation. Cet article montre comment utiliser Aspose.PDF for Python pour ajouter des en-têtes et pieds de page à l'aspect professionnel avec un style personnalisé tel que police, taille, couleur et alignement. Il montre également comment détecter et supprimer les artefacts de pagination existants tels que les en-têtes et pieds de page d'une page PDF. Grâce à des fonctions réutilisables et à des exemples clairs, les développeurs peuvent rapidement intégrer ces fonctionnalités aux systèmes de traitement de documents pour la marque, les rapports ou le nettoyage de fichiers.
---

## Créer des artefacts de texte stylisés

Cette fonction utilitaire explique comment créer un artefact de texte réutilisable pour les pages PDF en utilisant Aspose.PDF for Python. Elle est conçue pour générer des en-têtes ou pieds de page stylisés avec un formatage cohérent, incluant les paramètres de police, la couleur, la taille et l'alignement. La fonction abstrait la création d'artefact afin qu'elle puisse être réutilisée pour différentes décorations de texte au niveau de la page.

1. Instanciez l'objet artefact.
1. Définissez le contenu texte de l'artefact.
1. Appliquez le style du texte.
1. Définir l'alignement.
1. Retourner l'artefact configuré.

```python
from os import path
import aspose.pdf as ap
import sys

def _create_text_artifact(artifact_class, text):
    """Create a text artifact (header/footer) with common styling."""
    artifact = artifact_class()
    artifact.text = text
    artifact.text_state.font_size = 14
    artifact.text_state.font = ap.text.FontRepository.find_font("Arial")
    artifact.text_state.foreground_color = ap.Color.navy
    artifact.artifact_horizontal_alignment = ap.HorizontalAlignment.CENTER
    return artifact

```

## Ajouter un en-tête au PDF

1. Ouvrir le PDF d'entrée.
1. Créer un HeaderArtifact avec le texte "Sample Header".
1. Ajoutez-le à la première page.
1. Enregistrez le PDF mis à jour.

```python
from os import path
import aspose.pdf as ap
import sys

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## Ajouter un pied de page au PDF

1. Ouvrir le PDF d'entrée.
1. Créer un FooterArtifact avec le texte "Sample Footer".
1. Ajoutez-le à la première page.
1. Enregistrer le fichier de sortie.

```python
from os import path
import aspose.pdf as ap
import sys

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## Supprimer les artefacts d'en-tête ou de pied de page

1. Ouvrir le PDF.
1. Trouver les artefacts marqués comme en-têtes ou pieds de page de pagination.
1. Les supprimer de la première page.
1. Enregistrer le document nettoyé.

```python
from os import path
import aspose.pdf as ap
import sys

def delete_header_footer_artifact(infile, outfile):
    with ap.Document(infile) as document:
        header_footers = [
            artifact
            for artifact in document.pages[1].artifacts
            if artifact.type == ap.Artifact.ArtifactType.PAGINATION
            and (
                artifact.subtype == ap.Artifact.ArtifactSubtype.HEADER
                or artifact.subtype == ap.Artifact.ArtifactSubtype.FOOTER
            )
        ]

        for art in header_footers:
            document.pages[1].artifacts.delete(art)

        document.save(outfile)
```

## Sujets d'artefacts associés

- [Travailler avec les artefacts PDF en Python](/pdf/fr/python-net/artifacts/)
- [Ajouter des arrière-plans PDF en Python](/pdf/fr/python-net/add-backgrounds/)
- [Ajouter la numérotation Bates aux PDF en Python](/pdf/fr/python-net/add-bates-numbering/)
- [Compter les types d'artefacts dans les fichiers PDF](/pdf/fr/python-net/counting-artifacts/)