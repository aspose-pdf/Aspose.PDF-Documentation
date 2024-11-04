---
title: Preencher AcroForms
linktitle: Preencher AcroForms
type: docs
weight: 20
url: /php-java/fill-form/
description: Esta seção explica como preencher um campo de formulário em um documento PDF com Aspose.PDF para PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Documentos PDF são maravilhosos, e realmente o tipo de arquivo preferido, para criar Formulários.

Aspose.PDF para PHP via Java permite que você preencha um campo de formulário, obtenha o campo da coleção de Formulários do objeto Document.

Vamos ver o exemplo a seguir de como resolver esta tarefa:

```php

    // Abrir documento
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    
    // Obter um campo    
    $textBoxField = $document->getForm()->get("textbox1");

    // Modificar valor do campo
    $textBoxField->setValue("Valor a ser preenchido no campo");
        
    // Salvar documento atualizado
    $document->save($outputFile);
    $document->close();
```