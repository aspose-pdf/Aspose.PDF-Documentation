---
title: Adicionar String HTML usando DOM em PHP
linktitle: Adicionar String HTML usando DOM em PHP
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-php/
description: Explore como adicionar conteúdo HTML a um documento PDF usando o DOM em PHP com Aspose.PDF para criação de documentos sofisticados.
lastmod: "2026-06-09"
---
## Aspose.PDF - Adicionar HTML

Para adicionar uma string HTML em um documento PDF usando **Aspose.PDF Java para PHP**, basta invocar o módulo **AddHtml**.

Código PHP

```php
# Instantiate Document object
$doc = new Document();

# Add a page to pages collection of PDF file
$page = $doc->getPages()->add();

# Instantiate HtmlFragment with HTML contents
$title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");

# set MarginInfo for margin details
$margin = new MarginInfo();
$margin->setBottom(10);
$margin->setTop(200);

# Set margin information
$title->setMargin($margin);

# Add HTML Fragment to paragraphs collection of page
$page->getParagraphs()->add($title);

# Save PDF file
$doc->save($dataDir . "html.output.pdf");

print "HTML added successfully" . PHP_EOL;

```

**Baixar código em execução**

Baixe **Adicione HTML (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)
