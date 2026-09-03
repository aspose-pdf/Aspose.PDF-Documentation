---
title: Работа с PDF-слоями с использованием Java
linktitle: Работа с PDF-слоями
type: docs
weight: 50
url: /ru/java/working-with-pdf-layers/
description: Узнайте, как добавлять, блокировать, извлекать, уплощать и объединять PDF-слои в Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Управление PDF-слоями с помощью Java
Abstract: В этой статье объясняется, как работать с PDF-слоями, также известными как Optional Content Groups, используя Aspose.PDF for Java. Узнайте, как добавить слои на страницу, заблокировать существующий слой, извлечь содержимое слоя в файлы или потоки, уплощать слоистое содержимое и объединять слои в один.
---
Aspose.PDF for Java раскрывает слои PDF через `Layer` API на каждой странице. Вы можете создавать группы альтернативного контента, изменять их поведение и экспортировать или уплощать их содержимое при необходимости.

## Добавьте слои на страницу PDF

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте и настроить необходимые [Слой](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) объекты на странице.
1. Сохраните результирующий PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

Полный пример создает три отдельных слоя с красным, зелёным и синим содержимым линий.

## Заблокируйте слой

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите доступ к цели [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и получить его [Слой](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/) коллекцию.
1. Блокируйте цель [Слой](https://reference.aspose.com/pdf/java/com.aspose.pdf/layer/).
1. Сохраните обновлённый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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


