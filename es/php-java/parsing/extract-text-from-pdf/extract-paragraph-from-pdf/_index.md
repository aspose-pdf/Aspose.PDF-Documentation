---
title: Extraer Párrafo de PDF
linktitle: Extraer Párrafo
type: docs
weight: 20
url: es/php-java/extract-paragraph-from-pdf/
description: Este artículo describe cómo usar ParagraphAbsorber, una herramienta especial en Aspose.PDF para extraer texto de documentos PDF.
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraer Texto de documento PDF en forma de Párrafos

Podemos obtener texto de un documento PDF buscando un texto particular (usando "texto plano" o "expresiones regulares") de una sola página o de todo el documento, o podemos obtener el texto completo de una sola página, rango de páginas o documento completo. Sin embargo, en algunos casos, se requiere extraer párrafos de un documento PDF o texto en forma de párrafos. Hemos implementado la funcionalidad para buscar secciones y párrafos en el texto de las páginas del documento PDF. Hemos introducido la Clase ParagraphAbsorber (como TextFragmentAbsorber y TextAbsorber), que se puede usar para extraer párrafos de documentos PDF.

### Iterando a través de la colección de párrafos y obteniendo su texto

```php

// Abrir un archivo PDF existente
$document = new Document($inputFile);
// Instanciar ParagraphAbsorber
$absorber = new ParagraphAbsorber();
$absorber->visit($document);
$responseData = "";

foreach ($absorber->getPageMarkups() as $markup) {
    $i = 1;

    foreach ($markup->getSections() as $section) {
        $j = 1;

        foreach ($section->getParagraphs() as $paragraph) {
            $paragraphText = "\r\n";

            foreach ($paragraph->getLines() as $line) {
                foreach ($line as $fragment) {
                    $paragraphText = $paragraphText . $fragment->getText();
                }
                $paragraphText = $paragraphText . "\r\n";
            }
            $paragraphText = $paragraphText . "\r\n";

            $responseData = $responseData . "Párrafo " . $j++ . " de la sección " . $i++ . " en la página" . ":" . markup->getNumber();
            $responseData = $responseData . $paragraphText;
            $j++;
        }
        $i++;
    }
}

// Guardar el texto extraído en el archivo de salida.
file_put_contents($outputFile, $responseData);
```