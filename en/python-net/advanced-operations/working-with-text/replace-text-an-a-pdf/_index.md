---
title: Replace Text in PDF via Python
linktitle: Replace Text in PDF
type: docs
weight: 40
url: /python-net/replace-text-in-pdf/
description: Learn more about various ways of replacing and removing text from Aspose.PDF for Python via .NET library.
lastmod: "2025-02-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true 
AlternativeHeadline: How to replace Text in PDF using Python
Abstract: The article provides a comprehensive guide on various text manipulation techniques within PDF documents using Aspose.PDF for Python via .NET. It covers several text replacement strategies, including replacing text across all pages, within specific page regions, and using regular expressions. The article also explains how to replace fonts within PDFs, ensuring that unused fonts are removed, and how to manage text replacement to automatically rearrange page content. Additionally, it delves into rendering replaceable symbols during PDF creation, including their use in header/footer areas, to enhance document customization. Finally, it details methods to remove all text from a PDF document, optimizing operations for scenarios where complete text removal is necessary. Each section is supplemented with code snippets in Python and other supported languages to demonstrate practical implementation.
---

## Replace Text in all pages of PDF document

{{% alert color="primary" %}}

You can try to find in replace the text in the document using Aspose.PDF and get the results online at this [link](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

In order to replace text in all the pages of a PDF document, you first need to use [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) to find the particular phrase you want to replace. After that, you need to go through all the TextFragments to replace the text and change any other attributes. Once you have done that, you only need to save the output PDF using the Save method of the Document object. The following code snippet shows you how to replace text in all pages of PDF document.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Create TextAbsorber object to find all instances of the input search phrase
    absorber = ap.text.TextFragmentAbsorber("format")

    # Accept the absorber for all the pages
    document.pages.accept(absorber)

    # Get the extracted text fragments
    collection = absorber.text_fragments

    # Loop through the fragments
    for text_fragment in collection:
        # Update text and other properties
        text_fragment.text = "FORMAT"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
        text_fragment.text_state.font_size = 22
        text_fragment.text_state.foreground_color = ap.Color.blue
        text_fragment.text_state.background_color = ap.Color.green

    # Save the document
    document.save(output_pdf)
```

## Replace Text in particular page region

In order to replace text in a particular page region, first, we need to instantiate TextFragmentAbsorber object, specify page region using TextSearchOptions.Rectangle property and then iterate through all the TextFragments to replace the text. Once these operations are completed, we only need to save the output PDF using the Save method of the Document object.  The following code snippet shows you how to replace text in all pages of PDF document.

```python


```

## Replace Text Based on a Regular Expression

If you want to replace some phrases based on regular expression, you first need to find all the phrases matching that particular regular expression using TextFragmentAbsorber. You will have to pass the regular expression as a parameter to the TextFragmentAbsorber constructor. You also need to create TextSearchOptions object which specifies whether the regular expression is being used or not. Once you get the matching phrases in TextFragments, you need to loop through all of them and update as required. Finally, you need to save the updated PDF using the Save method of the Document object. The following code snippet shows you how to replace text based on a regular expression.

```python

```

## Replace fonts in existing PDF file

Aspose.PDF for Python via .NET supports the capability to replace text in PDF document. However, sometimes you have a requirement to only replace the font being used inside PDF document. So instead of replacing the text, only font being used is replaced. One of the overloads of TextFragmentAbsorber constructor accepts TextEditOptions object as an argument and we can use RemoveUnusedFonts value from TextEditOptions.FontReplace enumeration to accomplish our requirements. The following code snippet shows how to replace the font inside PDF document.

```python

```

## Text Replacement should automatically re-arrange Page Contents

Aspose.PDF for Python via .NET supports the feature to search and replace text inside the PDF file. However recently some customers encountered issues during text replace when particular TextFragment is replaced with smaller contents and some extra spaces are displayed in resultant PDF or in case the TextFragment is replaced with some longer string, then words overlap existing page contents. So the requirement was to introduce a mechanism that once the text inside a PDF document is replaced, the contents should be re-arranged.

In order to cater above-stated scenarios, Aspose.PDF for Python via .NET has been enhanced so that no such issues appear when replacing text inside PDF file. The following code snippet shows how to replace text inside PDF file and the page contents should be re-arranged automatically.

```python

```

## Rendering Replaceable Symbols during PDF creation

Replaceable symbols are special symbols in a text string that can be replaced with corresponding content at run time. Replaceable symbols currently support by new Document Object Model of Aspose.PDF namespace are `$P`, `$p,` `\n`, `\r`. The `$p` and `$P` are used to deal with the page numbering at run time. `$p` is replaced with the number of the page where the current Paragraph class is in. `$P` is replaced with the total number of pages in the document. When adding `TextFragment` to the paragraphs collection of PDF documents, it does not support line feed inside the text. However in order to add text with a line feed, please use `TextFragment` with `TextParagraph`:

- use "\r\n" or Environment.NewLine in TextFragment instead of single "\n";
- create a TextParagraph object. It will add text with line splitting;
- add the TextFragment with TextParagraph.AppendLine;
- add the TextParagraph with TextBuilder.AppendParagraph.

```python

```

## Replaceable symbols in Header/Footer area

Replaceable symbols can also be placed inside the Header/Footer section of PDF file. Please take a look over the following code snippet for details on how to add replaceable symbol in the footer section.

```python

```

## Remove Unused Fonts from PDF File

Aspose.PDF for Python via .NET supports the feature to embed fonts while creating a PDF document, as well as the capability to embed fonts in existing PDF files. From Aspose.PDF for Python via .NET 7.3.0, it also lets you remove duplicate or unused fonts from PDF documents.

To replace fonts, use the following approach:

1. Call the [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber) class.
1. Call the TextFragmentAbsorber class’ TextEditOptions.FontReplace.RemoveUnusedFonts parameter. (This removes fonts that have become unused during font replacement).
1. Set font individually for each text fragment.

The following code snippet replaces font for all text fragments of all document pages and removes unused fonts.

```python

```

## Remove All Text from PDF Document

### Remove All Text using Operators

In some text operation, you need to remove all text from PDF document and for that, you need to set found text as empty string value usually. The point is that changing the text for multitude text fragments invokes a number of checking and text position adjustment operations. They are essential in the text editing scenarios. The difficulty is that you cannot determine how many text fragments will be removed in the scenario where they are processed in a loop.

Therefore, we recommend using another approach for the scenario of removing all text from PDF pages. Please consider the following code snippet that works very fast.

```python

```

