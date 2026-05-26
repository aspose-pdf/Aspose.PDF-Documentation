---
title: Annotations et texte spécial avec Python
linktitle: Annotations et texte spécial
type: docs
weight: 40
url: /fr/python-net/annotation-and-special-text/
description: Apprenez comment extraire le texte des annotations de tampon, du texte surligné et du contenu exposant/sous‑exposant dans les documents PDF en utilisant Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Extraire le texte des annotations de tampon

Utiliser [TextAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textabsorber) pour extraire le texte intégré dans un [StampAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/stampannotation) flux d'apparence. Ceci est utile lorsque le contenu du tampon est rendu comme un Form XObject plutôt que stocké en texte brut.

1. Ouvrir le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Accédez à l'annotation cible depuis `page.annotations`.
1. Vérifiez que c'est un `StampAnnotation`, puis récupérer son apparence normale XForm.
1. Passez le XForm à `TextAbsorber.visit()` pour extraire le texte incorporé.

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

Itérer sur les annotations d’une page et utiliser [HighlightAnnotation.get_marked_text()](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) pour lire les segments de texte couverts par chaque surlignage. La collection d’annotations de la page est indexée à partir de 1.

1. Ouvrir le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) et sélectionnez la page cible.
1. Parcourir `page.annotations`.
1. Utiliser `is_assignable` filtrer pour [HighlightAnnotation](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/highlightannotation) instances.
1. Caster l'annotation et appeler `get_marked_text()` pour récupérer le contenu surligné.

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

## Extraire le texte en exposant et en indice

Les exposants et les indices apparaissent fréquemment dans les formules, les expressions mathématiques et les noms de composés chimiques. Aspose.PDF for Python via .NET prend en charge l'extraction de ce contenu via [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber), qui détecte les métadonnées de positionnement au niveau des caractères.

1. Ouvrir le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document).
1. Créer un `TextFragmentAbsorber` instance.
1. Appeler `document.pages[page_number].accept(absorber)` scanner la page cible.
1. Récupérer le texte complet extrait de `absorber.text`.
1. Écrivez le résultat dans un fichier et fermez le document.

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
        with open(outfile, "w", encoding="utf-8") as f:
            f.write(extracted_text)
    finally:
        document.close()
```

## Itérer à travers les fragments de texte pour détecter les exposants/sous‑exposants

Pour l'inspection fragment par fragment, itérez sur `absorber.text_fragments` et lire le `text_state.superscript` et `text_state.subscript` drapeaux booléens sur chaque [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment).

1. Ouvrir le [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document) et créer un [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber).
1. Accepter l'absorbeur sur la page cible afin de le remplir `absorber.text_fragments`.
1. Pour chaque fragment, lire `fragment.text`, `fragment.text_state.superscript`, et `fragment.text_state.subscript`.
1. Écrivez les résultats dans le fichier de sortie et fermez le document.

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

        with open(outfile, "w", encoding="utf-8") as f:
            for fragment in absorber.text_fragments:
                text = fragment.text
                is_sup = fragment.text_state.superscript  # True if superscript
                is_sub = fragment.text_state.subscript  # True if subscript
                f.write(
                    f"Text: '{text}' | Superscript: {is_sup} | Subscript: {is_sub}\n"
                )
    finally:
        document.close()
```
