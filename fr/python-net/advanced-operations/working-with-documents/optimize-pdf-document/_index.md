---
title: Optimiser, Compresser ou Réduire la Taille du PDF en Python
linktitle: Optimiser PDF
type: docs
weight: 30
url: /fr/python-net/optimize-pdf/
keywords: "optimiser pdf python"
description: Optimiser le fichier PDF, réduire toutes les images, réduire la taille du PDF, désintégrer les polices, supprimer les objets inutilisés avec Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Optimiser PDF avec Python",
    "alternativeHeadline": "Comment optimiser PDF avec Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "génération de documents pdf",
    "keywords": "pdf, python, optimiser pdf",
    "wordcount": "302",
    "proficiencyLevel":"Débutant",
    "publisher": {
        "@type": "Organization",
        "name": "Équipe Doc Aspose.PDF",
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
    "url": "/python-net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/optimize-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Optimiser le fichier PDF, réduire toutes les images, réduire la taille du PDF, désintégrer les polices, supprimer les objets inutilisés avec Python."
}
</script>


Un document PDF peut parfois contenir des données supplémentaires. Réduire la taille d'un fichier PDF vous aidera à optimiser le transfert réseau et le stockage. Cela est particulièrement utile pour la publication sur des pages web, le partage sur les réseaux sociaux, l'envoi par e-mail ou l'archivage dans le stockage. Nous pouvons utiliser plusieurs techniques pour optimiser les PDF :

- Optimiser le contenu des pages pour la navigation en ligne
- Réduire ou compresser toutes les images
- Activer la réutilisation du contenu des pages
- Fusionner les flux en double
- Désembedder les polices
- Supprimer les objets inutilisés
- Supprimer les champs de formulaire aplatis
- Supprimer ou aplatir les annotations

{{% alert color="primary" %}}

 Une explication détaillée des méthodes d'optimisation peut être trouvée dans la page Vue d'ensemble des méthodes d'optimisation.

{{% /alert %}}

## Optimiser un document PDF pour le Web

L'optimisation, ou linéarisation pour le Web, fait référence au processus de rendre un fichier PDF adapté à la navigation en ligne à l'aide d'un navigateur web. Pour optimiser un fichier pour l'affichage sur le web :

1. Ouvrez le document d'entrée dans un objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Utilisez la méthode [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. Enregistrez le document optimisé en utilisant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Le snippet de code suivant montre comment optimiser un document PDF pour le web.

```python 

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)

    # Optimiser pour le web
    document.optimize()

    # Enregistrer le document de sortie
    document.save(output_pdf)
```

## Réduire la taille du PDF

La méthode [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) vous permet de réduire la taille du document en éliminant les informations inutiles. Par défaut, cette méthode fonctionne comme suit :

- Les ressources qui ne sont pas utilisées sur les pages du document sont supprimées
- Les ressources égales sont fusionnées en un seul objet

- Les objets non utilisés sont supprimés

Le snippet ci-dessous est un exemple. Notez cependant que cette méthode ne peut pas garantir la réduction du document.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)
    # Optimiser le document PDF. Notez cependant que cette méthode ne peut pas garantir la réduction du document
    document.optimize_resources()
    # Enregistrer le document mis à jour
    document.save(output_pdf)
```

## Gestion de la Stratégie d'Optimisation

Nous pouvons également personnaliser la stratégie d'optimisation. Actuellement, la méthode [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) utilise 5 techniques. Ces techniques peuvent être appliquées en utilisant la méthode OptimizeResources() avec le paramètre [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/).

### Réduire ou Compresser Toutes les Images

Nous avons deux façons de travailler avec les images : réduire la qualité de l'image et/ou changer leur résolution.
 Dans tous les cas, [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) devrait être appliqué. Dans l'exemple suivant, nous réduisons les images en diminuant la qualité de l'image à 50.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)
    # Initialiser OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Définir l'option CompressImages
    optimizeOptions.image_compression_options.compress_images = True
    # Définir l'option ImageQuality
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimiser le document PDF en utilisant OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Enregistrer le document mis à jour
    document.save(output_pdf)
```

### Suppression des objets inutilisés

Un document PDF contient parfois des objets PDF qui ne sont référencés par aucun autre objet dans le document. Cela peut se produire, par exemple, lorsqu'une page est supprimée de l'arborescence des pages du document mais que l'objet de la page lui-même n'est pas supprimé. Supprimer ces objets ne rend pas le document invalide mais le réduit plutôt.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)
    # Définir l'option RemoveUsedObject
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimiser le document PDF en utilisant OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Enregistrer le document mis à jour
    document.save(output_pdf)
```

### Suppression des flux inutilisés

Parfois, le document contient des flux de ressources inutilisés. These streams are not “unused objects” because they are referenced from a page resource dictionary. Thus, they are not removed with a “remove unused objects” method. But these streams are never used with the page contents. This may happen in cases when an image has been removed from the page but not from the page resources. Also, this situation often occurs when pages are extracted from the document and document pages have “common” resources, that is, the same Resources object. Page contents are analyzed in order to determine if a resource stream is used or not. Unused streams are removed. It sometimes decreases the document size. The use of this technique is similar to the previous step:

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)
    # Définir l'option RemoveUsedStreams
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimiser le document PDF en utilisant OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Enregistrer le document mis à jour
    document.save(output_pdf)
```

### Liaison des Flux en Double

Certains documents peuvent contenir plusieurs flux de ressources identiques (comme des images, par exemple). Cela peut se produire, par exemple, lorsqu'un document est concaténé avec lui-même. Le document de sortie contient deux copies indépendantes du même flux de ressources. Nous analysons tous les flux de ressources et les comparons. Si des flux sont dupliqués, ils sont fusionnés, c'est-à-dire qu'une seule copie est conservée. Les références sont modifiées en conséquence, et les copies de l'objet sont supprimées. Dans certains cas, cela permet de réduire la taille du document.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)
    # Définir l'option LinkDuplcateStreams
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplcate_streams = True
    # Optimiser le document PDF en utilisant OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Enregistrer le document mis à jour
    document.save(output_pdf)
```

### Désintégration des Polices

Si le document utilise des polices intégrées, cela signifie que toutes les données de police sont stockées dans le document.
 L'avantage est que le document est consultable, que la police soit installée sur la machine de l'utilisateur ou non. Mais l'incorporation des polices rend le document plus volumineux. La méthode de suppression des polices intégrées supprime toutes les polices intégrées. Ainsi, la taille du document diminue, mais le document lui-même peut devenir illisible si la police correcte n'est pas installée.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)
    # Définir l'option UnembedFonts
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.unembed_fonts = True
    # Optimiser le document PDF en utilisant OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Enregistrer le document mis à jour
    document.save(output_pdf)
    file_stats_1 = os.stat(input_pdf)
    file_stats_2 = os.stat(output_pdf)
    print(
        "Taille du fichier original : {}. Taille du fichier réduite : {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

Les ressources d'optimisation appliquent ces méthodes au document. Si l'une de ces méthodes est appliquée, la taille du document diminuera probablement. Si aucune de ces méthodes n'est appliquée, la taille du document ne changera pas, ce qui est évident.

## Moyens supplémentaires pour réduire la taille du document PDF

### Suppression ou aplatissement des annotations

Les annotations peuvent être supprimées lorsqu'elles sont inutiles. Lorsqu'elles sont nécessaires mais ne nécessitent pas de modifications supplémentaires, elles peuvent être aplaties. Ces deux techniques réduiront la taille du fichier.

```python

    import aspose.pdf as ap

    # Ouvrir le document
    document = ap.Document(input_pdf)
    # Aplatir les annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Enregistrer le document mis à jour
    document.save(output_pdf)
```

### Suppression des champs de formulaire

Si le document PDF contient des AcroForms, nous pouvons essayer de réduire la taille du fichier en aplatissant les champs de formulaire.

```python

    import aspose.pdf as ap

    # Charger le formulaire PDF source
    doc = ap.Document(input_pdf)

    # Aplatir les formulaires
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Enregistrer le document mis à jour
    doc.save(output_pdf)
```

### Convertir un PDF de l'espace colorimétrique RGB en niveaux de gris

Un fichier PDF comprend du texte, des images, des pièces jointes, des annotations, des graphiques et d'autres objets. Vous pouvez rencontrer le besoin de convertir un PDF de l'espace colorimétrique RGB en niveaux de gris afin qu'il soit plus rapide lors de l'impression de ces fichiers PDF. De plus, lorsque le fichier est converti en niveaux de gris, la taille du document est également réduite, mais cela peut également entraîner une diminution de la qualité du document. Cette fonctionnalité est actuellement prise en charge par la fonctionnalité Pre-Flight d'Adobe Acrobat, mais en ce qui concerne l'automatisation de bureau, Aspose.PDF est une solution ultime pour fournir de tels avantages pour les manipulations de documents. Pour répondre à cette exigence, le code suivant peut être utilisé.

```python

    import aspose.pdf as ap

    # Charger le fichier PDF source
    document = ap.Document(input_pdf)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convertir l'image de l'espace colorimétrique RGB en niveaux de gris
        strategy.convert(page)

    # Enregistrer le fichier résultant
    document.save(output_pdf)
```


### Compression FlateDecode

Aspose.PDF pour Python via .NET prend en charge la compression FlateDecode pour la fonctionnalité d'optimisation PDF. Le code ci-dessous montre comment utiliser l'option dans l'optimisation pour stocker des images avec la compression **FlateDecode** :

```python

    import aspose.pdf as ap

    # Ouvrir le document
    doc = ap.Document(input_pdf)
    # Initialiser les options d'optimisation
    optimizationOptions = ap.optimization.OptimizationOptions()
    # Pour optimiser l'image en utilisant la compression FlateDecode, définir les options d'optimisation sur Flate
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # Définir les options d'optimisation
    doc.optimize_resources(optimizationOptions)
    # Enregistrer le document
    doc.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>