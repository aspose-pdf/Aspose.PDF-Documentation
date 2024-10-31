---
title: Trabalhando com Metadados de Arquivos PDF 
linktitle: Metadados de Arquivos PDF
type: docs
weight: 140
url: /php-java/pdf-file-metadata/
description: Esta seção explica como obter informações de arquivos PDF, como obter Metadados XMP de um arquivo PDF, definir Informações de Arquivo PDF.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obter Informações de Arquivo PDF

Para obter informações específicas do arquivo sobre um arquivo PDF, primeiro obtenha o objeto 'docInfo' usando a classe [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) [getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--). Uma vez que o objeto 'docInfo' é recuperado, você pode obter os valores das propriedades individuais.

O trecho de código a seguir mostra como definir informações de arquivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);
    
    // Obter informações do documento
    $docInfo = $document->getInfo();

    // Mostrar informações do documento
    $responseData1 = "Autor: " . $docInfo->getAuthor() . ", ";
    $responseData2 = "Data de Criação: " . $docInfo->getCreationDate() . ", ";
    $responseData3 = "Palavras-chave: " . $docInfo->getKeywords() . ", ";
    $responseData4 = "Data de Modificação: " . $docInfo->getModDate() . ", ";
    $responseData5 = "Assunto: " . $docInfo->getSubject() . ", ";
    $responseData6 = "Título: " . $docInfo->getTitle() . "";

    $document->close();
```