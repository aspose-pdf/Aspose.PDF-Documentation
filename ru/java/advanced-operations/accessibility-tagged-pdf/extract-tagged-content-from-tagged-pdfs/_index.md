---
title: Извлечение помеченного контента из PDF в Java
linktitle: Извлечь помеченный контент
type: docs
weight: 20
url: /ru/java/extract-tagged-content-from-tagged-pdfs/
description: Узнайте, как просматривать помеченный PDF‑контент в Java с помощью Aspose.PDF, включая доступ к помеченному контенту, доступ к корневой структуре и дочерним элементам структуры.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Используйте эти APIs, когда необходимо просмотреть логическое дерево структуры помеченного PDF и изучить или обновить метаданные элементов структуры.

## Получите метаданные помеченного контента

Используйте этот пример, когда вам нужен доступ к контейнеру помеченного контента и вы хотите задать базовые метаданные документа, такие как заголовок и язык.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/) объект из документа.
1. Установите метаданные помеченного содержимого и сохраните файл вывода.

```java
public static void getTaggedContent(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Simple Tagged Pdf Document");
        taggedContent.setLanguage("en-US");
        document.save(outputFile.toString());
    }
}
```

## Получите корневую структуру помеченного PDF

Этот пример показывает, как исследовать корневые объекты, представляющие дерево структуры Tagged PDF.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и получить его тегированное содержимое.
1. Установите требуемые метаданные документа.
1. Прочитайте и выведите корень дерева структуры и логический корневой элемент, затем сохраните файл.

```java
public static void getRootStructure(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Tagged Pdf Document");
        taggedContent.setLanguage("en-US");

        System.out.println("StructTreeRootElement: " + taggedContent.getStructTreeRootElement());
        System.out.println("RootElement: " + taggedContent.getRootElement());

        document.save(outputFile.toString());
    }
}
```

## Получите доступ и обновить дочерние элементы структуры

Используйте этот пример, когда вам нужно пройтись по дочерним элементам в структуре дерева, проверить их свойства и обновить выбранные метаданные.

1. Откройте исходный PDF с тегами [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Считайте дочерние элементы из корня дерева структуры и выведите доступные свойства.
1. Получите дочерние элементы первого корневого дочернего элемента, обновите их метаданные и сохраните документ.

```java
public static void accessChildElements(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        ITaggedContent taggedContent = document.getTaggedContent();

        ElementList elementList = taggedContent.getStructTreeRootElement().getChildElements();
        for (Object element : elementList) {
            if (element instanceof StructureElement structureElement) {
                System.out.println("StructureElement properties - "
                        + "title: " + structureElement.getTitle()
                        + ", language: " + structureElement.getLanguage()
                        + ", actual_text: " + structureElement.getActualText()
                        + ", expansion_text: " + structureElement.getExpansionText()
                        + ", alternative_text: " + structureElement.getAlternativeText());
            }
        }

        Element firstChild = taggedContent.getRootElement().getChildElements().get_Item(1);
        for (Object element : firstChild.getChildElements()) {
            if (element instanceof StructureElement structureElement) {
                structureElement.setTitle("title");
                structureElement.setLanguage("fr-FR");
                structureElement.setActualText("actual text");
                structureElement.setExpansionText("exp");
                structureElement.setAlternativeText("alt");
            }
        }

        document.save(outputFile.toString());
    }
}
```

