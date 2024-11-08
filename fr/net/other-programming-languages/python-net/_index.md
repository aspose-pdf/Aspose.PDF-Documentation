---
title: Utilisation de Aspose.PDF pour .NET avec Python
linktitle: Intégration avec Python
type: docs
weight: 100
url: /fr/net/python-net/
description: Dans ce tutoriel, vous explorerez les différentes manières de créer et de modifier des fichiers PDF en Python.
lastmod: "2022-01-10"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---

Cet article décrit de courts exemples de création de PDF en utilisant l'intégration de Aspose.PDF pour .NET avec Python.

## Prérequis

Pour utiliser Aspose.PDF pour .NET en Python, veuillez utiliser le `requirments.txt` suivant :

```bash
pip==21.3.1
pycparser==2.21
pythonnet==2.5.2
setuptools==60.1.0
```

Vous devriez également placer `Aspose.PDF.dll` dans le dossier souhaité.

## Création d'un PDF simple avec Python

Pour travailler, nous aurons besoin d'intégrer [PythonNet](https://github.com/pythonnet/pythonnet) à notre application et de faire quelques configurations.

```python
import clr

aspose_pdf = clr.AddReference("D:\\aspose-python-net\\Aspose.PDF.dll")

from System import TimeSpan

from Aspose.Pdf import Document, Color, License, BorderInfo, BorderSide, Rectangle, HorizontalAlignment
from Aspose.Pdf import Table, MarginInfo
from Aspose.Pdf.Text import TextFragment, Position, TextBuilder,FontRepository
```
### Générer un document simple

Créons un PDF simple avec le texte classique "Hello, world". Pour une explication plus détaillée, veuillez suivre [cette page](https://docs.aspose.com/pdf/net/hello-world-example/)

```python
class HelloWorld(object):
    def __init__(self,licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):

        # Initialiser l'objet document
        document = Document()
        # Ajouter une page
        page = document.Pages.Add()
        # Ajouter du texte à la nouvelle page
        textFragment = TextFragment("Hello,world!")
        textFragment.Position = Position(100, 600)

        textFragment.TextState.FontSize = 12
        textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman")
        textFragment.TextState.BackgroundColor = Color.Blue
        textFragment.TextState.ForegroundColor = Color.Yellow

        # Créer un objet TextBuilder
        textBuilder = TextBuilder(page)

        # Ajouter le fragment de texte à la page PDF
        textBuilder.AppendText(textFragment)

        document.Save("HelloWorld_out.pdf")
```
## Création de PDF complexes en utilisant Python

Les exemples suivants montrent comment nous pouvons créer un document PDF complexe avec des images et des tableaux. Cet exemple est basé sur la [page suivante](https://docs.aspose.com/pdf/net/complex-pdf-example/).

```python
class HelloWorld(object):
    def __init__(self,licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):
    # ... omis ...

    # Créer un document complexe
    def run_complex(self):

        # Initialiser l'objet document
        document = Document()
        # Ajouter une page
        page = document.Pages.Add()

        # Ajouter une image
        imageFileName = self.dataDir + "logo.png"
        page.AddImage(imageFileName, Rectangle(20, 730, 120, 830))

        # Ajouter un en-tête
        header = TextFragment("Nouvelles routes de ferry à l'automne 2020")
        header.TextState.Font = FontRepository.FindFont("Arial")
        header.TextState.FontSize = 24
        header.HorizontalAlignment = HorizontalAlignment.Center
        header.Position = Position(130, 720)
        page.Paragraphs.Add(header)

        # Ajouter une description
        descriptionText = "Les visiteurs doivent acheter leurs billets en ligne et les billets sont limités à 5 000 par jour. \
        Le service de ferry fonctionne à demi-capacité et selon un horaire réduit. Attendez-vous à des files d'attente."
        description = TextFragment(descriptionText)
        description.TextState.Font = FontRepository.FindFont("Times New Roman")
        description.TextState.FontSize = 14
        description.HorizontalAlignment = HorizontalAlignment.Left
        page.Paragraphs.Add(description)


        # Ajouter un tableau
        table = Table()

        table.ColumnWidths = "200"
        table.Border = BorderInfo(BorderSide.Box, 1.0, Color.DarkSlateGray)
        table.DefaultCellBorder = BorderInfo(BorderSide.Box, 0.5, Color.Black)
        table.DefaultCellPadding = MarginInfo(4.5, 4.5, 4.5, 4.5)
        table.Margin.Bottom = 10
        table.DefaultCellTextState.Font =  FontRepository.FindFont("Helvetica")

        headerRow = table.Rows.Add()
        headerRow.Cells.Add("Ville de départ")
        headerRow.Cells.Add("Île de départ")

        i=0
        while(i<headerRow.Cells.Count):
            headerRow.Cells[i].BackgroundColor = Color.Gray
            headerRow.Cells[i].DefaultCellTextState.ForegroundColor = Color.WhiteSmoke
            i+=1

        time = TimeSpan(6, 0, 0)
        incTime = TimeSpan(0, 30, 0)

        i=0
        while (i<10):
            dataRow = table.Rows.Add()
            dataRow.Cells.Add(time.ToString("hh\:mm"))
            time=time.Add(incTime)
            dataRow.Cells.Add(time.ToString("hh\:mm"))
            i+=1

        page.Paragraphs.Add(table)

        document.Save(self.dataDir + "Complex.pdf")
```
## Comment générer des PDFs sous Windows

Ce snippet montre comment exécuter les exemples ci-dessus sur un PC Windows. Nous supposons que `class HelloWorld` se trouve dans le fichier `example_get_started.py`.
Si vous exécutez la version d'essai de Aspose.PDF pour .NET, vous devriez passer une chaîne vide comme `license_path`.

```python
import example_get_started

def main():

    example = example_get_started.HelloWorld("<license_path>")
    example.run_simple()
    example.run_complex()


if __name__ == '__main__':
    main()
```
