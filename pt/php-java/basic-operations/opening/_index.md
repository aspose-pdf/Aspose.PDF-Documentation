---
title: Abrir Documento PDF
linktitle: Abrir
type: docs
weight: 20
url: /pt/php-java/open-pdf-document/
description: Aprenda como abrir um arquivo PDF com Aspose.PDF para PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Abrir documento PDF existente

Arquivos PDF ou arquivos em formato de documento portátil se tornaram o padrão universal para troca de documentos. Eles são amplamente usados para salvar o formato de um documento. No entanto, trabalhar com arquivos PDF usando linguagens de programação como PHP via Java pode ser um pouco difícil. Este artigo apresenta a biblioteca Aspose.PDF para PHP via Java, que permite abrir seu PDF de forma rápida e fácil.

```php

    $document = new Document($inputFile,"mypassword");
    $responseData = "O documento foi aberto com sucesso. Tamanho do arquivo: " . filesize($inputFile);
```