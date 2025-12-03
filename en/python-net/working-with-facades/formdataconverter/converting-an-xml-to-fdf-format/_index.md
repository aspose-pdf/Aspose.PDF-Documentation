---
title: Converting an XML to FDF format
type: docs
weight: 20
url: /python-net/converting-an-xml-to-fdf-format/
description: This section explains how you can convert an XML to FDF format with FormDataConverter.
lastmod: "2025-11-05"
---

{{% alert color="primary" %}}

The [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades) namespace in [Aspose.PDF for Python via .NET](/pdf/python-net/) supports AcroForms very well. It also supports importing and exporting form data to different file formats like FDF, XFDF, and XML. However, sometimes a developer need to convert one format to another. In this article, we’ll look into the feature which allows us to convert an FDF format into XML.

{{% /alert %}}

## Implementation details

FDF stands for Forms Data Format, and an FDF file contains the form values in a key/value pair. We also know that XML file contains the values as tags. Where, mostly the key is represented as the tag name and value is represented as the value within that tag. Now, [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades) provides the flexibility to convert an XML file format into FDF format.

Use the [FormDataConverter](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/FormDataConverter) class for this purpose. This class provides different methods for converting one data format into another. This article shows how to use one method, [convert_xml_to_fdf()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formdataconverter/#methods), which takes an FDF file as an input or source stream and saves it into XML format. The following code snippet shows how to convert an FDF file into an XML file.

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

from Aspose.Pdf.Facades import FormDataConverter
from System.IO import FileStream, FileMode, FileAccess

def convert_xml_to_fdf():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open XML file as input stream
    src = FileStream(os.path.join(data_dir, "log.xml"), FileMode.Open, FileAccess.Read)

    # Create FDF file as output stream
    dest = FileStream(os.path.join(data_dir, "XMLToPdf_out.fdf"), FileMode.Create, FileAccess.ReadWrite)

    # Convert XML to FDF
    FormDataConverter.ConvertXmlToFdf(src, dest)

    # Dispose resources
    src.Close()
    dest.Close()

    print("XML data successfully converted to FDF.")
```
