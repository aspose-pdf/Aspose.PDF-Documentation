---
title: Merger
type: docs
weight: 100
url: /net/plugins/merger/
description: How to Merge Multiple PDF Files into One using Aspose.PDF Merger Plugin
lastmod: "2024-01-24"
---

In this article, we will show you how to use the [Merger plugin](https://products.aspose.org/pdf/net/merger/), which can merge multiple PDF files into one and save it as a new file.

## Prerequisites

You will need the following:

* Visual Studio 2019 or later
* Aspose.PDF for .NET 21.1 or later
* Three sample PDF files that you want to merge

You can download the Aspose.PDF for .NET library from the official website or install them using the NuGet Package Manager in Visual Studio.

## Steps

The basic steps to merge multiple PDF files into one using the Merger plugin are:

1. Create an object of the Merger class
2. Create an object of the MergeOptions class and add the input and output file paths
3. Run the Process method of the Merger object

Let's see how to implement these steps in C# code.

### Step 1: Create an object of the Merger class

The Merger class is the main class that provides the functionality of merging multiple PDF files into one. To use it, you need to create an instance of it using the default constructor:

```cs
// Create a new instance of Merger
var pdfMerger = new Merger();
```

### Step 2: Create an object of the MergeOptions class and add the input and output file paths

The MergeOptions class is a helper class that allows you to specify various options and parameters for the merging process, such as the page range, the order, the security, etc. To use this class, you need to create an instance of it using the default constructor and add the input and output file paths using the Inputs and AddOutput methods. The input and output file paths can be either strings or FileDataSource objects. For example, to merge three PDF files named sample1.pdf, sample2.pdf, and sample3.pdf in the C:\Samples folder and save the merged file as TestMerge.pdf in the same folder, you can use the following code:

```cs
// Specify the input and output file paths
string inputFilePath1 = Path.Combine(@"C:\Samples\", "sample1.pdf");
string inputFilePath2 = Path.Combine(@"C:\Samples\", "sample2.pdf");
string inputFilePath3 = Path.Combine(@"C:\Samples\", "sample3.pdf");
var outputFilePath = "TestMerge.pdf";

// Create an instance of the MergeOptions class
var mergeOptions = new MergeOptions();

// Add the input and output file paths to the options
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath1));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath2));
mergeOptions.Inputs.Add(new FileDataSource(inputFilePath3));
mergeOptions.AddOutput(new FileDataSource(outputFilePath));
```

### Step 3: Run the Process method of the Merger object

The final step is to run the Process method of the Merger object, passing the mergeOptions object as a parameter. This method will perform the merging process and save the merged file to the output file path. For example, to run the merging process and print a confirmation message, you can use the following code:

```cs
// Process the merging and save the merged file
pdfMerger.Process(mergeOptions);

// Print a confirmation message
Console.WriteLine("The PDF files have been merged successfully.");
```
