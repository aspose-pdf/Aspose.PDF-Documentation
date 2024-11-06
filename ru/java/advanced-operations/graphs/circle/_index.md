---
title: Добавить объект круга в PDF файл
linktitle: Добавить круг
type: docs
weight: 20
url: ru/java/add-circle/
description: Эта статья объясняет, как создать объект круга в вашем PDF с использованием Aspose.PDF for Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Добавить объект круга

Как и столбчатые графики, круговые графики можно использовать для отображения данных в нескольких отдельных категориях. В отличие от столбчатых графиков, однако, круговые графики можно использовать только тогда, когда у вас есть данные для всех категорий, составляющих целое. Давайте посмотрим, как добавить объект [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Circle) с использованием Aspose.PDF for Java.

Следуйте шагам ниже:

1. Создайте экземпляр [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)

1. Создайте [Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) с определенными размерами

1. Установите [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) для объекта Drawing

1. Добавьте объект [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) в коллекцию параграфов страницы

1. Сохраните наш PDF файл

```java
public static void ExampleCircle() {
        // Создать экземпляр Document
        Document pdfDocument = new Document();
        // Добавить страницу в коллекцию страниц PDF файла
        Page page = pdfDocument.getPages().add();

        // Создать объект Drawing с определенными размерами
        Graph graph = new Graph(400, 200);
        // Установить границу для объекта Drawing
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);

        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(circle);

        // Добавить объект Graph в коллекцию параграфов страницы
        page.getParagraphs().add(graph);

        // Сохранить PDF файл
        pdfDocument.save(_dataDir + "DrawingCircle1_out.pdf");
    }
```


Наш нарисованный круг будет выглядеть так:

![Рисование круга](drawing_circle.png)

## Создать объект заполненного круга

Этот пример показывает, как добавить объект Circle, заполненный цветом.

```java

    public static void ExampleFilledCircle() {
        // Создаем экземпляр документа
        Document pdfDocument = new Document();
        // Добавляем страницу в коллекцию страниц PDF файла
        Page page = pdfDocument.getPages().add();

        // Создаем объект Drawing с определенными размерами
        Graph graph = new Graph(400, 200);
        // Устанавливаем границу для объекта Drawing
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());       
        circle.getGraphInfo().setFillColor(Color.getGreenYellow());

        graph.getShapes().add(circle);

        // Добавляем объект Graph в коллекцию абзацев страницы
        page.getParagraphs().add(graph);

        // Сохраняем PDF файл
        pdfDocument.save(_dataDir + "DrawingCircle2_out.pdf");
    }
```


Let's see the result of adding a filled Circle:

![Заполненный круг](filled_circle.png)