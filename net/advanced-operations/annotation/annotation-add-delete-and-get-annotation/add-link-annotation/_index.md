---
title: Add Link Annotation
type: docs
weight: 20
url: /net/add-link-annotation/
---
# Add Link Annotation

A [Link Annotation](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) is a hypertext link that leads to a destination elsewhere in the document or to an action to be performed.

A Link is a rectangular area that can be placed anywhere on the page. Each link has a corresponding PDF action associated with it. This action is performed when the user clicks in the area of this link.

The following code snippet shows how to add Link Annotation to a PDF file using a phone number example:
```csharp
using Aspose.Pdf.Annotations;
using Aspose.Pdf.Text;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleLinkAnnotations
    {
        // The path to the documents directory.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
 public static void AddLinkAnnotation()
    {
        try
        {
            // Load the PDF file
            Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume.pdf"));
            // Create TextFragmentAbsorber object to find a phone number
            TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("678-555-0103");

            // Accept the absorber for the 1st page only
            document.Pages[1].Accept(textFragmentAbsorber);

            var phoneNumberFragment = textFragmentAbsorber.TextFragments[1];

            // Create Link Annotation and set the action to call a phone number
            var linkAnnotation = new LinkAnnotation(document.Pages[1], phoneNumberFragment.Rectangle)
            {
                Action = new GoToURIAction("callto:678-555-0103")
            };

            // Add annotation to page
            document.Pages[1].Annotations.Add(linkAnnotation);
            document.Save(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        }
        catch (Exception ex)
        {
            Console.WriteLine(ex.Message);
        }
    }
```

Please try using the following code snippet to Get LinkAnnotation from PDF document.
```csharp
class ExampleLinkAnnotations
    {
        // The path to the documents directory.
        private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
 public static void GetLinkAnnotations()
    {
        // Load the PDF file
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);
        foreach (Aspose.Pdf.Annotations.Annotation annot in linkAnnotations)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
            TextAbsorber absorber = new TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            document.Pages[1].Accept(absorber);
            string extractedText = absorber.Text;
            // Print the text associated with hyperlink
            Console.WriteLine(extractedText);
        }
    }

```
The following code snippet shows how to Delete Link Annotation from PDF file. For this we need to find and and remove all link annotations on the 1st page. After this we will save document with removed annotation. 
```csharp
class ExampleLinkAnnotations
    {
        // The path to the documents directory.
        private const string _dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
  public static void DeleteLinkAnnotations()
    {
        // Load the PDF file
        Document document = new Document(System.IO.Path.Combine(_dataDir, "SimpleResume_mod.pdf"));
        // Find and delete all link annotation on the 1st page
        var linkAnnotations = document.Pages[1].Annotations.Where(a => a.AnnotationType == AnnotationType.Link);

        foreach (var la in linkAnnotations)
            document.Pages[1].Annotations.Delete(la);
        // Save document with removed annotation
        document.Save(System.IO.Path.Combine(_dataDir, "SimpleResume_del.pdf"));
    }
}
```




