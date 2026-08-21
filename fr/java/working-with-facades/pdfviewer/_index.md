---
title: Classe PDFViewer
linktitle: Classe PDFViewer
type: docs
weight: 135
url: /java/pdfviewer-class/
description: Découvrez comment utiliser la façade PdfViewer en Java pour décoder les pages PDF et inspecter les paramètres liés à la visionneuse.
lastmod: "2026-06-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Décodez les pages PDF et inspectez les données de la visionneuse en Java avec PdfViewer
Abstract: Cette section explique comment utiliser la façade PdfViewer dans Aspose.PDF pour Java pour le décodage de pages et les tâches d'inspection liées à la visionneuse. Les exemples Java actuels couvrent le rendu de toutes les pages en images, le décodage d'une page spécifique et l'inspection du nombre de pages, du type de coordonnées, de la résolution et des paramètres de la visionneuse liée.
---
La classe Java `PdfViewerExamples` illustre les principaux flux de travail de visualisation disponibles via l'API Facades.


## 
Décoder toutes les pages PDF



Utilisez ce flux de travail lorsque chaque page du PDF source doit être rendue sous forme d'image.


### 
Étapes


1. 
Créez et configurez une instance `PdfViewer`.
2. Liez le PDF source avec `bindPdf`.

3. 
Appelez `decodeAllPages()` pour afficher le document dans un tableau `BufferedImage`.

4. 
Enregistrez chaque page décodée dans un fichier image de sortie.

5. 
Fermez le fichier PDF lié.


### 
Exemple Java

```java
public static void decodeAllPages(Path inputFile, Path outputDir) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        BufferedImage[] pages = viewer.decodeAllPages();
        for (int index = 0; index < pages.length; index++) {
            ImageIO.write(pages[index], "png", outputDir.resolve("decode_all_pages_" + (index + 1) + ".png").toFile());
        }
    } finally {
        viewer.closePdfFile();
    }
}
```

## Décoder une page PDF spécifique



Utilisez ce flux de travail lorsqu'une seule page doit être rendue sur une image.


### 
Étapes


1. 
Créez et configurez une instance `PdfViewer`.

2. 
Liez le PDF source.
3. Appelez `decodePage()` pour la page que vous souhaitez afficher.

4. 
Enregistrez la page décodée dans un fichier image de sortie.

5. 
Fermez la visionneuse.


### 
Exemple Java


```java
public static void decodeSpecificPage(Path inputFile, Path outputFile) throws Exception {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        ImageIO.write(viewer.decodePage(1), "png", outputFile.toFile());
    } finally {
        viewer.close();
    }
}
```

## 
Inspecter les métadonnées PDF

Utilisez ce flux de travail lorsque vous avez besoin d'informations sur un document lié à la visionneuse avant le rendu ou l'impression.


### 
Étapes


1. 
Créez et configurez une instance `PdfViewer`.

2. 
Liez le PDF source.

3. 
Lisez le nombre de pages, le type de coordonnées et la résolution de rendu.
4. Utilisez ou imprimez les valeurs récupérées.

5. 
Fermez le fichier PDF lié.


### 
Exemple Java


```java
public static void inspectPdfMetadata(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Coordinate type: " + viewer.getCoordinateType());
        System.out.println("Resolution: " + viewer.getResolution());
    } finally {
        viewer.closePdfFile();
    }
}
```

## 
Inspecter les paramètres de la visionneuse liée



Utilisez ce flux de travail lorsque vous devez confirmer ou ajuster le comportement du visualiseur après avoir lié le PDF.

### Étapes


1. 
Créez et configurez une instance `PdfViewer`.

2. 
Liez le PDF source.

3. 
Définissez les options de la visionneuse telles que le redimensionnement automatique, la rotation automatique et la visibilité de la boîte de dialogue d'impression.

4. 
Lisez les paramètres de la visionneuse active et le nombre de pages.
5. Fermez la visionneuse.


### 
Exemple Java

```java
public static void inspectBoundViewerSettings(Path inputFile) {
    PdfViewer viewer = createViewer();
    try {
        viewer.bindPdf(inputFile.toString());
        viewer.setAutoResize(true);
        viewer.setAutoRotate(true);
        viewer.setPrintPageDialog(false);
        System.out.println("Page count: " + viewer.getPageCount());
        System.out.println("Print as image: " + viewer.getPrintAsImage());
        System.out.println("Auto resize: " + viewer.getAutoResize());
        System.out.println("Auto rotate: " + viewer.getAutoRotate());
    } finally {
        viewer.close();
    }
}
```
