---
title: Adicione texto a um arquivo PDF existente em PHP
linktitle: Adicione texto a um arquivo PDF existente em PHP
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-php/
description: Aprenda como adicionar novo texto a um documento PDF existente em PHP usando Aspose.PDF para aprimorar o conteúdo.
lastmod: "2026-06-09"
---
## Aspose.PDF - Adicionar texto

Para adicionar uma string de texto em um documento PDF usando **Aspose.PDF Java para PHP**, basta invocar o módulo **AddText**.

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

**Baixar código em execução**

Baixe **Adicionar texto (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)
