---
title: Creating a complex PDF
linktitle: Creating a complex PDF
type: docs
weight: 30
url: /java/complex-pdf-example/
description: Aspose.PDF for Java allows you to create more complex PDF documents that contain images, text fragments, and tables in one file.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Create a complex PDF using Java
Abstract: This article shows how to create a more complex PDF in Java using Aspose.PDF. The example adds an image, a formatted heading, a descriptive text block, and a table with styled header cells and generated schedule rows, then saves the result as a PDF document.
---
The [Hello World](/pdf/java/hello-world-example/) example covers the simplest PDF creation path. This example builds on that workflow and creates a richer document that combines graphics, text, and tabular content.

To create a more complex PDF document in Java:

1. Create a [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and add a [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Add an image to the [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) with `page.addImage(...)` and a target [Rectangle](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/rectangle/).
1. Create a header [TextFragment](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragment/) and set its font, size, alignment, and [Position](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/position/).
1. Create a second [TextFragment](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragment/) for the description paragraph.
1. Build a [Table](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/table/) with borders, padding, and header styling.
1. Add generated schedule rows to the [Table](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/table/).
1. Append the [Table](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/table/) to the [Page](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) paragraphs.
1. Save the output PDF [Document](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/).

The following Java code is based on `GetStartedExamples.java`.

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

The same example uses a helper method to prepare the schedule table with header formatting and generated departure times:

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
