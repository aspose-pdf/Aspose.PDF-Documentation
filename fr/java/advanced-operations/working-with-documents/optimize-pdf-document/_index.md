---
title: Optimiser les fichiers PDF en Java
linktitle: Optimiser le PDF
type: docs
weight: 30
url: /java/optimize-pdf/
description: Découvrez comment optimiser, compresser et réduire la taille d'un fichier PDF en Java à l'aide d'Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Compressez les ressources PDF et réduisez la taille des fichiers avec Java
Abstract: Cet article explique comment optimiser les fichiers PDF à l'aide d'Aspose.PDF pour Java. Il couvre l'optimisation de l'ensemble du document, la compression des ressources, la réduction de la qualité de l'image, la suppression des objets et des flux inutilisés, la liaison des flux en double, la désintégration des polices, l'aplatissement des annotations et des formulaires, la conversion des niveaux de gris et la compression d'image Flate.
---
Aspose.PDF pour Java expose les fonctionnalités d'optimisation via `Document.optimize`, `optimizeResources` et `OptimizationOptions`.


## 
Optimiser un PDF avec l'optimisation générale des documents



Utilisez cet exemple lorsque vous souhaitez qu’Aspose.PDF applique la routine intégrée d’optimisation de l’ensemble du document.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Appelez `optimize()` sur le document.
1. Enregistrez le fichier optimisé et comparez les tailles d'origine et de sortie.


```java
public static void optimizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimize();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
Réduisez la taille du PDF en optimisant les ressources



Cet exemple se concentre sur l'optimisation au niveau des ressources sans configurer manuellement les options individuelles.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Exécutez `optimizeResources()` pour optimiser les ressources internes.
1. Enregistrez le résultat et imprimez les tailles des fichiers d’entrée et de sortie.


```java
public static void reduceSizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimizeResources();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
Compresser toutes les images dans un PDF



Utilisez cette approche lorsque les documents contenant beaucoup d’images nécessitent une taille de fichier plus petite et qu’une certaine réduction de la qualité de l’image est acceptable.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez des [Options d'optimisation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) et activez la compression d'image avec le niveau de qualité requis.
1. Optimisez les ressources documentaires avec ces paramètres.

1. 
Enregistrez le fichier optimisé et comparez les tailles de fichiers.


```java
public static void shrinkingOrCompressingAllImages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.getImageCompressionOptions().setCompressImages(true);
        optimizeOptions.getImageCompressionOptions().setImageQuality(50);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
Supprimer les objets inutilisés d'un PDF



Cet exemple supprime les objets inutilisés qui peuvent rester dans la structure du document après des modifications ou des fusions.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Créez des [OptimizationOptions] (https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) et activez la suppression des objets inutilisés.

1. 
Optimisez les ressources et enregistrez le fichier mis à jour.

1. 
Imprimez les tailles de fichier originales et réduites.


```java
public static void removingUnusedObjects(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedObjects(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
Supprimer les flux inutilisés d'un PDF



Utilisez cette approche lorsque vous souhaitez supprimer les données de flux qui ne sont plus référencées par le document.

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Configurez [OptimizationOptions] (https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) pour supprimer les flux inutilisés.

1. 
Optimisez les ressources, enregistrez le document de sortie et comparez la taille des fichiers.


```java
public static void removingUnusedStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
Lier les flux en double dans un PDF



Cet exemple déduplique les flux répétés afin que le contenu identique ne puisse être stocké qu'une seule fois.

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez des [OptimizationOptions] (https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) et activez la liaison de flux en double.

1. 
Optimisez les ressources, enregistrez le document de sortie et imprimez la taille des fichiers.


```java
public static void linkingDuplicateStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setLinkDuplicateStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
Désintégrer les polices d'un PDF



Utilisez cette option lorsqu’il est plus important de réduire la taille du fichier que de conserver les données de police intégrées dans la sortie.

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Configurez [OptimizationOptions] (https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) pour désintégrer les polices.

1. 
Optimisez les ressources, enregistrez le document et comparez la taille des fichiers.


```java
public static void unembedFonts(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setUnembedFonts(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
Aplatir les annotations dans un PDF



Cet exemple convertit les annotations en contenu de page statique afin qu'elles ne restent plus des objets interactifs.

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez chaque [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) et sa collection [Annotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/).

1. 
Aplatissez chaque annotation et enregistrez le document mis à jour.


```java
public static void flattenAnnotations(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            for (Annotation annotation : page.getAnnotations()) {
                annotation.flatten();
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 
Aplatir les champs du formulaire PDF



Utilisez cette approche lorsque les champs de formulaire à remplir doivent devenir un contenu fixe avant la distribution ou l'archivage.

1. Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Vérifiez si le document contient des widgets de formulaire.

1. 
Aplatissez chaque [Field] (https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) représenté par une [WidgetAnnotation] (https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).

1. 
Enregistrez le fichier de sortie et imprimez les tailles de fichier.


```java
public static void flattenForms(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## 
Convertir un PDF en niveaux de gris

Cet exemple modifie chaque page en niveaux de gris, ce qui peut aider à réduire la complexité des couleurs et à standardiser la sortie pour les flux de travail d'archivage ou d'impression.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Parcourez chaque [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) du document.

1. 
Appelez `makeGrayscale()` sur chaque page et enregistrez le fichier de sortie.


```java
public static void convertPdfFromRgbColorspaceToGrayscale(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.makeGrayscale();
        }
        document.save(outputFile.toString());
    }
}
```

## 
Utiliser la compression d'image FlateDecode

Utilisez ce modèle lorsque vous souhaitez appliquer une compression basée sur Flate aux images lors de l'optimisation des ressources PDF.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez des [OptimizationOptions] (https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) et définissez le codage de l'image sur [ImageEncoding] (https://reference.aspose.com/pdf/java/com.aspose.pdf/imageencoding/).`Flate`.

1. 
Optimisez les ressources du document et enregistrez le fichier de sortie.


```java
public static void usingFlatedecodeCompression(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizationOptions = new OptimizationOptions();
        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);
        document.optimizeResources(optimizationOptions);
        document.save(outputFile.toString());
    }
}
```

## 
Imprimer des tailles de fichiers originales et optimisées

Cette méthode d'assistance signale la différence de taille entre le fichier source et le fichier de sortie optimisé.


1. 
Lisez la taille du fichier d'entrée.

1. 
Lisez la taille du fichier de sortie.

1. 
Imprimez les deux valeurs dans un seul message d'état.

```java
private static void printFileSizes(Path inputFile, Path outputFile) throws Exception {
    System.out.println("Original file size: " + Files.size(inputFile)
            + ". Reduced file size: " + Files.size(outputFile));
}
```
