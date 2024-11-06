---
title: Extrair Dados AcroForms
linktitle: Extrair Dados AcroForms
type: docs
weight: 30
url: pt/php-java/extract-form/
description: Esta seção explica como extrair formulários do seu documento PDF com Aspose.PDF para PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obter Valor de um Campo Individual de Documento PDF

O método [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--) do campo de formulário permite você obter o valor de um campo específico.

Para obter o valor, obtenha o campo de formulário da coleção Form do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Este exemplo seleciona um [textBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField) e recupera seu valor usando o método [getValue()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--).

```php

    // Abrir um documento
    $document = new Document($inputFile);

    // Obter um campo
    $textBoxField = $document->getForm()->get("textbox1");

    // Obter o nome do campo
    $responseData = "PartialName: " . $textBoxField->getPartialName();

    // Obter o valor do campo
    $responseData = $responseData . " Value: " . $textBoxField->getValue();
    $document->close();
```