---
title: Working with Actions in PDF
linktitle: Actions
type: docs
weight: 20
url: /net/actions/
description: This section explains how to add actions to the document and form fields programmatically with C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Actions in PDF",
    "alternativeHeadline": "How to add Actions in PDF",
    "author": {
        "@type": "Person",
        "name":"Andriy Andrukhovskiy",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, c#, actions in pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/actions/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/actions/"
    },
    "dateModified": "2022-02-04",
    "description": "This section explains how to add actions to the document and form fields programmatically with C#."
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Add Hyperlink in a PDF File

It is possible to add hyperlinks to PDF files, either to allow readers to navigate to another part of the PDF, or to external content.

In order to add web hyperlinks to PDF documents:

1. Create a [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) Class object.
1. Get the [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) Class you want to add the link to.
1. Create a [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) object using the Page and [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf/rectangle) objects. The rectangle object is used to specify the location on the page where the link should be added.
1. Set the Action property to the [GoToURIAction](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/gotouriaction) object which specifies the location of the remote URI.
1. To display a hyperlink text, add a text string on a location similar to where the [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) object is placed.
1. To add a free text:

- Instantiate an [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) object. It also accepts Page and Rectangle objects as argument, so it is possible to provide same values as specified against the LinkAnnotation constructor.
- Using the [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) object's Contents property, specify the string that should be displayed in the output PDF.
- Optionally, set the border width of both the [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) and FreeTextAnnotation objects to 0 so that they do not appear in the PDF document.
- Once the [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) and [FreeTextAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/freetextannotation) objects have been defined, add these links to the [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) object's Annotations collection.
- Finally, save the updated PDF using the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object's [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method.

The following code snippet shows you how to add a hyperlink to a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Open document
Document document = new Document(dataDir + "AddHyperlink.pdf");
// Create link
Page page = document.Pages[1];
// Create Link annotation object
LinkAnnotation link = new LinkAnnotation(page, new Aspose.Pdf.Rectangle(100, 100, 300, 300));
// Create border object for LinkAnnotation
Border border = new Border(link);
// Set the border width value as 0
border.Width = 0;
// Set the border for LinkAnnotation
link.Border = border;
// Specify the link type as remote URI
link.Action = new GoToURIAction("www.aspose.com");
// Add link annotation to annotations collection of first page of PDF file
page.Annotations.Add(link);

// Create Free Text annotation
FreeTextAnnotation textAnnotation = new FreeTextAnnotation(document.Pages[1], new Aspose.Pdf.Rectangle(100, 100, 300, 300), new DefaultAppearance(Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman"), 10, System.Drawing.Color.Blue));
// String to be added as Free text
textAnnotation.Contents = "Link to Aspose website";
// Set the border for Free Text Annotation
textAnnotation.Border = border;
// Add FreeText annotation to annotations collection of first page of Document
document.Pages[1].Annotations.Add(textAnnotation);

// Save updated document
document.Save(dataDir + "AddHyperlink_out.pdf");
```

## Create Hyperlink to pages in same PDF

Aspose.PDF for .NET provides a great feature to PDF creation as well as its manipulation. It also offers the feature to add links to PDF pages and a link can either direct to pages in another PDF file, a web URL, link to launch an Application or even link to pages in same PDF file. In order to add local hyperlinks (links to pages in same PDF file), a class named [LocalHyperlink](https://reference.aspose.com/pdf/net/aspose.pdf/localhyperlink) is added to Aspose.PDF namespace and this class has a property named TargetPageNumber, which is used to specify the target/destination page for hyperlink.

In order to add the local hyperlink, we need to create a TextFragment so that link can be associated with the TextFragment. The [TextFragment](https://reference.aspose.com/pdf/net/aspose.pdf.text/textfragment) class has a property named Hyperlink which is used to associate LocalHyperlink instance. The following code snippet shows the steps to accomplish this requirement.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Create Document instance
Document document = new Document();
// Add page to pages collection of PDF file
Page page = document.Pages.Add();
// Create Text Fragment instance
TextFragment text = new TextFragment("link page number test to page 7");
// Create local hyperlink instance
LocalHyperlink link = new LocalHyperlink();
// Set target page for link instance
link.TargetPageNumber = 7;
// Set TextFragment hyperlink
text.Hyperlink = link;
// Add text to paragraphs collection of Page
page.Paragraphs.Add(text);
// Create new TextFragment instance
text = new TextFragment("link page number test to page 1");
// TextFragment should be added over new page
text.IsInNewPage = true;
// Create another local hyperlink instance
link = new LocalHyperlink();
// Set Target page for second hyperlink
link.TargetPageNumber = 1;
// Set link for second TextFragment
text.Hyperlink = link;
// Add text to paragraphs collection of page object
page.Paragraphs.Add(text);

// Save updated document
document.Save(dataDir + "CreateLocalHyperlink_out.pdf");
```

## Get PDF Hyperlink Destination (URL)

Links are represented as annotations in a PDF file and they can be added, updated or deleted. Aspose.PDF for .NET also supports getting the destination (URL) of the hyperlink in PDF file.

To get a link's URL:

1. Create a [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Get the [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) you want to extract links from.
1. Use the [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) class to extract all the [LinkAnnotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/linkannotation) objects from the specified page.
1. Pass the [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) object to the [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) object's Accept method.
1. Get all the selected link annotations into an IList object using the [AnnotationSelector](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotationselector) object's Selected property.
1. Finally, extract the LinkAnnotation Action as GoToURIAction.

The following code snippet shows how to get hyperlink destinations (URL) from a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Load the PDF file
Document document = new Document(dataDir + "input.pdf");

// Traverse through all the page of PDF
foreach (Page page in document.Pages)
{
    // Get the link annotations from particular page
    AnnotationSelector selector = new AnnotationSelector(new LinkAnnotation(page, Aspose.Pdf.Rectangle.Trivial));

    page.Accept(selector);
    // Create list holding all the links
    IList<Annotation> list = selector.Selected;
    // Iterate through invidiaul item inside list
    foreach (LinkAnnotation a in list)
    {
        // Print the destination URL
        Console.WriteLine("\nDestination: " + (a.Action as GoToURIAction).URI + "\n");
    }
}
```

## Get Hyperlink Text

A hyperlink has two parts: the text that shows in the document, and the destination URL. In some cases, it's the text rather than the URL we need.

Text and annotations/actions in a PDF file are represented by different entities. Text on a page is just a set of words and characters, while annotations bring some interactivity such as that inherent in a hyperlink.

To find the URL content, you need to work with both annotation and text. The [Annotation](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/annotation) object does not have itself have the text but sits under the text on the page. So to get the text, the Annotation gives the URL's bounds, while the Text object gives the URL contents. Please see the following code snippet.

```csharp
public static void Run()
{
    try
    {
        // ExStart:GetHyperlinkText
        // The path to the documents directory.
        string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
        // Load the PDF file
        Document document = new Document(dataDir + "input.pdf");
        // Iterate through each page of PDF
        foreach (Page page in document.Pages)
        {
            // Show link annotation
            ShowLinkAnnotations(page);
        }
        // ExEnd:GetHyperlinkText
    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.Message);
    }
}

// ExStart:ShowLinkAnnotations
public static void ShowLinkAnnotations(Page page)
{
    foreach (Annotation annot in page.Annotations)
    {
        if (annot is LinkAnnotation)
        {
            // Print the URL of each Link Annotation
            Console.WriteLine("URI: " + ((annot as LinkAnnotation).Action as GoToURIAction).URI);
            TextAbsorber absorber = new TextAbsorber();
            absorber.TextSearchOptions.LimitToPageBounds = true;
            absorber.TextSearchOptions.Rectangle = annot.Rect;
            page.Accept(absorber);
            string extractedText = absorber.Text;
            // Print the text associated with hyperlink
            Console.WriteLine(extractedText);
        }

    }
}
// ExEnd:ShowLinkAnnotations
```

## Remove Document Open Action from a PDF File

[How to Specify PDF Page when Viewing Document](#how-to-specify-pdf-page-when-viewing-document) explained how to tell a document to open on a different page than the first. When concatenating several documents, and one or more has a GoTo action set, you probably want to remove them. For example, if combining two documents and the second one has a GoTo action that takes you to the second page, the output document will open on the second page of the second document instead of the first page of the combined document. To avoid this behavior, remove the open action command.

To remove an open action:

1. Set the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) object's [OpenAction](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/openaction) property to null.
1. Save the updated PDF using the Document object's [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method.

The following code snippet shows how to remove a document open action from the PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();
// Open document
Document document = new Document(dataDir + "RemoveOpenAction.pdf");
// Remove document open action
document.OpenAction = null;

// Save updated document
document.Save(dataDir + "RemoveOpenAction_out.pdf");
```

## How to Specify PDF Page when Viewing Document {#how-to-specify-pdf-page-when-viewing-document}

When viewing PDF files in a PDF viewer such as Adobe Reader, the files usually open on the first page. However, it is possible to set the file to open on a different page.

The [XYZExplicitDestination](https://reference.aspose.com/pdf/net/aspose.pdf.annotations/xyzexplicitdestination) class allows you to specify a page in a PDF file that you want to open. When passing the GoToAction object value to the [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class OpenAction property, the document opens at the page specified against the XYZExplicitDestination object. The following code snippet shows how to specify a page as the document open action.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_LinksActions();

// Load the PDF file
Document document = new Document(dataDir + "SpecifyPageWhenViewing.pdf");
// Get the instance of second page of document
Page page2 = document.Pages[2];
// Create the variable to set the zoom factor of target page
double zoom = 1;
// Create GoToAction instance
GoToAction action = new GoToAction(document.Pages[2]);
// Go to 2 page
action.Destination = new XYZExplicitDestination(page2, 0, page2.Rect.Height, zoom);
// Set the document open action
document.OpenAction = action;
// Save updated document
document.Save(dataDir + "goto2page_out.pdf");
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
