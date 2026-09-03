---
title: Extraer contenido etiquetado de PDFs en Java
linktitle: Extraer contenido etiquetado
type: docs
weight: 20
url: /es/java/extract-tagged-content-from-tagged-pdfs/
description: Aprenda cómo inspeccionar el contenido de PDF etiquetado en Java con Aspose.PDF, incluyendo el acceso al contenido etiquetado, el acceso a la estructura raíz y los elementos de estructura hijos.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Utilice estas API cuando necesite inspeccionar el árbol de estructura lógica de un PDF etiquetado y examinar o actualizar los metadatos de los elementos de estructura.

## Obtener metadatos de contenido etiquetado

Utilice este ejemplo cuando necesite acceder al contenedor de contenido etiquetado y desee definir metadatos básicos del documento, como el título y el idioma.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Obtener el [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/) objeto del documento.
1. Establecer los metadatos del contenido etiquetado y guardar el archivo de salida.

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

## Obtener la estructura raíz de un PDF etiquetado

Este ejemplo muestra cómo inspeccionar los objetos raíz que representan el árbol de estructura de un Tagged PDF.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y obtener su contenido etiquetado.
1. Establezca los metadatos de documento requeridos.
1. Lea e imprima la raíz del árbol de estructura y el elemento raíz lógico, luego guarde el archivo.

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

## Acceder y actualizar elementos de estructura secundarios

Utilice este ejemplo cuando necesite iterar a través de los elementos secundarios en el árbol de estructura, inspeccionar sus propiedades y actualizar los metadatos seleccionados.

1. Abra el PDF etiquetado de origen [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Lea los elementos secundarios del nodo raíz del árbol de estructura e imprima las propiedades disponibles.
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
