---
title: Manipuler un document PDF en Python via .NET
linktitle: Manipuler le document PDF
type: docs
weight: 20
url: /fr/python-net/manipulate-pdf-document/
description: Cet article contient des informations sur la façon de valider un document PDF pour la norme PDF A en utilisant Python, comment travailler avec la table des matières, comment définir la date d’expiration d’un PDF, etc.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guide sur la manipulation de documents PDF avec Python
Abstract: Cet article offre un guide complet sur la manipulation de documents PDF à l’aide de Python, en particulier avec la bibliothèque Aspose.PDF. Il couvre plusieurs fonctionnalités, notamment la validation de documents PDF pour la conformité PDF/A‑1a et PDF/A‑1b en utilisant la méthode `validate` de la classe `Document`. Il détaille également comment ajouter, personnaliser et gérer une table des matières (TOC) dans les fichiers PDF, comme la définition de différents TabLeaderTypes, la masquage des numéros de page et la personnalisation de la numérotation des pages avec un préfixe. De plus, l’article explique comment définir une date d’expiration pour un document PDF en intégrant du JavaScript pour restreindre l’accès et comment aplatir les formulaires remplissables d’un PDF afin de les rendre non éditables. Chaque section est accompagnée d’extraits de code démontrant la mise en œuvre de ces fonctionnalités avec Aspose.PDF en Python.
---

## Manipuler le document PDF en Python

## Valider le document PDF pour la norme PDF A (A 1A et A 1B)

Pour valider un document PDF pour la compatibilité PDF/A‑1a ou PDF/A‑1b, utilisez la classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) et sa méthode [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods). Cette méthode vous permet de spécifier le nom du fichier dans lequel le résultat sera enregistré ainsi que le type de validation requis via l’énumération PdfFormat : PDF_A_1A ou PDF_A_1B.

Le fragment de code suivant montre comment valider un document PDF pour PDF/A‑1A.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Validate PDF for PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1A)
```

Le fragment de code suivant montre comment valider un document PDF pour PDF/A‑1b.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Validate PDF for PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1B)
```

## Travailler avec la table des matières

### Ajouter une table des matières à un PDF existant

La TOC dans un PDF signifie « Table des Matières ». C’est une fonctionnalité qui permet aux utilisateurs de naviguer rapidement dans un document en offrant un aperçu de ses sections et titres.

Pour ajouter une table des matières à un fichier PDF existant, utilisez la classe Heading dans l’espace de noms [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/). L’espace de noms [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) permet à la fois de créer de nouveaux fichiers PDF et de manipuler ceux existants. Pour ajouter une TOC à un PDF existant, utilisez l’espace de noms Aspose.Pdf. Le fragment de code suivant montre comment créer une table des matières dans un fichier PDF existant en utilisant Python via .NET.

```python

    import aspose.pdf as ap

    # Load an existing PDF files
    doc = ap.Document(input_pdf)

    # Get access to first page of PDF file
    tocPage = doc.pages.insert(1)

    # Create object to represent TOC information
    tocInfo = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD

    # Set the title for TOC
    tocInfo.title = title
    tocPage.toc_info = tocInfo

    # Create string objects which will be used as TOC elements
    titles = ["First page", "Second page", "Third page", "Fourth page"]
    for i in range(0, 2):
        # Create Heading object
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = tocPage
        heading2.segments.append(segment2)

        # Specify the destination page for heading object
        heading2.destination_page = doc.pages[i + 2]

        # Destination page
        heading2.top = doc.pages[i + 2].rect.height

        # Destination coordinate
        segment2.text = titles[i]

        # Add heading to page containing TOC
        tocPage.paragraphs.add(heading2)

    # Save the updated document
    doc.save(output_pdf)
```

### Définir différents TabLeaderType pour différents niveaux de TOC

Aspose.PDF pour Python permet également de définir différents TabLeaderType pour différents niveaux de TOC. Vous devez définir la propriété [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) de [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python

    import aspose.pdf as ap

    doc = ap.Document()
    tocPage = doc.pages.add()
    toc_info = ap.TocInfo()

    # set LeaderType
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 30
    toc_info.title = title

    # Add the list section to the sections collection of the Pdf document
    tocPage.toc_info = toc_info
    # Define the format of the four levels list by setting the left margins
    # and
    # text format settings of each level

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
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

    # Create a section in the Pdf document
    page = doc.pages.add()

    # Add four headings in the section
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        heading2.toc_page = tocPage
        segment2.text = "Sample Heading" + str(Level)
        heading2.text_state.font = ap.text.FontRepository.find_font("Arial")

        # Add the heading into Table Of Contents.
        heading2.is_in_list = True
        page.paragraphs.add(heading2)

    # save the Pdf
    doc.save(output_pdf)
```

### Masquer les numéros de page dans la TOC

Dans le cas où vous ne souhaitez pas afficher les numéros de page, ainsi que les titres, dans la TOC, vous pouvez définir la propriété [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) de la classe [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) sur false. Veuillez consulter le fragment de code suivant pour masquer les numéros de page dans la table des matières :

```python

    import aspose.pdf as ap

    doc = ap.Document()
    toc_page = doc.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    # Add the list section to the sections collection of the Pdf document
    toc_page.toc_info = toc_info
    # Define the format of the four levels list by setting the left margins and
    # text format settings of each level

    toc_info.is_show_page_numbers = False
    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD
    page = doc.pages.add()
    # Add four headings in the section
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        segment2.text = "this is heading of level " + str(Level)
        heading2.is_in_list = True
        page.paragraphs.add(heading2)
    doc.save(output_pdf)

```

### Personnaliser les numéros de page lors de l’ajout de la TOC

Il est fréquent de personnaliser la numérotation des pages dans la TOC lors de l’ajout d’une TOC à un document PDF. Par exemple, il peut être nécessaire d’ajouter un préfixe avant le numéro de page comme P1, P2, P3, etc. Dans ce cas, Aspose.PDF pour Python fournit la propriété [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) de la classe [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) qui peut être utilisée pour personnaliser les numéros de page comme le montre l’exemple de code suivant.

```python

    import aspose.pdf as ap

    # Load an existing PDF files
    doc = ap.Document(input_pdf)
    # Get access to first page of PDF file
    toc_page = doc.pages.insert(1)
    # Create object to represent TOC information
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Table Of Contents")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    # Set the title for TOC
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info
    for i in range(len(doc.pages)):
        # Create Heading object
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        # Specify the destination page for heading object
        heading2.destination_page = doc.pages[i + 1]
        # Destination page
        heading2.top = doc.pages[i + 1].rect.height
        # Destination coordinate
        segment2.text = "Page " + str(i)
        # Add heading to page containing TOC
        toc_page.paragraphs.add(heading2)

    # Save the updated document
    doc.save(output_pdf)

```

## Comment définir la date d’expiration d’un PDF

Nous appliquons des privilèges d’accès aux fichiers PDF afin qu’un groupe d’utilisateurs puisse accéder à certaines fonctionnalités/objets des documents PDF. Pour restreindre l’accès à un fichier PDF, nous appliquons généralement un chiffrement et il peut être nécessaire de définir une date d’expiration du fichier PDF, afin que l’utilisateur qui accède/consulte le document reçoive une alerte appropriée concernant l’expiration du PDF.

```python

    import aspose.pdf as ap

    # Instantiate Document object
    doc = ap.Document()
    # Add page to pages collection of PDF file
    doc.pages.add()
    # Add text fragment to paragraphs collection of page object
    doc.pages[1].paragraphs.add(ap.text.TextFragment("Hello World..."))
    # Create JavaScript object to set PDF expiry date
    javaScript = ap.annotations.JavascriptAction(
        "var year=2017;"
        + "var month=5;"
        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        + "expiry = new Date(year, month);"
        + "if (today.getTime() > expiry.getTime())"
        + "app.alert('The file is expired. You need a new one.');"
    )
    # Set JavaScript as PDF open action
    doc.open_action = javaScript

    # Save PDF Document
    doc.save(output_pdf)
```

## Aplatir un PDF remplissable en Python

Les documents PDF contiennent souvent des formulaires avec des widgets interactifs remplissables tels que des boutons radio, des cases à cocher, des zones de texte, des listes, etc. Pour les rendre non éditables à des fins diverses, il faut aplatir le fichier PDF.
Aspose.PDF fournit la fonction permettant d’aplatir votre PDF en Python avec seulement quelques lignes de code :

```python

    import aspose.pdf as ap

    # Load source PDF form
    doc = ap.Document(input_pdf)

    # Flatten Flatten Fillable PDF
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(output_pdf)
```


