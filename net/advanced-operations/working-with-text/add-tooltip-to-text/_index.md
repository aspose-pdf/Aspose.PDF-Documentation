---
title: PDF Tooltip
linktitle: PDF Tooltip
type: docs
weight: 20
url: /net/pdf-tooltip/
description: Aspose.PDF implements a function of hiding actions, with which you can show/hide an annotation when you enter/leave the mouse over an invisible button.
lastmod: "2020-12-23"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Add Tooltip to Searched Text by adding Invisible Button

It is often required to add some details for a phrase or specific word as a tooltip in the PDF document so that it can popup when the user hovers the mouse cursor over the text. Aspose.PDF for .NET provides this feature to create tooltips by adding an invisible button over the searched text. The following code snippet will show you the way to achieve this functionality:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
string outputFile = dataDir + "Tooltip_out.pdf";

// Create sample document with text
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("Move the mouse cursor here to display a tooltip"));
doc.Pages[1].Paragraphs.Add(new TextFragment("Move the mouse cursor here to display a very long tooltip"));
doc.Save(outputFile);

// Open document with text
Document document = new Document(outputFile);
// Create TextAbsorber object to find all the phrases matching the regular expression
TextFragmentAbsorber absorber = new TextFragmentAbsorber("Move the mouse cursor here to display a tooltip");
// Accept the absorber for the document pages
document.Pages.Accept(absorber);
// Get the extracted text fragments
TextFragmentCollection textFragments = absorber.TextFragments;

// Loop through the fragments
foreach (TextFragment fragment in textFragments)
{
    // Create invisible button on text fragment position
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // AlternateName value will be displayed as tooltip by a viewer application
    field.AlternateName = "Tooltip for text.";
    // Add button field to the document
    document.Form.Add(field);
}

// Next will be sapmle of very long tooltip
absorber = new TextFragmentAbsorber("Move the mouse cursor here to display a very long tooltip");
document.Pages.Accept(absorber);
textFragments = absorber.TextFragments;

foreach (TextFragment fragment in textFragments)
{
    ButtonField field = new ButtonField(fragment.Page, fragment.Rectangle);
    // Set very long text
    field.AlternateName = "Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                            " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                            " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                            " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                            " Duis aute irure dolor in reprehenderit in voluptate velit" +
                            " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                            " occaecat cupidatat non proident, sunt in culpa qui officia" +
                            " deserunt mollit anim id est laborum.";
    document.Form.Add(field);
}

// Save document
document.Save(outputFile);
```

{{% alert color="primary" %}}

Concerning to the length of the tooltip, the tooltip text is contained in the PDF document as PDF string type, outside of the content stream. There is no effective restriction on such strings in PDF files (See PDF Reference Appendix C.). However, a conforming reader (e.g. Adobe Acrobat) running on a particular processor and in a particular operating environment does have such a limit. Please refer to your PDF reader application documentation.

{{% /alert %}}

## Create a Hidden Text Block and Show it on Mouse Over

In Aspose.PDF, a feature to hide actions is implemented by which it is possible to show/hide text box field (or any other type of annotation) on mouse enter/exit over some invisible button. For this purpose, Aspose.Pdf.Annotations.HideAction Class is used to assign the action of hide/show to the text block. Please use the following code snippet to Show/Hide a Text Block on Mouse Enter/Exit.

Please also take into account that PDF actions in the documents work fine in the conforming readers (e.g. Adobe Reader) but no warranties for other PDF readers (e.g. web browser plugins). We have provided a brief investigation and found:

- All implementations of the hide action in PDF documents work fine in Internet Explorer v.11.0.
- All implementations of the hide action also work in Opera v.12.14, but we spot some response delay at the first opening of the document.
- Only implementation using HideAction constructor accepting field name works if Google Chrome v.61.0 browses the document; Please use corresponding constructors if browsing in the Google Chrome is significant:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string outputFile = dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

// Create sample document with text
Document doc = new Document();
doc.Pages.Add().Paragraphs.Add(new TextFragment("Move the mouse cursor here to display floating text"));
doc.Save(outputFile);

// Open document with text
Document document = new Document(outputFile);
// Create TextAbsorber object to find all the phrases matching the regular expression
TextFragmentAbsorber absorber = new TextFragmentAbsorber("Move the mouse cursor here to display floating text");
// Accept the absorber for the document pages
document.Pages.Accept(absorber);
// Get the first extracted text fragment
TextFragmentCollection textFragments = absorber.TextFragments;
TextFragment fragment = textFragments[1];

// Create hidden text field for floating text in the specified rectangle of the page
TextBoxField floatingField = new TextBoxField(fragment.Page, new Rectangle(100, 700, 220, 740));
// Set text to be displayed as field value
floatingField.Value = "This is the \"floating text field\".";
// We recommend to make field 'readonly' for this scenario
floatingField.ReadOnly = true;
// Set 'hidden' flag to make field invisible on document opening
floatingField.Flags |= AnnotationFlags.Hidden;

// Setting a unique field name isn't necessary but allowed
floatingField.PartialName = "FloatingField_1";

// Setting characteristics of field appearance isn't necessary but makes it better
floatingField.DefaultAppearance = new DefaultAppearance("Helv", 10, System.Drawing.Color.Blue);
floatingField.Characteristics.Background = System.Drawing.Color.LightBlue;
floatingField.Characteristics.Border = System.Drawing.Color.DarkBlue;
floatingField.Border = new Border(floatingField);
floatingField.Border.Width = 1;
floatingField.Multiline = true;

// Add text field to the document
document.Form.Add(floatingField);

// Create invisible button on text fragment position
ButtonField buttonField = new ButtonField(fragment.Page, fragment.Rectangle);
// Create new hide action for specified field (annotation) and invisibility flag.
// (You also may reffer floating field by the name if you specified it above.)
// Add actions on mouse enter/exit at the invisible button field
buttonField.Actions.OnEnter = new HideAction(floatingField, false);
buttonField.Actions.OnExit = new HideAction(floatingField);

// Add button field to the document
document.Form.Add(buttonField);

// Save document
document.Save(outputFile);
```
