---
title: Adicionar Imagem a um Arquivo PDF Existente 
linktitle: Adicionar Imagem
type: docs
weight: 10
url: /php-java/add-image-to-existing-pdf-file/
description: Esta seção descreve como adicionar uma imagem a um arquivo PDF existente usando PHP.
lastmod: "2024-06-05"
---

Cada página PDF contém propriedades de Recursos e Conteúdos. Recursos podem ser imagens e formulários, por exemplo, enquanto o conteúdo é representado por um conjunto de operadores PDF. Cada operador tem seu nome e argumento. Este exemplo usa operadores para adicionar uma imagem a um arquivo PDF.

Para adicionar uma imagem a um arquivo PDF existente:

- Crie um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) e abra o documento PDF de entrada.
- Obtenha a página na qual você deseja adicionar uma imagem.
- Adicione uma nova página ao documento.
- Defina o tamanho da página para 1190.7 x 841.995.
- Adicione uma imagem à página usando o arquivo de imagem especificado e a caixa de corte da página.
- Salve o arquivo.

O trecho de código a seguir mostra como adicionar a imagem em um documento PDF.

```php

    // Abra o documento usando o arquivo de entrada especificado.
    $document = new Document($inputFile);
    
    // Adicione uma nova página ao documento.
    $page = $document->getPages()->add();
    
    // Defina o tamanho da página para 1190.7 x 841.995.
    $page->setPageSize(1190.7, 841.995);
    
    // Adicione uma imagem à página usando o arquivo de imagem especificado e a caixa de corte da página.
    $page->addImage($imageFileName, $page->getCropBox());
    
    // Salve o documento modificado no arquivo de saída especificado.
    $document->save($outputFile);
    
    // Feche o documento.
    $document->close();
```