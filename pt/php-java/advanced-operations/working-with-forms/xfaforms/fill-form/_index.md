---
title: Preencher AcroForms
linktitle: Preencher AcroForms
type: docs
weight: 20
url: /pt/php-java/fill-form/
description: Esta seção explica como preencher um campo de formulário em um documento PDF com Aspose.PDF para PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Documentos PDF são maravilhosos, e realmente o tipo de arquivo preferido, para criar formulários.

Aspose.PDF para PHP via Java permite que você preencha um campo de formulário, obtenha o campo da coleção de Formulários do objeto Document.

Vamos dar uma olhada no exemplo a seguir de como resolver esta tarefa:

```php

    // Carregar formulário XFA
    $document = new Document($inputFile);
    
    // Obter nomes dos campos do formulário XFA
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // Definir valores dos campos        
    $document->getForm()->getXFA()->set_Item($names[0],"Campo 0");
    $document->getForm()->getXFA()->set_Item($names[1],"Campo 1");
        
    // Salvar o documento atualizado
    $document->save($outputFile);
    
    // Salvar PDF modificado    
    $document->close();
```