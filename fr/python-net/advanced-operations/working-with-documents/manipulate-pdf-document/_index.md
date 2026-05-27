---
title: Manipuler les documents PDF en Python
linktitle: Manipuler le document PDF
type: docs
weight: 20
url: /fr/python-net/manipulate-pdf-document/
description: Apprenez à valider, structurer et modifier des documents PDF en Python, y compris la gestion de la TOC et les vérifications PDF/A.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guide sur la manipulation de documents PDF avec Python
Abstract: Cet article fournit un guide complet sur la manipulation de documents PDF avec Python, en particulier avec la bibliothèque Aspose.PDF. Il couvre plusieurs fonctionnalités, y compris la validation de documents PDF pour la conformité PDF/A-1a et PDF/A-1b en utilisant la méthode `validate` de la classe `Document`. Il détaille également comment ajouter, personnaliser et gérer une Table des matières (TOC) dans les fichiers PDF, comme définir différents TabLeaderTypes, masquer les numéros de page et personnaliser la numérotation des pages avec un préfixe. De plus, l'article explique comment définir une date d'expiration pour un document PDF en incorporant du JavaScript pour restreindre l'accès et comment aplatir les formulaires remplissables d'un PDF afin de les rendre non éditables. Chaque section est accompagnée d'extraits de code démontrant la mise en œuvre de ces fonctionnalités avec Aspose.PDF en Python.
---

Cette page est utile lorsque vous devez valider la conformité des PDF, créer ou personnaliser une table des matières, définir le comportement d'expiration du document, ou aplatir les PDF remplissables dans les flux de travail Python.

## Manipuler le Document PDF en Python

## Valider le document PDF pour la norme PDF/A (A 1A et A 1B)

Pour valider un document PDF pour la compatibilité PDF/A-1a ou PDF/A-1b, utilisez le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) classe [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) méthode. Cette méthode vous permet de spécifier le nom du fichier dans lequel le résultat doit être enregistré et le type de validation requis, l'énumération PdfFormat : PDF_A_1A ou PDF_A_1B.

L'extrait de code suivant vous montre comment valider un document PDF pour PDF/A-1A.

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1a(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1A)
```

Le fragment de code suivant vous montre comment valider un document PDF pour PDF/A-1b.

```python
import sys
from os import path
import aspose.pdf as ap


def validate_pdfa_standard_a1b(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.validate(output_pdf, ap.PdfFormat.PDF_A_1B)
```

## Travailler avec TOC

### Ajouter une table des matières au PDF existant

TOC dans PDF signifie "Table of Contents". C’est une fonctionnalité qui permet aux utilisateurs de naviguer rapidement dans un document en fournissant un aperçu de ses sections et titres. 

Pour ajouter une TOC à un fichier PDF existant, utilisez la classe Heading dans le [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) espace de noms. Le [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) L'espace de noms peut à la fois créer de nouveaux fichiers PDF et manipuler des fichiers PDF existants. Pour ajouter une TOC à un PDF existant, utilisez l'espace de noms Aspose.Pdf. Le fragment de code suivant montre comment créer une table des matières dans un fichier PDF existant en utilisant Python via .NET.

```python
import sys
from os import path
import aspose.pdf as ap


def add_table_of_contents(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_page.toc_info = toc_info

    titles = ["First page", "Second page"]
    for index, title_text in enumerate(titles[:2]):
        heading = ap.Heading(1)
        segment = ap.text.TextSegment(title_text)
        heading.toc_page = toc_page
        heading.segments.append(segment)
        destination_page = document.pages[index + 2]
        heading.destination_page = destination_page
        heading.top = destination_page.rect.height
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Définir un TabLeaderType différent pour chaque niveau de TOC

Aspose.PDF for Python permet également de définir différents TabLeaderType pour différents niveaux de TOC. Vous devez définir [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) propriété de [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python
import sys
from os import path
import aspose.pdf as ap


def set_toc_levels(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 5):
        heading = ap.Heading(level)
        heading.is_auto_sequence = True
        heading.toc_page = toc_page
        heading.text_state.font = ap.text.FontRepository.find_font("Arial")
        segment = ap.text.TextSegment(f"Sample Heading{level}")
        heading.segments.append(segment)
        heading.is_in_list = True
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Masquer les numéros de page dans le TOC

Dans le cas où vous ne voulez pas afficher les numéros de page, ainsi que les titres dans le TOC, vous pouvez utiliser [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) propriété de [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) Classe comme false. Veuillez vérifier le fragment de code suivant pour masquer les numéros de page dans la table des matières :

```python
import sys
from os import path
import aspose.pdf as ap


def hide_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.is_show_page_numbers = False
    toc_page.toc_info = toc_info

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    page = document.pages.add()
    for level in range(1, 2):
        heading = ap.Heading(level)
        heading.toc_page = toc_page
        heading.is_auto_sequence = True
        heading.is_in_list = True
        segment = ap.text.TextSegment(f"this is heading of level {level}")
        heading.segments.append(segment)
        page.paragraphs.add(heading)

    document.save(output_pdf)
```

### Personnaliser les numéros de page lors de l'ajout de la TOC

Il est courant de personnaliser la numérotation des pages dans la TOC lors de l'ajout de la TOC dans un document PDF. Par exemple, nous pourrions avoir besoin d'ajouter un préfixe avant le numéro de page comme P1, P2, P3, etc. Dans un tel cas, Aspose.PDF for Python fournit [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) propriété de [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) classe pouvant être utilisée pour personnaliser les numéros de page comme illustré dans l'exemple de code suivant.

```python
import sys
from os import path
import aspose.pdf as ap


def customize_page_numbers_in_toc(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    toc_page = document.pages.insert(1)
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info

    for index, page in enumerate(document.pages, start=1):
        heading = ap.Heading(1)
        heading.toc_page = toc_page
        heading.destination_page = page
        heading.top = page.rect.height
        segment = ap.text.TextSegment(f"Page {index}")
        heading.segments.append(segment)
        toc_page.paragraphs.add(heading)

    document.save(output_pdf)
```

## Comment définir la date d'expiration du PDF

Nous appliquons des privilèges d'accès sur les fichiers PDF afin qu'un groupe particulier d'utilisateurs puisse accéder à des fonctionnalités/objets spécifiques des documents PDF. Pour restreindre l'accès aux fichiers PDF, nous utilisons généralement le chiffrement et il peut y avoir une exigence de définir une expiration du fichier PDF, afin que l'utilisateur accédant/visualisant le document reçoive une invite valide concernant l'expiration du fichier PDF.

```python
import sys
from os import path
import aspose.pdf as ap


def set_pdf_expiry_date(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    document.pages.add()
    document.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    script = ap.annotations.JavascriptAction(
        "var year=2017;"
        "var month=5;"
        "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        "expiry = new Date(year, month);"
        "if (today.getTime() > expiry.getTime())"
        "app.alert('The file is expired. You need a new one.');"
    )
    document.open_action = script
    document.save(output_pdf)
```

## Aplatir le PDF remplissable en Python

Les documents PDF incluent souvent des formulaires avec des widgets interactifs remplissables tels que des boutons radio, des cases à cocher, des zones de texte, des listes, etc. Pour les rendre non modifiables à diverses fins d'application, nous devons aplatir le fichier PDF.
Aspose.PDF fournit la fonction pour aplatir votre PDF en Python avec seulement quelques lignes de code :

```python
import sys
from os import path
import aspose.pdf as ap


def flatten_fillable_pdf(input_pdf, output_pdf):
    document = ap.Document(input_pdf)
    if document.form and document.form.fields:
        for field in document.form.fields:
            field.flatten()
    document.save(output_pdf)
```

## Sujets de documents associés

- [Travailler avec des documents PDF en Python](/pdf/fr/python-net/working-with-documents/)
- [Formater des documents PDF en Python](/pdf/fr/python-net/formatting-pdf-document/)
- [Créer des fichiers PDF en Python](/pdf/fr/python-net/create-pdf-document/)
- [Optimiser les fichiers PDF en Python](/pdf/fr/python-net/optimize-pdf/)
