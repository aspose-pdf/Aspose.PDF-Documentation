---
title: Remplacer le texte dans le PDF avec Python
linktitle: Remplacer le texte dans le PDF
type: docs
weight: 40
url: /fr/python-net/replace-text-in-pdf/
description: Apprenez à remplacer du texte dans des fichiers PDF avec Python, y compris le remplacement du texte sur plusieurs pages, la limitation des modifications à une région de page, l’utilisation d’expressions régulières et la suppression de texte.
lastmod: "2026-05-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Remplacez et supprimez du texte dans des fichiers PDF en utilisant Python
Abstract: Cet article montre comment remplacer du texte dans des documents PDF avec Aspose.PDF for Python via .NET. Il couvre le remplacement de texte sur toutes les pages, le remplacement de zones de page, la correspondance regex, le remplacement de Font, l'ajustement de la mise en page du texte et la suppression de texte visible ou masqué.
---

Cette page montre comment **remplacer du texte dans un PDF avec Python** en utilisant Aspose.PDF for Python via .NET.

Utilisez ces exemples lorsque vous devez mettre à jour les valeurs de texte, supprimer le contenu indésirable, remplacer le texte dans une zone de page spécifique ou appliquer des règles de remplacement de texte sur plusieurs pages PDF.

## Remplacer le texte dans le PDF avec Python

### Remplacer le texte dans toutes les pages d'un document PDF

{{% alert color="primary" %}}

Vous pouvez essayer la recherche et le remplacement de texte en ligne avec Aspose.PDF [application de rédaction](https://products.aspose.app/pdf/redaction).

{{% /alert %}}

Le remplacement de texte est une exigence courante lors de la mise à jour ou de la correction du contenu de documents PDF existants — par exemple, changer les noms de produit, corriger les fautes de frappe ou mettre à jour la terminologie sur plusieurs pages.

Aspose.PDF for Python via .NET propose une méthode puissante et efficace pour rechercher et remplacer du texte programmatiquement à travers le [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) classe.

Cet exemple montre comment trouver toutes les occurrences d'une phrase spécifique (dans ce cas, "Black cat") et les remplacer par une nouvelle phrase ("White dog") dans l'ensemble d'un document PDF.

1. Spécifiez les expressions de recherche et de remplacement. Définissez le texte que vous souhaitez trouver et le texte par lequel vous souhaitez le remplacer.
1. Chargez le document PDF.
1. Créez un Text Absorber. Un TextFragmentAbsorber est initialisé avec la phrase de recherche. Il parcourt le document à la recherche de toutes les occurrences de la phrase donnée.
1. Appliquer l'Absorber à toutes les pages. Cela parcourt toutes les pages et collecte les fragments de texte correspondant à la phrase.
1. Remplacez chaque fragment trouvé. Chaque instance de "Black cat" doit être modifiée en "White dog".
1. Enregistrez le PDF mis à jour.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_on_all_pages(infile, outfile):
    search_phrase = "PDF"
    replace_phrase = "pdf"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Remplacer le texte dans une zone de page spécifique

Parfois, vous pouvez avoir besoin de remplacer du texte uniquement dans une zone spécifique d'une page PDF au lieu de rechercher dans tout le document — par exemple, mettre à jour un en‑tête, un pied de page ou une cellule de tableau à une position connue.

La bibliothèque Aspose.PDF for Python via .NET permet cette fonctionnalité en utilisant le [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) en conjonction avec la recherche de texte basée sur la région.

Cet exemple montre comment trouver et remplacer toutes les occurrences d’une phrase cible dans une région rectangulaire définie sur une page spécifique.

1. Spécifiez les phrases de recherche et de remplacement.
1. Chargez le document PDF.
1. Créer un Text Absorber pour la recherche. Initialiser un TextFragmentAbsorber pour trouver le texte souhaité.
1. Restreindre la zone de recherche. Le rectangle spécifie les limites des coordonnées x et y sur la page.
1. Appliquer l'Absorber à une page spécifique. Cela effectue la recherche et collecte les fragments de texte correspondants dans la zone spécifiée.
1. Remplacez le texte trouvé. Chaque occurrence de \u0027doc\u0027 dans la région définie devient \u0027DOC\u0027.
1. Enregistrez le PDF mis à jour.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_in_particular_page_region(infile, outfile):
    search_phrase = "doc"
    replace_phrase = "DOC"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        absorber.text_search_options.limit_to_page_bounds = True
        absorber.text_search_options.rectangle = ap.Rectangle(300, 442, 500, 742, True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### Redimensionner et déplacer le texte sans changer la taille de la police

Lors du remplacement de texte dans un PDF, il arrive parfois de vouloir ajuster ou repositionner le nouveau texte dans une zone spécifique sans modifier la taille de la police.
Aspose.PDF for Python via .NET offre des options pour ajuster la mise en page du texte et l'espacement tout en conservant la taille de police originale.

1. Chargez le document PDF.
1. Collectez tous les fragments de texte sur la page en utilisant un 'TextFragmentAbsorber'.
1. Sélectionnez le fragment à modifier.
1. Déplacer et redimensionner le rectangle de texte.
1. Ajuster l'espacement du texte. Activer l'ajustement de l'espacement pour faire tenir le texte dans le rectangle modifié.
1. Remplacez le texte du fragment.
1. Enregistrez le PDF mis à jour.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = fragment.rectangle
        rect.llx += 50
        rect.urx -= 50
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Redimensionner et déplacer un paragraphe dans le PDF

Lorsque vous travaillez avec des PDF, il arrive parfois de devoir remplacer ou développer un paragraphe tout en le maintenant visuellement aligné avec la mise en page de la page. Aspose.PDF vous permet de redimensionner le rectangle englobant du paragraphe et d’ajuster l’espacement pour faire tenir le nouveau texte, le tout sans modifier la taille de la police.

1. Chargez le document PDF.
1. Utilisez 'TextFragmentAbsorber' pour collecter tous les fragments de texte sur la page.
1. Sélectionnez le fragment à modifier.
1. Redimensionner et décaler le paragraphe. Utilisez la boîte média de la page pour déterminer les limites et ajuster le rectangle.
1. Ajuster l'espacement. Cela modifie l'espacement entre les mots/lettres au lieu de changer la taille de la police.
1. Remplacez le texte du fragment.
1. Enregistrez le PDF modifié.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = document.pages[1].media_box
        rect.llx += 20
        rect.urx -= 20
        rect.ury -= 20
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Remplacer le texte et agrandir automatiquement la police pour remplir la zone cible

Remplacer le texte dans un PDF tout en redimensionnant automatiquement et en agrandissant la police pour remplir une zone rectangulaire spécifique. En utilisant la bibliothèque Aspose.PDF for Python via .NET, le code ajuste dynamiquement la taille de la police et l'espacement afin que le nouveau contenu texte s'adapte parfaitement à une boîte englobante définie — sans calculs manuels de police.

1. Chargez le PDF.
1. Capturer des fragments de texte.
1. Sélectionner un fragment spécifique.
1. Définir le rectangle cible.
1. Activer les options d’ajustement du texte.
1. Remplacer le texte.
1. Enregistrez le document.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_expand_font(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = ap.Rectangle(100, 300, 512, 692, True)
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SCALE_TO_FILL
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Remplacer le texte et l'ajuster dans un rectangle

Remplacez le texte d’un document PDF tout en veillant à ce que le nouveau contenu tienne dans la zone rectangulaire du texte original en réduisant automatiquement la taille de la police si nécessaire.

En utilisant la bibliothèque Aspose.PDF for Python via .NET, cette fonction ajuste dynamiquement la mise en page du texte et la taille de la Font, tout en préservant la structure du document et en évitant le débordement.

1. Créez un objet TextFragmentAbsorber pour extraire tous les fragments de texte de la première page.
1. Accéder à un fragment de texte spécifique.
1. Définir la zone de remplacement.
1. Configurez les options d'ajustement du texte. Définissez deux options de remplacement clés :
    - Ajustement de la taille de la police - 'SHRINK_TO_FIT' réduit automatiquement la taille de la police si le nouveau texte est trop long.
    - Ajustement d'espacement - 'ADJUST_SPACE_WIDTH' maintient l'espacement proportionnel.
1. Remplacer le Texte.
1. Enregistrez le PDF modifié.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = fragment.rectangle
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### Remplacer automatiquement le texte de l'espace réservé et réarranger la mise en page du PDF

Remplacez le texte de remplacement dans un PDF (p. ex., modèles ou formulaires) par des données réelles telles que des noms ou des informations sur l'entreprise.
Il ajuste automatiquement la mise en page pour s'adapter au nouveau texte tout en appliquant un formatage personnalisé (police, couleur, taille).

1. Importer et charger le PDF.
1. Créer un TextAbsorber pour le Placeholder.
1. Appliquer l'Absorber à toutes les pages.
1. Parcourir les fragments de texte trouvés.
1. Appliquer une mise en forme de texte personnalisée.
1. Enregistrez le document mis à jour.

```python
import sys
import aspose.pdf as ap
from os import path

def automatically_rearrange_page_contents(input_file, output_file):
    document = ap.Document(input_file)

    absorber = ap.text.TextFragmentAbsorber("[Long_placeholder_Long_placeholder]")
    document.pages.accept(absorber)

    for text_fragment in absorber.text_fragments:
        # text_fragment.text = "John Smith"
        text_fragment.text = "John Smith, South Development Studio"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Calibri")
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.foreground_color = ap.Color.navy

    # Save PDF document
    document.save(output_file)
```

### Remplacer le texte en fonction d’une expression régulière

Lorsque vous travaillez avec des documents PDF, il peut être nécessaire de remplacer du texte qui suit un modèle plutôt qu'une phrase spécifique — par exemple, des numéros de téléphone, des codes ou des formats de type date.

Aspose.PDF for Python via .NET vous permet d'effectuer de tels remplacements en utilisant des expressions régulières (regex) avec la classe TextFragmentAbsorber.

Cet exemple montre comment rechercher des motifs de texte (dans ce cas, tout texte correspondant au format ####-####, tel que 1234-5678) et les remplacer par une chaîne formatée 'ABC1-2XZY'. Il montre également comment personnaliser la police, la couleur et la taille du texte remplacé.

L'extrait de code suivant vous montre comment remplacer du texte en fonction d'une expression régulière.

1. Chargez le document PDF.
1. Créez un TextAbsorber basé sur les expressions régulières. Initialisez le TextFragmentAbsorber avec un motif d'expression régulière.
1. Activez le mode d'expression régulière. Le paramètre 'True' active le mode de recherche d'expression régulière.
1. Appliquez l'Absorber à une page. Cela analyse la page pour tous les fragments de texte qui correspondent au modèle regex défini.
1. Remplacez chaque correspondance par un nouveau texte et appliquez un style personnalisé.
1. Enregistrez le document modifié.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_based_on_regex(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(r"\d{4}-\d{4}")
        absorber.text_search_options = ap.text.TextSearchOptions(True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = "ABC1-2XZY"
            fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            fragment.text_state.font_size = 12
            fragment.text_state.foreground_color = ap.Color.blue
            fragment.text_state.background_color = ap.Color.light_green

        document.save(outfile)
```

## Remplacer les polices ou supprimer les polices inutilisées

### Remplacer les polices dans le fichier PDF existant

Occasionnellement, vous devez standardiser ou mettre à jour les polices dans un PDF — par exemple, remplacer une police obsolète ou propriétaire par une police plus accessible. La bibliothèque Aspose.PDF for Python via .NET vous permet de détecter et de remplacer les polices de manière programmatique, garantissant une typographie cohérente et une compatibilité du document.

Cet exemple montre comment remplacer toutes les occurrences d'une police spécifique (par ex., 'Arial-BoldMT') par une autre police (par ex., 'Verdana') dans un document PDF.

L'extrait de code suivant montre comment remplacer la police à l'intérieur du document PDF :

1. Ouvrez le document PDF.
1. Initialisez un TextFragmentAbsorber.
1. Utilisez l'Absorber pour extraire les fragments de texte de chaque page du document.
1. Identifier et remplacer les polices. Le script vérifie si la police actuelle d’un fragment est 'Arial-BoldMT'. Si c’est le cas, il la remplace par la police 'Verdana' en utilisant la méthode FontRepository.find_font().
1. Enregistrez le document modifié.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_fonts(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### Supprimer les polices inutilisées

Au fil du temps, les documents PDF peuvent accumuler des polices inutilisées ou incorporées qui augmentent la taille du fichier et ralentissent le traitement. Ces polices inutilisées restent souvent même après des modifications ou des remplacements de texte, en particulier lors du travail avec des PDF volumineux ou complexes.

La bibliothèque Aspose.PDF for Python via .NET offre un moyen efficace de supprimer ces polices redondantes à l'aide de la classe TextEditOptions. Cela non seulement optimise votre document, mais garantit également qu'il n'utilise que les polices réellement appliquées au texte visible.

La méthode 'remove_unused_fonts()' est une façon simple mais puissante d'optimiser les fichiers PDF en supprimant les données de police redondantes.

Cet exemple montre comment :

- Analyser un PDF à la recherche de polices inutilisées.
- Supprimez-les en toute sécurité.
- Réassigner les fragments de texte actifs à une police cohérente (par exemple, Times New Roman).

1. Ouvrez le document PDF.
1. Configurer les options de modification du texte. Cela indique au moteur d'éliminer toutes les polices incorporées qui ne sont pas actuellement utilisées dans le texte visible.
1. Créez un Text Absorber avec Options. Un TextFragmentAbsorber extrait des fragments de texte du document pour les modifier.
1. Réassigner une police standard. Une fois que l'absorbeur a collecté tous les fragments, parcourez-les et appliquez une police cohérente.
1. Enregistrez le PDF nettoyé.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_unused_fonts(input_file, output_file):
    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(
        ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS
    )

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )

    # Save the updated PDF document
    document.save(output_file)
```

## Supprimer tout le texte

### Supprimer le texte du PDF

Supprimez tout le texte d'un fichier PDF tout en conservant les images, les formes et les structures de mise en page intacts.
En utilisant TextFragmentAbsorber, le code parcourt efficacement l'ensemble du document et supprime chaque fragment de texte trouvé sur chaque page.

1. Chargez le document PDF.
1. Un objet TextFragmentAbsorber est créé pour détecter et gérer les fragments de texte dans le PDF.
1. Supprimer tout le contenu texte. La méthode 'absorber.remove_all_text()' supprime chaque élément texte du document chargé, en laissant les composants non textuels intacts.
1. Enregistrez le document mis à jour.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber1(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### Supprimer tout le texte d'une page spécifique

Supprimez tout le texte d'une seule page d'un document PDF à l'aide de la classe TextFragmentAbsorber dans Aspose.PDF.
Contrairement à la suppression de l’ensemble du document, cette méthode effectue un nettoyage de texte au niveau de la page, supprimant le texte uniquement de la page sélectionnée tout en laissant les autres pages intactes.

1. Chargez le fichier PDF.
1. Créer une instance de TextFragmentAbsorber.
1. Supprimer tout le texte de la première page.
1. Enregistrez le PDF modifié.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber2(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### Supprimer tout le Texte d’une zone particulière sur la page PDF

Supprimez tout le texte d'une région rectangulaire spécifique sur une page en utilisant Aspose.PDF TextFragmentAbsorber.
Au lieu d'effacer une page entière, cette méthode effectue une suppression ciblée du texte, permettant un contrôle précis sur la partie de la page affectée.

1. Chargez le document PDF.
1. Créer un TextFragmentAbsorber.
1. Définir la zone cible (Rectangle).
1. Supprimer le texte de la région spécifiée.
1. Conserver le reste du document.
1. Enregistrez le PDF modifié.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber3(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(
            document.pages[1], ap.Rectangle(10, 200, 120, 600, True)
        )
        document.save(outfile)
```

### Supprimer tout le texte masqué d'un document PDF

Supprimez tout le texte d'une région rectangulaire spécifique sur une page en utilisant Aspose.PDF TextFragmentAbsorber.
Au lieu d'effacer une page entière, cette méthode effectue une suppression ciblée du texte, permettant un contrôle précis sur la partie de la page affectée.

1. Chargez le document PDF.
1. Créer un TextFragmentAbsorber.
1. Définir la zone cible (Rectangle).
1. Supprimer le texte de la région spécifiée.
1. Conserver le reste du document.
1. Enregistrez le PDF modifié.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_hidden_text(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(
            ap.text.TextReplaceOptions.ReplaceAdjustment.NONE
        )
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```

## Sujets de texte associés

- [Travailler avec du texte dans le PDF en utilisant Python](/pdf/fr/python-net/working-with-text/)
- [Ajout de texte au PDF](/pdf/fr/python-net/add-text-to-pdf-file/)
- [Rechercher et extraire le texte PDF en Python](/pdf/fr/python-net/search-and-get-text-from-pdf/)
- [Formater le texte PDF en Python](/pdf/fr/python-net/text-formatting-inside-pdf/)
