---
title: PDF Widget Annotation 
linktitle: Widget Annotation
type: docs
weight: 80
url: /java/widget-annotation/
description: This article describes how to add controls based on a widget annotations to PDF documents with Aspose.PDF for Java. 
lastmod: "2021-02-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Interactive forms use [Widget Annotations](https://apireference.aspose.com/pdf/java/com.aspose.pdf.class-use/WidgetAnnotation) to represent the appearance of fields and to manage user interactions.
We use these form elements that add to a PDF to make it easier to enter, submit information, or perform some other user interactions.

Widget Annotations are a graphical representation of a form field on specific pages, so we cannot create it directly as an annotation.

Each Widget Annotation will have appropriate graphics (appearance) depending on its type. After creation, certain visual aspects can be changed, such as border style and background color.
Other properties such as text color and font can be changed through the field, once attached to one. 

In some cases, you may want a field to appear on more than one page, repeating the same value. In that case, fields that normally have just one widget may have multiple widgets attached: a TextField, ListBox, ComboBox, and CheckBox usually have exactly one, while the RadioGroup has multiple widgets, one for each radio button.
Someone filling out the form may use any of those widgets to update the field's value, and this is reflected in all the other widgets as well.

Each form field for each place in the document represents one Widget Annotation. The location-specific data of Widget Annotation are added to the particular page. Each form field has several variations. A button can be a radio button, a checkbox, or a push-button. A choice widget can be a list box or a combo box.

In this sample, we will learn how to add the push-buttons for navigation in the document.

## Add Button to the Document

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWidgetAnnotation {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddButton()
    {
        // Load the PDF file
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);
       
        Rectangle rect = new Rectangle(72, 748, 164, 768);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("Print current document");
        printButton.setColor(Color.getBlack());
        printButton.setPartialName("printBtn1");
        printButton.setNormalCaption("Print Document");

        Border border = new Border(printButton);
        border.setStyle(BorderStyle.Solid);
        border.setWidth(2);
        
        printButton.setBorder(border);
        printButton.getCharacteristics().setBorder(Color.fromArgb(255, 0, 0, 255));
        printButton.getCharacteristics().setBackground(Color.fromArgb(255, 0, 191, 255));
        document.getForm().add(printButton);

        document.save(_dataDir + "sample_textannot.pdf");
    }
```

This button has border and set a background. Also we set a button name (Name), a tooltip (AlternateName), a label (NormalCaption), and a color of the label text (Color).

## Using Document-navigation actions

Exist more complex example of the Widget Annotations usage - document navigation in PDF document. This may be needed to prepare a PDF document presentation.
  
This example shows how to create 4 buttons:

```java
public static void AddDocumentNavigationActions() {
// Load the PDF file
Document document = new Document(_dataDir + "JSON Fundamenals.pdf");

ButtonField[] buttons = new ButtonField[4];
String[] alternateNames = { "Go to first page", "Go to prev page", "Go to next page", "Go to last page" };
String[] normalCaptions = { "First", "Prev", "Next", "Last" };
int[] actions = { PredefinedAction.FirstPage, PredefinedAction.PrevPage, PredefinedAction.NextPage,
PredefinedAction.LastPage };
Color clrBorder = Color.fromArgb(255, 0, 255, 0);
Color clrBackGround = Color.fromArgb(255, 0, 96, 70);

for (int i = 0; i < 4; i++) {
buttons[i] = new ButtonField(document, new Rectangle(32 + i * 80, 28, 104 + i * 80, 68));
buttons[i].setAlternateName(alternateNames[i]);
buttons[i].setColor(Color.getWhite());
buttons[i].setNormalCaption(normalCaptions[i]);
buttons[i].setOnActivated(new NamedAction(actions[i]));
Border border = new Border(buttons[i]);
border.setStyle(BorderStyle.Solid);
border.setWidth(2);
buttons[i].setBorder(border);
buttons[i].getCharacteristics().setBorder(clrBorder);
buttons[i].getCharacteristics().setBackground(clrBackGround);
}

for (int pageIndex = 1; pageIndex <= 1; pageIndex++)
for (int i = 0; i < 4; i++)
document.getForm().add(buttons[i], "btn" + pageIndex + "_" + (i + 1), pageIndex);

document.getForm().get("btn1_1").setReadOnly(true);
document.getForm().get("btn1_2").setReadOnly(true);

document.getForm().get("btn" + document.getPages().size() + "_3").setReadOnly(true);
document.getForm().get("btn" + document.getPages().size() + "_4").setReadOnly(true);
document.save(_dataDir + "sample_widgetannot_2.pdf");
}
```
## How to delete Widget Annotation 

Aspose.PDF for Java has rules for removing annotations from your file:

```java
public static void DeleteWidgetAnnotation() {
        // Load the PDF file
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // Filter annotations using AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(new ButtonField(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> buttonFields = annotationSelector.getSelected();

        // delete annotations
        for (Annotation wa : buttonFields) {
            page.getAnnotations().delete(wa);
        }
        document.save(_dataDir + "sample_widgetannot_del.pdf");
    }
}
```