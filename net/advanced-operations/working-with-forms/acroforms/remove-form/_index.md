---
title: Delete Forms from PDF in C#
linktitle: Delete Forms
type: docs
weight: 70
url: /net/remove-form/
keywords: delete form from pdf c#
description: Remove Text based on subtype/form with Aspose.PDF for .NET library. Remove all forms from the PDF.
lastmod: "2024-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Remove Text based on subtype/form

The next code snippet creates a new Document object using an input variable that contains the path to the PDF file. The example accesses the forms presented on page 2 of the document and checks for forms with certain properties. If a form with the type "Typewriter" and subtype "Form" is found, it uses TextFragmentAbsorber to visit and remove all text fragments in this form. Finally, the modified document is saved in two different output ways.

```cs

    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    foreach (var form in forms)
    {
        if (form.IT == "Typewriter" && form.Subtype == "Form")
        {
            var absorber = new TextFragmentAbsorber();
            absorber.Visit(form);

            foreach (var fragment in absorber.TextFragments)
            {
                fragment.Text = "";
            }
        }
    }

    document.Save(output);
```

## Remove Forms with "Typewriter" and a Subtype of "Form" from PDF

This code snippet searches the forms on the first page of a PDF document for forms with an intent (IT) of "Typewriter" and a subtype (Subtype) of "Form." If both conditions are met, the form is deleted from the PDF. The modified document is then saved to the specified output file.

The Aspose.PDF library provides two ways to remove such forms from PDFs:

```cs

    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    for (int i = 1; i <= forms.Count; i++)
    {
        if (forms[i].IT == "Typewriter" && forms[i].Subtype == "Form")
        {
            forms.Delete(forms[i].Name);
        }
    }

    document.Save(output);
```

```cs

    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    foreach (var form in forms)
    {
        if (form.IT == "Typewriter" && form.Subtype == "Form")
        {
            var name = forms.GetFormName(form);
            forms.Delete(name);
        }
    }

    document.Save(output);
```

## Remove all Forms from PDF

This code removes all form elements from the first page of a PDF document and then saves the modified document to the specified output path.

```cs

    var document = new Document(input);
    var forms = document.Pages[1].Resources.Forms;

    forms.Clear();

    document.Save(output);
```