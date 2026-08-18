---
title: Пример Hello World с использованием Java
linktitle: Привет, мир, пример
type: docs
weight: 20
url: /java/hello-world-example/
description: В этом примере показано, как создать простой PDF-документ со стилизованным текстом Hello World с помощью Aspose.PDF для Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Пример Hello World через Java
Abstract: В этой статье представлен пример Hello World для Aspose.PDF для Java. В примере создается новый документ PDF, добавляется страница, создается TextFragment с настраиваемым положением, шрифтом и цветами, добавляется текст на страницу с помощью TextBuilder и сохраняется результат в виде PDF-файла.
---
Пример «Hello World» — это кратчайший путь к пониманию основного рабочего процесса создания PDF-файлов. В этой статье в примере создается новый PDF-файл, размещается на странице стилизованный фрагмент текста и сохраняется выходной файл.

Пример Java следует следующим шагам:

1. Создайте объект [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Добавьте [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) в документ.
1. Создайте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) с текстом `Hello, world!`.
1. Установите [Позицию](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/), шрифт, размер шрифта, цвет фона и цвет переднего плана через фрагмент [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. Создайте [TextBuilder](https://reference.aspose.com/pdf/java/com.aspose.pdf/textbuilder/) для страницы.
1. Добавьте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) к [Странице](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Сохраните PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

Следующий код Java основан на `GetStartedExamples.java`.

```java
public static void simpleExample(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        TextFragment textFragment = new TextFragment("Hello, world!");
        textFragment.setPosition(new Position(100, 600));
        textFragment.getTextState().setFontSize(12);
        textFragment.getTextState().setFont(FontRepository.findFont("TimesNewRoman"));
        textFragment.getTextState().setBackgroundColor(Color.getBlue());
        textFragment.getTextState().setForegroundColor(Color.getYellow());

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(textFragment);

        document.save(outputFile.toString());
    }
}
```
