---
title: Ajouter des Couches au Fichier PDF en Ruby
type: docs
weight: 20
url: /java/add-layers-to-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - Ajouter des Couches

<ins> Pour ajouter des couches dans un document PDF en utilisant **Aspose.PDF Java pour Ruby**, il suffit d'invoquer le module **AddLayers**.

Code Ruby

```java
# Le chemin vers le répertoire des documents.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

doc = Rjb::import('com.aspose.pdf.Document').new

page = doc.getPages().add()

operator = Rjb::import('com.aspose.pdf.Operator')

layer = Rjb::import('com.aspose.pdf.Layer').new("oc1", "Ligne Rouge")

layer.getContents().add(operator.SetRGBColorStroke(1, 0, 0))

layer.getContents().add(operator.MoveTo(500, 700))

layer.getContents().add(operator.LineTo(400, 700))

layer.getContents().add(operator.Stroke())

page.setLayers(Rjb::import('java.util.ArrayList').new)

page.getLayers().add(layer)

layer = Rjb::import('com.aspose.pdf.Layer').new("oc2", "Ligne Verte")

layer.getContents().add(operator.SetRGBColorStroke(0, 1, 0))

layer.getContents().add(operator.MoveTo(500, 750))

layer.getContents().add(operator.LineTo(400, 750))

layer.getContents().add(operator.Stroke())

page.getLayers().add(layer)

layer = Rjb::import('com.aspose.pdf.Layer').new("oc3", "Ligne Bleue")

layer.getContents().add(operator.SetRGBColorStroke(0, 0, 1))

layer.getContents().add(operator.MoveTo(500, 800))

layer.getContents().add(operator.LineTo(400, 800))

layer.getContents().add(operator.Stroke())

page.getLayers().add(layer)

# Enregistrer le Document PDF

doc.save(data_dir + "Layers-Added.pdf")

puts "Couches ajoutées avec succès, veuillez vérifier le fichier de sortie."
```


## Télécharger le code en cours d'exécution

Téléchargez **Ajouter des couches (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addlayers.rb)