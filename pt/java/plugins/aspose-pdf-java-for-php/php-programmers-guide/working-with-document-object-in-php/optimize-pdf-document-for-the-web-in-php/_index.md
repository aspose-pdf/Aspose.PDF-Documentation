---
title: Otimizar Documento PDF para a Web em PHP
type: docs
weight: 60
url: /pt/java/optimize-pdf-document-for-the-web-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Otimizar PDF para Web

Para otimizar o documento PDF para a web usando **Aspose.PDF Java for PHP**, basta invocar o método **optimize_web** da classe **Optimize**.

Código PHP

```php

 public static function optimize_web($dataDir=null)

{

    # Abra um documento pdf.

    $doc = new Document($dataDir . "input1.pdf");

    # Otimizar para web

    $doc->optimize();

    #Salvar documento de saída

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "PDF otimizado para a Web, por favor, verifique o arquivo de saída." . PHP_EOL;

}    
```

**Baixar Código em Execução**

Baixar **Otimizar PDF para Web (Aspose.PDF)** de qualquer um dos sites de codificação social mencionados abaixo:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)