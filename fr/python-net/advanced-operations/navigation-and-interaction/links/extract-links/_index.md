---
title: Extraire les liens PDF en Python
linktitle: Extraire les liens
type: docs
weight: 30
url: /fr/python-net/extract-links/
description: Apprenez comment extraire les annotations de lien et les hyperliens des documents PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment extraire les liens d'un PDF
Abstract: Le guide Aspose.PDF for Python via .NET sur l'extraction des liens explique comment récupérer programmatiquement les annotations d'hyperlien à partir de documents PDF en utilisant Python. La documentation comprend des exemples de code pratiques et met en évidence comment cette fonctionnalité peut être utilisée pour des tâches telles que l'audit des liens, l'analyse de navigation ou la création de fonctionnalités de document interactives. Que vous travailliez avec des PDF d'une seule page ou que vous traitiez de gros lots, ce guide propose une approche claire et efficace de l'extraction d'hyperliens.
---

## Extraire les liens du fichier PDF

Cet exemple montre comment parcourir toutes les annotations de lien sur la première page d’un PDF en utilisant Aspose.PDF for Python. Il filtre les annotations pour identifier celles de type LinkAnnotation, les convertit en toute sécurité, puis affiche leur indice de page et leur position rectangulaire sur la page.

Cela peut être utilisé pour le débogage, l’analyse, ou les mises à jour automatisées des annotations de lien existantes dans un PDF.

1. Chargez le document PDF. Utilisez ap.Document(path_infile) pour ouvrir le fichier.
1. Accédez aux annotations de la première page. Utilisez document.pages[1].annotations pour récupérer toutes les annotations.
1. Filtrez uniquement les types LinkAnnotation. Vérifiez l’annotation_type de chaque annotation.
1. Convertissez et traitez les LinkAnnotations. Utilisez is_assignable() et cast() pour garantir un accès sécurisé aux propriétés de LinkAnnotation.
1. Imprimer les détails de l'annotation. Afficher l'indice de page et le rectangle (emplacement) de chaque lien.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_link_annotation(infile):

    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
```

## Extraire les hyperliens du fichier PDF

Ce code montre comment extraire tous les objets LinkAnnotation de la première page d'un document PDF à l'aide d'Aspose.PDF for Python, puis identifier ceux qui contiennent une GoToURIAction. Pour chaque lien de ce type, il affiche l'indice de page et l'URI cible.

Ceci est utile pour des tâches telles que :

- Audit des liens externes dans un PDF
- Extraction des URL de documentation ou de support
- Détection des hyperliens cassés ou obsolètes

1. Chargez le document PDF. Ouvrez le fichier en utilisant ap.Document.
1. Obtenez toutes les annotations de lien de la première page. Filtrez les annotations pour n’inclure que celles de type AnnotationType.LINK.
1. Vérifiez le type et effectuez le cast en LinkAnnotation. Assurez-vous que chaque annotation soit bien une LinkAnnotation avant d’accéder à ses propriétés.
1. Vérifiez le type d’action du lien. Filtrez les liens qui utilisent un GoToURIAction (c’est‑à‑dire les liens vers une URL web).
1. Extrayez et affichez l’URI et l’indice de page. Utilisez .uri pour obtenir le lien externe et .page_index pour le contexte.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def extract_hyperlinks(infile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        if is_assignable(la, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, la)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"Page {annotation.page_index}, URI:{action.uri}")
```

## Sujets liés aux liens

- [Travailler avec les liens PDF en Python](/pdf/fr/python-net/links/)
- [Créer des liens PDF en Python](/pdf/fr/python-net/create-links/)
- [Mettre à jour les liens du PDF en utilisant Python](/pdf/fr/python-net/update-links/)