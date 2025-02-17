---
title: Working with Headings in PDF
type: docs
weight: 70
url: /java/working-with-headings/
lastmod: "2025-02-17"
description: Create numbering in heading your PDF document with Java. Aspose.PDF for Java offers different kinds of numbering styles.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Manipulate Headings in PDF using Aspose.PDF for Java
Abstract: The article "Apply Numbering Style in Heading" discusses the significance of headings in documents and the importance of organizing them effectively for enhanced clarity and readability. It introduces Aspose.PDF for Java, a tool that provides various pre-defined numbering styles through its `NumberingStyle` enumeration. These styles include `NumeralsArabic`, `NumeralsRomanUppercase`, `NumeralsRomanLowercase`, `LettersUppercase`, and `LettersLowercase`, each offering a different formatting option for document headings. The article further illustrates the application of these styles using Java code, showcasing how to implement them through the `setStyle` property of the `com.aspose.pdf.Heading` class. A practical example is provided, demonstrating how to create a PDF document with numbered headings using the Aspose.PDF library. The example code details the process of setting up a document, adding pages, and applying different numbering styles to headings, culminating in the generation of a PDF file named "ApplyNumberStyle_out.pdf".
SoftwareApplication: java
---

## Apply Numbering Style in Heading

Headings are the important parts of any document. Writers always try to make headings more prominent and meaningful to its readers. If there are more than one headings in a document, a writer has several options to organize these headings. One of the most common approach to organize headings is to write headings in Numbering Style.

Aspose.PDF for Java offers many pre-defined numbering styles. These pre-defined numbering styles are stored in an enumeration, NumberingStyle. The pre-defined values of NumberingStyle enumeration and their descriptions are given below:

|**Heading Types**|**Description**|
| :- | :- |
|NumeralsArabic|Arab type,for example, 1,1.1,...|
|NumeralsRomanUppercase|Roman upper type, for example, I,I.II, ...|
|NumeralsRomanLowercase|Roman lower type, for example, i,i.ii, ...|
|LettersUppercase|English upper type, for example, A,A.B, ...|
|LettersLowercase|English lower type, for example, a,a.b, ...|
The [setStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) property of [com.aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) class is used to set the numbering styles of the headings.


The source code, to obtain the output shown in the above figure, is given below in the example.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleHeading {
    // The path to the documents directory.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ApplyNumberingStyleinHeading() {

        Document pdfDoc = new Document();
        pdfDoc.getPageInfo().setWidth(612.0);
        pdfDoc.getPageInfo().setHeight(792.0);
        pdfDoc.getPageInfo().setMargin(new MarginInfo());
        pdfDoc.getPageInfo().getMargin().setLeft(72);
        pdfDoc.getPageInfo().getMargin().setRight(72);
        pdfDoc.getPageInfo().getMargin().setTop(72);
        pdfDoc.getPageInfo().getMargin().setBottom(72);

        Page pdfPage = pdfDoc.getPages().add();
        pdfPage.getPageInfo().setWidth(612.0);
        pdfPage.getPageInfo().setHeight(792.0);
        pdfDoc.getPageInfo().setMargin(new MarginInfo());
        pdfDoc.getPageInfo().getMargin().setLeft(72);
        pdfDoc.getPageInfo().getMargin().setRight(72);
        pdfDoc.getPageInfo().getMargin().setTop(72);
        pdfDoc.getPageInfo().getMargin().setBottom(72);

        FloatingBox floatBox = new FloatingBox();
        floatBox.setMargin(pdfPage.getPageInfo().getMargin());

        pdfPage.getParagraphs().add(floatBox);

        Heading heading = new Heading(1);
        heading.setInList(true);
        heading.setStartNumber(1);
        heading.setText("List 1");
        heading.setStyle(NumberingStyle.NumeralsRomanLowercase);
        heading.setAutoSequence(true);

        floatBox.getParagraphs().add(heading);
        Heading heading2 = new Heading(1);
        heading2.setInList(true);
        heading2.setStartNumber(13);
        heading2.setText("List 2");
        heading2.setStyle(NumberingStyle.NumeralsRomanLowercase);
        heading2.setAutoSequence(true);

        floatBox.getParagraphs().add(heading2);

        Heading heading3 = new Heading(2);
        heading3.setInList(true);
        heading3.setStartNumber(1);
        heading3.setText("the value, as of the effective date of the plan, of property to be distributed under the plan onaccount of each allowed");
        heading3.setStyle (NumberingStyle.LettersLowercase);
        heading3.setAutoSequence(true);

        floatBox.getParagraphs().add(heading3);
        _dataDir = _dataDir + "ApplyNumberStyle_out.pdf";
        pdfDoc.save(_dataDir);

    }

}
```
