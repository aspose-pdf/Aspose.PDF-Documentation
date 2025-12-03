---
title: Converting an FDF to XML format
type: docs
weight: 10
url: /python-net/converting-an-fdf-to-xml-format/
description: This section explains how you can convert an FDF to XML format with FormDataConverter Class.
lastmod: "2025-11-05"
---

{{% alert color="primary" %}}

The [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades) namespace in [Aspose.PDF for Python via .NET](/pdf/python-net/) supports AcroForms very well. It also supports importing and exporting form data to different file formats like FDF, XFDF, and XML. However, sometimes developers might need to convert one format into another one. This article looks at the feature that converts FDF into XML.

{{% /alert %}}

## Implementation details

Convert form data from FDF format into XML using Aspose.PDF for Python via .NET. FDF (Forms Data Format) is a lightweight format for storing PDF form field values, while XML provides a more general and widely supported structure. By using the [FormDataConverter](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formdataconverter/) [convert_fdf_to_xml()](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/formdataconverter/#methods) method, developers can easily transform FDF data into XML for integration with other systems or applications.

FDF stands for Forms Data Format, and an FDF file contains the form values in a key/value pair. We also know that XML file contains the values as tags. Where, mostly the key is represented as the tag name and value is represented as the value within that tag. Now, [aspose.pdf.facades](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades) provides us the flexibility to convert an FDF file format into an XML format.

The following code snippet shows you how to convert an FDF file into an XML file:

```python

import os
import clr

# Add reference to Aspose.PDF (adjust path if needed)
clr.AddReference("Aspose.PDF")

from Aspose.Pdf.Facades import FormDataConverter
from System.IO import FileStream, FileMode

def convert_fdf_to_xml():
    # Path to documents directory
    data_dir = "/path/to/documents/"   # <- update this to your actual path

    # Open FDF file as input stream
    fdf_input_stream = FileStream(os.path.join(data_dir, "input.fdf"), FileMode.Open)

    # Create XML file as output stream
    xml_output_stream = FileStream(os.path.join(data_dir, "ConvertFdfToXML_out.xml"), FileMode.Create)

    # Convert FDF to XML
    FormDataConverter.ConvertFdfToXml(fdf_input_stream, xml_output_stream)

    # Dispose resources
    fdf_input_stream.Close()
    xml_output_stream.Close()

    print("FDF data successfully converted to XML.")
```
