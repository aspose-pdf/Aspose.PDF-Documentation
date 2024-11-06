---
title: Form Exporter
type: docs
weight: 60
url: es/net/plugins/formflattener/
description: Cómo aplanar campos de formulario en archivos PDF usando el complemento Aspose.PDF FormFlattener
lastmod: "2024-01-24"
---

En este artículo, le mostraremos cómo usar el [complemento FormFlattener](https://products.aspose.org/pdf/net/form-flattener/), que puede aplanar campos de formulario en archivos PDF.

## Prerrequisitos

Necesitará lo siguiente:

* Visual Studio 2019 o posterior
* Aspose.PDF para .NET 21.1 o posterior
* Un archivo PDF de muestra que contenga algunos campos de formulario

Puede descargar la biblioteca Aspose.PDF para .NET desde el sitio web oficial o instalarla usando el Administrador de Paquetes NuGet en Visual Studio.

## Pasos

Los pasos básicos para aplanar campos de formulario en archivos PDF usando el complemento FormFlattener son:

1. Crear un objeto de la clase FormFlattener
1. Crear un objeto de la clase FormFlattenAllFieldsOptions o FormFlattenSelectedFieldsOptions, dependiendo de si desea aplanar todos o algunos campos
1. Ejecute el método Process del objeto FormFlattener

Veamos cómo implementar estos pasos en código C#.

### Paso 1: Crear un objeto de la clase FormFlattener

La clase FormFlattener es la clase principal que proporciona la funcionalidad de aplanar campos de formulario en archivos PDF. Para usarla, necesitas crear una instancia de ella usando el constructor predeterminado:

```cs
// Crear una instancia del plugin FormFlattener
var plugin = new FormFlattener();
```

### Paso 2: Crear un objeto de la clase FormFlattenAllFieldsOptions o FormFlattenSelectedFieldsOptions, dependiendo de si desea aplanar todos o algunos campos

Las clases FormFlattenAllFieldsOptions y FormFlattenSelectedFieldsOptions son clases auxiliares que te permiten especificar varias opciones y parámetros para el proceso de aplanamiento.
Las clases FormFlattenAllFieldsOptions y FormFlattenSelectedFieldsOptions son clases auxiliares que te permiten especificar varias opciones y parámetros para el proceso de aplanamiento.

```cs
// Crear opciones para aplanar todos los campos
var options = new FormFlattenAllFieldsOptions();
```

Para aplanar solo los campos de formulario cuya coordenada x inferior izquierda sea mayor a 300, puedes usar el siguiente código:

```cs
// Crear opciones para aplanar campos seleccionados
var options = new FormFlattenSelectedFieldsOptions((field) => field.Rect.LLX > 300);
```

### Paso 3: Agregar las fuentes de datos de entrada y salida al objeto de opciones

Las fuentes de datos de entrada y salida son los archivos PDF que deseas aplanar y guardar.
Las fuentes de datos de entrada y salida son los archivos PDF que desea aplanar y guardar.

```cs
// Agregar fuentes de datos de entrada y salida a las opciones
options.Inputs.Add(new FileDataSource("sample.pdf"));
options.Outputs.Add(new FileDataSource("sample-flat.pdf"));
```

### Paso 4: Ejecutar el método Process del objeto FormFlattener

El paso final es ejecutar el método Process del objeto FormFlattener, pasando el objeto de opciones como parámetro. Este método realizará el proceso de aplanamiento y devolverá un objeto ResultContainer, que contiene los resultados del proceso, como el estado, los mensajes, las fuentes de datos de salida, etc. Puede acceder a los resultados utilizando las propiedades y métodos de la clase ResultContainer. Por ejemplo, para obtener el primer resultado de la colección de resultados e imprimirlo en la consola, puede usar el siguiente código:

```cs
// Procesar las opciones y obtener el contenedor de resultados
var resultContainer = plugin.Process(options);

// Obtener el primer resultado del contenedor de resultados
var result = resultContainer.ResultCollection[0];

// Imprimir el resultado
Console.WriteLine(result);
```
El resultado contendrá información como las rutas de los archivos de salida.
