---
title: Convertir un PDF au format SVG en Python
linktitle: Convertir un PDF au format SVG en Python
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-python/
description: Découvrez comment convertir des documents PDF au format SVG en Python à l'aide d'Aspose.PDF pour une sortie vectorielle évolutive.
lastmod: "2026-06-09"
---

Pour convertir un PDF au format SVG à l'aide de **Aspose.PDF Java pour Python**, invoquez simplement le module **PdfToSvg**.


```python

# Open the target document
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# instantiate an object of SvgSaveOptions
save_options = self.SvgSaveOptions()

# do not compress SVG image to Zip archive
save_options.CompressOutputToZipArchive = False;

# Save the output to XLS format
doc.save(self.dataDir + "Output1.svg", save_options)

print "Document has been converted successfully"
```


**Télécharger le code d'exécution**

Téléchargez** Convertir un PDF au format SVG (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)
