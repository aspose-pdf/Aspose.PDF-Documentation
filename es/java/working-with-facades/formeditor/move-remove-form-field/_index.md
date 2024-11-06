---
title: Mover y Eliminar Campo de Formulario
type: docs
weight: 50
url: es/java/move-remove-form-field/
description: Esta sección explica cómo puede mover y eliminar Campos de Formulario con la Clase FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Mover Campo de Formulario a una Nueva Ubicación en un Archivo PDF Existente

Si desea mover un campo de formulario a una nueva ubicación, puede usar el método [moveField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#moveField-java.lang.String-float-float-float-float-) de la clase [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor).
 Necesita proporcionar solo el nombre del campo y la nueva ubicación de este campo al método [moveField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#moveField-java.lang.String-float-float-float-float-). También necesita guardar el archivo PDF actualizado utilizando el método Save de la clase [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). El siguiente fragmento de código le muestra cómo mover un campo de formulario a una nueva ubicación en un archivo PDF.

```java
 public static void MoveField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-05.pdf");
            editor.MoveField("Last Name", 262.56f, 496.75f, 382.28f, 514.03f);
            editor.Save(_dataDir + "Sample-Form-05-mod.pdf");
        }
```

## Eliminar un Campo de Formulario de un Archivo PDF Existente

Para eliminar un campo de formulario de un archivo PDF existente, puede utilizar el método RemoveField de la clase FormEditor. Este método toma solo un argumento: el nombre del campo. Necesitas crear un objeto de la clase FormEditor, llamar al método [removeField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#removeField-java.lang.String-) para eliminar un campo particular del PDF y luego llamar al método Save para guardar el archivo PDF actualizado. El siguiente fragmento de código te muestra cómo eliminar campos de formulario de un archivo PDF existente.

```java
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

También puedes renombrar tu campo utilizando el método [renameField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#renameField-java.lang.String-java.lang.String-) de la clase [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor).
```java
    public static void RenameFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            // Cambiar el nombre del campo "Last Name" a "LastName"
            editor.RenameField("Last Name", "LastName");
            // Cambiar el nombre del campo "First Name" a "FirstName"
            editor.RenameField("First Name", "FirstName");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```