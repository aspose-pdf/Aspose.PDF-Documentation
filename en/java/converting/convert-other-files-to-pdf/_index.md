---
title: Convert Other File Formats to PDF in Java
linktitle: Convert other file formats to PDF
type: docs
weight: 80
url: /java/convert-other-files-to-pdf/
lastmod: "2026-06-16"
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

1. Open the OFD source by passing the file path and [`OfdLoadOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/ofdloadoptions/) into the [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) constructor.
1. Let Aspose.PDF parse the OFD package into the PDF document model.
1. Save the resulting PDF to the target output path.

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

1. Open the TeX source by passing the file path and [`TeXLoadOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/texloadoptions/) into the [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) constructor.
1. Let Aspose.PDF interpret the TeX markup and build the PDF layout during loading.
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

1. Open the PostScript source with [`PsLoadOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/psloadoptions/) in the [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) constructor.
1. Let Aspose.PDF translate the PostScript page-description stream into a PDF document model.
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

1. Open the EPS source with [`PsLoadOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/psloadoptions/) because EPS follows the same PostScript-based load path.
1. Load the file into a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) so the page-description content is converted during import.
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

1. Open the EPUB source by passing the file path and [`EpubLoadOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/epubloadoptions/) into the [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) constructor.
1. Let Aspose.PDF load the ebook structure and transform it into PDF pages.
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

1. Open the Markdown source by passing the file path and [`MdLoadOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/mdloadoptions/) into the [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) constructor.
1. Let Aspose.PDF interpret the Markdown content and render it into PDF page content.
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

1. Read the plain-text source with UTF-8 decoding so the text content is available as a Java string.
1. Create an empty [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and add a [`Page`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/).
1. Wrap the text in a [`TextFragment`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragment/) and add it to the page paragraphs collection.
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

1. Read all text lines from the input file so page-break markers can be inspected during conversion.
1. Create an empty [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) and configure each [`Page`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/page/) with margins and default text state.
1. Resolve the monospaced font through [`FontRepository`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/fontrepository/) and add each line as a [`TextFragment`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/textfragment/).
1. Save the output file after the page-building loop completes.

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

1. Create [`PclLoadOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/pclloadoptions/) and enable suppressed parsing errors when lenient import behavior is required.
1. Open the PCL source by passing the file path and load options into the [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) constructor.
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

1. Transform the XML source with the XSLT file into a temporary HTML file by calling the dedicated transformation method.
1. Pass the generated HTML file into the existing HTML-to-PDF conversion function so the final PDF uses the standard [`HtmlLoadOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/htmlloadoptions/) workflow.
1. Delete the temporary HTML file in the `finally` block after conversion completes.
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

1. Open the XPS source by passing the file path and [`XpsLoadOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/xpsloadoptions/) into the [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) constructor.
1. Let Aspose.PDF interpret the XPS page description during document loading.
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

1. Create [`XslFoLoadOptions`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/xslfoloadoptions/) with the XSLT path so the XML source can be transformed during loading.
1. Configure the parsing error handling mode to throw immediately when invalid XSL-FO is encountered.
1. Open the XML source in a [`Document`](https://reference.aspose.com/pdf/en/java/com.aspose.pdf/document/) with those load options.
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

Use this method when XML data must be transformed to HTML before the final PDF conversion step.

1. Open the XML and XSLT input files as transformation sources.
1. Create a `Transformer` from the XSLT stylesheet and run it against the XML source.
1. Write the transformed HTML file to disk so the downstream PDF conversion function can load it.

```java
private static void transformXmlToHtml(Path xmlFile, Path xsltFile, Path htmlFile) throws Exception {
    Transformer transformer = TransformerFactory.newInstance()
            .newTransformer(new StreamSource(xsltFile.toFile()));
    transformer.transform(new StreamSource(xmlFile.toFile()), new StreamResult(htmlFile.toFile()));
}
```
