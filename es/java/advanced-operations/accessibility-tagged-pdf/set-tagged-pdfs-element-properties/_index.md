---
title: Configuración de Propiedades de Elementos de Estructura en PDF Etiquetado
linktitle: Configuración de Propiedades de Elementos de Estructura
type: docs
weight: 30
url: es/java/set-tagged-pdfs-element-properties/
description: Con Aspose.PDF para Java, puedes configurar diferentes Propiedades de Elementos de Estructura. Hay configuración de Elementos de Estructura de Bloques de Texto, configuración de Elementos de Estructura en Línea, agregando Elemento de Estructura en Elementos, etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Configuración de Propiedades de Elementos de Estructura

Para configurar las propiedades de los elementos de estructura en un Documento PDF Etiquetado, Aspose.PDF ofrece los métodos **createSectElement()** y **createHeaderElement()** de la Interfaz [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). El siguiente fragmento de código muestra cómo configurar las propiedades de los elementos de estructura de un Documento PDF Etiquetado:

```java
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-Java
// La ruta al directorio de documentos.
String path = "pathTodir";
// Crear Documento PDF
Document document = new Document();

// Obtener Contenido para trabajar con TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Establecer Título e Idioma para el Documento
taggedContent.setTitle("Documento PDF Etiquetado");
taggedContent.setLanguage("en-US");

// Crear Elementos de Estructura
StructureElement rootElement = taggedContent.getRootElement();

SectElement sect = taggedContent.createSectElement();
rootElement.appendChild(sect);

HeaderElement h1 = taggedContent.createHeaderElement(1);
sect.appendChild(h1);
h1.setText("El Encabezado");

h1.setTitle("Título");
h1.setLanguage("en-US");
h1.setAlternativeText("Texto Alternativo");
h1.setExpansionText("Texto de Expansión");
h1.setActualText("Texto Real");

// Guardar Documento PDF Etiquetado
document.save(path + "StructureElementsProperties.pdf");
```


## Configuración de Elementos de Estructura de Texto

Para establecer los elementos de estructura de texto de un documento PDF etiquetado, Aspose.PDF ofrece la clase [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement). El siguiente fragmento de código muestra cómo establecer los elementos de estructura de texto de un documento PDF etiquetado:

```java
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-Java
// La ruta al directorio de documentos.
String path = "pathTodir";

// Crear documento Pdf
Document document = new Document();

// Obtener contenido para trabajar con TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Establecer título e idioma para el documento
taggedContent.setTitle("Documento PDF Etiquetado");
taggedContent.setLanguage("en-US");

// Obtener elementos de estructura raíz
StructureElement rootElement = taggedContent.getRootElement();

ParagraphElement p = taggedContent.createParagraphElement();
// Establecer texto al elemento de estructura de texto
p.setText("Párrafo.");
rootElement.appendChild(p);

// Guardar documento PDF etiquetado
document.save(path + "TextStructureElement.pdf");
```


## Configuración de Elementos de Estructura de Bloque de Texto

Para establecer elementos de estructura de bloque de texto de un Documento PDF Etiquetado, Aspose.PDF ofrece las Clases [HeaderElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls.class-use/headerelement) y [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement). Puedes agregar objetos de estas clases como un hijo del objeto **StructureElement**. El siguiente fragmento de código muestra cómo configurar elementos de estructura de bloque de texto de un Documento PDF Etiquetado:

```java
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-Java
// La ruta al directorio de documentos.
String path = "pathTodir";

// Crear Documento Pdf
Document document = new Document();

// Obtener Contenido para trabajar con TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Establecer Título e Idioma para el Documento
taggedContent.setTitle("Documento Pdf Etiquetado");
taggedContent.setLanguage("en-US");

// Obtener Elemento de Estructura Raíz
StructureElement rootElement = taggedContent.getRootElement();

HeaderElement h1 = taggedContent.createHeaderElement(1);
HeaderElement h2 = taggedContent.createHeaderElement(2);
HeaderElement h3 = taggedContent.createHeaderElement(3);
HeaderElement h4 = taggedContent.createHeaderElement(4);
HeaderElement h5 = taggedContent.createHeaderElement(5);
HeaderElement h6 = taggedContent.createHeaderElement(6);
h1.setText("H1. Encabezado de Nivel 1");
h2.setText("H2. Encabezado de Nivel 2");
h3.setText("H3. Encabezado de Nivel 3");
h4.setText("H4. Encabezado de Nivel 4");
h5.setText("H5. Encabezado de Nivel 5");
h6.setText("H6. Encabezado de Nivel 6");
rootElement.appendChild(h1);
rootElement.appendChild(h2);
rootElement.appendChild(h3);
rootElement.appendChild(h4);
rootElement.appendChild(h5);
rootElement.appendChild(h6);

ParagraphElement p = taggedContent.createParagraphElement();
p.setText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
rootElement.appendChild(p);

// Guardar Documento Pdf Etiquetado
document.save(path + "TextBlockStructureElements.pdf");
```


## Configuración de Elementos de Estructura en Línea

Para configurar los elementos de estructura en línea de un Documento PDF con Etiquetas, Aspose.PDF ofrece las Clases [SpanElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.ils/spanelement) y [ParagraphElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.bls/class-use/ParagraphElement). Puedes agregar objetos de estas clases como un hijo del objeto **StructureElement**. El siguiente fragmento de código muestra cómo configurar elementos de estructura en línea de un Documento PDF con Etiquetas:

```java
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-Java
// La ruta al directorio de documentos.
String path = "pathTodir";
// Crear Documento Pdf
Document document = new Document();

// Obtener Contenido para trabajar con TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Establecer Título e Idioma para el Documento
taggedContent.setTitle("Documento Pdf con Etiquetas");
taggedContent.setLanguage("en-US");

// Obtener Elemento de Estructura Raíz
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
spanH12.setText("Encabezado Nivel 1");
h1.appendChild(spanH12);

SpanElement spanH21 = taggedContent.createSpanElement();
spanH21.setText("H2. ");
h2.appendChild(spanH21);
SpanElement spanH22 = taggedContent.createSpanElement();
spanH22.setText("Encabezado Nivel 2");
h2.appendChild(spanH22);

SpanElement spanH31 = taggedContent.createSpanElement();
spanH31.setText("H3. ");
h3.appendChild(spanH31);
SpanElement spanH32 = taggedContent.createSpanElement();
spanH32.setText("Encabezado Nivel 3");
h3.appendChild(spanH32);

SpanElement spanH41 = taggedContent.createSpanElement();
spanH41.setText("H4. ");
h4.appendChild(spanH41);
SpanElement spanH42 = taggedContent.createSpanElement();
spanH42.setText("Encabezado Nivel 4");
h4.appendChild(spanH42);

SpanElement spanH51 = taggedContent.createSpanElement();
spanH51.setText("H5. ");
h5.appendChild(spanH51);
SpanElement spanH52 = taggedContent.createSpanElement();
spanH52.setText("Encabezado Nivel 5");
h5.appendChild(spanH52);

SpanElement spanH61 = taggedContent.createSpanElement();
spanH61.setText("H6. ");
h6.appendChild(spanH61);
SpanElement spanH62 = taggedContent.createSpanElement();
spanH62.setText("Encabezado Nivel 6");
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

// Guardar Documento Pdf con Etiquetas
document.save(path + "InlineStructureElements.pdf");
```


## Configuración de Nombre de Etiqueta Personalizada

Con el fin de establecer un nombre de etiqueta personalizado para los elementos de un Documento PDF Etiquetado, Aspose.PDF ofrece el método **setTag()** para los elementos. El siguiente fragmento de código muestra cómo establecer un nombre de etiqueta personalizado:

```java
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-Java
// La ruta al directorio de documentos.
String path = "pathTodir";
// Crear Documento Pdf
Document document = new Document();

// Obtener Contenido para trabajar con TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Establecer Título e Idioma para el Documento
taggedContent.setTitle("Documento Pdf Etiquetado");
taggedContent.setLanguage("en-US");

// Crear Elementos de Estructura Lógica
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

// Guardar Documento Pdf Etiquetado
document.save(path + "CustomTag.pdf");
```


## Añadiendo Elemento de Estructura a Elementos

Para establecer elementos de estructura de enlace en un Documento PDF Etiquetado, Aspose.PDF ofrece el método **createLinkElement()** de la Interfaz [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). El siguiente fragmento de código muestra cómo establecer elementos de estructura en un párrafo con texto de un Documento PDF Etiquetado:

```java
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-Java
// La ruta al directorio de documentos.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "AddStructureElementIntoElement_Output.pdf";
String logFile = dataDir + "46144_log.xml";

// Creación de documento y obtención de Contenido Pdf Etiquetado
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();


// Establecer Título y Lenguaje Natural para el documento
taggedContent.setTitle("Ejemplo de Elementos de Texto");
taggedContent.setLanguage("en-US");

// Obtener elemento de estructura Raíz (elemento de estructura del Documento)
StructureElement rootElement = taggedContent.getRootElement();


ParagraphElement p1 = taggedContent.createParagraphElement();
rootElement.appendChild(p1);
SpanElement span11 = taggedContent.createSpanElement();
span11.setText("Span_11");
SpanElement span12 = taggedContent.createSpanElement();
span12.setText(" y Span_12.");
p1.setText("Párrafo con ");
p1.appendChild(span11);
p1.appendChild(span12);


ParagraphElement p2 = taggedContent.createParagraphElement();
rootElement.appendChild(p2);
SpanElement span21 = taggedContent.createSpanElement();
span21.setText("Span_21");
SpanElement span22 = taggedContent.createSpanElement();
span22.setText("Span_22.");
p2.appendChild(span21);
p2.setText(" y ");
p2.appendChild(span22);


ParagraphElement p3 = taggedContent.createParagraphElement();
rootElement.appendChild(p3);
SpanElement span31 = taggedContent.createSpanElement();
span31.setText("Span_31");
SpanElement span32 = taggedContent.createSpanElement();
span32.setText(" y Span_32");
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
span421.setText("Span 421 y ");
span42.appendChild(span421);
span42.setText("Span_42");
p4.appendChild(span41);
p4.appendChild(span42);
p4.setText(".");


// Guardar Documento Pdf Etiquetado
document.save(outFile);
```


## Configuración del Elemento de Estructura de Nota

Aspose.PDF para Java API también permite agregar un **NoteElement** en un documento PDF etiquetado. El siguiente fragmento de código muestra cómo agregar un elemento de nota en un documento PDF etiquetado:

```java
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-Java
// La ruta al directorio de documentos.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
String outFile = dataDir + "CreateNoteStructureElement.pdf";
String logFile = dataDir + "45929_log.xml";

// Crear Documento Pdf
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("Ejemplo de Elementos de Nota");
taggedContent.setLanguage("en-US");

// Agregar Elemento de Párrafo
ParagraphElement paragraph = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(paragraph);

// Agregar NoteElement
NoteElement note1 = taggedContent.createNoteElement();
paragraph.appendChild(note1);
note1.setText("Nota con ID generado automáticamente. ");

// Agregar NoteElement
NoteElement note2 = taggedContent.createNoteElement();
paragraph.appendChild(note2);
note2.setText("Nota con ID = 'note_002'. ");
note2.setId("note_002");

// Agregar NoteElement
NoteElement note3 = taggedContent.createNoteElement();
paragraph.appendChild(note3);
note3.setText("Nota con ID = 'note_003'. ");
note3.setId("note_003");
// Guardar Documento Pdf Etiquetado
document.save(outFile);
```