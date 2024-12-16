---
title: Mover y Eliminar Campo de Formulario
type: docs
weight: 50
url: /es/net/move-remove-form-field/
description: Esta sección explica cómo puede mover y eliminar Campos de Formulario con la Clase FormEditor.
lastmod: "2021-06-05"
draft: false
---


## Mover el Campo de Formulario a una Nueva Ubicación en un Archivo PDF Existente

Si desea mover un campo de formulario a una nueva ubicación, puede usar el método [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) de la clase [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Necesitas proporcionar solo el nombre del campo y la nueva ubicación de este campo al método [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield). También necesitas guardar el archivo PDF actualizado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) de la clase [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). El siguiente fragmento de código te muestra cómo mover un campo de formulario a una nueva ubicación en un archivo PDF.

```csharp
public static void MoveField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-05.pdf");
            editor.MoveField("Last Name", 262.56f, 496.75f, 382.28f, 514.03f);
            editor.Save(_dataDir + "Sample-Form-05-mod.pdf");
        }
```

## Eliminar Campo de Formulario de un Archivo PDF Existente

Para eliminar un campo de formulario de un archivo PDF existente, puedes usar el método RemoveField de la clase FormEditor. Este método toma solo un argumento: el nombre del campo. Necesitas crear un objeto de la clase FormEditor, llamar al método [RemoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/removefield) para eliminar un campo en particular del PDF y luego llamar al método Save para guardar el archivo PDF actualizado. El siguiente fragmento de código te muestra cómo eliminar campos de formulario de un archivo PDF existente.

```csharp
  public static void RemoveFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.RemoveField("First Name");
            editor.RemoveField("Last Name");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```

## Renombrar Campos de Formulario en PDF

También puedes renombrar tu campo usando el método [RenameField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/renamefield) de la clase [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor).

```csharp

        public static void RenameFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.RenameField("Last Name", "LastName");
            editor.RenameField("First Name", "FirstName");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```