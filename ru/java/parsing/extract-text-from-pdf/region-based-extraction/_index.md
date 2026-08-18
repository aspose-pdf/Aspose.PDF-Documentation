---
title: Извлечение на основе регионов с использованием Java
linktitle: Региональное извлечение
type: docs
weight: 20
url: /java/region-based-extraction/
description: Узнайте, как извлечь текст из определенной области страницы или проверить геометрию абзацев в PDF-документах с помощью Aspose.PDF для Java.
lastmod: "2026-06-16"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Извлечение текста из прямоугольной области страницы

Используйте `TextSearchOptions` с `Rectangle`, чтобы ограничить извлечение определенной областью на странице.

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) для сбора текста из выбранной области страницы.
1. Создайте [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsearchoptions/) для целевого объекта [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) и включите `setLimitToPageBounds(true)`, чтобы извлечение оставалось внутри видимого поля страницы.
1. Примените настроенные параметры поиска к поглотителю и посетите целевую [Страницу](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Запишите извлеченный текстовый буфер в выходной файл.

```java
public static void extractTextFromRegion(Path inputFile, Path outputFile, int pageNumber, Rectangle rectangle)
        throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextAbsorber absorber = new TextAbsorber();
        TextSearchOptions options = new TextSearchOptions(rectangle);
        options.setLimitToPageBounds(true);
        absorber.setTextSearchOptions(options);
        document.getPages().get_Item(pageNumber).accept(absorber);
        Files.writeString(outputFile, absorber.getText());
    }
}
```

## Извлечение абзацев с информацией о геометрии

Используйте `ParagraphAbsorber` для проверки прямоугольников разделов и многоугольников абзацев вместе с извлеченным текстом.

1. Откройте исходный PDF-файл в экземпляре [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Создайте [ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) и посетите целевую [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/), чтобы создать информацию о разметке страницы.
1. Прочитайте первый результат разметки страницы и просмотрите его разделы и абзацы.
1. Соберите каждый прямоугольник раздела, многоугольник абзаца и текст абзаца, восстановленный из его строк [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Создайте выходной отчет с геометрией и извлеченными текстовыми деталями.
1. Запишите извлеченные данные в выходной файл.

```java
public static void extractParagraphsWithGeometry(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        PageMarkup pageMarkup = absorber.getPageMarkups().get(0);
        StringBuilder text = new StringBuilder();
        int sectionIndex = 1;
        for (MarkupSection section : pageMarkup.getSections()) {
            text.append("Section ").append(sectionIndex)
                    .append(": rectangle = ").append(section.getRectangle()).append("\n");
            int paragraphIndex = 1;
            for (MarkupParagraph paragraph : section.getParagraphs()) {
                text.append("  Paragraph ").append(paragraphIndex)
                        .append(": polygon = ").append(Arrays.toString(paragraph.getPoints())).append("\n");
                StringBuilder paragraphText = new StringBuilder();
                for (List<TextFragment> line : paragraph.getLines()) {
                    for (TextFragment fragment : line) {
                        paragraphText.append(fragment.getText());
                    }
                    paragraphText.append("\r\n");
                }
                text.append("    Text: ").append(paragraphText).append("\n\n");
                paragraphIndex++;
            }
            sectionIndex++;
        }

        Files.writeString(outputFile, text.toString());
    }
}
```
