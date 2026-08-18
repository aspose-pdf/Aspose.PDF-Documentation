---
title: Извлечение содержимого с тегами из PDF-файлов в Java
linktitle: Извлечь контент с тегами
type: docs
weight: 20
url: /java/extract-tagged-content-from-tagged-pdfs/
description: Узнайте, как проверять содержимое PDF с тегами в Java с помощью Aspose.PDF, включая доступ к содержимому с тегами, доступ к корневой структуре и элементам дочерней структуры.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Используйте эти API, когда вам нужно проверить дерево логической структуры PDF-файла с тегами, а также проверить или обновить метаданные элемента структуры.

## Получите метаданные контента с тегами

Используйте этот пример, если вам нужен доступ к контейнеру содержимого с тегами и вы хотите определить основные метаданные документа, такие как заголовок и язык.

1. Создайте новый PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите объект [ITaggedContent](https://reference.aspose.com/pdf/java/com.aspose.pdf/itaggedcontent/) из документа.
1. Установите метаданные размеченного контента и сохраните выходной файл.

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

## Получите корневую структуру PDF-файла с тегами

В этом примере показано, как проверить корневые объекты, которые представляют структурное дерево PDF-файла с тегами.

1. Создайте новый PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и получите его содержимое с тегами.
1. Установите необходимые метаданные документа.
1. Считайте и распечатайте корень дерева структуры и логический корневой элемент, затем сохраните файл.

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

## Доступ и обновление элементов дочерней структуры

Используйте этот пример, когда вам нужно перебрать дочерние элементы в дереве структуры, проверить их свойства и обновить выбранные метаданные.

1. Откройте исходный файл с тегом PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Считайте дочерние элементы из корня дерева структуры и распечатайте доступные свойства.
1. Получите доступ к дочерним элементам первого корневого дочернего элемента, обновите их метаданные и сохраните документ.

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
