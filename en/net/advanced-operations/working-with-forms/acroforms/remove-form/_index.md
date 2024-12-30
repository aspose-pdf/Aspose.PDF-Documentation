---
title: Delete Forms from PDF in C#
linktitle: Delete Forms
type: docs
weight: 70
url: /net/remove-form/
description: Remove Text based on subtype/form with Aspose.PDF for .NET library. Remove all forms from the PDF.
lastmod: "2024-09-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Delete Forms from PDF in C#",
    "alternativeHeadline": "Effortless Removal of Forms from PDFs in C#",
    "abstract": "Introducing the new functionality to delete forms from PDF documents in C# using the Aspose.PDF library. This feature streamlines the removal of specific form elements, such as subform, or even all forms from a PDF file, enhancing document management and customization capabilities for developers. Optimize your PDF editing processes with precise code snippets that ensure efficient text fragment removal and document saving",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "delete forms, remove text, PDF C#, Aspose.PDF for .NET library, TextFragmentAbsorber, remove all forms",
    "wordcount": "378",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/remove-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-form/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Remove Text based on subtype/form

The next code snippet creates a new Document object using an input variable that contains the path to the PDF file. The example accesses the forms presented on page 2 of the document and checks for forms with certain properties. If a form with the type "Typewriter" and subtype "Form" is found, it uses TextFragmentAbsorber to visit and remove all text fragments in this form.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void ClearTextInForm(string input, string output)
{
    // Load the document
    using (cument = new Aspose.Pdf.Document(input))
	{
		// Get the forms from the first page
		var forms = document.Pages[1].Resources.Forms;

		foreach (var form in forms)
		{
			// Check if the form is of type "Typewriter" and subtype "Form"
			if (form.IT == "Typewriter" && form.Subtype == "Form")
			{
				// Create a TextFragmentAbsorber to find text fragments
				var absorber = new Aspose.Pdf.Text.TextFragmentAbsorber();
				absorber.Visit(form);

				// Clear the text in each fragment
				foreach (var fragment in absorber.TextFragments)
				{
					fragment.Text = "";
				}
			}
		}

		// Save the modified document
		document.Save(output);
	}	
}
```

## Remove Forms with "Typewriter" and a Subtype of "Form" from PDF

This code snippet searches the forms on the first page of a PDF document for forms with an intent (IT) of "Typewriter" and a subtype (Subtype) of "Form." If both conditions are met, the form is deleted from the PDF. The modified document is then saved to the specified output file.

The Aspose.PDF library provides two ways to remove such forms from PDFs:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void DeleteSpecifiedForm(string input, string output)
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();
	
    // Load the document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
	{
		// Get the forms from the first page
		var forms = document.Pages[1].Resources.Forms;

		// Iterate through the forms and delete the ones with type "Typewriter" and subtype "Form"
		for (int i = forms.Count; i > 0; i--)
		{
			if (forms[i].IT == "Typewriter" && forms[i].Subtype == "Form")
			{
				forms.Delete(forms[i].Name);
			}
		}

		// Save the modified document
		document.Save(output);
	}
}
```

Method 2:

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void DeleteSpecifiedForm(string input, string output)
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load the document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
	{
		// Get the forms from the first page
		var forms = document.Pages[1].Resources.Forms;

		// Iterate through the forms and delete the ones with type "Typewriter" and subtype "Form"
		foreach (var form in forms)
		{
			if (form.IT == "Typewriter" && form.Subtype == "Form")
			{
				var name = forms.GetFormName(form);
				forms.Delete(name);
			}
		}

		// Save the modified document
		document.Save(output);
	}
}
```

## Remove all Forms from PDF

This code removes all form elements from the first page of a PDF document and then saves the modified document to the specified output path.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET

private static void RemoveAllForms(string input, string output)
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load the document
    using (var document = new Aspose.Pdf.Document(dataDir + "TextField.pdf"))
	{
		// Get the forms from the first page
		var forms = document.Pages[1].Resources.Forms;

		// Clear all forms
		forms.Clear();

		// Save the modified document
		document.Save(output);
	}
}
```