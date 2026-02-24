---
title: Extraire les liens du fichier PDF à l'aide de Python
linktitle: Extraire les liens
type: docs
weight: 30
url: /fr/python-net/extract-links/
description: Découvrez comment extraire les hyperliens des documents PDF en Python en utilisant Aspose.PDF pour la gestion de contenu et l'analyse des liens.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment extraire les liens d’un PDF
Abstract: Le guide Aspose.PDF pour Python via .NET sur l'extraction de liens explique comment récupérer programmatiquement les annotations d'hyperliens de documents PDF en utilisant Python. La documentation comprend des exemples de code pratiques et souligne comment cette fonctionnalité peut être utilisée pour des tâches telles que l'audit des liens, l'analyse de la navigation ou la création de fonctionnalités interactives dans les documents. Que vous travailliez avec des PDF d'une seule page ou que vous traitiez de grands lots, ce guide offre une approche claire et efficace de l'extraction d'hyperliens.
---

## Extraire les liens du fichier PDF

Cet exemple montre comment parcourir toutes les annotations de lien sur la première page d'un PDF à l'aide d'Aspose.PDF pour Python. Il filtre les annotations pour identifier celles de type LinkAnnotation, les convertit en toute sécurité, puis affiche leur indice de page et leur position rectangulaire sur la page.

Cela peut être utilisé pour le débogage, l'analyse ou les mises à jour automatisées des annotations de lien existantes dans un PDF.

1. Chargez le document PDF. Utilisez ap.Document(path_infile) pour ouvrir le fichier.
1. Accédez aux annotations de la première page. Utilisez document.pages[1].annotations pour récupérer toutes les annotations.
1. Filtrez uniquement les types LinkAnnotation. Vérifiez la propriété annotation_type de chaque annotation.
1. Convertissez et traitez les LinkAnnotations. Utilisez is_assignable() et cast() pour garantir un accès sûr aux propriétés de LinkAnnotation.
1. Affichez les détails de l'annotation. Sortez l'indice de page et le rectangle (emplacement) de chaque lien.

```python

    import aspose.pdf as ap
    from os import path

    # Construct full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # (Optional) You can construct the output file path if needed later
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only LinkAnnotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    # Iterate over each link annotation
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (type-safe check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Safely cast the annotation to LinkAnnotation type
            annotation = cast(ap.annotations.LinkAnnotation, la)
            
            # Print annotation location and page index
            print(f"Page: {annotation.page_index}, location: {annotation.rect}")
            print(annotation.page_index)
```

## Extraire les hyperliens du fichier PDF

Ce code montre comment extraire tous les objets LinkAnnotation de la première page d'un document PDF en utilisant Aspose.PDF pour Python, puis identifier ceux qui contiennent une GoToURIAction. Pour chaque lien de ce type, il affiche l'indice de page et l'URI cible.

Cela est utile pour des tâches telles que :

- Auditer les liens externes d'un PDF
- Extraire les URL de documentation ou de support
- Détecter les hyperliens cassés ou obsolètes

1. Chargez le document PDF. Ouvrez le fichier en utilisant ap.Document.
1. Obtenez toutes les annotations de lien de la première page. Filtrez les annotations pour n'inclure que celles de type AnnotationType.LINK.
1. Vérifiez le type et convertissez en LinkAnnotation. Assurez-vous que chaque annotation est bien une LinkAnnotation avant d'accéder à ses propriétés.
1. Vérifiez le type d'action du lien. Filtrez les liens qui utilisent une GoToURIAction (c’est‑à‑dire les liens vers une URL web).
1. Extrayez et affichez l'URI et l'indice de page. Utilisez .uri pour obtenir le lien externe et .page_index pour le contexte.

```python

    import aspose.pdf as ap
    from os import path

    # Construct the full path for the input PDF file
    path_infile = path.join(self.dataDir, infile)

    # Optional: construct output file path if needed
    # path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Retrieve all annotations from the first page and filter only link annotations
    link_annotations = [
        a
        for a in document.pages[1].annotations
        if a.annotation_type == ap.annotations.AnnotationType.LINK
    ]

    # Iterate through filtered link annotations
    for la in link_annotations:
        # Check if the annotation is a LinkAnnotation (safe type check)
        if is_assignable(la, ap.annotations.LinkAnnotation):
            # Cast the annotation to LinkAnnotation to access link-specific properties
            annotation = cast(ap.annotations.LinkAnnotation, la)

            # Check if the link's action is of type GoToURIAction (external web link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                # Cast the action to GoToURIAction to access the URI property
                action = cast(ap.annotations.GoToURIAction, annotation.action)

                # Print the page number and the link's URI
                print(f"Page {annotation.page_index}, URI: {action.uri}")
```
