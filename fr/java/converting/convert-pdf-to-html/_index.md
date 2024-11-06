---
title: Convertir un fichier PDF en format HTML
linktitle: Convertir un fichier PDF en format HTML
type: docs
weight: 50
url: fr/java/convert-pdf-to-html/
lastmod: "2021-11-19"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF en format HTML avec la bibliothèque Java.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Aspose.PDF pour Java offre de nombreuses fonctionnalités pour convertir divers formats de fichiers en documents PDF et pour convertir des fichiers PDF en divers formats de sortie. Cet article explique comment convertir un fichier PDF en format HTML et enregistrer les images du fichier PDF dans un dossier particulier.

{{% alert color="success" %}}
**Essayez de convertir un PDF en HTML en ligne**

Aspose.PDF pour Java vous présente une application gratuite en ligne ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Conversion PDF en HTML avec l'application gratuite Aspose.PDF](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)

{{% /alert %}}

When converting large PDF file with several pages to HTML format, the output appears as a single HTML page. It can end up being very long. To control page size, it is possible to split the output into several pages during PDF to HTML conversion.

## Convertir des pages PDF en HTML

Aspose.PDF pour Java offre de nombreuses fonctionnalités pour convertir divers formats de fichiers en documents PDF et convertir des fichiers PDF en divers formats de sortie. Cet article explique comment convertir un fichier PDF en format HTML et enregistrer les images du fichier PDF dans un dossier particulier.

Le code suivant vous montre toutes les options possibles que vous pouvez utiliser lors de la conversion de PDF en HTML.

```java
// Ouvrir le document PDF source
Document pdfDocument = new Document(_dataDir + "PDFToHTML.pdf");

// Enregistrer le fichier au format document MS
pdfDocument.save(_dataDir + "output_out.html", SaveFormat.Html);
```

## Convertir PDF en HTML - Division de la sortie en HTML multi-pages

Aspose.PDF pour Java prend en charge la fonctionnalité de conversion de documents PDF en divers formats de sortie, y compris HTML.
 Cependant, lors de la conversion de fichiers PDF volumineux (composés de plusieurs pages), vous pouvez avoir besoin de sauvegarder chaque page PDF individuelle dans un fichier HTML séparé.

Lors de la conversion d'un fichier PDF volumineux avec plusieurs pages au format HTML, le résultat apparaît comme une seule page HTML. Cela peut finir par être très long. Pour contrôler la taille de la page, il est possible de diviser le résultat en plusieurs pages lors de la conversion de PDF en HTML. Veuillez essayer d'utiliser l'extrait de code suivant.

```java
// Ouvrir le document PDF source
Document document = new Document(_dataDir + "PDFToHTML.pdf");

// Instancier un objet HtmlSaveOptions
HtmlSaveOptions htmlOptions = new HtmlSaveOptions();

// Spécifier de diviser le résultat en plusieurs pages
htmlOptions.setSplitIntoPages(true);

// Enregistrer le document
document.save(_dataDir + "MultiPageHTML_out.html", htmlOptions);    
```

## Convertir PDF en HTML - Éviter de Sauvegarder les Images au Format SVG

Le format de sortie par défaut pour la sauvegarde des images lors de la conversion de PDF en HTML est SVG. Pendant la conversion, certaines images du PDF sont transformées en images vectorielles SVG. Cela pourrait être lent. Au lieu de cela, les images pourraient être transformées en PNG. Pour permettre cela, Aspose.PDF a l'option d'utiliser SVG pour les vecteurs ou de créer des PNG.

Afin de supprimer complètement le rendu des images au format SVG lors de la conversion de fichiers PDF en format HTML, veuillez essayer d'utiliser l'extrait de code suivant.

```java
 // Charger le fichier PDF
Document document = new Document(DATA_DIR + "PDFToHTML.pdf")

// Instancier l'objet saveOptions pour la sauvegarde en HTML
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// Spécifier le dossier où les images SVG sont enregistrées lors de la conversion PDF en HTML
saveOptions.setSpecialFolderForSvgImages(DATA_DIR.toString());

// Sauvegarder le fichier de sortie
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
```

## Compression des Images SVG Pendant la Conversion

Pour compresser les images SVG lors de la conversion de PDF en HTML, veuillez essayer d'utiliser le code suivant :

```java
// Charger le fichier PDF
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

// Créer HtmlSaveOption avec la fonctionnalité testée
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// Compresser les images SVG s'il y en a
saveOptions.setCompressSvgGraphicsIfAny(true);
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
document.close();
```

## Convertir un PDF en HTML - Spécifier le Dossier des Images

Par défaut, lors de la conversion d'un fichier PDF en HTML, les images du PDF sont enregistrées dans un dossier séparé créé dans le même répertoire que celui où le HTML de sortie est créé. Mais parfois, il est nécessaire de spécifier un dossier différent pour enregistrer les images lors de la génération des fichiers HTML. Pour cela, nous avons introduit les [SaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SaveOptions).
La méthode [SpecialFolderForAllImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/#setSpecialFolderForAllImages-java.lang.String-) est utilisée pour spécifier le dossier cible pour stocker les images.

```java
// Charger le fichier PDF
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");
HtmlSaveOptions saveOptions = new HtmlSaveOptions();

// Spécifier le dossier séparé pour enregistrer les images
saveOptions.setSpecialFolderForAllImages(DATA_DIR.toString());
document.save(DATA_DIR + "SaveSVGFiles_out.html", saveOptions);
document.close();
```

## Créer des Fichiers Subséquents avec Seulement le Contenu du Corps

Avec l'extrait de code simple suivant, vous pouvez diviser le HTML de sortie en pages. Dans les pages de sortie, tous les objets HTML doivent aller exactement là où ils vont maintenant (traitement et sortie des polices, création et sortie du CSS, création et sortie des images), sauf que le HTML de sortie contiendra les contenus actuellement placés à l'intérieur des balises (maintenant les balises “body” seront omises).

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

HtmlSaveOptions saveOptions = new HtmlSaveOptions();

saveOptions.setHtmlMarkupGenerationMode(HtmlSaveOptions.HtmlMarkupGenerationModes.WriteOnlyBodyContent);
saveOptions.setSplitIntoPages(true);

document.save(DATA_DIR + "CreateSubsequentFiles_out.html", saveOptions);
document.close();
```

## Rendu de texte transparent

Dans le cas où le fichier PDF source/entrée contient des textes transparents masqués par des images de premier plan, il pourrait y avoir des problèmes de rendu de texte. Donc, afin de prendre en compte de tels scénarios, les méthodes `setSaveShadowedTextsAsTransparentTexts` et `setSaveTransparentTexts` peuvent être utilisées.

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");

// Instancier l'objet HTML SaveOptions
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();
htmlsaveOptions.setSaveShadowedTextsAsTransparentTexts(true);
htmlsaveOptions.setSaveTransparentTexts(true);

// Enregistrer le document
document.save(DATA_DIR + "TransparentTextRendering_out.html", htmlsaveOptions);
document.close();
```


## Rendu des couches de document PDF

Nous pouvons rendre les couches de document PDF dans un élément de type couche distinct lors de la conversion de PDF en HTML :

```java
Document document = new Document(DATA_DIR + "PDFToHTML.pdf");
// Instancier un objet HtmlSaveOptions

HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();

// Spécifier de rendre les couches de document PDF séparément dans le HTML de sortie
htmlsaveOptions.setConvertMarkedContentToLayers(true);

// Enregistrer le document
document.save(DATA_DIR + "LayersRendering_out.html", htmlsaveOptions);
document.close();
```

La conversion de PDF en HTML est l'une des fonctionnalités les plus populaires d'Aspose.PDF car elle permet de visualiser le contenu des fichiers PDF sur diverses plateformes sans utiliser de visionneuse de documents PDF. Le HTML de sortie est conforme aux normes WWW et peut être facilement affiché dans tous les navigateurs web. En utilisant cette fonctionnalité, les fichiers PDF peuvent être visualisés sur des appareils portables car vous n'avez pas besoin d'installer une application de visualisation PDF mais pouvez utiliser un simple navigateur web.


## PDF en HTML - Exclure les ressources de police

Si vous avez l'intention d'exclure toutes ou certaines ressources de polices lors de la conversion de PDF en HTML, Aspose.PDF pour Java API vous permet de le faire à l'aide de la classe HtmlSaveOptions. L'API offre deux options à cet effet.

- `htmlOptions.FontSavingMode = HTmlSaveOptions.FontSavingModes.DontSave` - pour empêcher l'exportation de toutes les polices
- `htmlOptions.ExcludeFontNameList = (new String[] { "ArialMT", "SymbolMT" });` - pour empêcher l'exportation de polices spécifiques (les noms de polices doivent être spécifiés sans dièse)

Afin de convertir un PDF en HTML en excluant les ressources de polices, utilisez les étapes suivantes :

1. Définissez un nouvel objet de la classe HtmlSaveOptions
1. Définissez et définissez les noms de polices à empêcher d'exporter dans HtmlSaveOptions.ExcludeFontNameList
1. Convertissez le PDF en HTML en utilisant la méthode save

```java
HtmlSaveOptions htmlsaveOptions = new HtmlSaveOptions();
htmlsaveOptions.setExplicitListOfSavedPages(
        new int[]{
                1
        }
);
htmlsaveOptions.setFixedLayout(true);
htmlsaveOptions.setCompressSvgGraphicsIfAny(false);
htmlsaveOptions.setSaveTransparentTexts(true);
htmlsaveOptions.setSaveShadowedTextsAsTransparentTexts(true);
htmlsaveOptions.setExcludeFontNameList(new String[]{"ArialMT", "SymbolMT"});
htmlsaveOptions.setFontSavingMode(HtmlSaveOptions.FontSavingModes.DontSave);
htmlsaveOptions.setDefaultFontName("Comic Sans MS");
htmlsaveOptions.setUseZOrder(true);
htmlsaveOptions
        .setLettersPositioningMethod(LettersPositioningMethods.UseEmUnitsAndCompensationOfRoundingErrorsInCss);
htmlsaveOptions
        .setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.NoEmbedding);
htmlsaveOptions
        .setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
htmlsaveOptions.setSplitIntoPages(false);

Document document = new Document(DATA_DIR + "sample.pdf");
document.save(DATA_DIR + "output_out.html", htmlsaveOptions);
document.close();
```