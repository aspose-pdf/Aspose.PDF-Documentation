---
title: Работа со слоями PDF с использованием Java
linktitle: Работа со слоями PDF
type: docs
weight: 50
url: /java/working-with-pdf-layers/
description: Узнайте, как добавлять, блокировать, извлекать, выравнивать и объединять слои PDF в Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Управление слоями PDF с помощью Java
Abstract: В этой статье объясняется, как работать со слоями PDF, также известными как группы дополнительного контента, с помощью Aspose.PDF для Java. Узнайте, как добавлять слои на страницу, блокировать существующий слой, извлекать содержимое слоя в файлы или потоки, выравнивать многоуровневое содержимое и объединять слои в один.
---
Aspose.PDF для Java предоставляет слои PDF через API `Layer` на каждой странице. Вы можете создавать дополнительные группы контента, изменять их поведение, а также экспортировать или сводить их контент при необходимости.

## Добавление слоев на страницу PDF

1. Создайте новый PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте и настройте необходимые объекты [Слой](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) на странице.
1. Сохраните выходной PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addLayers(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Layer layer = new Layer("oc1", "Red Line");
        layer.getContents().add(new SetRGBColorStroke(1, 0, 0));
        layer.getContents().add(new MoveTo(500, 700));
        layer.getContents().add(new LineTo(400, 700));
        layer.getContents().add(new Stroke());
        page.getLayers().add(layer);

        document.save(outputFile.toString());
    }
}
```

В полном примере создаются три отдельных слоя с содержимым красной, зеленой и синей линий.

## Заблокировать слой

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите доступ к целевой [Странице](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и получите ее коллекцию [Слой](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/).
1. Заблокируйте целевой [слой](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/).
1. Сохраните обновленный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void lockLayer(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        if (!page.getLayers().isEmpty()) {
            Layer layer = page.getLayers().getFirst();
            layer.lock();
            document.save(outputFile.toString());
        }
    }
}
```
