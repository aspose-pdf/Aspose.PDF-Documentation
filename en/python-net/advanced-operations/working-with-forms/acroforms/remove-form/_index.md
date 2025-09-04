---
title: Delete Forms from PDF in Python
linktitle: Delete Forms
type: docs
weight: 70
url: /python-net/remove-form/
description: Remove Text based on subtype/form with Aspose.PDF for Python via .NET library. Remove all forms from the PDF.
lastmod: "2025-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove Forms from PDF with Aspose.PDF for Python via .NET
Abstract: This document presents two Python-based approaches for removing form elements from PDF files using Aspose.PDF for Python via .NET. The first method demonstrates how to clear all form objects from a specific page by accessing its resource dictionary and invoking the clear() method on the forms collection. The second method provides a more targeted solution by iterating through form annotations, identifying typewriter-style forms, and selectively deleting them based on their attributes. Both techniques conclude with saving the updated PDF to a specified output path, offering flexible options for form cleanup and document refinement in automated workflows.
---

## Remove all Forms from PDF

This code removes all form elements from the first page of a PDF document and then saves the modified document to the specified output path.

1. Load the PDF document.
1. Access page resources.
1. Clear form objects.
1. Save the updated document.

```python

    import aspose.pdf as ap
    import os

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(data_dir, infile)
    path_outfile = os.path.join(data_dir, outfile)

    document = ap.Document(path_infile)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(path_outfile)
```

## Remove Specified Form

Next example iterates through the form objects on a given PDF page, identifies typewriter form annotations, deletes them, and then saves the updated PDF using Aspose.PDF for Python via .NET.

1. Load the PDF document.
1. Access page forms.
1. Iterate over forms.
1. Check for typewriter forms.
1. Delete the matched form.
1. Save the updated document.

```python

    import aspose.pdf as ap
    import os

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if (form.it == "Typewriter" and form.subtype == "Form"):
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(path_outfile)
```