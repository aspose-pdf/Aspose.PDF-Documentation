---
title: Convertir un document PDF en classeur Excel en Python
type: docs
weight: 20
url: /fr/java/convert-pdf-to-excel-workbook-in-python/
lastmod: "2021-06-05"
---

Pour convertir un document PDF en classeur Excel en utilisant **Aspose.PDF Java pour Python**, il suffit d'invoquer le module **PdfToExcel**.

```python

doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# Instancier l'objet ExcelSave Option
excelsave=self.ExcelSaveOptions();

# Enregistrer la sortie au format XLS
doc.save(self.dataDir + "Converted_Excel.xls", excelsave);
print "Le document a été converti avec succès"
```

**Télécharger le code en cours d'exécution**

Téléchargez **Convertir PDF en classeur Excel (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToExcel/PdfToExcel.py)