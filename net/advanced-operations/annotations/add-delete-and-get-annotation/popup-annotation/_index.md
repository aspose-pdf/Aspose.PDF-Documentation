---
title: PDF Popup Annotation | C#
linktitle: Popup Annotation
type: docs
weight: 110
url: /net/popup-annotation/
description: Pop-up annotation not appear alone, it is associated with a Markup annotation, its parent annotation, and shall be used for editing the parent’s text.
lastmod: "2020-12-25"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

A Pop-up Annotation displays text in a pop-up window for entry and editing. It shall not appear alone but is associated with a markup annotation, its parent annotation, and shall be used for editing the parent’s text.

It shall have no appearance stream or associated actions of its own and shall be identified by the Popup entry in the parent’s annotation dictionary.

## How to add Popup Annotation

The following code snippet shows you how to add [Popup Annotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/popupannotation) in a PDF page using an example of adding a parent's [Line annotation](/pdf/net/add-line-annotation/).

```csharp
using Aspose.Pdf.Annotations;
using System;
using System.Linq;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleLineAnnotation
    {
        // The path to the documents directory.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        public static void AddLineAnnotation()
        {
            try
            {
                // Load the PDF file
                Document document = new Document(System.IO.Path.Combine(_dataDir, "Appartments.pdf"));

                // Create Line Annotation 
                var lineAnnotation = new LineAnnotation(
                    document.Pages[1],
                    new Rectangle(550, 93, 562, 439),
                    new Point(556, 99), new Point(556, 443))
                {
                    Title = "John Smith",
                    Color = Color.Red,
                    Width = 3,
                    StartingStyle = LineEnding.OpenArrow,
                    EndingStyle = LineEnding.OpenArrow,
                    Popup = new PopupAnnotation(document.Pages[1], new Rectangle(842, 124, 1021, 266))
                };

                // Add annotation to the page 
                document.Pages[1].Annotations.Add(lineAnnotation);
                document.Save(System.IO.Path.Combine(_dataDir, "Appartments_mod.pdf"));
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
        }
```
