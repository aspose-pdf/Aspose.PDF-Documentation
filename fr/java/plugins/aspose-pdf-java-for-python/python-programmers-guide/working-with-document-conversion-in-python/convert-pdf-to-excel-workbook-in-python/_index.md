---
title: Convertir un PDF en classeur Excel en Python
linktitle: Convertir un PDF en classeur Excel en Python
type: docs
weight: 20
url: /java/convert-pdf-to-excel-workbook-in-python/
description: Découvrez comment convertir des documents PDF en classeurs Excel en Python à l'aide d'Aspose.PDF pour l'extraction de données structurées.
lastmod: "2026-06-09"
---

Pour convertir un document PDF en classeur Excel à l'aide de **Aspose.PDF Java pour Python**, invoquez simplement le module **PdfToExcel**.


```python

doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# Instantiate ExcelSave Option object
excelsave=self.ExcelSaveOptions();

# Save the output to XLS format
doc.save(self.dataDir + "Converted_Excel.xls", excelsave);
print "Document has been converted successfully"
```


**Télécharger le code d'exécution**

Téléchargez** Convertir un PDF en classeur Excel (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)
