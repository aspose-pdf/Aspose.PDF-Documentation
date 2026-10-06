---
title: Otimizar documento PDF para a web em PHP
linktitle: Otimizar documento PDF para a web em PHP
type: docs
weight: 60
url: /pt/java/optimize-pdf-document-for-the-web-in-php/
description: Aprenda como otimizar um documento PDF para desempenho web mais rápido e tamanho de arquivo reduzido em PHP com Aspose.PDF.
lastmod: "2026-10-06"
---
## Aspose.PDF - otimizar PDF para web

Para otimizar o documento PDF para a web usando **Aspose.PDF Java for PHP**, basta invocar o método **optimize_web** de  **Optimize** class.

Código PHP

```php

 public static function optimize_web($dataDir=null)

{

    # Open a pdf document.

    $doc = new Document($dataDir . "input1.pdf");

    # Optimize for web

    $doc->optimize();

    #Save output document

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "Optimized PDF for the Web, please check output file." . PHP_EOL;

}В В В
```

**Baixar Código em Execução**

Download **Otimizar PDF para Web (Aspose.PDF)** de qualquer um dos sites de código social abaixo mencionados:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)
