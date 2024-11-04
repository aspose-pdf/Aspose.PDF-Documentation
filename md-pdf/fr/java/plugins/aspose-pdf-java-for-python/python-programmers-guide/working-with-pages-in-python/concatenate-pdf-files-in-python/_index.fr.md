---
title: Concaténer des fichiers PDF en Python
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-python/
lastmod: "2021-06-05"
---

Pour concaténer des fichiers PDF en utilisant **Aspose.PDF Java pour Python**, il suffit d'invoquer la classe **ConcatenatePdfFiles**.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Ouvrir le document source
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# Ajouter les pages du document source au document cible
pdf1.getPages().add(pdf1.getPages())

# Enregistrer le fichier de sortie concaténé (le document cible)
doc.save(self.dataDir + "Concatenate_output.pdf")

print "Le nouveau document a été enregistré, veuillez vérifier le fichier de sortie"
```

**Télécharger le code en cours d'exécution**

Téléchargez **Concaténer des fichiers PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)