---
title: Aspose.PDF for Java 23.1 Release Notes
type: docs
weight: 140
url: /java/aspose-pdf-for-java-23-1-release-notes/
lastmod: "2023-01-26
---

{{% alert color="primary" %}}

This page contains release notes information for Aspose.PDF for Java 23.1.

{{% /alert %}}
## **Improvements and Changes**

|**Key**|**Summary**|**Category**|
| :- | :- | :- |
|PDFJAVA-42369|Add support to get the actual font name through the public API|New Feature|
|PDFJAVA-42451|Create PrinterMark annotation|New Feature|
|PDFJAVA-42309|PDF to Excel: Remove text under vector images|Bug|
|PDFJAVA-42423|PDF to DOCX: Extra borders|Bug|
|PDFJAVA-42157|PDF to DOCX: No space between table and paragraph below it|Bug|
|PDFJAVA-42346|PDF to DOCX: Page number should be in another section|Bug|
|PDFJAVA-42361|PDF to DOCX: Textlines are merged|Bug|
|PDFJAVA-42382|OutOfMemoryError while converting PDF to DOCX|Bug|
|PDFJAVA-42415|PDF to Excel: Border colors are incorrect|Bug|
|PDFJAVA-42343|Aspose.Words 22.11: Text artefacts with DOCX to PDf conversion|Bug|
|PDFJAVA-41958|Example shows compile time errors|Bug|
|PDFJAVA-41796|Two "Overview" nodes in Aspose.PDF for Java documentation|Bug|
|PDFJAVA-40734|Problem adding a visible but non selectable text watermark|Bug|
|PDFJAVA-38598|setDraw method renders incorrect stamp|Bug|
|PDFJAVA-41830|Concatenating a PDF results in mismatched bookmarks and links|Bug|
|PDFJAVA-42348|Method PdfFileEditor.resizeContentsWithNormalization fails with some PDF files|Bug|
|PDFJAVA-42340|PDF concatenate throws NullPointerException|Bug|

## **Public API and Backwards Incompatible Changes**


**Added new classes**

- com.aspose.pdf.**ColorBarAnnotation**
- com.aspose.pdf.**PrinterMarkAnnotation**

**Added new methods**

- com.aspose.pdf.**AnnotationSelector**.visit(ColorBarAnnotation)
- com.aspose.pdf.**Font**.getActualFontName()
- com.aspose.pdf.**WatermarkAnnotation**.changeAfterResize(Matrix)

**Added new fields**

- com.aspose.pdf.**AnnotationType**.ColorBar


