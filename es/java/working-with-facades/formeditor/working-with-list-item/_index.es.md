---
title: Trabajando con Elemento de Lista
type: docs
weight: 30
url: /java/working-with-list-item/
description: Esta sección explica cómo trabajar con Elemento de Lista con com.aspose.pdf.facades usando la Clase FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Añadir Elemento de Lista en un Archivo PDF Existente

El método [addListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#addListItem-java.lang.String-java.lang.String-) te permite añadir un elemento en un campo ListBox. El primer argumento es el nombre del campo y el segundo argumento es el ítem del campo. Puedes pasar un solo ítem de campo o puedes pasar un array de cadenas que contiene una lista de ítems. Este método es proporcionado por la clase [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). El siguiente fragmento de código te muestra cómo añadir elementos de lista en un archivo PDF.

```java
public static void AddListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        editor.addField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
        editor.addListItem("Country", "USA");
        editor.addListItem("Country", "Canada");
        editor.addListItem("Country", "France");
        editor.addListItem("Country", "Spain");
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```


## Eliminar un Elemento de Lista de un Archivo PDF Existente

El método [delListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#delListItem-java.lang.String-java.lang.String-) te permite eliminar un elemento particular de la ListBox. El primer parámetro es el nombre del campo, mientras que el segundo parámetro es el elemento que deseas eliminar de la lista. Este método es proporcionado por la clase [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). El siguiente fragmento de código te muestra cómo eliminar un elemento de lista del archivo PDF.

```java
    public static void DelListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-04.pdf");
        // -----
        editor.delListItem("Country", "France");
        // -----
        editor.save(_dataDir + "Sample-Form-04-mod.pdf");
    }
```