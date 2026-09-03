---
title: Extraer texto de todas las páginas de un documento PDF en PHP
linktitle: Extraer texto de todas las páginas de un documento PDF en PHP
type: docs
weight: 30
url: /es/java/extract-text-from-all-the-pages-of-a-pdf-document-in-php/
description: Descubra cómo extraer texto de todas las páginas de un documento PDF en PHP usando Aspose.PDF para análisis de texto.
lastmod: "2026-09-03"
---
## Aspose.PDF - Extraer texto de todas las páginas

Para extraer TextrFrom todas las páginas del documento Pdf usando **Aspose.PDF Java for PHP**, simplemente invoque el módulo **ExtractTextFromAllPages**.
Código PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# create TextAbsorber object to extract text
$text_absorber = new TextAbsorber();

# accept the absorber for all the pages
$pdf->getPages()->accept($text_absorber);

# In order to extract text from specific page of document, we need to specify the particular page using its index against accept(..) method.
# accept the absorber for particular PDF page
# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

#get the extracted text
$extracted_text = $text_absorber->getText();

# create a writer and open the file
$writer = new FileWriter(new File($dataDir . "extracted_text.out.txt"));
$writer->write($extracted_text);
# write a line of text to the file
# tw.WriteLine(extractedText);
# close the stream
$writer->close();

print "Text extracted successfully. Check output file." . PHP_EOL;

```

**Descargar Código en Ejecución**

DescargarВ **Extraer texto de todas las páginas (Aspose.PDF)**В deВ cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/ExtractTextFromAllPages.php)
