---
title: Extract Text From Stamps using C#
type: docs
weight: 60
url: /net/extract-text-from-stamps/
---

## Extract Text from Stamp Annotations

Aspose.PDF for NET lets you extract text from stamp annotations. In order to extract text from Stamp Annotations in a PDF, the following steps can be used.

1. Create a Document class object
1. Get the desired Annotation from list of annotations of a page
1. Define a new object of TextAbsorber class
1. Use the TextAbsorber's visit method to get the Text

```csharp
public static void ExtractText()
{
   Document document = new Document(_dataDir + "ExtractStampText.pdf");
   Annotation item = document.Pages[1].Annotations[1];
   if (item is StampAnnotation annot) {
         TextAbsorber ta = new TextAbsorber();
         XForm ap = annot.Appearance["N"];
         ta.Visit(ap);
         Console.WriteLine(ta.Text);
   }
}
```
