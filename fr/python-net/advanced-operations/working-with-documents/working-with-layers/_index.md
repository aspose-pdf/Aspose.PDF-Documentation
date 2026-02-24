---
title: Travailler avec les calques PDF à l’aide de Python
linktitle: Travailler avec les calques PDF
type: docs
weight: 50
url: /fr/python-net/working-with-pdf-layers/
description: La tâche suivante explique comment verrouiller un calque PDF, extraire les éléments d’un calque PDF, aplatir un PDF à calques et fusionner tous les calques d’un PDF en un seul.
lastmod: "2025-11-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Manipuler les calques PDF
Abstract: Ce guide fournit un aperçu complet de la manière de gérer et de manipuler les calques PDF à l'aide de la bibliothèque Aspose.PDF for Python via .NET. Les calques PDF — également appelés Groupes de contenu optionnel (OCG) — permettent d'organiser le contenu en composants visuels séparés qui peuvent être activés ou désactivés.
---

Les calques PDF sont un moyen puissant d'organiser et de présenter le contenu de manière flexible au sein d'un même fichier PDF, permettant aux utilisateurs d'afficher ou de masquer différentes parties selon leurs besoins.

Avec **Aspose.PDF for Python via .NET**, vous pouvez :

- Verrouiller/Déverrouiller les calques pour contrôler la visibilité.
- Extraire les calques dans des fichiers ou flux séparés.
- Aplatir les calques pour les rendre permanents.
- Fusionner les calques en un seul calque unifié.

## Ajouter des calques à un PDF

Cet exemple montre comment créer et ajouter plusieurs calques à un document PDF à l'aide d'Aspose.PDF for Python via .NET. Chaque calque contient un contenu graphique distinct, tel que des lignes colorées, qui peuvent être activées ou désactivées dans les visionneuses PDF prenant en charge les calques.

1. Créez un nouveau document PDF et ajoutez une page.
1. Créez et ajoutez le calque rouge.
1. Créez et ajoutez le calque vert.
1. Créez et ajoutez le calque bleu.
1. Enregistrez le document PDF.

Le PDF résultant contiendra trois calques distincts : une ligne rouge, une ligne verte et une ligne bleue. Chacun peut être activé ou désactivé dans les lecteurs PDF qui prennent en charge le contenu à calques.

```python

import aspose.pdf as ap
from os import path

def add_colored_layers(outfile: str, data_dir: str) -> None:
    """
    Creates a PDF with three layers (Red, Green, Blue lines).
    
    Args:
        outfile (str): Name of the output PDF file.
        data_dir (str): Directory path to save the file.
    """
    path_outfile = path.join(data_dir, outfile)

    try:
        # Create a new PDF document and add a blank page
        document = ap.Document()
        page = document.pages.add()

        # Helper function to add a colored line layer
        def add_layer(layer_id: str, layer_name: str, color: tuple, y_position: int):
            layer = ap.Layer(layer_id, layer_name)
            layer.contents.append(ap.operators.SetRGBColorStroke(*color))
            layer.contents.append(ap.operators.MoveTo(500, y_position))
            layer.contents.append(ap.operators.LineTo(400, y_position))
            layer.contents.append(ap.operators.Stroke())
            page.layers.append(layer)

        # Add Red, Green, and Blue layers
        add_layer("oc1", "Red Line", (1, 0, 0), 700)
        add_layer("oc2", "Green Line", (0, 1, 0), 750)
        add_layer("oc3", "Blue Line", (0, 0, 1), 800)

        # Save the document
        document.save(path_outfile)
        print(f"\nLayers added successfully.\nFile saved at: {path_outfile}")

    except Exception as e:
        print(f"Error adding layers: {e}")
```

## Verrouiller un calque PDF

Avec Aspose.PDF for Python via .NET, vous pouvez ouvrir un PDF, verrouiller un calque spécifique sur la première page et enregistrer le document avec les modifications.

Cet exemple montre comment verrouiller un calque (Groupe de contenu optionnel, OCG) dans un document PDF à l'aide d'Aspose.PDF for Python via .NET. Le verrouillage empêche les utilisateurs de modifier la visibilité du calque dans un lecteur PDF, garantissant que le contenu reste toujours visible (ou masqué) selon les définitions du document.

Méthodes et propriétés disponibles :

- layer.lock() – Verrouille le calque.
- layer.unlock() – Déverrouille le calque.
- layer.locked – Retourne l’état de verrouillage actuel.

1. Ouvrez le document PDF.
1. Accédez à la première page du PDF.
1. Vérifiez si la page possède des calques.
1. Récupérez le premier calque et verrouillez-le.
1. Enregistrez le PDF mis à jour.

Si le PDF contient des calques, le premier calque sera verrouillé, garantissant que son état de visibilité ne puisse être modifié par l'utilisateur. Si aucun calque n'est trouvé, un message est affiché à la place.

```python

import aspose.pdf as ap
from os import path

def lock_layer(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]
        layer = page.layers[0]

        # Lock the layer
        layer.lock()

        # Save updated PDF
        document.save(path_outfile)
```

## Extraire les éléments d’un calque PDF

Cet exemple utilise la bibliothèque Aspose.PDF for Python via .NET pour extraire les calques individuels de la première page d’un document PDF et enregistrer chaque calque comme fichier PDF séparé.

Pour créer un nouveau PDF à partir d’un calque, le fragment de code suivant peut être utilisé :

1. Chargez le document PDF. Le PDF d’entrée est chargé dans un objet Aspose.PDF.Document.
1. Accédez aux calques de la page 1. Le script récupère tous les calques de la première page à l’aide de document.pages[1].layers.
1. Vérifiez la présence de calques. Si aucun calque n’est trouvé, un message est affiché et la fonction se termine.
1. Parcourez et enregistrez chaque calque.

```python

import aspose.pdf as ap
from os import path

def save_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers

        # Save each layer to a new PDF
        for layer in layers:
            layer.save(path_outfile)
```

Il est possible d’extraire les éléments d’un calque PDF et de les enregistrer dans un nouveau flux de fichier PDF :

```python

import aspose.pdf as ap
from os import path

def save_layers_to_stream(path_infile, output_stream):
    with ap.Document(path_infile) as document:
        layers = document.pages[1].layers
        for layer in layers:
            layer.save(output_stream)
```

## Aplatir un PDF à calques

Ce script utilise Aspose.PDF for Python via .NET pour aplatir tous les calques de la première page d’un document PDF. L’aplatissement fusionne le contenu visuel de chaque calque en un seul calque unifié, facilitant l’impression, le partage ou l’archivage sans perte de fidélité visuelle ou de données spécifiques aux calques.

1. Charger le document PDF. Le PDF d'entrée est chargé dans un objet Aspose.PDF.Document.
1. Accéder aux calques de la page 1. Le script récupère tous les calques de la première page en utilisant document.pages[1].layers.
1. Vérifier la présence de calques. Si aucun calque n'est trouvé, un message est affiché et la fonction se termine.
1. Aplatir chaque calque. Chaque calque est aplati à l'aide de layer.flatten(True), ce qui fusionne son contenu avec la page.
1. Enregistrer le document modifié.

```python

import aspose.pdf as ap
from os import path

def flatten_layers(path_infile, path_outfile):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if not page.layers:
            print("No layers found in the document.")
            return
        # Flatten each layer
        for layer in page.layers:
            layer.flatten(cleanup_content_stream=True)

        document.save(path_outfile)
```

## Fusionner tous les calques du PDF en un seul

Cet extrait de code utilise Aspose.PDF pour fusionner tous les calques de la première page d'un PDF en un seul calque unifié avec un nom personnalisé.

1. Charger le document PDF. Le PDF est chargé dans un objet Aspose.PDF.Document.
1. Accéder à la page et à ses calques. La première page est sélectionnée et ses calques sont récupérés.
1. Vérifier les calques. Si aucun calque n'existe, un message est affiché et le processus se termine.
1. Définir le nom du nouveau calque. Un nouveau nom de calque ("LayerNew") est spécifié pour le résultat fusionné.
1. Fusionner les calques. Si un ID de groupe de contenu optionnel est fourni, il est utilisé lors de la fusion. Sinon, les calques sont fusionnés en utilisant uniquement le nouveau nom.
1. Enregistrer le document

```python

import aspose.pdf as ap
from os import path

def merge_layers(path_infile, path_outfile, new_layer_name, optional_group_id=None):
    with ap.Document(path_infile) as document:
        page = document.pages[1]

        if optional_group_id:
            page.merge_layers(new_layer_name, optional_group_id)
        else:
            page.merge_layers(new_layer_name)

        document.save(path_outfile)
```
