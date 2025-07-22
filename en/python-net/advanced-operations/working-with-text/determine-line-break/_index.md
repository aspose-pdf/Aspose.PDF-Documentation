---
title: Determine Line Break
linktitle: Determine Line Break
type: docs
weight: 70
url: /python-net/determine-line-break/
description: Learn more about how to determinate a line break of multi-line TextFragment using Python
lastmod: "2025-05-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: How to Determine Line Break in PDF using Python
Abstract: This article presents a method for tracking the line-breaking behavior of multi-line `TextFragment` objects within a PDF document using a code snippet based on the Aspose.PDF library. The core function, `track_line_breaking()`, is designed to generate a PDF document and a corresponding text file that details the line-breaking notifications. The process involves creating a new PDF document, adding a page, and inserting four instances of `TextFragment` with pre-inserted line breaks to simulate multi-line text. Each text fragment is set to a font size of 20 points before being added to the document. After saving the PDF, the function extracts line-breaking notifications from the document's second page using the `get_notifications()` method and writes these to a text file. This example demonstrates how to programmatically create a PDF with multi-line text and analyze its layout by extracting line-break information, offering insights into text rendering within PDF documents.
---

## Track Line Breaking of Multi-Line TextFragment

The next code snippet shows how to track the line-breaking behavior of a multi-line TextFragment within a PDF document.

The track_line_breaking() function is defined to demonstrate this functionality. It begins by specifying output file paths for both the generated PDF document and a corresponding text file that will contain information about line breaking.

Within the function, a new PDF document object is created, and a new page is added to it. Subsequently, a loop is employed to generate four instances of a TextFragment containing a text with line breaks ("\r\n") inserted within the string to simulate multi-line text.

Each TextFragment is configured with a font size of 20 points before being added to the page's paragraphs.

After all TextFragments are added, the document is saved.

The function then proceeds to extract notifications about line breaking from the second page of the generated PDF document using the get_notifications() method. These notifications are written to a text file specified earlier.

This code snippet illustrates how to create a PDF document containing multi-line text and then extract information regarding line-breaking behavior, providing insights into how the text is laid out within the document.

```python

    import aspose.pdf as ap

    # Create PDF document
    with ap.Document() as document:
        page = document.pages.add()
        for i in range(4):
            text = ap.text.TextFragment(
                "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
            )
            text.text_state.font_size = 20
            page.paragraphs.add(text)
        document.save(path_outfile)

        notifications = document.pages[1].get_notifications()
        with open(path_out_textfile, "w") as f:
            f.write(notifications)
```

