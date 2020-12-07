---
title: Complex PDF
type: docs
weight: 40
url: /java/complex-pdf/
description: Aspose.PDF for Java allows you to create more complex documents that contain images, text fragments, and tables in one document.
---

The [Hello, World](/pdf/net/hello-world/) example showed simple steps to create a PDF document. Let's take a look at creating a more complex document.
Our document will contain a image, two text fragments (header and paragraph), and a table. 

As an example, we'll take a document from a fictitious company that operates passenger ferry services.

Below code snippet follows these steps:

1. Instantiate a [Document](https://apireference.aspose.com/pdf/java/com.aspose.pdf/document) object.
1. Add a [Page](https://apireference.aspose.com/pdf/java/com.aspose.pdf/page) to the document object.
1. Add a [Image](https://apireference.aspose.com/pdf/java/com.aspose.pdf/image).
1. Using GSave operator: this operator saves current graphics state.
1. Create a [Matrix](https://apireference.aspose.com/pdf/java/com.aspose.pdf/matrix/) object.
1. Using ConcatenateMatrix operator: defines how image must be placed.
1. Using Do operator: this operator draws image.
1. Using GRestore operator: this operator restores graphics state.
1. Create a [TextFragment](https://apireference.aspose.com/pdf/java/com.aspose.pdf.text/textfragment) (header).
1. Add (header) to the page [Paragraphs](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Create a [TextFragment](https://apireference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) (description).
1. Add (description) to the page Paragraphs.
1. Create a table, add table properties.
1. Add (table) to the page [Paragraphs](https://apireference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
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
    // Path filePath = Paths.get(currentPath.toString(), "data", "foo.txt");

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
