---
title: Excluir uma Página Específica do Arquivo PDF em PHP
type: docs
weight: 20
url: pt/java/delete-a-particular-page-from-the-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Excluir Página

Para excluir uma Página Específica do documento PDF usando **Aspose.PDF Java for PHP**, simplesmente invoque a classe **DeletePage**.

Código PHP

```php

# Abra o documento alvo
$pdf = new Document($dataDir . 'input1.pdf');

# exclua uma página específica
$pdf->getPages()->delete(2);

# salve o arquivo PDF recém-gerado
$pdf->save($dataDir . "output.pdf");

print "Página excluída com sucesso!";

```

**Download em Execução**

Baixe **Excluir Página (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)