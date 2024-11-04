---
title: Criar ou Adicionar Tabela em PDF 
linktitle: Criar ou Adicionar Tabela
type: docs
weight: 10
url: /php-java/add-table-in-existing-pdf-document/
description: Aprenda como criar ou adicionar tabela a um documento PDF, aplicando estilo de célula, dividindo a tabela em páginas e personalizando as linhas e colunas, etc.
lastmod: "2024-05-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adicionando Tabela em Documento PDF Existente

Para adicionar uma tabela a um arquivo PDF existente com Aspose.PDF para PHP, siga os seguintes passos:

1. Carregue o arquivo fonte.
1. Inicialize uma tabela
1. Defina a cor da borda da tabela como LightGray
1. Defina a borda para as células da tabela
1. Crie um loop para adicionar 10 linhas
1. Adicione o objeto tabela à primeira página do documento de entrada
1. Salve o arquivo.

Os seguintes trechos de código mostram como adicionar texto em um arquivo PDF existente.

```php

    // Abrir documento
    $document = new Document($inputFile);        
    // Inicializa uma nova instância da Tabela
    $table = new Table();
    $colors= new Color();
    // Defina a cor da borda da tabela como LightGray
    $borderSide = new BorderSide();
    $borderInfo = new BorderInfo($borderSide->All, 0.5, $colors->getLightGray());
    $table->setBorder($borderInfo);
    // defina a borda para as células da tabela
    $table->setDefaultCellBorder($borderInfo);
    // crie um loop para adicionar 10 linhas
    for ($row_count = 1; $row_count < 10; $row_count++) {
        // adicione linha à tabela
        $row = $table->getRows()->add();
        // adicione células à tabela
        $row->getCells()->add("Coluna (" . $row_count . ", 1)");
        $row->getCells()->add("Coluna (" . $row_count . ", 2)");
        $row->getCells()->add("Coluna (" . $row_count . ", 3)");
    }
    // Adicione o objeto tabela à primeira página do documento de entrada
    $document->getPages()->add()->getParagraphs()->add($table);

    // Salve o documento PDF resultante.    
    $document->save($outputFile);
    $document->close();
```