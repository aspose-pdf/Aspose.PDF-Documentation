---
title: Salvar Documento PDF 
linktitle: Salvar
type: docs
weight: 30
url: /pt/php-java/save-pdf-document/
description: Aprenda como salvar arquivo PDF com Aspose.PDF para PHP via biblioteca Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Salvar documento PDF no sistema de arquivos

Você pode salvar o documento PDF criado ou manipulado no sistema de arquivos usando o método save da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

```php

    $document = new Document($inputFile);        
    $document->save($outputFile);
```