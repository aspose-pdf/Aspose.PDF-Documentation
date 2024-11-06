---
title: Extraer Contenido Etiquetado de PDF 
linktitle: Extraer Contenido Etiquetado
type: docs
weight: 20
url: es/java/extract-tagged-content-from-tagged-pdfs/
description: Este artículo explica cómo extraer contenido etiquetado de un documento PDF usando Aspose.PDF para Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtener Contenido de PDF Etiquetado

Para obtener el contenido de un Documento PDF con Texto Etiquetado, Aspose.PDF ofrece el método [getTaggedContent()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getTaggedContent--) de la Clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). El siguiente fragmento de código muestra cómo obtener el contenido de un documento PDF con Texto Etiquetado:

```java
// Para ejemplos completos y archivos de datos, por favor vaya a https://github.com/aspose-pdf/Aspose.PDF-for-Java
// La ruta al directorio de documentos.
String path = "pathTodir";

// Crear Documento Pdf
Document document = new Document();

// Obtener Contenido para trabajar con TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

//
// Trabajar con contenido de Pdf Etiquetado
//

// Establecer Título e Idioma para el Documento
taggedContent.setTitle("Documento Pdf Etiquetado Simple");
taggedContent.setLanguage("en-US");

// Guardar Documento Pdf Etiquetado
document.save(path + "TaggedPDFContent.pdf");
```


## Obtener la Estructura Raíz

Para obtener la estructura raíz de un Documento PDF Etiquetado, Aspose.PDF ofrece los métodos [getStructTreeRootElement]()(https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent#getStructTreeRootElement--) y **getStructureElement()** de la Interfaz [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.tagged/ITaggedContent). El siguiente fragmento de código muestra cómo obtener la estructura raíz de un Documento PDF Etiquetado:

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

// Las propiedades StructTreeRootElement y RootElement se utilizan para acceder a
// el objeto StructTreeRoot del documento pdf y al elemento de estructura raíz (elemento de estructura del Documento).
StructTreeRootElement structTreeRootElement = taggedContent.getStructTreeRootElement();
StructureElement rootElement = taggedContent.getRootElement();
```


## Acceso a Elementos Hijos

Para acceder a los elementos hijos de un Documento PDF Etiquetado, Aspose.PDF ofrece la Clase **ElementList**. El siguiente fragmento de código muestra cómo acceder a los elementos hijos de un Documento PDF Etiquetado:

```java
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-Java
String path = "pathTodir";
// Abrir Documento Pdf
Document document = new Document( path +"StructureElements.pdf");

// Obtener contenido para trabajar con TaggedPdf
ITaggedContent taggedContent = document.getTaggedContent();

// Acceder al(los) elemento(s) raíz
ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement =  (StructureElement)element;

        // Obtener propiedades
        String title = structureElement.getTitle();
        String language = structureElement.getLanguage();
        String actualText = structureElement.getActualText();
        String expansionText = structureElement.getExpansionText();
        String alternativeText = structureElement.getAlternativeText();
    }
}

// Acceder a los elementos hijos del primer elemento en el elemento raíz
elementList = taggedContent.getRootElement().getChildElements().get_Item(1).getChildElements();
for (Element element : elementList)
{
    if (element instanceof StructureElement)
    {
        StructureElement structureElement = (StructureElement)element;

        // Establecer propiedades
        structureElement.setTitle("título");
        structureElement.setLanguage("fr-FR");
        structureElement.setActualText("texto real");
        structureElement.setExpansionText("exp");
        structureElement.setAlternativeText("alt");
    }
}

// Guardar Documento Pdf Etiquetado
document.save( path +"AccessChildrenElements.pdf");
```