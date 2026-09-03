---
title: Extraiga contenido etiquetado de archivos PDF en Java
linktitle: Extraer contenido etiquetado
type: docs
weight: 20
url: /java/extract-tagged-content-from-tagged-pdfs/
description: Aprenda a inspeccionar contenido PDF etiquetado en Java con Aspose.PDF, incluido el acceso al contenido etiquetado, el acceso a la estructura raíz y los elementos de la estructura secundaria.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Utilice estas API cuando necesite inspeccionar el árbol de estructura lógica de un PDF etiquetado y examinar o actualizar los metadatos del elemento de estructura.


## 
Obtener metadatos de contenido etiquetado

Utilice este ejemplo cuando necesite acceder al contenedor de contenido etiquetado y desee definir metadatos básicos del documento, como el título y el idioma.


1. Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Obtenga el objeto [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/) del documento.

1. Configure los metadatos del contenido etiquetado y guarde el archivo de salida.


```java
public static void getTaggedContent(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Simple Tagged Pdf Document");
        taggedContent.setLanguage("en-US");
        document.save(outputFile.toString());
    }
}
```

## 
Obtenga la estructura raíz de un PDF etiquetado

Este ejemplo muestra cómo inspeccionar los objetos raíz que representan el árbol de estructura de un PDF etiquetado.


1. Cree un nuevo [Documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y obtenga su contenido etiquetado.

1. Establezca los metadatos del documento requeridos.

1. Lea e imprima la raíz del árbol de estructura y el elemento de raíz lógica, luego guarde el archivo.


```java
public static void getRootStructure(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        System.out.println("StructTreeRootElement: " + taggedContent.getStructTreeRootElement());
        System.out.println("RootElement: " + taggedContent.getRootElement());

        document.save(outputFile.toString());
    }
}
```

## 
Acceder y actualizar elementos de la estructura secundaria.

Utilice este ejemplo cuando necesite recorrer elementos secundarios en el árbol de estructura, inspeccionar sus propiedades y actualizar los metadatos seleccionados.


1. Abra la fuente etiquetada PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. Lea los elementos secundarios de la raíz del árbol de estructura e imprima las propiedades disponibles.

1. Acceda a los elementos secundarios del primer hijo raíz, actualice sus metadatos y guarde el documento.

```java
public static void accessChildElements(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ITaggedContent taggedContent = document.getTaggedContent();

        ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
        for (Object element : elementList) {
            if (element instanceof StructureElement structureElement) {
                System.out.println("StructureElement properties - "
                        + "title: " + structureElement.getTitle()
                        + ", language: " + structureElement.getLanguage()
                        + ", actual_text: " + structureElement.getActualText()
                        + ", expansion_text: " + structureElement.getExpansionText()
                        + ", alternative_text: " + structureElement.getAlternativeText());
            }
        }

        Element firstChild = taggedContent.getRootElement().getChildElements().get_Item(1);
        for (Object element : firstChild.getChildElements()) {
            if (element instanceof StructureElement structureElement) {
                structureElement.setTitle("title");
                structureElement.setLanguage("fr-FR");
                structureElement.setActualText("actual text");
                structureElement.setExpansionText("exp");
                structureElement.setAlternativeText("alt");
            }
        }

        document.save(outputFile.toString());
    }
}
```
