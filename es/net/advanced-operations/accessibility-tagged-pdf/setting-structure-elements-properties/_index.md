---
title: Configuración de Propiedades de Elementos de Estructura
linktitle: Configuración de Propiedades de Elementos de Estructura
type: docs
weight: 30
url: /es/net/setting-structure-elements-properties/
description: Puede configurar diferentes propiedades de los elementos de estructura en un documento PDF con Aspose.PDF para .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Configuración de Propiedades de Elementos de Estructura",
    "alternativeHeadline": "Cómo configurar las propiedades de los elementos estructurales",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "generación de documentos PDF",
    "keywords": "pdf, c#, configurar estructura de texto, configurar idioma, configurar título, configurar elemento de estructura de nota",
    "wordcount": "302",
    "proficiencyLevel":"Principiante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipo de Documentación de Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/setting-structure-elements-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/setting-structure-elements-properties/"
    },
    "dateModified": "2022-02-04",
    "description": "Puede configurar diferentes propiedades de los elementos de estructura en un documento PDF con Aspose.PDF para .NET."
}
</script>
Para establecer las propiedades de los elementos de estructura en un Documento PDF Etiquetado, Aspose.PDF ofrece los métodos [CreateSectElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createsectelement) y [CreateHeaderElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createheaderelement/index) de la interfaz [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent).

El siguiente fragmento de código muestra cómo establecer las propiedades de los elementos de estructura de un Documento PDF Etiquetado:

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Crear Documento Pdf
Document document = new Document();

// Obtener Contenido para trabajar con TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Establecer Título e Idioma para el Documento
taggedContent.SetTitle("Documento PDF Etiquetado");
taggedContent.SetLanguage("en-US");

// Crear Elementos de Estructura
StructureElement rootElement = taggedContent.RootElement;

SectElement sect = taggedContent.CreateSectElement();
rootElement.AppendChild(sect);

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
sect.AppendChild(h1);
h1.SetText("El Encabezado");

h1.Title = "Título";
h1.Language = "en-US";
h1.AlternativeText = "Texto Alternativo";
h1.ExpansionText = "Texto de Expansión";
h1.ActualText = "Texto Actual";

// Guardar Documento PDF Etiquetado
document.Save(dataDir + "StructureElementsProperties.pdf");
```
## Configuración de Elementos de Estructura de Texto

Para configurar los elementos de estructura de texto de un Documento PDF Etiquetado, Aspose.PDF ofrece la clase [ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement). El siguiente fragmento de código muestra cómo configurar los elementos de estructura de texto de un Documento PDF Etiquetado:

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Crear Documento Pdf
Document document = new Document();

// Obtener Contenido para trabajar con TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Establecer Título e Idioma para el Documento
taggedContent.SetTitle("Documento PDF Etiquetado");
taggedContent.SetLanguage("en-US");

// Obtener Elementos de Estructura Raíz
StructureElement rootElement = taggedContent.RootElement;

ParagraphElement p = taggedContent.CreateParagraphElement();
// Establecer Texto al Elemento de Estructura de Texto
p.SetText("Párrafo.");
rootElement.AppendChild(p);


// Guardar Documento PDF Etiquetado
document.Save(dataDir + "TextStructureElement.pdf");
```
## Establecer Elementos de Estructura de Bloque de Texto

Para establecer elementos de estructura de bloque de texto de un Documento PDF Etiquetado, Aspose.PDF ofrece las clases [HeaderElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/headerelement) y [ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement). Puedes añadir objetos de estas clases como hijo de un objeto [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement).
El siguiente fragmento de código muestra cómo establecer elementos de estructura de bloque de texto de un Documento PDF Etiquetado:

```csharp
// Para ejemplos completos y archivos de datos, por favor visita https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Crear Documento PDF
Document document = new Document();

// Obtener Contenido para trabajar con TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Establecer Título e Idioma para el Documento
taggedContent.SetTitle("Documento PDF Etiquetado");
taggedContent.SetLanguage("en-US");

// Obtener Elemento de Estructura Raíz
StructureElement rootElement = taggedContent.RootElement;

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
HeaderElement h2 = taggedContent.CreateHeaderElement(2);
HeaderElement h3 = taggedContent.CreateHeaderElement(3);
HeaderElement h4 = taggedContent.CreateHeaderElement(4);
HeaderElement h5 = taggedContent.CreateHeaderElement(5);
HeaderElement h6 = taggedContent.CreateHeaderElement(6);
h1.SetText("H1. Encabezado de Nivel 1");
h2.SetText("H2. Encabezado de Nivel 2");
h3.SetText("H3. Encabezado de Nivel 3");
h4.SetText("H4. Encabezado de Nivel 4");
h5.SetText("H5. Encabezado de Nivel 5");
h6.SetText("H6. Encabezado de Nivel 6");
rootElement.AppendChild(h1);
rootElement.AppendChild(h2);
rootElement.AppendChild(h3);
rootElement.AppendChild(h4);
rootElement.AppendChild(h5);
rootElement.AppendChild(h6);

ParagraphElement p = taggedContent.CreateParagraphElement();
p.SetText("P. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean nec lectus ac sem faucibus imperdiet. Sed ut erat ac magna ullamcorper hendrerit. Cras pellentesque libero semper, gravida magna sed, luctus leo. Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
rootElement.AppendChild(p);

// Guardar Documento PDF Etiquetado
document.Save(dataDir + "TextBlockStructureElements.pdf");
```
## Establecimiento de Elementos de Estructura en Línea

Para establecer elementos de estructura en línea de un Documento PDF Etiquetado, Aspose.PDF ofrece las clases [SpanElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/spanelement) y [ParagraphElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/paragraphelement). Puedes añadir objetos de estas clases como hijo de un objeto [StructureElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement). El siguiente fragmento de código muestra cómo establecer elementos de estructura en línea de un Documento PDF Etiquetado:

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Crear Documento Pdf
Document document = new Document();

// Obtener Contenido para trabajar con TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Establecer Título e Idioma para el Documento
taggedContent.SetTitle("Documento PDF Etiquetado");
taggedContent.SetLanguage("en-US");

// Obtener Elemento de Estructura Raíz
StructureElement rootElement = taggedContent.RootElement;

HeaderElement h1 = taggedContent.CreateHeaderElement(1);
HeaderElement h2 = taggedContent.CreateHeaderElement(2);
HeaderElement h3 = taggedContent.CreateHeaderElement(3);
HeaderElement h4 = taggedContent.CreateHeaderElement(4);
HeaderElement h5 = taggedContent.CreateHeaderElement(5);
HeaderElement h6 = taggedContent.CreateHeaderElement(6);
rootElement.AppendChild(h1);
rootElement.AppendChild(h2);
rootElement.AppendChild(h3);
rootElement.AppendChild(h4);
rootElement.AppendChild(h5);
rootElement.AppendChild(h6);

SpanElement spanH11 = taggedContent.CreateSpanElement();
spanH11.SetText("H1. ");
h1.AppendChild(spanH11);
SpanElement spanH12 = taggedContent.CreateSpanElement();
spanH12.SetText("Encabezado Nivel 1");
h1.AppendChild(spanH12);

SpanElement spanH21 = taggedContent.CreateSpanElement();
spanH21.SetText("H2. ");
h2.AppendChild(spanH21);
SpanElement spanH22 = taggedContent.CreateSpanElement();
spanH22.SetText("Encabezado Nivel 2");
h2.AppendChild(spanH22);

SpanElement spanH31 = taggedContent.CreateSpanElement();
spanH31.SetText("H3. ");
h3.AppendChild(spanH31);
SpanElement spanH32 = taggedContent.CreateSpanElement();
spanH32.SetText("Encabezado Nivel 3");
h3.AppendChild(spanH32);

SpanElement spanH41 = taggedContent.CreateSpanElement();
spanH41.SetText("H4. ");
h4.AppendChild(spanH41);
SpanElement spanH42 = taggedContent.CreateSpanElement();
spanH42.SetText("Encabezado Nivel 4");
h4.AppendChild(spanH42);

SpanElement spanH51 = taggedContent.CreateSpanElement();
spanH51.SetText("H5. ");
h5.AppendChild(spanH51);
SpanElement spanH52 = taggedContent.CreateSpanElement();
spanH52.SetText("Encabezado Nivel 5");
h5.AppendChild(spanH52);

SpanElement spanH61 = taggedContent.CreateSpanElement();
spanH61.SetText("H6. ");
h6.AppendChild(spanH61);
SpanElement spanH62 = taggedContent.CreateSpanElement();
spanH62.SetText("Encabezado Nivel 6");
h6.AppendChild(spanH62);

ParagraphElement p = taggedContent.CreateParagraphElement();
p.SetText("P. ");
rootElement.AppendChild(p);
SpanElement span1 = taggedContent.CreateSpanElement();
span1.SetText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. ");
p.AppendChild(span1);
SpanElement span2 = taggedContent.CreateSpanElement();
span2.SetText("Aenean nec lectus ac sem faucibus imperdiet. ");
p.AppendChild(span2);
SpanElement span3 = taggedContent.CreateSpanElement();
span3.SetText("Sed ut erat ac magna ullamcorper hendrerit. ");
p.AppendChild(span3);
SpanElement span4 = taggedContent.CreateSpanElement();
span4.SetText("Cras pellentesque libero semper, gravida magna sed, luctus leo. ");
p.AppendChild(span4);
SpanElement span5 = taggedContent.CreateSpanElement();
span5.SetText("Fusce lectus odio, laoreet nec ullamcorper ut, molestie eu elit. ");
p.AppendChild(span5);
SpanElement span6 = taggedContent.CreateSpanElement();
span6.SetText("Interdum et malesuada fames ac ante ipsum primis in faucibus. ");
p.AppendChild(span6);
SpanElement span7 = taggedContent.CreateSpanElement();
span7.SetText("Aliquam lacinia sit amet elit ac consectetur. Donec cursus condimentum ligula, vitae volutpat sem tristique eget. ");
p.AppendChild(span7);
SpanElement span8 = taggedContent.CreateSpanElement();
span8.SetText("Nulla in consectetur massa. Vestibulum vitae lobortis ante. Nulla ullamcorper pellentesque justo rhoncus accumsan. ");
p.AppendChild(span8);
SpanElement span9 = taggedContent.CreateSpanElement();
span9.SetText("Mauris ornare eu odio non lacinia. Aliquam massa leo, rhoncus ac iaculis eget, tempus et magna. Sed non consectetur elit. ");
p.AppendChild(span9);
SpanElement span10 = taggedContent.CreateSpanElement();
span10.SetText("Sed vulputate, quam sed lacinia luctus, ipsum nibh fringilla purus, vitae posuere risus odio id massa. Cras sed venenatis lacus.");
p.AppendChild(span10);

// Guardar Documento PDF Etiquetado
document.Save(dataDir + "InlineStructureElements.pdf");
```
## Configuración del Nombre de Etiqueta Personalizado

Para configurar el nombre de etiqueta personalizado de los elementos de un Documento PDF Etiquetado, Aspose.PDF ofrece el método [SetTag](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/structureelement/methods/settag) de la clase StructureElement para los elementos. El siguiente fragmento de código muestra cómo configurar un nombre de etiqueta personalizado:

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Crear Documento Pdf
Document document = new Document();

// Obtener Contenido para trabajar con TaggedPdf
ITaggedContent taggedContent = document.TaggedContent;

// Establecer Título e Idioma para el Documento
taggedContent.SetTitle("Documento Pdf Etiquetado");
taggedContent.SetLanguage("en-US");

// Crear Elementos de Estructura Lógica
SectElement sect = taggedContent.CreateSectElement();
taggedContent.RootElement.AppendChild(sect);

ParagraphElement p1 = taggedContent.CreateParagraphElement();
ParagraphElement p2 = taggedContent.CreateParagraphElement();
ParagraphElement p3 = taggedContent.CreateParagraphElement();
ParagraphElement p4 = taggedContent.CreateParagraphElement();

p1.SetText("P1. ");
p2.SetText("P2. ");
p3.SetText("P3. ");
p4.SetText("P4. ");

p1.SetTag("P1");
p2.SetTag("Para");
p3.SetTag("Para");
p4.SetTag("Paragraph");

sect.AppendChild(p1);
sect.AppendChild(p2);
sect.AppendChild(p3);
sect.AppendChild(p4);

SpanElement span1 = taggedContent.CreateSpanElement();
SpanElement span2 = taggedContent.CreateSpanElement();
SpanElement span3 = taggedContent.CreateSpanElement();
SpanElement span4 = taggedContent.CreateSpanElement();

span1.SetText("Span 1.");
span2.SetText("Span 2.");
span3.SetText("Span 3.");
span4.SetText("Span 4.");

span1.SetTag("SPAN");
span2.SetTag("Sp");
span3.SetTag("Sp");
span4.SetTag("TheSpan");

p1.AppendChild(span1);
p2.AppendChild(span2);
p3.AppendChild(span3);
p4.AppendChild(span4);

// Guardar Documento Pdf Etiquetado
document.Save(dataDir + "CustomTag.pdf");
```
## Agregar Elemento Estructural en Elementos

**Esta característica es soportada por la versión 19.4 o superior.**

Para establecer elementos estructurales de enlace en un Documento PDF etiquetado, Aspose.PDF ofrece el método [CreateLinkElement](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent/methods/createlinkelement) de la interfaz [ITaggedContent](https://reference.aspose.com/pdf/net/aspose.pdf.tagged/itaggedcontent). El siguiente fragmento de código muestra cómo establecer elementos estructurales en párrafo con texto de Documento PDF Etiquetado:

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "LinkStructureElements_Output.pdf";
string logFile = dataDir + "46035_log.xml";
string imgFile = dataDir + "google-icon-512.png";

// Creación del documento y obtención del Contenido PDF Etiquetado
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;


// Establecimiento del Título y Lenguaje Natural para el documento
taggedContent.SetTitle("Ejemplo de Elementos de Enlace");
taggedContent.SetLanguage("en-US");

// Obtención del elemento estructural raíz (elemento estructural del documento)
StructureElement rootElement = taggedContent.RootElement;


ParagraphElement p1 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p1);
LinkElement link1 = taggedContent.CreateLinkElement();
p1.AppendChild(link1);
link1.Hyperlink = new WebHyperlink("http://google.com");
link1.SetText("Google");
link1.AlternateDescriptions = "Enlace a Google";


ParagraphElement p2 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p2);
LinkElement link2 = taggedContent.CreateLinkElement();
p2.AppendChild(link2);
link2.Hyperlink = new WebHyperlink("http://google.com");
SpanElement span2 = taggedContent.CreateSpanElement();
span2.SetText("Google");
link2.AppendChild(span2);
link2.AlternateDescriptions = "Enlace a Google";


ParagraphElement p3 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p3);
LinkElement link3 = taggedContent.CreateLinkElement();
p3.AppendChild(link3);
link3.Hyperlink = new WebHyperlink("http://google.com");
SpanElement span31 = taggedContent.CreateSpanElement();
span31.SetText("G");
SpanElement span32 = taggedContent.CreateSpanElement();
span32.SetText("oogle");
link3.AppendChild(span31);
link3.SetText("-");
link3.AppendChild(span32);
link3.AlternateDescriptions = "Enlace a Google";


ParagraphElement p4 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p4);
LinkElement link4 = taggedContent.CreateLinkElement();
p4.AppendChild(link4);
link4.Hyperlink = new WebHyperlink("http://google.com");
link4.SetText("El enlace multilínea: Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google Google");
link4.AlternateDescriptions = "Enlace a Google (multilínea)";


ParagraphElement p5 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p5);
LinkElement link5 = taggedContent.CreateLinkElement();
p5.AppendChild(link5);
link5.Hyperlink = new WebHyperlink("http://google.com");
FigureElement figure5 = taggedContent.CreateFigureElement();
figure5.SetImage(imgFile, 1200);
figure5.AlternativeText = "Icono de Google";
StructureAttributes linkLayoutAttributes = link5.Attributes.GetAttributes(AttributeOwnerStandard.Layout);
StructureAttribute placementAttribute = new StructureAttribute(AttributeKey.Placement);
placementAttribute.SetNameValue(AttributeName.Placement_Block);
linkLayoutAttributes.SetAttribute(placementAttribute);
link5.AppendChild(figure5);
link5.AlternateDescriptions = "Enlace a Google";


// Guardar el Documento PDF Etiquetado
document.Save(outFile);

// Comprobación de la conformidad PDF/UA
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Conformidad PDF/UA: {0}", isPdfUaCompliance));
```

## Establecimiento de Elemento de Estructura de Enlace

**Esta característica está soportada por la versión 19.4 o superior.**

Aspose.PDF para la API de .NET también permite agregar elementos de estructura de enlace. El siguiente fragmento de código muestra cómo agregar un elemento de estructura de enlace en un Documento PDF Etiquetado:

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "AddStructureElementIntoElement_Output.pdf";
string logFile = dataDir + "46144_log.xml";

// Creación del documento y obtención de Contenido PDF Etiquetado
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;


// Estableciendo Título e Idioma Natural para el documento
taggedContent.SetTitle("Ejemplo de Elementos de Texto");
taggedContent.SetLanguage("en-US");

// Obteniendo el elemento de estructura raíz (elemento de estructura del documento)
StructureElement rootElement = taggedContent.RootElement;


ParagraphElement p1 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p1);
SpanElement span11 = taggedContent.CreateSpanElement();
span11.SetText("Span_11");
SpanElement span12 = taggedContent.CreateSpanElement();
span12.SetText(" y Span_12.");
p1.SetText("Párrafo con ");
p1.AppendChild(span11);
p1.AppendChild(span12);


ParagraphElement p2 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p2);
SpanElement span21 = taggedContent.CreateSpanElement();
span21.SetText("Span_21");
SpanElement span22 = taggedContent.CreateSpanElement();
span22.SetText("Span_22.");
p2.AppendChild(span21);
p2.SetText(" y ");
p2.AppendChild(span22);


ParagraphElement p3 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p3);
SpanElement span31 = taggedContent.CreateSpanElement();
span31.SetText("Span_31");
SpanElement span32 = taggedContent.CreateSpanElement();
span32.SetText(" y Span_32");
p3.AppendChild(span31);
p3.AppendChild(span32);
p3.SetText(".");


ParagraphElement p4 = taggedContent.CreateParagraphElement();
rootElement.AppendChild(p4);
SpanElement span41 = taggedContent.CreateSpanElement();
SpanElement span411 = taggedContent.CreateSpanElement();
span411.SetText("Span_411, ");
span41.SetText("Span_41, ");
span41.AppendChild(span411);
SpanElement span42 = taggedContent.CreateSpanElement();
SpanElement span421 = taggedContent.CreateSpanElement();
span421.SetText("Span 421 y ");
span42.AppendChild(span421);
span42.SetText("Span_42");
p4.AppendChild(span41);
p4.AppendChild(span42);
p4.SetText(".");


// Guardar Documento PDF Etiquetado
document.Save(outFile);

// Verificación de cumplimiento PDF/UA
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Cumplimiento PDF/UA: {0}", isPdfUaCompliance));
```
## Estableciendo Elemento de Estructura de Nota

Aspose.PDF para API .NET también permite agregar [NoteElement](https://reference.aspose.com/pdf/net/aspose.pdf.logicalstructure/noteelement) en un documento PDF etiquetado. El siguiente fragmento de código muestra cómo agregar un elemento de nota en un Documento PDF Etiquetado:

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
string outFile = dataDir + "45929_doc.pdf";
string logFile = dataDir + "45929_log.xml";

// Crear Documento PDF
Document document = new Document();
ITaggedContent taggedContent = document.TaggedContent;

taggedContent.SetTitle("Ejemplo de Elementos de Nota");
taggedContent.SetLanguage("en-US");

// Agregar Elemento de Párrafo
ParagraphElement paragraph = taggedContent.CreateParagraphElement();
taggedContent.RootElement.AppendChild(paragraph);

// Agregar NoteElement
NoteElement note1 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note1);
note1.SetText("Nota con ID autogenerado. ");

// Agregar NoteElement
NoteElement note2 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note2);
note2.SetText("Nota con ID = 'note_002'. ");
note2.SetId("note_002");

// Agregar NoteElement
NoteElement note3 = taggedContent.CreateNoteElement();
paragraph.AppendChild(note3);
note3.SetText("Nota con ID = 'note_003'. ");
note3.SetId("note_003");

// Debe lanzar excepción - Aspose.Pdf.Tagged.TaggedException : Elemento de estructura con ID='note_002' ya existe
//note3.SetId("note_002");

// El documento resultante no cumple con PDF/UA si se usa ClearId() para el Elemento de Estructura de Nota
//note3.ClearId();


// Guardar Documento PDF Etiquetado
document.Save(outFile);

// Verificando cumplimiento PDF/UA
document = new Document(outFile);
bool isPdfUaCompliance = document.Validate(logFile, PdfFormat.PDF_UA_1);
Console.WriteLine(String.Format("Cumplimiento PDF/UA: {0}", isPdfUaCompliance));
```
## Configuración de Idioma y Título

**Esta característica es compatible con la versión 19.6 o superior.**

Aspose.PDF para la API .NET también le permite configurar el idioma y el título de un documento según la especificación PDF/UA. El idioma se puede configurar tanto para todo el documento como para sus elementos estructurales separados. El siguiente fragmento de código muestra cómo configurar el idioma y el título en un Documento PDF etiquetado:

```csharp
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
Document document = new Document();
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

// Obtener ContenidoEtiquetado
Tagged.ITaggedContent taggedContent = document.TaggedContent;

// Establecer Título e Idioma
taggedContent.SetTitle("Documento Etiquetado de Ejemplo");
taggedContent.SetLanguage("en-US");

// Encabezado (en-US, heredado del documento)
LogicalStructure.HeaderElement h1 = taggedContent.CreateHeaderElement(1);
h1.SetText("Frase en diferentes idiomas");
taggedContent.RootElement.AppendChild(h1);

// Párrafo (Inglés)
LogicalStructure.ParagraphElement pEN = taggedContent.CreateParagraphElement();
pEN.SetText("Hello, World!");
pEN.Language = "en-US";
taggedContent.RootElement.AppendChild(pEN);

// Párrafo (Alemán)
LogicalStructure.ParagraphElement pDE = taggedContent.CreateParagraphElement();
pDE.SetText("Hallo Welt!");
pDE.Language = "de-DE";
taggedContent.RootElement.AppendChild(pDE);

// Párrafo (Francés)
LogicalStructure.ParagraphElement pFR = taggedContent.CreateParagraphElement();
pFR.SetText("Bonjour le monde!");
pFR.Language = "fr-FR";
taggedContent.RootElement.AppendChild(pFR);

// Párrafo (Español)
LogicalStructure.ParagraphElement pSP = taggedContent.CreateParagraphElement();
pSP.SetText("¡Hola Mundo!");
pSP.Language = "es-ES";
taggedContent.RootElement.AppendChild(pSP);

// Guardar Documento PDF Etiquetado
document.Save(dataDir + "SetupLanguageAndTitle.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Biblioteca Aspose.PDF para .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "ventas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "ventas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "ventas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de manipulación de PDF para .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
```

