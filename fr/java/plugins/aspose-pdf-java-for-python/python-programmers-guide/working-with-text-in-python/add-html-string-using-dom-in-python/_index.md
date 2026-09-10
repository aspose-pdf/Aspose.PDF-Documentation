---
title: Ajouter une chaîne HTML à l'aide de DOM en Python
linktitle: Ajouter une chaîne HTML à l'aide de DOM en Python
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-python/
lastmod: "2026-06-09"
description: Explique comment ajouter une chaîne HTML dans DOM à l'aide de Python avec la bibliothèque de formats de fichier PDF
---
## 
Ajouter une chaîne HTML dans PDF DOM à l'aide de Python



Pour ajouter une chaîne HTML dans un document PDF à l'aide de **Aspose.PDF Java pour Python**, invoquez simplement le module **AddHtml**.

```python

# Instantiate Document object
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# Set margin information
title.setMargin(margin)

# Add HTML Fragment to paragraphs collection of page
page.getParagraphs().add(title)

# Save PDF file
doc.save(self.dataDir + 'html.output.pdf')

print "HTML added successfully"
```

**Télécharger le code d'exécution**



Téléchargez** Ajouter du HTML (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)
