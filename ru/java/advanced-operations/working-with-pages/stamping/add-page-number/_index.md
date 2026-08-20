---
title: Добавить номера страниц в PDF на Java
linktitle: Добавление номера страницы
type: docs
weight: 30
url: /ru/java/add-page-number/
description: Узнайте, как добавить штампы с номерами страниц в PDF‑документы на Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавьте штампы с номерами страниц в PDF‑файлы с помощью Java
Abstract: В этой статье объясняется, как добавить штампы с номерами страниц, используя Aspose.PDF for Java. Описывается стандартная нумерация страниц с пользовательским оформлением шрифта и нумерация римскими цифрами с настраиваемым начальным номером.
---
## Добавьте штамп с номером страницы

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) объект.
1. Настройте необходимые параметры размещения штампа и нумерации.
1. Установите требуемые параметры форматирования текста, включая [FontRepository](https://reference.aspose.com/pdf/java/com.aspose.pdf/fontrepository/) и [Цвет](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Добавьте настроенный [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/pagenumberstamp/) к целевому [Страница](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Сохраните обновлённый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addPageNumStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PageNumberStamp pageNumberStamp = new PageNumberStamp();
        pageNumberStamp.setBackground(false);
        pageNumberStamp.setFormat("Page # of " + document.getPages().size());
        pageNumberStamp.setBottomMargin(10);
        pageNumberStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        pageNumberStamp.setStartingNumber(1);
        pageNumberStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        pageNumberStamp.getTextState().setFontSize(14.0f);
        pageNumberStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        pageNumberStamp.getTextState().setForegroundColor(Color.getBlueViolet());

        document.getPages().get_Item(1).addStamp(pageNumberStamp);
        document.save(outputFile.toString());
    }
}
```


