---
title: What's is the difference between FDF, XML, and XFDF formats
type: docs
weight: 30
url: /python-net/whats-the-difference-between-xml-fdf-and-xfdf/
description: This section difference between XML, FDF and XFDF forms with Aspose.PDF Facades using Form Class.
lastmod: "2025-11-05"
---

{{% alert color="primary" %}}

We mixed many different terms like FDF, XML and XFDF. All these terms are related to each other somehow. This article explores these concepts and their relationship to each other.

{{% /alert %}}

## Unraveling Forms

When working with PDF forms, you often need to import or export form field data. Aspose.PDF supports several formats for this purpose: XML, FDF, and XFDF. Each format has its own characteristics and use cases.

Aspose.PDF for Python via .NET is used to manipulate PDF documents standardized by Adobe. And PDF documents contain interactive forms called AcroForms. These interactive forms have a number of form fields, like combo, text box, and radio button. Adobe's interactive forms, and form fields, work in the same way as an HTML form and its form fields.

It is possible to store the values of form fields in a separate file: an FDF (Forms Data Format) file. This contains the values of the form fields in key/pair fashion. FDF files are still used for this purpose. But Adobe also provides an XML encoded type of FDF called XFDF. An XFDF file stores the values of the form fields in a hierarchical manner using XML tags.

With Aspose.PDF developers can not only export the values of PDF form fields to an FDF or XFDF file but also to an XML file. All these files use different syntax to save PDF form field values. The example below explains the differences.

### What is XML format?

Extensible Markup Language (XML) is a markup language and file format for storing, transmitting, and reconstructing data.

**Format:** Standard XML file containing form field names and values.

**Use case:** Easy to read and integrate with other applications that support XML.

**Aspose.PDF support:** You can import/export form data directly in XML format.

The following code snippet shows how to export to XML format:

```python

import os, clr
clr.AddReference("Aspose.PDF")
import Aspose.Pdf.Facades as pdf_facades
from System.IO import FileStream, FileMode

data_dir = "/path/to/docs/"

form = pdf_facades.Form()
form.BindPdf(os.path.join(data_dir, "input.pdf"))

xml_stream = FileStream(os.path.join(data_dir, "formdata.xml"), FileMode.Create)
form.ExportXml(xml_stream)

xml_stream.Close()
form.Dispose()
```

### FDF (Forms Data Format)

An FDF (Forms Data Format) file is a compact text file that stores only the data from a PDF form, not the entire PDF document itself.

**Format:** A lightweight file format designed specifically for PDF form data.

**Use case:** Stores only field values, not the entire PDF. Useful for exchanging data separately from the document.

**Aspose.PDF support:** You can import/export form data using FDF streams.

The following code snippet shows how to import from FDF:

```python

from System.IO import FileStream, FileMode

form = pdf_facades.Form()
form.BindPdf(os.path.join(data_dir, "input.pdf"))

fdf_stream = FileStream(os.path.join(data_dir, "student.fdf"), FileMode.Open)
form.ImportFdf(fdf_stream)

form.Save(os.path.join(data_dir, "filled_from_fdf.pdf"))

fdf_stream.Close()
form.Dispose()
```

### XFDF (XML Forms Data Format)

An XFDF (XML Forms Data Format) file is an XML-based file that stores and exchanges form data and annotations for PDF documents.

**Format:** XML‑based representation of FDF data.

**Use case:** More structured than FDF, easier to parse with XML tools.

**Aspose.PDF support:** You can import/export XFDF data just like XML or FDF.

The following code snippet shows how to export to XFDF:

```python

xfdf_stream = FileStream(os.path.join(data_dir, "formdata.xfdf"), FileMode.Create)
form = pdf_facades.Form()
form.BindPdf(os.path.join(data_dir, "input.pdf"))

form.ExportXfdf(xfdf_stream)
form.Save(os.path.join(data_dir, "exported_xfdf.pdf"))

xfdf_stream.Close()
form.Dispose()
```

### Comparison Table

|**Format**|**Based On**|**Stores**|**Best For**|
| :- | :- | :- | :- |
|XML|Standard XML|Field names + values|General data exchange|
|FDF|PDF spec|Field values only|Lightweight storage, fast exchange|
|XFDF|XML version of FDF|Field names + values|Structured, XML‑friendly integration|

- Use XML when you want broad compatibility with other systems.

- Use FDF when you need a compact format for form data only.

- Use XFDF when you prefer XML structure but still want PDF‑specific form data handling.

Aspose.PDF for Python via .NET makes it easy to import and export form data in all three formats, giving you flexibility depending on your workflow.