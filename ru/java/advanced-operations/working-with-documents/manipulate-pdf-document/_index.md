---
title: Управление PDF-документами в Java
linktitle: Управление PDF-документом
type: docs
weight: 20
url: /java/manipulate-pdf-document/
description: Узнайте, как проверять, структурировать и изменять PDF-документы на Java, включая управление оглавлением и проверки PDF/A.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Проверка, реструктуризация и выравнивание PDF-документов с помощью Java
Abstract: В этой статье объясняется, как манипулировать PDF-документами с помощью Aspose.PDF для Java. Он охватывает проверку соответствия PDF/A, добавление и настройку оглавления, скрытие или настройку номеров страниц содержания, назначение сценария истечения срока действия и выравнивание полей интерактивной формы.
---
Aspose.PDF для Java включает в себя операции со структурой документа, выходящие за рамки простого редактирования страниц.

## Проверка соответствия PDF/A-1a

Используйте этот пример, когда вам нужно проверить, соответствует ли документ архивному стандарту PDF/A-1a.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Запустите проверку по требуемому целевому объекту [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/).
1. Сохраните отчет о проверке в указанном пути вывода.

```java
public static void validatePdfaStandardA1a(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1A);
    }
}
```

## Проверка соответствия PDF/A-1b

Этот вариант проверяет тот же исходный документ на соответствие уровню соответствия PDF/A-1b.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вызовите метод проверки со значением [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) для PDF/A-1b.
1. Запишите результат проверки в выходной файл отчета.

```java
public static void validatePdfaStandardA1b(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.validate(outputFile.toString(), PdfFormat.PDF_A_1B);
    }
}
```

## Добавьте оглавление

Используйте этот подход, когда документ должен включать сгенерированную страницу содержания со ссылками на страницы контента.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вставьте новую оглавление [страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и настройте ее [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Создайте записи [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/), указывающие на целевые страницы.
1. Сохраните обновленный документ.

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

## Настройте уровни содержания и форматирование

В этом примере показано, как назначить различные визуальные настройки нескольким уровням оглавления.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте оглавление [страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и настройте массив формата [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Создайте образцы записей [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) с разными уровнями.
1. Сохраните документ с отформатированным содержанием.

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

## Скрыть номера страниц в оглавлении

Используйте этот пример, когда в оглавлении должны отображаться заголовки записей без номеров страниц.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте оглавление [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и отключите номера страниц в [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Создайте необходимую запись [Заголовок](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/) и добавьте ее на страницу содержимого.
1. Сохраните обновленный документ.

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

## Настройте префиксы номеров страниц оглавления

В этом примере добавляется пользовательский префикс к номерам страниц, отображаемым в созданном оглавлении.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Вставьте оглавление [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) и установите нужный префикс номера страницы в [TocInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo/).
1. Создайте записи [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/heading/), указывающие на каждую страницу.
1. Сохраните обновленный документ.

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

## Добавьте сценарий истечения срока действия PDF

Используйте этот подход, когда документ должен запускать JavaScript при открытии и отображать предупреждение об истечении срока действия после определенной даты.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте необходимое содержимое.
1. Создайте [JavascriptAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/javascriptaction/) с логикой истечения срока действия.
1. Назначьте сценарий в качестве действия открытия документа и сохраните выходной файл.

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

## Сведение заполняемой PDF-формы

В этом примере поля интерактивной формы преобразуются в статическое содержимое страницы, поэтому полученный документ больше нельзя редактировать как форму.

1. Откройте исходный PDF-файл [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Проверьте, содержит ли документ виджеты форм.
1. Сгладьте каждое [Поле](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/), представленное [WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/).
1. Сохраните сведенный документ.

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
