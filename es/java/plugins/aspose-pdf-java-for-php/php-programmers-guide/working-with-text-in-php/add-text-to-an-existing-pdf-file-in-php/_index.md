---
title: Agregar texto a un archivo PDF existente en PHP
linktitle: Agregar texto a un archivo PDF existente en PHP
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-php/
description: Aprenda a agregar texto nuevo a un documento PDF existente en PHP usando Aspose.PDF para mejorar el contenido.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Agregar texto



Para agregar una cadena de texto en un documento PDF usando **Aspose.PDF Java para PHP**, simplemente invoque el módulo **AddText**.

Código PHP


```php

# Instantiate Document object
$doc = new Document($dataDir . 'input1.pdf');

# get particular page
$pdf_page = $doc->getPages()->get_Item(1);

# create text fragment
$text_fragment = new TextFragment("main text");
$text_fragment->setPosition(new Position(100, 600));

$font_repository = new FontRepository();
$color = new Color();

# set text properties
$text_fragment->getTextState()->setFont($font_repository->findFont("Verdana"));
$text_fragment->getTextState()->setFontSize(14);

# create TextBuilder object
$text_builder = new TextBuilder($pdf_page);

# append the text fragment to the PDF page
$text_builder->appendText($text_fragment);

# Save PDF file
$doc->save($dataDir . "Text_Added.pdf");

print "Text added successfully" . PHP_EOL;

```


**Descargar código de ejecución**



Descargue **Agregar texto (Aspose.PDF)**В desde cualquiera de los sitios de codificación social mencionados a continuación:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)
