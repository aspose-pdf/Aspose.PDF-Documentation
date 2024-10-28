---
title: Définir l'expiration du PDF en Python
type: docs
weight: 80
url: /java/set-pdf-expiration-in-python/
lastmod: "2021-06-05"
---

Pour définir l'expiration d'un document Pdf en utilisant **Aspose.PDF Java pour Python**, il suffit d'invoquer la classe **SetExpiration**.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2021; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('Le fichier est expiré. Vous avez besoin d'un nouveau.');");

doc.setOpenAction(javascript);

# enregistrer le document mis à jour avec de nouvelles informations
doc.save(self.dataDir + "set_expiration.pdf");

print "Informations du document mises à jour, veuillez vérifier le fichier de sortie."
```

**Télécharger le code en cours d'exécution**

Téléchargez **Définir l'expiration du PDF (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)