---
title: Манипулировать PDF‑документами в Java
linktitle: Манипулировать PDF‑документом
type: docs
weight: 20
url: /ru/java/manipulate-pdf-document/
description: Узнайте, как проверять, структурировать и изменять PDF‑документы в Java, включая управление TOC и проверку PDF/A.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Проверяйте, реструктурируйте и уплощайте PDF‑документы с помощью Java.
Abstract: В этой статье объясняется, как манипулировать PDF‑документами с помощью Aspose.PDF for Java. Охватывается проверка соответствия PDF/A, добавление и настройка оглавления (TOC), скрытие или настройка номеров страниц TOC, назначение скрипта истечения и уплощение интерактивных полей формы.
---
Aspose.PDF for Java включает операции со структурой документа, выходящие за рамки простого редактирования страниц.

## Проверьте соответствие PDF/A-1a

Используйте этот пример, когда вам нужно проверить, соответствует ли документ архивному стандарту PDF/A-1a.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Выполните проверку в соответствии с требуемым [PDF-формат](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) цель.
1. Сохраните отчет проверки в указанный путь вывода.

```java
public static void validatePdfaStandardA1a(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1A);
    }
}
```

## Проверьте соответствие PDF/A-1b

Этот вариант проверяет тот же исходный документ на соответствие уровню PDF/A-1b.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вызовите метод проверки с [PDF-формат](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) значение для PDF/A-1b.
1. Запишите результат валидации в выходной файл отчета.

```java
public static void validatePdfaStandardA1b(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1B);
    }
}
```

## Добавьте оглавление

Используйте этот подход, когда документ должен включать сгенерированную страницу TOC со ссылками на страницы содержимого.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вставьте новое оглавление [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и настроить его [ИнформацияОСодержание](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Создайте [Заголовок](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) записи, указывающие на целевые страницы.
1. Сохраните обновлённый документ.

```java
public static void addTableOfContents(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().insert(1);
        TocInfo tocInfo = new TocInfo();
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(20);
        title.getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.setTitle(title);
        tocPage.setTocInfo(tocInfo);

        String[] titles = {"First page", "Second page"};
        for (int index = 0; index < titles.length && index + 2 <= document.getPages().size(); index++) {
            Heading heading = new Heading(1);
            TextSegment segment = new TextSegment(titles[index]);
            heading.setTocPage(tocPage);
            heading.getSegments().add(segment);
            Page destinationPage = document.getPages().get_Item(index + 2);
            heading.setDestinationPage(destinationPage);
            heading.setTop(destinationPage.getRect().getHeight());
            tocPage.getParagraphs().add(heading);
        }

        document.save(outputFile.toString());
    }
}
```

## Настройте уровни TOC и форматирование

Этот пример показывает, как назначить разные визуальные настройки для нескольких уровней оглавления.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте Оглавление [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и настроить [ИнформацияОСодержание](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/) форматировать массив.
1. Создайте образец [Заголовок](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) записи с разными уровнями.
1. Сохраните документ с отформатированным TOC.

```java
public static void setTocLevels(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().add();
        TocInfo tocInfo = new TocInfo();
        tocInfo.setLineDash(TabLeaderType.Solid);
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(30);
        tocInfo.setTitle(title);
        tocPage.setTocInfo(tocInfo);

        tocInfo.setFormatArrayLength(4);
        tocInfo.getFormatArray()[0].getMargin().setLeft(0);
        tocInfo.getFormatArray()[0].getMargin().setRight(30);
        tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
        tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        tocInfo.getFormatArray()[1].getMargin().setLeft(10);
        tocInfo.getFormatArray()[1].getMargin().setRight(30);
        tocInfo.getFormatArray()[1].setLineDash(3);
        tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
        tocInfo.getFormatArray()[2].getMargin().setLeft(20);
        tocInfo.getFormatArray()[2].getMargin().setRight(30);
        tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
        tocInfo.getFormatArray()[3].getMargin().setLeft(30);
        tocInfo.getFormatArray()[3].getMargin().setRight(30);
        tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

        try (Page page = document.getPages().add()) {
            for (int level = 1; level < 5; level++) {
                Heading heading = new Heading(level);
                heading.setAutoSequence(true);
                heading.setTocPage(tocPage);
                heading.getTextState().setFont(FontRepository.findFont("Arial"));
                heading.getSegments().add(new TextSegment("Sample Heading" + level));
                heading.setInList(true);
                page.getParagraphs().add(heading);
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Скройте номера страниц в оглавлении

Используйте этот пример, когда оглавление должно показывать заголовки записей без номеров страниц.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте Оглавление [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и отключить номера страниц в [ИнформацияОСодержание](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Создайте требуемое [Заголовок](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) запись и добавить её на страницу содержания.
1. Сохраните обновлённый документ.

```java
public static void hidePageNumbersInToc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page;
        Heading heading;
        try (Page tocPage = document.getPages().add()) {
            TocInfo tocInfo = new TocInfo();
            TextFragment title = new TextFragment("Table Of Contents");
            title.getTextState().setFontSize(20);
            title.getTextState().setFontStyle(FontStyles.Bold);
            tocInfo.setTitle(title);
            tocInfo.setShowPageNumbers(false);
            tocPage.setTocInfo(tocInfo);

            tocInfo.setFormatArrayLength(4);
            tocInfo.getFormatArray()[0].getMargin().setRight(0);
            tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
            tocInfo.getFormatArray()[1].getMargin().setLeft(30);
            tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
            tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
            tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
            tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

            page = document.getPages().add();
            heading = new Heading(1);
            heading.setTocPage(tocPage);
        }
        heading.setAutoSequence(true);
        heading.setInList(true);
        heading.getSegments().add(new TextSegment("this is heading of level 1"));
        page.getParagraphs().add(heading);

        document.save(outputFile.toString());
    }
}
```

## Настройте префиксы номеров страниц в TOC

Этот пример добавляет пользовательский префикс к номерам страниц, отображаемым в сгенерированном оглавлении.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вставьте оглавление [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и установить желаемый префикс номера страницы в [ИнформацияОСодержание](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Создайте [Заголовок](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) записи, указывающие на каждую страницу.
1. Сохраните обновлённый документ.

```java
public static void customizePageNumbersInToc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page tocPage = document.getPages().insert(1);
        TocInfo tocInfo = new TocInfo();
        TextFragment title = new TextFragment("Table Of Contents");
        title.getTextState().setFontSize(20);
        title.getTextState().setFontStyle(FontStyles.Bold);
        tocInfo.setTitle(title);
        tocInfo.setPageNumbersPrefix("P");
        tocPage.setTocInfo(tocInfo);

        for (int index = 1; index <= document.getPages().size(); index++) {
            Page page = document.getPages().get_Item(index);
            Heading heading = new Heading(1);
            heading.setTocPage(tocPage);
            heading.setDestinationPage(page);
            heading.setTop(page.getRect().getHeight());
            heading.getSegments().add(new TextSegment("Page " + index));
            tocPage.getParagraphs().add(heading);
        }

        document.save(outputFile.toString());
    }
}
```

## Добавьте скрипт истечения срока действия PDF

Используйте этот подход, когда документ должен выполнять JavaScript при открытии и отображать предупреждение об истечении срока после определённой даты.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте любой необходимый контент.
1. Создайте [JavascriptAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/javascriptaction/) с логикой истечения.
1. Назначьте скрипт как действие открытия документа и сохраните выходной файл.

```java
public static void setPdfExpiryDate(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(new TextFragment("Hello World..."));
        }
        JavascriptAction script = new JavascriptAction(
                "var year=2017;"
                        + "var month=5;"
                        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
                        + "expiry = new Date(year, month);"
                        + "if (today.getTime() > expiry.getTime())"
                        + "app.alert('The file is expired. You need a new one.');");
        document.setOpenAction(script);
        document.save(outputFile.toString());
    }
}
```

## Свести заполняемую PDF-форму в плоский PDF

Этот пример преобразует интерактивные поля формы в статическое содержимое страницы, поэтому полученный документ больше не может быть отредактирован как форма.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Проверьте, содержит ли документ виджеты формы.
1. Сделайте плоским каждый [Поле](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) представлен(а) [WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
1. Сохраните уплощенный документ.

```java
public static void flattenFillablePdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```


