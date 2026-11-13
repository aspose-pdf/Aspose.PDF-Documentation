---
title: Ajouter des en-têtes et pieds de page PDF en Python
linktitle: Ajouter des en-têtes et pieds de page
type: docs
weight: 70
url: /fr/python-net/artifacts-header-footer/
description: Ajouter des éléments d’en-tête et de pied de page stylisés aux pages PDF en Python.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des en-têtes et pieds de page à un PDF avec Python
Abstract: Ajouter des éléments d’en-tête et de pied de page stylisés aux pages PDF en Python.
---

Utiliser `HeaderArtifact` et `FooterArtifact` pour ajouter du texte en cours aux pages PDF. Ces exemples ajoutent des artefacts à la première page.

## Créer des artefacts de texte stylisé

Définissez cette fonction utilitaire avant d’exécuter un exemple d’ajout. Elle applique la même police, la même taille, la même couleur et le même alignement aux en-têtes et pieds de page.

```python
import aspose.pdf as ap

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

Passez `HeaderArtifact` à la fonction utilitaire et ajoutez l’artefact obtenu à la page.

```python
import aspose.pdf as ap

def add_header_artifact(infile, outfile):
    """Add a header artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        header = _create_text_artifact(ap.HeaderArtifact, "Sample Header")
        document.pages[1].artifacts.append(header)
        document.save(outfile)
```

## Ajouter un pied de page au PDF

Passez `FooterArtifact` à la fonction utilitaire et ajoutez l’artefact obtenu à la page.

```python
import aspose.pdf as ap

def add_footer_artifact(infile, outfile):
    """Add a footer artifact to the first page of a PDF document."""
    with ap.Document(infile) as document:
        footer = _create_text_artifact(ap.FooterArtifact, "Sample Footer")
        document.pages[1].artifacts.append(footer)
        document.save(outfile)
```

## Rubriques connexes

- [Supprimer les en-têtes et pieds de page](/pdf/fr/python-net/remove-headers-footers/)
- [Travailler avec les artefacts PDF en Python](/pdf/fr/python-net/artifacts/)
