---
title: Using Aspose.PDF FormEditor plugin (.NET version)
type: docs
weight: 30
url: /net/plugins/formeditor/
description: How to Add, Update, and Remove Form Fields in PDF Files using Aspose.PDF Plugins
lastmod: "2024-01-24"
draft: false
---

Aspose.PDF is a powerful and versatile library that allows you to work with PDF documents in various ways. One of the features of Aspose.PDF is the ability to use plugins that extend its functionality and provide more capabilities. In this article, we will show you how to use the FormEditor plugin, which can add, update, and remove form fields in PDF files.

Prerequisites
To follow this tutorial, you will need the following:

* Visual Studio 2019 or later
* Aspose.PDF for .NET 24.1 or later
* A sample PDF file that contains some form fields

You can download the Aspose.PDF and Aspose.PDF.Plugins libraries from the official website or install them using the NuGet Package Manager in Visual Studio.

## Steps

The basic steps to add, update, and remove form fields in PDF files using the FormEditor plugin are:

1. Create an object of the FormEditor class
1. Create an object of the FormEditorAddOptions, FormEditorSetOptions, or FormRemoveSelectedFieldsOptions class, depending on the operation you want to perform
1. Add the input and output data sources to the options object
1. Run the Process method of the FormEditor object

Let's see how to implement these steps in C# code for each operation.

### Step 1: Create an object of the FormEditor class

The FormEditor class is the main class that provides the functionality of adding, updating, and removing form fields in PDF files. To use it, you need to create an instance of it using the default constructor:

```cs
// Create an instance of the FormEditor plugin
var plugin = new FormEditor();
```

### Step 2: Create an object of the FormEditorAddOptions, FormEditorSetOptions, or FormRemoveSelectedFieldsOptions class, depending on the operation you want to perform

The `FormEditorAddOptions`, `FormEditorSetOptions`, and `FormRemoveSelectedFieldsOptions` classes are helper classes that allow you to specify various options and parameters for the form editing operations, such as the form field types, values, properties, predicates, etc. To use them, you need to create an instance of the appropriate class, and pass an array of form field creation options, a predicate and a value, or a predicate. For example, to add three form fields (a checkbox, a combo box, and a textbox) to the first page of the PDF file, you can use the following code:

```cs
    // Create options for adding form fields.
    var options = new FormEditorAddOptions(
        [
            // Create a checkbox form field.
            new FormCheckBoxFieldCreateOptions(1, new Rectangle(110, 700, 125, 715))
            {
                Value = "CheckBoxField 1",
                PartialName = "CheckBoxField_1",
                Color = Color.Blue,
            },
            // Create a combo box form field.
            new FormComboBoxFieldCreateOptions(1, new Rectangle(310, 600, 350, 615))
            {
                Color = Color.Red,
                Editable = true,
                DefaultAppearance = new DefaultAppearance("Arial Bold", 12, System.Drawing.Color.DarkGreen),
                Options = ["option1", "option2", "option3"],
                Selected = 2
            },
            // Create a textbox form field.
            new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715))
            {
                MaxLen = 10,
                Value = "Some text",
                Color = Color.Chocolate
            }
        ]);
```

To update the values of the form fields whose values are "a value" or "an another value" to "new value", you can use the following code:

```cs
    var options = new FormEditorSetOptions(
    (field) => { return field.Value == "a value" || field.Value == "an another value"; },
    new FormFieldSetOptions()
    {
        Value = "new value"
    });
```

To remove the form fields whose lower-left x-coordinate is greater than 300, you can use the following code:

```cs
// Create options for removing form fields
var options = new FormRemoveSelectedFieldsOptions((field) => field.Rect.LLX > 300);
```

### Step 3: Add the input and output data sources to the options object

The input and output data sources are the PDF files that you want to edit and save. They can be either file paths or streams. To add them to the options object, you need to use the AddInput and AddOutput methods of the options class. For example, to edit a PDF file named sample_forms.pdf in the C:\Samples\Output folder and save it as sample_forms2.pdf in the same folder, you can use the following code:

```cs
// Specify the input and output file paths
string inputPath = $@"C:\Samples\Output\sample_forms.pdf";
string outputPath = $@"C:\Samples\Output\sample_forms2.pdf";

// Create a new instance of the FileDataSource class for the input and output files
FileDataSource inputData = new(inputPath);
FileDataSource outputData = new(outputPath);

// Add the input and output data sources to the options
options.AddInput(inputData);
options.AddOutput(outputData);
```

### Step 4: Run the Process method of the FormEditor object

The final step is to run the Process method of the FormEditor object, passing the options object as a parameter. This method will perform the form editing operation and return a ResultContainer object, which contains the results of the operation, such as the status, the messages, the output data sources, etc. You can access the results using the properties and methods of the ResultContainer class. For example, to get the first result from the result collection and print it to the console, you can use the following code:

```cs
// Process the form editing operation using the plugin and options
ResultContainer result = plugin.Process(options);

// Get the first result from the result collection
var result = resultContainer.ResultCollection[0];

// Print the result
Console.WriteLine(result);
```

The result will contain information such as the input and output file paths, the status, the message, the exception, etc. For example, if the operation is successful, the result might look like this:

Input: C:\Samples\Output\sample_forms.pdf
Output: C:\Samples\Output\sample_forms2.pdf
Status: Success
Message: Form editing operation completed successfully
Exception: null

If the operation fails, the result might look like this:

Input: C:\Samples\Output\sample_forms.pdf
Output: C:\Samples\Output\sample_forms2.pdf
Status: Failure
Message: An error occurred while editing the form fields
Exception: System.IO.FileNotFoundException: Could not find file 'C:\Samples\Output\sample_forms.pdf'
