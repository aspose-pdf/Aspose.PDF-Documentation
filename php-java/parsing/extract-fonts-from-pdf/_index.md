---
title: Extract fonts from PDF 
linktitle: Extract fonts
type: docs
weight: 30
url: /php-java/extract-fonts-from-pdf/
description: How to extract font from PDF using Aspose.PDF for PHP
lastmod: "2024-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

In case you want to get all fonts from a PDF document, you can use [Document.IDocumentFontUtilities.getAllFonts()](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#getFontUtilities--) method provided in Document class.
Please check following code snippet in order to get all fonts from an existing PDF document:

```php

    // Create a new instance of the License class and set the license file.
    $licenceObject = new License();
    $licenceObject->setLicense($license);

    // Set the path to the directory containing the PDF document and the output directory for the extracted fonts.
    $dataDir = getcwd() . DIRECTORY_SEPARATOR . "samples";
    $inputFile = $dataDir . DIRECTORY_SEPARATOR . "sample.pdf";

    // Initialize the response data variable.
    $responseData = "";

    try {
        // Load the PDF document.
        $document = new Document($inputFile);

        // Get all the fonts used in the PDF document.
        $fonts = java_values($document->getFontUtilities()->getAllFonts());

        // Iterate over each font and save it as a TrueType font file.
        foreach ($fonts as $font) {
            // Set the output file path for the font file.
            $outputFile = $dataDir . DIRECTORY_SEPARATOR . "results" . DIRECTORY_SEPARATOR . $font->getFontName() . ".ttf";

            // Create a FileOutputStream object to write the font file.
            $fontStream = new java("java.io.FileOutputStream", $outputFile);

            // Save the font as a TrueType font file.
            $font->save($fontStream);

            // Close the font stream.
            $fontStream->close();

            // Append the font name to the response data.
            $responseData = $responseData . $font->getFontName() . ", ";
        }

        // Close the PDF document.
        $document->close();
    }
```
