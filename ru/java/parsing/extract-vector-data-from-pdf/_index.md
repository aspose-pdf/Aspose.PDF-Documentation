---
title: Извлечь векторные данные из PDF‑файла с использованием Java
linktitle: Извлечь векторные данные из PDF
type: docs
weight: 80
url: /ru/java/extract-vector-data-from-pdf/
description: Aspose.PDF упрощает извлечение векторных данных из PDF‑файла. Вы можете получить векторные данные, такие как позиция, границы прямоугольника и SVG‑вывод.
lastmod: "2026-08-19"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
## Получите доступ к векторным данным из PDF‑документа

Использовать `GraphicsAbsorber` для проверки векторных графических элементов на странице и записи их базовой геометрии в текстовый файл.

1. Откройте исходный PDF в [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) и посетить цель [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) для сбора операций векторной графики.
1. Итерировать по извлеченным [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) объекты и прочитать их коллекции прямоугольников, позиций и операторов.
1. Сформируйте выходной текст с деталями геометрии и количества операторов для каждого элемента.
1. Запишите извлечённые векторные данные в выходной файл.

```java
public static void extractGraphicsElements(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        StringBuilder text = new StringBuilder();
        int index = 1;
        for (GraphicElement element : absorber.getElements()) {
            text.append("Element ").append(index)
                    .append(": Rectangle = ").append(element.getRectangle())
                    .append(", Position = ").append(element.getPosition())
                    .append(", Operators = ").append(element.getOperators().size())
                    .append("\n");
            index++;
        }
        Files.writeString(outputFile, text.toString());
    }
}
```

## Сохраните векторную графику страницы в SVG

1. Откройте исходный PDF в [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Получите цель [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) из документа.
1. Вызов `page.trySaveVectorGraphics(outputFile.toString())` для экспорта векторного графического содержимого этой страницы непосредственно в SVG.

```java
public static void saveVectorGraphicsToSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.trySaveVectorGraphics(outputFile.toString());
    }
}
```

## Сохраните каждый извлечённый элемент в отдельный SVG

1. Откройте исходный PDF в [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) и посетить цель [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Создайте директорию вывода для извлечённых подпутей перед записью любых файлов.
1. Итерировать по извлеченным [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) объекты и вызов `saveToSvg(...)` для каждого элемента.
1. Сохраните каждый извлечённый элемент в отдельный файл SVG.

```java
public static void extractSubpathsToSvgs(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        Path subpathsDir = outputDir.resolve("subpaths");
        Files.createDirectories(subpathsDir);

        int index = 1;
        for (GraphicElement element : absorber.getElements()) {
            element.saveToSvg(subpathsDir.resolve("subpath_" + index + ".svg").toString());
            index++;
        }
    }
}
```

## Объединить извлечённые элементы в один SVG

1. Откройте исходный PDF в [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) и посетить цель [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Создайте разметку-обертку SVG, которая будет содержать объединённые векторные фрагменты.
1. Итерировать по извлеченным [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) объекты и добавить каждый сгенерированный SVG‑фрагмент.
1. Записать объединённый SVG‑вывод в целевой файл.

```java
public static void extractListOfElementsToSingleImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        StringBuilder svg = new StringBuilder();
        svg.append("<svg xmlns=\"http://www.w3.org/2000/svg\">\n");
        for (GraphicElement element : absorber.getElements()) {
            svg.append(element.saveToSvg()).append("\n");
        }
        svg.append("</svg>\n");
        Files.writeString(outputFile, svg.toString());
    }
}
```

## Извлеките отдельный векторный элемент

1. Откройте исходный PDF в [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) и посетить цель [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Получите необходимое [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) из извлеченной коллекции элементов.
1. Проверьте, является ли выбранный элемент [XFormPlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/xformplacement/) и перейдите к его вложенным элементам, если это необходимо.
1. Сохраните выбранный векторный элемент в выходной файл SVG.

```java
public static void extractSingleVectorElement(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        Page page = document.getPages().get_Item(1);
        graphicsAbsorber.visit(page);
        if (graphicsAbsorber.getElements().size() > 1) {
            GraphicElement xformPlacement = graphicsAbsorber.getElements().get_Item(1);
            if (xformPlacement instanceof XFormPlacement) {
                XFormPlacement placement = (XFormPlacement) xformPlacement;
                if (placement.getElements().size() > 2) {
                    placement.getElements().get_Item(2).saveToSvg(outputFile.toString());
                }
            } else {
                xformPlacement.saveToSvg(outputFile.toString());
            }
        }
    }
}
```

