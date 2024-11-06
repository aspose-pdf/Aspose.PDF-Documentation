---
title: Form Exporter
type: docs
weight: 50
url: es/net/plugins/formexpoter/
description: Cómo exportar valores de campos de formulario a archivos CSV utilizando el complemento Aspose.PDF Form Exporter
lastmod: "2024-01-24"
draft: false
---

En este artículo, te mostraremos cómo usar el [complemento Form Exporter](https://products.aspose.org/pdf/net/form-exporter/), que puede exportar valores de campos de formulario desde archivos PDF a archivos CSV.

## Prerrequisitos

Necesitarás lo siguiente:

* Visual Studio 2019 o posterior
* Aspose.PDF para .NET 21.1 o posterior
* Un archivo PDF de muestra que contenga algunos campos de formulario

Puedes descargar la biblioteca Aspose.PDF para .NET desde el sitio web oficial o instalarla usando el Gestor de Paquetes NuGet en Visual Studio.

## Pasos

Los pasos básicos para exportar valores de campos de formulario a archivos CSV utilizando el complemento FormExporter son:

1. Crea un objeto de la clase `FormExporter`
1. Crea un objeto de la clase `FormExporterValuesToCsvOptions` y especifica el predicado y el delimitador
1.
1.
1. Ejecute el método `Process` del objeto `FormExporter`

Veamos cómo implementar estos pasos en código C#.

### Paso 1: Cree un objeto de la clase FormExporter

La clase FormExporter es la clase principal que proporciona la funcionalidad de exportar los valores de los campos de formulario a archivos CSV. Para usarla, necesita crear una instancia de la misma utilizando el constructor predeterminado:

```cs
// Crear una instancia del plugin FormExporter
var plugin = new FormExporter();
```

### Paso 2: Cree un objeto de la clase FormExporterValuesToCsvOptions y especifique el predicado y el delimitador

La clase FormExporterValuesToCsvOptions es una clase auxiliar que le permite especificar varias opciones y parámetros para el proceso de exportación, como el predicado y el delimitador.
La clase FormExporterValuesToCsvOptions es una clase auxiliar que te permite especificar varias opciones y parámetros para el proceso de exportación, como el predicado y el delimitador.

```cs
// Crear opciones para exportar valores de campos de formulario a CSV
var options = new FormExporterValuesToCsvOptions(
(field) => { return field is TextBoxField && field.PageIndex == 2; }, ';');
```

### Paso 3: Agregar las fuentes de datos de entrada y salida al objeto de opciones

Las fuentes de datos de entrada y salida son los archivos PDF de los que deseas exportar y el archivo CSV que deseas guardar.
Las fuentes de datos de entrada y salida son los archivos PDF de los que desea exportar y el archivo CSV que desea guardar.

```cs
// Añadir archivos de entrada y salida a las opciones
options.AddInput(new FileDataSource("inputFileNameWithFields-1.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-2.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-3.pdf"));
options.AddInput(new FileDataSource("inputFileNameWithFields-4.pdf"));
options.AddOutput(new FileDataSource("outputFileName.csv"));

```

### Paso 4: Ejecutar el método Process del objeto FormExporter

El paso final es ejecutar el método Process del objeto FormExporter, pasando el objeto de opciones como parámetro.
El paso final es ejecutar el método Process del objeto FormExporter, pasando el objeto de opciones como parámetro.

```cs
// Procesar los valores de los campos del formulario utilizando el complemento
var resultContainer = plugin.Process(options);
var result = resultContainer.ResultCollection[0];
Console.WriteLine(result);

```

El resultado contendrá información como las rutas de los archivos de entrada y salida.
