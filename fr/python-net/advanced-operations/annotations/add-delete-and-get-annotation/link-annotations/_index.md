---
title: Utilisation des annotations de lien dans le PDF
linktitle: Annotations de lien
type: docs
weight: 70
url: /fr/python-net/link-annotations/
description: Aspose.PDF pour Python via .NET vous permet d'ajouter, d'obtenir et de supprimer des annotations de lien de votre document PDF.
lastmod: "2025-07-28"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
---

## Ajouter une annotation de lien dans un fichier PDF existant

[Liens](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) sont des annotations qui ouvrent des URL ou se déplacent vers certaines positions dans le même document ou dans un document externe lorsque vous cliquez.

Une annotation de lien est une zone rectangulaire qui peut être placée n'importe où sur la page. Chaque lien possède une action PDF correspondante qui lui est associée. Cette action est exécutée lorsque l'utilisateur clique dans la zone de ce lien.

L'extrait de code suivant montre comment ajouter une annotation de lien à un fichier PDF en utilisant un exemple de numéro de téléphone :

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    # Create TextFragmentAbsorber object to find a phone number
    textFragmentAbsorber = ap.text.TextFragmentAbsorber("file")

    # Accept the absorber for the 1st page only
    document.pages[1].accept(textFragmentAbsorber)

    phoneNumberFragment = textFragmentAbsorber.text_fragments[1]

    # Create Link Annotation and set the action to call a phone number
    linkAnnotation = ap.annotations.LinkAnnotation(document.pages[1], phoneNumberFragment.rectangle)
    linkAnnotation.action = ap.annotations.GoToURIAction("www.aspose.com")

    # Add annotation to page
    document.pages[1].annotations.append(linkAnnotation)
    document.save(output_file)
```

### Obtenir une annotation de lien

Veuillez essayer d'utiliser l'extrait de code suivant pour obtenir [LinkAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/linkannotation/) à partir du document PDF.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    linkAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for la in linkAnnotations:
        print(la.rect)
```

### Supprimer l'annotation de lien

L'extrait de code suivant montre comment supprimer une annotation de lien d'un fichier PDF. Pour cela, nous devons trouver et supprimer toutes les annotations de lien sur la première page. Après cela, nous enregistrerons le document avec l'annotation supprimée.

```python

    import aspose.pdf as ap

    document = ap.Document(input_file)
    highlightAnnotations = [
        a
        for a in document.pages[1].annotations
        if (a.annotation_type == ap.annotations.AnnotationType.LINK)
    ]

    for hs in highlightAnnotations:
        document.pages[1].annotations.delete(hs)

    document.save(output_file)
```
