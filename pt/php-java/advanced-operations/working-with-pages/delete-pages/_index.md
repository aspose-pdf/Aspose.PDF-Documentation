---
title: Excluir Páginas de PDF programaticamente
linktitle: Excluir Páginas de PDF
type: docs
weight: 40
url: /pt/php-java/delete-pages/
description: Você pode excluir páginas do seu arquivo PDF usando PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Excluir Página de Arquivo PDF

1. Chame o método delete e especifique o índice da página
1. Chame o método save para salvar o arquivo PDF atualizado
O trecho de código a seguir mostra como excluir uma página específica do arquivo PDF usando PHP.

```php

    // Abrir documento
    $document = new Document($inputFile);      

    $pages = $document->getPages();

    // Excluir uma página específica
    $pages->delete(2);

    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();
```