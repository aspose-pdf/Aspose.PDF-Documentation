---
title: Trabajando con Rotación de Página
type: docs
weight: 10
url: /net/working-with-page-rotation/
description: Esta sección explica cómo trabajar con la Rotación de Página usando la Clase PdfPageEditor.
lastmod: "2021-07-07"
draft: false
---

{{% alert color="primary" %}}

La clase [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) proporciona la capacidad de rotar una página.

{{% /alert %}}

## Rotar página usando PageRotations

Para rotar páginas en un documento podemos usar [PageRotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/pagerotations).
`PageRotations` contiene el número de página y el grado de rotación, la clave representa el número de página, el valor de la clave representa la rotación en grados.

```csharp
public static void RotatePages1()
{
    var editor = new PdfPageEditor();
    editor.BindPdf(_dataDir + "sample.pdf");

    editor.PageRotations = new System.Collections.Generic.Dictionary<int, int> { { 1, 90 }, { 2, 180 }, { 3,270 } };

    editor.Save(_dataDir + "sample-rotate-a.pdf");
}
```

## Rotar página usando Rotación

También podemos usar la propiedad [Rotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/rotation). La rotación debe ser 0, 90, 180 o 270

```csharp
public static void RotatePages2()
{
    var editor = new PdfPageEditor();
    editor.BindPdf(_dataDir + "sample.pdf");

    editor.ProcessPages = new int[] { 1, 3 };
    editor.Rotation = 90;

    editor.Save(_dataDir + "sample-rotate-a.pdf");
}
```