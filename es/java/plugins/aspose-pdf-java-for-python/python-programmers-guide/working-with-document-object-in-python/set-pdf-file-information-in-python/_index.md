---
title: Set PDF File Information in Python
linktitle: Set PDF File Information in Python
type: docs
weight: 90
url: /java/set-pdf-file-information-in-python/
description: Aprenda a configurar la información del archivo PDF, como el autor, el título y más, en Python usando Aspose.PDF para organizar documentos.
lastmod: "2026-06-09"
---
To update Pdf document information using **Aspose.PDF Java for Python**, simply invoke **SetPdfFileInfo** class.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Get document information
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF for java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("PDF Information");
doc_info.setTitle("Setting PDF Document Information");

# save update document with new information

doc.save(self.dataDir + "Updated_Information.pdf")
print "Update document information, please check output file."
```

**Download Running Code**

DownloadВ **Set PDF File Information (Aspose.PDF)**В fromВ any of the below mentioned social coding sites:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)
