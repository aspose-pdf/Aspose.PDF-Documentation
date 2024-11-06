---
title: Добавление Объекта Кривой в PDF файл
linktitle: Добавить Кривую
type: docs
weight: 30
url: ru/java/add-curve/
description: В этой статье объясняется, как создать объект кривой в вашем PDF с использованием Aspose.PDF для Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Добавление объекта Кривой

Граф [Кривая](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Curve) представляет собой соединенное объединение проективных линий, каждая из которых встречает три другие в обычных двойных точках.

Aspose.PDF для Java демонстрирует, как использовать кривые Безье в ваших графиках.
Кривые Безье широко используются в компьютерной графике для моделирования гладких кривых. Кривая полностью содержится в выпуклой оболочке своих контрольных точек, точки могут быть графически отображены и использованы для интуитивного управления кривой.
Вся кривая содержится в четырехугольнике, углы которого определяются четырьмя данными точками (их выпуклая оболочка).

В этой статье мы рассмотрим простые графики кривых и заполненные кривые, которые вы можете создать в своем PDF документе.

Следуйте инструкциям ниже:

1. Создайте экземпляр [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Создайте [Drawing object](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) с определенными размерами.

1. Установите [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) для Drawing object.

1. Добавьте объект [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) в коллекцию параграфов страницы.

1. Сохраните ваш PDF файл

```java
    public static void ExampleCurve() {
        // Создайте экземпляр Document
        Document pdfDocument = new Document();
        // Добавьте страницу в коллекцию страниц PDF файла
        Page page = pdfDocument.getPages().add();

        // Создайте Drawing object с определенными размерами
        Graph graph = new Graph(400, 200);
        // Установите границу для Drawing object
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});

        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // Добавьте объект Graph в коллекцию параграфов страницы
        page.getParagraphs().add(graph);

        // Сохраните PDF файл
        pdfDocument.save(_dataDir + "DrawingCurve1_out.pdf");
    }
```


Следующая картина показывает результат выполнения нашего фрагмента кода:

![Drawing Curve](drawing_curve.png)

## Создание объекта Заполненной Кривой

Этот пример показывает, как добавить объект Кривой, заполненный цветом.

```java
    public static void ExampleFilledCurve() {
        // Создаем экземпляр документа
        Document pdfDocument = new Document();
        // Добавляем страницу в коллекцию страниц PDF файла
        Page page = pdfDocument.getPages().add();

        // Создаем объект Рисунка с определенными размерами
        Graph graph = new Graph(400, 200);
        // Устанавливаем границу для объекта Рисунка
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        // Создаем кривую с заданными координатами
        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // Добавляем объект Graph в коллекцию параграфов страницы
        page.getParagraphs().add(graph);

        // Сохраняем PDF файл
        pdfDocument.save(_dataDir + "DrawingCurve2_out.pdf");
    }
```


Look at the result of adding a filled Curve:

![Заполненная Кривая](filled_curve.png)