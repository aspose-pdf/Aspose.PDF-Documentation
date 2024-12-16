---
title: Insira uma Página Vazia em um Arquivo PDF em PHP
type: docs
weight: 70
url: /pt/java/insert-an-empty-page-into-a-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Inserir uma Página Vazia

Para inserir uma página vazia em um documento Pdf usando **Aspose.PDF Java para PHP**, basta invocar a classe **InsertEmptyPage**.

Código PHP

```php

# Abra o documento de destino
$pdf = new Document($dataDir . 'input1.pdf');

# insira uma página vazia em um PDF
$pdf->getPages()->insert(1);

# Salve o arquivo de saída concatenado (o documento de destino)
$pdf->save($dataDir . "output.pdf");

print "Página vazia adicionada com sucesso!";

```

**Baixar Código em Execução**

Baixar **Inserir uma Página Vazia (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)