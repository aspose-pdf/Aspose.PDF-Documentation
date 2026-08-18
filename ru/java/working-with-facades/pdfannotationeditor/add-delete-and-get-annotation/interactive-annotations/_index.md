---
title: Интерактивные аннотации с использованием Java
linktitle: Интерактивные аннотации
type: docs
weight: 30
url: /java/pdfannotationeditor-class/interactive-annotations/
description: Узнайте, как добавлять, проверять и удалять аннотации ссылок в документах PDF с помощью Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Работа с интерактивными аннотациями PDF в Java
Abstract: В этой статье объясняется, как работать с интерактивными аннотациями ссылок в файлах PDF с помощью Java. Он охватывает поиск текста, создание аннотации ссылки в соответствующей текстовой области, чтение существующих аннотаций ссылки и их удаление.
---
## Добавьте аннотацию ссылки

1. Загрузите исходный PDF-документ и найдите целевой текст на первой странице.
2. Используйте соответствующий текстовый прямоугольник, чтобы создать `LinkAnnotation` и назначить URI назначения.
3. Добавьте аннотацию на страницу и сохраните обновленный PDF-файл.

```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1), phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```
