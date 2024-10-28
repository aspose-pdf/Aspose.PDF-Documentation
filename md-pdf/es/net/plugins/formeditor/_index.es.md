---
title: Form Editor
type: docs
weight: 40
url: /net/plugins/formeditor/
description: Cómo Agregar, Actualizar y Eliminar Campos de Formularios en Archivos PDF utilizando los Plugins de Aspose.PDF
lastmod: "2024-01-24"
draft: false
---

En este artículo, le mostraremos cómo usar el [plugin de Editor de Formularios](https://products.aspose.org/pdf/net/form-editor/), que puede agregar, actualizar y eliminar campos de formularios en archivos PDF.

## Prerrequisitos

Necesitará lo siguiente:

* Visual Studio 2019 o posterior
* Aspose.PDF para .NET 24.1 o posterior
* Un archivo PDF de muestra que contenga algunos campos de formulario

Puede descargar la biblioteca Aspose.PDF para .NET desde el sitio web oficial o instalarla utilizando el Administrador de Paquetes NuGet en Visual Studio.

## Pasos

Los pasos básicos para agregar, actualizar y eliminar campos de formulario en archivos PDF utilizando el plugin FormEditor son:

1. Crear un objeto de la clase FormEditor
1. Crear un objeto de la clase FormEditorAddOptions, FormEditorSetOptions, o FormRemoveSelectedFieldsOptions, dependiendo de la operación que desea realizar
1.
1.
1. Ejecutar el método Process del objeto FormEditor

Veamos cómo implementar estos pasos en código C# para cada operación.

### Paso 1: Crear un objeto de la clase FormEditor

La clase FormEditor es la clase principal que proporciona la funcionalidad de añadir, actualizar y eliminar campos de formulario en archivos PDF. Para usarla, necesitas crear una instancia de ella usando el constructor por defecto:

```cs
// Crear una instancia del plugin FormEditor
var plugin = new FormEditor();
```

### Paso 2: Crear un objeto de la clase FormEditorAddOptions, FormEditorSetOptions o FormRemoveSelectedFieldsOptions, dependiendo de la operación que desees realizar

Las clases `FormEditorAddOptions`, `FormEditorSetOptions` y `FormRemoveSelectedFieldsOptions` son clases auxiliares que te permiten especificar varias opciones y parámetros para las operaciones de edición de formulario, como los tipos de campos de formulario, valores, propiedades, predicados, etc.
Las clases `FormEditorAddOptions`, `FormEditorSetOptions` y `FormRemoveSelectedFieldsOptions` son clases auxiliares que te permiten especificar varias opciones y parámetros para las operaciones de edición de formularios, como los tipos de campos de formulario, valores, propiedades, predicados, etc.

```cs
    // Crear opciones para añadir campos de formulario.
    var options = new FormEditorAddOptions(
        [
            // Crear un campo de formulario de casilla de verificación.
            new FormCheckBoxFieldCreateOptions(1, new Rectangle(110, 700, 125, 715))
            {
                Value = "CampoDeCasilla 1",
                PartialName = "CampoDeCasilla_1",
                Color = Color.Blue,
            },
            // Crear un campo de formulario de cuadro combinado.
            new FormComboBoxFieldCreateOptions(1, new Rectangle(310, 600, 350, 615))
            {
                Color = Color.Red,
                Editable = true,
                DefaultAppearance = new DefaultAppearance("Arial Bold", 12, System.Drawing.Color.DarkGreen),
                Options = ["opción1", "opción2", "opción3"],
                Selected = 2
            },
            // Crear un campo de formulario de cuadro de texto.
            new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715))
            {
                MaxLen = 10,
                Value = "Algún texto",
                Color = Color.Chocolate
            }
        ]);
```
Para actualizar los valores de los campos del formulario cuyos valores son "a value" o "an another value" a "new value", puedes usar el siguiente código:

```cs
    var options = new FormEditorSetOptions(
    (field) => { return field.Value == "a value" || field.Value == "an another value"; },
    new FormFieldSetOptions()
    {
        Value = "new value"
    });
```

Para eliminar los campos del formulario cuya coordenada x inferior izquierda es mayor que 300, puedes usar el siguiente código:

```cs
// Crear opciones para eliminar campos del formulario
var options = new FormRemoveSelectedFieldsOptions((field) => field.Rect.LLX > 300);
```

### Paso 3: Agrega las fuentes de datos de entrada y salida al objeto de opciones

Las fuentes de datos de entrada y salida son los archivos PDF que deseas editar y guardar.
Las fuentes de datos de entrada y salida son los archivos PDF que desea editar y guardar.

```cs
// Especifique las rutas de los archivos de entrada y salida
string inputPath = $@"C:\Samples\Output\sample_forms.pdf";
string outputPath = $@"C:\Samples\Output\sample_forms2.pdf";

// Cree una nueva instancia de la clase FileDataSource para los archivos de entrada y salida
FileDataSource inputData = new(inputPath);
FileDataSource outputData = new(outputPath);

// Agregue las fuentes de datos de entrada y salida a las opciones
options.AddInput(inputData);
options.AddOutput(outputData);
```

### Paso 4: Ejecutar el método Process del objeto FormEditor

El paso final es ejecutar el método Process del objeto FormEditor, pasando el objeto de opciones como parámetro.
El paso final es ejecutar el método Process del objeto FormEditor, pasando el objeto de opciones como parámetro.

```cs
// Procesar la operación de edición de formulario utilizando el plugin y las opciones
ResultContainer result = plugin.Process(options);

// Obtener el primer resultado de la colección de resultados
var result = resultContainer.ResultCollection[0];

// Imprimir el resultado
Console.WriteLine(result);
```

El resultado contendrá información como las rutas de los archivos de salida.
