---
title: Optimiser, compresser ou réduire la taille d'un PDF en Python
linktitle: Optimiser le PDF
type: docs
weight: 30
url: /fr/python-net/optimize-pdf/
description: Apprenez comment optimiser les documents PDF en Python pour améliorer les performances web et réduire la taille du fichier en utilisant Aspose.PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Compresser les pages PDF avec Python
Abstract: Cet article fournit un guide complet sur l'optimisation des fichiers PDF afin de réduire leur taille et d'améliorer les performances sur diverses plateformes, telles que les pages web, les courriels et les systèmes de stockage. Les techniques d'optimisation incluent la réduction de la taille des images, la suppression des ressources inutilisées et le désincorporation des polices. Des méthodes spécifiques pour optimiser les PDF pour le web et réduire la taille globale du fichier sont abordées, utilisant les méthodes `Optimize` et `OptimizeResources` d'Aspose.PDF pour Python. La personnalisation des stratégies d'optimisation est possible via `OptimizationOptions`, permettant des actions ciblées comme la compression des images, la suppression des objets et des flux inutilisés, la liaison des flux en double et le désincorporation des polices. Des stratégies supplémentaires couvrent l'aplatissement des annotations, la suppression des champs de formulaire, et la conversion des fichiers PDF de RVB en niveaux de gris pour réduire davantage la taille. L'article met également en avant l'utilisation de la compression FlateDecode pour l'optimisation des images, assurant une gestion efficace des fichiers PDF tout en maintenant la qualité et les fonctionnalités.
---

Un document PDF peut parfois contenir des données supplémentaires. Réduire la taille d'un fichier PDF vous aidera à optimiser le transfert réseau et le stockage. Cela est particulièrement utile pour la publication sur des pages web, le partage sur les réseaux sociaux, l'envoi par e‑mail ou l'archivage. Nous pouvons utiliser plusieurs techniques pour optimiser les PDF :

- Optimiser le contenu des pages pour la navigation en ligne
- Réduire ou compresser toutes les images
- Permettre la réutilisation du contenu des pages
- Fusionner les flux en double
- Désincorporer les polices
- Supprimer les objets inutilisés
- Supprimer les champs de formulaire aplatis
- Supprimer ou aplatir les annotations

{{% alert color="primary" %}}

Une explication détaillée des méthodes d'optimisation peut être trouvée sur la page Aperçu des méthodes d'optimisation.

{{% /alert %}}

## Optimiser le document PDF pour le Web

L'optimisation, ou linéarisation pour le Web, désigne le processus qui rend un fichier PDF adapté à la navigation en ligne via un navigateur web. Pour optimiser un fichier pour l'affichage web :

1. Ouvrez le document d'entrée dans un objet [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Utilisez la méthode [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. Enregistrez le document optimisé en utilisant la méthode [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

Le segment de code suivant montre comment optimiser un document PDF pour le web.

```python

    import aspose.pdf as ap

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    document.optimize()
    document.save(path_outfile)
```

## Réduire la taille du PDF

La méthode [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) vous permet de réduire la taille du document en éliminant les informations inutiles. Par défaut, cette méthode fonctionne comme suit :

- Les ressources qui ne sont pas utilisées sur les pages du document sont supprimées
- Les ressources identiques sont fusionnées en un seul objet
- Les objets inutilisés sont supprimés

L'extrait ci‑dessous est un exemple. Notez toutefois que cette méthode ne peut pas garantir la réduction du document.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(output_pdf)
```

## Gestion de la stratégie d'optimisation

Nous pouvons également personnaliser la stratégie d'optimisation. Actuellement, la méthode [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) utilise 5 techniques. Ces techniques peuvent être appliquées en utilisant la méthode OptimizeResources() avec le paramètre [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/).

### Réduction ou compression de toutes les images

Nous avons deux façons de travailler avec les images : réduire la qualité de l'image et/ou changer sa résolution. Dans tous les cas, [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) doit être appliqué. Dans l'exemple suivant, nous réduisons les images en diminuant ImageQuality à 50.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Suppression des objets inutilisés

Un document PDF contient parfois des objets PDF qui ne sont référencés par aucun autre objet du document. Cela peut se produire, par exemple, lorsqu'une page est supprimée de l'arborescence des pages du document mais que l'objet page lui‑même n’est pas retiré. La suppression de ces objets ne rend pas le document invalide, mais le réduit.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set RemoveUsedObject option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Suppression des flux inutilisés

Parfois, le document contient des flux de ressources inutilisés. Ces flux ne sont pas des « objets inutilisés » car ils sont référencés depuis le dictionnaire des ressources d’une page. Ainsi, ils ne sont pas supprimés par la méthode « supprimer les objets inutilisés ». Cependant, ces flux ne sont jamais utilisés dans le contenu des pages. Cela peut se produire lorsqu’une image a été retirée de la page mais pas des ressources de la page. De plus, cette situation survient souvent lorsque des pages sont extraites du document et que les pages du document partagent des ressources « communes », c’est‑à‑dire le même objet Resources. Le contenu des pages est analysé afin de déterminer si un flux de ressources est utilisé ou non. Les flux inutilisés sont supprimés. Cela diminue parfois la taille du document. L’utilisation de cette technique est similaire à l’étape précédente :

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set RemoveUsedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Liaison des flux en double

Certains documents peuvent contenir plusieurs flux de ressources identiques (comme des images, par exemple). Cela peut se produire, par exemple, lorsqu'un document est concaténé avec lui‑même. Le document de sortie contient deux copies indépendantes du même flux de ressources. Nous analysons tous les flux de ressources et les comparons. Si les flux sont dupliqués, ils sont fusionnés, c’est‑à‑dire qu’il ne reste qu’une seule copie. Les références sont modifiées en conséquence et les copies de l’objet sont supprimées. Dans certains cas, cela contribue à diminuer la taille du document.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set LinkDuplicateStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplcate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Désincorporation des polices

Si le document utilise des polices incorporées, cela signifie que toutes les données de la police sont stockées dans le document. L’avantage est que le document est affichable quel que soit l’état d’installation de la police sur la machine de l’utilisateur. Mais l’incorporation des polices augmente la taille du document. La méthode de désincorporation des polices supprime toutes les polices incorporées. Ainsi, la taille du document diminue, mais le document peut devenir illisible si la police correcte n’est pas installée.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set UnembedFonts  option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
    file_stats_1 = os.stat(input_pdf)
    file_stats_2 = os.stat(output_pdf)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

Les ressources d'optimisation appliquent ces méthodes au document. Si l’une de ces méthodes est appliquée, la taille du document diminuera très probablement. Si aucune de ces méthodes n’est appliquée, la taille du document ne changera pas, ce qui est évident.

## Moyens supplémentaires de réduire la taille du document PDF

### Supprimer ou aplatir les annotations

Les annotations peuvent être supprimées lorsqu'elles ne sont pas nécessaires. Lorsqu'elles sont nécessaires mais ne nécessitent pas d'édition supplémentaire, elles peuvent être aplaties. Ces deux techniques permettront de réduire la taille du fichier.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(output_pdf)
```

### Suppression des champs de formulaire

Si le document PDF contient des AcroForms, nous pouvons essayer de réduire la taille du fichier en aplatissant les champs de formulaire.

```python

    import aspose.pdf as ap

    # Load source PDF form
    doc = ap.Document(input_pdf)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(output_pdf)
```

### Convertir un PDF de l'espace colorimétrique RGB en niveaux de gris

Un fichier PDF comprend du texte, des images, des pièces jointes, des annotations, des graphiques et d'autres objets. Vous pouvez être amené à convertir un PDF de l'espace colorimétrique RGB en niveaux de gris afin d'accélérer l'impression de ces fichiers PDF. De plus, lorsque le fichier est converti en niveaux de gris, la taille du document est également réduite, mais cela peut également entraîner une diminution de la qualité du document. Cette fonctionnalité est actuellement prise en charge par la fonction Pre‑Flight d'Adobe Acrobat, mais lorsqu'il s'agit d'automatisation Office, Aspose.PDF est une solution ultime pour offrir de telles possibilités de manipulation de documents. Pour répondre à cette exigence, le fragment de code suivant peut être utilisé.

```python

    import aspose.pdf as ap

    # Load source PDF file
    document = ap.Document(input_pdf)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(output_pdf)
```

### Compression FlateDecode

Aspose.PDF pour Python via .NET prend en charge la compression FlateDecode pour la fonctionnalité d'optimisation PDF. Le fragment de code suivant montre comment utiliser l'option d'optimisation pour stocker les images avec une compression **FlateDecode** :

```python

    import aspose.pdf as ap

    # Open Document
    doc = ap.Document(input_pdf)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(output_pdf)
```


