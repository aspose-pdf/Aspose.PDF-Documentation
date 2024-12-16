---
title: Supprimer les métadonnées d'un PDF en Python
type: docs
weight: 70
url: /fr/python-java/remove-metadata-from-pdf-in-python/
---

<ins>Pour supprimer les métadonnées d'un document Pdf en utilisant **Aspose.PDF Java for Python**, il suffit d'invoquer la classe **RemoveMetadata**.

**Code Python**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

if (re.findall('/pdfaid:part/',doc.getMetadata())):
doc.getMetadata().removeItem("pdfaid:part")


if (re.findall('/dc:format/',doc.getMetadata())):
doc.getMetadata().removeItem("dc:format")


# enregistrer le document mis à jour avec les nouvelles informations
doc.save(self.dataDir + "Remove_Metadata.pdf")

print "Les métadonnées ont été supprimées avec succès, veuillez vérifier le fichier de sortie."
```

**Télécharger le code en cours d'exécution**

Téléchargez **Supprimer les métadonnées (Aspose.PDF)** depuis l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/RemoveMetadata/RemoveMetadata.py)