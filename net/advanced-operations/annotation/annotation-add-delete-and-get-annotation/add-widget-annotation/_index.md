---
title: Add Widget Annotation
type: docs
weight: 80
url: /net/add-widget-annotation/
description: This page describes how to add widget annotations to PDF documents with Aspose.PDF for .NET. The example of code snippet shows how to create buttons for the PDF file.
---

Interactive forms use [Widget Annotations](https://apireference.aspose.com/pdf/net/aspose.pdf.annotations/widgetannotation) to represent the appearance of fields and to manage user interactions.
We use these form elements that add to a PDF to make it easier to enter, submit information, or perform some other user interactions.

Widget Annotations are a graphical representation of a form field on specific pages, so we cannot create it directly as an annotation.

Each Widget Annotation will have appropriate graphics (appearance) depending on its type. After creation, certain visual aspects can be changed, such as border style and background color.
Other properties such as text color and font can be changed through the field, once attached to one. 

In some cases, you may want a field to appear on more than one page, repeating the same value. In that case, fields that normally have just one widget may have multiple widgets attached: a TextField, ListBox, ComboBox, and CheckBox usually have exactly one, while the RadioGroup has multiple widgets, one for each radio button.
Someone filling out the form may use any of those widgets to update the field's value, and this is reflected in all the other widgets as well.

Each form field for each place in the document represents one Widget Annotation. The location-specific data of Widget Annotation are added to the particular page. Each form field has several variations. A button can be a radio button, a checkbox, or a push-button. A choice widget can be a list box or a combo box.

In this sample, we will learn how to add the push-buttons for navigation in the document.

## Add Button to the Document

```csharp
document = new Document();
var page = document.Pages.Add();
var rect = new Rectangle(72, 748, 164, 768);
var printButton = new ButtonField(page, rect)
{
    AlternateName = "Print current document",
    Color = Color.Black,
    PartialName = "printBtn1",
    NormalCaption = "Print Document"
};
var border = new Border(printButton)
{
    Style = BorderStyle.Solid,
    Width = 2
};
printButton.Border = border;
printButton.Characteristics.Border =
    System.Drawing.Color.FromArgb(255, 0, 0, 255);
printButton.Characteristics.Background =  
    System.Drawing.Color.FromArgb(255, 0, 191, 255);
document.Form.Add(printButton);
```

This button has border and set a background. Also we set a button name (Name), a tooltip (AlternateName), a label (NormalCaption), and a color of the label text (Color).

## Using Document-navigation actions

Exist more complex example of the Widget Annotations usage - document navigation in PDF document. This may be needed to prepare a PDF document presentation.
  
This example shows how to create 4 buttons:

```csharp
var document = new Document(@"C:\\tmp\\JSON Fundamenals.pdf");
var buttons = new ButtonField[4];
var alternateNames = new[] { "Go to first page", "Go to prev page", "Go to next page", "Go to last page" };
var normalCaptions = new[] { "First", "Prev", "Next", "Last" };
PredefinedAction[] actions = {
PredefinedAction.FirstPage,
PredefinedAction.PrevPage,
PredefinedAction.NextPage,
PredefinedAction.LastPage };
var clrBorder = System.Drawing.Color.FromArgb(255, 0, 255, 0);
var clrBackGround = System.Drawing.Color.FromArgb(255, 0, 96, 70);
```

We should create the buttons without attaching them to the page.

```csharp
for (var i = 0; i < 4; i++)
{
    buttons[i] = new ButtonField(document,
           new Rectangle(32 + i * 80, 28, 104 + i * 80, 68))
    {
       AlternateName = alternateNames[i],
       Color = Color.White,
       NormalCaption = normalCaptions[i],
       OnActivated = new NamedAction(actions[i])
    };
    buttons[i].Border = new Border(buttons[i])
    {
       Style = BorderStyle.Solid,
       Width = 2
    };
    buttons[i].Characteristics.Border = clrBorder;
    buttons[i].Characteristics.Background = clrBackGround;
}
```

We should duplicate this array of buttons on each page in the document.

```csharp
for (var pageIndex = 1; pageIndex <= document.Pages.Count;
                                                        pageIndex++)
    for (var i = 0; i < 4; i++)
        document.Form.Add(buttons[i], 
          $"btn{pageIndex}_{i + 1}", pageIndex);
 
```

We call [Form.Add method](https://apireference.aspose.com/pdf/net/aspose.pdf.forms.form/add/methods/2) with the following parameters: field, name, and the index of the pages that this field will be added to.

And to get the full result, we need disable the “First” and “Prev” buttons on the first page and the “Next” and “Last” buttons on the last page.

```csharp
document.Form["btn1_1"].ReadOnly = true;
document.Form["btn1_2"].ReadOnly = true;

document.Form[$"btn{document.Pages.Count}_3"].ReadOnly = true;
document.Form[$"btn{document.Pages.Count}_4"].ReadOnly = true;
```

For more detailed information and possibilities of this features see also the [Working with Forms](/pdf/net/acroforms//).