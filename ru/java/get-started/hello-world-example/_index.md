---
title: Пример Hello World с использованием Java
linktitle: Пример Hello World
type: docs
weight: 20
url: /ru/java/hello-world-example/
description: Этот пример демонстрирует, как создать простой PDF‑документ со стилизованным текстом Hello World с использованием Aspose.PDF for Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Пример Hello World через Java
Abstract: В этой статье предоставлен пример Hello World для Aspose.PDF for Java. Пример создает новый PDF‑документ, добавляет страницу, создает объект TextFragment с пользовательским расположением, шрифтом и цветами, добавляет текст на страницу с помощью TextBuilder и сохраняет результат как PDF‑файл.
---
Пример "Hello World" — это самый простой путь к пониманию базового рабочего процесса создания PDF. В этой статье пример создает новый PDF, размещает стилизованный фрагмент текста на странице и сохраняет выходной файл.

Пример на Java включает следующие шаги:

1. Создайте [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) объект.
1. Добавьте [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) к документу.
1. Создайте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) с текстом `Hello, world!`.
1. Установите [Position](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/), шрифт, размер шрифта, цвет фона и цвет переднего плана через фрагмент [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstate/).
1. Создайте [TextBuilder](https://reference.aspose.com/pdf/java/com.aspose.pdf/textbuilder/) для страницы.
1. Добавьте [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) к [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Сохраните PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

Следующий код на Java основан на `GetStartedExamples.java`.

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


