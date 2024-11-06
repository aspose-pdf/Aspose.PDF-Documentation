---
title: Convertir des documents PDF en documents Microsoft Word en .NET
linktitle: Convertir PDF en Word
type: docs
weight: 10
url: fr/net/convert-pdf-to-word/
lastmod: "2022-08-04"
description: Apprenez à écrire du code C# pour la conversion de formats PDF en Microsoft Word avec Aspose.PDF pour .NET. et optimisez la conversion PDF en DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Aperçu

Cet article explique comment **convertir des documents PDF en documents Microsoft Word en utilisant C#**. Il couvre ces sujets.

_Format_ : **DOC**

- [C# PDF en DOC](#csharp-pdf-to-doc)
- [C# Convertir PDF en DOC](#csharp-pdf-to-doc)
- [C# Comment convertir un fichier PDF en DOC](#csharp-pdf-to-doc)

_Format_ : **DOCX**

- [C# PDF en DOCX](#csharp-pdf-to-docx)
- [C# Convertir PDF en DOCX](#csharp-pdf-to-docx)
- [C# Comment convertir un fichier PDF en DOCX](#csharp-pdf-to-docx)

_Format_ : **Word**

- [C# PDF en Word](#csharp-pdf-to-docx)
- [C# Convertir PDF en Word](#csharp-pdf-to-doc)
- [C# Comment convertir un fichier PDF en Word](#csharp-pdf-to-docx)

Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).
Le code suivant fonctionne également avec la bibliothèque [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Conversion de PDF en DOC et DOCX

L'une des fonctionnalités les plus populaires est la conversion de PDF en document Microsoft Word DOC, ce qui facilite la gestion du contenu. **Aspose.PDF pour .NET** vous permet de convertir des fichiers PDF en formats DOC et DOCX rapidement et efficacement.

## Convertir un PDF en fichier DOC (Microsoft Word 97-2003)

Convertissez des fichiers PDF en format DOC facilement et avec un contrôle complet. Aspose.PDF pour .NET est flexible et prend en charge une grande variété de conversions. Par exemple, convertir des pages de documents PDF en images est une fonctionnalité très populaire.

De nombreux clients ont demandé une conversion de PDF en DOC : convertir un fichier PDF en document Microsoft Word. Les clients le souhaitent car les fichiers PDF ne peuvent pas être facilement modifiés, contrairement aux documents Word. Certaines entreprises souhaitent que leurs utilisateurs puissent manipuler du texte, des tableaux et des images dans des fichiers qui étaient à l'origine des PDFs.

Perpétuant la tradition de rendre les choses simples et compréhensibles, Aspose.PDF pour .NET vous permet de transformer un fichier PDF source en un fichier DOC en deux lignes de code.
Gardant vivante la tradition de rendre les choses simples et compréhensibles, Aspose.PDF pour .NET vous permet de transformer un fichier PDF source en un fichier DOC avec deux lignes de code.

Le code C# suivant montre la conversion d'un fichier PDF au format DOC.

<a name="csharp-pdf-to-doc"><strong>Étapes : Convertir PDF en DOC en C#</strong></a>

1. Créez une instance de l'objet [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document/) avec le document PDF source.
2. Enregistrez-le au format **SaveFormat.Doc** en appelant la méthode **Document.Save()**.

```csharp
public static void ConvertPDFtoWord()
{
    // Ouvrir le document PDF source
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // Enregistrer le fichier au format de document MS
    pdfDocument.Save(_dataDir + "PDFToDOC_out.doc", SaveFormat.Doc);

}
```

### Utiliser la classe DocSaveOptions

La classe [`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) offre de nombreuses propriétés qui améliorent la conversion des fichiers PDF au format DOC.
La classe [`DocSaveOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions) offre de nombreuses propriétés qui améliorent la conversion de fichiers PDF au format DOC.

- Le mode [`Textbox`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) est rapide et efficace pour préserver l'apparence originale du fichier PDF, mais l'éditabilité du document résultant pourrait être limitée. Chaque bloc de texte visuellement regroupé dans le PDF original est converti en une zone de texte dans le document de sortie. Cela permet une ressemblance maximale avec l'original, donc le document de sortie est visuellement agréable, mais il est entièrement composé de zones de texte, ce qui pourrait rendre l'édition dans Microsoft Word assez difficile.
- Le mode [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/recognitionmode) est un mode de reconnaissance complet, où le moteur effectue un regroupement et une analyse multi-niveaux pour restaurer le document original selon l'intention de l'auteur tout en produisant un document facilement éditable.
- [`Flow`](https://reference.aspose.com/pdf/net/aspose.pdf.docsaveoptions/recognitionmode) est un mode de reconnaissance complet, où le moteur effectue un regroupement et une analyse multi-niveaux pour restaurer le document original selon l'intention de l'auteur tout en produisant un document facilement modifiable.

La propriété [`RelativeHorizontalProximity`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/relativehorizontalproximity) peut être utilisée pour contrôler la proximité relative entre les éléments textuels. Cela signifie que la distance est normalisée par la taille de la police. Les polices plus grandes peuvent avoir de plus grands espaces entre les syllabes et être toujours considérées comme un tout unique. Elle est spécifiée en pourcentage de la taille de la police ; par exemple, 1 = 100%. Cela signifie que deux caractères de 12pt placés à 12 pt de distance sont proximaux.
- [`RecognitionBullets`](https://reference.aspose.com/pdf/net/aspose.pdf/docsaveoptions/properties/recognizebullets) est utilisé pour activer la reconnaissance des puces pendant la conversion.

```csharp
public static void ConvertPDFtoWordDocAdvanced()
{
    var pdfFile = Path.Combine(_dataDir, "PDF-to-DOC.pdf");
    var docFile = Path.Combine(_dataDir, "PDF-to-DOC.doc");
    Document pdfDocument = new Document(pdfFile);
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        Format = DocSaveOptions.DocFormat.Doc,
        // Définir le mode de reconnaissance comme Flow
        Mode = DocSaveOptions.RecognitionMode.Flow,
        // Définir la proximité horizontale à 2.5
        RelativeHorizontalProximity = 2.5f,
        // Activer la valeur pour reconnaître les puces pendant le processus de conversion
        RecognizeBullets = true
    };
    pdfDocument.Save(docFile, saveOptions);
}
```
{{% alert color="success" %}}
**Essayez de convertir un PDF en DOC en ligne**

Aspose.PDF pour .NET vous présente une application gratuite en ligne ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), où vous pouvez explorer la fonctionnalité et la qualité de son fonctionnement.

[![Convertir PDF en DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Convertir un PDF en fichier DOCX (Microsoft Word 2007-2021)

L'API Aspose.PDF pour .NET vous permet de lire et de convertir des documents PDF en DOCX en utilisant C# et tout autre langage .NET. Le DOCX est un format bien connu pour les documents Microsoft Word dont la structure a été modifiée de binaire simple à une combinaison de fichiers XML et binaires. Les fichiers Docx peuvent être ouverts avec Word 2007 et les versions ultérieures, mais pas avec les versions antérieures de MS Word, qui prennent en charge les extensions de fichier DOC.

Le morceau de code C# suivant montre comment convertir un fichier PDF en format DOCX.

<a name="csharp-pdf-to-docx"><strong>Étapes : Convertir un PDF en DOCX en C#</strong></a>

1.
1.
2. Enregistrez-le au format **SaveFormat.DocX** en appelant la méthode **Document.Save()**.

```csharp
public static void ConvertPDFtoWord_DOCX_Format()
{
    // Ouvrir le document PDF source
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");
    // Enregistrer le fichier DOC résultant
    pdfDocument.Save(_dataDir + "saveOptionsOutput_out.doc", SaveFormat.DocX);
}
```

### Convertir PDF en DOCX en mode amélioré

Pour obtenir de meilleurs résultats de conversion de PDF en DOCX, vous pouvez utiliser le mode `EnhancedFlow`.
La principale différence entre le mode Flow et le mode Enhanced Flow est que les tables (avec ou sans bordures) sont reconnues comme de véritables tables, et non comme du texte avec une image en arrière-plan.
Il y a aussi la reconnaissance des listes numérotées et de nombreuses autres petites choses.

```csharp
public static void ConvertPDFtoWord_Advanced_DOCX_Format()
{    
    // Ouvrir le document PDF source
    Document pdfDocument = new Document(_dataDir + "PDFToDOC.pdf");

    // Instancier l'objet DocSaveOptions
    DocSaveOptions saveOptions = new DocSaveOptions
    {
        // Spécifier le format de sortie comme DOCX
        Format = DocSaveOptions.DocFormat.DocX,
        // Définir d'autres paramètres de DocSaveOptions
        Mode = DocSaveOptions.RecognitionMode.EnhancedFlow
    };
    // Enregistrer le document au format docx
    pdfDocument.Save("ConvertToDOCX_out.docx", saveOptions);
}
```
{{% alert color="warning" %}}
**Essayez de convertir un PDF en DOCX en ligne**

Aspose.PDF pour .NET vous présente une application gratuite en ligne ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), où vous pouvez essayer d'explorer la fonctionnalité et la qualité de son fonctionnement.

[![Aspose.PDF Conversion PDF to Word Free App](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Voir aussi

Cet article couvre également ces sujets. Les codes sont les mêmes que ci-dessus.

_Format_ : **Word**

- [Code C# PDF vers Word](#csharp-pdf-to-docx)
- [API C# PDF vers Word](#csharp-pdf-to-docx)
- [C# PDF vers Word Programmatically](#csharp-pdf-to-docx)
- [Bibliothèque C# PDF vers Word](#csharp-pdf-to-docx)
- [C# Enregistrer PDF comme Word](#csharp-pdf-to-docx)
- [C# Générer Word depuis PDF](#csharp-pdf-to-docx)
- [C# Créer Word depuis PDF](#csharp-pdf-to-docx)
- [Convertisseur C# PDF vers Word](#csharp-pdf-to-docx)

_Format_ : **DOC**

- [Code C# PDF vers DOC](#csharp-pdf-to-doc)
- [API C# PDF vers DOC](#csharp-pdf-to-doc)
- [API C# PDF vers DOC](#csharp-pdf-to-doc)
- [C# PDF vers DOC Programmation](#csharp-pdf-to-doc)
- [Bibliothèque C# PDF vers DOC](#csharp-pdf-to-doc)
- [C# Enregistrer PDF en tant que DOC](#csharp-pdf-to-doc)
- [C# Générer DOC à partir de PDF](#csharp-pdf-to-doc)
- [C# Créer DOC à partir de PDF](#csharp-pdf-to-doc)
- [Convertisseur C# PDF vers DOC](#csharp-pdf-to-doc)

_Format_ : **DOCX**

- [Code C# PDF vers DOCX](#csharp-pdf-to-docx)
- [API C# PDF vers DOCX](#csharp-pdf-to-docx)
- [C# PDF vers DOCX Programmation](#csharp-pdf-to-docx)
- [Bibliothèque C# PDF vers DOCX](#csharp-pdf-to-docx)
- [C# Enregistrer PDF en tant que DOCX](#csharp-pdf-to-docx)
- [C# Générer DOCX à partir de PDF](#csharp-pdf-to-docx)
- [C# Créer DOCX à partir de PDF](#csharp-pdf-to-docx)
- [Convertisseur C# PDF vers DOCX](#csharp-pdf-to-docx)
