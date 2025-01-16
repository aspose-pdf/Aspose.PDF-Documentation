---
title: Create AcroForm - Create Fillable PDF in C#
linktitle: Create AcroForm
type: docs
weight: 10
url: /net/create-form/
description: With Aspose.PDF for .NET you may create a form from scratch in your PDF file
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Create AcroForm - Create Fillable PDF in C#",
    "alternativeHeadline": "Create Interactive Forms in PDF with C#",
    "abstract": "Aspose.PDF for .NET introduces the ability to create fillable PDF forms from scratch, allowing developers to seamlessly integrate customizable form fields such as text boxes, radio buttons, and combo boxes into their PDFs. This functionality empowers users to enhance document interactivity and improve data collection within their applications",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Create AcroForm, fillable PDF, C#, Aspose.PDF, form fields, TextBoxField, RadioButtonField, ComboBoxField, add tooltip, PDF document generation",
    "wordcount": "1125",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
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
    "url": "/net/create-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/create-form/"
    },
    "dateModified": "2024-11-25",
    "description": "With Aspose.PDF for .NET you may create a form from scratch in your PDF file"
}
</script>

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Create form from scratch

### Add Form Field in a PDF Document

The [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) class provides a collection named [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form) which helps you manage form fields in a PDF document.

To add a form field:

1. Create the form field you want to add.
1. Call the [Form](https://reference.aspose.com/pdf/net/aspose.pdf/document/properties/form) collection's Add method.

### Adding TextBoxField

Below example shows how to add a [TextBoxField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/textboxfield).

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextBoxFieldToPdf()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
	{
		// Create a field
		var textBoxField = new Aspose.Pdf.Forms.TextBoxField(document.Pages[1], new Aspose.Pdf.Rectangle(100, 200, 300, 300));
		textBoxField.PartialName = "textbox1";
		textBoxField.Value = "Text Box";

		// Configure border
		var border = new Aspose.Pdf.Annotations.Border(textBoxField);
		border.Width = 5;
		border.Dash = new Aspose.Pdf.Annotations.Dash(1, 1);
		textBoxField.Border = border;

		// Set color
		textBoxField.Color = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);

		// Add field to the document
		document.Form.Add(textBoxField, 1);

		// Save PDF document
		document.Save(dataDir + "TextBox_out.pdf");
	}
}
```

### Adding RadioButtonField

The following code snippets show how to add [RadioButtonField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/radiobuttonfield) in a PDF document.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRadioButtonToPdf()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
	{
		// Add a page to PDF file
		document.Pages.Add();

		// Instantiate RadioButtonField object with page number as argument
		var radio = new Aspose.Pdf.Forms.RadioButtonField(document.Pages[1]);

		// Add first radio button option and also specify its origin using Rectangle object
		radio.AddOption("Test", new Aspose.Pdf.Rectangle(0, 0, 20, 20));

		// Add second radio button option
		radio.AddOption("Test1", new Aspose.Pdf.Rectangle(20, 20, 40, 40));

		// Add radio button to form object of Document object
		document.Form.Add(radio);

		// Save PDF document
		document.Save(dataDir + "RadioButton_out.pdf");
	}
}
```

The following code snippet shows the steps to add RadioButtonField with three options and place them inside Table cells.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddRadioButtonWithOptionsToPdf()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
	{
		// Add a page to PDF file
		var page = document.Pages.Add();

		// Create a table
		var table = new Aspose.Pdf.Table();
		table.ColumnWidths = "120 120 120";
		page.Paragraphs.Add(table);

		// Add a row to the table
		var r1 = table.Rows.Add();

		// Add cells to the row
		var c1 = r1.Cells.Add();
		var c2 = r1.Cells.Add();
		var c3 = r1.Cells.Add();

		// Create a RadioButtonField
		var rf = new Aspose.Pdf.Forms.RadioButtonField(page);
		rf.PartialName = "radio";
		document.Form.Add(rf, 1);

		// Create RadioButtonOptionField options
		var opt1 = new Aspose.Pdf.Forms.RadioButtonOptionField();
		var opt2 = new Aspose.Pdf.Forms.RadioButtonOptionField();
		var opt3 = new Aspose.Pdf.Forms.RadioButtonOptionField();

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

		// Configure borders and captions for options
		opt1.Border = new Aspose.Pdf.Annotations.Border(opt1);
		opt1.Border.Width = 1;
		opt1.Border.Style = Aspose.Pdf.Annotations.BorderStyle.Solid;
		opt1.Characteristics.Border = System.Drawing.Color.Black;
		opt1.DefaultAppearance.TextColor = System.Drawing.Color.Red;
		opt1.Caption = new Aspose.Pdf.Text.TextFragment("Item1");

		opt2.Border = new Aspose.Pdf.Annotations.Border(opt2);
		opt2.Border.Width = 1;
		opt2.Border.Style = Aspose.Pdf.Annotations.BorderStyle.Solid;
		opt2.Characteristics.Border = System.Drawing.Color.Black;
		opt2.DefaultAppearance.TextColor = System.Drawing.Color.Red;
		opt2.Caption = new Aspose.Pdf.Text.TextFragment("Item2");

		opt3.Border = new Aspose.Pdf.Annotations.Border(opt3);
		opt3.Border.Width = 1;
		opt3.Border.Style = Aspose.Pdf.Annotations.BorderStyle.Solid;
		opt3.Characteristics.Border = System.Drawing.Color.Black;
		opt3.DefaultAppearance.TextColor = System.Drawing.Color.Red;
		opt3.Caption = new Aspose.Pdf.Text.TextFragment("Item3");

		// Add options to the cells
		c1.Paragraphs.Add(opt1);
		c2.Paragraphs.Add(opt2);
		c3.Paragraphs.Add(opt3);

		// Save PDF document
		document.Save(dataDir + "RadioButtonWithOptions_out.pdf");
	}
}
```

### Adding Caption to RadioButtonField

Following code snippet shows how to add caption which will be associated with RadioButtonField:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddingCaptionToRadioButtonField()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load source PDF form
    using (var form1 = new Aspose.Pdf.Facades.Form(dataDir + "RadioButtonField.pdf"))
    {
        using (var document = new Aspose.Pdf.Document(dataDir + "RadioButtonField.pdf"))
        {
            foreach (var item in form1.FieldNames)
            {
                Console.WriteLine(item.ToString());
                var radioOptions = form1.GetButtonOptionValues(item);

                if (item.Contains("radio1"))
                {
                    var field0 = document.Form[item] as Aspose.Pdf.Forms.RadioButtonField;
                    var fieldoption = new Aspose.Pdf.Forms.RadioButtonOptionField();
                    fieldoption.OptionName = "Yes";
                    fieldoption.PartialName = "Yesname";

                    var updatedFragment = new Aspose.Pdf.Text.TextFragment("test123");
                    updatedFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("Arial");
                    updatedFragment.TextState.FontSize = 10;
                    updatedFragment.TextState.LineSpacing = 6.32f;

                    // Create TextParagraph object
                    var par = new Aspose.Pdf.Text.TextParagraph();

                    // Set paragraph position
                    par.Position = new Aspose.Pdf.Text.Position(field0.Rect.LLX, field0.Rect.LLY + updatedFragment.TextState.FontSize);
                    // Specify word wraping mode
                    par.FormattingOptions.WrapMode = Aspose.Pdf.Text.TextFormattingOptions.WordWrapMode.ByWords;

                    // Add new TextFragment to paragraph
                    par.AppendLine(updatedFragment);

                    // Add the TextParagraph using TextBuilder
                    var textBuilder = new Aspose.Pdf.Text.TextBuilder(document.Pages[1]);
                    textBuilder.AppendParagraph(par);

                    field0.DeleteOption("item1");
                }
            }

            // Save PDF document
            document.Save(dataDir + "RadioButtonField_out.pdf");
        }
    }
}
```

### Adding ComboBox field

The following code snippets show how to add ComboBox field in a PDF document.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddComboBoxToPdf()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
	{
		// Add page to document object
		document.Pages.Add();

		// Instantiate ComboBox Field object
		var combo = new Aspose.Pdf.Forms.ComboBoxField(document.Pages[1], new Aspose.Pdf.Rectangle(100, 600, 150, 616));

		// Add options to ComboBox
		combo.AddOption("Red");
		combo.AddOption("Yellow");
		combo.AddOption("Green");
		combo.AddOption("Blue");

		// Add combo box object to form fields collection of document object
		document.Form.Add(combo);

		// Save PDF document
		document.Save(dataDir + "ComboBox_out.pdf");
	}
}
```

### Add Tooltip to Form Field

The Document class provides a collection named Form which manages form fields in a PDF document. To add a tooltip to a form field, use the Field class AlternateName. Adobe Acrobat uses the ‘alternate name’ as a field tooltip.

The code snippets that follow show how to add a tooltip to a form field, first using C# and then Visual Basic.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTooltipToField()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddTooltipToField.pdf"))
	{
		// Set the tooltip for textfield
		if (document.Form["textbox1"] is Aspose.Pdf.Forms.Field field)
		{
			field.AlternateName = "Text box tool tip";
		}

		// Save PDF document
		document.Save(dataDir + "AddTooltipToField_out.pdf");
	}
}
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
