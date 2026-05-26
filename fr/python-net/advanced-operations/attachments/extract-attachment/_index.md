---
title: Extraire les pièces jointes du PDF
linktitle: Extraire les pièces jointes
type: docs
weight: 50
url: /fr/python-net/extract-attachment/
description: Apprenez comment travailler avec les pièces jointes PDF en utilisant Python et Aspose.PDF.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Guide complet pour gérer les pièces jointes PDF en Python : ajouter, extraire et traiter les fichiers intégrés"
Abstract: Les pièces jointes PDF sont largement utilisées pour stocker des documents de support, des rapports, des images et d'autres ressources directement à l'intérieur d'un fichier PDF. Cet article fournit un aperçu complet de la gestion des pièces jointes PDF avec Python en utilisant Aspose.PDF. Il explique comment intégrer des fichiers externes dans des PDF existants, extraire des pièces jointes spécifiques ou toutes, inspecter les métadonnées telles que la taille du fichier et les horodatages, et récupérer les fichiers stockés en tant qu'annotations FileAttachment. Chaque exemple montre des techniques pratiques pour automatiser les flux de travail de pièces jointes, améliorer la portabilité des documents et simplifier la gestion des fichiers. Que vous construisiez des systèmes de documents d'entreprise ou des scripts d'automatisation personnalisés, les développeurs peuvent utiliser ces méthodes pour gérer efficacement les fichiers intégrés au sein des documents PDF.
---

## Extraire une pièce jointe spécifique du PDF

Extrait un fichier intégré unique d'un document PDF à l'aide de Python et Aspose.PDF. Il recherche une pièce jointe par nom, récupère son contenu et l'enregistre en tant que fichier séparé. Cela est utile pour accéder aux documents intégrés tels que des rapports, des journaux ou des fichiers d'assistance stockés dans le PDF.

1. Définir la fonction 'extract_single_attachment()'.
1. Ouvrir le document PDF.
1. Rechercher la pièce jointe.
1. Extraire le contenu de la pièce jointe.

```python
import aspose.pdf as ap

def extract_single_attachment(infile, attachment_name, outfile):
    with ap.Document(infile) as document:
        print(f"Extracting attachment: {attachment_name}")

        attachment_found = False
        for file_spec in document.embedded_files:
            if file_spec.name == attachment_name:
                with open(outfile, "wb") as f:
                    f.write(file_spec.contents.read())
                print("Attachment extracted successfully")
                attachment_found = True
                break

        if not attachment_found:
            raise ValueError(f"Attachment '{attachment_name}' not found in PDF")
```

## Afficher les métadonnées de la pièce jointe de fichier

Cette fonction d'assistance affiche les informations de métadonnées d'un objet de spécification de fichier. Elle est généralement utilisée lors du travail avec des pièces jointes de fichiers intégrées dans les PDF en utilisant Aspose.PDF, permettant aux développeurs d'inspecter des détails tels que la somme de contrôle, la date de création, la date de modification et la taille du fichier.

```python
def _print_file_params(params):
    """Helper to print file specification parameters."""
    if params:
        print(f"CheckSum: {params.check_sum}")
        print(f"Creation Date: {params.creation_date}")
        print(f"Modification Date: {params.mod_date}")
        print(f"Size: {params.size}")
```

## Extraire et inspecter toutes les pièces jointes PDF

Cet extrait de code montre comment extraire tous les fichiers embarqués d'un document PDF en utilisant Python et Aspose.PDF. Il enregistre non seulement chaque pièce jointe dans un dossier spécifié, mais affiche également des métadonnées détaillées telles que le nom du fichier, la description, le type MIME, la somme de contrôle et les horodatages. Cela est utile pour l’audit, l’exportation ou le traitement du contenu embarqué dans les fichiers PDF.

```python
from os import path
import aspose.pdf as ap

def extract_attachments(infile, output_dir):
    with ap.Document(infile) as document:
        print(f"Total files: {len(document.embedded_files)}")

        for file_spec in document.embedded_files:
            print(f"Name: {file_spec.name}")
            print(f"Description: {file_spec.description}")
            print(f"Mime Type: {file_spec.mime_type}")
            _print_file_params(file_spec.params)

            output_path = path.join(output_dir, file_spec.name)
            with open(output_path, "wb") as f:
                f.write(file_spec.contents.read())
```

## Extraire des fichiers des annotations de pièces jointes PDF

Extraire un fichier intégré à partir d'une annotation FileAttachment dans un PDF en utilisant Python et Aspose.PDF. Il recherche la première page pour la première annotation de pièce jointe, récupère le fichier intégré et le sauvegarde dans un répertoire de sortie sélectionné. Cela est utile lorsque les PDF contiennent des icônes de pièces jointes cliquables au lieu de collections de fichiers intégrés standard.

```python
from os import path
import aspose.pdf as ap
from aspose.pycore import cast

def extract_file_attachment_annotation(infile, output_dir):
    # Open PDF document
    with ap.Document(infile) as document:

        # Get first page
        page = document.pages[1]

        # Find first FileAttachment annotation
        file_attachment = next(
            (
                annot
                for annot in page.annotations
                if annot.annotation_type == ap.annotations.AnnotationType.FILE_ATTACHMENT
            ),
            None,
        )

        if file_attachment is None:
            print("No FileAttachment annotation found on the first page.")
            return

        # Cast to FileAttachmentAnnotation
        faa = cast(ap.annotations.FileAttachmentAnnotation, file_attachment)

        # Access embedded file
        file_spec = faa.file
        print(f"File name: {file_spec.name}")

        # Save embedded file to disk
        output_path = path.join(output_dir, f"extracted-{file_spec.name}")
        with open(output_path, "wb") as f:
            f.write(file_spec.contents.read())

        print(f"Extracted to: {output_path}")
```