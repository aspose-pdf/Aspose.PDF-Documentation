---
title: Alterar Tamanho da Página do PDF Programaticamente
linktitle: Alterar Tamanho da Página do PDF
type: docs
weight: 50
url: /pt/php-java/change-page-size/
description: Alterar o tamanho da página do seu arquivo PDF usando PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Alterar Tamanho da Página do PDF

Aspose.PDF para PHP via Java permite que você altere o tamanho da página do PDF com simples linhas de código em suas aplicações Java. Este tópico explica como atualizar/alterar as dimensões (tamanho) da página de um arquivo PDF existente.

A classe [Page](https://reference.aspose.com/pdf//java/com.aspose.pdf/page) contém o método SetPageSize(...) que permite definir o tamanho da página. O trecho de código abaixo atualiza as dimensões da página em alguns passos fáceis:

1. Carregue o arquivo PDF de origem.
1. Obtenha as páginas no objeto [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/pagecollection).
1. Obtenha uma determinada página.
1. Chame o método setPageSize(..) para atualizar suas dimensões.

1. Chame o método save(..) da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) para gerar o arquivo PDF com as dimensões de página atualizadas.

O snippet de código a seguir mostra como alterar as dimensões da página PDF para o tamanho A4.

```php

    // Abrir documento
    $document = new Document($inputFile);
      
    // Obter coleção de páginas
    $pageCollection = $document->getPages();

    // Obter página específica
    $page = $pageCollection->get_Item(1);

    // Definir o tamanho da página como A4 (11.7 x 8.3 in) e no Aspose.Pdf, 1 polegada = 72 pontos
    // Então as dimensões A4 em pontos serão (842.4, 597.6)
    $page.setPageSize(597.6, 842.4);

    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();
```

## Obter Tamanho da Página PDF

Você pode ler o tamanho da página PDF de um arquivo PDF existente usando o Aspose.PDF para PHP via Java. O exemplo de código a seguir mostra como ler as dimensões da página PDF usando PHP.

```php

    // Abrir documento
    $document = new Document($inputFile);
      
    // Adiciona uma página em branco ao documento PDF
    $page = $document->getPages()->size() > 0 
        ? $document->getPages()->get_Item(1) 
        : $document->getPages()->add();
    
    // Obter informações de altura e largura da página
    $responseData = $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // Rotacionar página em um ângulo de 90 graus
    $rotation = new Rotation();
    $page->setRotate($rotation->getOn90());

    // Obter informações de altura e largura da página
    $responseData = $responseData . $page->getPageRect(true)->getWidth() . ":" . $page->getPageRect(true)->getHeight();
    
    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();
```