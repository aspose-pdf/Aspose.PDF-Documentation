---
title: Crear PDF Etiquetado 
linktitle: Crear PDF Etiquetado 
type: docs
weight: 10
lastmod: "2021-06-05"
url: /java/create-tagged-pdf-documents/
description: Este artículo explica cómo crear elementos de estructura para un documento PDF etiquetado programáticamente utilizando Aspose.PDF para Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Creación de Elementos de Estructura

Para crear elementos de estructura en un Documento PDF Etiquetado, Aspose.PDF ofrece métodos para crear elementos de estructura utilizando la Interfaz [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). El siguiente fragmento de código muestra cómo crear elementos de estructura de un PDF Etiquetado:

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

// Crear Elementos de Agrupación
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

// Crear Elementos de Estructura de Texto a Nivel de Bloque
ParagraphElement paragraphElement = taggedContent.createParagraphElement();
HeaderElement headerElement = taggedContent.createHeaderElement();
HeaderElement h1Element = taggedContent.createHeaderElement(1);

// Crear Elementos de Estructura de Texto a Nivel Inline
SpanElement spanElement = taggedContent.createSpanElement();
QuoteElement quoteElement = taggedContent.createQuoteElement();
NoteElement noteElement = taggedContent.createNoteElement();

// Crear Elementos de Estructura de Ilustración
FigureElement figureElement = taggedContent.createFigureElement();
FormulaElement formulaElement = taggedContent.createFormulaElement();

// Métodos están en desarrollo
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

// Guardar Documento Pdf Etiquetado
document.save(path + "StructureElements.pdf");
```


## Creación del Árbol de Elementos de Estructura

Para crear un árbol de elementos de estructura en un Documento PDF Etiquetado, Aspose.PDF ofrece métodos para crear un árbol de elementos de estructura utilizando la Interfaz [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). El siguiente fragmento de código muestra cómo crear un árbol de elementos de estructura de un Documento PDF Etiquetado:

```java
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-Java
// La ruta al directorio de documentos.
String path = "pathTodir";
// Crear Documento Pdf
Document document = new Document();

// Obtener contenido para trabajar con TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Establecer título e idioma para el documento
taggedContent.setTitle("Documento Pdf Etiquetado");
taggedContent.setLanguage("en-US");

// Obtener elemento de estructura raíz (Documento)
StructureElement rootElement = taggedContent.getRootElement();

// Crear Estructura Lógica
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

// Guardar Documento Pdf Etiquetado
document.save(path + "StructureElementsTree.pdf");
```


## Estructura de Estilo de Texto

Para estilizar la estructura de texto en un Documento PDF Etiquetado, Aspose.PDF ofrece las propiedades **setFont()**, **setFontSize()**, **setFontStyle()** y **setForegroundColor()** de la Clase [StructureTextState](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/StructureTextState). El siguiente fragmento de código muestra cómo estilizar la estructura de texto en un Documento PDF Etiquetado:

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

ParagraphElement p = taggedContent.createParagraphElement();
taggedContent.getRootElement().appendChild(p);

// En Desarrollo
p.getStructureTextState().setFontSize(18F);
p.getStructureTextState().setForegroundColor(Color.getRed());
p.getStructureTextState().setFontStyle(FontStyles.Italic);

p.setText("Texto en cursiva rojo.");

// Guardar Documento Pdf Etiquetado
document.save(path + "StyleTextStructure.pdf");
```


## Ilustrando Elementos de Estructura

Para ilustrar elementos de estructura en un Documento PDF Etiquetado, Aspose.PDF ofrece la Clase [IllustrationElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged.logicalstructure.elements.class-use/IllustrationElement). El siguiente fragmento de código muestra cómo ilustrar elementos de estructura en un Documento PDF Etiquetado:

```java
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-Java
// La ruta al directorio de documentos.
String path = "pathTodir";
// Crear Documento Pdf
Document document = new Document();

// Obtener Contenido para trabajar con TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Establecer Título e Idioma para el Documento
taggedContent.setTitle("Documento Pdf Etiquetado");
taggedContent.setLanguage("en-US");

// En Desarrollo
IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setActualText("Figura Uno");
figure1.setTitle("Imagen 1");
figure1.setTag("Fig1");
figure1.setImage("image.png");

// Guardar Documento Pdf Etiquetado
document.save(path + "IllustrationStructureElements.pdf");
```


## **Crear PDF con Imagen Etiquetada**

Para crear un PDF con Imagen Etiquetada, Aspose.PDF ofrece el método [createFigureElement()](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#createFigureElement--) de la Interfaz [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). El siguiente fragmento de código muestra la funcionalidad.

```java
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-Java
Document document = new Document();
ITaggedContent taggedContent = document.getTaggedContent();

taggedContent.setTitle("CreatePDFwithTaggedImage");
taggedContent.setLanguage("en-US");

IllustrationElement figure1 = taggedContent.createFigureElement();
taggedContent.getRootElement().appendChild(figure1);
figure1.setAlternativeText("Logo de Aspose");
figure1.setTitle("Imagen 1");
figure1.setTag("Fig");
// Añadir imagen con resolución de 300 DPI (por defecto)
figure1.setImage("aspose-logo.jpg");
// Guardar Documento PDF
document.save("PDFwithTaggedImage.pdf");
```


## Crear PDF con Texto Etiquetado

Para crear un PDF con Texto Etiquetado, Aspose.PDF ofrece la [Interfaz ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). El siguiente fragmento de código muestra la funcionalidad.

```java
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-Java
// La ruta al directorio de documentos.
String dataDir = Utils.getDataDir() + "TaggedPDFs\\";
// Crear Documento Pdf
Document document = new Document();

// Obtener Contenido para trabajar con TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Establecer Título e Idioma para el Documento
taggedContent.setTitle("Documento Pdf Etiquetado");
taggedContent.setLanguage("en-US");

// Crear Elementos de Estructura a Nivel de Bloque de Texto
HeaderElement headerElement = taggedContent.createHeaderElement();
headerElement.setActualText("Encabezado 1");
ParagraphElement paragraphElement1 = taggedContent.createParagraphElement();
paragraphElement1.setActualText("prueba 1");
ParagraphElement paragraphElement2 = taggedContent.createParagraphElement();
paragraphElement2.setActualText("prueba 2");
ParagraphElement paragraphElement3 = taggedContent.createParagraphElement();
paragraphElement3.setActualText("prueba 3");
ParagraphElement paragraphElement4 = taggedContent.createParagraphElement();
paragraphElement4.setActualText("prueba 4");
ParagraphElement paragraphElement5 = taggedContent.createParagraphElement();
paragraphElement5.setActualText("prueba 5");
ParagraphElement paragraphElement6 = taggedContent.createParagraphElement();
paragraphElement6.setActualText("prueba 6");
ParagraphElement paragraphElement7 = taggedContent.createParagraphElement();
paragraphElement7.setActualText("prueba 7");

// Guardar Documento PDF
document.save(dataDir + "PDFconTextoEtiquetado.pdf");
```