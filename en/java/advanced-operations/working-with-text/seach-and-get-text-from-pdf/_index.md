---
title: Search and Get Text from Pages of PDF Document 
linktitle: Search and Get Text
type: docs
weight: 60
url: /java/search-and-get-text-from-pdf/
description: Explore how to search and extract text from a PDF document in Java with Aspose.PDF for content extraction.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to search and extract text from a PDF document using Aspose.PDF for Java
Abstract: The article provides a comprehensive guide on using the `TextFragmentAbsorber` class to search and extract text from PDF documents using the Aspose.PDF library in Java. It outlines methods to find text matching a specific phrase across all pages of a PDF, retrieve text segments, and employ regular expressions for text searches. The process involves utilizing the `accept()` method on the PDF document's `Pages` collection, which takes a `TextFragmentAbsorber` object and returns a collection of `TextFragment` objects. The article includes Java code snippets demonstrating how to loop through these fragments to access their properties such as text content, position, font characteristics, and color. Additionally, it explains how to target specific pages for text extraction and highlights the use of regular expressions to refine search criteria, including case-insensitive searches.
SoftwareApplication: java 
---

## Search and Get Text from All the Pages of PDF Document

TextFragmentAbsorber allows you to find text, matching a particular phrase, from all pages of a PDF document.

To search text in the whole document, call the [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) collection's accept() method. The [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) method takes a TextFragmentAbsorber object as a parameter, which returns a collection of TextFragment objects. Loop through all the fragments to get their properties, for example Text, Position, XIndent, YIndent, FontName, FontSize, IsAccessible, IsEmbedded, IsSubset, ForegroundColor etc.

The following code snippet shows how to search an the entire document and display all matches in a console.

```java
// Open document
Document pdfDocument = new Document("input.pdf");

// Create TextAbsorber object to find all instances of the input search phrase
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// Accept the absorber for all the pages
pdfDocument.getPages().accept(textFragmentAbsorber);

// Get the extracted text fragments into collection
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// Loop through the fragments
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("Text :- " + textFragment.getText());
    System.out.println("Position :- " + textFragment.getPosition());
    System.out.println("XIndent :- " + textFragment.getPosition().getXIndent());
    System.out.println("YIndent :- " + textFragment.getPosition().getYIndent());
    System.out.println("Font - Name :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("Font - IsAccessible :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("Font - IsEmbedded - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("Font - IsSubset :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("Font Size :- " + textFragment.getTextState().getFontSize());
    System.out.println("Foreground Color :- " + textFragment.getTextState().getForegroundColor());
}
```

To search text on a particular page and get properties associated with it, provide the page index:

```java
// Accept the absorber for first page of document
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## Search and Get Text Segments from Pages of PDF

To search text segments on all pages in a document, get a document's TextFragment objects.

TextFragmentAbsorber allows you to find text, matching a particular phrase, from all the pages in a PDF document. To search text in the whole document, call the [Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection) collection's [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) method. The [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) method takes a TextFragmentAbsorber object as a parameter, which returns a collection of TextFragment objects.

{{% alert color="primary" %}}

When the TextFragmentCollection collection has been fetched from the document, loop through it to get each TextFragment object's TextSegmentCollection collection. After that, you can get the individual TextSegment object's properties.

{{% /alert %}}

The following code snippet shows how to search text segments on all pages.

```java
// Open document
Document pdfDocument = new Document("input.pdf");

// Create TextAbsorber object to find all instances of the input search phrase
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// Accept the absorber for first page of document
pdfDocument.getPages().accept(textFragmentAbsorber);

// Get the extracted text fragments into collection
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// Loop through the Text fragments
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    // Iterate through text segments
    for (TextSegment textSegment : (Iterable<TextSegment>) textFragment.getSegments()) {
        System.out.println("Text :- " + textSegment.getText());
        System.out.println("Position :- " + textSegment.getPosition());
        System.out.println("XIndent :- " + textSegment.getPosition().getXIndent());
        System.out.println("YIndent :- " + textSegment.getPosition().getYIndent());
        System.out.println("Font - Name :- " + textSegment.getTextState().getFont().getFontName());
        System.out.println("Font - IsAccessible :- " + textSegment.getTextState().getFont().isAccessible());
        System.out.println("Font - IsEmbedded - " + textSegment.getTextState().getFont().isEmbedded());
        System.out.println("Font - IsSubset :- " + textSegment.getTextState().getFont().isSubset());
        System.out.println("Font Size :- " + textSegment.getTextState().getFontSize());
        System.out.println("Foreground Color :- " + textSegment.getTextState().getForegroundColor());
    }
}
```

To search a specific text segment and get the properties associated, specify the page index for the page you want to search:

```java
// Accept the absorber for the first page of document.
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## Search and Get Text from pages using Regular Expression

TextFragmentAbsorber helps you search and retrieve text from all pages in a document, based on a regular expression.

To search and get text from a document:

1. Pass the search term as a regular expression to the TextFragmentAbsorber constructor.
1. Set the TextFragmentAbsorber object's TextSearchOptions property.
   This property requires a TextSearchOptions object: pass true to its constructor when creating a new object.
1. To retrieve matching text from all pages, call the [Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection) collection's [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) method.
   TextFragmentAbsorber returns a TextFragmentCollection containing all the fragments matching the criteria specified by the regular expression.

The following code snippet shows how to search all pages in a document and get text based on a regular expression.

```java
// Open a document
Document pdfDocument = new Document("source.pdf");

// Create TextAbsorber object to find all instances of the input search phrase
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // like 1999-2000

// Set text search option to specify regular expression usage
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

// Accept the absorber for first page of document
pdfDocument.getPages().accept(textFragmentAbsorber);

// Get the extracted text fragments into collection
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// Loop through the fragments
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("Text :- " + textFragment.getText());
    System.out.println("Position :- " + textFragment.getPosition());
    System.out.println("XIndent :- " + textFragment.getPosition().getXIndent());
    System.out.println("YIndent :- " + textFragment.getPosition().getYIndent());
    System.out.println("Font - Name :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("Font - IsAccessible :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("Font - IsEmbedded - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("Font - IsSubset :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("Font Size :- " + textFragment.getTextState().getFontSize());
    System.out.println("Foreground Color :- " + textFragment.getTextState().getForegroundColor());
}
```

To search text on a particular page and get its properties, specify the page index:

```java
// Accept the absorber for the first page of the document.
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber)
```

In order to search a string in either upper case or lowercase, you may consider using regular expression.

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));
```

Example:

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[\\S]+");
```
