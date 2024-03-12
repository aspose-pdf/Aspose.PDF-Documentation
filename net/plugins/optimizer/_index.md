---
title: Using Aspose.PDF Optimizer plugin (.NET version)
type: docs
weight: 80
url: /net/plugins/merger/
description: How to Optimizing and Manipulating PDF Files with Aspose.PDF Optimizer
lastmod: "2024-01-24"
---

## Optimizing and Manipulating PDF Files with Aspose.PDF

In this chapter, we'll explore how to utilize the Aspose.PDF library to optimize, resize, and rotate PDF files in your C# applications. 
Let's dive in and learn how to perform these tasks step by step.

## Table of Contents

1. [Introduction](#introduction)
2. [Optimizing PDF Files](#optimizing-pdf-files)
3. [Resizing PDF Files](#resizing-pdf-files)
4. [Rotating PDF Pages](#rotating-pdf-pages)

## Introduction<a name="introduction"></a>

The Aspose.PDF library provides powerful functionalities for working with PDF documents in C# applications. With Aspose.PDF, you can optimize PDF files to reduce their size, resize pages to fit different dimensions, and rotate pages to adjust their orientation.

## 1. Optimizing PDF Files<a name="optimizing-pdf-files"></a>

Optimizing a PDF file involves reducing its size and improving performance. The `OptimizerDemo` class provides a method `RunOptimize()` to achieve this task. Here's how you can optimize a PDF file:

- Create a new file data source for the input PDF file.
- Create a new file data source for the optimized output PDF file.
- Create an instance of `OptimizeOptions`.
- Add the input and output data sources to the optimize options.
- Create an instance of `Optimizer` and process the optimization using the optimize options.

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

## 2. Resizing PDF Files<a name="resizing-pdf-files"></a>

Resizing a PDF file involves changing its page size. The `OptimizerDemo` class provides a method `RunResize()` to accomplish this task. Follow these steps to resize a PDF file:

- Create a new file data source for the input PDF file.
- Create a new file data source for the resized output PDF file.
- Create an instance of `ResizeOptions` and set the desired page size.
- Add the input and output data sources to the resize options.
- Create an instance of `Optimizer` and process the resizing using the resize options.

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

## 3. Rotating PDF Pages<a name="rotating-pdf-pages"></a>

Rotating PDF pages allows you to change the orientation of pages within a PDF document. The `OptimizerDemo` class provides a method `RunRotate()` to achieve this. Here's how you can rotate PDF pages:

- Create a new file data source for the input PDF file.
- Create a new file data source for the output PDF file.
- Create an instance of `RotateOptions` and set the rotation value.
- Add the input and output data sources to the rotation options.
- Create an instance of `Optimizer` and process the rotation using the rotation options.

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

You've learned how to optimize, resize, and rotate PDF files using the Aspose.PDF library in C#. Incorporate these techniques into your applications to efficiently manipulate PDF documents according to your requirements.
