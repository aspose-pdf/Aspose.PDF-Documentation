---

title: Convertir PDF en Microsoft Word  
linktitle: Convertir PDF en Word  
type: docs  
weight: 10  
url: /php-java/convert-pdf-to-word/  
lastmod: "2024-05-20"  
description: Convertir un fichier PDF en format DOC et DOCX facilement et avec un contrôle total grâce à Aspose.PDF pour PHP. Apprenez comment optimiser la conversion de PDF en documents Microsoft Word.  
sitemap:  
    changefreq: "monthly"  
    priority: 0.7  

## Aperçu

Cet article explique comment convertir un PDF en Word en utilisant PHP. Le code est très simple, il suffit de charger le PDF dans la classe Document et de l'enregistrer au format de sortie Microsoft Word DOC ou DOCX. Il couvre les sujets suivants

- [PHP PDF en Word](#convert-pdf-to-doc)  
- [PHP PDF en DOC](#convert-pdf-to-doc)  
- [PHP PDF en DOCX](#convert-pdf-to-docx)  
- [PHP Convertir PDF en Word](#convert-pdf-to-docx)  
- [PHP Convertir PDF en DOC](#convert-pdf-to-doc)  
- [PHP Convertir PDF en DOCX](#convert-pdf-to-docx)  
- [PHP Comment convertir un fichier PDF en DOC Word](#convert-pdf-to-doc) ou [DOCX Word](#convert-pdf-to-docx)  

- [PHP Bibliothèque PDF en Word, API ou Code pour enregistrer, générer ou créer des documents Word à partir de PDF de manière programmatique](#convert-pdf-to-docx)  

## Convertir PDF en DOC

L'une des fonctionnalités les plus populaires est la conversion de PDF en DOC Microsoft Word, ce qui rend le contenu facile à manipuler. Aspose.PDF pour PHP vous permet de convertir des fichiers PDF en DOC.

**Aspose.PDF pour PHP** peut créer des documents PDF à partir de zéro et est un excellent outil pour mettre à jour, éditer et manipuler des documents PDF existants. Une fonctionnalité importante est la capacité de convertir des pages et des documents PDF entiers en images. Une autre fonctionnalité populaire est la conversion de PDF en DOC Microsoft Word, ce qui rend le contenu facile à manipuler. (La plupart des utilisateurs ne peuvent pas éditer des documents PDF, mais peuvent facilement travailler avec des tableaux, du texte et des images dans Microsoft Word.)

Pour simplifier les choses, Aspose.PDF pour PHP propose un code en deux lignes pour transformer un fichier PDF source en fichier DOC.

Le fragment de code Java suivant montre le processus de conversion d'un fichier PDF au format DOC.

1. Créez une instance de l'objet [Document](https://reference.aspose.com/page/java/com.aspose.page/document) avec le document PDF source.

2. Enregistrez-le au format **SaveFormat.Doc** en appelant la méthode **Document.save()**.

```php
// Charger le document PDF
$document = new Document($inputFile);

// Créer un nouvel objet DocSaveOptions
$saveOption = new DocSaveOptions();

// Définir le format de sortie sur DOC
$saveOption->setFormat(DocSaveOptions_DocFormat::$Doc);

// Enregistrer le document en tant que DOC
$document->save($outputFile, $saveOption);
```

## Utilisation de la classe DocSaveOptions

La [classe DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocSaveOptions) offre de nombreuses propriétés qui améliorent le processus de conversion des fichiers PDF au format DOC. Parmi ces propriétés, Mode vous permet de spécifier le mode de reconnaissance pour le contenu PDF. Vous pouvez spécifier n'importe quelle valeur de l'énumération RecognitionMode pour cette propriété. Chacune de ces valeurs a des avantages et des limitations spécifiques :

- Le mode [Textbox](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) est rapide et bon pour préserver l'apparence originale d'un fichier PDF, mais l'éditabilité du document résultant pourrait être limitée.
 Chaque bloc de texte visuellement groupé dans le PDF original est converti en une zone de texte dans le document de sortie. Cela permet de ressembler au maximum à l'original pour que le document de sortie soit esthétique, mais il est entièrement composé de zones de texte, ce qui pourrait rendre l'édition dans Microsoft Word difficile.

- Flow est le mode de reconnaissance complet, où le moteur effectue un regroupement et une analyse multiniveau pour restaurer le document original selon l'intention de l'auteur tout en produisant un document facilement modifiable. La limitation est que le document de sortie pourrait sembler différent de l'original.

- La propriété RelativeHorizontalProximity peut être utilisée pour contrôler la proximité relative entre les éléments textuels, ce qui signifie que la distance est normée par la taille de la police. Les polices plus grandes peuvent avoir des distances plus importantes entre les syllabes et être toujours considérées comme un tout unique. Elle est spécifiée en pourcentage de la taille de la police, par exemple, 1 = 100%. Cela signifie que deux caractères de 12pt placés à 12 pt l'un de l'autre sont proximaux.

- RecognitionBullets est utilisé pour activer la reconnaissance des puces lors de la conversion.
```php
// Charger le document PDF
$document = new Document($inputFile);

// Créer un nouvel objet DocSaveOptions
$saveOption = new DocSaveOptions();

// Définir le mode de reconnaissance sur EnhancedFlow
$saveOption->setMode(DocSaveOptions_RecognitionMode::$EnhancedFlow);

// Définir le format de sortie sur DOC
$saveOption->setFormat(DocSaveOptions_DocFormat::$Doc);

// Définir le mode de reconnaissance comme Flow
saveOptions->setMode(DocSaveOptions_RecognitionMode::$Flow);

// Définir la proximité horizontale à 2,5
saveOptions->setRelativeHorizontalProximity(2.5f);

// Activer la reconnaissance des puces lors du processus de conversion
saveOptions->setRecognizeBullets(true);

// Enregistrer le document en tant que DOCX
$document->save($outputFile, $saveOption);
```

{{% alert color="success" %}}
**Essayez de convertir un PDF en DOC en ligne**

Aspose.PDF pour PHP vous propose une application en ligne gratuite ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-doc), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.


[![Convertir PDF en DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir PDF en DOCX

L'énumération DocFormat offre également la possibilité de choisir DOCX comme format de sortie pour les documents Word. Pour rendre le fichier PDF source au format DOCX, utilisez l'extrait de code spécifié ci-dessous.

## Comment convertir un PDF en DOCX

L'extrait de code Java suivant montre le processus de conversion d'un fichier PDF en format DOCX.

1. Créez une instance de l'objet [Document](https://reference.aspose.com/page/java/com.aspose.page/document) avec le document PDF source.
2. Enregistrez-le au format **SaveFormat.DocX** en appelant la méthode **Document.save()**.

```php
    // Charger le document PDF
    $document = new Document($inputFile);
    
    // Enregistrer le document en tant que DOCX
    $document->save($outputFile, SaveFormat::$DocX);
```

La classe [DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions) possède une propriété nommée Format qui offre la capacité de spécifier le format du document résultant, c'est-à-dire DOC ou DOCX.
 Afin de convertir un fichier PDF au format DOCX, veuillez passer la valeur Docx de l'énumération DocSaveOptions.DocFormat.

Veuillez consulter l'extrait de code suivant qui fournit la capacité de convertir un fichier PDF au format DOCX avec Java.

```php
// Charger le document PDF
$document = new Document($inputFile);

// Créer un nouvel objet DocSaveOptions
$saveOption = new DocSaveOptions();

// Définir le mode de reconnaissance sur EnhancedFlow
$saveOption->setMode(DocSaveOptions_RecognitionMode::$EnhancedFlow);

// Définir le format de sortie sur DOCX
$saveOption->setFormat(DocSaveOptions_DocFormat::$DocX);

// Enregistrer le document en tant que DOCX
$document->save($outputFile, $saveOption);
```

{{% alert color="warning" %}}
**Essayez de convertir PDF en DOCX en ligne**

Aspose.PDF pour PHP vous présente l'application en ligne gratuite ["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité de son fonctionnement.


[![Application gratuite Aspose.PDF Conversion PDF en DOCX](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)