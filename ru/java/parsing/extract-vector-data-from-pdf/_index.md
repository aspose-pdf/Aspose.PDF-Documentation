---
title: Извлечение векторных данных из файла PDF с помощью Java
linktitle: Извлечь векторные данные из PDF
type: docs
weight: 80
url: /java/extract-vector-data-from-pdf/
description: Aspose.PDF позволяет легко извлекать векторные данные из файла PDF. Вы можете получить векторные данные, такие как положение, границы прямоугольника и выходные данные SVG.
lastmod: "2026-06-16"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
## Доступ к векторным данным из PDF-документа

Используйте `GraphicsAbsorber` для проверки элементов векторной графики на странице и записи их базовой геометрии в текстовый файл.

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) и посетите целевую [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), чтобы собрать операции с векторной графикой.
1. Перебирайте извлеченные объекты [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) и читайте их коллекции прямоугольников, позиций и операторов.
1. Создайте выходной текст с подробностями геометрии и количества операторов для каждого элемента.
1. Запишите извлеченные векторные данные в выходной файл.

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

## Сохранение векторной графики страницы в SVG

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Получите целевую [страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) из документа.
1. Вызовите `page.trySaveVectorGraphics(outputFile.toString())`, чтобы экспортировать содержимое векторной графики этой страницы непосредственно в SVG.

```java
public static void saveVectorGraphicsToSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.trySaveVectorGraphics(outputFile.toString());
    }
}
```

## Сохраните каждый извлеченный элемент в отдельный SVG.

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) и посетите целевую [страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Прежде чем записывать файлы, создайте выходной каталог для извлеченных подпутей.
1. Переберите извлеченные объекты [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) и вызовите `saveToSvg(...)` для каждого элемента.
1. Сохраните каждый извлеченный элемент в отдельный файл SVG.

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

## Объедините извлеченные элементы в один SVG.

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) и посетите целевую [страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Создайте разметку-оболочку SVG, которая будет содержать объединенные векторные фрагменты.
1. Переберите извлеченные объекты [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) и добавьте каждый сгенерированный фрагмент SVG.
1. Запишите объединенный вывод SVG в целевой файл.

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

## Извлеките один векторный элемент

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) и посетите целевую [страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Получите необходимый [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) из извлеченной коллекции элементов.
1. Проверьте, является ли выбранный элемент [XFormPlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/xformplacement/), и при необходимости перейдите к его вложенным элементам.
1. Save the selected vector element to the output SVG file.

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
