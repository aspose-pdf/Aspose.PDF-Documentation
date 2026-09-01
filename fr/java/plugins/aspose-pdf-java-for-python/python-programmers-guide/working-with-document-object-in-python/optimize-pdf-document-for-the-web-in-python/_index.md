---
title: Optimiser un document PDF pour le Web en Python
linktitle: Optimiser un document PDF pour le Web en Python
type: docs
weight: 60
url: /java/optimize-pdf-document-for-the-web-in-python/
description: Découvrez comment optimiser les fichiers PDF pour un chargement Web plus rapide en Python avec Aspose.PDF, améliorant ainsi l'expérience utilisateur et les performances.
lastmod: "2026-06-09"
---

Pour optimiser un document PDF pour le Web à l'aide de **Aspose.PDF Java pour Python**, invoquez simplement la méthode **optimize_web** de la classe **Optimize**.


```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Optimize for web
doc.optimize();

#Save output document
doc.save(self.dataDir + "Optimized_Web.pdf")

print "Optimized PDF for the Web, please check output file."
```


**Télécharger le code d'exécution**

Téléchargez** Optimiser le PDF pour le Web (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)
