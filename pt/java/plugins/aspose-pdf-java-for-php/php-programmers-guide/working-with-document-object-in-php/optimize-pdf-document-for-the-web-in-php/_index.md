---
title: Otimize documentos PDF para a Web em PHP
linktitle: Otimize documentos PDF para a Web em PHP
type: docs
weight: 60
url: /java/optimize-pdf-document-for-the-web-in-php/
description: Aprenda como otimizar um documento PDF para desempenho mais rápido na web e tamanho de arquivo reduzido em PHP com Aspose.PDF.
lastmod: "2026-06-09"
---
## Aspose.PDF - Otimize PDF para Web

Para otimizar documentos PDF para a web usando **Aspose.PDF Java para PHP**, basta invocar o método **optimize_web** da classe **Optimize**.

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

**Baixar código em execução**

Baixe **Optimize PDF for Web (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)
