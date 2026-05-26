---
title: Optimiser les fichiers PDF en Python
linktitle: Optimiser le PDF
type: docs
weight: 30
url: /fr/python-net/optimize-pdf/
description: Apprenez à optimiser, compresser et réduire la taille des fichiers PDF en Python avec Aspose.PDF.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Compressez les pages PDF en utilisant Python.
Abstract: Cet article fournit un guide complet sur l'optimisation des fichiers PDF afin de réduire leur taille et d'améliorer les performances sur diverses plateformes, telles que les pages Web, les e‑mails et les systèmes de stockage. Les techniques d'optimisation comprennent la réduction de la taille des images, la suppression des ressources inutilisées et le désintégration des polices. Des méthodes spécifiques pour optimiser les PDF pour le Web et réduire la taille globale du fichier sont abordées, en utilisant les méthodes `Optimize` et `OptimizeResources` dans Aspose.PDF for Python. La personnalisation des stratégies d'optimisation est possible via `OptimizationOptions`, permettant des actions ciblées comme la compression des images, la suppression des objets et flux inutilisés, la liaison des flux dupliqués et le désintégration des polices. Des stratégies supplémentaires couvrent l'aplatissement des annotations, la suppression des champs de formulaire et la conversion des fichiers PDF de RVB en niveaux de gris pour réduire davantage la taille. L'article met également en avant l'utilisation de la compression FlateDecode pour l'optimisation des images, garantissant une gestion efficace des fichiers PDF tout en maintenant la qualité et la fonctionnalité.
---

Un document PDF peut parfois contenir des données supplémentaires. Réduire la taille d'un fichier PDF vous aidera à optimiser le transfert réseau et le stockage. Cela est particulièrement pratique pour la publication sur des pages web, le partage sur les réseaux sociaux, l'envoi par e‑mail ou l'archivage. Nous pouvons utiliser plusieurs techniques pour optimiser le PDF :

Utilisez cette page lorsque vous devez réduire la taille du PDF pour la diffusion sur le Web, le partage par e‑mail, les économies de stockage ou une sortie adaptée à l’impression, sans reconstruire le document à partir de zéro.

- Optimiser le contenu de la page pour la navigation en ligne
- Réduire ou compresser toutes les images
- Activer la réutilisation du contenu de la page
- Fusionner les flux dupliqués
- Désincorporer les polices
- Supprimer les objets inutilisés
- Supprimer l’aplatissement des champs de formulaire
- Supprimer ou aplatir les annotations

{{% alert color="primary" %}}

 Une explication détaillée des méthodes d'optimisation se trouve sur la page Aperçu des méthodes d'optimisation.

{{% /alert %}}

## Optimiser le document PDF pour le Web

L'optimisation, ou linéarisation pour le Web, désigne le processus consistant à rendre un fichier PDF adapté à la navigation en ligne à l'aide d'un navigateur Web. Pour optimiser un fichier pour l'affichage Web :

1. Ouvrez le document d'entrée dans un [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objet.
1. Utilisez le [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode.
1. Enregistrez le document optimisé en utilisant le [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode.

Le fragment de code suivant montre comment optimiser un document PDF pour le Web.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def optimize_pdf(infile, outfile):
    document = ap.Document(infile)
    document.optimize()
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## Réduire la taille du PDF

Le [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) La méthode vous permet de réduire la taille du document en éliminant les informations inutiles. Par défaut, cette méthode fonctionne comme suit :

- Les ressources qui ne sont pas utilisées sur les pages du document sont supprimées
- Les ressources égales sont regroupées en un seul objet
- Les objets inutilisés sont supprimés

L'extrait ci-dessous est un exemple. Notez cependant que cette méthode ne peut garantir une réduction du document.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def reduce_size_pdf(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## Gestion de la stratégie d'optimisation

Nous pouvons également personnaliser la stratégie d'optimisation. Actuellement, le [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) La méthode utilise 5 techniques. Ces techniques peuvent être appliquées en utilisant la méthode OptimizeResources() avec le [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) paramètre.

### Réduction ou compression de toutes les images

Nous avons deux façons de travailler avec les images : réduire la qualité de l'image et/ou changer leur résolution. Dans tous les cas, [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) doit être appliqué. Dans l'exemple suivant, nous réduisons les images en diminuant ImageQuality à 50.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def shrinking_or_compressing_all_images(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Suppression des objets inutilisés

Un document PDF contient parfois des objets PDF qui ne sont référencés par aucun autre objet du document. Cela peut se produire, par exemple, lorsqu’une page est supprimée de l’arborescence des pages du document mais que l’objet de la page lui‑même n’est pas supprimé. La suppression de ces objets ne rend pas le document invalide, mais le réduit.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_objects(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedObjects option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Suppression des flux inutilisés

Parfois, le document contient des flux de ressources inutilisés. Ces flux ne sont pas « unused objects » car ils sont référencés depuis le dictionnaire de ressources d’une page. Ainsi, ils ne sont pas supprimés avec la méthode « remove unused objects ». Mais ces flux ne sont jamais utilisés avec le contenu des pages. Cela peut se produire dans les cas où une image a été supprimée de la page mais pas des ressources de la page. De plus, cette situation survient souvent lorsque des pages sont extraites du document et que les pages du document ont des ressources « common », c’est‑à‑dire le même objet Resources. Le contenu des pages est analysé afin de déterminer si un flux de ressources est utilisé ou non. Les flux inutilisés sont supprimés. Cela diminue parfois la taille du document. L’utilisation de cette technique est similaire à l’étape précédente :

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Lier les flux dupliqués

Certains documents peuvent contenir plusieurs flux de ressources identiques (comme des images, par exemple). Cela peut se produire, par exemple lorsqu'un document est concaténé avec lui‑même. Le document de sortie contient deux copies indépendantes du même flux de ressources. Nous analysons tous les flux de ressources et les comparons. Si des flux sont dupliqués, ils sont fusionnés, c’est‑à‑dire qu’il ne reste qu’une seule copie. Les références sont modifiées en conséquence, et les copies de l’objet sont supprimées. Dans certains cas, cela aide à réduire la taille du document.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def linking_duplicate_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set link_duplicate_streams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplicate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Désincorporation des polices

Si le document utilise des polices incorporées, cela signifie que toutes les données de police sont stockées dans le document. L'avantage est que le document peut être visualisé quel que soit le fait que la police soit installée ou non sur la machine de l'utilisateur. Cependant, l'incorporation de polices augmente la taille du document. La méthode de désincorporation des polices supprime toutes les polices incorporées. Ainsi, la taille du document diminue, mais le document lui‑même peut devenir illisible si la police correcte n'est pas installée.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def unembed_fonts(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set unembed_fonts option
    optimize_options = ap.optimization.OptimizationOptions()
    optimize_options.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimize_options)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

Les ressources d'optimisation appliquent ces méthodes au document. Si l'une de ces méthodes est appliquée, la taille du document diminuera très probablement. Si aucune de ces méthodes n'est appliquée, la taille du document ne changera pas, ce qui est évident.

## Moyens supplémentaires pour réduire la taille du Document PDF

### Suppression ou aplatissage des annotations

Les annotations peuvent être supprimées lorsqu'elles ne sont pas nécessaires. Lorsqu'elles sont nécessaires mais ne nécessitent pas d'édition supplémentaire, elles peuvent être aplaties. Les deux techniques permettront de réduire la taille du fichier.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_annotations(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(outfile)
```

### Suppression des Form Fields

Si le document PDF contient des AcroForms, nous pouvons essayer de réduire la taille du fichier en aplatissant les champs de formulaire.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_forms(infile, outfile):
    # Load source PDF form
    doc = ap.Document(infile)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Convertir un PDF de l'espace colorimétrique RVB en niveaux de gris

Un fichier PDF comprend du texte, des images, des pièces jointes, des annotations, des graphiques et d'autres objets. Vous pourriez rencontrer le besoin de convertir un PDF de l'espace couleur RGB en niveaux de gris afin que l'impression de ces fichiers PDF soit plus rapide. De plus, lorsque le fichier est converti en niveaux de gris, la taille du document est également réduite, mais cela peut également entraîner une diminution de la qualité du document. Cette fonctionnalité est actuellement prise en charge par la fonctionnalité Pre-Flight d'Adobe Acrobat, mais lorsqu'il s'agit d'automatisation de bureau, Aspose.PDF est une solution ultime pour offrir de tels avantages lors des manipulations de documents. Pour répondre à ce besoin, le fragment de code suivant peut être utilisé.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def сonvert_PDF_from_RGB_colorspace_to_grayscale(infile, outfile):
    document = ap.Document(infile)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(outfile)
```

### Compression FlateDecode

Aspose.PDF for Python via .NET fournit la prise en charge de la compression FlateDecode pour la fonctionnalité d'optimisation PDF. Le fragment de code suivant montre comment utiliser l'option d'Optimisation pour stocker les images avec la compression **FlateDecode** :

```python
import aspose.pdf as ap
from os import path, stat
import sys


def using_flatedecode_compression(infile, outfile):

    # Open Document
    doc = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = (
        ap.optimization.ImageEncoding.FLATE
    )
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(outfile)
```

## Sujets de documents associés

- [Travailler avec des documents PDF en Python](/pdf/fr/python-net/working-with-documents/)
- [Fusionner des fichiers PDF en Python](/pdf/fr/python-net/merge-pdf-documents/)
- [Diviser les fichiers PDF en Python](/pdf/fr/python-net/split-document/)
- [Manipuler des documents PDF en Python](/pdf/fr/python-net/manipulate-pdf-document/)

