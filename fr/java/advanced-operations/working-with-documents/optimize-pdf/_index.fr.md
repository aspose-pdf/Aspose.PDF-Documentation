---
title: Optimiser, compresser ou réduire la taille d'un PDF en Java
linktitle: Optimiser le document PDF
type: docs
weight: 40
url: /java/optimize-pdf/
description: Optimiser un fichier PDF, réduire toutes les images, réduire la taille du PDF, désincorporer les polices, supprimer les objets inutilisés avec Java.
lastmod: "2021-06-05"
---

Un document PDF peut parfois contenir des données supplémentaires. Réduire la taille d'un fichier PDF vous aidera à optimiser le transfert et le stockage réseau. Cela est particulièrement utile pour la publication sur des pages web, le partage sur les réseaux sociaux, l'envoi par e-mail ou l'archivage dans un stockage. Nous pouvons utiliser plusieurs techniques pour optimiser un PDF :

- Optimiser le contenu des pages pour la navigation en ligne
- Réduire ou compresser toutes les images
- Activer la réutilisation du contenu des pages
- Fusionner les flux en double
- Désincorporer les polices
- Supprimer les objets inutilisés
- Supprimer les champs de formulaire aplatis
- Supprimer ou aplatir les annotations

## Optimiser le document PDF pour le Web

L'optimisation ou la linéarisation se réfère au processus de rendre un fichier PDF adapté à la navigation en ligne à l'aide d'un navigateur web.
 Aspose.PDF prend en charge ce processus.

Pour optimiser un PDF pour l'affichage web :

1. Ouvrez le document d'entrée dans un objet [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Utilisez la méthode [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--).
1. Enregistrez le document optimisé en utilisant la méthode save(..).

L'extrait de code suivant montre comment optimiser un document PDF pour le web.

```java
package com.aspose.pdf.examples;

import java.io.FileNotFoundException;
import java.time.Clock;
import java.time.Duration;

import com.aspose.pdf.*;
import com.aspose.pdf.optimization.ImageCompressionVersion;
import com.aspose.pdf.optimization.ImageEncoding;

public class ExampleOptimize {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void OptimizePDFDocumentForTheWeb() {

        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Optimiser pour le web
        pdfDocument.optimize();

        // Enregistrer le document de sortie
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## Réduire la Taille du Fichier PDF

Ce sujet explique les étapes pour optimiser/réduire la taille du fichier PDF. L'API Aspose.PDF fournit la classe [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions) qui offre la flexibilité d'optimiser le PDF de sortie en supprimant les objets inutiles et en compressant les fichiers PDF contenant des images. Ces deux options sont expliquées dans les sections suivantes.

### Supprimer les Objets Inutiles
Nous pouvons optimiser la taille des documents PDF en supprimant les objets en double et inutilisés. Le code suivant montre comment.

```java
public static void ReduceSizePDF() {

        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // Optimiser le document PDF. Notez, cependant, que cette méthode ne
        // peut pas garantir la réduction du document
        pdfDocument.optimizeResources();

        // Enregistrer le document de sortie
        pdfDocument.save(_dataDir + "OptimizeDocument_out.pdf");
    }
```

## Rétrécir ou Compresser Toutes les Images

If le fichier PDF source contient des images, envisagez de compresser les images et de définir leur qualité. Afin d'activer la compression des images, passez true comme argument à la méthode setCompressImages(..). Toutes les images d'un document seront recompressées. La compression est définie par la méthode setImageQuality(..), qui est la valeur de la qualité en pourcentage. 100% correspond à une qualité et une taille d'image inchangées. Pour diminuer la taille de l'image, passez un argument inférieur à 100 à la méthode setImageQuality(..).

```java
public static void ShrinkingCompressing() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "Shrinkimage.pdf");

        // Initialiser les options d'optimisation
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Définir l'option de compression des images
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // Définir l'option de qualité de l'image
        optimizationOptions.getImageCompressionOptions().setImageQuality(50);

        // Optimiser le document PDF en utilisant les options d'optimisation
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "Shrinkimage_out.pdf";
        // Enregistrer le document mis à jour
        pdfDocument.save(_dataDir);
    }
```

Une autre façon est de redimensionner les images avec une résolution inférieure. Dans ce cas, nous devons définir ResizeImages sur true et MaxResolution sur la valeur appropriée.

```java
public static void ShrinkingCompressing2() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // Initialiser OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Définir l'option CompressImages
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);
        // Définir l'option ImageQuality
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // Définir l'option ResizeImage
        optimizationOptions.getImageCompressionOptions().setResizeImages(true);

        // Définir l'option MaxResolution
        optimizationOptions.getImageCompressionOptions().setMaxResolution(300);

        // Optimiser le document PDF en utilisant OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "ResizeImages_out.pdf";
        // Enregistrer le document mis à jour
        pdfDocument.save(_dataDir);
    }
```

Another important issue is the execution time. But again, we can manage this setting too. Currently, we can use two algorithms - Standard and Fast. To control the execution time we should set a Version property. The following snippet demonstrates the Fast algorithm:

Un autre problème important est le temps d'exécution. Mais encore une fois, nous pouvons également gérer ce paramètre. Actuellement, nous pouvons utiliser deux algorithmes - Standard et Rapide. Pour contrôler le temps d'exécution, nous devons définir une propriété Version. L'extrait suivant démontre l'algorithme Rapide :

```java
public static void ShrinkingCompressing3() {

        Clock clock = Clock.systemUTC();

        Duration tickDuration = Duration.ofNanos(250000);
        Clock clock1 = Clock.tick(clock, tickDuration);
        System.out.println("Start : " + clock.instant());

        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "ResizeImage.pdf");

        // Initialiser OptimizationOptions
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        // Définir l'option CompressImages
        optimizationOptions.getImageCompressionOptions().setCompressImages(true);

        // Définir l'option ImageQuality
        optimizationOptions.getImageCompressionOptions().setImageQuality(75);

        // Définir la version de compression d'image à rapide
        optimizationOptions.getImageCompressionOptions().setVersion(ImageCompressionVersion.Fast);

        // Optimiser le document PDF en utilisant OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "ResizeImages_out.pdf";

        // Enregistrer le document mis à jour
        pdfDocument.save(_dataDir);
        System.out.println("Finish : " + clock1.instant());
    }
```

## Suppression des objets inutilisés

Un document PDF contient parfois des objets PDF qui ne sont référencés par aucun autre objet dans le document. Cela peut se produire, par exemple, lorsqu'une page est supprimée de l'arborescence des pages du document mais que l'objet de la page lui-même n'est pas supprimé. Supprimer ces objets ne rend pas le document invalide mais le réduit plutôt.

```java
    public static void RemovingUnusedObjects() {

        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        
        optimizationOptions.setRemoveUnusedObjects(true);
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "emoveUnusedObjects_out.pdf";

        // Enregistrer le document mis à jour
        pdfDocument.save(_dataDir);

    }
```
## Suppression des flux inutilisés

Parfois, un document contient des flux de ressources inutilisés.
 Ces flux ne sont pas des « objets inutilisés » car ils sont référencés à partir du dictionnaire des ressources d'une page. Cela peut se produire dans des cas où une image a été retirée de la page mais pas des ressources de la page. De plus, cette situation se produit souvent lorsque des pages sont extraites du document et que les pages du document ont des ressources « communes », c'est-à-dire le même objet Resources. Le contenu des pages est analysé afin de déterminer si un flux de ressources est utilisé ou non. Les flux inutilisés sont supprimés. Parfois, cela diminue la taille du document.

```java
public static void RemovingUnusedStream() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + 
        "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "removeUnusedObjects_out.pdf";
        
        // Enregistrer le document mis à jour
        pdfDocument.save(_dataDir);
        
    }
```
## Lier des flux en double

Parfois, un document contient plusieurs flux de ressources identiques (par exemple, des images). Cela peut se produire, par exemple, lorsqu'un document est concaténé avec lui-même. Le document de sortie contient deux copies indépendantes du même flux de ressources. Nous analysons tous les flux de ressources et les comparons. Si les flux sont dupliqués, ils sont fusionnés, c'est-à-dire qu'une seule copie est conservée, les références sont modifiées en conséquence et les copies de l'objet sont supprimées. Parfois, cela réduit la taille du document.

```java
    public static void LinkingDuplicateStream() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setRemoveUnusedStreams(true);
        
        // Optimiser le document PDF à l'aide des options d'optimisation
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // Enregistrer le document mis à jour
        pdfDocument.save(_dataDir);
    }
```

De plus, nous pouvons utiliser les paramètres AllowReusePageContent. Si cette propriété est définie sur true, le contenu de la page sera réutilisé lors de l'optimisation du document pour des pages identiques.

```java
public static void AllowReusePageContent() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setAllowReusePageContent(true);
        
        // Optimiser le document PDF en utilisant OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        
        // Enregistrer le document mis à jour
        pdfDocument.save(_dataDir);
    }
```
## Désintégration des polices

Si le document utilise des polices intégrées, cela signifie que toutes les données de police sont placées dans le document.
 L'avantage est que le document est visible que la police soit installée ou non sur la machine de l'utilisateur. Mais l'intégration des polices rend le document plus volumineux. La méthode de désintégration des polices supprime toutes les polices intégrées. Cela diminue la taille du document, mais le document peut devenir illisible si la police correcte n'est pas installée.

```java
    public static void UnembedFonts() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();
        optimizationOptions.setUnembedFonts(true);
        
        // Optimiser le document PDF en utilisant OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);
        
        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // Enregistrer le document mis à jour
        pdfDocument.save(_dataDir);
    }
```

## Suppression ou Aplatissement des Annotations

Les annotations peuvent être supprimées lorsqu'elles sont inutiles. Lorsqu'ils sont nécessaires mais ne nécessitent pas de modification supplémentaire, ils peuvent être aplatis. Ces deux techniques réduiront la taille du fichier.

```java
    public static void FlatteningAnnotations() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        for (Page page : pdfDocument.getPages()) {
            for (Annotation annotation : page.getAnnotations())
                annotation.flatten();
        }

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // Enregistrer le document mis à jour
        pdfDocument.save(_dataDir);
    }

```
## Suppression des champs de formulaire

Si le document PDF contient des AcroForms, nous pouvons essayer de réduire la taille du fichier en aplatissant les champs de formulaire.

```java
    public static void RemovingFormFields() {
        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        // Aplatir les formulaires
        if (pdfDocument.getForm().getFields().length > 0) {
            for (Field field : pdfDocument.getForm().getFields()) {
                field.flatten();
            }
        }
        _dataDir = _dataDir + "FlattenForms_out.pdf";
        // Enregistrer le document mis à jour
        pdfDocument.save(_dataDir);
    }

```
## Convertir un PDF de l'espace colorimétrique RVB en niveaux de gris

Un fichier PDF est composé de texte, d'images, de pièces jointes, d'annotations, de graphiques et d'autres objets. Vous pouvez avoir besoin de convertir un PDF de l'espace colorimétrique RVB en niveaux de gris afin qu'il soit plus rapide lors de l'impression de ces fichiers PDF. De plus, lorsque le fichier est converti en niveaux de gris, la taille du document est également réduite, mais avec ce changement, la qualité du document peut diminuer. Actuellement, cette fonctionnalité est prise en charge par la fonctionnalité Pre-Flight d'Adobe Acrobat, mais lorsqu'il s'agit d'automatisation de bureau, Aspose.PDF est une solution ultime pour offrir de telles facilités pour la manipulation de documents.

Pour réaliser cette exigence, le code suivant peut être utilisé.

```java
    public static void ConvertRGBtoGrayscale() {

        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");

        com.aspose.pdf.RgbToDeviceGrayConversionStrategy strategy = new com.aspose.pdf.RgbToDeviceGrayConversionStrategy();
        for (int idxPage = 1; idxPage <= pdfDocument.getPages().size(); idxPage++) {
            Page page = pdfDocument.getPages().get_Item(idxPage);
            strategy.convert(page);
        }
        pdfDocument.save("output.pdf");
    }
```

## Compression FlateDecode

Aspose.PDF pour Java offre la prise en charge de la compression FlateDecode pour la fonctionnalité d'optimisation PDF. Le code ci-dessous montre comment utiliser l'option dans l'Optimisation pour stocker des images avec la compression FlateDecode :

```java
    public static void FlateDecodeCompression() {

        // Ouvrir le document
        Document pdfDocument = new Document(_dataDir + "OptimizeDocument.pdf");
        com.aspose.pdf.optimization.OptimizationOptions optimizationOptions = new com.aspose.pdf.optimization.OptimizationOptions();

        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);

        // Optimiser le document PDF en utilisant OptimizationOptions
        pdfDocument.optimizeResources(optimizationOptions);

        _dataDir = _dataDir + "OptimizeDocument_out.pdf";
        // Enregistrer le document mis à jour
        pdfDocument.save(_dataDir);
    }
```
## Stocker l'image dans XImageCollection

Aspose.PDF pour Java permet de stocker de nouvelles images dans [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection) avec la compression FlateDecode.
 Pour activer cette option, vous pouvez utiliser le drapeau ImageFilterType.Flate. Le snippet de code suivant montre comment utiliser cette fonctionnalité :

```java
    public static void StoreImageInXImageCollection() {
        // Initialiser le document
        Document document = new Document();
        document.getPages().add();
        Page page = document.getPages().get_Item(1);

        // Charger l'image dans le flux
        java.io.FileInputStream imageStream = null;
        try {
            imageStream = new java.io.FileInputStream(new java.io.File("input_image1.jpg"));
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            return;
        }
        page.getResources().getImages().add(imageStream, ImageFilterType.Flate);
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        page.getContents().add(new com.aspose.pdf.operators.GSave());

        // Définir les coordonnées
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });
        // Utilisation de l'opérateur ConcatenateMatrix (concaténer la matrice) : définit comment l'image doit être placée
        page.getContents().add(new com.aspose.pdf.operators.ConcatenateMatrix(matrix));
        page.getContents().add(new com.aspose.pdf.operators.Do(ximage.getName()));
        page.getContents().add(new com.aspose.pdf.operators.GRestore());

        document.save(_dataDir + "FlateDecodeCompression.pdf");
    }

}
```