---
title: Ajouter des calques au fichier PDF dans Ruby
linktitle: Ajouter des calques au fichier PDF dans Ruby
type: docs
weight: 20
url: /java/add-layers-to-pdf-file-in-ruby/
description: Découvrez comment ajouter des calques à un fichier PDF dans Ruby à l'aide d'Aspose.PDF pour une meilleure structure du document et un meilleur contrôle de la visibilité.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - Ajouter des calques



<ins> Pour ajouter des calques dans un document PDF à l'aide de **Aspose.PDF Java pour Ruby**, invoquez simplement le module **AddLayers**.

Code Rubis


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

doc = Rjb::import('com.aspose.pdf.Document').new

page = doc.getPages().add()

operator = Rjb::import('com.aspose.pdf.Operator')

layer = Rjb::import('com.aspose.pdf.Layer').new("oc1", "Red Line")

layer.getContents().add(operator.SetRGBColorStroke(1, 0, 0))

layer.getContents().add(operator.MoveTo(500, 700))

layer.getContents().add(operator.LineTo(400, 700))

layer.getContents().add(operator.Stroke())

page.setLayers(Rjb::import('java.util.ArrayList').new)

page.getLayers().add(layer)

layer = Rjb::import('com.aspose.pdf.Layer').new("oc2", "Green Line")

layer.getContents().add(operator.SetRGBColorStroke(0, 1, 0))

layer.getContents().add(operator.MoveTo(500, 750))

layer.getContents().add(operator.LineTo(400, 750))

layer.getContents().add(operator.Stroke())

page.getLayers().add(layer)

layer = Rjb::import('com.aspose.pdf.Layer').new("oc3", "Blue Line")

layer.getContents().add(operator.SetRGBColorStroke(0, 0, 1))

layer.getContents().add(operator.MoveTo(500, 800))

layer.getContents().add(operator.LineTo(400, 800))

layer.getContents().add(operator.Stroke())

page.getLayers().add(layer)

# Save PDF Document

doc.save(data_dir + "Layers-Added.pdf")

puts "Added Layers Successfully, please check the output file."
```

## 
Télécharger le code d'exécution



Téléchargez** Ajouter des couches (Aspose.PDF)** à partir de l'un des sites de codage social mentionnés ci-dessous :


- 
[GitHub] (https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addlayers.rb)
