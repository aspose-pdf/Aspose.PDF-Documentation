---
title: Añadir Campos de Formulario PDF
type: docs
weight: 10
url: es/net/add-form-fields/
description: Este tema explica cómo trabajar con Campos de Formulario con Aspose.PDF Facades usando la Clase FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Añadir Campo de Formulario en un Archivo PDF Existente

Para añadir un campo de formulario en un archivo PDF existente, necesitas usar el método [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) de la clase [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor). Este método requiere que especifiques el tipo de campo que deseas agregar junto con el nombre y la ubicación del campo. Necesitas crear un objeto de la clase [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor), usar el método [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) para añadir un nuevo campo en el PDF. Además, puedes especificar un límite en el número de caracteres en tu campo con [SetFieldLimit](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldlimit) y finalmente usar el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) para guardar el archivo PDF actualizado. El siguiente fragmento de código te muestra cómo agregar un campo de formulario en un archivo PDF existente.

```csharp
   public static void AddField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir+"Sample-Form-01.pdf");
            editor.AddField(FieldType.Text, "Country", 1, 232.56f, 496.75f, 352.28f, 514.03f);
            editor.SetFieldLimit("Country", 20);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```
## Añadir URL del Botón de Envío en un Archivo PDF Existente

El método [AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) te permite establecer la URL del botón de envío en un archivo PDF. Esta es la URL donde se envían los datos cuando se hace clic en el botón de envío. En nuestro código de ejemplo, especificamos la URL, el nombre de nuestro campo, el número de página al que queremos añadir, y las coordenadas de ubicación del botón. El método [AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) requiere el nombre del campo del botón de envío y la URL. Este método es proporcionado por la clase [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). El siguiente fragmento de código te muestra cómo establecer la URL del botón de envío.

```csharp
public static void AddSubmitBtn()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddSubmitBtn("Submit", 1, "Submit", "http://localhost:3000", 232.56f, 466.75f, 352.28f, 484.03f);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## Añadir JavaScript para Botón de Presión

El método [AddFieldScript](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfieldscript) te permite añadir JavaScript a un botón de presión en un archivo PDF. Este método requiere el nombre del botón de presión y el JavaScript. Este método es proporcionado por la clase [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). El siguiente fragmento de código te muestra cómo establecer JavaScript a un botón de presión.

```csharp
     public static void AddFieldScript()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.AddFieldScript("Last Name", "app.alert(\"Only one last name\",3);");
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```