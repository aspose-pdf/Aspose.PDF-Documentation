---
title: Convert PDF file to other formats 
linktitle: Convert PDF to other formats 
type: docs
weight: 90
url: /php-java/convert-pdf-to-other-files/
lastmod: "2024-05-20"
description: This topic show you how to Aspose.PDF allows to convert PDF file to other file formats.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convert PDF to EPUB

{{% alert color="success" %}}
**Try to convert PDF to EPUB online**

Aspose.PDF for PHP presents you online free application ["PDF to EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to EPUB with Free App](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** (short for electronic publication) is a free and open e-book standard from the International Digital Publishing Forum (IDPF). Files have the extension .epub.EPUB is designed for reflowable content, meaning that an EPUB reader can optimize text for a particular display device. EPUB also supports fixed-layout content. The format is intended as a single format that publishers and conversion houses can use in-house, as well as for distribution and sale. It supersedes the Open eBook standard.

Aspose.PDF for PHP supports the feature to convert PDF documents to EPUB format. Aspose.PDF for PHP has a class named [EpubSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/EpubSaveOptions) which can be used as the second argument to the [Document.save(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-) method, to generate an EPUB file. Please try using the following code snippet to accomplish this requirement.

```php
// Create a new instance of the Document class and load the input PDF file
$document = new Document($inputFile);

// Create a new instance of the EpubSaveOptions class
$saveOption = new EpubSaveOptions();

// Save the document as EPUB format using the specified save options
$document->save($outputFile, $saveOption);
```

## Convert PDF to LaTeX/TeX

**Aspose.PDF for PHP** support converting PDF to LaTeX/TeX.
The LaTeX file format is a text file format with the special markup and used in TeX-based document preparation system for high-quality typesetting.

To convert PDF files to TeX, Aspose.PDF has the class [LaTeXSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaTeXSaveOptions) which provides the method `setOutDirectoryPath` for saving temporary images during the conversion process.

The following code snippet shows the process of converting PDF files into the TEX format with Java.

```php
// Create a new Document object and load the input PDF file
$document = new Document($inputFile);

// Create a new LaTeXSaveOptions object
$saveOption = new LaTeXSaveOptions();
$saveOption->setOutDirectoryPath ($pathToOutputDirectory)

// Save the document as LaTeX
$document->save($outputFile, $saveOption);
```

{{% alert color="success" %}}
**Try to convert PDF to LaTeX/TeX online**

Aspose.PDF for PHP presents you online free application ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to LaTeX/TeX with Free App](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Convert PDF to Text

**Aspose.PDF for PHP** support converting whole PDF document and single page to a Text file.

### Convert whole PDF document to Text file

You can convert PDF document to TXT file using Visit method of [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) class.

The following code snippet explains how to extract the texts from the all pages.

```php
// Load the PDF document
$document = new Document($inputFile);

// Create a TextAbsorber object to extract text from the document
$textAbsorber = new TextAbsorber();

// Extract the text from the document
$textAbsorber->visit($document);
$content = $textAbsorber->getText();

// Save the extracted text to the output file
file_put_contents($outputFile, $content);

// Get the file size of the output file
$fileSize = filesize($outputFile);
```

{{% alert color="success" %}}
**Try to convert Convert PDF to Text online**

Aspose.PDF for PHP presents you online free application ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to Text with Free App](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

### Convert PDF page to text file

You can convert PDF document to TXT file with Aspose.PDF for PHP. You should use Visit method of [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) class for resolve this task.

The following code snippet explains how to extract the texts from the particular pages.

```php
// Load the PDF document
$document = new Document($inputFile);

// Create a TextAbsorber object to extract text from the document
$textAbsorber = new TextAbsorber();

$array = array(1, 3, 4);

foreach ($array as $page) {
    $textAbsorber->visit($document->getPages()->get_Item($page));
    $content = $textAbsorber->getText();
    
    $outputFile = $dataDir . DIRECTORY_SEPARATOR . 'result-pdf-to-text'. $page . '.txt';
    // Save the extracted text to the output file
    file_put_contents($outputFile, $content);
}
```

## Convert PDF to XPS

**Aspose.PDF for PHP** gives a possibility to convert PDF files to <abbr title="XML Paper Specification">XPS</abbr> format. Let try to use the presented code snippet for converting PDF files to XPS format with Java.

{{% alert color="success" %}}
**Try to convert PDF to XPS online**

Aspose.PDF for PHP presents you online free application ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), where you may try to investigate the functionality and quality it works.

[![Aspose.PDF Convertion PDF to XPS with Free App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

The XPS file type is primarily associated with the XML Paper Specification by Microsoft Corporation. The XML Paper Specification (XPS), formerly codenamed Metro and subsuming the Next Generation Print Path (NGPP) marketing concept, is Microsoft's initiative to integrate document creation and viewing into the Windows operating system.

To convert PDF files to XPS, Aspose.PDF has the class [XpsSaveOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/XpsSaveOptions) class that is used as the second argument to the Document.save(..) constructor to generate the XPS file. The following code snippet shows the process of converting PDF files into XPS format.

```php
// Create a new Document object and load the input PDF file
$document = new Document($inputFile);

// Create a new XpsSaveOptions object
$saveOption = new XpsSaveOptions();

// Save the document as XPS using the specified save options
$document->save($outputFile, $saveOption);
```
