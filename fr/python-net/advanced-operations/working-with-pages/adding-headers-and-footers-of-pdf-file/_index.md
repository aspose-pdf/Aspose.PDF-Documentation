---
title: Ajouter des en‑têtes et pieds de page PDF en Python
linktitle: Ajouter un en‑tête et un pied de page au PDF
type: docs
weight: 50
url: /fr/python-net/add-headers-and-footers-of-pdf-file/
description: Apprenez comment ajouter des en-têtes et des pieds de page aux fichiers PDF en Python en utilisant du texte, des images et du contenu structuré.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajoutez des en-têtes et des pieds de page aux fichiers PDF avec Python
Abstract: Cet article montre comment ajouter des en-têtes et des pieds de page aux documents PDF avec Aspose.PDF for Python via .NET. Il couvre le texte, la numérotation des pages, le HTML, l'image, le tableau et le contenu d'en-tête et de pied de page basé sur LaTeX.
---

Utilisez cette page pour ajouter un en-tête et un pied de page cohérents sur les pages PDF avec **Aspose.PDF for Python via .NET**.

Vous pouvez créer des en-têtes et des pieds de page avec [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/), [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/), et [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) objets, puis les appliquer via [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) sur chaque page.

## Ajout d’en-têtes et de pieds de page en tant que fragments de texte

Ajoutez des en-têtes et pieds de page texte simples à toutes les pages d'un PDF. Il crée [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objets, insertions [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) éléments dans eux, ensembles [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) pour un positionnement correct, et les attache à chaque page du document. Le résultat est un PDF où chaque page affiche des en-têtes et pieds de page cohérents.

Le fragment de code suivant montre comment ajouter des en-têtes et des pieds de page sous forme de fragments de texte dans un PDF à l'aide de Python :

1. Créer des fragments de texte pour l'en-tête et le pied de page.
1. Créez des objets HeaderFooter et ajoutez les fragments de texte à ceux-ci.
1. Définir les paramètres de marge pour contrôler le placement de l’en-tête et du pied de page.
1. Chargez le document PDF depuis le fichier d'entrée.
1. Parcourir toutes les pages du document.
1. Attribuez l'en-tête et le pied de page à chaque page.
1. Enregistrez le PDF modifié dans le fichier de sortie.

```python
import aspose.pdf as ap

def add_header_and_footer_as_text(input_file, output_file):
    # Create header text
    header_text = ap.text.TextFragment("Demo header")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Demo footer")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

Cette méthode est utile pour ajouter des titres cohérents, des indicateurs de page ou des mentions légales en haut et en bas de chaque page. Vous pouvez également l'étendre pour inclure des images ou du contenu dynamique, tel que les numéros de page.

## Ajout d'en-têtes et de pieds de page pour la numérotation des pages

Ajoutez une numérotation automatique des pages aux en-têtes et pieds de page d'un document PDF à l'aide d'Aspose.PDF for Python. En utilisant les variables intégrées $p (numéro de page actuel) et $P (nombre total de pages), le script insère dynamiquement la numérotation des pages sur chaque page. Les en-têtes affichent le format 'Page X de Y', tandis que les pieds de page montrent 'Page X / Y'. The [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) assure un placement correct sur chaque page.

1. Créer un TextFragment pour l’en-tête en utilisant "Page $p de $P" pour afficher la page actuelle et le nombre total de pages.
1. Créez un objet HeaderFooter et ajoutez-y le texte d’en-tête.
1. Créez un TextFragment pour le pied de page en utilisant "Page $p / $P" pour un style de numérotation alternatif.
1. Créer un objet Footer et ajouter le texte du pied de page.
1. Définissez les paramètres de marge (gauche = 50, haut = 20) et appliquez‑les à l’en‑tête et au pied de page.
1. Ouvrez le document PDF à partir du fichier d'entrée.
1. Parcourez toutes les pages et attribuez l'en-tête et le pied de page à chaque page.
1. Enregistrez le PDF mis à jour dans le chemin de sortie.

```python
import aspose.pdf as ap

def using_header_and_footer_for_page_numbering(input_file, output_file):
    # Create header text
    header_text = ap.text.TextFragment("Page $p from $P")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Page $p / $P")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Create margins
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20

    # Set header margin
    header.margin = margin
    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Ajout d’en-têtes et de pieds de page en tant que fragments HTML

Appliquer des en‑têtes et pieds de page au format HTML à chaque page d'un document PDF en utilisant Aspose.PDF for Python. En utilisant [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), le script permet le style de texte enrichi—comme le gras et l’italique—d'apparaître dans l'en-tête et le pied de page. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) est appliqué pour un placement correct, et les mêmes éléments formatés sont attachés à chaque page du document.

Le fragment de code suivant montre comment ajouter des en-têtes et des pieds de page en tant que fragments HTML à un PDF en utilisant Python :

1. Créer un extrait d'en-tête HTML en utilisant HtmlFragment—y compris du texte stylisé tel que '<strong>' pour gras.
1. Créez un objet HeaderFooter et ajoutez-y l'en-tête HTML.
1. Créer un extrait de pied de page HTML en utilisant '<i>' pour le style italique.
1. Créer un objet Footer et ajouter le HTML du pied de page à celui-ci.
1. Configurez les marges (gauche = 50, haut = 20) et attribuez‑les à l’en‑tête et au pied de page.
1. Chargez le document PDF en utilisant 'ap.Document()'.
1. Parcourez toutes les pages et attribuez l'en-tête et le pied de page à chacune d'elles.
1. Enregistrez le PDF modifié à l'emplacement de sortie spécifié.

```python
import aspose.pdf as ap

def add_header_and_footer_as_html(input_file, output_file):
    # Create header HTML
    header_html = ap.HtmlFragment("This is an HTML <strong>Header</strong>")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_html)

    # Create footer HTML
    footer_html = ap.HtmlFragment("Powered by <i>Aspose.PDF</i>")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_html)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

L'utilisation de HtmlFragment permet une mise en forme riche avec des styles en ligne ou du balisage HTML, vous offrant davantage de flexibilité de conception par rapport au texte brut.

## Ajout d'en-têtes et pieds de page en tant qu'images

Ajoutez des en-têtes et pieds de page basés sur des images à chaque page d'un document PDF en utilisant Aspose.PDF for Python. Le même fichier image est utilisé à la fois pour l'en-tête et le pied de page sur chaque page. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) positionne les images, et l'image s'ajuste automatiquement pour s'adapter à la zone d'en-tête/pied de page.

Le fragment de code suivant démontre comment ajouter des en-têtes et des pieds de page sous forme d'images à un PDF en utilisant Python :

1. Chargez l'image dans un objet 'ap.Image' et préparez-le à être utilisé comme en-tête.
1. Créez un objet HeaderFooter et attachez l'image d'en-tête à celui-ci.
1. Chargez à nouveau la même image pour l’utiliser comme pied de page.
1. Créez un objet Footer et ajoutez-y l'image du pied de page.
1. Chargez le document PDF d'entrée en utilisant 'ap.Document()'.
1. Parcourir toutes les pages du document.
1. Appliquer des marges (gauche = 50) pour positionner l'en‑tête et le pied de page.
1. Attribuez l'en-tête et le pied de page à chaque page du PDF.
1. Enregistrez le PDF mis à jour dans le fichier de sortie spécifié.

Cette technique est idéale pour marquer les documents avec des logos ou des filigranes dans la zone d'en-tête/pied de page.

```python
import aspose.pdf as ap

def add_header_and_footer_as_image(input_file, image_file, output_file):
    # Create header image
    header_image = ap.Image()
    header_image.file = image_file
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_image)

    # Create footer image
    footer_image = ap.Image()
    footer_image.file = image_file

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_image)

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Set header margin
            margin = ap.MarginInfo()
            margin.left = 50
            header.margin = margin

            # Set footer margin
            footer.margin = margin

            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Ajout d’en-têtes et de pieds de page sous forme de tableau

Ajoutez des en-têtes et pieds de page structurés, basés sur des tableaux, à toutes les pages d'un document PDF en utilisant Aspose.PDF for Python. [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) les objets offrent un meilleur contrôle de la mise en page, de l'alignement et une mise en forme cohérente pour les en-têtes et pieds de page complexes. Le texte de l'en-tête est centré tandis que le texte du pied de page est aligné à gauche, les deux utilisant la police Arial 12 pt. Les largeurs de colonne sont calculées dynamiquement en fonction des dimensions de la page afin d'assurer un placement correct.

Cet extrait de code ajoute des en-têtes et des pieds de page (en utilisant des tableaux) à chaque page d'un document PDF avec Aspose.PDF for Python via .NET.

1. Définir les styles de texte en utilisant [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) pour l'en-tête et le pied de page (police, taille, alignement).
1. Créer [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objets pour l'en-tête et le pied de page.
1. Construire l'en-tête [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) avec une seule ligne et une cellule contenant le texte d'en-tête.
1. Construire le pied de page [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) avec une seule ligne et cellule contenant le texte du pied de page.
1. Ajoutez les tableaux aux correspondants [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objets.
1. Définir le pied de page [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) pour un positionnement horizontal correct.
1. Ouvrez le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) en utilisant des méthodes appropriées.
1. Parcourir toutes les pages et attribuer l’en-tête et le pied de page basés sur un tableau à chaque page.
1. Enregistrer le modifié [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) vers le fichier de sortie.

```python
import aspose.pdf as ap

def add_header_and_footer_as_table(input_file, output_file):
    text_state_header = ap.text.TextState()
    text_state_header.font = ap.text.FontRepository.find_font("Arial")
    text_state_header.font_size = 12
    text_state_header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    text_state_footer = ap.text.TextState()
    text_state_footer.font = ap.text.FontRepository.find_font("Arial")
    text_state_footer.font_size = 12
    text_state_footer.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Create header
    header = ap.HeaderFooter()
    # Create footer
    footer = ap.HeaderFooter()
    # Create header Table
    table_header = ap.Table()
    table_header.column_widths = str(594 - header.margin.left - header.margin.right)
    header_row = table_header.rows.add()
    header_row.cells.add("This is a Table Header", text_state_header)
    # Create footer Table
    table = ap.Table()
    table.column_widths = str(594 - footer.margin.left - footer.margin.right)
    table.rows.add().cells.add("Powered by Aspose.PDF", text_state_footer)
    header.paragraphs.add(table_header)
    footer.paragraphs.add(table)
    # Set footer margin
    footer.margin.left = 150

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Ajout d'en-têtes et de pieds de page en LaTeX

Ajoutez des en-têtes et des pieds de page contenant du contenu formaté en LaTeX à toutes les pages d'un document PDF en utilisant Aspose.PDF for Python. LaTeX permet de rendre des symboles mathématiques, des dates, des marques de copyright et d'autres formats avancés. L'en-tête comprend une date dynamique, tandis que le pied de page affiche le symbole de copyright ainsi que le numéro de page actuel et le nombre total de pages.

Le fragment de code suivant montre comment utiliser [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) dans les en-têtes et pieds de page d'un PDF utilisant Aspose.PDF for Python via .NET.

1. Ouvrez le [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) en utilisant des méthodes appropriées.
1. Déterminez le nombre total de pages à utiliser dans les pieds de page dynamiques.
1. Parcourir toutes les pages du document.
1. Créer un [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objet pour l'en-tête.
1. Créer un [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) pour le texte d'en-tête contenant des commandes LaTeX (par exemple, `\\today\\`).
1. Créer un [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) objet pour le pied de page.
1. Créer un [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) pour le texte du pied de page incluant les symboles LaTeX et la numérotation des pages.
1. Ajouter le [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) vers l'objet d'en-tête/pied de page correspondant.
1. Lier l'en-tête et le pied de page à la page actuelle.
1. Enregistrer le modifié [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) vers le fichier de sortie.

```python
import aspose.pdf as ap

def add_header_and_footer_as_latex(input_file, output_file):
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTeX Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = (
                f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            )
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## Sujets de page associés

- [Travailler avec des pages PDF en Python](/pdf/fr/python-net/working-with-pages/)
- [Ajouter des numéros de page à un PDF en Python](/pdf/fr/python-net/add-page-number/)
- [Tamponner les pages PDF en Python](/pdf/fr/python-net/stamping/)
- [Formater les documents PDF en Python](/pdf/fr/python-net/formatting-pdf-document/)