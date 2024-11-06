---
title: Adding multi line watermark 
type: docs
weight: 10
url: es/net/adding-multi-line-watermark-to-existing-pdf/
description: Esta sección explica cómo agregar una marca de agua de varias líneas a un PDF existente usando la clase FormattedText.
lastmod: "2021-06-05"
draft: false
---

{{% alert color="primary" %}}

Muchos usuarios quieren estampar sus documentos PDF con texto de varias líneas. Usualmente intentan usar `\n` y `<br>`, pero estos tipos de caracteres no son soportados por el espacio de nombres Aspose.Pdf.Facades. Por lo tanto, para hacer esto posible, hemos añadido otro método llamado [AddNewLineText()](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext/methods/addnewlinetext/index) en la clase [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) del espacio de nombres Aspose.Pdf.Facades.

{{% /alert %}}

## Implementación

Por favor, consulte el siguiente fragmento de código para agregar una marca de agua de varias líneas en un PDF existente.

```csharp

// Instanciar un objeto de sello
Stamp logoStamp = new Stamp();

// Instanciar un objeto de la clase FormattedText
FormattedText formatText = new FormattedText("¡Hola Mundo!",
System.Drawing.Color.FromArgb(180, 0, 0), FontStyle.TimesItalic, EncodingType.Winansi, false, 50);

// Añadir otra línea para el sello
formatText.AddNewLineText("Buena suerte");
// Vincular logo al PDF
logoStamp.BindLogo(formatText);
```