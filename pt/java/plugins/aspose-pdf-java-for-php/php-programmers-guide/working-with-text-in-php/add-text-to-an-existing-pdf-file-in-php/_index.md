---
title: Adicionar Texto a um arquivo PDF existente em PHP
type: docs
weight: 20
url: pt/java/add-text-to-an-existing-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Adicionar Texto

Para adicionar uma string de texto em um documento Pdf usando **Aspose.PDF Java for PHP**, simplesmente invoque o módulo **AddText**.

Código PHP

```php

# Instanciar objeto Document
$doc = new Document($dataDir . 'input1.pdf');

# obter página específica
$pdf_page = $doc->getPages()->get_Item(1);

# criar fragmento de texto
$text_fragment = new TextFragment("texto principal");
$text_fragment->setPosition(new Position(100, 600));

$font_repository = new FontRepository();
$color = new Color();

# definir propriedades do texto
$text_fragment->getTextState()->setFont($font_repository->findFont("Verdana"));
$text_fragment->getTextState()->setFontSize(14);

# criar objeto TextBuilder
$text_builder = new TextBuilder($pdf_page);

# anexar o fragmento de texto à página PDF
$text_builder->appendText($text_fragment);

# Salvar arquivo PDF
$doc->save($dataDir . "Text_Added.pdf");

print "Texto adicionado com sucesso" . PHP_EOL;

```


**Baixar Código em Execução**

Baixar **Adicionar Texto (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)