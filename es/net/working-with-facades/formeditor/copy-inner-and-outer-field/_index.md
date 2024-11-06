---
title: Copiar Campo Interno y Externo
type: docs
weight: 40
url: es/net/copy-inner-and-outer-field/
description: Esta sección explica cómo copiar Campo Interno y Externo con Aspose.PDF Facades usando la Clase FormEditor.
lastmod: "2021-06-05"
draft: false
---

El método [CopyInnerField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyinnerfield/index) te permite copiar un campo en el mismo archivo, en las mismas coordenadas, en la página especificada. Este método requiere el nombre del campo que deseas copiar, el nuevo nombre del campo y el número de página en el que el campo necesita ser copiado. La clase [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) proporciona este método. El siguiente fragmento de código te muestra cómo copiar el campo en la misma ubicación en el mismo archivo.

```csharp
  public static void CopyInnerField()
        {
            var editor = new FormEditor();
            var document = new Aspose.Pdf.Document(_dataDir + "Sample-Form-01.pdf");
            document.Pages.Add();
            editor.BindPdf(document);
            editor.CopyInnerField("Last Name", "Last Name 2", 2);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## Copiar Campo Externo en un Archivo PDF Existente

El método [CopyOuterField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyouterfield/index) te permite copiar un campo de formulario desde un archivo PDF externo y luego agregarlo al archivo PDF de entrada en la misma ubicación y el número de página especificado. Este método requiere el archivo PDF del cual se necesita copiar el campo, el nombre del campo y el número de página en el que se necesita copiar el campo. Este método es proporcionado por la clase [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). El siguiente fragmento de código te muestra cómo copiar un campo desde un archivo PDF externo.

```csharp
   public static void CopyOuterField()
        {
            var editor = new FormEditor();
            var document = new Aspose.Pdf.Document();
            document.Pages.Add();
            editor.BindPdf(document);
            editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
            editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
            editor.Save(_dataDir + "Sample-Form-02-mod.pdf");
        }
```