---
title: Añadir Texto a un archivo PDF existente en PHP
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Añadir Texto

Para añadir una cadena de texto en un documento Pdf usando **Aspose.PDF Java para PHP**, simplemente invoca el módulo **AddText**.

Código PHP

```php

# Instanciar el objeto Document
$doc = new Document($dataDir . 'input1.pdf');

# obtener una página en particular
$pdf_page = $doc->getPages()->get_Item(1);

# crear fragmento de texto
$text_fragment = new TextFragment("texto principal");
$text_fragment->setPosition(new Position(100, 600));

$font_repository = new FontRepository();
$color = new Color();

# establecer propiedades del texto
$text_fragment->getTextState()->setFont($font_repository->findFont("Verdana"));
$text_fragment->getTextState()->setFontSize(14);

# crear objeto TextBuilder
$text_builder = new TextBuilder($pdf_page);

# añadir el fragmento de texto a la página PDF
$text_builder->appendText($text_fragment);

# Guardar archivo PDF
$doc->save($dataDir . "Text_Added.pdf");

print "Texto añadido exitosamente" . PHP_EOL;

```


**Descargar Código en Ejecución**

Descargar **Agregar Texto (Aspose.PDF)** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)