---
title: Convertir HTML en PDF en Java
linktitle: Convertir HTML en fichier PDF
type: docs
weight: 40
url: /java/convert-html-to-pdf/
lastmod: "2026-06-16"
description: Découvrez comment convertir des pages HTML, MHTML et Web en PDF en Java avec Aspose.PDF, y compris les paramètres multimédias, les règles de page CSS, l'intégration de polices, le contenu SVG et la sortie d'une seule page.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Comment convertir du HTML en PDF en Java avec Aspose.PDF
Abstract: Cet article explique comment convertir des fichiers HTML et MHTML en PDF à l'aide d'Aspose.PDF pour Java. Il couvre le flux de travail de base HTML vers PDF et montre comment contrôler le rendu avec les types de médias, la priorité des règles de page CSS, les polices intégrées, le contenu SVG, la sortie d'une seule page et la conversion directe à partir d'une page Web en direct.
---
Aspose.PDF pour Java peut convertir des fichiers HTML locaux, du contenu MHTML archivé et des pages Web en direct en documents PDF. Vous pouvez contrôler le pipeline de conversion avec `HtmlLoadOptions` et `MhtLoadOptions` pour influencer la mise à l'échelle de la mise en page, la gestion des médias CSS, la priorité des règles de page, l'intégration des polices, la résolution des ressources et le comportement de rendu d'une seule page.


## 
Convertir HTML en PDF



Utilisez cet exemple lorsqu'un fichier HTML local doit être converti directement en document PDF.


1. 
Créez une instance [`HtmlLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) pour configurer la façon dont la source HTML est interprétée lors de l'importation.

1. 
Définissez [`HtmlPageLayoutOption`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlpagelayoutoption/) sur `ScaleToPageWidth` afin que le contenu HTML large soit adapté à la largeur de la page PDF cible au lieu d'être tronqué.
1. Ouvrez le fichier HTML source en transmettant son chemin et les options de chargement configurées dans le constructeur [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Enregistrez le [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) généré en tant que fichier PDF dans le chemin de sortie cible.


```java
public static void convertHtmlToPdf(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPageLayoutOption(HtmlPageLayoutOption.ScaleToPageWidth);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertissez HTML en PDF avec les options de type de média



Utilisez cet exemple lorsque la gestion du type de média CSS doit être contrôlée lors de la conversion HTML.


1. 
Créez une instance [`HtmlLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) pour les paramètres de conversion.
1. Définissez [`HtmlMediaType`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlmediatype/) sur `Screen` lorsque le code HTML doit être rendu avec des règles CSS destinées à l'affichage à l'écran plutôt qu'à l'impression.

1. 
Ouvrez le fichier HTML avec les options de chargement configurées afin que les styles dépendants des requêtes multimédias soient appliqués lors de la conversion.

1. 
Enregistrez le [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) résultant en tant que fichier PDF.


```java
public static void convertHtmlToPdfMediaType(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setHtmlMediaType(HtmlMediaType.Screen);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir du HTML en PDF avec la priorité des règles de page CSS



Utilisez cet exemple lorsque les règles CSS `@page` doivent influencer la mise en page finale du PDF.

1. Créez une instance [`HtmlLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) avant d'ouvrir le fichier HTML.

1. 
Configurez `setPriorityCssPageRule(false)` lorsque les autres paramètres de mise en page doivent avoir priorité sur les déclarations CSS `@page` dans le balisage source.

1. 
Chargez le contenu HTML dans un [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) avec les options configurées afin que la mise en page soit résolue lors de l'importation.

1. 
Enregistrez le fichier PDF généré.


```java
public static void convertHtmlToPdfPriorityCssPageRule(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setPriorityCssPageRule(false);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir du HTML en PDF avec des polices intégrées

Utilisez cet exemple lorsque le PDF de sortie doit conserver les polices HTML en les incorporant.


1. 
Créez une instance [`HtmlLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) pour la configuration de l'importation HTML.

1. 
Activez `setEmbedFonts(true)` pour que les polices résolues lors du rendu HTML soient stockées dans le PDF de sortie.

1. 
Ouvrez la source HTML avec ces options de chargement pour conserver la typographie originale disponible dans le document final.

1. 
Enregistrez le [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) au format PDF avec les ressources de polices intégrées incluses.

```java
public static void convertHtmlToPdfEmbedFonts(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setEmbedFonts(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Afficher le contenu HTML sur une seule page PDF



Utilisez cet exemple lorsque le contenu HTML long doit être conservé sur une seule page PDF au lieu de s'étendre sur plusieurs pages.


1. 
Créez une instance [`HtmlLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) pour les paramètres de conversion.

1. 
Activez `setRenderToSinglePage(true)` pour que le code HTML importé soit disposé sur une seule page PDF plutôt que réparti sur plusieurs pages.

1. 
Ouvrez le HTML source avec les options de chargement configurées et laissez Aspose.PDF créer la mise en page dans un [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Enregistrez le fichier PDF de sortie.


```java
public static void convertHtmlToPdfRenderContentToSamePage(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions();
    loadOptions.setRenderToSinglePage(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir du HTML contenant du SVG en ligne



Utilisez cet exemple lorsque la source HTML inclut des données SVG en ligne qui doivent être restituées dans le PDF.


1. 
Créez une instance [`HtmlLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) avec le répertoire parent du fichier HTML comme chemin de base afin que les ressources associées puissent être résolues de manière cohérente lors de la conversion.

1. 
Ouvrez le fichier HTML contenant le balisage SVG en ligne en transmettant le chemin source et les options de chargement dans le constructeur [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Laissez Aspose.PDF restituer le DOM HTML avec les éléments SVG intégrés dans le contenu de la page PDF.

1. 
Enregistrez le document PDF généré.


```java
public static void convertHtmlToPdfWithSvgData(Path inputFile, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(inputFile.getParent().toString());
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 
Convertir une page Web en PDF



Utilisez cet exemple lorsqu'une URL Web en direct doit être affichée et enregistrée en tant que document PDF.


1. 
Créez une instance [`HtmlLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/) avec l'URL cible afin que les ressources relatives telles que les feuilles de style et les images puissent être résolues par rapport à cette adresse.
1. Convertissez la chaîne URL en un objet `URL` et ouvrez son flux d'entrée pour récupérer le contenu HTML en direct.

1. 
Créez un [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) à partir du flux de réponse et des options de chargement configurées afin que la page téléchargée soit traitée avec l'URL de base correcte.

1. 
Enregistrez la page Web rendue sous forme de fichier PDF et fermez automatiquement les ressources de flux avec try-with-resources.


```java
public static void convertWebPageToPdf(String urlString, Path outputFile) {
    HtmlLoadOptions loadOptions = new HtmlLoadOptions(urlString);
    try {
        URL url = URI.create(urlString).toURL();

        try (InputStream inputStream = url.openStream()) {
            try (Document document = new Document(inputStream, loadOptions)) {
                document.save(outputFile.toString());
            }
        }
        System.out.println(url + " converted into " + outputFile);
    } catch (Exception e) {
        e.printStackTrace();
    }
}
```

## 
Convertir MHTML en PDF



Utilisez cet exemple lorsqu'un fichier MHTML archivé doit être converti en document PDF.

1. Créez une instance [`MhtLoadOptions`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/mhtloadoptions/) pour indiquer à Aspose.PDF de charger la source en tant que contenu HTML MIME.

1. 
Ouvrez le fichier `.mht` ou `.mhtml` en passant son chemin et les options de chargement MHTML dans le constructeur [`Document`] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Laissez Aspose.PDF analyser le contenu HTML archivé et ses ressources intégrées dans le modèle de document PDF.

1. 
Enregistrez le fichier PDF généré.

```java
public static void convertMhtmlToPdf(Path inputFile, Path outputFile) {
    MhtLoadOptions loadOptions = new MhtLoadOptions();
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
