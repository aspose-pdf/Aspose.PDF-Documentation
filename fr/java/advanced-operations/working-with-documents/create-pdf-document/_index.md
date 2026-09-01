---
title: Créer des fichiers PDF en Java
linktitle: Créer un document PDF
type: docs
weight: 10
url: /java/create-pdf-document/
description: Apprenez à créer des fichiers PDF et à créer des PDF consultables en Java à l'aide d'Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Créez des fichiers PDF et des documents PDF consultables avec Java
Abstract: Cet article montre comment créer des documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre la création d'un nouveau PDF à partir de zéro et la conversion d'un document basé sur une image en un PDF consultable en fournissant une sortie HOCR à partir d'un moteur OCR externe.
---
Aspose.PDF pour Java prend en charge à la fois la création simple de documents et les flux de travail PDF consultables assistés par OCR.


## 
Créer un nouveau document PDF



Utilisez cette approche lorsque vous devez générer un simple fichier PDF à partir de zéro.


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez une [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au document.
1. Créez un [TextFragment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) et ajoutez-le à la page.

1. 
Enregistrez le PDF de sortie [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


```java
public static void createNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment("Hello World!"));
        document.save(outputFile.toString());
    }
}
```

## 
Créer un PDF consultable



L'exemple `createSearchablePdf` utilise `Document.convert(...)` avec une implémentation `CallBackGetHocr`. Le rappel écrit l'image source dans un fichier temporaire, appelle Tesseract avec l'option `hocr`, lit le balisage HOCR généré et le renvoie à Aspose.PDF.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Créez le rappel `CallBackGetHocr` et convertissez le document source en contenu PDF consultable.

1. 
Enregistrez le [Document] PDF mis à jour (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


```java
public static void createSearchablePdf(Path inputFile, Path outputFile) {
    Path tempDir = outputFile.getParent().resolve("ocr-temp");
    CallBackGetHocr cbgh = new CallBackGetHocr() {
        @Override
        public String invoke(java.awt.image.BufferedImage img) {
            // save the image, run Tesseract with "hocr", and return the HOCR text
            return fileContents.toString();
        }
    };
    try (Document document = new Document(inputFile.toString())) {
        document.convert(cbgh);
        document.save(outputFile.toString());
    }
}
```

## 
Obtenir les paramètres de la fenêtre du document



Utilisez cet exemple pour inspecter les préférences actuelles de la visionneuse stockées dans un document PDF existant.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Lisez la fenêtre requise et affichez les propriétés du document.

1. 
Affichez les paramètres actuels pour l'inspection ou le débogage.


```java
public static void getDocumentWindow(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("CenterWindow: " + document.isCenterWindow());
        System.out.println("Direction: " + document.getDirection());
        System.out.println("DisplayDocTitle: " + document.isDisplayDocTitle());
        System.out.println("FitWindow: " + document.isFitWindow());
        System.out.println("HideMenuBar: " + document.isHideMenubar());
        System.out.println("HideToolBar: " + document.isHideToolBar());
        System.out.println("HideWindowUI: " + document.isHideWindowUI());
        System.out.println("NonFullScreenPageMode: " + document.getNonFullScreenPageMode());
        System.out.println("PageLayout: " + document.getPageLayout());
        System.out.println("PageMode: " + document.getPageMode());
    }
}
```

## 
Définir les préférences de la fenêtre du document



Cet exemple met à jour la façon dont le PDF doit être affiché lorsqu'il est ouvert dans une visionneuse compatible.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Définissez les préférences requises en matière de fenêtre, de mise en page et de mode page.

1. 
Enregistrez le [Document] PDF mis à jour (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


```java
public static void setDocumentWindow(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setCenterWindow(true);
        document.setDirection(Direction.R2L);
        document.setDisplayDocTitle(true);
        document.setFitWindow(true);
        document.setHideMenubar(true);
        document.setHideToolBar(true);
        document.setHideWindowUI(true);
        document.setNonFullScreenPageMode(PageMode.UseOC);
        document.setPageLayout(PageLayout.TwoColumnLeft);
        document.setPageMode(PageMode.UseThumbs);
        document.save(outputFile.toString());
    }
}
```

## 
Incorporer des polices dans un PDF existant



Utilisez cette approche lorsqu'un document doit contenir les polices requises pour un rendu plus fiable sur d'autres systèmes.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Activez l'intégration de polices standard et parcourez les polices utilisées par chaque [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Marquez tous les objets [Font] (https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) non intégrés pour l'intégration.

1. 
Enregistrez le document mis à jour.


```java
public static void embeddedFonts(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setEmbedStandardFonts(true);
        for (Page page : document.getPages()) {
            for (Font pageFont : page.getResources().getFonts()) {
                if (!pageFont.isEmbedded()) {
                    pageFont.setEmbedded(true);
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 
Intégrer des polices lors de la création d'un nouveau PDF



Cet exemple crée un nouveau PDF et attribue dès le début une police intégrée au contenu du texte.

1. Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) et ajoutez une [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).

1. 
Créez les [TextFragment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/), [TextSegment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textsegment/) et [TextState] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/) requis.

1. 
Résolvez la cible [Font] (https://reference.aspose.com/pdf/java/com.aspose.pdf/font/) du référentiel et marquez-la comme intégrée.

1. 
Ajoutez le contenu du texte à la page et enregistrez le document de sortie.


```java
public static void embeddedFontsInNewDocument(Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            TextFragment fragment = new TextFragment("");
            TextSegment segment = new TextSegment(" This is a sample text using Custom font.");
            TextState textState = new TextState();
            Font font = FontRepository.findFont("Arial");
            font.setEmbedded(true);
            textState.setFont(font);
            segment.setTextState(textState);
            fragment.getSegments().add(segment);
            page.getParagraphs().add(fragment);
        }
        document.save(outputFile.toString());
    }
}
```

## 
Définir une police par défaut pour la sortie PDF

Utilisez ce modèle lorsque le document enregistré doit utiliser une police spécifique lors de la génération de la sortie.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez [PdfSaveOptions] (https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfsaveoptions/) et définissez le nom de police par défaut.

1. 
Enregistrez le document avec les options d'enregistrement configurées.


```java
public static void setDefaultFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PdfSaveOptions saveOptions = new PdfSaveOptions();
        saveOptions.setDefaultFontName("Arial");
        document.save(outputFile.toString(), saveOptions);
    }
}
```

## 
Obtenez toutes les polices utilisées dans un PDF

Cet exemple répertorie toutes les polices détectées dans le document afin que vous puissiez vérifier l'utilisation des polices avant d'exporter ou de mettre à jour le fichier.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Énumérez les polices renvoyées par les utilitaires de polices de document.

1. 
Affichez le nom de chaque [Police] détectée (https://reference.aspose.com/pdf/java/com.aspose.pdf/font/).


```java
public static void getAllFonts(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Font font : document.getFontUtilities().getAllFonts()) {
            System.out.println(font.getFontName());
        }
    }
}
```

## 
Améliorer l'intégration des polices en sous-définissant les polices

Utilisez cette approche lorsque vous souhaitez réduire la charge utile des polices tout en gardant les données de polices incorporées alignées sur l'utilisation du document.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Exécutez le sous-ensemble de polices via les utilitaires de polices de document avec les valeurs [FontSubsetStrategy] (https://reference.aspose.com/pdf/java/com.aspose.pdf/fontsubsetstrategy/) requises.

1. 
Enregistrez le document optimisé.


```java
public static void improveFontsEmbedding(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetAllFonts);
        document.getFontUtilities().subsetFonts(FontSubsetStrategy.SubsetEmbeddedFontsOnly);
        document.save(outputFile.toString());
    }
}
```

## 
Définir le facteur de zoom d'ouverture du document

Cet exemple configure le niveau de zoom initial qui doit être appliqué lors de l'ouverture du PDF.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Créez une [GoToAction] (https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) avec une [XYZExplicitDestination] (https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).

1. 
Attribuez l’action comme action d’ouverture de document et enregistrez le résultat.


```java
public static void setZoomFactor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GoToAction action = new GoToAction(new XYZExplicitDestination(1, 0.0, 0.0, 0.5));
        document.setOpenAction(action);
        document.save(outputFile.toString());
    }
}
```

## 
Obtenez le facteur de zoom d'ouverture du document

Utilisez cet exemple pour vérifier si un PDF définit déjà un niveau de zoom explicite pour son action d'ouverture.


1. 
Ouvrez le PDF source [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Vérifiez si l'action d'ouverture est une [GoToAction] (https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) avec une [XYZExplicitDestination] (https://reference.aspose.com/pdf/java/com.aspose.pdf/xyzexplicitdestination/).

1. 
Affichez la valeur de zoom configurée ou signalez qu'aucun zoom n'est défini.

```java
public static void getZoomFactor(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getOpenAction() instanceof GoToAction action
                && action.getDestination() instanceof XYZExplicitDestination destination) {
            System.out.println("Zoom: " + destination.getZoom());
        } else {
            System.out.println("Zoom: not set");
        }
    }
}
```
