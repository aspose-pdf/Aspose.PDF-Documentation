---
title: Extract SuperScripts and SubScripts text from PDF
linktitle: Extract SuperScripts and SubScripts 
type: docs
weight: 30
url: /net/extract-superscripts-subscripts-from-pdf/
description: This article describes various ways to extract SuperScripts and SubScripts text from PDF using Aspose.PDF in C#. 
lastmod: "2022-10-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extract SuperScripts and SubScripts Text

Extracting text from a PDF document is a common thing. However, in such text, when extracted, the **SuperScripts and SubScripts** contained in them, which are typical for technical documents and articles, may not be displayed. A SubScript or SuperScript is a character, number, or letter placed below or above a regular line of text. It is usually smaller than the rest of the text.

**SubScripts and SuperScripts** are most often used in formulas, mathematical expressions, and specifications of chemical compounds. It is tough to edit them when there can be many of them in the same passage of text.
In one of the latest releases, the **Aspose.PDF for .NET** library added support for extracting SuperScripts and SubScripts text from PDF.

Use the **TextFragmentAbsorber** class and you can already do anything with the found text, i.e., you can simply use the entire text. Try the next code snippet:

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            writer.WriteLine(absorber.Text);
        }
```

Or use **TextFragments** separately and do all sorts of manipulations with them, for example, sort by coordinates or by size.

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            foreach (var textFragment in absorber.TextFragments)
            {
                writer.Write(textFragment.Text);
            }
        }
```

