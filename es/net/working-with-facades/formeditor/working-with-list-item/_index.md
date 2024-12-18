---
title: Trabajando con Elemento de Lista
type: docs
weight: 30
url: /es/net/working-with-list-item/
description: Esta sección explica cómo trabajar con el Elemento de Lista usando Aspose.PDF Facades con la clase FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Agregar Elemento de Lista en un Archivo PDF Existente

El método [AddListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addlistitem) te permite agregar un elemento en un campo [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield). El primer argumento es el nombre del campo y el segundo argumento es el elemento del campo. Puedes pasar un único elemento de campo o puedes pasar un array de cadenas que contiene una lista de elementos. Este método es proporcionado por la clase [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). El siguiente fragmento de código te muestra cómo agregar elementos de lista en un archivo PDF.

```csharp
  public static void AddListItem()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
            editor.AddListItem("Country", "USA");
            editor.AddListItem("Country", "Canada");
            editor.AddListItem("Country", "France");
            editor.AddListItem("Country", "Spain");
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## Eliminar un Elemento de Lista de un Archivo PDF Existente

El método [DelListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/dellistitem) te permite eliminar un elemento particular del [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield). El primer parámetro es el nombre del campo, mientras que el segundo parámetro es el elemento que deseas eliminar de la lista. Este método es proporcionado por la clase [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). El siguiente fragmento de código te muestra cómo eliminar un elemento de lista del archivo PDF.

```csharp
      public static void DelListItem()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-04.pdf");
            //-----
            editor.DelListItem("Country", "France");
            //-----
            editor.Save(_dataDir + "Sample-Form-04-mod.pdf");
        }
```