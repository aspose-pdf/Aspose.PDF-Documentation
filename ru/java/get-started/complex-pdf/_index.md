---
title: Создание сложного PDF
linktitle: Создание сложного PDF
type: docs
weight: 30
url: /ru/java/complex-pdf-example/
description: Aspose.PDF for Java позволяет создавать более сложные PDF‑документы, содержащие изображения, фрагменты текста и таблицы в одном файле.
lastmod: "2026-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создайте сложный PDF с использованием Java
Abstract: В этой статье показано, как создать более сложный PDF в Java с использованием Aspose.PDF. В примере добавляются изображение, отформатированный заголовок, описательный текстовый блок и таблица со стилизованными ячейками заголовка и сгенерированными строками расписания, после чего результат сохраняется в виде PDF‑документа.
---
Пример [Hello World](/pdf/ru/java/hello-world-example/) демонстрирует базовый процесс создания PDF. Этот пример развивает его: в документ добавляются графика, текст и таблица.

Чтобы создать более сложный PDF-документ в Java:

1. Создайте объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавьте страницу [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Добавьте изображение на страницу [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) с помощью `page.addImage(...)`, указав область размещения [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Создайте заголовок с помощью [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) и установите его шрифт, размер, выравнивание и [Position](https://reference.aspose.com/pdf/java/com.aspose.pdf/position/).
1. Создайте второй [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) для абзаца описания.
1. Создайте [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) с границами, отступами и стилизацией заголовка.
1. Добавьте сгенерированные строки расписания в [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/).
1. Добавьте таблицу [Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/table/) в коллекцию абзацев страницы [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/).
1. Сохраните объект [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) в формате PDF.

Следующий код Java основан на `GetStartedExamples.java`.

```java
public static void complexExample(Path imageFile, Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        page.addImage(imageFile.toString(), new Rectangle(20, 730, 120, 830, true));

        TextFragment header = new TextFragment("New ferry routes in Fall 2029");
        header.getTextState().setFont(FontRepository.findFont("Arial"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment(HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        String descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. "
                + "Ferry service is operating at half capacity and on a reduced schedule. "
                + "Expect lineups.";
        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);

        page.getParagraphs().add(createScheduleTable());

        document.save(outputFile.toString());
    }
}
```

В этом же примере используется вспомогательный метод для подготовки таблицы расписания с форматированием заголовков и сгенерированным временем отправления:

```java
private static Table createScheduleTable() {
    Table table = new Table();
    table.setColumnWidths("200 200");
    table.setBorder(new BorderInfo(BorderSide.Box, 1.0f, Color.getDarkSlateGray()));
    table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
    table.setDefaultCellPadding(new MarginInfo(4.5, 4.5, 4.5, 4.5));
    table.getMargin().setBottom(10);
    table.getDefaultCellTextState().setFont(FontRepository.findFont("Helvetica"));

    Row headerRow = table.getRows().add();
    Cell departsCityCell = headerRow.getCells().add("Departs City");
    Cell departsIslandCell = headerRow.getCells().add("Departs Island");
    styleHeaderCell(departsCityCell);
    styleHeaderCell(departsIslandCell);

    Duration time = Duration.ofHours(6);
    Duration increment = Duration.ofMinutes(30);
    for (int index = 0; index < 10; index++) {
        Row dataRow = table.getRows().add();
        dataRow.getCells().add(formatTime(time));
        time = time.plus(increment);
        dataRow.getCells().add(formatTime(time));
    }

    return table;
}
```


