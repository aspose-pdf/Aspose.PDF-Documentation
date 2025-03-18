---
title: Determine Line Break
linktitle: Determine Line Break
type: docs
weight: 70
url: /python-net/determine-line-break/
description: Learn more about how to determinate a line break of multi-line TextFragment using Python
lastmod: "2025-02-27"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: How to determinate a line break
Abstract: The article, authored and published by the Aspose.PDF Doc Team, provides a beginner-level guide on determining line breaks within a multi-line TextFragment in PDF documents using Python. It introduces a function, `track_line_breaking()`, which demonstrates how to create a PDF with multi-line text and extract line-breaking notifications. The process involves creating a new PDF document, adding a page, and inserting TextFragments with simulated line breaks. Each TextFragment is assigned a font size of 20 points. After saving the document, line-breaking notifications are extracted and written to a text file. This example highlights the use of Aspose.PDF for .NET to understand text layout within a document.
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

    def track_line_breaking():
        """Track Line Breaking of Multi-Line TextFragment"""
        output_pdf = DIR_OUTPUT_TEXTS + "track_line_breaking.pdf"
        output_txt = DIR_OUTPUT_TEXTS + "track_line_breaking.txt"

        # Create new document object
        document = ap.Document()
        page = document.pages.add()

        for i in range(4):
            text = ap.text.TextFragment(
                "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
            )
            text.text_state.font_size = 20
            page.paragraphs.add(text)
        document.save(output_pdf)

        notifications = document.pages[1].get_notifications()
        with open(output_txt, "w") as f:
            f.write(notifications)
```

