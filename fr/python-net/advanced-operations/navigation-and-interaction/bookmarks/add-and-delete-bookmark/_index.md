---
title: Ajouter et Supprimer un Signet en Python
linktitle: Ajouter et Supprimer un Signet
type: docs
weight: 10
url: fr/python-net/add-and-delete-bookmark/
description: Vous pouvez ajouter un signet à un document PDF avec Python. Il est possible de supprimer tous les signets ou certains d'entre eux d'un document PDF.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Ajouter et Supprimer un Signet",
    "alternativeHeadline": "Comment ajouter et supprimer un Signet d'un PDF",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "génération de document pdf",
    "keywords": "pdf, python, supprimer signet, ajouter signet",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe de Documentation Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "ventes",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventes",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventes",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/add-and-delete-bookmark/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-and-delete-bookmark/"
    },
    "dateModified": "2023-02-04",
    "description": "Vous pouvez ajouter un signet à un document PDF avec Python. Il est possible de supprimer tous les signets ou certains d'entre eux d'un document PDF."
}
</script>


## Ajouter un signet à un document PDF

Les signets sont contenus dans la collection [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) de l'objet Document, elle-même dans la collection [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).

Pour ajouter un signet à un PDF :

1. Ouvrez un document PDF à l'aide de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
2. Créez un signet et définissez ses propriétés.
3. Ajoutez la collection [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/) à la collection Outlines.

Le code suivant vous montre comment ajouter un signet dans un document PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Créer un objet signet
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Test Signet"
    outline.italic = True
    outline.bold = True
    # Définir le numéro de la page de destination
    outline.action = ap.annotations.GoToAction(document.pages[1])
    # Ajouter le signet dans la collection d'outline du document.
    document.outlines.append(outline)

    # Enregistrer le résultat
    document.save(output_pdf)
```


## Ajouter un Signet Enfant au Document PDF

Les signets peuvent être imbriqués, indiquant une relation hiérarchique avec des signets parents et enfants. Cet article explique comment ajouter un signet enfant, c'est-à-dire un signet de deuxième niveau, à un PDF.

Pour ajouter un signet enfant à un fichier PDF, ajoutez d'abord un signet parent :

1. Ouvrez un document.
1. Ajoutez un signet à la [OutlineItemCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlineitemcollection/), en définissant ses propriétés.
1. Ajoutez la OutlineItemCollection à la collection [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/) de l'objet Document.

Le signet enfant est créé exactement comme le signet parent, expliqué ci-dessus, mais est ajouté à la collection Outlines du signet parent.

Les extraits de code suivants montrent comment ajouter un signet enfant à un document PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Créer un objet signet parent
    outline = ap.OutlineItemCollection(document.outlines)
    outline.title = "Parent Outline"
    outline.italic = True
    outline.bold = True

    # Créer un objet signet enfant
    childOutline = ap.OutlineItemCollection(document.outlines)
    childOutline.title = "Child Outline"
    childOutline.italic = True
    childOutline.bold = True

    # Ajouter un signet enfant dans la collection du signet parent
    outline.append(childOutline)
    # Ajouter un signet parent dans la collection de contours du document.
    document.outlines.append(outline)

    # Sauvegarder le résultat
    document.save(output_pdf)
```


## Supprimer tous les signets d'un document PDF

Tous les signets d'un PDF sont contenus dans la collection [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). Cet article explique comment supprimer tous les signets d'un fichier PDF.

Pour supprimer tous les signets d'un fichier PDF :

1. Appelez la méthode Delete de la collection [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
2. Enregistrez le fichier modifié en utilisant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) de l'objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

Les extraits de code suivants montrent comment supprimer tous les signets d'un document PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Supprimer tous les signets
    document.outlines.delete()

    # Enregistrer le fichier mis à jour
    document.save(output_pdf)

```

## Supprimer un signet particulier d'un document PDF

Pour supprimer un signet particulier d'un fichier PDF :

1. Passez le titre du signet comme paramètre à la méthode Delete de la collection [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/).
1. Ensuite, enregistrez le fichier mis à jour avec la méthode Save de l'objet Document.

La classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) fournit la collection [OutlineCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/). La méthode [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/outlinecollection/#methods) supprime tout signet avec le titre passé à la méthode.

Les extraits de code suivants montrent comment supprimer un signet particulier du document PDF.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Supprimer un contour particulier par titre
    document.outlines.delete("Child Outline")

    # Enregistrer le fichier mis à jour
    document.save(output_pdf)