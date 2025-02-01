---
title: Using Tooltip 
linktitle: PDF Tooltip
type: docs
weight: 20
url: /java/pdf-tooltip/
description: Learn how to add tooltip to the text fragment in PDF using Java and Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: 
Abstract: The article provides a detailed guide on how to add tooltips to specific text within a PDF document using Aspose.PDF for Java. The process involves creating an invisible button over the text that will display the tooltip when hovered over by the mouse. This is achieved by using the `TextFragmentAbsorber` to locate the text and `ButtonField` to create an invisible button with an `AlternateName` as the tooltip. Additionally, the article discusses implementing a feature to show or hide a text block on mouse hover using `Aspose.Pdf.Annotations.HideAction` class. The article includes Java code snippets demonstrating both functionalities and highlights compatibility considerations for different PDF readers, noting specific behaviors in browsers like Internet Explorer, Opera, and Google Chrome. It emphasizes checking PDF reader documentation for handling tooltip lengths and provides insights into ensuring the correct display of hidden text blocks across platforms.
---

## Add Tooltip to Searched Text by adding Invisible Button

It is often required to add some details for a phrase or specific word as a tooltip in the PDF document so that it can popup when the user hovers the mouse cursor over the text. Aspose.PDF for Java provides this feature to create tooltips by adding an invisible button over the searched text. The following code snippet will show you the way to achieve this functionality:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.ButtonField;
import com.aspose.pdf.Document;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.TextFragmentAbsorber;
import com.aspose.pdf.TextFragmentCollection;

public class ExampleToolTip {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddToolTip() {
        String outputFile = _dataDir + "Tooltip_out.pdf";

        // Create sample document with text
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("Move the mouse cursor here to display a tooltip"));
        doc.getPages().get_Item(1).getParagraphs().add(new TextFragment("Move the mouse cursor here to display a very long tooltip"));
        doc.save(outputFile);

        // Open document with text
        Document document = new Document(outputFile);
        // Create TextAbsorber object to find all the phrases matching the regular expression
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("Move the mouse cursor here to display a tooltip");
        // Accept the absorber for the document pages
        document.getPages().accept(absorber);
        // Get the extracted text fragments
        TextFragmentCollection textFragments = absorber.getTextFragments();

        // Loop through the fragments
        for(TextFragment fragment : textFragments)
        {
            // Create invisible button on text fragment position
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // AlternateName value will be displayed as tooltip by a viewer application
            field.setAlternateName ("Tooltip for text.");
            // Add button field to the document
            document.getForm().add(field);
        }

        // Next will be sapmle of very long tooltip
        absorber = new TextFragmentAbsorber("Move the mouse cursor here to display a very long tooltip");
        document.getPages().accept(absorber);
        textFragments = absorber.getTextFragments();

        for(TextFragment fragment : textFragments)
        {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // Set very long text
            field.setAlternateName ("Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                                    " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                                    " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                                    " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                                    " Duis aute irure dolor in reprehenderit in voluptate velit" +
                                    " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                                    " occaecat cupidatat non proident, sunt in culpa qui officia" +
                                    " deserunt mollit anim id est laborum.");
            document.getForm().add(field);
        }

        // Save document
        document.save(outputFile);
    }
}
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

```java
    public static void name() {
        String outputFile = _dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

        // Create sample document with text
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("Move the mouse cursor here to display floating text"));
        doc.save(outputFile);

        // Open document with text
        Document document = new Document(outputFile);
        // Create TextAbsorber object to find all the phrases matching the regular expression
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("Move the mouse cursor here to display floating text");
        // Accept the absorber for the document pages
        document.getPages().accept(absorber);
        // Get the first extracted text fragment
        TextFragmentCollection textFragments = absorber.getTextFragments();
        TextFragment fragment = textFragments.get_Item(1);

        // Create hidden text field for floating text in the specified rectangle of the page
        TextBoxField floatingField = new TextBoxField(fragment.getPage(), new Rectangle(100, 700, 220, 740));
        // Set text to be displayed as field value
        floatingField.setValue ("This is the \"floating text field\".");
        // We recommend to make field 'readonly' for this scenario
        floatingField.setReadOnly(true);

        // Set 'hidden' flag to make field invisible on document opening
        floatingField.setFlags( floatingField.getFlags() | AnnotationFlags.Hidden);

        // Setting a unique field name isn't necessary but allowed
        floatingField.setPartialName ("FloatingField_1");

        // Setting characteristics of field appearance isn't necessary but makes it better
        DefaultAppearance da = new DefaultAppearance("Helvetica", 16, java.awt.Color.RED);
        floatingField.setDefaultAppearance(da);
        //new DefaultAppearance("Helv", 10, Color.getBlue()
        floatingField.getCharacteristics().setBackground(Color.getLightBlue());
        floatingField.getCharacteristics().setBorder(Color.getDarkBlue());;
        floatingField.setBorder(new Border(floatingField));
        floatingField.getBorder().setWidth(1);
        floatingField.setMultiline(true);

        // Add text field to the document
        document.getForm().add(floatingField);

        // Create invisible button on text fragment position
        Field buttonField = new ButtonField(fragment.getPage(), fragment.getRectangle());
        // Create new hide action for specified field (annotation) and invisibility flag.
        // (You also may reffer floating field by the name if you specified it above.)
        // Add actions on mouse enter/exit at the invisible button field
        buttonField.getActions().setOnEnter(new HideAction(floatingField, false));
        buttonField.getActions().setOnExit (new HideAction(floatingField));

        // Add button field to the document
        document.getForm().add(buttonField);

        // Save document
        document.save(outputFile);
    }
```
