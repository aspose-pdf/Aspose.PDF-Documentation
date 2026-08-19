---
title: Работа с векторной графикой в Java
linktitle: Работа с векторной графикой
type: docs
weight: 100
url: /ru/java/working-with-vector-graphics/
description: Узнайте, как извлекать, перемещать, удалять, копировать и экспортировать векторную графику в PDF‑документах с помощью Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Используйте GraphicsAbsorber для проверки и манипулирования векторной графикой PDF в Java
Abstract: В этой статье объясняется, как работать с векторной графикой в Aspose.PDF for Java с использованием класса GraphicsAbsorber. Узнайте, как проверять векторные элементы на странице, перемещать или удалять их, копировать графику между страницами и экспортировать векторный контент в SVG.
---
Aspose.PDF for Java предоставляет векторный контент через `GraphicsAbsorber` и `GraphicElement` объекты. Это позволяет вам просматривать низкоуровневые векторные элементы на странице, а затем обновлять, удалять, копировать или экспортировать их.

## Проверьте векторную графику на странице

Используйте этот пример, когда вам нужно перечислить векторные элементы и проверить их страницу, позицию и количество операторов.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) и посетите целевую страницу.
1. Перебрать поглощённые [Графический элемент](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicelement/) объекты и вывод их свойств.

```java
public static void usingGraphicsAbsorber(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            graphicsAbsorber.visit(page);
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                System.out.println("Page Number: " + element.getSourcePage().getNumber());
                System.out.println("Position: (" + element.getPosition().getX() + ", "
                        + element.getPosition().getY() + ")");
                System.out.println("Number of Operators: " + element.getOperators().size());
            }
        } finally {
            graphicsAbsorber.dispose();
        }
    }
}
```

## Переместить векторную графику на странице

Используйте этот пример, когда все обнаруженные векторные элементы должны быть смещены в новое положение.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Посетите целевую страницу с [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) и временно подавлять обновления.
1. Измените позицию каждого поглощённого элемента, возобновите обновления и сохраните документ.

```java
public static void moveGraphics(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            graphicsAbsorber.visit(page);
            graphicsAbsorber.suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                Point position = element.getPosition();
                element.setPosition(new Point(position.getX() + 150, position.getY() - 10));
            }
            graphicsAbsorber.resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics moved in " + outputFile);
}
```

## Удалите векторную графику по позиции с удалением элемента

Используйте этот пример, когда векторные элементы внутри определённого прямоугольника нужно удалять по одному.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Посетите страницу с [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) и определить цель [Прямоугольник](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Удалите соответствующие элементы, возобновите обновления и сохраните документ.

```java
public static void removeGraphicsMethod1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            Rectangle rectangle = new Rectangle(70, 248, 170, 252, true);
            graphicsAbsorber.visit(page);
            graphicsAbsorber.suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                if (rectangle.contains(element.getPosition(), false)) {
                    element.remove();
                }
            }
            graphicsAbsorber.resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics removed with method 1 in " + outputFile);
}
```

## Удалите векторную графику, удалив коллекцию

Используйте этот пример, когда векторные элементы, соответствующие условию, следует сначала собрать, а затем удалить в одной операции со страницей.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Посетите страницу с [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) и собрать соответствующие элементы.
1. Удалите собранную графику из содержимого страницы и сохраните обновлённый документ.

```java
public static void removeGraphicsMethod2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            Rectangle rectangle = new Rectangle(70, 248, 170, 252, true);
            graphicsAbsorber.visit(page);
            GraphicElementCollection removedElements = new GraphicElementCollection();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                if (rectangle.contains(element.getPosition(), false)) {
                    removedElements.add(element);
                }
            }
            page.getContents().suppressUpdate();
            page.deleteGraphics(removedElements);
            page.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics removed with method 2 in " + outputFile);
}
```

## Копировать векторную графику на другую страницу элемент за элементом

Используйте этот пример, когда каждый извлечённый векторный элемент должен быть добавлен по отдельности на новую страницу.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить страницу назначения.
1. Посетите исходную страницу с [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/).
1. Добавьте каждый [Графический элемент](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicelement/) на страницу назначения и сохранить документ.

```java
public static void addToAnotherPageMethod1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page1 = document.getPages().get_Item(1);
            Page page2 = document.getPages().add();
            graphicsAbsorber.visit(page1);
            page2.getContents().suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                element.addOnPage(page2);
            }
            page2.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics copied with method 1 in " + outputFile);
}
```

## Копировать векторную графику на другую страницу в виде коллекции

Используйте этот пример, когда всю поглощённую коллекцию векторных графиков нужно скопировать на новую страницу за один вызов.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить страницу назначения.
1. Посетите исходную страницу с [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/).
1. Добавьте собранную графику в коллекцию на целевую страницу и сохраните документ.

```java
public static void addToAnotherPageMethod2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page1 = document.getPages().get_Item(1);
            Page page2 = document.getPages().add();
            graphicsAbsorber.visit(page1);
            page2.getContents().suppressUpdate();
            page2.addGraphics(graphicsAbsorber.getElements());
            page2.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics copied with method 2 in " + outputFile);
}
```

