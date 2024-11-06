---
title: Optimiser un document PDF pour le Web en Python
type: docs
weight: 60
url: fr/java/optimize-pdf-document-for-the-web-in-python/
lastmod: "2021-06-05"
---

Pour optimiser un document PDF pour le web en utilisant **Aspose.PDF Java pour Python**, il suffit d'invoquer la méthode **optimize_web** de la classe **Optimize**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Optimiser pour le web
doc.optimize();

# Enregistrer le document de sortie
doc.save(self.dataDir + "Optimized_Web.pdf")

print "PDF optimisé pour le Web, veuillez vérifier le fichier de sortie."
```

**Télécharger le code en cours d'exécution**

Téléchargez **Optimize PDF for Web (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)