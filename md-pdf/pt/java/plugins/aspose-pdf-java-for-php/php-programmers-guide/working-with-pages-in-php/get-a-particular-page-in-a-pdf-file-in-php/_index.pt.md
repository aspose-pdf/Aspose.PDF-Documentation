---
title: Obter uma Página Específica em um Arquivo PDF em PHP
type: docs
weight: 30
url: /java/obter-uma-pagina-especifica-em-um-arquivo-pdf-em-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obter Página

Para obter uma Página Específica em um documento PDF usando **Aspose.PDF Java for Ruby**, basta invocar a classe **GetPage**.

Código Ruby

```php

# Abrir o documento alvo
$pdf = new Document($dataDir . 'input1.pdf');

# obter a página em um índice específico da Coleção de Páginas
$pdf_page = $pdf->getPages()->get_Item(1);

# criar um novo objeto Documento
$new_document = new Document();

# adicionar página à coleção de páginas do novo objeto documento
$new_document->getPages()->add($pdf_page);

# salvar o arquivo PDF recém-gerado
$new_document->save($dataDir . "output.pdf");

print "Processo concluído com sucesso!";

```

## Baixar Código em Execução

Baixe **Obter Página (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)