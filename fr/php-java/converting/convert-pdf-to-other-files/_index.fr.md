---
title: Convertir un fichier PDF en d'autres formats
linktitle: Convertir PDF en d'autres formats
type: docs
weight: 90
url: /php-java/convert-pdf-to-other-files/
lastmod: "2024-05-20"
description: Ce sujet vous montre comment Aspose.PDF permet de convertir un fichier PDF en d'autres formats de fichier.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir PDF en EPUB

{{% alert color="success" %}}
**Essayez de convertir PDF en EPUB en ligne**

Aspose.PDF pour PHP vous présente l'application en ligne gratuite ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en EPUB avec une application gratuite](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** (abréviation de publication électronique) est une norme de livre électronique libre et ouverte de l'International Digital Publishing Forum (IDPF).
 Les fichiers ont l'extension .epub. EPUB est conçu pour un contenu reformatable, ce qui signifie qu'un lecteur EPUB peut optimiser le texte pour un appareil d'affichage particulier. EPUB prend également en charge le contenu à mise en page fixe. Le format est conçu comme un format unique que les éditeurs et les maisons de conversion peuvent utiliser en interne, ainsi que pour la distribution et la vente. Il remplace la norme Open eBook.

Aspose.PDF pour PHP prend en charge la fonctionnalité de conversion de documents PDF en format EPUB. Aspose.PDF pour PHP a une classe nommée [EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions) qui peut être utilisée comme second argument de la méthode [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-) pour générer un fichier EPUB. Veuillez essayer d'utiliser l'extrait de code suivant pour répondre à cette exigence.

```php
// Créer une nouvelle instance de la classe Document et charger le fichier PDF d'entrée
$document = new Document($inputFile);

// Créer une nouvelle instance de la classe EpubSaveOptions
$saveOption = new EpubSaveOptions();

// Enregistrer le document au format EPUB en utilisant les options de sauvegarde spécifiées
$document->save($outputFile, $saveOption);
```

## Convertir PDF en LaTeX/TeX

**Aspose.PDF pour PHP** prend en charge la conversion de PDF en LaTeX/TeX. Le format de fichier LaTeX est un format de fichier texte avec un balisage spécial utilisé dans le système de préparation de documents basé sur TeX pour une composition de haute qualité.

Pour convertir des fichiers PDF en TeX, Aspose.PDF dispose de la classe [LaTeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaTeXSaveOptions) qui fournit la méthode `setOutDirectoryPath` pour enregistrer les images temporaires pendant le processus de conversion.

Le code suivant montre le processus de conversion de fichiers PDF au format TEX avec Java.

```php
// Créer un nouvel objet Document et charger le fichier PDF d'entrée
$document = new Document($inputFile);

// Créer un nouvel objet LaTeXSaveOptions
$saveOption = new LaTeXSaveOptions();
$saveOption->setOutDirectoryPath ($pathToOutputDirectory)

// Enregistrer le document au format LaTeX
$document->save($outputFile, $saveOption);
```

{{% alert color="success" %}}
**Essayez de convertir PDF en LaTeX/TeX en ligne**


Aspose.PDF pour PHP vous présente une application en ligne gratuite ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), où vous pouvez essayer de découvrir la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Convertir PDF en Texte

**Aspose.PDF pour PHP** prend en charge la conversion de l'ensemble du document PDF et d'une seule page en un fichier texte.

### Convertir l'ensemble du document PDF en fichier texte

Vous pouvez convertir un document PDF en fichier TXT en utilisant la méthode Visit de la classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber).

Le code suivant explique comment extraire les textes de toutes les pages.

```php
// Charger le document PDF
$document = new Document($inputFile);

// Créer un objet TextAbsorber pour extraire le texte du document
$textAbsorber = new TextAbsorber();

// Extraire le texte du document
$textAbsorber->visit($document);
$content = $textAbsorber->getText();

// Enregistrer le texte extrait dans le fichier de sortie
file_put_contents($outputFile, $content);

// Obtenir la taille du fichier de sortie
$fileSize = filesize($outputFile);
```

{{% alert color="success" %}}
**Essayez de convertir Convertir PDF en texte en ligne**

Aspose.PDF pour PHP vous présente une application en ligne gratuite ["PDF en texte"](https://products.aspose.app/pdf/conversion/pdf-to-txt), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en texte avec application gratuite](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### Convertir une page PDF en fichier texte

Vous pouvez convertir un document PDF en fichier TXT avec Aspose.PDF pour PHP. Vous devez utiliser la méthode Visit de la classe [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) pour résoudre cette tâche.

Le fragment de code suivant explique comment extraire les textes des pages particulières.

```php
// Charger le document PDF
$document = new Document($inputFile);

// Créer un objet TextAbsorber pour extraire le texte du document
$textAbsorber = new TextAbsorber();

$array = array(1, 3, 4);

foreach ($array as $page) {
    $textAbsorber->visit($document->getPages()->get_Item($page));
    $content = $textAbsorber->getText();
    
    $outputFile = $dataDir . DIRECTORY_SEPARATOR . 'result-pdf-to-text'. $page . '.txt';
    // Enregistrer le texte extrait dans le fichier de sortie
    file_put_contents($outputFile, $content);
}
```


## Convertir PDF en XPS

**Aspose.PDF pour PHP** offre la possibilité de convertir des fichiers PDF au format <abbr title="XML Paper Specification">XPS</abbr>. Essayons d'utiliser l'extrait de code présenté pour convertir des fichiers PDF au format XPS avec Java.

{{% alert color="success" %}}
**Essayez de convertir PDF en XPS en ligne**

Aspose.PDF pour PHP vous présente une application gratuite en ligne ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF en XPS avec l'application gratuite](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Le type de fichier XPS est principalement associé au XML Paper Specification de Microsoft Corporation. Le XML Paper Specification (XPS), anciennement connu sous le nom de code Metro et intégrant le concept marketing Next Generation Print Path (NGPP), est l'initiative de Microsoft pour intégrer la création et la visualisation de documents dans le système d'exploitation Windows.

Pour convertir des fichiers PDF en XPS, Aspose.PDF dispose de la classe [XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions) qui est utilisée comme deuxième argument du constructeur Document.save(..) pour générer le fichier XPS.
 Le code ci-dessous montre le processus de conversion de fichiers PDF en format XPS.

```php
// Créez un nouvel objet Document et chargez le fichier PDF d'entrée
$document = new Document($inputFile);

// Créez un nouvel objet XpsSaveOptions
$saveOption = new XpsSaveOptions();

// Enregistrez le document en tant que XPS en utilisant les options de sauvegarde spécifiées
$document->save($outputFile, $saveOption);
```