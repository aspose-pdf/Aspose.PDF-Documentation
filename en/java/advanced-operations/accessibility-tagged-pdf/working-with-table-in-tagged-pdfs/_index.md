---
title: Work with Tables in Tagged PDFs in Java
linktitle: Working with Table in Tagged PDFs
type: docs
weight: 40
url: /java/working-with-table-in-tagged-pdfs/
description: Learn how to work with accessible tables in tagged PDFs in Java with Aspose.PDF, including table structure, cell spans, styling, row settings, and positioning.
lastmod: "2026-06-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
Tagged table APIs let you create accessible table structures with explicit headers, body rows, footers, and per-cell semantics.

## Create a tagged table

1. Create a new PDF document.
1. Get the document's tagged content.
1. Set the tagged document title and language.
1. Create a table element and append it to the root structure.
1. Set the table border style.
1. Fill the table with rows and cells.
1. Get the standard table structure attributes.
1. Create and assign a summary attribute for the table.
1. Save the tagged PDF document.

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

1. Create a new PDF document.
1. Get the document's tagged content.
1. Set the tagged document title and language.
1. Create a table element and append it to the root structure.
1. Create position settings for the table.
1. Set horizontal alignment, margin, vertical alignment, and flow options.
1. Apply the position settings to the table element.
1. Fill the table with rows and cells.
1. Save the tagged PDF document.

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
