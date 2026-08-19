---
title: Аннотации фигур через Java
linktitle: Аннотации фигур
type: docs
weight: 20
url: /ru/java/shape-annotations/
description: Узнайте, как добавлять, проверять и удалять аннотации квадратов, кругов, полигонов и полилиний в PDF‑документах с помощью Aspose.PDF for Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Работайте с геометрическими PDF‑аннотациями в Java.
Abstract: В этой статье объясняется, как создавать, проверять и удалять геометрические аннотации в PDF‑документах с использованием Aspose.PDF for Java. Описываются аннотации квадратной, круглой, многоугольной и полилинейной формы с настройками цвета, непрозрачности, всплывающего окна и точек.
---
Аннотации формы в этом разделе охватывают геометрические типы аннотаций, такие как квадраты, окружности, многоугольники, полилинии и линии.

## Добавьте аннотации квадрат, круг, полигон и полилиния

Используйте эти примеры, когда вам нужно разместить геометрические аннотации с пользовательскими цветами, прозрачностью, данными всплывающих окон или массивами точек.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте требуемую аннотацию формы и настройте её прямоугольник, точки и визуальные свойства.
1. Добавьте аннотацию на страницу и сохраните обновлённый документ.

```java
public static void squareAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SquareAnnotation squareAnnotation = new SquareAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(60, 600, 250, 450, true));
        squareAnnotation.setTitle("John Smith");
        squareAnnotation.setColor(Color.getBlue());
        squareAnnotation.setInteriorColor(Color.getBlueViolet());
        squareAnnotation.setOpacity(0.25);

        document.getPages().get_Item(1).getAnnotations().add(squareAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void circleAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        CircleAnnotation circleAnnotation = new CircleAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(270, 160, 483, 383, true));
        circleAnnotation.setTitle("John Smith");
        circleAnnotation.setColor(Color.getRed());
        circleAnnotation.setInteriorColor(Color.getMistyRose());
        circleAnnotation.setOpacity(0.5);
        circleAnnotation.setPopup(new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 316, 1021, 459, true)));

        document.getPages().get_Item(1).getAnnotations().add(circleAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void polygonAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PolygonAnnotation polygonAnnotation = new PolygonAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(200, 300, 400, 400, true),
                new Point[]{
                        new Point(200, 300),
                        new Point(220, 300),
                        new Point(250, 330),
                        new Point(300, 304),
                        new Point(300, 400)
                });
        polygonAnnotation.setTitle("John Smith");
        polygonAnnotation.setColor(Color.getBlue());
        polygonAnnotation.setInteriorColor(Color.getBlueViolet());
        polygonAnnotation.setOpacity(0.25);

        document.getPages().get_Item(1).getAnnotations().add(polygonAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void polylineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PolylineAnnotation polylineAnnotation = new PolylineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(270, 193, 571, 383, true),
                new Point[]{
                        new Point(545, 150),
                        new Point(545, 190),
                        new Point(667, 190),
                        new Point(667, 110),
                        new Point(626, 111)
                });
        polylineAnnotation.setTitle("John Smith");
        polylineAnnotation.setColor(Color.getRed());
        polylineAnnotation.setPopup(new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 196, 1021, 338, true)));

        document.getPages().get_Item(1).getAnnotations().add(polylineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## Получите аннотации квадрат, круг, полигон и полилиния

Эти примеры проверяют коллекцию аннотаций страницы и выводят прямоугольники геометрических аннотаций по типу.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перебрать аннотации страницы.
1. Фильтровать по требуемому [ТипАннотации](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/) значение и вывести прямоугольник.

```java
public static void squareAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Square) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void circleAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Circle) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void polygonAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Polygon) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

```java
public static void polylineAnnotationGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.PolyLine) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## Удалите аннотации квадрат, круг, многоугольник и полилиния

Используйте эти примеры, когда необходимо удалить аннотации фигур определённого типа со страницы.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Соберите аннотации требуемого геометрического типа.
1. Удалите собранные аннотации и сохранить выходной файл.

```java
public static void squareAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Square) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

```java
public static void circleAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Circle) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

```java
public static void polygonAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Polygon) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

```java
public static void polylineAnnotationDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.PolyLine) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## Добавьте линейную аннотацию

Этот пример создает аннотацию линии со стрелочными окончаниями, форматированием границы и всплывающей заметкой.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [Линейная аннотация](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/) с начальной и конечной точками.
1. Настройте внешний вид, добавьте всплывающее окно и сохраните документ.

```java
public static void lineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        LineAnnotation lineAnnotation = new LineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(550, 93, 562, 439, true),
                new Point(556, 99),
                new Point(556, 443));
        lineAnnotation.setTitle("John Smith");
        lineAnnotation.setColor(Color.getRed());
        lineAnnotation.setStartingStyle(LineEnding.OpenArrow);
        lineAnnotation.setEndingStyle(LineEnding.OpenArrow);

        Border border = new Border(lineAnnotation);
        border.setWidth(3);
        lineAnnotation.setBorder(border);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 124, 1021, 266, true));
        lineAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(lineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## Получите линейные аннотации

Этот пример считывает линейные аннотации и выводит их начальные и конечные координаты.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перебрать аннотации страницы и выбрать [ТипАннотации](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Line`.
1. Привести каждое совпадение к [Линейная аннотация](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/) и вывести её координаты.

```java
public static void lineAnnotationsGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Line) {
                LineAnnotation la = (LineAnnotation) annotation;
                System.out.printf("[%s,%s]-[%s,%s]%n",
                        la.getStarting().getX(), la.getStarting().getY(),
                        la.getEnding().getX(), la.getEnding().getY());
            }
        }
    }
}
```

## Удалите аннотации линий

Используйте этот подход, когда необходимо удалить линейные аннотации со страницы.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Собрать аннотации типа [ТипАннотации](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Line`.
1. Удалите собранные аннотации и сохраните документ.

```java
public static void lineAnnotationsDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : page.getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Line) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            page.getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## Связанные темы аннотаций

- [Интерактивные аннотации](/pdf/ru/java/interactive-annotations/)
- [Аннотации разметки](/pdf/ru/java/markup-annotations/)
- [Аннотации безопасности](/pdf/ru/java/security-annotations/)
- [Текстовые аннотации](/pdf/ru/java/text-based-annotations/)
- [Аннотации водяного знака](/pdf/ru/java/watermark-annotations/)
- [Импорт и экспорт аннотаций](/pdf/ru/java/import-export-annotations/)

