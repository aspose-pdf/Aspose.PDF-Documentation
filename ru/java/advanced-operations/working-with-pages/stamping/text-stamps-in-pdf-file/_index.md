---
title: Добавить текстовые штампы в PDF на Java
linktitle: Текстовые штампы в PDF-файле
type: docs
weight: 20
url: /ru/java/text-stamps-in-the-pdf-file/
description: Узнайте, как добавить текстовые штампы в PDF‑документы на Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавьте текстовые штампы в PDF‑файлы с помощью Java
Abstract: В этой статье объясняется, как добавить текстовые штампы в PDF‑файлы с использованием Aspose.PDF for Java. Рассматривается создание фонового текстового штампа, его позиционирование, вращение, а также настройка шрифта, размера, стиля и цвета.
---
Используйте текстовые штампы, когда необходимо добавить видимые метки или водяные знаки на страницы PDF.

## Добавьте текстовый штамп

Используйте этот пример, когда страница должна отображать повернутый текстовый штамп с пользовательским оформлением.

1. Откройте исходный PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/textstamp/) и настройте его размещение и внешний вид текста.
1. Добавьте штамп на целевую страницу и сохраните документ.

```java
public static void addTextStamp(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextStamp textStamp = new TextStamp("Sample Stamp");
        textStamp.setBackground(true);
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        textStamp.setRotate(Rotation.on90);
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0f);
        textStamp.getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getDarkGreen());
        document.getPages().get_Item(1).addStamp(textStamp);
        document.save(outputFile.toString());
    }
}
```

