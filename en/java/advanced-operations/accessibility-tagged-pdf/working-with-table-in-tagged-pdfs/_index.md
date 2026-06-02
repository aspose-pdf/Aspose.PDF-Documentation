---
title: Work with Tables in Tagged PDFs in Java
linktitle: Working with Table in Tagged PDFs
type: docs
weight: 40
url: /java/working-with-table-in-tagged-pdfs/
description: Learn how to work with accessible tables in tagged PDFs in Java with Aspose.PDF, including table structure, cell spans, styling, row settings, and positioning.
lastmod: "2026-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Tagged table APIs let you create accessible table structures with explicit headers, body rows, footers, and per-cell semantics.

## Create a tagged table

1. Initialize the PDF document and any resources required by this example.
2. Build and configure the Aspose.PDF objects needed to create a tagged table.
3. Save the output document or generated file.

```java
public static void createTable(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example table");
        taggedContent.setLanguage("en-US");

        TableElement tableElement = taggedContent.createTableElement();
        taggedContent.getRootElement().appendChild(tableElement, true);
        tableElement.setBorder(new BorderInfo(BorderSide.All, 1.2f, Color.getDarkBlue()));

        fillTable(tableElement, 50, 4, true);

        StructureAttributes tableAttributes = tableElement.getAttributes().getAttributes(AttributeOwnerStandard.Table);
        StructureAttribute summaryAttribute = new StructureAttribute(AttributeKey.Summary);
        summaryAttribute.setStringValue("The summary text for table");
        tableAttributes.setAttribute(summaryAttribute);

        document.save(outputFile.toString());
    }
}
```

## Apply table styling

The table examples also demonstrate:

- background colors and borders
- repeating rows and repeating columns
- column widths and auto-fit behavior
- row-level styling, fixed height, and page-breaking behavior
- cell-level styling, row span, and column span

## Adjust tagged table position

1. Open or create the PDF document used in this example.
2. Use the Aspose.PDF API calls shown in the snippet to adjust tagged table position.
3. Save the document or inspect the result, depending on the scenario.

```java
public static void adjustTablePosition(Path outputFile) {
    try (Document document = new Document()) {
        ITaggedContent taggedContent = document.getTaggedContent();
        taggedContent.setTitle("Example table position");
        taggedContent.setLanguage("en-US");

        TableElement tableElement = taggedContent.createTableElement();
        taggedContent.getRootElement().appendChild(tableElement, true);

        PositionSettings positionSettings = new PositionSettings();
        positionSettings.setHorizontalAlignment(HorizontalAlignment.None);
        positionSettings.setMargin(new MarginInfo(20, 0, 0, 0));
        positionSettings.setVerticalAlignment(VerticalAlignment.None);
        positionSettings.setFirstParagraphInColumn(false);
        positionSettings.setKeptWithNext(false);
        positionSettings.setInNewPage(false);
        positionSettings.setInLineParagraph(false);
        tableElement.adjustPosition(positionSettings);

        fillTable(tableElement, 4, 4, true);
        document.save(outputFile.toString());
    }
}
```
