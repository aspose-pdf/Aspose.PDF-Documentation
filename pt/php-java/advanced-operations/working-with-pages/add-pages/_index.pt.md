---
title: Adicionar Páginas em PDF
linktitle: Adicionar Páginas
type: docs
weight: 10
url: /php-java/add-pages/
description: Este artigo ensina como inserir (adicionar) uma página na localização desejada em um arquivo PDF. Aprenda como mover, remover (excluir) páginas de um arquivo PDF usando PHP.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar ou Inserir Página em um Arquivo PDF

Aspose.PDF para PHP via Java permite que você insira uma página em um documento PDF em qualquer local do arquivo, bem como adicione páginas ao final de um arquivo PDF. Você precisa passar a localização onde deseja inserir a página em branco para o método de inserção. Esta seção mostra como adicionar páginas a um PDF com Aspose.PDF para PHP via Java.

### Inserir Página Vazia em um Arquivo PDF na Localização Desejada

O seguinte trecho de código mostra como inserir uma página em branco em um arquivo PDF:

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) com o arquivo PDF de entrada.
1. Adicione a página e insira-a em um PDF.

1. Salve o PDF de saída usando o método Save.

O trecho de código a seguir mostra como inserir uma página em um arquivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Adicionar página
    $document->getPages()->add();

    // Inserir uma página vazia em um PDF
    $document->getPages()->insert(2);

    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();
```

No exemplo acima, adicionamos uma página vazia com parâmetros padrão. Se você precisar fazer com que o tamanho da página seja o mesmo de outra página no documento, você deve adicionar algumas linhas de código:

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Adicionar página
    $page1 = $document->getPages()->add();

    // Inserir uma página vazia em um PDF
    $page2 = $document->getPages()->insert(2);

    // copiar parâmetros da página da página 1
    $page2->setCropBox($page1->getCropBox());
    $page2->setMediaBox($page1->getMediaBox());
    $page2->setTrimBox($page1->getTrimBox());
    $page2->setArtBox($page1->getArtBox());
    $page2->setBleedBox($page1->getBleedBox());
    
    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();
```


### Adicionar uma Página em Branco no Final de um Arquivo PDF

Às vezes, você quer garantir que um documento termine em uma página em branco. Este tópico explica como inserir uma página em branco no final do documento PDF.

Para inserir uma página em branco no final de um arquivo PDF:

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) com o arquivo PDF de entrada.
1. Adicione uma página e insira-a em um PDF.
1. Salve o PDF de saída usando o método save.

O snippet de código a seguir mostra como inserir uma página em branco no final de um arquivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);

    // Adicionar página
    $document->getPages()->add();

    // Inserir uma página em branco em um PDF
    $document->getPages()->insert(2);

    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();
```