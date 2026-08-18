---
title: Используйте FloatingBox для макета PDF в Java
linktitle: Использование плавающего бокса
type: docs
weight: 30
url: /java/floating-box/
description: Узнайте, как использовать FloatingBox для макетирования текста, многоколоночного содержимого и точного позиционирования в документах PDF с помощью Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Создавайте и размещайте стилизованные контейнеры FloatingBox в PDF с помощью Java.
Abstract: В этой статье объясняется, как использовать FloatingBox в Aspose.PDF для Java. Он охватывает размещение текста в плавающих контейнерах с рамкой, создание повторяющихся макетов из нескольких столбцов, использование цветов фона, абсолютных смещений и параметров горизонтального или вертикального выравнивания.
---
Aspose.PDF для Java использует `FloatingBox` для создания многократно используемых текстовых контейнеров и макетов на основе столбцов.

## Создайте и добавьте плавающий блок

Используйте этот пример, когда текст необходимо поместить внутри плавающего контейнера с рамкой.

1. Создайте новый PDF-документ и добавьте страницу.
1. Создайте `FloatingBox`, установите его размер и границу, а также добавьте текстовое содержимое.
1. Добавьте поле на страницу и сохраните документ.

```java
public static void createAndAddFloatingBox(Path outputFile) {
       try (Document document = new Document()) {
           Page page = document.getPages().add();

           FloatingBox box = new FloatingBox(400, 30);
           box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
           box.setNeedRepeating(false);
           String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
           box.getParagraphs().add(new TextFragment(phrase));

           page.getParagraphs().add(box);
           document.save(outputFile.toString());
       }
   }
```

## Создайте повторяющийся макет из нескольких столбцов.

Используйте этот пример, когда длинный текст должен располагаться по нескольким столбцам внутри одного плавающего блока.

1. Создайте страницу и настройте поля.
1. Рассчитайте ширину столбца и настройте параметры столбца `FloatingBox`.
1. Добавьте в поле повторяющиеся фрагменты текста и сохраните документ.

```java
public static void multiColumnLayout(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().setMargin(new MarginInfo(36, 18, 36, 18));

        int columnCount = 3;
        int spacing = 10;
        double width = page.getPageInfo().getWidth()
                - page.getPageInfo().getMargin().getLeft()
                - page.getPageInfo().getMargin().getRight()
                - (columnCount - 1) * spacing;
        double columnWidth = width / 3;

        FloatingBox box = new FloatingBox();
        box.setNeedRepeating(true);
        box.getColumnInfo().setColumnWidths(columnWidth + " " + columnWidth + " " + columnWidth);
        box.getColumnInfo().setColumnSpacing(String.valueOf(spacing));
        box.getColumnInfo().setColumnCount(3);

        String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
        for (int i = 0; i < 10; i++) {
            box.getParagraphs().add(new TextFragment(phrase));
        }

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## Начинайте каждый фрагмент как первый элемент в столбце.

Используйте этот пример, когда каждый вставленный фрагмент должен начинать новый сегмент потока колонки.

1. Создайте страницу и настройте многоколонку `FloatingBox`.
1. Создайте фрагменты текста и пометьте их `setFirstParagraphInColumn(true)`.
1. Добавьте поле на страницу и сохраните PDF-файл.

```java
public static void multiColumnLayout2(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().setMargin(new MarginInfo(36, 18, 36, 18));

        int columnCount = 3;
        int spacing = 10;
        double width = page.getPageInfo().getWidth()
                - page.getPageInfo().getMargin().getLeft()
                - page.getPageInfo().getMargin().getRight()
                - (columnCount - 1) * spacing;
        double columnWidth = width / 3;

        FloatingBox box = new FloatingBox();
        box.setNeedRepeating(true);
        box.getColumnInfo().setColumnWidths(columnWidth + " " + columnWidth + " " + columnWidth);
        box.getColumnInfo().setColumnSpacing(String.valueOf(spacing));
        box.getColumnInfo().setColumnCount(3);

        String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
        for (int i = 0; i < 10; i++) {
            TextFragment text = new TextFragment(phrase);
            text.setFirstParagraphInColumn(true);
            box.getParagraphs().add(text);
        }

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## Добавьте плавающую рамку с цветом фона.

Используйте этот пример, когда плавающий контейнер должен иметь видимую фоновую заливку.

1. Создайте новый PDF-документ и добавьте страницу.
1. Создайте `FloatingBox`, установите цвет фона и добавьте текст.
1. Поместите поле на страницу и сохраните документ.

```java
public static void backgroundSupport(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setBackgroundColor(Color.getLightGreen());
        box.setNeedRepeating(false);
        box.getParagraphs().add(new TextFragment("text example"));

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## Разместите плавающий прямоугольник с абсолютными смещениями

Используйте этот пример, когда плавающий блок должен располагаться с точным смещением на странице.

1. Создайте страницу и подготовьте окружающий ее текстовый контент.
1. Создайте `FloatingBox`, установите абсолютное позиционирование и назначьте смещения сверху и слева.
1. Добавьте содержимое на страницу и сохраните документ.

```java
public static void offsetSupport(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setTop(45);
        box.setLeft(15);
        box.setPositioningMode(ParagraphPositioningMode.Absolute);
        box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
        box.getParagraphs().add(new TextFragment("text example 1"));

        page.getParagraphs().add(new TextFragment("text example 2"));
        page.getParagraphs().add(box);
        page.getParagraphs().add(new TextFragment("text example 3"));

        document.save(outputFile.toString());
    }
}
```

## Выравнивание текста внутри плавающих блоков

Используйте этот пример, когда плавающие блоки должны демонстрировать различное вертикальное выравнивание при одном и том же горизонтальном выравнивании.

1. Создайте новый PDF-документ и добавьте страницу.
1. Создайте несколько объектов `FloatingBox` с разными настройками выравнивания.
1. Добавьте их на страницу и сохраните результат.

```java
public static void alignTextToFloat(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox floatBox = new FloatingBox(100, 100);
        floatBox.setVerticalAlignment(VerticalAlignment.Bottom);
        floatBox.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom"));
        floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox);

        FloatingBox floatBox2 = new FloatingBox(100, 100);
        floatBox2.setVerticalAlignment(VerticalAlignment.Center);
        floatBox2.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox2.getParagraphs().add(new TextFragment("FloatingBox_center"));
        floatBox2.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox2);

        FloatingBox floatBox3 = new FloatingBox(100, 100);
        floatBox3.setVerticalAlignment(VerticalAlignment.Top);
        floatBox3.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox3.getParagraphs().add(new TextFragment("FloatingBox_top"));
        floatBox3.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox3);

        document.save(outputFile.toString());
    }
}
```
