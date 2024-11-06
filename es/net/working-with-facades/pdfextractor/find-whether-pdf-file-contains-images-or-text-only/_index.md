---
title: Encontrar si un PDF contiene imágenes o texto
linktitle: Verificar presencia de texto e imágenes
type: docs
weight: 40
url: es/net/find-whether-pdf-file-contains-images-or-text-only/
description: Este tema explica cómo encontrar si un archivo PDF contiene solo imágenes o solo texto con la clase PdfExtractor.
lastmod: "2021-06-05"
draft: false
---

## Antecedentes

Un archivo PDF puede contener tanto texto como imágenes. A veces, un usuario podría necesitar averiguar si un archivo PDF contiene solo texto, o si contiene solo imágenes. También podemos encontrar si contiene ambos o ninguno.

{{% alert color="primary" %}}

El siguiente fragmento de código muestra cómo cumplir con este requisito.

{{% /alert %}}

```csharp
 public static void CheckIfPdfContainsTextOrImages()
{
    // Instanciar un objeto memoryStream para contener el texto extraído del documento
    MemoryStream ms = new MemoryStream();
    // Instanciar el objeto PdfExtractor
    PdfExtractor extractor = new PdfExtractor();

    // Vincular el documento PDF de entrada al extractor
    extractor.BindPdf(_dataDir + "FilledForm.pdf");
    // Extraer texto del documento PDF de entrada
    extractor.ExtractText();
    // Guardar el texto extraído en un archivo de texto
    extractor.GetText(ms);
    // Verificar si la longitud de MemoryStream es mayor o igual a 1

    bool containsText = ms.Length >= 1;

    // Extraer imágenes del documento PDF de entrada
    extractor.ExtractImage();

    // Llamar al método HasNextImage en un bucle while. Cuando se terminen las imágenes, el bucle saldrá
    bool containsImage = extractor.HasNextImage();

    // Ahora averiguar si este PDF es solo texto o solo imagen

    if (containsText && !containsImage)
        Console.WriteLine("El PDF contiene solo texto");
    else if (!containsText && containsImage)
        Console.WriteLine("El PDF contiene solo imágenes");
    else if (containsText && containsImage)
        Console.WriteLine("El PDF contiene tanto texto como imágenes");
    else if (!containsText && !containsImage)
        Console.WriteLine("El PDF no contiene ni texto ni imágenes");
}
```