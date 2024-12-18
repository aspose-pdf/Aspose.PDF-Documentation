---
title: Extraer Texto de Todas las Páginas de un Documento PDF en PHP
type: docs
weight: 30
url: /es/java/extract-text-from-all-the-pages-of-a-pdf-document-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Extraer Texto de Todas las Páginas

Para extraer texto de todas las páginas de un documento PDF usando **Aspose.PDF Java para PHP**, simplemente invoque el módulo **ExtractTextFromAllPages**.
Código PHP

```php

# Abrir el documento objetivo
$pdf = new Document($dataDir . 'input1.pdf');

# crear un objeto TextAbsorber para extraer texto
$text_absorber = new TextAbsorber();

# aceptar el absorvedor para todas las páginas
$pdf->getPages()->accept($text_absorber);

# Para extraer texto de una página específica del documento, necesitamos especificar la página particular usando su índice contra el método accept(..).
# aceptar el absorvedor para una página PDF particular
# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

# obtener el texto extraído
$extracted_text = $text_absorber->getText();

# crear un escritor y abrir el archivo
$writer = new FileWriter(new File($dataDir . "extracted_text.out.txt"));
$writer->write($extracted_text);
# escribir una línea de texto en el archivo
# tw.WriteLine(extractedText);
# cerrar el flujo
$writer->close();

print "Texto extraído exitosamente. Verifica el archivo de salida." . PHP_EOL;

```


**Descargar Código en Ejecución**

Descargar **Extraer Texto de Todas las Páginas (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/ExtractTextFromAllPages.php)