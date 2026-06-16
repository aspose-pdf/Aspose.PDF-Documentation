---
title: Convert Other File Formats to PDF in Java
linktitle: Convert other file formats to PDF
type: docs
weight: 80
url: /java/convert-other-files-to-pdf/
lastmod: "2026-06-09"
description: Learn how to convert EPUB, Markdown, PCL, XPS, PostScript, XML, XSL-FO, OFD, and TeX files to PDF in Java with Aspose.PDF.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: How to Convert other file formats to PDF in Java
Abstract: This article explains how to convert multiple source file formats to PDF using Aspose.PDF for Java. It covers EPUB, Markdown, OFD, PCL, PostScript, EPS, TeX, text, XML, XPS, and XSL-FO conversion workflows using format-specific load options and preprocessing steps where needed.
---
Aspose.PDF for Java supports conversion from document, markup, and page-description formats into PDF.

## Convert OFD to PDF

Use this example when an OFD document should be converted into PDF.

1. Open the OFD input file.
1. Create the PDF document from the OFD source.
1. Save the resulting PDF.

```java
public static void convertOfdToPdf(Path inputFile, Path outputFile) {
       try (Document document = new Document(inputFile.toString(), new OfdLoadOptions())) {
           document.save(outputFile.toString());
       }
       System.out.println(inputFile + " converted into " + outputFile);
   }
```

## Convert TeX to PDF

Use this example when TeX content should be rendered directly as PDF.

1. Open the TeX input file.
1. Create the PDF document from the TeX source.
1. Save the generated PDF.

```java
public static void convertTexToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new com.aspose.pdf.TeXLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PostScript to PDF

Use this example when a PostScript file should be converted into a PDF document.

1. Open the PostScript input file.
1. Create the PDF document from that source.
1. Save the converted PDF file.

```java
public static void convertPostScripToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert EPS to PDF

Use this example when an Encapsulated PostScript file should be converted to PDF.

1. Open the EPS source file.
1. Load the EPS content into the PDF conversion flow.
1. Save the output PDF.

```java
public static void convertEpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new PsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert EPUB to PDF

Use this example when an EPUB eBook should be converted into PDF.

1. Open the EPUB input document.
1. Create the PDF document from the EPUB source.
1. Save the converted PDF.

```java
public static void convertEpubToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new EpubLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert Markdown to PDF

Use this example when Markdown content should be rendered and saved as PDF.

1. Open the Markdown source file.
1. Convert the Markdown content into a PDF document.
1. Save the output PDF file.

```java
public static void convertMdToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new MdLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert text to PDF with a simple workflow

Use this example when a plain text file should be quickly converted to PDF.

1. Read the text input file.
1. Create a PDF document and place the text on a page.
1. Save the generated PDF.

```java
public static void convertTxtToPdfSimple(Path inputFile, Path outputFile) throws Exception {
    String textContent = Files.readString(inputFile, StandardCharsets.UTF_8);
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getParagraphs().add(new TextFragment(textContent));
        page.close();
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert text to PDF with advanced options

Use this example when plain text should be converted with additional layout or encoding options.

1. Open the text file with the required options.
1. Create the PDF document from the text content.
1. Save the output file.

```java
public static void convertTxtToPdf(Path inputFile, Path outputFile) throws Exception {
    List<String> lines = Files.readAllLines(inputFile);
    try (Document document = new Document()) {
        com.aspose.pdf.Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(20);
        page.getPageInfo().getMargin().setRight(10);
        page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
        page.getPageInfo().getDefaultTextState().setFontSize(12);

        int pageCount = 1;
        for (String line : lines) {
            if (!line.isEmpty() && line.charAt(0) == '\f') {
                page = document.getPages().add();
                page.getPageInfo().getMargin().setLeft(20);
                page.getPageInfo().getMargin().setRight(10);
                page.getPageInfo().getDefaultTextState().setFont(FontRepository.findFont("Courier New"));
                page.getPageInfo().getDefaultTextState().setFontSize(12);
                pageCount++;
                if (pageCount == 4) {
                    break;
                }
            } else {
                page.getParagraphs().add(new TextFragment(line));
            }
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert PCL to PDF

Use this example when a PCL print stream should be converted into PDF.

1. Open the PCL input file.
1. Create the PDF document from the PCL source.
1. Save the result as PDF.

```java
public static void convertPclToPdf(Path inputFile, Path outputFile) {
    PclLoadOptions loadOptions = new PclLoadOptions();
    loadOptions.setSupressErrors(true);
    try (Document document = new Document(inputFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert XML to PDF through XSLT and HTML

Use this example when XML data should be transformed before final PDF generation.

1. Transform the XML source with the XSLT file.
1. Load the intermediate content into the PDF conversion flow.
1. Save the generated PDF file.

```java
public static void convertXmlToPdf(Path xsltFile, Path xmlFile, Path outputFile) throws Exception {
    Path htmlFile = Files.createTempFile("aspose-pdf-xml-", ".html");
    try {
        transformXmlToHtml(xmlFile, xsltFile, htmlFile);
        HtmlToPdfExamples.convertHtmlToPdf(htmlFile, outputFile);
    } finally {
        Files.deleteIfExists(htmlFile);
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## Convert XPS to PDF

Use this example when an XPS document should be converted into PDF.

1. Open the XPS source file.
1. Create the PDF document from the XPS input.
1. Save the converted PDF.

```java
public static void convertXpsToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new XpsLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## Convert XSL-FO to PDF

Use this example when XSL-FO content should be rendered as PDF.

1. Provide the XML and XSLT inputs.
1. Transform them into XSL-FO-compatible output and load it.
1. Save the resulting PDF document.

```java
public static void convertXslFoToPdf(Path xsltFile, Path xmlFile, Path outputFile) {
    XslFoLoadOptions loadOptions = new XslFoLoadOptions(xsltFile.toString());
    loadOptions.setParsingErrorsHandlingType(XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately);
    try (Document document = new Document(xmlFile.toString(), loadOptions)) {
        document.save(outputFile.toString());
    }
    System.out.println(xmlFile + " converted into " + outputFile);
}
```

## Transform XML to intermediate HTML

Use this helper when XML data must be transformed to HTML before the final PDF conversion step.

1. Open the XML and XSLT input files.
1. Apply the XSLT transformation to build HTML output.
1. Write the transformed HTML file for downstream conversion.

```java
private static void transformXmlToHtml(Path xmlFile, Path xsltFile, Path htmlFile) throws Exception {
    Transformer transformer = TransformerFactory.newInstance()
            .newTransformer(new StreamSource(xsltFile.toFile()));
    transformer.transform(new StreamSource(xmlFile.toFile()), new StreamResult(htmlFile.toFile()));
}
```
