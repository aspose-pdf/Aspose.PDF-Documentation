---
title: Trabajar con Imágenes usando PdfContentEditor
type: docs
weight: 50
url: /net/working-with-images-in-pdf
description: Esta sección explica cómo agregar y eliminar Imágenes con Aspose.PDF Facades usando la Clase PdfContentEditor.
lastmod: "2021-06-24"
---

## Eliminar Imágenes de una Página Particular de PDF (Facades)

Para eliminar las imágenes de una página particular, necesitas llamar al método [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) con los parámetros pageNumber e index. El parámetro index representa un arreglo de enteros: los índices de las imágenes a eliminar. En primer lugar, necesitas crear un objeto de la clase [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) y luego llamar al método [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1). Después de eso, puedes guardar el archivo PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

El siguiente fragmento de código te muestra cómo eliminar imágenes de una página específica de un PDF.

```csharp
public static void DeleteImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage(2, new[] { 2 });
    editor.Save(_dataDir + "PdfContentEditorDemo10.pdf");
}
```

## Eliminar Todas las Imágenes de un Archivo PDF (Facades)

Todas las imágenes se pueden eliminar de un archivo PDF utilizando el método [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) de [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Llama al método [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1), la sobrecarga sin ningún parámetro, para eliminar todas las imágenes, y luego guarda el archivo PDF actualizado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

El siguiente fragmento de código te muestra cómo eliminar todas las imágenes de un archivo PDF.

```csharp
public static void DeleteImages()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage();
    editor.Save(_dataDir + "PdfContentEditorDemo11.pdf");
}
```

## Reemplazar Imagen en un Archivo PDF (Facades)

El [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) te permite reemplazar tu imagen en un archivo PDF, para esto llama al método [ReplaceImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replaceimage) y guarda el resultado.

```csharp
public static void ReplaceImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
    editor.ReplaceImage(2, 4, @"C:\Samples\Facades\PdfContentEditor\cat04.jpg");
    editor.Save(_dataDir + "PdfContentEditorDemo12.pdf");
}
```