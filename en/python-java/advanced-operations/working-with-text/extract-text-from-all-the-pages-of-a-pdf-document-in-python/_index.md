---
title: Extract Text From All the Pages of a PDF Document in Python
type: docs
weight: 30
url: /python-java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
description: Discover how to extract text from every page of a PDF document using Python and Aspose.PDF for data extraction and analysis.
---

To extract TextrFrom All the Pages Pdf document using **Aspose.PDF Java for Python**, simply invoke **ExtractTextFromAllPages** module.

```python
# Open the target document
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "Text extracted successfully. Check output file."

```

**Download Running Code**

Download **Extract Text From All the Pages (Aspose.PDF)** from any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)
