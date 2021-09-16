---
title: Aspose.PDF for Java 21.5 Release Notes
type: docs
weight: 100
url: /java/aspose-pdf-for-java-21-5-release-notes/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

This page contains release notes information for Aspose.PDF for Java 21.5.

{{% /alert %}}
## **Improvements and Changes**

|**Key**|**Summary**|**Category**|
| :- | :- | :- |
|PDFJAVA-40474|Add API for merging images|New Feature|
|PDFJAVA-40491|XFA: Add 3of9 barcode support for XFA to standard forms conversion|Enhancement|
|PDFJAVA-39657|FontNotFoundException: Font Times New Roman was not found, but only sometimes|Enhancement|
|PDFJAVA-40490|How to extract font full name from it description/resource at PDF?|Enhancement|
|PDFJAVA-40394|Culture Name: en-cn is not a supported culture|Enhancement|
|PDFJAVA-39504|PDF to PDF/A - Link are lost in output PDF|Bug|
|PDFJAVA-39982|Create TOC to jump to specific heading instead of complete page|Bug|
|PDFJAVA-39127|PDF file not properly converted to DOCX|Bug|
|PDFJAVA-40408|Binarize a color pdf page to a b&w image|Bug|
|PDFJAVA-40406|PDF to TIFF results in blank output pages|Bug|
|PDFJAVA-34809|PDF to DOCX - Missing text/Strange text placement in resultant file|Bug|
|PDFJAVA-35584|Unable to extracting complete table contents from PDF|Bug|



## **Public API and Backwards Incompatible Changes**



**Added new methods** 
- com.aspose.pdf.**Artifact**.getLines()
- com.aspose.pdf.**Artifact**.getTextState()
- com.aspose.pdf.**Artifact**.setTextState(TextState)
- com.aspose.pdf.devices.**PngDevice**.processToBufferedImageBinarized(Page,double)
- com.aspose.pdf.**Font**.getBaseFont()
- com.aspose.pdf.**FontRepository**.addSystemFont(Font)
- com.aspose.pdf.**XImage**.getMetadata()

Changed method's parameter:
- com.aspose.pdf.facades.**PdfConverter**.mergeImages(java.util.List&lt;java.io.InputStream&gt;,**ImageFormat**,int,Integer,Integer) -> mergeImages(java.util.List&lt;java.io.InputStream&gt;,**int**,int,Integer,Integer)

Renamed methods:
- com.aspose.pdf.optimization.**ImageCompressionOptions**.getCompressImages() -> isCompressImages()
- com.aspose.pdf.**Stamp**.getBackground() -> isBackground()

Added new class:
- com.aspose.pdf.**ImageFormat**


