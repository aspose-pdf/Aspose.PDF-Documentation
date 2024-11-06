---
title: Извлечение Текста из Штампов
type: docs
weight: 60
url: ru/php-java/extract-text-from-stamps/
---

## Извлечение Текста из Аннотаций Штампов

Aspose.PDF для PHP через Java позволяет извлекать текст из аннотаций штампов. Для извлечения текста из аннотаций штампов в PDF можно использовать следующие шаги.

1. Загрузите PDF документ
1. Получите нужную страницу документа
1. Создайте новый экземпляр класса StampAnnotation
1. Создайте новый экземпляр класса AnnotationSelector и передайте ему аннотацию штампа
1. Примените селектор аннотаций на странице
1. Получите выбранные аннотации штампов
1. Создайте новый экземпляр класса TextAbsorber
1. Получите первую аннотацию штампа
1. Получите нормальное отображение аннотации штампа
1. Посетите отображение с использованием поглотителя текста
1. Получите извлеченный текст из поглотителя текста
1. Закройте документ

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