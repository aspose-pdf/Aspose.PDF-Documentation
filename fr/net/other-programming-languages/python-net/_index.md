---
title: Utiliser Aspose.PDF for .NET avec Python
linktitle: Intégration avec Python
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 100
url: /fr/net/python-net/
description: Dans ce tutoriel, vous explorerez les différentes manières de créer et de modifier des fichiers PDF en Python.
lastmod: "2022-01-10"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Using Aspose.PDF for .NET with Python",
    "alternativeHeadline": "Integrate Aspose.PDF for .NET with Python Effortlessly",
    "abstract": "Découvrez l'intégration puissante de Aspose.PDF for .NET avec Python, permettant aux utilisateurs de créer et de modifier des documents PDF en toute simplicité. Cette fonctionnalité offre des exemples simples pour générer des PDF simples et complexes, mettant en avant des fonctionnalités telles que l'ajout de texte, d'images et de tableaux, tout en tirant parti des capacités robustes de la bibliothèque .NET dans un environnement Python. Débloquez de nouvelles possibilités pour la manipulation et la génération de PDF de manière efficace avec cette intégration innovante.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "681",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/python-net/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/python-net/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF peut effectuer non seulement des tâches simples et faciles, mais aussi faire face à des objectifs plus complexes. Consultez la section suivante pour les utilisateurs et développeurs avancés."
}
</script>

Cet article décrit de courts exemples sur la façon de créer un PDF en utilisant l'intégration Aspose.PDF for .NET avec Python.

## Prérequis

Pour utiliser Aspose.PDF for .NET en Python, veuillez utiliser le fichier `requirments.txt` suivant :

```bash
pip==21.3.1
pycparser==2.21
pythonnet==2.5.2
setuptools==60.1.0
```

De plus, vous devez placer `Aspose.PDF.dll` dans le dossier souhaité.

## Création d'un PDF simple avec Python

Pour travailler, nous devrons intégrer [PythonNet](https://github.com/pythonnet/pythonnet) dans notre application et effectuer quelques configurations.

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

        # Create PDF document
        document = Document()
        # Add page
        page = document.Pages.Add()
        # Add text to new page
        textFragment = TextFragment("Hello,world!")
        textFragment.Position = Position(100, 600)

        textFragment.TextState.FontSize = 12
        textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman")
        textFragment.TextState.BackgroundColor = Color.Blue
        textFragment.TextState.ForegroundColor = Color.Yellow

        # Create TextBuilder object
        textBuilder = TextBuilder(page)

        # Append the text fragment to the PDF page
        textBuilder.AppendText(textFragment)

        # Save PDF document
        document.Save("HelloWorld_out.pdf")
```

## Création d'un PDF complexe avec Python

Les exemples suivants montrent comment nous pouvons créer un document PDF complexe avec des images et des tableaux. Cet exemple est basé sur [la page suivante](https://docs.aspose.com/pdf/net/complex-pdf-example/).

```python
class HelloWorld(object):
    def __init__(self,licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):
    # ... skipped ...

    # Make a Complex Document
    def run_complex(self):

        # Create PDF document
        document = Document()
        # Add page
        page = document.Pages.Add()

        # Add image
        imageFileName = self.dataDir + "logo.png"
        page.AddImage(imageFileName, Rectangle(20, 730, 120, 830))

        # Add Header
        header = TextFragment("New ferry routes in Fall 2020")
        header.TextState.Font = FontRepository.FindFont("Arial")
        header.TextState.FontSize = 24
        header.HorizontalAlignment = HorizontalAlignment.Center
        header.Position = Position(130, 720)
        page.Paragraphs.Add(header)

        # Add description
        descriptionText = "Visitors must buy tickets online and tickets are limited to 5,000 per day. \
        Ferry service is operating at half capacity and on a reduced schedule. Expect lineups."
        description = TextFragment(descriptionText)
        description.TextState.Font = FontRepository.FindFont("Times New Roman")
        description.TextState.FontSize = 14
        description.HorizontalAlignment = HorizontalAlignment.Left
        page.Paragraphs.Add(description)

        # Add table
        table = Table()

        table.ColumnWidths = "200"
        table.Border = BorderInfo(BorderSide.Box, 1.0, Color.DarkSlateGray)
        table.DefaultCellBorder = BorderInfo(BorderSide.Box, 0.5, Color.Black)
        table.DefaultCellPadding = MarginInfo(4.5, 4.5, 4.5, 4.5)
        table.Margin.Bottom = 10
        table.DefaultCellTextState.Font =  FontRepository.FindFont("Helvetica")

        headerRow = table.Rows.Add()
        headerRow.Cells.Add("Departs City")
        headerRow.Cells.Add("Departs Island")

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

        # Save PDF document
        document.Save(self.dataDir + "Complex.pdf")
```

## Comment exécuter la génération de PDF sous Windows

Ce snippet montre comment exécuter les exemples ci-dessus sur un PC Windows. Nous avons supposé que `class HelloWorld` se trouve dans le fichier `example_get_started.py`. Si vous exécutez la version d'essai de Aspose.PDF for .NET, vous devez passer une chaîne vide comme `license_path`.

```python
import example_get_started

def main():

    example = example_get_started.HelloWorld("<license_path>")
    example.run_simple()
    example.run_complex()


if __name__ == '__main__':
    main()
```