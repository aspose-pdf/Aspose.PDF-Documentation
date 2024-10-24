---
title: Working with Forms using Python
linktitle: Forms in PDF document
type: docs
weight: 60
url: /python-java/forms/
lastmod: "2023-05-19"
description: This section contains articles relating to work with forms in PDF documents using Python API.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Forms are files with areas for users to select or fill out information for the purpose of collecting and storing information.

AcroForms are PDF files that contain form fields. Data can be entered into these fields (manually or through an automated process) by the end-users or the author of the form. Internally AcroForms are annotations or fields applied to a PDF document.

In this section describes a quick and simple approach to programmatically completing a PDF document through the use of the Aspose.PDF. The section also discusses how one might go about using the Aspose.PDF for Java to discover and map the fields available within an existing PDF with AcroForms.


**Our Aspose.PDF for Python via Java** library allows you to successfully, quickly and easily cork with forms in PDF documents.

- **AcroForms** - create form, fill form field, extract data from form, modifing fields in your PDF with Java library.
- **XFA Forms** - fill XFA fields, convert XFA, get XFA fields properties.

## The following functions are available:

- export/import fdf
- export/import xfdf
- export/import xml
- export/set XfaData
- fill fields
- flatten fields
- determining valid radio button values
- get field names, flags, types, values
- rename fields

```python

from asposepdf import Api, Forms


# init license
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

DIR_INPUT = baseDir+"testdata/forms/"
DIR_OUTPUT = baseDir+"testout/"

# fill field example

input_pdf1 = DIR_INPUT + "Testing.pdf"
output_pdf = DIR_OUTPUT + "test5_1.pdf"

form = Forms.Form(sourceFileName=input_pdf1)
print(form.getFieldType("form1[0].Page1[0].fldBarCode1[0]"))
form.fillField("form1[0].Page1[0].fldBarCode1[0]", "54321")

form.save(output_pdf)
```
