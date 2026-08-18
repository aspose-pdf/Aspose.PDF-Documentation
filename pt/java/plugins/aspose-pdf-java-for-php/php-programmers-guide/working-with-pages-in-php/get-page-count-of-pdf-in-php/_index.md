---
title: Obtenha contagem de páginas de PDF em PHP
linktitle: Obtenha contagem de páginas de PDF em PHP
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-php/
description: Descubra como recuperar a contagem total de páginas de um documento PDF em PHP usando Aspose.PDF para análise de documentos.
lastmod: "2026-06-09"
---
## Aspose.PDF - Obter contagem de páginas

Para obter a contagem de páginas do documento PDF usando **Aspose.PDF Java para PHP**, basta invocar a classe **GetNumberOfPages**.

Código PHP

```php

# Create PDF document

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "Page Count:" . $page_count . PHP_EOL;

```

**Baixar código em execução**

Baixe **Obter contagem de páginas (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)
