---
title: AcroForms
type: docs
weight: 10
url: /net/acroforms/
description: With Aspose.PDF for .NET you may create a form from scratch, fill the form field in a PDF document, extract data from the form, add or remove fields in the existing form.
---

## Fundamentals of AcroForms

**AcroForms** are the original PDF forms technology. AcroForms is a page oriented form. They were first introduced in 1998. They accept input in Forms Data Format or FDF and XML Forms Data Format or xFDF. Third party vendors support AcroForms. When Adobe introduced the AcroForms, they referred to them as “PDF form that is authored with Adobe Acrobat Pro/Standard and that is not a special type of static or dynamic XFA form. Acroforms are portable and they work on all platforms.

You can use AcroForms to add additional pages to the PDF form document. Thanks to the concept of Templates, you can use AcroForms to support populating the form with multiple database records.

PDF 1.7 supports two different methods for integrating data and PDF forms.

*AcroForms (also known as Acrobat forms)*, introduced and included in the PDF 1.2 format specification.

*Adobe XML Forms Architecture (XFA) forms*, introduced in the PDF 1.5 format specification as an optional feature (The XFA specification is not included in the PDF specification, it is only referenced.

In order to understand **Acroforms** vs **XFA** forms, we need to understand the basics first. For starters, both are PDF forms that you can use. Acroforms is the older one, created back in 1998, and it is still referred as the classic PDF form. XFA forms are webpages you can save as a PDF, and appeared back in 2003. It took some time before PDF started accepting XFA forms.

AcroForms have capabilities not found in XFA and conversely XFA has some capabilities not found in AcroForms.  For example:

- AcroForms support the concept of “Templates”, allowing additional pages to be added to the PDF form document to support populating the form with multiple database records.
- XFA supports the concept of document reflow allowing a field to resize if needed to accommodate data.

## Create form from scratch

### Add Form Field in a PDF Document

The [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) class provides a collection named [Form](https://apireference.aspose.com/pdf/net/aspose.pdf/document/properties/form) which helps you manage form fields in a PDF document.

To add a form field:

1. Create the form field you want to add.
1. Call the [Form](https://apireference.aspose.com/pdf/net/aspose.pdf/document/properties/form) collection’s Add method.

### Adding TextBoxField

Below example shows how to add a [TextBoxField](https://apireference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield).

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Open document
Document pdfDocument = new Document(dataDir + "TextField.pdf");

// Create a field
TextBoxField textBoxField = new TextBoxField(pdfDocument.Pages[1], new Aspose.Pdf.Rectangle(100, 200, 300, 300));
textBoxField.PartialName = "textbox1";
textBoxField.Value = "Text Box";

// TextBoxField.Border = new Border(
Border border = new Border(textBoxField);
border.Width = 5;
border.Dash = new Dash(1, 1);
textBoxField.Border = border;

textBoxField.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);

// Add field to the document
pdfDocument.Form.Add(textBoxField, 1);

dataDir = dataDir + "TextBox_out.pdf";
// Save modified PDF
pdfDocument.Save(dataDir);
``` 

### Adding RadioButtonField 

The following code snippets show how to add [RadioButtonField](https://apireference.aspose.com/pdf/net/aspose.pdf.forms/radiobuttonfield) in a PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Instantiate Document object
Document pdfDocument = new Document();
// Add a page to PDF file
pdfDocument.Pages.Add();
// Instatiate RadioButtonField object with page number as argument
RadioButtonField radio = new RadioButtonField(pdfDocument.Pages[1]);
// Add first radio button option and also specify its origin using Rectangle object
radio.AddOption("Test", new Rectangle(0, 0, 20, 20));
// Add second radio button option
radio.AddOption("Test1", new Rectangle(20, 20, 40, 40));
// Add radio button to form object of Document object
pdfDocument.Form.Add(radio);

dataDir = dataDir + "RadioButton_out.pdf";
// Save the PDF file
pdfDocument.Save(dataDir);
```

The following code snippet shows the steps to add RadioButtonField with three options and place them inside Table cells.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

Document doc = new Document();
Page page = doc.Pages.Add();
Aspose.Pdf.Table table = new Aspose.Pdf.Table();
table.ColumnWidths = "120 120 120";
page.Paragraphs.Add(table);
Row r1 = table.Rows.Add();
Cell c1 = r1.Cells.Add();
Cell c2 = r1.Cells.Add();
Cell c3 = r1.Cells.Add();

RadioButtonField rf = new RadioButtonField(page);
rf.PartialName = "radio";
doc.Form.Add(rf, 1);

RadioButtonOptionField opt1 = new RadioButtonOptionField();
RadioButtonOptionField opt2 = new RadioButtonOptionField();
RadioButtonOptionField opt3 = new RadioButtonOptionField();

opt1.OptionName = "Item1";
opt2.OptionName = "Item2";
opt3.OptionName = "Item3";

opt1.Width = 15;
opt1.Height = 15;
opt2.Width = 15;
opt2.Height = 15;
opt3.Width = 15;
opt3.Height = 15;

rf.Add(opt1);
rf.Add(opt2);
rf.Add(opt3);

opt1.Border = new Border(opt1);
opt1.Border.Width = 1;
opt1.Border.Style = BorderStyle.Solid;
opt1.Characteristics.Border = System.Drawing.Color.Black;
opt1.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt1.Caption = new TextFragment("Item1");
opt2.Border = new Border(opt1);
opt2.Border.Width = 1;
opt2.Border.Style = BorderStyle.Solid;
opt2.Characteristics.Border = System.Drawing.Color.Black;
opt2.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt2.Caption = new TextFragment("Item2");
opt3.Border = new Border(opt1);
opt3.Border.Width = 1;
opt3.Border.Style = BorderStyle.Solid;
opt3.Characteristics.Border = System.Drawing.Color.Black;
opt3.DefaultAppearance.TextColor = System.Drawing.Color.Red;
opt3.Caption = new TextFragment("Item3");
c1.Paragraphs.Add(opt1);
c2.Paragraphs.Add(opt2);
c3.Paragraphs.Add(opt3);

dataDir = dataDir + "RadioButtonWithOptions_out.pdf";
// Save the PDF file
doc.Save(dataDir);
```

### Adding Caption to RadioButtonField

Following code snippet shows how to add caption which will be associated with RadioButtonField:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Load source PDF form
Aspose.Pdf.Facades.Form form1 = new Aspose.Pdf.Facades.Form(dataDir + "RadioButtonField.pdf");
Document PDF_Template_PDF_HTML = new Document(dataDir + "RadioButtonField.pdf");
foreach (var item in form1.FieldNames)
{
    Console.WriteLine(item.ToString());
    Dictionary<string, string> radioOptions = form1.GetButtonOptionValues(item);
    if (item.Contains("radio1"))
    {
        Aspose.Pdf.Forms.RadioButtonField field0 = PDF_Template_PDF_HTML.Form[item] as Aspose.Pdf.Forms.RadioButtonField;
        Aspose.Pdf.Forms.RadioButtonOptionField fieldoption = new Aspose.Pdf.Forms.RadioButtonOptionField();
        fieldoption.OptionName = "Yes";
        fieldoption.PartialName = "Yesname";

        var updatedFragment = new Aspose.Pdf.Text.TextFragment("test123");
        updatedFragment.TextState.Font = FontRepository.FindFont("Arial");
        updatedFragment.TextState.FontSize = 10;
        updatedFragment.TextState.LineSpacing = 6.32f;

        // Create TextParagraph object
        TextParagraph par = new TextParagraph();

        // Set paragraph position
        par.Position = new Position(field0.Rect.LLX, field0.Rect.LLY + updatedFragment.TextState.FontSize);
        // Specify word wraping mode
        par.FormattingOptions.WrapMode = TextFormattingOptions.WordWrapMode.ByWords;

        // Add new TextFragment to paragraph
        par.AppendLine(updatedFragment);

        // Add the TextParagraph using TextBuilder
        TextBuilder textBuilder = new TextBuilder(PDF_Template_PDF_HTML.Pages[1]);
        textBuilder.AppendParagraph(par);

        field0.DeleteOption("item1");
    }
}
PDF_Template_PDF_HTML.Save(dataDir + "RadioButtonField_out.pdf");
```

### Adding ComboBox field

The following code snippets show how to add ComboBox field in a PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Create Document object
Document doc = new Document();

// Add page to document object
doc.Pages.Add();

// Instantiate ComboBox Field object
ComboBoxField combo = new ComboBoxField(doc.Pages[1], new Aspose.Pdf.Rectangle(100, 600, 150, 616));

// Add option to ComboBox
combo.AddOption("Red");
combo.AddOption("Yellow");
combo.AddOption("Green");
combo.AddOption("Blue");

// Add combo box object to form fields collection of document object
doc.Form.Add(combo);
dataDir = dataDir + "ComboBox_out.pdf";
// Save the PDF document
doc.Save(dataDir);
```

### Add Tooltip to Form Field

The Document class provides a collection named Form which manages form fields in a PDF document. To add a tooltip to a form field, use the Field class AlternateName. Adobe Acrobat uses the ‘alternate name’ as a field tooltip.

The code snippets that follow show how to add a tooltip to a form field, first using C# and then Visual Basic.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Load source PDF form
Document doc = new Document(dataDir + "AddTooltipToField.pdf");

// Set the tooltip for textfield
(doc.Form["textbox1"] as Field).AlternateName = "Text box tool tip";

dataDir = dataDir + "AddTooltipToField_out.pdf";
// Save the updated document
doc.Save(dataDir);
```

## Fill Form Field in a PDF Document

To fill a form field, get the field from the Document object’s Form collection. then set the field value using the field’s Value property.

This example selects a TextBoxField and sets its value using the Value property.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Open document
Document pdfDocument = new Document(dataDir + "FillFormField.pdf");

// Get a field
TextBoxField textBoxField = pdfDocument.Form["textbox1"] as TextBoxField;

// Modify field value
textBoxField.Value = "Value to be filled in the field";
dataDir = dataDir + "FillFormField_out.pdf";
// Save updated document
pdfDocument.Save(dataDir); 
```

## Extract data from form

### Get Values from all the Fields of PDF Document

To get values from all the fields in a PDF document, you need to navigate through all the form fields and then get the value using the Value property. Get each field from the Form collection, in the base field type called Field and access its Value property.

The following code snippets show how to get the values of all the fields from a PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Open document
Document pdfDocument = new Document(dataDir + "GetValuesFromAllFields.pdf");

// Get values from all fields
foreach (Field formField in pdfDocument.Form)
{
    Console.WriteLine("Field Name : {0} ", formField.PartialName);
    Console.WriteLine("Value : {0} ", formField.Value);
}
```

### Get/Set FieldLimit

The FormEditor class SetFieldLimit("textbox1", 20) method allows you to set a field limit, the maximum number of characters that can be entered into a field.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Adding Field with limit
FormEditor form = new FormEditor();

form.BindPdf( dataDir + "input.pdf");
form.SetFieldLimit("textbox1", 15);
dataDir = dataDir + "SetFieldLimit_out.pdf";
form.Save(dataDir);
```
Similarly, Aspose.PDF has a method that gets the field limit using the DOM approach. The following code snippet shows the steps.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
// Getting maximum field limit using DOM
Document doc = new Document(dataDir + "FieldLimit.pdf");
Console.WriteLine("Limit: " + (doc.Form["textbox1"] as TextBoxField).MaxLen);
```
You can also get the same value using the *Aspose.PDF.Facades* namespace using the following code snippet.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
// Getting maximum field limit using Facades
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
form.BindPdf(dataDir + "FieldLimit.pdf");
Console.WriteLine("Limit: " + form.GetFieldLimit("textbox1"));
```
### Get Value from an Individual Field of PDF Document

The form field’s Value property allows you to get the value of a particular field. To get the value, get the form field from the Document object’s Form collection. This example selects a [TextBoxField](https://apireference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield) and retrieves its value using the Value property.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Open document
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");

// Get a field
TextBoxField textBoxField = pdfDocument.Form["textbox1"] as TextBoxField;

// Get field value
Console.WriteLine("PartialName : {0} ", textBoxField.PartialName);
Console.WriteLine("Value : {0} ", textBoxField.Value);
```
To get the submit button’s URL, use the following lines of code.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Open document
Document pdfDocument = new Document(dataDir + "GetValueFromField.pdf");
SubmitFormAction act = pdfDocument.Form[1].OnActivated as SubmitFormAction;
if(act != null)
Console.WriteLine(act.Url.Name);
```
### Get Form Fields from a Specific Region of PDF File

Sometimes, you might know where in a document a form field is, but not have it’s name. For example, if all you have to go from is a schematic of a printed form. With Aspose.PDF for .NET, this is not a problem. You can find out which fields are in a given region of a PDF file. To get form fields from a specific region of a PDF file:

1. Open the PDF file using the [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object.
1. Get the form from the document’s Forms collection.
1. Specify the rectangular region and pass it to the Form object’s GetFieldsInRect method. A Fields collection is returned.
1. Use this to manipulate the fields.

The following code snippet shows how to get form fields in a specific rectangular region of a PDF file.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Open pdf file
Aspose.Pdf.Document doc = new Aspose.Pdf.Document(dataDir + "GetFieldsFromRegion.pdf");

// Create rectangle object to get fields in that area
Aspose.Pdf.Rectangle rectangle = new Aspose.Pdf.Rectangle(35, 30, 500, 500);

// Get the PDF form
Aspose.Pdf.Forms.Form form = doc.Form;

// Get fields in the rectangular area
Aspose.Pdf.Forms.Field[] fields = form.GetFieldsInRect(rectangle);

// Display Field names and values
foreach (Field field in fields)
{
    // Display image placement properties for all placements
    Console.Out.WriteLine("Field Name: " + field.FullName + "-" + "Field Value: " + field.Value);
}
```
### Set Form Field Font Other Than the 14 Core PDF Fonts

Form fields in Adobe PDF files can be configured to use specific default fonts. In the early versions of Aspose.PDF, only the 14 default fonts were supported. Later releases allowed developers to apply any font. To set and update the default font used for form fields, use the DefaultAppearance(Font font, double size, Color color) class. This class can be found under the Aspose.PDF.InteractiveFeatures namespace. To use this object, use the Field class DefaultAppearance property.

The following code snippet shows how to set the default font for PDF form fields.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Open document
Document pdfDocument = new Document(dataDir + "FormFieldFont14.pdf");

// Get particular form field from document
Aspose.Pdf.Forms.Field field = pdfDocument.Form["textbox1"] as Aspose.Pdf.Forms.Field;

// Create font object
Aspose.Pdf.Text.Font font = FontRepository.FindFont("ComicSansMS");

// Set the font information for form field
// Field.DefaultAppearance = new Aspose.Pdf.Forms.in.DefaultAppearance(font, 10, System.Drawing.Color.Black);

dataDir = dataDir + "FormFieldFont14_out.pdf";
// Save updated document
pdfDocument.Save(dataDir); 
```
## Add/remove fields in existing form

All the form fields are contained in the Document object’s Form collection. This collection provides different methods that manage form fields, including the Delete method. If you want to delete a particular field, pass the field name as a parameter to the Delete method and then save the updated PDF document. The following code snippet shows how to delete a particular field from a PDF document.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

// Open document
Document pdfDocument = new Document(dataDir + "DeleteFormField.pdf");

// Delete a particular field by name
pdfDocument.Form.Delete("textbox1");
dataDir = dataDir + "DeleteFormField_out.pdf";
// Save modified document
pdfDocument.Save(dataDir);
```
