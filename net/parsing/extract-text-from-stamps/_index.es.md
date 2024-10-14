---
title: Extraer texto de sellos usando C#
type: docs
weight: 60
url: /net/extract-text-from-stamps/
description: Aprende a usar la función especial de Aspose.PDF para .NET - extracción de texto de anotaciones de sello
lastmod: "2021-01-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraer texto de anotaciones de sello

Aspose.PDF para NET te permite extraer texto de anotaciones de sello. Para extraer texto de Anotaciones de Sello en un PDF, se pueden utilizar los siguientes pasos.

1. Crear un objeto de la clase `Document`
1. Obtener la `Annotation` deseada de la lista de anotaciones de una página
1. Definir un nuevo objeto de la clase `TextAbsorber`
1. Usar el método visit de TextAbsorber para obtener el Texto

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void ExtractText()
{
   Document document = new Document(_dataDir + "ExtractStampText.pdf");
   Annotation item = document.Pages[1].Annotations[1];
   if (item is StampAnnotation annot) {
         TextAbsorber ta = new TextAbsorber();
         XForm ap = annot.Appearance["N"];
         ta.Visit(ap);
         Console.WriteLine(ta.Text);
   }
}
```

