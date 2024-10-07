---
title: Extraer fuentes de PDF C#
linktitle: Extraer fuentes de PDF
type: docs
weight: 30
url: /net/extract-fonts-from-pdf/
description: Utiliza la biblioteca Aspose.PDF for. NET para extraer todas las fuentes incrustadas de tu documento PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

En caso de que quieras obtener todas las fuentes de un documento PDF, puedes usar el método FontUtilities.GetAllFonts() proporcionado en la clase Document. Por favor revisa el siguiente fragmento de código para obtener todas las fuentes de un documento PDF existente:

El siguiente fragmento de código también funciona con la biblioteca [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Para ejemplos completos y archivos de datos, por favor ve a https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// La ruta al directorio de documentos.
string dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
Document doc = new Document(dataDir + "input.pdf");
Aspose.Pdf.Text.Font[] fonts = doc.FontUtilities.GetAllFonts();
foreach (Aspose.Pdf.Text.Font font in fonts)
{
    Console.WriteLine(font.FontName);
}
```

