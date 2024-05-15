---
title: Optimizer 
type: docs
weight: 80
url: /net/plugins/optimizer/
description: How to Optimizing and Manipulating PDF Files with Aspose.PDF Optimizer
lastmod: "2024-01-24"
---

In this chapter, we'll explore how to utilize the [Aspose.PDF Optimizer](https://products.aspose.org/pdf/net/optimizer/) to optimize, resize, and rotate PDF files in your C# applications.
Let's dive in and learn how to perform these tasks step by step.

## Prerequisites

You will need the following:

* Visual Studio 2019 or later
* Aspose.PDF for .NET 24.1 or later
* A sample PDF file that contains some form fields

## Optimizing PDF Files

Optimizing a PDF file involves reducing its size and improving performance. The following snippets show how to achieve this task. Here's how you can optimize a PDF file:

* Create a new file data source for the input PDF file.
* Create a new file data source for the optimized output PDF file.
* Create an instance of `OptimizeOptions`.
* Add the input and output data sources to the optimize options.
* Create an instance of `Optimizer` and process the optimization using the optimize options.

```cs
// Create a new file data source for the input PDF file.
var inputDataSource = new FileDataSource(inputPath);

// Create a new file data source for the optimized output PDF file.
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// Create a new instance of OptimizeOptions.
var options = new OptimizeOptions();

// Add the input and output data sources to the optimize options.
options.AddInput(inputDataSource);
options.AddOutput(outputDataSource);


// Create a new instance of Optimizer.
var optimizer = new Optimizer();

// Process the optimization using the optimize options.
optimizer.Process(options);
```

## Resizing PDF Files

Resizing a PDF file involves changing its page size. The following code shows how to accomplish this task. Follow these steps to resize a PDF file:

* Create a new file data source for the input PDF file.
* Create a new file data source for the resized output PDF file.
* Create an instance of `ResizeOptions` and set the desired page size.
* Add the input and output data sources to the resize options.
* Create an instance of `Optimizer` and process the resizing using the resize options.

```cs
// Create a new file data source for the input PDF file.
var inputDataSource = new FileDataSource("sample.pdf");

// Create a new file data source for the resized output PDF file.
var outputDataSource = new FileDataSource("sample_resized.pdf");

// Create a new instance of ResizeOptions and set the desired page size.
var opt = new ResizeOptions
{
    PageSize = PageSize.PageLetter
};

// Add the input and output data sources to the resize options.
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// Create a new instance of Optimizer.
var optimizer = new Optimizer();

// Process the resizing using the resize options.
optimizer.Process(opt);
```

## Rotating PDF Pages

Rotating PDF pages allows you to change the orientation of pages within a PDF document. Here's how you can rotate PDF pages:

* Create a new file data source for the input PDF file.
* Create a new file data source for the output PDF file.
* Create an instance of `RotateOptions` and set the rotation value.
* Add the input and output data sources to the rotation options.
* Create an instance of `Optimizer` and process the rotation using the rotation options.

```cs
// Create a new file data source for the input PDF file.
var inputDataSource = new FileDataSource(inputPath);

// Create a new file data source for the optimized output PDF file.
var outputDataSource = new FileDataSource("sample_optimized.pdf");

// Create a new instance of OptimizeOptions.
var opt = new RotateOptions();

// Add the input and output data sources to the optimize options.
opt.AddInput(inputDataSource);
opt.AddOutput(outputDataSource);

// Set rotation value
opt.Rotation = Rotation.on180;

// Create a new instance of Optimizer.
var optimizer = new Optimizer();

// Process the optimization using the optimize options.
optimizer.Process(opt)
```

## Conclusion

You've learned how to optimize, resize, and rotate PDF files using the Aspose.PDF Optimizer Plugin in C#. Incorporate these techniques into your applications to efficiently manipulate PDF documents according to your requirements.
