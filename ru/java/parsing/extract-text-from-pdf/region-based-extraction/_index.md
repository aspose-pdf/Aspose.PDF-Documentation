---
title: Региональное извлечение с Java
linktitle: Региональное извлечение
type: docs
weight: 20
url: /ru/java/region-based-extraction/
description: Узнайте, как извлекать текст из определённого региона страницы или проверять геометрию абзацев в PDF‑документах с помощью Aspose.PDF for Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Извлеките текста из прямоугольного региона страницы

использовать `TextSearchOptions` с `Rectangle` ограничить извлечение определённой областью на странице.

1. Откройте исходный PDF в [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) для сбора текста с выбранной области страницы.
1. Создайте [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/textsearchoptions/) для цели [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) и включить `setLimitToPageBounds(true)` чтобы извлечение оставалось внутри видимой области страницы.
1. Примените настроенные параметры поиска к поглотителю и перейдите к целевому объекту. [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Запишите извлечённый буфер текста в выходной файл.

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

## Извлеките абзацы с геометрической информацией

использовать `ParagraphAbsorber` для проверки прямоугольников секций и многоугольников абзацев вместе с извлечённым текстом.

1. Откройте исходный PDF в [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) экземпляр.
1. Создайте [ParagraphAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/paragraphabsorber/) и перейдите к цели [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) для создания информации о разметке страницы.
1. Прочитайте первый результат разметки страницы и пройдитесь по его секциям и абзацам.
1. Соберите каждый прямоугольник секции, полигон абзаца и реконструированный из него текст абзаца [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) строки.
1. Создайте отчет вывода с геометрией и деталями извлечённого текста.
1. Запишите извлечённые детали в выходной файл.

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


