---
title: Extract Paragraph from PDF 
linktitle: Extract Paragraph
type: docs
weight: 20
url: /java/extract-paragraph-from-pdf/
description: Discover how to extract paragraphs from a PDF document in Java with Aspose.PDF for easier content analysis.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to Extract Paragraph from PDF with Aspose.PDF for Java
Abstract: The article discusses methods for extracting text from PDF documents in the form of paragraphs using a specialized `ParagraphAbsorber` class. This functionality allows users to either draw borders around sections and paragraphs on a PDF page or iterate through the collection of paragraphs to retrieve their text. The first method involves visually marking the text's boundaries on the page using Java code to draw rectangles and polygons, highlighting the sections and paragraphs. The second method involves programmatically iterating over the paragraphs to extract and print their text content, providing a structured overview of the document's layout. Both approaches utilize the `ParagraphAbsorber` class, demonstrating its capabilities in managing PDF text extraction tasks.
SoftwareApplication: java
---

## Extract Text from PDF document in Paragraphs form

We can get text from a PDF document by searching a particular text (using "plain text" or "regular expressions") from a single page or whole document, or we can get the complete text of a single page, range of pages or complete document. However, in some cases, you require to extract paragraphs from a PDF document or text in the form of Paragraphs. We have implemented functionality for searching sections and paragraphs in the text of PDF document pages. We have introduced ParagraphAbsorber Class (like TextFragmentAbsorber and TextAbsorber), which can be used to extract paragraphs from PDF documents. There are two following ways in which you can use ParagraphAbsorber:

**1- By drawing the border of sections and paragraphs of text on PDF page:**

```java
public static void ExtractParagraph() {
    // The path to the documents directory.
    Document doc = new Document(_dataDir + "input.pdf");
    Page page = doc.getPages().get_Item(2);

    ParagraphAbsorber absorber = new ParagraphAbsorber();
    absorber.visit(page);

    PageMarkup markup = absorber.getPageMarkups().get(0);

    for (MarkupSection section : markup.getSections()) {
        DrawRectangleOnPage(section.getRectangle(), page);
        for (MarkupParagraph paragraph : section.getParagraphs()) {
            DrawPolygonOnPage(paragraph.getPoints(), page);
        }
    }

    doc.save(_dataDir + "output_out.pdf");
}

private static void DrawRectangleOnPage(Rectangle rectangle, Page page) {
    page.getContents().add(new GSave());
    page.getContents().add(new ConcatenateMatrix(1, 0, 0, 1, 0, 0));
    page.getContents().add(new SetRGBColorStroke(0, 1, 0));
    page.getContents().add(new SetLineWidth(2));
    page.getContents().add(new Re(rectangle.getLLX(), rectangle.getLLY(), rectangle.getWidth(), rectangle.getHeight()));
    page.getContents().add(new ClosePathStroke());
    page.getContents().add(new GRestore());
}

private static void DrawPolygonOnPage(Point[] polygon, Page page) {
    page.getContents().add(new GSave());
    page.getContents().add(new ConcatenateMatrix(1, 0, 0, 1, 0, 0));
    page.getContents().add(new SetRGBColorStroke(0, 0, 1));
    page.getContents().add(new SetLineWidth(1));
    page.getContents().add(new MoveTo(polygon[0].getX(), polygon[0].getY()));
    for (int i = 1; i < polygon.length; i++) {
        page.getContents().add(new LineTo(polygon[i].getX(), polygon[i].getY()));
    }
    page.getContents().add(new LineTo(polygon[0].getX(), polygon[0].getY()));
    page.getContents().add(new ClosePathStroke());
    page.getContents().add(new GRestore());
}
```

**2- By iterating through paragraphs collection and get the text of them:**

```java
public static void ExtractParagraph02() {
        // Open an existing PDF file
        Document doc = new Document(_dataDir + "input.pdf");
        // Instantiate ParagraphAbsorber
        ParagraphAbsorber absorber = new ParagraphAbsorber();
        absorber.visit(doc);

        for (PageMarkup markup : absorber.getPageMarkups()) {
            int i = 1;
            for (MarkupSection section : markup.getSections()) {
                int j = 1;

                for (MarkupParagraph paragraph : section.getParagraphs()) {
                    StringBuilder paragraphText = new StringBuilder();

                    for (java.util.List<TextFragment> line : paragraph.getLines()) {
                        for (TextFragment fragment : line) {
                            paragraphText.append(fragment.getText());
                        }
                        paragraphText.append("\r\n");
                    }
                    paragraphText.append("\r\n");

                    System.out.println("Paragraph "+j+" of section "+ i + " on page"+ ":"+markup.getNumber());
                    System.out.println(paragraphText.toString());

                    j++;
                }
                i++;
            }
        }
    }
```
