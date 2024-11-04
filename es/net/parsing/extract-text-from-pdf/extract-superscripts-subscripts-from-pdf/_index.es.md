---
title: Extraer texto Superíndices y Subíndices de PDF
linktitle: Extraer Superíndices y Subíndices
type: docs
weight: 30
url: /net/extract-superscripts-subscripts-from-pdf/
description: Este artículo describe varias formas de extraer texto de Superíndices y Subíndices de un PDF utilizando Aspose.PDF en C#.
lastmod: "2022-10-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extraer Texto de Superíndices y Subíndices

Extraer texto de un documento PDF es algo común. Sin embargo, en dicho texto, cuando se extrae, los **Superíndices y Subíndices** contenidos en ellos, que son típicos en documentos técnicos y artículos, pueden no mostrarse. Un Subíndice o Superíndice es un carácter, número o letra colocado debajo o encima de una línea regular de texto. Generalmente es más pequeño que el resto del texto.

**Los Subíndices y Superíndices** se usan más a menudo en fórmulas, expresiones matemáticas y especificaciones de compuestos químicos.
**Subíndices y Superíndices** son más utilizados en fórmulas, expresiones matemáticas y especificaciones de compuestos químicos.
En una de las últimas versiones, la biblioteca **Aspose.PDF para .NET** agregó soporte para extraer texto de Superíndices y Subíndices de PDF.

Utiliza la clase **TextFragmentAbsorber** y ya puedes hacer cualquier cosa con el texto encontrado, es decir, puedes simplemente usar todo el texto. Prueba el siguiente fragmento de código:

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            writer.WriteLine(absorber.Text);
        }
```

O utiliza **TextFragments** por separado y realiza todo tipo de manipulaciones con ellos, por ejemplo, ordenar por coordenadas o por tamaño.

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).
El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            foreach (var textFragment in absorber.TextFragments)
            {
                writer.Write(textFragment.Text);
            }
        }
```
