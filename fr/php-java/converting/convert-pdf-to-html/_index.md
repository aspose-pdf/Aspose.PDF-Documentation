---
title: Convertir un fichier PDF au format HTML
linktitle: Convertir un fichier PDF au format HTML
type: docs
weight: 50
url: /fr/php-java/convert-pdf-to-html/
lastmod: "2024-05-20"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF au format HTML avec la bibliothèque PHP.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Aspose.PDF pour PHP offre de nombreuses fonctionnalités pour convertir divers formats de fichiers en documents PDF et convertir des fichiers PDF en divers formats de sortie. Cet article explique comment convertir un fichier PDF en format HTML et enregistrer les images du fichier PDF dans un dossier particulier.

{{% alert color="success" %}}
**Essayez de convertir PDF en HTML en ligne**

Aspose.PDF pour PHP vous présente l'application en ligne gratuite ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF vers HTML avec l'application gratuite](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)

{{% /alert %}}

Lorsque vous convertissez un fichier PDF volumineux avec plusieurs pages au format HTML, le résultat apparaît comme une seule page HTML. Cela peut finir par être très long. Pour contrôler la taille de la page, il est possible de diviser la sortie en plusieurs pages lors de la conversion de PDF en HTML.

## Convertir des pages PDF en HTML

Aspose.PDF pour PHP offre de nombreuses fonctionnalités pour convertir divers formats de fichiers en documents PDF et convertir des fichiers PDF en divers formats de sortie. Cet article explique comment convertir un fichier PDF en format HTML et enregistrer les images du fichier PDF dans un dossier particulier.

L'extrait de code suivant vous montre toutes les options possibles que vous pouvez utiliser lors de la conversion de PDF en HTML.

```php
// Créer un nouvel objet Document et charger le fichier PDF d'entrée
$document = new Document($inputFile);

// Créer un nouvel objet HtmlSaveOptions pour enregistrer le document en tant que HTML
$saveOption = new HtmlSaveOptions();

// Enregistrer le document en tant que HTML en utilisant les options de sauvegarde spécifiées
$document->save($outputFile, $saveOption);
```

## Convertir PDF en HTML - Division de la sortie en HTML multi-pages

Aspose.PDF pour PHP prend en charge la fonctionnalité de conversion de documents PDF en divers formats de sortie, y compris HTML. Cependant, lors de la conversion de fichiers PDF volumineux (composés de plusieurs pages), vous pouvez avoir besoin de sauvegarder chaque page PDF individuelle dans un fichier HTML séparé.

Lors de la conversion d'un fichier PDF volumineux avec plusieurs pages au format HTML, le résultat apparaît comme une seule page HTML. Cela peut finir par être très long. Pour contrôler la taille de la page, il est possible de diviser la sortie en plusieurs pages pendant la conversion de PDF en HTML. Veuillez essayer d'utiliser l'extrait de code suivant.

```php
// Créer un nouvel objet Document et charger le fichier PDF d'entrée
$document = new Document($inputFile);

// Créer un nouvel objet HtmlSaveOptions pour enregistrer le document en HTML
$saveOption = new HtmlSaveOptions();

// Spécifier de diviser la sortie en plusieurs pages
$saveOption->setSplitIntoPages(true);

// Enregistrer le document en HTML en utilisant les options de sauvegarde spécifiées
$document->save($outputFile, $saveOption);
```

## Convertir PDF en HTML - Éviter d'enregistrer les images au format SVG


Le format de sortie par défaut pour enregistrer des images lors de la conversion de PDF en HTML est SVG. Pendant la conversion, certaines images du PDF sont transformées en images vectorielles SVG. Cela peut être lent. Au lieu de cela, les images peuvent être transformées en PNG. Pour permettre cela, Aspose.PDF a l'option d'utiliser SVG pour les vecteurs ou de créer des PNG.

Afin de supprimer complètement le rendu des images au format SVG lors de la conversion des fichiers PDF au format HTML, veuillez essayer d'utiliser l'extrait de code suivant.

```php
// Créez un nouvel objet Document et chargez le fichier PDF d'entrée
$document = new Document($inputFile);

// Créez un nouvel objet HtmlSaveOptions pour enregistrer le document en tant que HTML
$saveOption = new HtmlSaveOptions();

// Spécifiez le dossier où les images SVG sont enregistrées lors de la conversion de PDF en HTML
$saveOption->setSpecialFolderForSvgImages(DATA_DIR);

// Enregistrez le document en tant que HTML en utilisant les options de sauvegarde spécifiées
$document->save($outputFile, $saveOption);
```

## Compression des images SVG lors de la conversion

Pour compresser les images SVG lors de la conversion de PDF en HTML, veuillez essayer d'utiliser le code suivant :

```php
// Créez un nouvel objet Document et chargez le fichier PDF d'entrée
$document = new Document($inputFile);

// Créez un nouvel objet HtmlSaveOptions pour enregistrer le document en tant que HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions = setCompressSvgGraphicsIfAny(true);

// Enregistrez le document en tant que HTML en utilisant les options d'enregistrement spécifiées
$document->save($outputFile, $saveOptions);
```

## Convertir PDF en HTML - Spécifier le dossier des images

Par défaut, lors de la conversion d'un fichier PDF en HTML, les images dans le PDF sont enregistrées dans un dossier séparé créé dans le même répertoire que celui dans lequel le HTML de sortie est créé. Mais parfois, il est nécessaire de spécifier un dossier différent pour enregistrer les images lors de la génération de fichiers HTML. Pour cela, nous avons introduit les [SaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/SaveOptions).

La méthode [setSpecialFolderForAllImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlsaveoptions/#setSpecialFolderForSvgImages-java.lang.String-) est utilisée pour spécifier le dossier cible pour stocker les images.


```php
// Créer un nouvel objet Document et charger le fichier PDF d'entrée
$document = new Document($inputFile);

// Créer un nouvel objet HtmlSaveOptions pour enregistrer le document en tant que HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setSpecialFolderForAllImages(DATA_DIR);

// Enregistrer le document en tant que HTML en utilisant les options d'enregistrement spécifiées
$document->save($outputFile, $saveOptions);
```

## Rendu de Texte Transparent

Dans le cas où le fichier PDF source/d'entrée contient des textes transparents masqués par des images de premier plan, il peut y avoir des problèmes de rendu de texte. Donc, afin de prendre en compte ces scénarios, les propriétés SaveShadowedTextsAsTransparentTexts et SaveTransparentTexts peuvent être utilisées.

```php
// Créer un nouvel objet Document et charger le fichier PDF d'entrée
$document = new Document($inputFile);

// Créer un nouvel objet HtmlSaveOptions pour enregistrer le document en tant que HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setSaveShadowedTextsAsTransparentTexts(true);
$saveOptions->setTransparentTexts(true);

// Enregistrer le document en tant que HTML en utilisant les options d'enregistrement spécifiées
$document->save($outputFile, $saveOptions);
```


## Rendu des couches de document PDF

Nous pouvons rendre les couches de document PDF dans un élément de type couche distinct lors de la conversion PDF en HTML :

```php
// Créer un nouvel objet Document et charger le fichier PDF d'entrée
$document = new Document($inputFile);

// Créer un nouvel objet HtmlSaveOptions pour enregistrer le document en tant que HTML
$saveOptions = new HtmlSaveOptions();
$saveOptions->setConvertMarkedContentToLayers(true);

// Enregistrer le document en tant que HTML en utilisant les options de sauvegarde spécifiées
$document->save($outputFile, $saveOptions);
```

La conversion PDF en HTML est l'une des fonctionnalités les plus populaires d'Aspose.PDF car elle permet de visualiser le contenu des fichiers PDF sur diverses plateformes sans utiliser de visionneuse de documents PDF. Le HTML de sortie est conforme aux normes WWW et peut être facilement affiché dans tous les navigateurs web. En utilisant cette fonctionnalité, les fichiers PDF peuvent être visualisés sur des appareils portables car vous n'avez pas besoin d'installer une application de visualisation PDF mais pouvez utiliser un simple navigateur web.