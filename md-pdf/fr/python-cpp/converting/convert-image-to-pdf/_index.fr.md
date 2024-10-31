---
title: Convertir une Image en PDF en Python
linktitle: Convertir une Image en fichier PDF
type: docs
weight: 10
url: /python-cpp/convert-image-to-pdf/
lastmod: "2024-04-22"
description: Ce sujet vous montre comment convertir une image en PDF en utilisant la bibliothèque Aspose.PDF pour Python via C++.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

Notre bibliothèque démontre des extraits de code pour convertir les formats d'image les plus populaires - JPEG. Vous pouvez très facilement convertir une image JPG en PDF avec Aspose.PDF pour Python via C++ en suivant ces étapes :

## Convertir une Image en PDF

Vous pouvez très facilement convertir une image JPG en PDF avec Aspose.PDF pour C++ en suivant ces étapes :

1. Ouvrir le fichier image d'entrée en utilisant la bibliothèque PIL
1. Obtenir la largeur et la hauteur de l'image
1. Créer une nouvelle instance de Document en utilisant la bibliothèque AsposePDFPythonWrappers
1. Définir la hauteur et la largeur fixes de l'image
1. Ajouter une nouvelle page au document
1. Ajouter l'image à la page
1. Enregistrer le PDF de sortie avec la méthode 'document.save'.

L'extrait de code ci-dessous montre comment convertir une image JPG en PDF en utilisant Python via C++ :

```python
import AsposePDFPythonWrappers as apw
import os
import os.path
from PIL import Image

# Définir le chemin du répertoire pour les fichiers de données
dataDir = os.path.join(os.getcwd(), "samples")

# Définir le chemin du fichier d'entrée
input_file = os.path.join(dataDir, "sample.jpg")

# Définir le chemin du fichier de sortie
output_file = os.path.join(dataDir, "results", "jpg-to-pdf.pdf")

# Ouvrir le fichier image d'entrée en utilisant la bibliothèque PIL
pil_img = Image.open(input_file)

# Obtenir la largeur et la hauteur de l'image
width, height = pil_img.size

# Créer une nouvelle instance de Document en utilisant la bibliothèque AsposePDFPythonWrappers
document = apw.Document()

# Créer une nouvelle instance d'Image en utilisant la bibliothèque AsposePDFPythonWrappers
image = apw.Image()

# Définir le chemin du fichier de l'image
image.file = input_file

# Définir la hauteur et la largeur fixes de l'image
image.fix_height = height
image.fix_width = width

# Ajouter une nouvelle page au document
page = document.pages.add()

# Ajouter l'image à la page
page.paragraphs.add(image)

# Enregistrer le document dans le chemin du fichier de sortie
document.save(output_file)
```