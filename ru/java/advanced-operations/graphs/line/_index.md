---
title: Добавить объект линии в PDF файл
linktitle: Добавить линию
type: docs
weight: 40
url: /ru/java/add-line/
description: В этой статье объясняется, как создать объект линии в вашем PDF с использованием Aspose.PDF для Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Добавить объект линии

Aspose.PDF для Java поддерживает возможность добавления графических объектов (например, график, линия, прямоугольник и т.д.) в PDF документы. Вы также можете добавить объект [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Line), где можно задать шаблон штрихов, цвет и другие параметры форматирования для элемента линии.

Следуйте шагам ниже:

1. Создайте экземпляр [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Добавьте [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) в коллекцию страниц PDF файла.

1. Создайте экземпляр [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph).

1. Добавьте объект Graph в коллекцию параграфов экземпляра страницы.

1. Создайте экземпляр [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).

1. Установите ширину линии.

1. Добавьте объект [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) в коллекцию фигур объекта Graph.

1. Сохраните ваш PDF файл.

Следующий фрагмент кода показывает, как добавить объект [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle), заполненный цветом.

```java
 public static void ExampleLine() {
        // Создайте экземпляр Document
        Document pdfDocument = new Document();
        // Добавьте страницу в коллекцию страниц PDF файла
        Page page = pdfDocument.getPages().add();
        // Создайте экземпляр Graph
        Graph graph = new Graph(100, 400);

        // Добавьте объект graph в коллекцию абзацев экземпляра страницы
        page.getParagraphs().add(graph);

        // Создайте экземпляр Rectangle
        Line line = new Line(new float[] { 100, 100, 200, 100 });
        
        line.getGraphInfo().setLineWidth(5);
        
        // Добавьте объект rectangle в коллекцию фигур объекта Graph
        graph.getShapes().add(line);

        // Сохраните PDF файл
        pdfDocument.save(_dataDir + "LineAdded.pdf");
    }
```


![Add Line](add_line.png)

## Как добавить пунктирную линию в ваш PDF документ

```java
public static void ExampleDashedLine() {
        // Создать экземпляр документа
        Document pdfDocument = new Document();
        // Добавить страницу в коллекцию страниц PDF файла
        Page page = pdfDocument.getPages().add();

        // Создать объект рисования с определенными размерами
        Graph canvas = new Graph(100, 400);
        // Добавить объект рисования в коллекцию абзацев экземпляра страницы
        page.getParagraphs().add(canvas);

        // Создать объект линии
        Line line = new Line(new float[] { 100, 100, 200, 100 });

        // Установить цвет для объекта линии
        line.getGraphInfo().setColor(Color.getRed());
        // Указать массив штрихов для объекта линии
        line.getGraphInfo().setDashArray(new int[] { 0, 1, 0 });
        // Установить фазу штриха для экземпляра линии
        line.getGraphInfo().setDashPhase(1);
        // Добавить линию в коллекцию фигур объекта рисования
        canvas.getShapes().add(line);
        // Сохранить PDF документ
        pdfDocument.save(_dataDir + "DashLength_out.pdf");
    }
```


Давайте проверим результат:

![Пунктирная линия](dash_line.png)

## Нарисовать линию через страницу

Мы также можем использовать объект линии, чтобы нарисовать крест, начиная с нижнего левого до верхнего правого угла и от верхнего левого до нижнего правого угла.

Пожалуйста, ознакомьтесь с приведенным ниже фрагментом кода, чтобы выполнить это требование.

```java
    public static void ExampleLineAcrossPage() {
        // Создать экземпляр документа
        Document pdfDocument = new Document();
        // Добавить страницу в коллекцию страниц PDF файла
        Page page = pdfDocument.getPages().add();
        // Установить отступ страницы по всем сторонам равным 0

        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);

        // Создать объект Graph с шириной и высотой, равными размерам страницы
        Graph graph = new Graph((float) page.getPageInfo().getWidth(), (float) page.getPageInfo().getHeight());

        // Создать первый объект линии, начиная с нижнего левого до верхнего правого угла страницы
        Line line = new Line(new float[] { (float) page.getRect().getLLX(), 0, (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getURY() });

        // Добавить линию в коллекцию фигур объекта Graph
        graph.getShapes().add(line);
        // Нарисовать линию от верхнего левого угла страницы до нижнего правого угла страницы
        Line line2 = new Line(new float[] { 0, (float) page.getRect().getURY(), (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getLLX() });

        // Добавить линию в коллекцию фигур объекта Graph
        graph.getShapes().add(line2);
        // Добавить объект Graph в коллекцию абзацев страницы
        page.getParagraphs().add(graph);

        // Сохранить PDF файл
        pdfDocument.save(_dataDir + "DrawingLine_out.pdf");
    }
```


![Рисование линии](draw_line.png)