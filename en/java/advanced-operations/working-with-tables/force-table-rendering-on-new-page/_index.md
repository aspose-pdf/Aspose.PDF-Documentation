---
title: Force Table Rendering on New Page
type: docs
weight: 20
url: /java/force-table-rendering-on-new-page/
description: Ensure tables render on a new page in PDF documents using Aspose.PDF for Java. Enhance layout control in your reports.
lastmod: "2025-02-17"
TechArticle: true 
AlternativeHeadline: How to render a table on a new page in a PDF document using the Aspose.PDF for Java
Abstract: This article discusses how to render a table on a new page in a PDF document using the Aspose.PDF library for Java. By default, elements are added to a page's Paragraphs collection, but the `IsInNewPage` method in the `BaseParagraph` class allows for rendering a table on a new page. The article provides a code example demonstrating this process, which involves creating a `Document` object, configuring page margins and orientation, and adding tables to the document. The first table renders on the current page, while the second table is set to render on a new page using the `setInNewPage(true)` method. The article also highlights the importance of using the latest Document Object Model (DOM) of the Aspose.PDF package for new features and issue resolution, while maintaining backward compatibility through the `isInNewPage` method.
SoftwareApplication: java  
---

## Render Table on New Page

By default, paragraphs are added to a Page object's Paragraphs collection. However, it is possible to render a table on a new page instead of directly after the previously added paragraph level object on the page.

### Adding a Table

To render table on a new page, use the [IsInNewPage](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) method in the [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/baseparagraph) class. The following code snippet shows how.

```java
public static void RenderTableOnNewPage(){
        Document doc = new Document();
        PageInfo pageInfo = doc.getPageInfo();
        MarginInfo marginInfo = pageInfo.getMargin();

        marginInfo.setLeft (37);
        marginInfo.setRight (37);
        marginInfo.setTop (37);
        marginInfo.setBottom (37);

        pageInfo.setLandscape(true);

        Table table = new Table();
        table.setColumnWidths ("50 100");
        // Added page.
        Page curPage = doc.getPages().add();
        for (int i = 1; i <= 120; i++)
        {
            Row row = table.getRows().add();
            row.setFixedRowHeight (15);
            Cell cell1 = row.getCells().add();
            cell1.getParagraphs().add(new TextFragment("Content 1"));
            Cell cell2 = row.getCells().add();
            cell2.getParagraphs().add(new TextFragment("HHHHH"));
        }
        Paragraphs paragraphs = curPage.getParagraphs();
        paragraphs.add(table);
        /********************************************/
        Table table1 = new Table();
        table.setColumnWidths ("100 100");
        for (int i = 1; i <= 10; i++)
        {
            Row row = table1.getRows().add();
            Cell cell1 = row.getCells().add();
            cell1.getParagraphs().add(new TextFragment("LAAAAAAA"));
            Cell cell2 = row.getCells().add();
            cell2.getParagraphs().add(new TextFragment("LAAGGGGGG"));
        }
        table1.setInNewPage (true);
        // I want to keep table 1 to next page please...
        paragraphs.add(table1);
        
        doc.save(_dataDir + "IsNewPageProperty_Test_out.pdf");
    }
}
```

{{% alert color="primary" %}}

The com.aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table) class provides makes it possible to create/render tables in PDF documents. A similar feature is also supported by the aspose.pdf.[Table](https://reference.aspose.com/pdf/java/com.aspose.pdf/Table) class but we encourage our customers to try using the latest Document Object Model (DOM) of the com.aspose.pdf package, because all the new features and issue resolution is being performed in new DOM. However, the legacy Aspose.PDF for Java (the aspose.pdf package) has a method [isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) in the paragraph class, so that the paragraph is rendered on a new page. For backward compatibility, the [isInNewPage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph#isInNewPage--) method has been added to the [BaseParagraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/BaseParagraph) class.

{{% /alert %}}