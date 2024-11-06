---
title: Generador de Tablas
type: docs
weight: 130
url: es/net/plugins/tablegenerator/
description: Permite agregar/insertar una tabla en el número de página especificado del documento PDF.
lastmod: "2024-01-24"
draft: false
---

¿Necesitas crear tablas dinámicas y visualmente atractivas en tus documentos PDF usando .NET? Aspose.PDF para .NET ofrece una clase poderosa, TableGenerator, que simplifica el proceso. En este capítulo, vamos a explicar los pasos para generar tablas en un documento PDF usando [Aspose.PDF Table Generator](https://products.aspose.org/pdf/net/table-generator/), desde crear un documento de demostración hasta generar tablas con la clase TableGenerator.
Vamos a sumergirnos y aprender cómo generar tablas paso a paso.

## Prerrequisitos

Necesitarás lo siguiente:

* Visual Studio 2019 o posterior
* Aspose.PDF para .NET 24.3 o posterior
* Un archivo PDF de muestra

## Creando un Documento de Demostración

Antes de comenzar a generar tablas, vamos a crear un documento de demostración con páginas vacías donde se insertarán nuestras tablas.
Antes de sumergirnos en la generación de tablas, creemos un documento de demostración con páginas vacías donde se insertarán nuestras tablas.

* Crea un nuevo documento PDF.
* Añade páginas vacías al documento.
* Guarda el documento en el archivo especificado.

```cs
// <summary>
// Crea un documento de demostración con páginas vacías.
//
// Parámetros:
// - fileName: La ruta y nombre del archivo de salida.
// </summary>
internal static void CreateDemoDocument(string fileName)
{
    // Crea un nuevo documento PDF.
    var document = new Aspose.Pdf.Document();

    // Añade cuatro páginas vacías al documento.
    for (int i = 0; i < 2; i++)
    {
        document.Pages.Add();
    }

    // Guarda el documento en el archivo especificado.
    document.Save(fileName);
}
```

## Generación de Tablas

Una vez que tenemos nuestro documento de demostración listo, podemos comenzar a generar tablas usando la clase `TableGenerator`. El siguiente fragmento demuestra cómo generar tablas con varios tipos de contenido y opciones de formato. Así es como se generan las tablas:

* Crea una nueva instancia de la clase `TableGenerator`.
* Crear una nueva instancia de la clase `TableGenerator`.
* Crear opciones de tabla y especificar fuentes de datos de archivos de entrada y salida.
* Agregar tablas con filas y celdas a las opciones, especificando contenido y formato.
* Procesar la generación de la tabla usando el método `Process` y obtener el contenedor de resultados.

### Creando Tablas

Para crear una tabla usando Aspose.PDF, sigue estos pasos:

```cs
// Crear una nueva instancia de la clase TableGenerator.
var generator = new TableGenerator();

// Crear opciones de tabla y agregar tablas de demostración.
var options = new TableOptions();

// Agregar fuentes de datos de archivos de entrada y salida a las opciones.
options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

// Agregar la primera tabla a las opciones.
options
    .InsertPageAfter(1)
    .AddTable()
```

En el código anterior, creamos una instancia de `TableOptions` y especificamos fuentes de datos de archivos de entrada y salida para el documento PDF.
En el código anterior, creamos una instancia de `TableOptions` y especificamos las fuentes de datos de archivos de entrada y salida para el documento PDF.

### Agregar Contenido a las Tablas

Una vez que la tabla está creada, puedes poblarla con filas y celdas que contienen varios tipos de contenido, como texto, HTML, imágenes, etc. Aquí te mostramos cómo agregar contenido a una tabla:

```csharp
options
    .AddTable()
        .AddRow()
            .AddCell()
                .AddParagraph(new HtmlFragment("<h1>Encabezado 1</h1>")) // Agrega contenido HTML a la celda.
            .AddCell()
                .AddParagraph(new HtmlFragment("<h2>Encabezado 2</h2>"))
            .AddCell()
                .AddParagraph(new HtmlFragment("<h3>Encabezado 3</h3>"));
```

En este ejemplo, agregamos una fila a la tabla y la poblamos con celdas que contienen fragmentos HTML que representan encabezados.

Métodos útiles:

* **InsertPageAfter**: Inserta una página después del número de página especificado.
* **InsertPageBefore**: Inserta una página después del número de página especificado.
* **AddTable**: Agrega una tabla al documento.
* **AddTable**: Agrega una tabla al documento.
* **AddRow**: Agrega una fila a la tabla.
* **AddCell**: Agrega celdas a la fila.
* **AddParagraph**: Agrega contenido a la celda.

Puedes agregar los siguientes tipos de contenido como párrafo:

* **HtmlFragment** - un contenido basado en marcado HTML
* **TeXFragment** - un contenido basado en marcado TeX/LaTeX
* **TextFragment** - un contenido de texto simple
* **Image** - gráficos

## Generación de tablas

Después de agregar el contenido, podemos comenzar a crear la tabla.

```cs
// Procesar la generación de la tabla y obtener el contenedor de resultados.
var resultContainer = generator.Process(options);

// Imprimir el número de resultados en la colección de resultados.
Console.WriteLine(resultContainer.ResultCollection.Count);
```

El método `Process` realiza la generación de la tabla. Este método también puede envolverse con try-catch para manejar errores.

A continuación, puedes ver el código completo del ejemplo:

```cs
using Aspose.Pdf;
using Aspose.Pdf.Plugins;
using Aspose.Pdf.Text;

namespace AsposePluginsNet8.Documentation
{
    // <summary>
    // Representa una clase que demuestra el uso de la generación de tablas en Aspose.Pdf.
    // </summary>
    internal static class TableDemo
    {
        // <summary>
        // Ejecuta la demostración de generación de tablas.
        // </summary>
        internal static void Run()
        {
            // Crear un documento de demostración y generar tablas.
            CreateDemoDocument(@"C:\Samples\Results\table-generator-demo.pdf");
            CreateDemoTable();
        }

        // <summary>
        // Crea un documento de demostración con cuatro páginas vacías.
        //
        // Parámetros:
        // - fileName: La ruta y el nombre del archivo de salida.
        // </summary>
        internal static void CreateDemoDocument(string fileName)
        {
            // Crear un nuevo documento PDF.
            var document = new Aspose.Pdf.Document();

            // Agregar cuatro páginas vacías al documento.
            for (int i = 0; i < 2; i++)
            {
                document.Pages.Add();
            }

            // Guardar el documento en el archivo especificado.
            document.Save(fileName);
        }

        // <summary>
        // Genera tablas usando la clase TableGenerator.
        // </summary>
        internal static void CreateDemoTable()
        {
            // Crear una nueva instancia de la clase TableGenerator.
            var generator = new TableGenerator();

            // Crear opciones de tabla y agregar tablas de demostración.
            var options = new TableOptions();

            // Agregar fuentes de datos de archivos de entrada y salida a las opciones.
            options.AddInput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));
            options.AddOutput(new FileDataSource(@"C:\Samples\Results\table-generator-demo.pdf"));

            // Agregar la primera tabla a las opciones.
            options
                .InsertPageAfter(1)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h1>Encabezado 1</h1>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h2>Encabezado 2</h2>"))
                        .AddCell()
                            .AddParagraph(new HtmlFragment("<h3>Encabezado 3</h3>"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TeXFragment("{\\small La ecuación $E=mc^2$, descubierta en 1905 por Albert Einstein.}", true))
                        .AddCell()
                            .AddParagraph(new TextFragment("Celda 2 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Celda 2 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("Celda 3 1a"))
                            .AddParagraph(new TextFragment("Celda 3 1b"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Celda 3 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Celda 3 3"));

            // Agregar la segunda tabla a las opciones.
            options
                .InsertPageBefore(2)
                .AddTable()
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new TextFragment("Encabezado 1 1"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Encabezado 1 2"))
                        .AddCell()
                            .AddParagraph(new TextFragment("Encabezado 1 3"))
                    .AddRow()
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\logo.png",
                                FixWidth = 75,
                                FixHeight = 75,
                            })
                        .AddCell()
                            .AddParagraph(new Image()
                            {
                                File = @"C:\Samples\sample.svg",
                                FileType = ImageFileType.Svg,
                                FixWidth = 75,
                                FixHeight = 75
                            })
                        .AddCell()
                            .AddParagraph new Image()
                            {
                                ImageStream = File.OpenRead(@"C:\Samples\Conversion\Demo.dcm"),
                                FileType = ImageFileType.Dicom,
                                FixWidth = 75,
                                FixHeight = 75
                            });

            // Procesar la generación de la tabla y obtener el contenedor de resultados.
            var resultContainer = generator.Process(options);

            // Imprimir el número de resultados en la colección de resultados.
            Console.WriteLine(resultContainer.ResultCollection.Count);
        }
    }
}
```

