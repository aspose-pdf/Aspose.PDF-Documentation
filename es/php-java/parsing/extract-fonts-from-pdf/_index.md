---
title: Extraer fuentes de PDF 
linktitle: Extraer fuentes
type: docs
weight: 30
url: es/php-java/extract-fonts-from-pdf/
description: Cómo extraer fuentes de PDF usando Aspose.PDF para PHP
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

En caso de que desees obtener todas las fuentes de un documento PDF, puedes usar el método [Document.IDocumentFontUtilities.getAllFonts()](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getFontUtilities--) proporcionado en la clase Document. Por favor, revisa el siguiente fragmento de código para obtener todas las fuentes de un documento PDF existente:

```php

    // Crear una nueva instancia de la clase License y establecer el archivo de licencia.
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // Establecer la ruta al directorio que contiene el documento PDF y el directorio de salida para las fuentes extraídas.
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.pdf";

    // Inicializar la variable de datos de respuesta.
    $responseData = "";

    try {
        // Cargar el documento PDF.
        $document = new Document($inputFile);

        // Obtener todas las fuentes utilizadas en el documento PDF.
        $fonts = java_values($document->getFontUtilities()->getAllFonts());

        // Iterar sobre cada fuente y guardarla como un archivo de fuente TrueType.
        foreach ($fonts as $font) {
            // Establecer la ruta de archivo de salida para el archivo de fuente.
            $outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . $font->getFontName() . ".ttf";

            // Crear un objeto FileOutputStream para escribir el archivo de fuente.
            $fontStream = new java("java.io.FileOutputStream", $outputFile);

            // Guardar la fuente como un archivo de fuente TrueType.
            $font->save($fontStream);

            // Cerrar el flujo de fuente.
            $fontStream->close();

            // Añadir el nombre de la fuente a los datos de respuesta.
            $responseData = $responseData . $font->getFontName() . ", ";
        }

        // Cerrar el documento PDF.
        $document->close();
    }
```