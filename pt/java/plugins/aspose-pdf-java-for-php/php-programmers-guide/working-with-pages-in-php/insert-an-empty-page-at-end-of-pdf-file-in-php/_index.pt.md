---
title: Inserir uma Página Vazia no Final do Arquivo PDF em PHP
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Inserir uma Página Vazia no Final do Arquivo PDF

Para inserir uma página vazia no final do documento PDF usando **Aspose.PDF Java para PHP**, basta invocar a classe **InsertEmptyPageAtEndOfFile**.

Código PHP

```php

# Abra o documento alvo
$pdf = new Document($dataDir . 'input1.pdf');

# insira uma página vazia em um PDF
$pdf->getPages()->add();

# Salve o arquivo de saída concatenado (o documento alvo)
$pdf->save($dataDir . "output.pdf");

print "Página vazia adicionada com sucesso!" . PHP_EOL;

```

## Baixar Código em Execução

Baixe **Inserir uma Página Vazia no Final do Arquivo PDF (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)