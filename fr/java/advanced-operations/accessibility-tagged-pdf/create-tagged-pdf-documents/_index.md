---
title: Créer un PDF Étiqueté
linktitle: Créer un PDF Étiqueté
type: docs
weight: 10
lastmod: "2021-06-05"
url: /fr/java/create-tagged-pdf-documents/
description: Cet article explique comment créer des éléments de structure pour un document PDF étiqueté par programmation en utilisant Aspose.PDF pour Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Création d'Éléments de Structure

Afin de créer des éléments de structure dans un document PDF étiqueté, Aspose.PDF offre des méthodes pour créer des éléments de structure en utilisant l'interface [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Le code suivant montre comment créer des éléments de structure d'un PDF étiqueté :

```java
// Pour des exemples complets et des fichiers de données, veuillez consulter https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Le chemin vers le répertoire des documents.
String path = "pathTodir";

// Créer un document Pdf
Document document = new Document();

// Obtenez le contenu pour travailler avec TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Définir le titre et la langue du document
taggedContent.setTitle("Document Pdf Étiqueté");
taggedContent.setLanguage("en-US");

// Créer des éléments de regroupement
PartElement partElement = taggedContent.createPartElement();
ArtElement artElement = taggedContent.createArtElement();
SectElement sectElement = taggedContent.createSectElement();
DivElement divElement = taggedContent.createDivElement();
BlockQuoteElement blockQuoteElement = taggedContent.createBlockQuoteElement();
CaptionElement captionElement = taggedContent.createCaptionElement();
TOCElement tocElement = taggedContent.createTOCElement();
TOCIElement tociElement = taggedContent.createTOCIElement();
IndexElement indexElement = taggedContent.createIndexElement();
NonStructElement nonStructElement = taggedContent.createNonStructElement();
PrivateElement privateElement = taggedContent.createPrivateElement();

// Créer des éléments de structure de texte au niveau bloc
ParagraphElement paragraphElement = taggedContent.createParagraphElement();
HeaderElement headerElement = taggedContent.createHeaderElement();
HeaderElement h1Element = taggedContent.createHeaderElement(1);

// Créer des éléments de structure de texte en ligne
SpanElement spanElement = taggedContent.createSpanElement();
QuoteElement quoteElement = taggedContent.createQuoteElement();
NoteElement noteElement = taggedContent.createNoteElement();

// Créer des éléments de structure d'illustration
FigureElement figureElement = taggedContent.createFigureElement();
FormulaElement formulaElement = taggedContent.createFormulaElement();

// Les méthodes sont en cours de développement
ListElement listElement = taggedContent.createListElement();
TableElement tableElement = taggedContent.createTableElement();
ReferenceElement referenceElement = taggedContent.createReferenceElement();
BibEntryElement bibEntryElement = taggedContent.createBibEntryElement();
CodeElement codeElement = taggedContent.createCodeElement();
LinkElement linkElement = taggedContent.createLinkElement();
AnnotElement annotElement = taggedContent.createAnnotElement();
RubyElement rubyElement = taggedContent.createRubyElement();
WarichuElement warichuElement = taggedContent.createWarichuElement();
FormElement formElement = taggedContent.createFormElement();

// Enregistrer le document Pdf Étiqueté
document.save(path + "StructureElements.pdf");
```


## Création de l'Arbre des Éléments de Structure

Pour créer un arbre des éléments de structure dans un document PDF étiqueté, Aspose.PDF offre des méthodes pour créer un arbre d'éléments de structure en utilisant l'interface [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Le fragment de code suivant montre comment créer un arbre d'éléments de structure d'un document PDF étiqueté :

```java
// Pour des exemples complets et des fichiers de données, veuillez consulter https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Le chemin vers le répertoire des documents.
String path = "pathTodir";
// Créer un document PDF
Document document = new Document();

// Obtenir le contenu pour travailler avec TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Définir le titre et la langue pour le document
taggedContent.setTitle("Document PDF Étiqueté");
taggedContent.setLanguage("en-US");

// Obtenir l'élément de structure racine (Document)
StructureElement rootElement = taggedContent.getRootElement();

// Créer une structure logique
SectElement sect1 = taggedContent.createSectElement();
rootElement.appendChild(sect1);

SectElement sect2 = taggedContent.createSectElement();
rootElement.appendChild(sect2);

DivElement div11 = taggedContent.createDivElement();
sect1.appendChild(div11);

DivElement div12 = taggedContent.createDivElement();
sect1.appendChild(div12);

ArtElement art21 = taggedContent.createArtElement();
sect2.appendChild(art21);

ArtElement art22 = taggedContent.createArtElement();
sect2.appendChild(art22);

DivElement div211 = taggedContent.createDivElement();
art21.appendChild(div211);

DivElement div212 = taggedContent.createDivElement();
art21.appendChild(div212);

DivElement div221 = taggedContent.createDivElement();
art22.appendChild(div221);

DivElement div222 = taggedContent.createDivElement();
art22.appendChild(div222);

SectElement sect3 = taggedContent.createSectElement();
rootElement.appendChild(sect3);

DivElement div31 = taggedContent.createDivElement();
sect3.appendChild(div31);

// Enregistrer le document PDF étiqueté
document.save(path + "StructureElementsTree.pdf");
```


## Structuration du Texte de Style

Pour styliser la structure du texte dans un document PDF balisé, Aspose.PDF offre les propriétés **setFont()**, **setFontSize()**, **setFontStyle()** et **setForegroundColor()** de la classe [StructureTextState](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/StructureTextState). Le code suivant montre comment styliser la structure du texte dans un document PDF balisé :

```java
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Le chemin vers le répertoire des documents.
String path = "pathTodir";
// Créer un document Pdf
Document document = new Document();

// Obtenir le contenu pour travailler avec TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Définir le titre et la langue pour le document
taggedContent.setTitle("Document Pdf Balisé");
taggedContent.setLanguage("en-US");

ParagraphElement p = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(p);

// En développement
p.getStructureTextState().setFontSize(18F);
p.getStructureTextState().setForegroundColor(Color.getRed());
p.getStructureTextState().setFontStyle(FontStyles.Italic);

p.setText("Texte en italique rouge.");

// Enregistrer le document Pdf balisé
document.save(path + "StyleTextStructure.pdf");
```


## Illustration des Éléments de Structure

Pour illustrer les éléments de structure dans un document PDF balisé, Aspose.PDF propose la classe [IllustrationElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/IllustrationElement). Le code suivant montre comment illustrer les éléments de structure dans un document PDF balisé :

```java
// Pour des exemples complets et des fichiers de données, veuillez consulter https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Le chemin vers le répertoire des documents.
String path = "pathTodir";
// Créer un document Pdf
Document document = new Document();

// Obtenir le contenu pour travailler avec TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Définir le titre et la langue pour le document
taggedContent.setTitle("Document Pdf Balisé");
taggedContent.setLanguage("en-US");

// En cours de développement
IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setActualText("Figure Un");
figure1.setTitle("Image 1");
figure1.setTag("Fig1");
figure1.setImage("image.png");

// Enregistrer le document Pdf Balisé
document.save(path + "IllustrationStructureElements.pdf");
```


## **Créer un PDF avec une Image Étiquetée**

Afin de créer un PDF avec une image étiquetée, Aspose.PDF offre la méthode [createFigureElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createFigureElement--) de l'interface [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Le code suivant montre la fonctionnalité.

```java
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-Java
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("CreatePDFwithTaggedImage");
taggedContent.setLanguage("en-US");

IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setAlternativeText("Logo Aspose");
figure1.setTitle("Image 1");
figure1.setTag("Fig");
// Ajouter une image avec une résolution de 300 DPI (par défaut)
figure1.setImage("aspose-logo.jpg");
// Enregistrer le document PDF
document.save("PDFwithTaggedImage.pdf");
```


## Créer un PDF avec du texte balisé

Afin de créer un PDF avec du texte balisé, Aspose.PDF propose l'interface [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Le code suivant montre la fonctionnalité.

```java
// Pour des exemples complets et des fichiers de données, veuillez vous rendre sur https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Le chemin vers le répertoire des documents.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
// Créer un document Pdf
Document document = new Document();

// Obtenir le contenu pour travailler avec TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Définir le titre et la langue pour le document
taggedContent.setTitle("Document Pdf Balisé");
taggedContent.setLanguage("en-US");

// Créer des éléments de structure de niveau bloc de texte
HeaderElement headerElement = taggedContent.createHeaderElement();
headerElement.setActualText("Titre 1");
ParagraphElement paragraphElement1 = taggedContent.createParagraphElement();
paragraphElement1.setActualText("test1");
ParagraphElement paragraphElement2 = taggedContent.createParagraphElement();
paragraphElement2.setActualText("test 2");
ParagraphElement paragraphElement3 = taggedContent.createParagraphElement();
paragraphElement3.setActualText("test 3");
ParagraphElement paragraphElement4 = taggedContent.createParagraphElement();
paragraphElement4.setActualText("test 4");
ParagraphElement paragraphElement5 = taggedContent.createParagraphElement();
paragraphElement5.setActualText("test 5");
ParagraphElement paragraphElement6 = taggedContent.createParagraphElement();
paragraphElement6.setActualText("test 6");
ParagraphElement paragraphElement7 = taggedContent.createParagraphElement();
paragraphElement7.setActualText("test 7");

// Enregistrer le document PDF
document.save( dataDir + "PDFavecTexteBalise.pdf");
```