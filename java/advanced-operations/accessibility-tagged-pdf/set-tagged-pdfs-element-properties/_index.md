---
title: Setting Structure Elements Properties in Tagged PDF
linktitle: Setting Structure Elements Properties
type: docs
weight: 30
url: /java/set-tagged-pdfs-element-properties/
description: With Aspose.PDF for Java, you may set different Structure Elements Properties. There are setting Text Block Structure Elements, setting Inline Structure Elements, adding Structure Element into Elements and etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Setting Structure Elements Properties

In order to set structure elements properties in a Tagged PDF Document, Aspose.PDF offers **createSectElement()** and **createHeaderElement()** methods of [ITaggedContent](https://apireference.aspose.com/java/pdf/com.aspose.pdf.tagged/ITaggedContent) Interface. Following code snippet shows how to set structure elements properties of a Tagged PDF Document:

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
// The path to the documents directory.
String path = "pathTodir";
// Create Pdf Document
Document document = new Document();

// Get Content for work with TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Set Title and Language for Documnet
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Create Structure Elements
StructureElement rootElement = taggedContent.getRootElement();

SectElement sect = taggedContent.createSectElement();
rootElement.appendChild(sect);

HeaderElement h1 = taggedContent.createHeaderElement(1);
sect.appendChild(h1);
h1.setText("The Header");

h1.setTitle("Title");
h1.setLanguage("en-US");
h1.setAlternativeText("Alternative Text");
h1.setExpansionText("Expansion Text");
h1.setActualText("Actual Text");

// Save Tagged Pdf Document
document.save(path + "StructureElementsProperties.pdf");
```

## Setting Text Structure Elements

In order to set text structure elements of a Tagged PDF Document, Aspose.PDF offers [ParagraphElement](https://apireference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement) Class. Following code snippet shows how to set text structure elements of a Tagged PDF Document:

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
// The path to the documents directory.
String path = "pathTodir";

// Create Pdf Document
Document document = new Document();

// Get Content for work with TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Set Title and Language for Documnet
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Get Root Structure Elements
StructureElement rootElement = taggedContent.getRootElement();

ParagraphElement p = taggedContent.createParagraphElement();
// Set Text to Text Structure Element
p.setText("Paragraph.");
rootElement.appendChild(p);


// Save Tagged Pdf Document
document.save(path + "TextStructureElement.pdf");
```

## Setting Text Block Structure Elements

In order to set text block structure elements of a Tagged PDF Document, Aspose.PDF offers [HeaderElement](https://apireference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls.class-use/headerelement) and [ParagraphElement](https://apireference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement) Classes. You can append objects of these classes as a child of **StructureElement** object. Following code snippet shows how to set text block structure elements of a Tagged PDF Document:

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
// The path to the documents directory.
String path = "pathTodir";

// Create Pdf Document
Document document = new Document();

// Get Content for work with TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Set Title and Language for Documnet
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Get Root Structure Element
StructureElement rootElement = taggedContent.getRootElement();

HeaderElement h1 = taggedContent.createHeaderElement(1);
HeaderElement h2 = taggedContent.createHeaderElement(2);
HeaderElement h3 = taggedContent.createHeaderElement(3);
HeaderElement h4 = taggedContent.createHeaderElement(4);
HeaderElement h5 = taggedContent.createHeaderElement(5);
HeaderElement h6 = taggedContent.createHeaderElement(6);
h1.setText("H1. Header of Level 1");
h2.setText("H2. Header of Level 2");
h3.setText("H3. Header of Level 3");
h4.setText("H4. Header of Level 4");
h5.setText("H5. Header of Level 5");
h6.setText("H6. Header of Level 6");
rootElement.appendChild(h1);
rootElement.appendChild(h2);
rootElement.appendChild(h3);
rootElement.appendChild(h4);
rootElement.appendChild(h5);
rootElement.appendChild(h6);

ParagraphElement p = taggedContent.createParagraphElement();
p.setText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
rootElement.appendChild(p);

// Save Tagged Pdf Document
document.save(path + "TextBlockStructureElements.pdf");
```

## Setting Inline Structure Elements

In order to set inline structure elements of a Tagged PDF Document, Aspose.PDF offers [SpanElement](https://apireference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.ils/spanelement) and [ParagraphElement](https://apireference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement) Classes. You can append objects of these classes as a child of **StructureElement** object. Following code snippet shows how to set inline structure elements of a Tagged PDF Document:

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
// The path to the documents directory.
String path = "pathTodir";
// Create Pdf Document
Document document = new Document();

// Get Content for work with TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Set Title and Language for Documnet
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Get Root Structure Element
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
spanH12.setText("Level 1 Header");
h1.appendChild(spanH12);

SpanElement spanH21 = taggedContent.createSpanElement();
spanH21.setText("H2. ");
h2.appendChild(spanH21);
SpanElement spanH22 = taggedContent.createSpanElement();
spanH22.setText("Level 2 Header");
h2.appendChild(spanH22);

SpanElement spanH31 = taggedContent.createSpanElement();
spanH31.setText("H3. ");
h3.appendChild(spanH31);
SpanElement spanH32 = taggedContent.createSpanElement();
spanH32.setText("Level 3 Header");
h3.appendChild(spanH32);

SpanElement spanH41 = taggedContent.createSpanElement();
spanH41.setText("H4. ");
h4.appendChild(spanH41);
SpanElement spanH42 = taggedContent.createSpanElement();
spanH42.setText("Level 4 Header");
h4.appendChild(spanH42);

SpanElement spanH51 = taggedContent.createSpanElement();
spanH51.setText("H5. ");
h5.appendChild(spanH51);
SpanElement spanH52 = taggedContent.createSpanElement();
spanH52.setText("Level 5 Header");
h5.appendChild(spanH52);

SpanElement spanH61 = taggedContent.createSpanElement();
spanH61.setText("H6. ");
h6.appendChild(spanH61);
SpanElement spanH62 = taggedContent.createSpanElement();
spanH62.setText("Level 6 Header");
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

// Save Tagged Pdf Document
document.save(path + "InlineStructureElements.pdf");
```

## Setting Custom Tag Name

In order to set a custom tag name of the elements of a Tagged PDF Document, Aspose.PDF offers **setTag()** method for elements. Following code snippet shows how to set custom tag name:

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
// The path to the documents directory.
String path = "pathTodir";
// Create Pdf Document
Document document = new Document();

// Get Content for work with TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Set Title and Language for Documnet
taggedContent.setTitle("Tagged Pdf Document");
taggedContent.setLanguage("en-US");

// Create Logical Structure Elements
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

// Save Tagged Pdf Document
document.save(path + "CustomTag.pdf");
```

## Adding Structure Element into Elements

In order to set link structure elements in a Tagged PDF Document, Aspose.PDF offers **createLinkElement()** method of [ITaggedContent](https://apireference.aspose.com/java/pdf/com.aspose.pdf.tagged/ITaggedContent) Interface. Following code snippet shows how to set structure elements in paragraph with text of Tagged PDF Document:

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
// The path to the documents directory.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "AddStructureElementIntoElement_Output.pdf";
String logFile = dataDir + "46144_log.xml";

// Creation document and getting Tagged Pdf Content
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();


// Setting Title and Nature Language for document
taggedContent.setTitle("Text Elements Example");
taggedContent.setLanguage("en-US");

// Getting Root structure element (Document structure element)
StructureElement rootElement = taggedContent.getRootElement();


ParagraphElement p1 = taggedContent.createParagraphElement();
rootElement.appendChild(p1);
SpanElement span11 = taggedContent.createSpanElement();
span11.setText("Span_11");
SpanElement span12 = taggedContent.createSpanElement();
span12.setText(" and Span_12.");
p1.setText("Paragraph with ");
p1.appendChild(span11);
p1.appendChild(span12);


ParagraphElement p2 = taggedContent.createParagraphElement();
rootElement.appendChild(p2);
SpanElement span21 = taggedContent.createSpanElement();
span21.setText("Span_21");
SpanElement span22 = taggedContent.createSpanElement();
span22.setText("Span_22.");
p2.appendChild(span21);
p2.setText(" and ");
p2.appendChild(span22);


ParagraphElement p3 = taggedContent.createParagraphElement();
rootElement.appendChild(p3);
SpanElement span31 = taggedContent.createSpanElement();
span31.setText("Span_31");
SpanElement span32 = taggedContent.createSpanElement();
span32.setText(" and Span_32");
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
span421.setText("Span 421 and ");
span42.appendChild(span421);
span42.setText("Span_42");
p4.appendChild(span41);
p4.appendChild(span42);
p4.setText(".");


// Save Tagged Pdf Document
document.save(outFile);
```

## Setting Note Structure Element

Aspose.PDF for Java API also allows you to add **NoteElement** in a tagged PDF document. Following code snippet shows how to add note element in Tagged PDF Document:

```java
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-Java
// The path to the documents directory.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "CreateNoteStructureElement.pdf";
String logFile = dataDir + "45929_log.xml";

// Create Pdf Document
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Sample of Note Elements");
taggedContent.setLanguage("en-US");

// Add Paragraph Element
ParagraphElement paragraph = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(paragraph);

// Add NoteElement
NoteElement note1 = taggedContent.createNoteElement();
paragraph.appendChild(note1);
note1.setText("Note with auto generate ID. ");

// Add NoteElement
NoteElement note2 = taggedContent.createNoteElement();
paragraph.appendChild(note2);
note2.setText("Note with ID = 'note_002'. ");
note2.setId("note_002");

// Add NoteElement
NoteElement note3 = taggedContent.createNoteElement();
paragraph.appendChild(note3);
note3.setText("Note with ID = 'note_003'. ");
note3.setId("note_003");
// Save Tagged Pdf Document
document.save(outFile);
```
