---
title: Add Widget Annotation
type: docs
weight: 80
url: /net/add-widget-annotation/
---
# Add Widget Annotation

Interactive forms use widget annotations to represent the appearance of fields and to manage user interactions.
We use these form elements that add to a PDF to make it easier to enter, submit information, or perform some other user interactions.

Widget Annotations can be created explicitly with the new operator. Since each field has specific needs for its widget annotations, there are classes derived from the abstract base class WidgetAnnotation for each of them: RadioButtonWidgetAnnotation, CheckBoxWidgetAnnotation, TextBoxWidgetAnnotation, CombBoxWidgetAnnotation, and ListBoxWidgetAnnotation.

The constructors take two parameters: the page on which the annotation is to appear and the rectangle defining the location and size on that page. 

Each widget annotation will have appropriate graphics (appearance) depending on its type. After creation, certain visual aspects can be changed, such as border style and background color.
Other properties such as text color and font can be changed through the field, once attached to one. 

In some cases, you may want a field to appear on more than one page, repeating the same value. In that case, fields that normally have just one widget may have multiple widgets attached: a TextField, ListBox, ComboBox, and CheckBox usually have exactly one, while the RadioGroup has multiple widgets, one for each radio button.
Someone filling out the form may use any of those widgets to update the field's value, and this is reflected in all the other widgets as well.