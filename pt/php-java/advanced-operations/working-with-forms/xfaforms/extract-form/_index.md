---
title: Extrair Formulário XFA
linktitle: Extrair Formulário XFA
type: docs
weight: 30
url: pt/php-java/extract-form/
description: Esta seção explica como extrair formulários do seu documento PDF com Aspose.PDF para PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obter Valor de um Campo de Formulário do Documento PDF

O [método getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) do campo de formulário permite que você obtenha o valor de um campo específico.

Para obter o valor, obtenha o campo de formulário da coleção Form do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Este exemplo seleciona um [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) e recupera seu valor usando o [método getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```php

    // Carregar formulário XFA
    $document = new Document($inputFile);
    
    // Obter nomes dos campos do formulário XFA
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // Obter valores dos campos
    $document->getForm()->getXFA()->get_Item($names[0]);
    $document->getForm()->getXFA()->get_Item($names[1]);
    
    // Salvar PDF modificado    
    $document->close();
```