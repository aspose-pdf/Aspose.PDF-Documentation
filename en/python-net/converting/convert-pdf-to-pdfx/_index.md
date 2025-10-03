---
title: Convert PDF to PDF/x formats in Python
linktitle: Convert PDF to PDF/x formats
type: docs
weight: 120
url: /python-net/convert-pdf-to-pdf_x/
lastmod: "2025-09-27"
description: This topic shows you how to convert PDF to PDF/x formats using Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: How to convert PDF to PDF/x formats
Abstract: The article provides a comprehensive guide on converting PDF to PDF/A, PDF/E, and PDF/X formats using Aspose.PDF for Python.
---

**PDF to PDF/x format means the ability to convert PDF to additional formats, namely PDF/A, PDF/E and PDF/X.**

## Convert PDF to PDF/A

**Aspose.PDF for Python** allows you to convert a PDF file to a <abbr title="Portable Document Format / A">PDF/A</abbr> compliant PDF file. Before doing so, the file must be validated. This topic explains how.

{{% alert color="primary" %}}

Please note we follow Adobe Preflight for validating PDF/A conformance. All tools on the market have their own “representation” of PDF/A conformance. Please check this article on PDF/A validation tools for reference. We chose Adobe products for verifying how Aspose.PDF produces PDF files because Adobe is at the center of everything connected to PDF.

{{% /alert %}}

Convert the file using the Document class Convert method. Before converting the PDF to PDF/A compliant file, validate the PDF using the Validate method. The validation result is stored in an XML file and then this result is also passed to the Convert method. You can also specify the action for the elements which cannot be converted using the ConvertErrorAction enumeration.

{{% alert color="success" %}}
**Try to convert PDF to PDF/A online**

Aspose.PDF for Python presents you online free application ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to PDF/A with Free App](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

The 'document.validate()' method validates whether a PDF file conforms to the PDF/A-1B standard (an ISO-standardized version of PDF designed for long-term archiving). The validation results are saved in a log file.

1. Load the PDF document using 'ap.Document'.
1. Call the validate method with the target compliance level (ap.PdfFormat.PDF_A_1B).
1. The results of the validation are written into the specified log file.

```python

    path_infile = path.join(self.data_dir, infile)
    path_logfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.validate(path_logfile, ap.PdfFormat.PDF_A_1B)
```

### Convert PDF to PDF/A-1B

The following code snippet shows how to convert PDF files to PDF/A-1B format:

1. Load the PDF document using 'ap.Document'.
1. Call the convert method with the following parameters:
    - Log file path - stores the details of the conversion process and compliance checks.
    - Target format - 'ap.PdfFormat.PDF_A_1B' (archival standard).
    - Error action - 'ap.ConvertErrorAction.DELETE' — automatically removes elements that prevent compliance.
1. Save the converted PDF/A-compliant file to the output path.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.convert(
        self.data_dir + "pdf_pdfa.log",
        ap.PdfFormat.PDF_A_1B,
        ap.ConvertErrorAction.DELETE,
    )
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

### Convert PDF to PDF 2.0 and PDF/A-4

This example demonstrates how to convert a PDF document into newer standardized formats: PDF 2.0 and PDF/A-4.
Both conversions help ensure compliance with modern specifications and archival requirements.

1. Load the input document using ap.Document.
1. Perform the first conversion to PDF 2.0 by calling document.convert with:
    - Log file path for conversion details.
    - Target format - 'ap.PdfFormat.V_2_0'.
    - Error action - 'ap.ConvertErrorAction.DELETE' to remove non-compliant elements.
1. Perform a second conversion to PDF/A-4 using the same method, ensuring the file is also compliant with archival standards.
1. Save the resulting document in the specified output path.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    document.convert(path_logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)

    document.convert(path_logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

### Convert PDF to PDF/A-3A with Embedded Files

Next code snippet demonstrates how to embed external files into a PDF and then convert the PDF into PDF/A-3A format, which supports attachments and is suitable for long-term archival with embedded content.

1. Load the input PDF using 'ap.Document'.
1. Create a 'FileSpecification' object pointing to the file to embed (e.g., "aspose-logo.jpg") with a description.
1. Add the file specification to the PDF’s 'embedded_files' collection.
1. Convert the document to PDF/A-3A using 'document.convert', specifying:
    - Log file path.
    - Target format - 'ap.PdfFormat.PDF_A_3A'.
    - Error action - 'ap.ConvertErrorAction.DELETE' to remove non-compliant elements.
1. Save the converted PDF to the output path.
1. Print a confirmation message.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)

    fileSpecification = ap.FileSpecification(self.data_dir + "aspose-logo.jpg", "Large Image file")
    document.embedded_files.add(fileSpecification)
    document.convert(path_logfile, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

### Convert PDF to PDF/A-1B with Font Substitution

This function converts a PDF into PDF/A-1B format while handling missing fonts by substituting them with available ones. This ensures the converted PDF remains visually consistent and compliant with archival standards.

1. Load the PDF using 'ap.Document'.
1. Convert the PDF to PDF/A-1B using 'document.convert', specifying:
    - Log file path.
    - Target format - 'ap.PdfFormat.PDF_A_1B'.
    - Error action - 'ap.ConvertErrorAction.DELETE' to remove non-compliant elements.
1. Save the converted PDF to the output path.
1. Print a confirmation message.

```python

    from os import path
    import aspose.pdf as ap 

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    try:
        ap.text.FontRepository.find_font("AgencyFB")

    except ap.FontNotFoundException:
        font_substitution = ap.text.SimpleFontSubstitution("AgencyFB", "Arial")
        ap.text.FontRepository.Substitutions.append(font_substitution)

    document = ap.Document(path_infile)
    document.convert(path_logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

### Convert PDF to PDF/A-1B with Automatic Tagging

This function converts a PDF document into PDF/A-1B format while automatically tagging the content for accessibility and structural consistency. Automatic tagging improves document usability for screen readers and ensures proper semantic structure.

1. Load the PDF using 'ap.Document'.
1. Create 'PdfFormatConversionOptions' specifying:
    - Log file path.
    - Target format - 'ap.PdfFormat.PDF_A_1B'.
    - Error action - 'ap.ConvertErrorAction.DELETE' to remove non-compliant elements.
1. Configure 'AutoTaggingSettings':
    - Enable 'enable_auto_tagging = True'.
    - Set 'heading_recognition_strategy = AUTO' to automatically detect headings.
1. Assign the auto-tagging settings to the conversion options.
1. Convert the PDF using 'document.convert(options)'.
1. Save the converted PDF to the output path.
1. Print a confirmation message.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)

    auto_tagging_settings = ap.AutoTaggingSettings()
    auto_tagging_settings.enable_auto_tagging = True

    auto_tagging_settings.heading_recognition_strategy = ap.HeadingRecognitionStrategy.AUTO

    options.auto_tagging_settings = auto_tagging_settings
    document.convert(options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Convert PDF to PDF/E

This snippet validates whether a PDF document conforms to the PDF/E-1 standard, which is an ISO standard tailored for engineering and technical documents. The validation results are saved to a log file.

1. Load the PDF document using 'ap.Document'.
1. Call the validate method, specifying:
    - Log file path to store validation results.
    - Target format - 'ap.PdfFormat.PDF_E_1'.
1. The validation results are saved in the log file for review.

```python

    path_infile = path.join(self.data_dir, infile)
    path_logfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.validate(path_logfile, ap.PdfFormat.PDF_E_1)
```

Next example demonstrates how to convert a PDF into PDF/E-1 format, which is an ISO standard tailored for engineering and technical documentation. This format preserves precise layout, graphics, and metadata required for engineering workflows.

1. Load the source PDF using 'ap.Document'.
1. Create 'PdfFormatConversionOptions' specifying:
    - Log file path for tracking conversion issues.
    - Target format - 'ap.PdfFormat.PDF_E_1'.
    - Error action - 'ap.ConvertErrorAction.DELETE' to remove non-compliant elements.
1. Convert the PDF using 'document.convert(options)'.
1. Save the converted PDF to the specified output path.
1. Print a confirmation message.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE)

    document.convert(options)

    # Save PDF document
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Convert PDF to PDF/X

Next code snippet converts a PDF document into PDF/X-4 format, which is an ISO standard commonly used in the printing and publishing industry. PDF/X-4 ensures color accuracy, maintains transparency, and embeds ICC profiles for consistent output across devices.

1. Load the source PDF using 'ap.Document'.
1. Create 'PdfFormatConversionOptions' specifying:
    - Log file path.
    - Target format - 'ap.PdfFormat.PDF_X_4'.
    - Error action - 'ap.ConvertErrorAction.DELETE' to remove non-compliant elements.
1. Provide the **ICC profile file** for color management via 'icc_profile_file_name'.
1. Specify an **OutputIntent** with a condition identifier (e.g., "FOGRA39") for printing requirements.
1. Convert the PDF using 'document.convert()'.
1. Save the converted PDF to the specified output path.
1. Print a confirmation message.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE)

    # Provide the name of the external ICC profile file (optional)
    options.icc_profile_file_name = path.join(self.data_dir,"ISOcoated_v2_eci.icc")
    # Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.output_intent = ap.OutputIntent("FOGRA39")

    document.convert(options)

    # Save PDF document
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```