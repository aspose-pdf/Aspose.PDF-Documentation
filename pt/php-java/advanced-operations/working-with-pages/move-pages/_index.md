---
title: Mover Páginas de PDF
linktitle: Mover Páginas de PDF
type: docs
weight: 20
url: pt/php-java/move-pages/
description: Tente mover páginas para a localização desejada ou para o final de um arquivo PDF usando Aspose.PDF para PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Movendo uma Página de um Documento PDF para Outro

Este tópico explica como mover uma página de um documento PDF para o final de outro documento usando PHP.
Para mover uma página devemos:

1. Criar um objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) com o arquivo PDF de origem
1. Criar um objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) com o arquivo PDF de destino
1. Adicionar a página ao documento de saída. Salvar o arquivo de saída
1. Excluir a página do documento de entrada. Salvar o documento de entrada modificado
1. Fechar os documentos
1. Salvar e fechar o documento de saída

O seguinte trecho de código mostra como mover uma página.

```php

    // Abrir documento
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $page = $document->getPages()->get_Item(2);
    $dstDocument->getPages()->add($page);

    // Salvar arquivo de saída
    $dstDocument->save($srcFileName);
    $document->getPages()->delete(2);
    $document->save($dstFileName);
    $document->close();
    $dstDocument->close();
  
    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();
```


## Movendo um Conjunto de Páginas de um Documento PDF para Outro

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) com o arquivo PDF de origem.
1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) com o arquivo PDF de destino.
1. Defina as páginas a serem copiadas do documento de entrada para o documento de saída.
1. Execute um loop através do array:
    1. Obtenha a página no índice especificado do documento de entrada.
    1. Adicione a página ao documento de destino.
1. Salve o PDF de saída usando o método Save.
1. Exclua a página no documento de origem usando o array.
1. Salve o PDF de origem usando o método Save.

O seguinte trecho de código mostra como inserir uma página vazia no final de um arquivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $pages = [1, 3 ];
    foreach ($pages as $pageIndex) {
      $page = $document->getPages()->get_Item($pageIndex);
      $dstDocument->getPages()->add(page);
    }
    // Salvar arquivos de saída
    $dstDocument->save($srcFileName);
    $document->getPages()->delete($pages);

    $document->save(dstFileName);

    $document->close();
    $dstDocument->close();  
```


## Movendo uma Página para uma nova localização no Documento PDF atual

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) com o arquivo PDF de origem.
1. Obtenha a Página da coleção [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection).
1. Adicione a página à nova localização.
1. Exclua a página no índice 2.
1. Salve o PDF de saída usando o método save.

```php

    // Abrir documento
    $document = new Document($inputFile);
        
    $pageCollection = $document->getPages();
    
    $page = $pageCollection->get_Item(2);
    $pageCollection->add(page);
    $pageCollection->delete(2);

    // Salvar arquivo de saída
    $document->save($outputFile);
    $document->close();      
```