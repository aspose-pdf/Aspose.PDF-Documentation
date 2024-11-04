---
title: Définir les Propriétés des Éléments de Structure dans un PDF Tagué
linktitle: Définir les Propriétés des Éléments de Structure
type: docs
weight: 30
url: /java/set-tagged-pdfs-element-properties/
description: Avec Aspose.PDF pour Java, vous pouvez définir différentes propriétés des éléments de structure. Il s'agit de définir les éléments de structure de bloc de texte, de définir les éléments de structure en ligne, d'ajouter un élément de structure dans les éléments, etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Définir les Propriétés des Éléments de Structure

Pour définir les propriétés des éléments de structure dans un document PDF tagué, Aspose.PDF propose les méthodes **createSectElement()** et **createHeaderElement()** de l'interface [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Le code suivant montre comment définir les propriétés des éléments de structure d'un document PDF tagué :

```java
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Le chemin vers le répertoire des documents.
String path = "pathTodir";
// Créer un document PDF
Document document = new Document();

// Obtenir le contenu pour travailler avec TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Définir le titre et la langue pour le document
taggedContent.setTitle("Document PDF Tagué");
taggedContent.setLanguage("en-US");

// Créer des éléments de structure
StructureElement rootElement = taggedContent.getRootElement();

SectElement sect = taggedContent.createSectElement();
rootElement.appendChild(sect);

HeaderElement h1 = taggedContent.createHeaderElement(1);
sect.appendChild(h1);
h1.setText("L'En-tête");

h1.setTitle("Titre");
h1.setLanguage("en-US");
h1.setAlternativeText("Texte Alternatif");
h1.setExpansionText("Texte d'Extension");
h1.setActualText("Texte Réel");

// Sauvegarder le document PDF tagué
document.save(path + "StructureElementsProperties.pdf");
```


## Définir les Éléments de Structure de Texte

Afin de définir les éléments de structure de texte d'un Document PDF Étiqueté, Aspose.PDF propose la classe [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement). Le code suivant montre comment définir les éléments de structure de texte d'un Document PDF Étiqueté :

```java
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Le chemin vers le répertoire des documents.
String path = "pathTodir";

// Créer un Document Pdf
Document document = new Document();

// Obtenir le Contenu pour travailler avec TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Définir le Titre et la Langue pour le Document
taggedContent.setTitle("Document Pdf Étiqueté");
taggedContent.setLanguage("en-US");

// Obtenir les Éléments de Structure Racine
StructureElement rootElement = taggedContent.getRootElement();

ParagraphElement p = taggedContent.createParagraphElement();
// Définir le Texte de l'Élément de Structure de Texte
p.setText("Paragraphe.");
rootElement.appendChild(p);

// Sauvegarder le Document Pdf Étiqueté
document.save(path + "TextStructureElement.pdf");
```


## Définir les éléments de structure de bloc de texte

Afin de définir les éléments de structure de bloc de texte d'un document PDF balisé, Aspose.PDF propose les classes [HeaderElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls.class-use/headerelement) et [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement). Vous pouvez ajouter des objets de ces classes comme enfant de l'objet **StructureElement**. Le code suivant montre comment définir les éléments de structure de bloc de texte d'un document PDF balisé :

```java
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Le chemin vers le répertoire des documents.
String path = "pathTodir";

// Créer un document PDF
Document document = new Document();

// Obtenez le contenu pour travailler avec TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Définir le titre et la langue du document
taggedContent.setTitle("Document PDF balisé");
taggedContent.setLanguage("en-US");

// Obtenez l'élément de structure racine
StructureElement rootElement = taggedContent.getRootElement();

HeaderElement h1 = taggedContent.createHeaderElement(1);
HeaderElement h2 = taggedContent.createHeaderElement(2);
HeaderElement h3 = taggedContent.createHeaderElement(3);
HeaderElement h4 = taggedContent.createHeaderElement(4);
HeaderElement h5 = taggedContent.createHeaderElement(5);
HeaderElement h6 = taggedContent.createHeaderElement(6);
h1.setText("H1. En-tête de niveau 1");
h2.setText("H2. En-tête de niveau 2");
h3.setText("H3. En-tête de niveau 3");
h4.setText("H4. En-tête de niveau 4");
h5.setText("H5. En-tête de niveau 5");
h6.setText("H6. En-tête de niveau 6");
rootElement.appendChild(h1);
rootElement.appendChild(h2);
rootElement.appendChild(h3);
rootElement.appendChild(h4);
rootElement.appendChild(h5);
rootElement.appendChild(h6);

ParagraphElement p = taggedContent.createParagraphElement();
p.setText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
rootElement.appendChild(p);

// Enregistrer le document PDF balisé
document.save(path + "TextBlockStructureElements.pdf");
```


## Définir les Éléments de Structure Inline

Afin de définir des éléments de structure inline d'un document PDF balisé, Aspose.PDF propose les classes [SpanElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.ils/spanelement) et [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement). Vous pouvez ajouter des objets de ces classes comme un enfant de l'objet **StructureElement**. Le code suivant montre comment définir des éléments de structure inline d'un document PDF balisé :

```java
// Pour des exemples complets et des fichiers de données, veuillez consulter https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Le chemin vers le répertoire des documents.
String path = "pathTodir";
// Créer un document Pdf
Document document = new Document();

// Obtenir le contenu pour travailler avec TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Définir le titre et la langue du document
taggedContent.setTitle("Document PDF balisé");
taggedContent.setLanguage("en-US");

// Obtenir l'élément de structure racine
StructureElement rootElement = taggedContent.getRootElement();

HeaderElement h1 = taggedContent.createHeaderElement(1);
HeaderElement h2 = taggedContent.createHeaderElement(2);
HeaderElement h3 = taggedContent.createHeaderElement(3);
HeaderElement h4 = taggedContent.createHeaderElement(4);
HeaderElement h5 = taggedContent.createHeaderElement(5);
HeaderElement h6 = taggedContent.createHeaderElement(6);
rootElement.appendChild(h1);
rootElement.appendChild(h2);
rootElement.appendChild(h3);
rootElement.appendChild(h4);
rootElement.appendChild(h5);
rootElement.appendChild(h6);

SpanElement spanH11 = taggedContent.createSpanElement();
spanH11.setText("H1. ");
h1.appendChild(spanH11);
SpanElement spanH12 = taggedContent.createSpanElement();
spanH12.setText("En-tête de niveau 1");
h1.appendChild(spanH12);

SpanElement spanH21 = taggedContent.createSpanElement();
spanH21.setText("H2. ");
h2.appendChild(spanH21);
SpanElement spanH22 = taggedContent.createSpanElement();
spanH22.setText("En-tête de niveau 2");
h2.appendChild(spanH22);

SpanElement spanH31 = taggedContent.createSpanElement();
spanH31.setText("H3. ");
h3.appendChild(spanH31);
SpanElement spanH32 = taggedContent.createSpanElement();
spanH32.setText("En-tête de niveau 3");
h3.appendChild(spanH32);

SpanElement spanH41 = taggedContent.createSpanElement();
spanH41.setText("H4. ");
h4.appendChild(spanH41);
SpanElement spanH42 = taggedContent.createSpanElement();
spanH42.setText("En-tête de niveau 4");
h4.appendChild(spanH42);

SpanElement spanH51 = taggedContent.createSpanElement();
spanH51.setText("H5. ");
h5.appendChild(spanH51);
SpanElement spanH52 = taggedContent.createSpanElement();
spanH52.setText("En-tête de niveau 5");
h5.appendChild(spanH52);

SpanElement spanH61 = taggedContent.createSpanElement();
spanH61.setText("H6. ");
h6.appendChild(spanH61);
SpanElement spanH62 = taggedContent.createSpanElement();
spanH62.setText("En-tête de niveau 6");
h6.appendChild(spanH62);

ParagraphElement p = taggedContent.createParagraphElement();
p.setText("P. ");
rootElement.appendChild(p);
SpanElement span1 = taggedContent.createSpanElement();
span1.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ");
p.appendChild(span1);
SpanElement span2 = taggedContent.createSpanElement();
span2.setText("Aenean nec lectus ac sem faucibus imperdiet. ");
p.appendChild(span2);
SpanElement span3 = taggedContent.createSpanElement();
span3.setText("Sed ut erat ac magna ullamcorper hendrerit. ");
p.appendChild(span3);
SpanElement span4 = taggedContent.createSpanElement();
span4.setText("Cras pellentesque libero semper, gravida magna sed, luctus leo. ");
p.appendChild(span4);
SpanElement span5 = taggedContent.createSpanElement();
span5.setText("Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. ");
p.appendChild(span5);
SpanElement span6 = taggedContent.createSpanElement();
span6.setText("Interdum et malesuada fames ac ante ipsum primis in faucibus. ");
p.appendChild(span6);
SpanElement span7 = taggedContent.createSpanElement();
span7.setText("Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. ");
p.appendChild(span7);
SpanElement span8 = taggedContent.createSpanElement();
span8.setText("Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. ");
p.appendChild(span8);
SpanElement span9 = taggedContent.createSpanElement();
span9.setText("Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
p.appendChild(span9);
SpanElement span10 = taggedContent.createSpanElement();
span10.setText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
p.appendChild(span10);

// Enregistrer le document PDF balisé
document.save(path + "InlineStructureElements.pdf");
```


## Définir un Nom de Tag Personnalisé

Afin de définir un nom de tag personnalisé pour les éléments d'un Document PDF Tagué, Aspose.PDF propose la méthode **setTag()** pour les éléments. Le code suivant montre comment définir un nom de tag personnalisé :

```java
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Le chemin vers le répertoire des documents.
String path = "pathTodir";
// Créer un Document PDF
Document document = new Document();

// Obtenir le contenu pour travailler avec TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Définir le titre et la langue pour le document
taggedContent.setTitle("Document PDF Tagué");
taggedContent.setLanguage("en-US");

// Créer des Éléments de Structure Logique
SectElement sect = taggedContent.createSectElement();
taggedContent.getRootElement().appendChild(sect);

ParagraphElement p1 = taggedContent.createParagraphElement();
ParagraphElement p2 = taggedContent.createParagraphElement();
ParagraphElement p3 = taggedContent.createParagraphElement();
ParagraphElement p4 = taggedContent.createParagraphElement();

p1.setText("P1. ");
p2.setText("P2. ");
p3.setText("P3. ");
p4.setText("P4. ");

p1.setTag("P1");
p2.setTag("Para");
p3.setTag("Para");
p4.setTag("Paragraph");

sect.appendChild(p1);
sect.appendChild(p2);
sect.appendChild(p3);
sect.appendChild(p4);

SpanElement span1 = taggedContent.createSpanElement();
SpanElement span2 = taggedContent.createSpanElement();
SpanElement span3 = taggedContent.createSpanElement();
SpanElement span4 = taggedContent.createSpanElement();

span1.setText("Span 1.");
span2.setText("Span 2.");
span3.setText("Span 3.");
span4.setText("Span 4.");

span1.setTag("SPAN");
span2.setTag("Sp");
span3.setTag("Sp");
span4.setTag("TheSpan");

p1.appendChild(span1);
p2.appendChild(span2);
p3.appendChild(span3);
p4.appendChild(span4);

// Enregistrer le Document PDF Tagué
document.save(path + "CustomTag.pdf");
```


## Ajout d'un Élément de Structure aux Éléments

Afin de définir des éléments de structure de lien dans un document PDF balisé, Aspose.PDF offre la méthode **createLinkElement()** de l'interface [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). Le fragment de code suivant montre comment définir des éléments de structure dans un paragraphe avec du texte d'un document PDF balisé :

```java
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Le chemin vers le répertoire des documents.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "AddStructureElementIntoElement_Output.pdf";
String logFile = dataDir + "46144_log.xml";

// Création du document et obtention du contenu PDF balisé
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();


// Définition du titre et de la langue naturelle pour le document
taggedContent.setTitle("Exemple d'Éléments de Texte");
taggedContent.setLanguage("en-US");

// Obtention de l'élément de structure racine (élément de structure du document)
StructureElement rootElement = taggedContent.getRootElement();


ParagraphElement p1 = taggedContent.createParagraphElement();
rootElement.appendChild(p1);
SpanElement span11 = taggedContent.createSpanElement();
span11.setText("Span_11");
SpanElement span12 = taggedContent.createSpanElement();
span12.setText(" et Span_12.");
p1.setText("Paragraphe avec ");
p1.appendChild(span11);
p1.appendChild(span12);


ParagraphElement p2 = taggedContent.createParagraphElement();
rootElement.appendChild(p2);
SpanElement span21 = taggedContent.createSpanElement();
span21.setText("Span_21");
SpanElement span22 = taggedContent.createSpanElement();
span22.setText("Span_22.");
p2.appendChild(span21);
p2.setText(" et ");
p2.appendChild(span22);


ParagraphElement p3 = taggedContent.createParagraphElement();
rootElement.appendChild(p3);
SpanElement span31 = taggedContent.createSpanElement();
span31.setText("Span_31");
SpanElement span32 = taggedContent.createSpanElement();
span32.setText(" et Span_32");
p3.appendChild(span31);
p3.appendChild(span32);
p3.setText(".");


ParagraphElement p4 = taggedContent.createParagraphElement();
rootElement.appendChild(p4);
SpanElement span41 = taggedContent.createSpanElement();
SpanElement span411 = taggedContent.createSpanElement();
span411.setText("Span_411, ");
span41.setText("Span_41, ");
span41.appendChild(span411);
SpanElement span42 = taggedContent.createSpanElement();
SpanElement span421 = taggedContent.createSpanElement();
span421.setText("Span 421 et ");
span42.appendChild(span421);
span42.setText("Span_42");
p4.appendChild(span41);
p4.appendChild(span42);
p4.setText(".");


// Enregistrer le document PDF balisé
document.save(outFile);
```


## Définir l'élément de structure de note

Aspose.PDF pour Java API vous permet également d'ajouter un **NoteElement** dans un document PDF balisé. Le code suivant montre comment ajouter un élément de note dans un document PDF balisé :

```java
// Pour des exemples complets et des fichiers de données, veuillez visiter https://github.com/aspose-pdf/Aspose.PDF-for-Java
// Le chemin vers le répertoire des documents.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "CreateNoteStructureElement.pdf";
String logFile = dataDir + "45929_log.xml";

// Créer un document Pdf
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Exemple d'éléments de note");
taggedContent.setLanguage("en-US");

// Ajouter un élément de paragraphe
ParagraphElement paragraph = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(paragraph);

// Ajouter NoteElement
NoteElement note1 = taggedContent.createNoteElement();
paragraph.appendChild(note1);
note1.setText("Note avec ID généré automatiquement. ");

// Ajouter NoteElement
NoteElement note2 = taggedContent.createNoteElement();
paragraph.appendChild(note2);
note2.setText("Note avec ID = 'note_002'. ");
note2.setId("note_002");

// Ajouter NoteElement
NoteElement note3 = taggedContent.createNoteElement();
paragraph.appendChild(note3);
note3.setText("Note avec ID = 'note_003'. ");
note3.setId("note_003");
// Enregistrer le document PDF balisé
document.save(outFile);
```