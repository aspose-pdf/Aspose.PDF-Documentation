---
title: Интерактивные аннотации с использованием Java
linktitle: Интерактивные аннотации
type: docs
weight: 60
url: /ru/java/interactive-annotations/
description: Узнайте, как добавлять, просматривать и удалять аннотации ссылок в PDF‑документах с использованием Aspose.PDF for Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Работайте с интерактивными PDF‑аннотациями в Java.
Abstract: В этой статье объясняется, как работать с интерактивными аннотациями ссылок в PDF‑файлах с использованием Aspose.PDF for Java. Описывается поиск текста, создание аннотации ссылки над найденной областью текста, чтение существующих аннотаций ссылок и их удаление.
---
Интерактивные аннотации в этом разделе сосредоточены на рабочих процессах, основанных на ссылках и кнопках, которые реагируют на действия пользователя внутри просмотрщика PDF.

## Добавьте аннотацию ссылки

Используйте этот пример, когда вам нужно разместить кликабельную ссылку поверх текста, найденного на странице.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Найдите целевой фрагмент текста и создайте [Аннотация ссылки](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) над его прямоугольником.
1. Назначить [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) и сохраните обновлённый документ.

```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        var phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);
        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1),
                phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("https://www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```

## Получите аннотации ссылок

Этот пример сканирует коллекцию аннотаций страницы и сообщает местоположение каждой аннотации ссылки.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Перебрать аннотации на целевой странице.
1. Фильтровать аннотации по [Тип аннотации](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link` и вывести их прямоугольники.

```java
public static void linkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## Удалите аннотации ссылок

Используйте этот подход, когда необходимо удалить существующие аннотации ссылок со страницы.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Собрать аннотации, тип которых [Тип аннотации](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link`.
1. Удалите собранные аннотации и сохраните выходной файл.

```java
public static void linkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
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

Этот пример создает интерактивную линейную аннотацию со стилями стрелок, настройками границы и всплывающей заметкой.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [Линейная аннотация](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/) с начальной и конечной точками.
1. Настройте его внешний вид и всплывающую аннотацию, затем сохраните документ.

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

## Добавьте кнопки навигации

Используйте этот пример, когда PDF должен включать кнопки «previous-page» и «next-page» для интерактивной навигации.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и убедитесь, что документ содержит требуемые страницы.
1. Создайте [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) элементы управления с предопределёнными действиями навигации.
1. Добавьте кнопки в коллекцию Form и сохраните обновлённый документ.

```java
public static void navigationButtonsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();

        record ButtonConfig(String name, double xPos, PredefinedAction action) {}
        List<ButtonConfig> buttonConfigs = List.of(
                new ButtonConfig("Previous Page", 120.0, PredefinedAction.PrevPage),
                new ButtonConfig("Next Page", 230.0, PredefinedAction.NextPage));

        for (Page page : document.getPages()) {
            for (ButtonConfig config : buttonConfigs) {
                Rectangle rect = new Rectangle(config.xPos(), 10.0, config.xPos() + 100, 40.0, true);
                ButtonField button = new ButtonField(page, rect);
                button.setPartialName(config.name());
                button.setValue(config.name());
                button.getCharacteristics().setBorder(Color.getRed());
                button.getCharacteristics().setBackground(Color.getOrange().toRgb());
                button.getAnnotationActions().setOnReleaseMouseBtn(new NamedAction(config.action()));
                document.getForm().add(button);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## Добавьте кнопку печати

В этом примере создаётся кнопка, которая запускает команду печати, когда пользователь нажимает её.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить страницу.
1. Создайте [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) и назначьте предварительно определённое действие печати.
1. Настройте границу и фон кнопки, добавьте её в форму и сохраните документ.

```java
public static void printButtonAdd(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle rect = new Rectangle(72, 748, 164, 768, true);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("Print current document");
        printButton.setColor(Color.getBlack());
        printButton.setPartialName("printBtn1");
        printButton.setValue("Print Document");
        printButton.getAnnotationActions().setOnReleaseMouseBtn(
                new NamedAction(PredefinedAction.File_Print));

        Border border = new Border(printButton);
        border.setStyle(BorderStyle.Solid);
        border.setWidth(2);
        printButton.setBorder(border);

        printButton.getCharacteristics().setBorder(Color.getBlue());
        printButton.getCharacteristics().setBackground(Color.getLightBlue().toRgb());

        document.getForm().add(printButton);
        document.save(outputFile.toString());
    }
}
```


