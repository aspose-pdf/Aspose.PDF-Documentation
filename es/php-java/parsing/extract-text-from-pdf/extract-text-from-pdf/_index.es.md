---
title: Extracción de texto sin formato de un archivo PDF
linktitle: Extraer texto de PDF
type: docs
weight: 10
url: /php-java/extract-text-from-all-pdf/
description: Este artículo describe varias formas de extraer texto de documentos PDF usando Aspose.PDF para PHP. De páginas enteras, de una parte específica, basado en columnas, etc.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraer Texto de Todas las Páginas de un Documento PDF

La extracción de texto de un documento PDF es un requisito común. En este ejemplo, verás cómo Aspose.PDF para PHP permite extraer texto de todas las páginas de un documento PDF.
Para extraer texto de todas las páginas del PDF:

1. Crea un objeto de la clase [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber).

1. Abra el PDF usando la clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y llame al método [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) de la colección [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
1. La clase [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) absorbe el texto del documento y lo devuelve en el [método getText()](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/#getText--).

El siguiente fragmento de código le muestra cómo extraer texto de todas las páginas de un documento PDF.

```php

    // Crear un nuevo objeto Document desde el archivo PDF de entrada.
    $document = new Document($inputFile);

    // Crear un nuevo objeto TextAbsorber para extraer texto del documento.
    $textAbsorber = new TextAbsorber();

    // Extraer texto del documento.
    $textAbsorber->visit($document);

    // Obtener el contenido de texto extraído.
    $content = $textAbsorber->getText();

    // Guardar el texto extraído en el archivo de salida.
    file_put_contents($outputFile, $content);
```