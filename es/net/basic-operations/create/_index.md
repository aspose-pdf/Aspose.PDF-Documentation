---
title: Crear documento PDF programáticamente
linktitle: Crear PDF
type: docs
weight: 10
url: es/net/create-document/
description: Esta página describe cómo crear un documento PDF desde cero con la biblioteca Aspose.PDF.
---

Aspose.PDF para la API de .NET te permite crear y leer archivos PDF usando C# y VB.NET. La API puede ser utilizada en una variedad de aplicaciones .NET incluyendo WinForms, ASP.NET, y varias otras. En este artículo, vamos a mostrar cómo utilizar Aspose.PDF para la API de .NET para generar y leer archivos PDF fácilmente en aplicaciones .NET.

## Cómo crear un archivo PDF usando C#

Para crear un archivo PDF usando C#, los siguientes pasos pueden ser utilizados.

1. Crear un objeto de la clase [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document)
1. Añadir un objeto [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) a la colección [Pages](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/pages) del objeto Document
1.
1. Guarde el documento PDF resultante

El siguiente fragmento de código también funciona con la nueva interfaz gráfica [Aspose.Drawing](/pdf/net/drawing/).

```csharp
// Para ejemplos completos y archivos de datos, por favor visite https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_QuickStart();

// Inicializar el objeto de documento
Document document = new Document();
// Añadir página
Page page = document.Pages.Add();
// Añadir texto a la nueva página
page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("¡Hola Mundo!"));
// Guardar el PDF actualizado
document.Save(dataDir + "HelloWorld_out.pdf")
```

En este caso, creamos un documento PDF de una página con tamaño de página A4, orientación vertical. Nuestra página contendrá un "Hola, Mundo" en la parte superior izquierda de la página.
