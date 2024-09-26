---
title: Creando un PDF complejo
linktitle: Creando un PDF complejo
type: docs
weight: 60
url: /net/complex-pdf-example/
description: Aspose.PDF para NET permite crear documentos más complejos que contienen imágenes, fragmentos de texto y tablas en un solo documento.
aliases:
    - /net/complex-pdf/
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

El ejemplo [Hola, Mundo](/pdf/net/hello-world-example/) mostró pasos simples para crear un documento PDF usando C# y Aspose.PDF. En este artículo, veremos cómo crear un documento más complejo con C# y Aspose.PDF para .NET. Como ejemplo, tomaremos un documento de una compañía ficticia que opera servicios de ferry para pasajeros.
Nuestro documento contendrá una imagen, dos fragmentos de texto (encabezado y párrafo) y una tabla. Para construir un documento así, utilizaremos el enfoque basado en DOM. Puedes leer más en la sección [Fundamentos de la API DOM](/pdf/net/basics-of-dom-api/).

Si creamos un documento desde cero necesitamos seguir ciertos pasos:

1.
1. Agrega una [Página](https://reference.aspose.com/pdf/net/aspose.pdf/page) al objeto del documento. Así que ahora nuestro documento tendrá una página.
1. Añade una [Imagen](https://reference.aspose.com/pdf/net/aspose.pdf/image/methods/index) a la Página.
1. Crea un [Fragmento de Texto](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) para el encabezado. Para el encabezado usaremos la fuente Arial con tamaño de fuente de 24pt y alineación centrada.
1. Añade el encabezado a los [Párrafos](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) de la página.
1. Crea un [Fragmento de Texto](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) para la descripción. Para la descripción usaremos la fuente Arial con tamaño de fuente de 24pt y alineación centrada.
1. Añade (descripción) a los Párrafos de la página.
1. Crea una tabla, añade propiedades a la tabla.
1. Añade (tabla) a los [Párrafos](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/paragraphs) de la página.
1. Guarda el documento "Complex.pdf".

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
using Aspose.Pdf.Text;
using System;
using System.IO;

namespace Aspose.Pdf.Examples
{
    public static class ExampleGetStarted
    {
        private static readonly string _dataDir = "..\\..\\..\\Samples";
        public static void MakeComplexDocument()
        {
            // Inicializar objeto documento
            Document document = new Document();
            // Agregar página
            Page page = document.Pages.Add();

            // -------------------------------------------------------------
            // Agregar imagen
            var imageFileName = System.IO.Path.Combine(_dataDir, "logo.png");
            page.AddImage(imageFileName, new Rectangle(20, 730, 120, 830));

            // -------------------------------------------------------------
            // Agregar encabezado
            var header = new TextFragment("Nuevas rutas de ferry en otoño 2020");
            header.TextState.Font = FontRepository.FindFont("Arial");
            header.TextState.FontSize = 24;
            header.HorizontalAlignment = HorizontalAlignment.Center;
            header.Position = new Position(130, 720);
            page.Paragraphs.Add(header);

            // Agregar descripción
            var descriptionText = "Los visitantes deben comprar los boletos en línea y los boletos están limitados a 5,000 por día. El servicio de ferry está operando a media capacidad y en un horario reducido. Espere filas.";
            var description = new TextFragment(descriptionText);
            description.TextState.Font = FontRepository.FindFont("Times New Roman");
            description.TextState.FontSize = 14;
            description.HorizontalAlignment = HorizontalAlignment.Left;
            page.Paragraphs.Add(description);

            // Agregar tabla
            var table = new Table
            {
                ColumnWidths = "200",
                Border = new BorderInfo(BorderSide.Box, 1f, Color.DarkSlateGray),
                DefaultCellBorder = new BorderInfo(BorderSide.Box, 0.5f, Color.Black),
                DefaultCellPadding = new MarginInfo(4.5, 4.5, 4.5, 4.5),
                Margin =
                {
                    Bottom = 10
                },
                DefaultCellTextState =
                {
                    Font =  FontRepository.FindFont("Helvetica")
                }
            };

            var headerRow = table.Rows.Add();
            headerRow.Cells.Add("Sale de la ciudad");
            headerRow.Cells.Add("Sale de la isla");
            foreach (Cell headerRowCell in headerRow.Cells)
            {
                headerRowCell.BackgroundColor = Color.Gray;
                headerRowCell.DefaultCellTextState.ForegroundColor = Color.WhiteSmoke;
            }

            var time = new TimeSpan(6, 0, 0);
            var incTime = new TimeSpan(0, 30, 0);
            for (int i = 0; i < 10; i++)
            {
                var dataRow = table.Rows.Add();
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
                time=time.Add(incTime);
                dataRow.Cells.Add(time.ToString(@"hh\:mm"));
            }

            page.Paragraphs.Add(table);

            document.Save(System.IO.Path.Combine(_dataDir, "Complex.pdf"));

        }
    }
}
```

