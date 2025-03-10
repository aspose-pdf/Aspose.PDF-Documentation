---
title: Creating a complex PDF 
linktitle: Creating a complex PDF
type: docs
weight: 60
url: /java/complex-pdf-example/
description: Aspose.PDF for Java allows you to create more complex documents that contain images, text fragments, and tables in one document.
lastmod: "2025-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Generate complex PDF with Aspose.PDF for Java
Abstract: The article provides a detailed guide on creating a complex PDF document using Java and the Aspose.PDF library. The example document simulates one from a fictitious passenger ferry service company and includes an image, text fragments (header and paragraph), and a table. The process is built upon a Document Object Model (DOM) approach, which is further explained in the linked section "Basics of DOM API". The article outlines a step-by-step method for document creation - initializing a Document object, adding a Page, and incorporating an Image using various PDF operators such as GSave, ConcatenateMatrix, Do, and GRestore. A header and a descriptive paragraph are added using TextFragment objects, formatted with specific fonts and alignments. A table is constructed with defined properties and populated with rows of data. The complete document is then saved as "Complex.pdf". The provided Java code illustrates these operations, showcasing the integration of Aspose.PDF functionalities to achieve the desired complex document structure.
SoftwareApplication: java
---

The [Hello, World](/pdf/java/hello-world-example/) example showed simple steps to create a PDF document using Java and Aspose.PDF. In this article, we will take a look at creating a more complex document with Java and Aspose.PDF for Java. As an example, we'll take a document from a fictitious company that operates passenger ferry services.
Our document will contain a image, two text fragments (header and paragraph), and a table. To build such a document, we will use DOM-base approach. You can read more in section [Basics of DOM API](/pdf/java/basics-of-dom-api/).

If we create a document from scratch we need to follow certain steps:

1. Instantiate a [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document) object. In this step we will create an empty PDF document with some metadata but without pages.
1. Add a [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) to the document object. So, now our document will have one page.
1. Add a [Image](https://reference.aspose.com/pdf/java/com.aspose.pdf/image). It's a complex operation based on low level actions with PDF operators.
    - Load image from stream
    - Add image to Images collection of Page Resources
    - Using GSave operator: this operator saves current graphics state.
    - Create a [Matrix](https://reference.aspose.com/pdf/java/com.aspose.pdf/matrix/) object.
    - Using ConcatenateMatrix operator: defines how image must be placed.
    - Using Do operator: this operator draws image.
    - Using GRestore operator: this operator restores graphics state.
1. Create a [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) for header. For the header we will use Arial font with font size 24pt and center alignment.
1. Add header to the page [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Create a [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) for description. For the description we will use Arial font with font size 24pt and center alignment.
1. Add (description) to the page Paragraphs.
1. Create a table, add table properties.
1. Add (table) to the page [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Save a document "Complex.pdf".

```java
package com.aspose.pdf.examples;

/**
 * Complex Example
 */

import java.io.FileNotFoundException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.Duration;
import java.time.LocalTime;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.ConcatenateMatrix;
import com.aspose.pdf.operators.Do;
import com.aspose.pdf.operators.GRestore;
import com.aspose.pdf.operators.GSave;

public final class ComplexExample {

    private ComplexExample() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/");

    public static void main(String[] args) throws FileNotFoundException {
        // Initialize document object
        Document document = new Document();
        // Add page
        Page page = document.getPages().add();

        // -------------------------------------------------------------
        // Add image
        Path imageFileName = Paths.get(_dataDir.toString(),"logo.png");
        java.io.FileInputStream imageStream = new java.io.FileInputStream(new java.io.File(imageFileName.toString()));
        // Add image to Images collection of Page Resources
        page.getResources().getImages().add(imageStream);

        // Using GSave operator: this operator saves current graphics state
        page.getContents().add(new GSave());
        Rectangle _logoPlaceHolder = new Rectangle(20, 730, 120, 830);

        // Create Matrix object
        Matrix matrix = new Matrix(new double[] {
            _logoPlaceHolder.getURX() - _logoPlaceHolder.getLLX(), 0, 0,
            _logoPlaceHolder.getURY() - _logoPlaceHolder.getLLY(),
            _logoPlaceHolder.getLLX(), _logoPlaceHolder.getLLY() });

        // Using ConcatenateMatrix (concatenate matrix) operator: defines how image must be placed
        page.getContents().add(new ConcatenateMatrix(matrix));
        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // Using Do operator: this operator draws image
        page.getContents().add(new Do(ximage.getName()));
        // Using GRestore operator: this operator restores graphics state
        page.getContents().add(new GRestore());

        // -------------------------------------------------------------
        // Add Header
        TextFragment header = new TextFragment("New ferry routes in Fall 2020");
        header.getTextState().setFont(FontRepository.findFont("Arial"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment (HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        // Add description
        String descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. Ferry service is operating at half capacity and on a reduced schedule. Expect lineups.";
        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Times New Roman"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);


        // Add table
        Table table = new Table();
        table.setColumnWidths("200");
        table.setBorder(new BorderInfo(BorderSide.Box, 1f, Color.getDarkSlateGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
        table.getMargin().setBottom(10);
        table.getDefaultCellTextState().setFont(FontRepository.findFont("Helvetica"));

        Row headerRow = table.getRows().add();
        headerRow.getCells().add("Departs City");
        headerRow.getCells().add("Departs Island");

        for (Cell headerRowCell : headerRow.getCells())
        {
            headerRowCell.setBackgroundColor(Color.getGray());
            headerRowCell.getDefaultCellTextState().setForegroundColor(Color.getWhiteSmoke());
        }

        LocalTime time = LocalTime.of(6,0);
        Duration incTime = Duration.ofMinutes(30);

        for (int i = 0; i < 10; i++)
        {
            Row dataRow = table.getRows().add();
            dataRow.getCells().add(time.toString());
            time=time.plus(incTime);
            dataRow.getCells().add(time.toString());
        }

        page.getParagraphs().add(table);

        document.save(Paths.get(_dataDir.toString(), "Complex.pdf").toString());
    }

}
```
