---
title: Manipulate PDF Document 
linktitle: Manipulate PDF Document
type: docs
weight: 30
url: /java/manipulate-pdf-document/
description: Learn how to manipulate PDF documents in Java using Aspose.PDF, including editing and content updates.
lastmod: "2025-02-17"
TechArticle: true 
AlternativeHeadline: Guide on using Aspose.PDF for Java to perform various operations on PDF documents
Abstract: This article provides a comprehensive guide on using Aspose.PDF for Java to perform various operations on PDF documents. It outlines the method to validate PDF documents against PDF/A-1a and PDF/A-1b standards using the `Document` class's `validate(..)` method, which generates an XML report detailing compliance issues. The article also covers how to add and customize a Table of Contents (TOC) in PDF files, including setting different `TabLeaderType` for TOC levels and hiding page numbers. Additionally, it explains how to customize page numbers in the TOC by adding prefixes like "P1, P2, P3," etc. The guide further delves into adding layers to PDF documents, allowing for content segregation, such as multilingual texts or animations. Finally, it demonstrates setting a PDF expiration date using JavaScript to trigger alerts when a PDF is accessed beyond its validity period. Each section is supplemented with code snippets to illustrate the application of these features.
SoftwareApplication: java
---

## Validate PDF Document for PDF A Standard (A 1A and A 1B)

To validate a PDF document for PDF/A-1a or PDF/A-1b compatibility, use the [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) class' [validate(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#validate-java.io.OutputStream-int-) method. This method allows you to specify the name of the file in which the result is to be saved and the required validation type [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfFormat) enumeration: PDF_A_1A or PDF_A_1B.

The output XML format is a custom Aspose format. The XML contains a collection of tags with the name Problem; each tag contains the details of a particular problem. The Problem tag's ObjectID attribute represents the ID of the particular object this problem is related to. The Clause attribute represents a corresponding rule in the PDF specification.

```java
  public static void ValidatePDFDocumentForPDF_A_Standard() {
    // Open document
    Document pdfDocument = new Document(_dataDir + "sample.pdf");

    // Validate PDF for PDF/A-1a
    pdfDocument.validate(_dataDir + "validation-result-A1A.xml", PdfFormat.PDF_A_1A);

    // Save updated PDF file
    // document.save(_dataDir + "UpdatedFile_output.pdf");
  }
```
## Working with TOC

### Add TOC to Existing PDF

The ListSection class in the aspose.pdf package allows you to create a table of contents when creating a PDF document from scratch. To add headings, which are elements of the TOC, use the [aspose.pdf.Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) class.

To add a TOC to an existing PDF file, use the [Heading](https://reference.aspose.com/pdf/java/com.aspose.pdf/Heading) class in the com.aspose.pdf package. The com.aspose.pdf package can both create new and manipulate existing PDF files. To add a TOC to an existing PDF, use com.aspose.pdf package.

The following code snippet shows how to create a table of contents inside an existing PDF file.

```java
public static void AddTOCtoExistingPDF() {
    // Load an existing PDF files
    Document document = new Document(_dataDir + "sample.pdf");

    // Get access to first page of PDF file
    Page tocPage = document.getPages().insert(1);

    // Create object to represent TOC information
    com.aspose.pdf.TocInfo tocInfo = new com.aspose.pdf.TocInfo();
    com.aspose.pdf.TextFragment title = new com.aspose.pdf.TextFragment("Table Of Contents");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(com.aspose.pdf.FontStyles.Bold);

    // Set the title for TOC
    tocInfo.setTitle(title);
    tocPage.setTocInfo(tocInfo);

    // Create string objects which will be used as TOC elements
    String[] titles = new String[4];
    titles[0] = "First page";
    titles[1] = "Second page";
    titles[2] = "Third page";
    titles[3] = "Fourth page";
    for (int i = 0; i < 4; i++) {
      // Create Heading object
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(1);

      com.aspose.pdf.TextSegment segment2 = new com.aspose.pdf.TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);

      // Specify the destination page for heading object
      heading2.setDestinationPage(document.getPages().get_Item(i + 2));

      // Destination page
      heading2.setTop(document.getPages().get_Item(i + 2).getRect().getHeight());

      // Destination coordinate
      segment2.setText(titles[i]);

      // Add heading to page containing TOC
      tocPage.getParagraphs().add(heading2);
    }
    // Save the updated document
    document.save("TOC_Output_Java.pdf");
  }
```
### Set different TabLeaderType for different TOC Levels

Aspose.PDF also allows setting different TabLeaderType for different TOC levels. You need to set LineDash property of FormatArray with the appropriate value of TabLeaderType enum as following.

```java
  public static void SetDifferentTabLeaderTypeForTOCLevels() {

    String outFile = "TOC.pdf";

    Document document = new Document();
    Page tocPage = document.getPages().add();

    TocInfo tocInfo = new TocInfo();

    // set LeaderType

    tocInfo.setLineDash(TabLeaderType.Solid);

    TextFragment title = new TextFragment("Table Of Contents");
    title.getTextState().setFontSize(30);
    tocInfo.setTitle(title);

    // Add the list section to the sections collection of the Pdf document

    tocPage.setTocInfo(tocInfo);

    // Define the format of the four levels list by setting the left margins and
    // text format settings of each level

    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setLeft(0);
    tocInfo.getFormatArray()[0].getMargin().setRight(30);
    tocInfo.getFormatArray()[0].setLineDash(TabLeaderType.Dot);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);
    tocInfo.getFormatArray()[1].getMargin().setLeft(10);
    tocInfo.getFormatArray()[1].getMargin().setRight(30);
    tocInfo.getFormatArray()[1].setLineDash(TabLeaderType.None);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);
    tocInfo.getFormatArray()[2].getMargin().setLeft(20);
    tocInfo.getFormatArray()[2].getMargin().setRight(0);
    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].setLineDash(TabLeaderType.Solid);
    tocInfo.getFormatArray()[3].getMargin().setLeft(30);
    tocInfo.getFormatArray()[3].getMargin().setRight(30);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    // Create a section in the Pdf document
    Page page = document.getPages().add();

    // Add four headings in the section
    for (int Level = 1; Level <= 4; Level++) {
      com.aspose.pdf.Heading heading2 = new com.aspose.pdf.Heading(Level);
      TextSegment segment2 = new TextSegment();

      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      heading2.setTocPage(tocPage);

      segment2.setText("Sample Heading" + Level);
      heading2.getTextState().setFont(FontRepository.findFont("Arial UnicodeMS"));

      // Add the heading into Table Of Contents.
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }

    // save the PDF
    document.save(outFile);
  }
```
### Hide Page Numbers in TOC

In case if you do not want to display page numbers, along with the headings in TOC, you can use [IsShowPageNumbers](https://reference.aspose.com/pdf/java/com.aspose.pdf/TocInfo) property of [TOCInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/tocinfo) Class as false. Please check following code snippet to hide page numbers in the table of contents:

```java
public static void HidePageNumbersInTOC() {
    String outFile = _dataDir + "HiddenPageNumbers_out.pdf";
    Document doc = new Document();
    Page tocPage = doc.getPages().add();
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("Table Of Contents");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.setTitle(title);

    // Add the list section to the sections collection of the Pdf document
    tocPage.setTocInfo(tocInfo);

    // Define the format of the four levels list by setting the left margins and
    // text format settings of each level

    tocInfo.setShowPageNumbers(false);
    tocInfo.setFormatArrayLength(4);
    tocInfo.getFormatArray()[0].getMargin().setRight(0);
    tocInfo.getFormatArray()[0].getTextState().setFontStyle(FontStyles.Bold | FontStyles.Italic);

    tocInfo.getFormatArray()[1].getMargin().setLeft(30);
    tocInfo.getFormatArray()[1].getTextState().setUnderline(true);
    tocInfo.getFormatArray()[1].getTextState().setFontSize(10);

    tocInfo.getFormatArray()[2].getTextState().setFontStyle(FontStyles.Bold);
    tocInfo.getFormatArray()[3].getTextState().setFontStyle(FontStyles.Bold);

    Page page = doc.getPages().add();

    // Add four headings in the section
    for (int Level = 1; Level != 5; Level++) {
      Heading heading2 = new Heading(Level);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      heading2.setAutoSequence(true);
      segment2.setText("this is heading of level " + Level);
      heading2.setInList(true);
      page.getParagraphs().add(heading2);
    }
    doc.save(_dataDir + outFile);
  }
```

### Customize Page Numbers while adding TOC

It is common to customize the page numbering in the TOC while adding TOC in a PDF document. For example, we may need to add some prefix before page number like P1, P2, P3 and so on. In such a case, Aspose.PDF for Java provides PageNumbersPrefix property of TocInfo class that can be used to customize page numbers as shown in the following code sample.

```java
  public static void CustomizePageNumbersWhileAddingTOC() {

    String inFile = _dataDir + "sample.pdf";
    String outFile = _dataDir + "42824_out.pdf";

    // Load an existing PDF files
    Document doc = new Document(inFile);
    // Get access to first page of PDF file
    Page tocPage = doc.getPages().insert(1);
    // Create object to represent TOC information
    TocInfo tocInfo = new TocInfo();
    TextFragment title = new TextFragment("Table Of Contents");
    title.getTextState().setFontSize(20);
    title.getTextState().setFontStyle(FontStyles.Bold);

    // Set the title for TOC
    tocInfo.setTitle(title);
    tocInfo.setPageNumbersPrefix("P");
    tocPage.setTocInfo(tocInfo);

    for (int i = 1; i < doc.getPages().size(); i++) {
      // Create Heading object
      Heading heading2 = new Heading(1);
      TextSegment segment2 = new TextSegment();
      heading2.setTocPage(tocPage);
      heading2.getSegments().add(segment2);
      // Specify the destination page for heading object
      heading2.setDestinationPage(doc.getPages().get_Item(i + 1));
      // Destination page
      heading2.setTop(doc.getPages().get_Item(i + 1).getRect().getHeight());
      // Destination coordinate
      segment2.setText("Page " + i);
      // Add heading to page containing TOC
      tocPage.getParagraphs().add(heading2);
    }

    // Save the updated document
    doc.save(outFile);
  }
```

## Add Layers to PDF File

Layers can be used in PDF documents in many ways. You might have a multi-lingual file that you want to distribute and want text in each language to appear on different layers, with the background design appearing on a separate layer. You might also create documents with animation that appears on a separate layer. One example could be to add a license agreement to your file, and you don’t want a user to view the content until they agree to the terms of the agreement.

Aspose.PDF for Java supports adding layers to PDF files.

To work with layers in PDF files, use the following API members.

The [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) class represents a layer and contains the following properties:

- **Name** – the layer's name.
- **Id** – the layer's ID.
- **Contents** – a list of layer operators.

Once the [Layer](https://reference.aspose.com/pdf/java/com.aspose.pdf/Layer) objects have been defined, add them to the [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) object's Layers collection. The code below shows how to add layers to a PDF document.

```java
public static void AddLayersToPDFFile() {
    Document doc = new Document();
    Page page = doc.getPages().add();
    Layer layer = new Layer("oc1", "Red Line");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(1, 0, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 700));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 700));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.setLayers(new ArrayList<Layer>());
    page.getLayers().add(layer);
    layer = new Layer("oc2", "Green Line");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 1, 0));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 750));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 750));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    layer = new Layer("oc3", "Blue Line");
    layer.getContents().add(new com.aspose.pdf.operators.SetRGBColorStroke(0, 0, 1));
    layer.getContents().add(new com.aspose.pdf.operators.MoveTo(500, 800));
    layer.getContents().add(new com.aspose.pdf.operators.LineTo(400, 800));
    layer.getContents().add(new com.aspose.pdf.operators.Stroke());
    page.getLayers().add(layer);
    doc.save("output.pdf");
  
```
## Set PDF Expiration

The PDF expiration feature sets how long a PDF file is valid for. On a particular date, if someone tries to access it, a pop-up is displayed, explaining that the file has expired and that they need a new one.

Aspose.PDF allows you to set expiration when creating and editing PDF files.

The code snippet below shows how to set the expiration date for a PDF file. You need to use JavaScript as files saved by third party components (for example OwnerGuard) cannot be viewed on other workstations without that utility.

The PDF file can be created using PDF OwnerGuard using an existing file with an expiration date. But the new file can be opened only on a workstation that has PDF OwnerGuard installed. Workstations without PDF OwnerGuard will give an ExpirationFeatureError. For example, PDF Reader opens the file if OwnerGuard is installed, but Adobe Acrobat returns an error.

```java
  public static void SetPDFExpiration() {
    Document document = new Document(_dataDir+"sample.pdf");    
    JavascriptAction javaScript = new JavascriptAction(
      "var year=2020;" + 
      "var month=4;" + 
      "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());" + 
      "expiry = new Date(year, month);" + 
      "if (today.getTime() > expiry.getTime())" + 
      "app.alert('The file is expired. You need a new one.');"
      );
    document.setOpenAction(javaScript);
    document.save(_dataDir + "JavaScript-Added.pdf");
  }
```


