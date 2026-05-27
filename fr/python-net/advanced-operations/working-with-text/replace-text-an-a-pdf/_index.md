---
title: Remplacer le texte dans le PDF avec Python
linktitle: Remplacer le texte dans le PDF
type: docs
weight: 40
url: /fr/python-net/replace-text-in-pdf/
description: Apprenez comment remplacer, réorganiser et supprimer du texte dans des documents PDF à l'aide de Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: Remplacez, supprimez et ajustez le contenu texte dans un PDF à l'aide de Python
Abstract: Cet article couvre les flux de travail pratiques de remplacement de texte dans les documents PDF utilisant Aspose.PDF for Python via .NET. Il comprend le remplacement de texte à travers les pages, la limitation du remplacement à des régions spécifiques, l'ajustement de la mise en page du texte lors du remplacement, le travail avec la correspondance basée sur les expressions régulières, le remplacement des polices, et la suppression du contenu texte lorsque nécessaire.
---

Ces exemples montrent comment **modifier ou supprimer du texte dans un PDF existant**.

Utilisez cette page lorsque vous devez mettre à jour les valeurs de texte, supprimer le contenu indésirable ou appliquer des règles de remplacement de texte sur les pages PDF.

## Remplacer le texte existant

### Remplacer le texte dans toutes les pages du document PDF

{{% alert color="primary" %}}

Vous pouvez essayer de trouver et remplacer le texte dans le document en utilisant Aspose.PDF et obtenir les résultats en ligne à cet endroit [lien](https://products.aspose.app/pdf/redaction)

{{% /alert %}}

Le remplacement de texte est une exigence courante lors de la mise à jour ou de la correction du contenu de documents PDF existants — par exemple, changer les noms de produits, corriger les fautes de frappe ou mettre à jour la terminologie sur plusieurs pages.

Aspose.PDF for Python via .NET offre une méthode puissante et efficace pour rechercher et remplacer du texte programmatiquement à travers le [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) classe.

Cet exemple montre comment trouver toutes les occurrences d'une phrase spécifique (dans ce cas, "Black cat") et les remplacer par une nouvelle phrase ("White dog") dans l’ensemble d’un document PDF complet.

1. Spécifiez les expressions de recherche et de remplacement. Définissez le texte que vous souhaitez trouver et le texte avec lequel vous souhaitez le remplacer.
1. Chargez le PDF Document.
1. Créez un Text Absorber. Un TextFragmentAbsorber est initialisé avec la phrase de recherche. Il parcourt le document à la recherche de toutes les occurrences de la phrase donnée.
1. Appliquer l'Absorber à toutes les pages. Cela parcourt toutes les pages et collecte les fragments de texte correspondant à la phrase.
1. Remplacez chaque fragment trouvé. Chaque occurrence de "Black cat" doit être remplacée par "White dog".
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

### Remplacer le texte dans une région particulière de la page

Parfois, vous pouvez avoir besoin de remplacer du texte uniquement dans une zone spécifique d’une page PDF au lieu de rechercher dans l’ensemble du document — par exemple, mettre à jour un en‑tête, un pied de page ou une cellule de tableau à une position connue.

La bibliothèque Aspose.PDF for Python via .NET active cette fonctionnalité en utilisant le [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) en conjonction avec la recherche de texte basée sur les régions.

Cet exemple montre comment rechercher et remplacer toutes les occurrences d’une phrase cible dans une région rectangulaire définie sur une page spécifique.

1. Spécifiez les expressions de recherche et de remplacement.
1. Chargez le PDF Document.
1. Créer un TextAbsorber pour la recherche. Initialiser un TextFragmentAbsorber afin de trouver le texte souhaité.
1. Restreindre la zone de recherche. Le rectangle spécifie les limites des coordonnées x et y sur la page.
1. Appliquer l'Absorber à une page spécifique. Cette opération effectue la recherche et collecte les fragments de texte correspondants dans la zone spécifiée.
1. Remplacez le texte trouvé. Chaque occurrence de 'doc' dans la région définie devient 'DOC'.
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
Aspose.PDF for Python via .NET propose des options pour ajuster la disposition et l'espacement du texte tout en conservant la taille de police d'origine.

1. Chargez le PDF Document.
1. Collectez tous les fragments de texte sur la page en utilisant un 'TextFragmentAbsorber'.
1. Sélectionnez le Fragment à modifier.
1. Déplacer et redimensionner le rectangle de texte.
1. Ajuster l'espacement du texte. Activer l'ajustement de l'espacement pour faire tenir le texte à l'intérieur du rectangle modifié.
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

Lorsque vous travaillez avec des PDF, il arrive parfois de devoir remplacer ou étendre un paragraphe tout en le maintenant visuellement aligné avec la mise en page de la page. Aspose.PDF vous permet de redimensionner le rectangle englobant du paragraphe et d’ajuster l’espacement pour faire tenir le nouveau texte, le tout sans modifier la taille de la police.

1. Chargez le PDF Document.
1. Utilisez 'TextFragmentAbsorber' pour collecter tous les fragments de texte sur la page.
1. Sélectionnez le Fragment à modifier.
1. Redimensionner et déplacer le paragraphe. Utilisez la boîte média de la page pour déterminer les limites et ajuster le rectangle.
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

Remplacez le texte dans un PDF tout en redimensionnant automatiquement et en élargissant la police pour remplir une zone rectangulaire spécifique. En utilisant la bibliothèque Aspose.PDF for Python via .NET, le code ajuste dynamiquement la taille de la police et l'espacement afin que le nouveau contenu texte s'adapte parfaitement à une boîte englobante définie — sans calculs manuels de police.

1. Chargez le PDF.
1. Capture des fragments de texte.
1. Sélectionner un fragment spécifique.
1. Définir le rectangle cible.
1. Activer les options d’ajustement du texte.
1. Remplacer le texte.
1. Enregistrez le Document.

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

Remplacez le texte dans un document PDF tout en vous assurant que le nouveau contenu tient dans la zone rectangulaire du texte original en réduisant automatiquement la taille de la police si nécessaire.

En utilisant la bibliothèque Aspose.PDF for Python via .NET, cette fonction ajuste dynamiquement la disposition du texte et la taille du Font, tout en préservant la structure du Document et en évitant le dépassement.

1. Créer un objet TextFragmentAbsorber pour extraire tous les fragments de texte de la première page.
1. Accéder à un fragment de texte spécifique.
1. Définir la zone de remplacement.
1. Configurez les options d'ajustement du texte. Définissez deux options de remplacement clés :
    - Ajustement de la taille de police - 'SHRINK_TO_FIT' réduit automatiquement la taille de la police si le nouveau texte est trop long.
    - Ajustement de l'espacement - 'ADJUST_SPACE_WIDTH' maintient l'espacement proportionnel.
1. Remplacez le texte.
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

### Remplacer automatiquement le texte d'espace réservé et réarranger la mise en page du PDF

Remplacez le texte de l'espace réservé à l'intérieur d'un PDF (p. ex., des modèles ou des formulaires) par des données réelles telles que des noms ou des informations d\'entreprise.
Il ajuste automatiquement la mise en page pour accueillir du nouveau texte tout en appliquant une mise en forme personnalisée (police, couleur, taille).

1. Importer et charger le PDF.
1. Créer un Text Absorber pour le Placeholder.
1. Appliquer l'Absorber à toutes les pages.
1. Parcourir les fragments de texte trouvés.
1. Appliquer le formatage de texte personnalisé.
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

### Remplacer le texte basé sur une expression régulière

Lorsque vous travaillez avec des documents PDF, il se peut que vous deviez remplacer du texte qui suit un modèle plutôt qu'une phrase spécifique — par exemple, des numéros de téléphone, des codes ou des formats similaires à des dates.

Aspose.PDF for Python via .NET vous permet d'effectuer de tels remplacements à l'aide d'expressions régulières (regex) avec la classe TextFragmentAbsorber.

Cet exemple montre comment trouver des motifs de texte (dans ce cas, tout texte correspondant au format ####-####, comme 1234-5678) et les remplacer par une chaîne formatée \u0027ABC1-2XZY\u0027. Il montre également comment personnaliser la police, la couleur et la taille du texte remplacé.

L'extrait de code suivant vous montre comment remplacer du texte en fonction d'une expression régulière.

1. Chargez le PDF Document.
1. Créer un Text Absorber basé sur les expressions régulières. Initialisez le TextFragmentAbsorber avec un modèle d'expression régulière.
1. Activer le mode d'expression régulière. Le paramètre \u0027True\u0027 active le mode de recherche d'expression régulière.
1. Appliquez l'Absorber à une Page. Cela analyse la page pour tous les fragments de texte qui correspondent au modèle regex défini.
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

Il arrive parfois que vous deviez standardiser ou mettre à jour les polices d'un PDF — par exemple, remplacer une police obsolète ou propriétaire par une police plus accessible. La bibliothèque Aspose.PDF for Python via .NET vous permet de détecter et de remplacer les polices de manière programmatique, garantissant une typographie cohérente et une compatibilité du document.

Cet exemple montre comment remplacer toutes les occurrences d’une police spécifique (par exemple, 'Arial-BoldMT') par une autre police (par exemple, 'Verdana') dans un document PDF.

L'extrait de code suivant montre comment remplacer la police dans le document PDF :

1. Ouvrez le Document PDF.
1. Initialisez un TextFragmentAbsorber.
1. Utilisez l'Absorber pour extraire les fragments de texte de chaque page du document.
1. Identifier et remplacer les polices. Le script vérifie si la police actuelle d'un fragment est 'Arial-BoldMT'. Si c'est le cas, il la remplace par la police 'Verdana' en utilisant la méthode FontRepository.find_font().
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

Au fil du temps, les documents PDF peuvent accumuler des polices inutilisées ou intégrées qui augmentent la taille du fichier et ralentissent le traitement. Ces polices inutilisées restent souvent même après des modifications ou remplacements de texte, en particulier lorsqu’on travaille avec des PDF volumineux ou complexes.

La bibliothèque Aspose.PDF for Python via .NET offre une méthode efficace pour supprimer ces polices redondantes en utilisant la classe TextEditOptions. Cela optimise non seulement votre document, mais garantit également qu'il n'utilise que les polices réellement appliquées au texte visible.

La méthode 'remove_unused_fonts()' est une façon simple mais puissante d'optimiser les fichiers PDF en supprimant les données de police redondantes.

Cet exemple montre comment :

- Scannez un PDF pour les polices inutilisées.
- Supprimez-les en toute sécurité.
- Réattribuer les fragments de texte actifs à une police cohérente (par exemple, Times New Roman).

1. Ouvrez le Document PDF.
1. Configurez les options d'édition de texte. Cela indique au moteur d'éliminer toutes les polices incorporées qui ne sont pas actuellement utilisées dans le texte visible.
1. Créer un TextAbsorber avec des options. Un TextFragmentAbsorber extrait des fragments de texte du document pour les modifier.
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

Supprimez tout le contenu texte d'un fichier PDF tout en conservant les images, les formes et les structures de mise en page intactes.
En utilisant TextFragmentAbsorber, le code analyse efficacement l'ensemble du document et supprime chaque fragment de texte trouvé sur chaque page.

1. Chargez le PDF Document.
1. Un objet TextFragmentAbsorber est créé pour détecter et gérer les fragments de texte dans le PDF.
1. Supprimer tout le contenu texte. La méthode ‘absorber.remove_all_text()’ supprime chaque élément texte du document chargé, laissant les composants non textuels intacts.
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

Supprimez tout le texte d'une seule page d'un document PDF en utilisant la classe TextFragmentAbsorber dans Aspose.PDF.
Contrairement à la suppression de l'ensemble du document, cette méthode effectue un nettoyage du texte au niveau de la page, supprimant le texte uniquement de la page choisie tout en laissant les autres pages intactes.

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

### Supprimer tout le texte d'une zone particulière sur la page PDF

Supprimez tout le texte d'une région rectangulaire spécifique sur une page en utilisant TextFragmentAbsorber d'Aspose.PDF.
Au lieu d'effacer une page entière, cette méthode effectue une suppression ciblée du texte, permettant un contrôle précis de la partie de la page qui est affectée.

1. Chargez le PDF Document.
1. Créer un TextFragmentAbsorber.
1. Définir la zone cible (Rectangle).
1. Supprimer le texte de la région spécifiée.
1. Conservez le reste du document.
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

### Supprimer tout le texte caché d'un document PDF

Supprimez tout le texte d'une région rectangulaire spécifique sur une page en utilisant TextFragmentAbsorber d'Aspose.PDF.
Au lieu d'effacer une page entière, cette méthode effectue une suppression ciblée du texte, permettant un contrôle précis de la partie de la page qui est affectée.

1. Chargez le PDF Document.
1. Créer un TextFragmentAbsorber.
1. Définir la zone cible (Rectangle).
1. Supprimer le texte de la région spécifiée.
1. Conservez le reste du document.
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

- [Travailler avec le texte dans le PDF en utilisant Python](/pdf/fr/python-net/working-with-text/)
- [Ajout de texte au PDF](/pdf/fr/python-net/add-text-to-pdf-file/)
- [Rechercher et extraire le texte PDF en Python](/pdf/fr/python-net/search-and-get-text-from-pdf/)
- [Formater le texte PDF en Python](/pdf/fr/python-net/text-formatting-inside-pdf/)
