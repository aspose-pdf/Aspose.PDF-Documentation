---
title: Extrair Texto de Carimbos
type: docs
weight: 60
url: /php-java/extract-text-from-stamps/
---

## Extrair Texto de Anotações de Carimbo

Aspose.PDF para PHP via Java permite que você extraia texto de anotações de carimbo. Para extrair texto de Anotações de Carimbo em um PDF, os seguintes passos podem ser usados.

1. Carregar o documento PDF
1. Obter a página desejada do documento
1. Criar uma nova instância da classe StampAnnotation
1. Criar uma nova instância da classe AnnotationSelector e passar a anotação de carimbo para ela
1. Aceitar o seletor de anotações na página
1. Obter as anotações de carimbo selecionadas
1. Criar uma nova instância da classe TextAbsorber
1. Obter a primeira anotação de carimbo
1. Obter a aparência normal da anotação de carimbo
1. Visitar a aparência usando o absorvedor de texto
1. Obter o texto extraído do absorvedor de texto
1. Fechar o documento

```php
    $responseData = "";
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    $stampAnnotation = new StampAnnotation($document);
    $annotationSelector = new AnnotationSelector($stampAnnotation);
    $page->accept($annotationSelector);
    $stampAnnotations = $annotationSelector->getSelected();
    $textAbsorber = new TextAbsorber();
    $stampAnnotation = $stampAnnotations->get(0);    
    $appearance = $stampAnnotation->getNormalAppearance();
    $textAbsorber->visit($appearance);
    $responseData = java_values($textAbsorber->getText());       
    $document->close();
```