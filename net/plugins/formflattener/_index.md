---
title: Using Aspose.PDF FormExporter plugin (.NET version)
type: docs
weight: 50
url: /net/plugins/formflattener/
description: How to Flatten Form Fields in PDF Files using Aspose.PDF FormFlattener Plugin
lastmod: "2024-01-24"
draft: false
---


Aspose.PDF is a powerful and versatile library that allows you to work with PDF documents in various ways. One of the features of Aspose.PDF is the ability to use plugins that extend its functionality and provide additional capabilities. In this article, we will show you how to use the FormFlattener plugin, which can flatten form fields in PDF files.

Prerequisites
To follow this tutorial, you will need the following:

•  Visual Studio 2019 or later

•  Aspose.PDF for .NET 21.1 or later

•  Aspose.PDF.Plugins for .NET 21.1 or later

•  A sample PDF file that contains some form fields

You can download the Aspose.PDF and Aspose.PDF.Plugins libraries from the official website or install them using the NuGet Package Manager in Visual Studio.

Steps
The basic steps to flatten form fields in PDF files using the FormFlattener plugin are:

1. 
Create an object of the FormFlattener class
2. 
Create an object of the FormFlattenAllFieldsOptions or FormFlattenSelectedFieldsOptions class, depending on whether you want to flatten all or some fields
3. 
Add the input and output data sources to the options object
4. 
Run the Process method of the FormFlattener object

Let's see how to implement these steps in C# code.

Step 1: Create an object of the FormFlattener class
The FormFlattener class is the main class that provides the functionality of flattening form fields in PDF files. To use it, you need to create an instance of it using the default constructor:

// Create an instance of the FormFlattener plugin
var plugin = new FormFlattener();

Step 2: Create an object of the FormFlattenAllFieldsOptions or FormFlattenSelectedFieldsOptions class, depending on whether you want to flatten all or some fields
The FormFlattenAllFieldsOptions and FormFlattenSelectedFieldsOptions classes are helper classes that allow you to specify various options and parameters for the flattening process. The FormFlattenAllFieldsOptions class flattens all the form fields in the PDF file, while the FormFlattenSelectedFieldsOptions class flattens only the form fields that match a given predicate. To use these classes, you need to create an instance of the appropriate class using the default constructor or passing a predicate as a parameter. For example, to flatten all the form fields in the PDF file, you can use the following code:

// Create options for flattening all fields
var options = new FormFlattenAllFieldsOptions();

To flatten only the form fields whose lower-left x-coordinate is greater than 300, you can use the following code:

// Create options for flattening selected fields
var options = new FormFlattenSelectedFieldsOptions((field) => field.Rect.LLX > 300);

Step 3: Add the input and output data sources to the options object
The input and output data sources are the PDF files that you want to flatten and save. They can be either file paths or streams. To add them to the options object, you need to use the Inputs and Outputs properties of the options class. These properties are collections of data sources that you can add using the Add method. For example, to flatten a PDF file named sample.pdf in the current folder and save it as sample-flat.pdf in the same folder, you can use the following code:

// Add input and output data sources to the options
options.Inputs.Add(new FileDataSource("sample.pdf"));
options.Outputs.Add(new FileDataSource("sample-flat.pdf"));

Step 4: Run the Process method of the FormFlattener object
The final step is to run the Process method of the FormFlattener object, passing the options object as a parameter. This method will perform the flattening process and return a ResultContainer object, which contains the results of the process, such as the status, the messages, the output data sources, etc. You can access the results using the properties and methods of the ResultContainer class. For example, to get the first result from the result collection and print it to the console, you can use the following code:

// Process the options and get the result container
var resultContainer = plugin.Process(options);

// Get the first result from the result container
var result = resultContainer.ResultCollection[0];

// Print the result
Console.WriteLine(result);

The result will contain information such as the input and output file paths, the status, the message, the exception, etc. For example, if the flattening process is successful, the result might look like this:

Input: sample.pdf
Output: sample-flat.pdf
Status: Success
Message: Flattening process completed successfully
Exception: null

If the flattening process fails, the result might look like this:

Input: sample.pdf
Output: sample-flat.pdf
Status: Failure
Message: An error occurred while flattening the form fields
Exception: System.IO.FileNotFoundException: Could not find file 'sample.pdf'

Conclusion
In this article, we have shown you how to use the Aspose.PDF plugins to flatten form fields in PDF files. We have explained the basic steps and the code examples for each step. We have also shown you how to access the results of the process and handle any errors. You can use the FormFlattener plugin to flatten any form fields in any PDF file with ease and flexibility. You can also customize the flattening process using the various options and parameters available in the options classes.