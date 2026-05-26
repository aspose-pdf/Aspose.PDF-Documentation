---
title: Mettre à jour les liens PDF en Python
linktitle: Mettre à jour les liens
type: docs
weight: 20
url: /fr/python-net/update-links/
description: Apprenez comment mettre à jour l'apparence et les destinations des liens PDF en Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment mettre à jour les liens dans le PDF
Abstract: Le guide Aspose.PDF for Python via .NET sur la mise à jour des liens accompagne les développeurs dans le processus de modification du comportement des hyperliens au sein des documents PDF à l'aide de Python. Il explique comment changer les destinations des liens pour qu'ils pointent vers des pages spécifiques, des sites Web externes ou même d'autres fichiers PDF. La documentation couvre également la façon d'ajuster l'apparence des annotations de lien, y compris la couleur du texte, et fournit des exemples de code pratiques pour chaque scénario. Que vous corrigiez des URL obsolètes ou amélioriez la navigation, cette ressource offre une approche claire et efficace pour gérer les liens programmatiquement.
---

## Mettre à jour la couleur du texte LinkAnnotation

Cet exemple montre comment détecter toutes les annotations de lien sur la première page d'un PDF en utilisant Aspose.PDF for Python, puis surligner le texte près de chaque lien en changeant la couleur de la police en rouge. Il utilise TextFragmentAbsorber avec une zone légèrement élargie autour de chaque rectangle de lien pour trouver et modifier le texte à proximité.

Cela peut être utilisé pour:

- Marquer visuellement les liens dans un document
- Améliorer l'accessibilité en mettant en évidence le contenu lié
- Prétraitement des fichiers PDF avant la révision ou l'exportation

Pour chacune de ces annotations de lien, le script récupère sa frontière rectangulaire et étend légèrement cette région pour inclure le texte voisin, permettant une identification visuelle plus large. Il applique ensuite un TextFragmentAbsorber sur cette zone agrandie afin d'extraire les fragments de texte qui s'y trouvent. Ces fragments capturés sont modifiés en changeant leur couleur de police en rouge, marquant ainsi le texte environnant pour mettre en évidence et réviser. Après avoir appliqué toutes ces modifications, le document modifié est enregistré dans le chemin de sortie, en conservant les annotations mises en surbrillance et leur texte associé.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_text_color(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        ta = ap.text.TextFragmentAbsorber()
        rect = la.rect
        rect.llx -= 2
        rect.lly -= 2
        rect.urx += 2
        rect.ury += 2
        ta.text_search_options = ap.text.TextSearchOptions(rect)
        ta.visit(document.pages[1])
        for textFragment in ta.text_fragments:
            textFragment.text_state.foreground_color = ap.Color.red

    document.save(outfile)
```

## Mettre à jour la bordure

Le script se concentre sur la première page du document et filtre toutes les annotations, ne sélectionnant que celles de type LINK — ces dernières représentent généralement des éléments interactifs, tels que des hyperliens ou des déclencheurs de navigation. Pour chacune de ces annotations de lien, le code les convertit en type LinkAnnotation et met à jour leur propriété couleur en rouge, les mettant en évidence visuellement afin qu’elles se distinguent du reste du contenu. Après que toutes les annotations de lien ont été modifiées, le document mis à jour est enregistré à l’emplacement de sortie défini, en conservant le nouveau style.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_border(infile, outfile):
    document = ap.Document(infile)
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in link_annotations:
        link_annotation = cast(ap.annotations.LinkAnnotation, la)
        link_annotation.color = ap.Color.red

    document.save(outfile)
```

## Mettre à jour la destination Web

Une fois les chemins en place, le document original est chargé à l'aide de la bibliothèque Aspose.PDF, rendant son contenu accessible à la modification. Le script se concentre ensuite sur la première page du document, en filtrant toutes les annotations et en ne sélectionnant que celles de type lien, représentant généralement des zones cliquables ou des hyperliens. Pour éviter les erreurs de type et garantir une manipulation sûre, chaque annotation est vérifiée avec is_assignable puis convertie en type LinkAnnotation approprié. Si le lien est associé à une GoToURIAction, signifiant qu'il pointe vers une adresse web, le script met à jour cette URI pour rediriger les utilisateurs vers "https://www.aspose.com". Enfin, après que toutes les modifications souhaitées ont été appliquées, le document modifié est enregistré à l'emplacement de sortie spécifié.

```python
import aspose.pdf as ap
import sys
from os import path
from aspose.pycore import cast, is_assignable

def link_annotation_update_web_destination(infile, outfile):
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
                action.uri = "https://www.aspose.com"
    document.save(outfile)
```

## Sujets liés aux liens

- [Travailler avec les liens PDF en Python](/pdf/fr/python-net/links/)
- [Créer des liens PDF en Python](/pdf/fr/python-net/create-links/)
- [Extraire les liens PDF en Python](/pdf/fr/python-net/extract-links/)