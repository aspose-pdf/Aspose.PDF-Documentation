---
title: Adicionar texto a um arquivo PDF existente em PHP
linktitle: Adicionar texto a um arquivo PDF existente em PHP
type: docs
weight: 20
url: /pt/java/add-text-to-an-existing-pdf-file-in-php/
description: Aprenda como adicionar novo texto a um documento PDF existente em PHP usando Aspose.PDF para aprimoramento de conteúdo.
lastmod: "2026-10-06"
---
## Aspose.PDF - Adicionar Texto

Para adicionar uma string de Texto em um documento Pdf usando **Aspose.PDF Java for PHP**, basta invocar o módulo **AddText**.

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

**Download do Código em Execução**

Baixar\u0412\u00A0**Adicionar Texto (Aspose.PDF)**\u0412\u00A0de\u0412\u00A0qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)
