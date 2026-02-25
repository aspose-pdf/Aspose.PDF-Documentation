---
title: Annotations et texte spécial avec Python
linktitle: Annotations et texte spécial
type: docs
weight: 40
url: /fr/python-net/annotation-and-special-text/
description: Cette section contient des articles sur l'annotation et l'extraction de texte spécial à partir de documents PDF en utilisant Aspose.PDF en Python.
lastmod: "2025-11-05"
sitemap: 
    changefreq: "weekly"
    priority: 0.7
---

## Extraire le texte des annotations de tampon

La bibliothèque Aspose.PDF for Python permet d'extraire le texte d'une annotation de type tampon (plus précisément une StampAnnotation) sur une page PDF.

1. Ouvrir le document.
1. Accéder à l'annotation de tampon depuis la collection d'annotations de la page.
1. Obtenir le flux d'apparence du tampon (XForm).
1. Utiliser un 'TextAbsorber' pour extraire le texte intégré de cette apparence.

```python

import os
import aspose.pdf as ap

def extract_text_from_stamp(infile, page_number, annotation_index, outfile):
    """
    Extracts text from a stamp annotation on a given page in a PDF document.
    Args:
        infile (str): Path to the input PDF file.
        page_number (int): 1-based index of the page containing the stamp.
        annotation_index (int): 1-based index of the annotation in that page.
        outfile (str): Path to the output text file where extracted text will be saved.
    """
    document = ap.Document(infile)
    try:
        page = document.pages[page_number]
        annot = page.annotations[annotation_index]
        # Ensure it's a StampAnnotation
        if isinstance(annot, ap.annotations.StampAnnotation):
            # Get normal appearance XForm of the stamp
            xform = annot.appearance["N"]
            absorber = ap.text.TextAbsorber()
            absorber.visit(xform)
            extracted = absorber.text
            with open(outfile, "w", encoding="utf-8") as f:
                f.write(extracted)
    finally:
        document.close()
```

## Extraire le texte surligné

Le standard PDF offre la possibilité de mettre en surbrillance des parties de texte dans un document. Pour extraire ce contenu surligné, suivez ces étapes :

1. Importer `aspose.pdf as ap` et les auxiliaires que vous utilisez (`is_assignable`, `cast`).
2. Appeler `ap.Document(infile)` pour ouvrir le PDF.
3. Sélectionner la page souhaitée avec `document.pages` (la collection de pages commence à 1).
4. Parcourir `page.annotations` pour examiner chaque annotation sur cette page.
5. Filtrer les annotations afin que seules les annotations de surlignage soient traitées.
6. Convertir l'annotation en `HighlightAnnotation` et appeler `get_marked_text()` pour lire le texte surligné.
7. Imprimer ou gérer autrement le texte retourné.

```python
def extract_highlight_text(infile):
    """
    Extract text from highlight annotations.

    Args:
        infile (str): Input PDF filename

    Returns:
        None

    Example:
        extract_highlight_text("sample.pdf")

    Note:
        Prints marked text from each highlight annotation on first page.
    """
    document = ap.Document(infile)
    page = document.pages[1]

    for annotation in page.annotations:
        if is_assignable(annotation, ap.annotations.HighlightAnnotation):
            highlight_annotation = cast(ap.annotations.HighlightAnnotation, annotation)
            print(highlight_annotation.get_marked_text())
```

## Extraire le texte des exposants et indices

**Indices et exposants** sont le plus souvent utilisés dans les formules, les expressions mathématiques et les spécifications de composés chimiques. Il est difficile de les éditer lorsqu'ils sont nombreux dans le même passage de texte.
Dans l'une des dernières versions, la bibliothèque **Aspose.PDF for Python via .NET** a ajouté la prise en charge de l'extraction du texte des exposants et indices à partir de PDF. Extrayez tout le texte (y compris les exposants et indices) d'une page spécifique d'un document PDF en utilisant 'TextFragmentAbsorber'.

1. Charger le document PDF.
1. Instancier un 'TextFragmentAbsorber()', qui prend en charge la détection du texte en exposant/indice selon les capacités de la version.
1. Appeler 'document.pages[page_number].accept(absorber)' pour analyser uniquement la page donnée.
1. Récupérer le texte extrait via 'absorber.text'.
1. Écrire le texte dans le fichier de sortie en utilisant les I/O standard.
1. Fermer le document pour libérer les ressources.

```python

import os
import aspose.pdf as ap

def extract_super_sub_text(infile, outfile, page_number=1):
    """
    Extract text (including superscript/subscript) from a specified page of a PDF and write to a text file.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based index of the page to extract.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        # Accept only the specific page for extraction
        document.pages[page_number].accept(absorber)
        extracted_text = absorber.text
        with open(outfile, "w", encoding="utf‑8") as f:
            f.write(extracted_text)
    finally:
        document.close()
```

## Parcourir les TextFragments pour détecter les exposants/indices

Parcourir chaque fragment de texte dans une page, vérifier s'il s'agit d'un exposant ou d'un indice, et traiter en conséquence.

1. Charger le document PDF.
1. Créer 'TextFragmentAbsorber()' et l'accepter sur la page choisie.
1. Accéder à 'absorber.text_fragments', qui renvoie une collection de fragments trouvés sur cette page.
1. Pour chaque fragment :
- Récupérer 'fragment.text'.
- Vérifier 'fragment.text_state.superscript' et 'fragment.text_state.subscript'.
- Écrire une ligne dans le fichier de sortie avec le texte du fragment et les indicateurs.
1. Fermer le fichier et le document.

```python

import os
import aspose.pdf as ap

def extract_super_sub_details(infile, outfile, page_number=1):
    """
    Extract details of each text fragment on a page, identifying superscript and subscript items.
    Args:
        infile (str): Path to input PDF file.
        outfile (str): Path to output text file.
        page_number (int): 1‑based page index.
    """
    document = ap.Document(infile)
    try:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages[page_number].accept(absorber)

        with open(outfile, "w", encoding="utf‑8") as f:
            for fragment in absorber.text_fragments:
                text = fragment.text
                is_sup = fragment.text_state.superscript  # True if superscript
                is_sub = fragment.text_state.subscript    # True if subscript
                f.write(f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n")
    finally:
        document.close()
```
