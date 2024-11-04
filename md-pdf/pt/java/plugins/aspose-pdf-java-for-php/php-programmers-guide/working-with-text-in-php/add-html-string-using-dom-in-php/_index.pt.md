---
title: Adicionar String HTML usando DOM em PHP
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Adicionar HTML

Para adicionar uma string HTML em um documento Pdf usando **Aspose.PDF Java para PHP**, simplesmente invoque o módulo **AddHtml**.

Código PHP

```php
# Instanciar objeto Document
$doc = new Document();

# Adicionar uma página à coleção de páginas do arquivo PDF
$page = $doc->getPages()->add();

# Instanciar HtmlFragment com conteúdos HTML
$title = new HtmlFragment("<fontsize=10><b><i>Tabela</i></b></fontsize>");

# Definir MarginInfo para detalhes de margem
$margin = new MarginInfo();
$margin->setBottom(10);
$margin->setTop(200);

# Definir informações de margem
$title->setMargin($margin);

# Adicionar Fragmento HTML à coleção de parágrafos da página
$page->getParagraphs()->add($title);

# Salvar arquivo PDF
$doc->save($dataDir . "html.output.pdf");

print "HTML adicionado com sucesso" . PHP_EOL;

```

**Baixar Código em Execução**

Baixar **Adicionar HTML (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)