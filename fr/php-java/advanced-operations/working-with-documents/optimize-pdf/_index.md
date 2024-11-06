---
title: Optimiser, Compresser ou Réduire la Taille d'un PDF en PHP
linktitle: Optimiser le Document PDF
type: docs
weight: 40
url: fr/php-java/optimize-pdf/
description: Optimiser le fichier PDF, réduire toutes les images, réduire la taille du PDF, désintégrer les polices, supprimer les objets inutilisés en utilisant PHP.
lastmod: "2024-06-05"
---

Un document PDF peut parfois contenir des données supplémentaires. Réduire la taille d'un fichier PDF vous aidera à optimiser le transfert et le stockage en réseau. Cela est particulièrement utile pour la publication sur des pages web, le partage sur les réseaux sociaux, l'envoi par e-mail ou l'archivage dans le stockage. Nous pouvons utiliser plusieurs techniques pour optimiser le PDF :

- Optimiser le contenu de la page pour la navigation en ligne
- Réduire ou compresser toutes les images
- Permettre la réutilisation du contenu des pages
- Fusionner les flux en double
- Désintégrer les polices
- Supprimer les objets inutilisés
- Supprimer les champs de formulaire aplatis
- Supprimer ou aplatir les annotations

## Optimiser le Document PDF pour le Web

L'optimisation ou la linéarisation fait référence au processus de rendre un fichier PDF adapté à la navigation en ligne à l'aide d'un navigateur web.
 Aspose.PDF prend en charge ce processus.

Pour optimiser un PDF pour l'affichage web :

1. Ouvrez le document d'entrée dans un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Utilisez la méthode [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--).
1. Enregistrez le document optimisé en utilisant la méthode save(..).

L'extrait de code suivant montre comment optimiser un document PDF pour le web.

```php

    // Ouvrir le document
    $document = new Document($inputFile);

    // Optimiser pour le web
    $document->optimize();

    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();
```

## Réduire la Taille du Fichier PDF

Ce sujet explique les étapes pour optimiser/réduire la taille du fichier PDF. Aspose.PDF API fournit la classe [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions) qui offre la flexibilité d'optimiser le PDF de sortie en supprimant les objets inutiles et en comprimant les fichiers PDF contenant des images. Ces deux options sont détaillées dans les sections suivantes.

### Supprimer les objets inutiles

Nous pouvons optimiser la taille des documents PDF en supprimant les objets en double et inutilisés. Le code suivant montre comment procéder.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    
    // Optimiser le document PDF. Notez cependant que cette méthode ne peut pas garantir
    // la réduction du document
    $document->optimizeResources();

    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();

```

## Réduire ou compresser toutes les images

Si le fichier PDF source contient des images, envisagez de compresser les images et de définir leur qualité. Afin d'activer la compression d'images, passez true comme argument à la méthode setCompressImages(..). Toutes les images d'un document seront recompressées. La compression est définie par la méthode setImageQuality(..), qui est la valeur de la qualité en pourcentage. 100% est une qualité inchangée et une taille d'image inchangée. Pour diminuer la taille de l'image, passez un argument inférieur à 100 à la méthode setImageQuality(..).

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    
    // Initialiser les options d'optimisation
    $optimizationOptions = new OptimizationOptions();

    // Définir l'option CompressImages
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // Définir l'option ImageQuality
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(50);

    // Optimiser le document PDF en utilisant les options d'optimisation
    $document->optimizeResources($optimizationOptions);

    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();
```

Une autre méthode consiste à redimensionner les images avec une résolution plus basse. Dans ce cas, nous devrions définir ResizeImages sur true et MaxResolution sur la valeur appropriée.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    
    // Initialiser les options d'optimisation
    $optimizationOptions = new OptimizationOptions();

    // Définir l'option CompressImages
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);
    
    // Définir l'option ImageQuality
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);

    // Définir l'option ResizeImage
    $optimizationOptions->getImageCompressionOptions()->setResizeImages(true);

    // Définir l'option MaxResolution
    $optimizationOptions->getImageCompressionOptions()->setMaxResolution(300);

    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();
```

Un autre problème important est le temps d'exécution. Mais encore une fois, nous pouvons également gérer ce paramètre. Actuellement, nous pouvons utiliser deux algorithmes - Standard et Rapide. Pour contrôler le temps d'exécution, nous devons définir une propriété Version. L'extrait suivant démontre l'algorithme Rapide :

```php
    // Ouvrir le document
    $document = new Document($inputFile);
    
    // Initialiser OptimizationOptions
    $optimizationOptions = new optimization_OptimizationOptions();

    // Définir l'option CompressImages
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // Définir l'option ImageQuality
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);
    $optimization_ImageCompressionVersion = new optimization_ImageCompressionVersion();

    // Définir la version de compression d'image à rapide
    $optimizationOptions->getImageCompressionOptions()->setVersion($optimization_ImageCompressionVersion->Fast);

    // Optimiser le document PDF en utilisant OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();
```

## Suppression des objets inutilisés

Un document PDF contient parfois des objets PDF qui ne sont référencés par aucun autre objet dans le document. Cela peut arriver, par exemple, lorsqu'une page est supprimée de l'arborescence des pages du document, mais que l'objet de la page lui-même n'est pas supprimé. Supprimer ces objets ne rend pas le document invalide mais le réduit plutôt.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    
    // Initialiser les options d'optimisation
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedObjects(true);

    // Optimiser le document PDF en utilisant les options d'optimisation
    $document->optimizeResources($optimizationOptions);

    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();
```

## Suppression des flux inutilisés

Parfois, un document contient des flux de ressources inutilisés.
 Ces flux ne sont pas des « objets inutilisés » car ils sont référencés à partir du dictionnaire des ressources d'une page. Cela peut se produire dans des cas où une image a été supprimée de la page mais pas des ressources de la page. De plus, cette situation se produit souvent lorsque les pages sont extraites du document et que les pages du document ont des ressources « communes », c'est-à-dire le même objet Resources. Le contenu des pages est analysé afin de déterminer si un flux de ressources est utilisé ou non. Les flux inutilisés sont supprimés. Parfois, cela diminue la taille du document.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    
    // Initialiser OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedStreams(true);

    // Optimiser le document PDF en utilisant OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();
```

## Lier les flux en double

Parfois, un document contient plusieurs flux de ressources identiques (par exemple des images). Cela peut se produire par exemple lorsqu'un document est concaténé avec lui-même. Le document de sortie contient deux copies indépendantes du même flux de ressources. Nous analysons tous les flux de ressources et les comparons. Si les flux sont dupliqués, ils sont fusionnés, c'est-à-dire qu'une seule copie est conservée, les références sont modifiées en conséquence et les copies de l'objet sont supprimées. Parfois, cela réduit la taille du document.

```php
    // Ouvrir le document
    $document = new Document($inputFile);
    
    // Initialiser les options d'optimisation
    $optimizationOptions = new OptimizationOptions();
    
    $optimizationOptions->setLinkDuplcateStreams(true);
    
    // Optimiser le document PDF en utilisant les options d'optimisation
    $document->optimizeResources($optimizationOptions);

    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();
```

De plus, nous pouvons utiliser les paramètres AllowReusePageContent. Si cette propriété est définie sur true, le contenu de la page sera réutilisé lors de l'optimisation du document pour les pages identiques.

```php
    // Ouvrir le document
    $document = new Document($inputFile);
    
    // Initialiser les options d'optimisation
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setAllowReusePageContent(true);

    // Optimiser le document PDF en utilisant les options d'optimisation
    $document->optimizeResources($optimizationOptions);

    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();
```

## Désintégration des Polices

Si le document utilise des polices incorporées, cela signifie que toutes les données de police sont placées dans le document. L'avantage est que le document est visible indépendamment de l'installation ou non de la police sur l'ordinateur de l'utilisateur. Mais l'incorporation de polices rend le document plus volumineux. La méthode de désintégration des polices supprime toutes les polices incorporées. Cela réduit la taille du document, mais le document peut devenir illisible si la police correcte n'est pas installée.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    
    // Initialiser les Options d'Optimisation
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // Optimiser le document PDF en utilisant les Options d'Optimisation
    $document->optimizeResources($optimizationOptions);

    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();
```

## Suppression ou Aplatissement des Annotations

Les annotations peuvent être supprimées lorsqu'elles sont inutiles.
 Quand ils sont nécessaires mais ne nécessitent pas d'édition supplémentaire, ils peuvent être aplatis. Ces deux techniques réduiront la taille du fichier.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    $pages = $document->getPages();

    for ($i=1; $i < $pages->size() ; $i++) { 
        $page = $pages->get_Item($i);
        $annotations = $page->getAnnotations();
        for ($idx=0; $idx < $annotations->size(); $idx++) { 
            $annotation = $annotations->get_Item($idx);
            $annotation->flatten();
        }
    }
     
    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();
```

## Suppression des champs de formulaire

Si le document PDF contient des AcroForms, nous pouvons essayer de réduire la taille du fichier en aplatissant les champs de formulaire.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    
    // Aplatir les formulaires
    $fields = $document->getForm()->getFields();
    foreach ($fields as $field) {
        $field->flatten();
    }            

    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();
```

## Convertir un PDF de l'espace colorimétrique RVB en niveaux de gris

Un fichier PDF est composé de texte, d'image, de pièce jointe, d'annotations, de graphiques et d'autres objets. Vous pouvez avoir besoin de convertir un PDF de l'espace colorimétrique RVB en niveaux de gris afin qu'il soit plus rapide lors de l'impression de ces fichiers PDF. De plus, lorsque le fichier est converti en niveaux de gris, la taille du document est également réduite, mais avec ce changement, la qualité du document peut diminuer. Actuellement, cette fonctionnalité est prise en charge par la fonction Pre-Flight d'Adobe Acrobat, mais lorsqu'il s'agit d'automatisation de bureau, Aspose.PDF est une solution ultime pour fournir de tels avantages pour la manipulation de documents.

Pour réaliser cette exigence, le code suivant peut être utilisé.

```php

    // Ouvrir le document
    $document = new Document($inputFile);
    
    $strategy = new RgbToDeviceGrayConversionStrategy();
    for ($idxPage = 1; $idxPage <= $document->getPages()->size(); $idxPage++) {
        $page = $document->getPages()->get_Item($idxPage);
        $strategy->convert($page);
    }          

    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();
```


## Compression FlateDecode

Aspose.PDF pour PHP via Java offre la prise en charge de la compression FlateDecode pour la fonctionnalité d'optimisation PDF. Le code suivant montre comment utiliser l'option dans l'Optimisation pour stocker des images avec la compression FlateDecode :

```php

    // Ouvrir le document
    $document = new Document($inputFile);

    // Initialiser OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // Optimiser le document PDF en utilisant OptimizationOptions
    $optimizationOptions->getImageCompressionOptions()->setEncoding(optimization_ImageEncoding::$Flate);

    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();
```

## Stocker l'Image dans XImageCollection

Aspose.PDF pour PHP via Java offre la possibilité de stocker de nouvelles images dans [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection) avec la compression FlateDecode.
 Pour activer cette option, vous pouvez utiliser le drapeau ImageFilterType.Flate. Le code suivant montre comment utiliser cette fonctionnalité :

```php
    // Ouvrir le document
    $document = new Document($inputFile);

    // Initialiser le document
    $page = $document->getPages()->get_Item(1);

    // Charger l'image dans le flux
    $imageStream = new java("java.io.FileInputStream",$inputFile);
    $imageFilterType = new ImageFilterType();
    $page->getResources()->getImages()->add($imageStream, $imageFilterType->Flate);
    $idx = $page->getResources()->getImages()->size();
    $ximage = $page->getResources()->getImages()->get_Item($idx);
    $page->getContents()->add(new operators_GSave());

    // Définir les coordonnées
    $lowerLeftX = 0;
    $lowerLeftY = 0;
    $upperRightX = 600;
    $upperRightY = 600;
    $rectangle = new Rectangle($lowerLeftX, $lowerLeftY, $upperRightX, $upperRightY);
    $matrixData = [
        $rectangle->getURX() - $rectangle->getLLX(), 0, 
        0, $rectangle->getURY() - $rectangle->getLLY(), 
        $rectangle->getLLX(), $rectangle->getLLY()];
    $matrix = new Matrix($matrixData);

    // Utilisation de l'opérateur ConcatenateMatrix (concatenation de matrice) : définit comment l'image doit être placée
    $page->getContents()->add(new operators_ConcatenateMatrix($matrix));
    $page->getContents()->add(new operators_Do($ximage->getName()));
    $page->getContents()->add(new operators_GRestore());

    // Enregistrer le document mis à jour
    $document->save($outputFile);
    $document->close();
```