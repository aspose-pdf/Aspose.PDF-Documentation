---
title: Rotacionar Páginas de PDF programaticamente
linktitle: Rotacionar Páginas de PDF
type: docs
weight: 60
url: /pt/php-java/rotate-pages/
description: Mudar a orientação da página e ajustar o conteúdo da página para a nova orientação usando Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mudar a Orientação da Página

Este artigo descreve como atualizar ou mudar a orientação das páginas em um arquivo PDF existente.

Aspose.PDF para PHP via Java tem a funcionalidade de mudar a orientação da página de paisagem para retrato e vice-versa.

1. Abra o documento usando o arquivo de entrada especificado.
1. Obtenha todas as páginas do documento.
1. Itere através de cada página e defina a rotação para 90 graus.
1. Salve o documento modificado no arquivo de saída especificado.
1. Feche o documento.

```php

    // Abrir documento
    $document = new Document($inputFile);                
    $pages = $document->getPages();
    $pagesSize = java_values($pages->size());
       
    // Percorrer todas as páginas
    for ($pageCount = 1; $pageCount <= $pagesSize; $pageCount++) {
        $page = $pages->get_Item($pageCount);
       
        $page->setRotate((new Rotation())->On90);
    }

    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();
```