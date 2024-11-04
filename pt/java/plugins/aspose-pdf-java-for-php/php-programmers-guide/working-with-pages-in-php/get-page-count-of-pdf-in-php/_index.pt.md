---
title: Obter Contagem de Páginas de PDF em PHP
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Obter Contagem de Páginas

Para obter a contagem de páginas de um documento PDF usando **Aspose.PDF Java para PHP**, simplesmente invoque a classe **GetNumberOfPages**.

Código PHP

```php

# Criar documento PDF

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "Contagem de Páginas:" . $page_count . PHP_EOL;

```

**Baixar Código em Execução**

Baixe **Obter Contagem de Páginas (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)