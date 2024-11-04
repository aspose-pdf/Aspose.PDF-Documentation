---
title: Anotações Adesivas em PDF
linktitle: Anotação Adesiva
type: docs
weight: 50
url: /php-java/sticky-annotations/
description: Este tópico é sobre anotações adesivas, como exemplo mostramos a Anotação de Marca d'Água no texto. É usada para representar gráficos na página. Confira o trecho de código para resolver esta tarefa.
lastmod: "2024-06-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar Anotação de Marca d'Água

Uma anotação de marca d'água deve ser usada para representar gráficos que devem ser impressos em um tamanho e posição fixos em uma página, independentemente das dimensões da página impressa.

Você pode adicionar Texto de Marca d'Água usando [WatermarkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/WatermarkAnnotation) em uma posição específica da página PDF. A opacidade da Marca d'Água também pode ser controlada usando a propriedade de opacidade.

Por favor, verifique o seguinte trecho de código para adicionar WatermarkAnnotation.

```php

    // Abrir documento
    $document = new Document($inputFile);
    $fontRepository = new FontRepository();
    $colors = new Color();
    // obter página específica
    $page = $document->getPages()->get_Item(1);
    
    //Criar Anotação
    $wa = new WatermarkAnnotation($page, new Rectangle(100, 500, 400, 600));

    //Adicionar anotação na coleção de Anotações da Página
    $page->getAnnotations()->add($wa);

    //Criar TextState para configurações de Fonte
    $ts = new TextState();

    $ts->setForegroundColor($colors->getBlue());
    $ts->setFont($fontRepository->findFont("Times New Roman"));
    $ts->setFontSize(32);

    //Definir nível de opacidade do Texto da Anotação
    $wa->setOpacity(0.5);
            
    $watermarkStrings = ["Aspose.PDF", "Marca d'Água", "Demonstração" ];
    //Adicionar Texto à Anotação
    $wa->setTextAndState($watermarkStrings, $ts);

    // Salvar documento PDF resultante.    
    $document->save($outputFile);
    $document->close();
```