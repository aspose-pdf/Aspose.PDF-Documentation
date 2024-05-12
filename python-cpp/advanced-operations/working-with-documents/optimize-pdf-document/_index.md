---
title: Optimize PDF using Python via C++
linktitle: Optimize PDF
type: docs
weight: 30
url: /python-cpp/optimize-pdf/
keywords: "optimize pdf python"
description: Optimize PDF file with Python via C++ application.
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Optimize PDF Document

1. Load the PDF document using the AsposePDFPythonWrappers library
1. Optimize the PDF document to reduce its size using [document_optimize](https://reference.aspose.com/pdf/python-cpp/core/document_optimize/) function
1. Save the optimized document to the specified output file path with [document_save](https://reference.aspose.com/pdf/python-cpp/core/document_save/) function

This example loads a PDF file, optimizes it, and saves the optimized version to a specified output file:

```python 

    import AsposePDFPythonWrappers as apw
    import AsposePDFPython as apCore
    import os
    import os.path

    # Define the directory path where the PDF files are located
    dataDir = os.path.join(os.getcwd(), "samples")

    # Define the input file path
    input_file = os.path.join(dataDir, "sample0.pdf")

    # Define the output file path
    output_file = os.path.join(dataDir, "results", "optimized-document.pdf")

    # Load the PDF document using the AsposePDFPythonWrappers library
    document = apw.Document(input_file)

    # Optimize the PDF document to reduce its size
    document.optimize()

    # Save the optimized document to the specified output file path
    document.Save(output_file)
```


