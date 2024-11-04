---
title: Convertir un PDF au format SVG en Python
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-python/
lastmod: "2021-06-05"
---

Pour convertir un PDF au format SVG en utilisant **Aspose.PDF Java pour Python**, il suffit d'invoquer le module **PdfToSvg**.

```python

# Ouvrir le document cible
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# instancier un objet de SvgSaveOptions
save_options = self.SvgSaveOptions()

# ne pas compresser l'image SVG dans une archive Zip
save_options.CompressOutputToZipArchive = False;

# Enregistrer la sortie au format XLS
doc.save(self.dataDir + "Output1.svg", save_options)

print "Le document a été converti avec succès"
```

**Télécharger le Code Exécutant**

Téléchargez **Convertir un PDF au format SVG (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)