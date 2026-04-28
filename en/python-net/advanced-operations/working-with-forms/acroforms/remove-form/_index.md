---
title: Delete Forms from PDF in Python
linktitle: Delete Forms
type: docs
weight: 70
url: /python-net/remove-form/
description: Remove form objects from PDF pages by using Aspose.PDF for Python via .NET, including full cleanup and targeted deletion.
lastmod: "2026-04-28"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remove Forms from PDF with Aspose.PDF for Python via .NET
Abstract: This article presents two approaches for removing form elements from PDF documents by using Aspose.PDF for Python via .NET. The first method clears all form objects from a selected page, while the second method removes only matching Typewriter form resources. These examples help with form cleanup, template preparation, and document normalization workflows.
---

## Remove All Forms from a Page

This code removes all form objects from the page specified by `page_num` and saves the updated document.

1. Load the PDF document.
1. Access page resources.
1. Clear form objects.
1. Save the updated document.

```python
import aspose.pdf as ap

def remove_all_forms(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    forms.clear()
    document.save(output_file_name)
```

## Remove a Specific Form Type

Next example iterates through the form objects on a given PDF page, identifies typewriter form annotations, deletes them, and then saves the updated PDF using Aspose.PDF for Python via .NET.

1. Load the PDF document.
1. Access page forms.
1. Iterate over forms.
1. Check for typewriter forms.
1. Delete the matched form.
1. Save the updated document.

```python
import aspose.pdf as ap

def remove_specified_form(input_file_name, page_num, output_file_name):
    document = ap.Document(input_file_name)
    forms = document.pages[page_num].resources.forms
    for form in forms:
        if form.it == "Typewriter" and form.subtype == "Form":
            name = forms.get_form_name(form)
            forms.delete(name)
    document.save(output_file_name)
```

## Related Topics

- [Create AcroForm](/pdf/python-net/create-form/)
- [Fill AcroForm](/pdf/python-net/fill-form/)
- [Modifying AcroForm](/pdf/python-net/modifying-form/)
- [Posting Forms](/pdf/python-net/posting-form/)
