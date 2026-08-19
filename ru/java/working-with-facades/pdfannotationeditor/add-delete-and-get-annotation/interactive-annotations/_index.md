---
title: Интерактивные аннотации с использованием Java
linktitle: Интерактивные аннотации
type: docs
weight: 30
url: /ru/java/pdfannotationeditor-class/interactive-annotations/
description: Узнайте, как добавлять, проверять и удалять аннотации-ссылки в PDF‑документах с помощью Java.
lastmod: "2026-08-19"
TechArticle: true
AlternativeHeadline: Работа с интерактивными PDF‑аннотациями в Java
Abstract: В этой статье объясняется, как работать с интерактивными аннотациями‑ссылками в PDF‑файлах с использованием Java. Охватывается поиск текста, создание аннотации‑ссылки над найденной областью текста, чтение существующих аннотаций‑ссылок и их удаление.
---
## Добавьте аннотацию‑ссылку

1. Загрузите исходный PDF‑документ и выполните поиск целевого текста на первой странице.
2. Используйте найденный прямоугольник текста для создания `LinkAnnotation` и назначьте целевой URI.
3. Добавьте аннотацию на страницу и сохраните обновлённый PDF.

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

