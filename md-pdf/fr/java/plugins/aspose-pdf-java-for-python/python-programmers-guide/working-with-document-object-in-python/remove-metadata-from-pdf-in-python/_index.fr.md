---
title: Supprimer les métadonnées d'un PDF en Python
type: docs
weight: 70
url: /java/remove-metadata-from-pdf-in-python/
lastmod: "2021-06-05"
---

Pour supprimer les métadonnées d'un document PDF en utilisant **Aspose.PDF Java pour Python**, il suffit d'invoquer la classe **RemoveMetadata**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# enregistrer le document mis à jour avec les nouvelles informations
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "Métadonnées supprimées avec succès, veuillez vérifier le fichier de sortie."

```

**Télécharger le code en cours d'exécution**

Téléchargez **Remove Metadata (Aspose.PDF)** depuis n'importe lequel des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)