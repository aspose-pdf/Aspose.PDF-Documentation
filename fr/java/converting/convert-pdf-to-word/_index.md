---
title: Convertir un PDF en Word en Java
linktitle: Convertir un PDF en Word
type: docs
weight: 10
url: /java/convert-pdf-to-word/
lastmod: "2026-06-16"
description: Apprenez à convertir des fichiers PDF en DOC et DOCX en Java avec Aspose.PDF pour faciliter l'édition et la réutilisation de documents.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comment convertir un PDF en Word en Java
Abstract: Cet article explique comment convertir des fichiers PDF aux formats Microsoft Word à l'aide d'Aspose.PDF pour Java. Il couvre la sortie DOC, la sortie DOCX, la conversion DOCX à flux amélioré, les sauts de ligne préservés, la reconnaissance des puces et le contrôle de la résolution d'image via `DocSaveOptions`.
---
Aspose.PDF pour Java peut exporter des documents PDF aux formats Microsoft Word avec différentes options de reconnaissance et de mise en page. Utilisez [`DocSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) pour contrôler la façon dont le texte, les listes et les images PDF sont mappés dans la sortie Word.


## 
Convertir un PDF en DOC



Utilisez cet exemple lorsqu'un document PDF doit être exporté vers l'ancien format DOC. Le code crée `DocSaveOptions`, définit le format sur `Doc` et transmet les options à une méthode de sauvegarde partagée.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`DocSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) et définissez le format sur `Doc`.
1. Appelez `document.save(outputFile.toString(), saveOptions)` pour que le PDF soit exporté au format de document binaire Microsoft Word.

1. 
Enregistrez le fichier DOC converti.


```java
public static void convertPdfToDoc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir un PDF en DOCX



Utilisez cet exemple lorsqu'un document PDF doit être exporté sous forme de fichier DOCX. DOCX est le format préféré pour la plupart des nouveaux flux de travail de traitement de texte, car il est largement pris en charge et plus facile à modifier.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Créez [`DocSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) et définissez le format sur `DocX`.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` pour que le contenu PDF soit exporté en tant que document Office Open XML Word.

1. 
Enregistrez le fichier DOCX résultant.


```java
public static void convertPdfToDocx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertissez un PDF en DOCX avec une reconnaissance de flux améliorée



Utilisez cet exemple lorsque l’exportation Word doit privilégier un contenu modifiable fluide plutôt qu’une présentation visuelle fixe.

1. Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`DocSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) pour la sortie `DocX`.

1. 
Activez `setMode(DocSaveOptions.RecognitionMode.EnhancedFlow)` pour que le convertisseur utilise une reconnaissance de flux améliorée lors de la génération DOCX.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` et enregistrez la sortie DOCX convertie.


```java
public static void convertPdfToDocxAdvanced(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setMode(DocSaveOptions.RecognitionMode.EnhancedFlow);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir un PDF en DOCX avec des sauts de ligne préservés

Utilisez cet exemple lorsque les fins de ligne du PDF source doivent être conservées dans la sortie Word.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`DocSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) pour l'exportation `DocX`.

1. 
Activez `setAddReturnToLineEnd(true)` pour que les sauts de ligne explicites soient conservés lors de la conversion.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` et enregistrez le fichier DOCX.

```java
public static void convertPdfToDocxWithLineBreaks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setAddReturnToLineEnd(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convertir un PDF en DOCX avec la reconnaissance des puces



Utilisez cet exemple lorsque les puces de liste du PDF source doivent être reconnues et conservées en tant que structures de liste dans Word.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`DocSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) pour l'exportation `DocX`.

1. 
Activez `setRecognizeBullets(true)` pour que le contenu PDF de type liste soit reconnu comme liste à puces lors de la conversion.
1. Appelez `document.save(outputFile.toString(), saveOptions)` et enregistrez le fichier DOCX.


```java
public static void convertPdfToDocxWithBulletRecognition(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setRecognizeBullets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertissez un PDF en DOCX avec une résolution d'image personnalisée



Utilisez cet exemple lorsque la fidélité de l'image à l'intérieur du DOCX généré doit être contrôlée lors de la conversion.


1. 
Ouvrez le PDF source dans une instance [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [`DocSaveOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) pour l'exportation `DocX`.
1. Définissez `setImageResolutionX(300)` et `setImageResolutionY(300)` pour que le contenu raster soit généré à la résolution demandée.

1. 
Appelez `document.save(outputFile.toString(), saveOptions)` et enregistrez la sortie DOCX.

```java
public static void convertPdfToDocxWithImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setImageResolutionX(300);
        saveOptions.setImageResolutionY(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
