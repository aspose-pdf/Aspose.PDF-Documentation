---
title: Convertir PDF en documents Microsoft Word en Java
linktitle: Convertir PDF en Word
type: docs
weight: 10
url: /fr/java/convert-pdf-to-word/
lastmod: "2021-11-19"
description: Convertissez facilement un fichier PDF en formats DOC et DOCX avec un contrôle total grâce à Aspose.PDF pour Java. Apprenez-en plus sur comment optimiser la conversion de PDF en documents Microsoft Word.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Vue d'ensemble

Cet article explique comment convertir un PDF en Word en utilisant Java. Le code est très simple, il suffit de charger le PDF dans la classe Document et de l'enregistrer au format de sortie Microsoft Word DOC ou DOCX. Il couvre les sujets suivants

- [Java PDF en Word](#convert-pdf-to-doc)
- [Java PDF en DOC](#convert-pdf-to-doc)
- [Java PDF en DOCX](#convert-pdf-to-docx)
- [Java Convertir PDF en Word](#convert-pdf-to-docx)
- [Java Convertir PDF en DOC](#convert-pdf-to-doc)
- [Java Convertir PDF en DOCX](#convert-pdf-to-docx)
- [Java Comment convertir un fichier PDF en DOC Word](#convert-pdf-to-doc) ou [Word DOCX](#convert-pdf-to-docx)

- [Java Bibliothèque PDF en Word, API ou Code pour enregistrer, générer ou créer des documents Word de manière programmatique à partir de PDF](#convert-pdf-to-docx)

## Convertir PDF en DOC

L'une des fonctionnalités les plus populaires est la conversion de PDF en DOC Microsoft Word, ce qui facilite la manipulation du contenu. Aspose.PDF pour Java vous permet de convertir des fichiers PDF en DOC.

**Aspose.PDF pour Java** peut créer des documents PDF à partir de zéro et est un excellent outil pour mettre à jour, éditer et manipuler des documents PDF existants. Une fonctionnalité importante est la capacité de convertir des pages et des documents PDF entiers en images. Une autre fonctionnalité populaire est la conversion de PDF en DOC Microsoft Word, ce qui facilite la manipulation du contenu. (La plupart des utilisateurs ne peuvent pas éditer des documents PDF mais peuvent facilement travailler avec des tableaux, du texte et des images dans Microsoft Word.)

Pour simplifier les choses, Aspose.PDF pour Java fournit un code en deux lignes pour transformer un fichier PDF source en fichier DOC.

Le code Java suivant montre le processus de conversion d'un fichier PDF en format DOC.

1. Créez une instance de l'objet [Document](https://reference.aspose.com/page/java/com.aspose.page/document) avec le document PDF source.
2. Enregistrez-le au format **SaveFormat.Doc** en appelant la méthode **Document.save()**.

```java
public static void convertPDFtoWord() {
    // Ouvrir le document PDF source
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");
    // Enregistrer le fichier au format document MS
    document.save(DATA_DIR + "PDFToDOC_out.doc", SaveFormat.Doc);
    document.close();
}
```

## Utilisation de la classe DocSaveOptions

La [classe DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocSaveOptions) fournit de nombreuses propriétés qui améliorent le processus de conversion des fichiers PDF au format DOC. Parmi ces propriétés, le mode permet de spécifier le mode de reconnaissance pour le contenu PDF. Vous pouvez spécifier n'importe quelle valeur de l'énumération RecognitionMode pour cette propriété. Chacune de ces valeurs a des avantages et des limitations spécifiques :

- Le mode [Textbox](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) est rapide et bon pour préserver l'apparence originale d'un fichier PDF, mais l'éditabilité du document résultant pourrait être limitée.
 Chaque bloc de texte visuellement groupé dans le PDF original est converti en une zone de texte dans le document de sortie. Cela permet d'obtenir une ressemblance maximale avec l'original pour que le document de sortie ait une belle apparence, mais il est entièrement composé de zones de texte, ce qui peut rendre l'édition dans Microsoft Word difficile.

- Flow est le mode de reconnaissance complet, où le moteur effectue un groupement et une analyse à plusieurs niveaux pour restaurer le document original selon l'intention de l'auteur tout en produisant un document facilement éditable. La limitation est que le document de sortie pourrait sembler différent de l'original.

- La propriété RelativeHorizontalProximity peut être utilisée pour contrôler la proximité relative entre les éléments textuels et signifie que la distance est normalisée par la taille de la police. Les polices plus grandes peuvent avoir des distances plus importantes entre les syllabes et être encore considérées comme un tout unique. Elle est spécifiée en pourcentage de la taille de la police, par exemple, 1 = 100%. Cela signifie que deux caractères de 12 pt qui sont placés à 12 pt d'écart sont proximaux.

- RecognitionBullets est utilisé pour activer la reconnaissance des puces lors de la conversion.
```java
public static void convertPDFtoWordDocAdvanced() {
    Path pdfFile = Paths.get(DATA_DIR.toString(), "PDF-to-DOC.pdf");
    Path docFile = Paths.get(DATA_DIR.toString(), "PDF-to-DOC.doc");
    Document document = new Document(pdfFile.toString());
    DocSaveOptions saveOptions = new DocSaveOptions();

    // Spécifiez le format de sortie comme DOC
    saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
    // Définir le mode de reconnaissance comme Flow
    saveOptions.setMode(DocSaveOptions.RecognitionMode.Flow);

    // Définir la proximité horizontale à 2.5
    saveOptions.setRelativeHorizontalProximity(2.5f);

    // Activer la valeur pour reconnaître les puces pendant le processus de conversion
    saveOptions.setRecognizeBullets(true);

    document.save(docFile.toString(), saveOptions);
    document.close();
}
```

{{% alert color="success" %}}
**Essayez de convertir PDF vers DOC en ligne**


Aspose.PDF pour Java vous présente une application gratuite en ligne ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-doc), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Convert PDF to DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) {{% /alert %}}

## Convertir PDF en DOCX

L'énumération DocFormat offre également l'option de choisir DOCX comme format de sortie pour les documents Word. Pour rendre le fichier PDF source au format DOCX, utilisez l'extrait de code spécifié ci-dessous.

## Comment convertir un PDF en DOCX

L'extrait de code Java suivant montre le processus de conversion d'un fichier PDF en format DOCX.

1. Créer une instance de l'objet [Document](https://reference.aspose.com/page/java/com.aspose.page/document) avec le document PDF source.
2. Enregistrez-le au format **SaveFormat.DocX** en appelant la méthode **Document.save()**.

```java
public static void convertPDFtoWord_DOCX_Format() {
    // Ouvrir le document PDF source
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");
    // Enregistrer le fichier DOC résultant
    document.save(DATA_DIR + "saveOptionsOutput_out.doc", SaveFormat.DocX);
    document.close();
}
```

La classe [DocSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions) a une propriété nommée Format qui offre la capacité de spécifier le format du document résultant, c'est-à-dire DOC ou DOCX.
 Afin de convertir un fichier PDF au format DOCX, veuillez passer la valeur Docx de l'énumération DocSaveOptions.DocFormat.

Veuillez consulter l'extrait de code suivant qui offre la possibilité de convertir un fichier PDF au format DOCX avec Java.

```java
public static void convertPDFtoWord_Advanced_DOCX_Format() {
    // Ouvrir le document PDF source
    Document document = new Document(DATA_DIR + "PDFToDOC.pdf");

    // Instancier un objet DocSaveOptions
    DocSaveOptions saveOptions = new DocSaveOptions();
    // Spécifier le format de sortie comme DOCX
    saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
    // Définir d'autres paramètres de DocSaveOptions
    // ....

    // Enregistrer le document au format docx
    document.save("ConvertToDOCX_out.docx", saveOptions);
    document.close();
}
```

{{% alert color="warning" %}}
**Essayez de convertir PDF en DOCX en ligne**

Aspose.PDF pour Java vous propose une application en ligne gratuite ["PDF to DOCX"](https://products.aspose.app/pdf/conversion/pdf-to-docx), où vous pouvez essayer d'examiner la fonctionnalité et la qualité qu'elle offre.
[![Aspose.PDF Conversion PDF to DOCX Free App](pdf_to_docx.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}