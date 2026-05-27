---
title: Travailler avec les actions PDF en Python
linktitle: Actions
type: docs
weight: 20
url: /fr/python-net/actions/
description: Apprenez comment ajouter, mettre à jour et supprimer les actions de document, de page et de formulaire dans les fichiers PDF à l'aide de Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Ajoutez des actions de document, de page et de formulaire aux fichiers PDF en Python.
Abstract: Cet article explore comment travailler avec les actions dans les documents PDF en utilisant la bibliothèque Aspose.PDF, couvrant les interactions au niveau du document, de la page et du formulaire. Les actions PDF sont des déclencheurs prédéfinis ou personnalisables qui répondent aux événements utilisateur, permettant la navigation, l'exécution de JavaScript, la lecture multimédia, la soumission de formulaires, et plus encore. Le guide montre comment ajouter, personnaliser et supprimer des actions, comme l'ouverture d'URL lors d'événements du document, la création de navigation ou d'effets de zoom spécifiques à une page, l'ajout de boutons interactifs pour l'impression et la navigation, le masquage dynamique des éléments du formulaire, et la soumission des données de formulaire à des points de terminaison Web. Grâce à des exemples de code Python détaillés, les lecteurs apprennent à améliorer l'interactivité des PDF, à rationaliser les flux de travail et à intégrer les PDF avec des systèmes externes tout en comprenant les considérations de compatibilité des visionneuses.
---

Les actions dans un PDF sont des tâches prédéfinies qui sont déclenchées par l'interaction de l'utilisateur ou les événements du document. Elles peuvent être utilisées pour :

- Naviguer vers une page spécifique ou un fichier externe
- Ouvrir un lien web
- Lire le contenu multimédia
- Exécuter JavaScript
- Soumettre ou réinitialiser un formulaire
- Afficher/masquer les champs
- Modifier le niveau de zoom ou le mode d'affichage

La plupart des actions utilisent des paramètres intégrés, mais il en existe certains qui peuvent être personnalisés. Par exemple - les actions JavaScript.

## Ajouter des actions de lancement PDF

Ajoutez des actions de lancement basées sur JavaScript à un document PDF à l'aide de Python et d'Aspose.PDF. Cela attribue des actions aux principaux événements du document tels que l'ouverture, l'enregistrement et l'impression, permettant le lancement automatique d'URL lorsque ces événements se produisent dans les visionneuses PDF prises en charge.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_launch_actions(infile, outfile):
    """Add JavaScript launch actions for document events.

    Adds JavaScript actions that launch URLs when specific document events occur:
    - On document open: launches http://localhost:3000/open
    - Before saving: launches http://localhost:3000/save
    - Before printing: launches http://localhost:3000/print

    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to save the output PDF with document actions.

    Returns:
        None

    Example:
        >>> add_launch_actions("sample_data/input/add_launch_actions_in.pdf", "sample_data/output/add_launch_actions_out.pdf")

    Notes:
        - Uses `ap.annotations.JavascriptAction` with `app.launchURL()`.
        - URLs are opened in the default browser depending on viewer support.
    """

    document = ap.Document(infile)

    # Add JavaScript actions for document events
    document.open_action = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/open');"
    )
    document.actions.before_saving = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/save');"
    )
    document.actions.before_printing = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/print');"
    )

    document.save(outfile)
```

## Suppression des actions du document PDF

Pour nettoyer (ou supprimer) des actions, il suffit de définir le gestionnaire sur `None`.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def remove_page_actions(infile, outfile):
    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]
    page.actions.remove_actions()

    document.save(outfile)
```

## Ajout d'actions à la page dans le Document PDF

Les déclencheurs similaires sont fournis pour les pages : `on_open`, `on_close`.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_page_actions(infile, outfile):
    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]

    # Add GoTo action on page open - navigate to top of page
    action = ap.annotations.GoToAction(page)
    action.destination = ap.annotations.XYZExplicitDestination(
        page, 0, page.page_info.height, 1
    )
    page.actions.on_open = action

    # Add JavaScript action on page close
    page.actions.on_close = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/page/3');"
    )

    document.save(outfile)
```

## Actions dans AcroForms

### Utilisation des actions de navigation

La norme PDF prévoit un certain ensemble d'actions nommées. La signification de ces actions est déterminée par leur nom.
Dans le code suivant, nous utiliserons des actions pour la navigation.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_navigation_buttons(infile, outfile):
    # Configuration for each navigation button
    button_config = [
        ("First Page", 10.0, PredefinedAction.FIRST_PAGE, lambda p, t: p == 1),
        ("Previous Page", 120.0, PredefinedAction.PREV_PAGE, lambda p, t: p == 1),
        ("Next Page", 230.0, PredefinedAction.NEXT_PAGE, lambda p, t: p == t),
        ("Last Page", 340.0, PredefinedAction.LAST_PAGE, lambda p, t: p == t),
    ]

    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Add navigation buttons to each page
    for page in document.pages:
        for name, x_pos, action, is_readonly_fn in button_config:
            # Create button rectangle
            rect = Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            # Disable button when not applicable
            button.read_only = is_readonly_fn(page.number, total_pages)
            button.actions.on_release_mouse_btn = NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

Ce code ajoute des boutons de navigation à chaque page d'un document PDF, facilitant ainsi le déplacement des utilisateurs entre les pages. Il commence par déterminer les chemins d'accès complets aux fichiers d'entrée et de sortie à l'aide d'une méthode d'assistance. La liste button_config définit quatre types de boutons de navigation—First Page, Previous Page, Next Page, et Last Page—avec leurs positions horizontales, les actions de navigation prédéfinies qu'ils déclenchent, et une fonction lambda qui détermine si chaque bouton doit être en lecture seule sur une page donnée (par exemple, les boutons « First Page » et « Previous Page » sont en lecture seule sur la première page).

Le code charge ensuite le PDF et parcourt chaque page. Pour chaque page, il boucle sur les configurations de boutons, crée une zone rectangulaire pour chaque bouton et instancie un ButtonField à cet emplacement. Chaque bouton reçoit un nom, son statut en lecture seule est défini en fonction de la page actuelle, et son action de clic est attribuée à l'action de navigation correspondante. Le bouton est ensuite ajouté aux champs de formulaire du PDF.

Après que tous les boutons ont été ajoutés à toutes les pages, le document modifié est enregistré. Si des erreurs surviennent pendant ce processus, elles sont interceptées et affichées. Cette approche garantit que chaque page possède un ensemble cohérent de contrôles de navigation, améliorant la convivialité des PDF multi‑pages. Une subtilité réside dans l’utilisation de la lambda is_readonly_fn pour désactiver les boutons de navigation lorsqu’ils n’ont pas de sens (par exemple "Next Page" sur la dernière page), ce qui aide à prévenir la confusion des utilisateurs.

### Utilisation des actions d\'impression

Lors de l'utilisation de formulaires PDF, il est souvent nécessaire d'imprimer ces documents PDF. Cette action peut être effectuée à l'aide d'un lecteur PDF, mais il est parfois plus pratique de le faire directement depuis le document à l'aide d'un bouton spécial.

En fait, c’est encore un autre exemple d’utilisation d’actions nommées. Nous allons utiliser `PredefinedAction.FILE_PRINT` (en simulant l’utilisation de l’élément de menu File‑>Print), mais vous pouvez également l’utiliser `PredefinedAction.PRINT` ou `PredefinedAction.PRINT_DIALOG`, selon vos propres objectifs.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_named_action_print(infile, outfile):
    document = ap.Document(infile)
    page = document.pages[1]

    # Create print button with specific dimensions and position
    rect = Rectangle(10, 10, 100, 40, True)
    print_button = ButtonField(page, rect)
    print_button.partial_name = "printButton"
    print_button.value = "Print"
    print_button.actions.on_release_mouse_btn = NamedAction(PredefinedAction.FILE_PRINT)

    # Add border for better visibility
    border = ap.annotations.Border(print_button)
    border.width = 1
    print_button.border = border

    # Add button to the form on page 1
    document.form.add(print_button, 1)
    document.save(outfile)
```

Cet extrait de code montre comment ajouter un bouton "Print" à la première page d'un document PDF. Il commence par charger le PDF depuis le chemin de fichier d'entrée spécifié et sélectionne la première page (document.pages[1]).

Une zone rectangulaire est définie pour la position et la taille du bouton sur la page. Un ButtonField est ensuite créé à cet emplacement, nommé "printButton", et sa valeur d'affichage est définie sur "Print". Le bouton est configuré de sorte que lorsqu'il est cliqué (plus précisément, lorsque le bouton de la souris est relâché), il déclenche l'action prédéfinie "Print File", invitant le visualiseur PDF à ouvrir la boîte de dialogue d'impression.

Pour améliorer l'apparence du bouton, une bordure est créée et attribuée au bouton, avec une largeur fixée à 1 unité. Le bouton est ensuite ajouté aux champs de formulaire PDF sur la première page. Enfin, le document modifié est enregistré dans le chemin du fichier de sortie. Cette approche offre aux utilisateurs un moyen pratique d'imprimer le document directement depuis le PDF. Notez que l'efficacité de cette fonctionnalité dépend du support du visualiseur PDF pour les champs de formulaire interactifs et les actions prédéfinies.

### Utilisation de l'action Masquer

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_named_action_hide(infile, outfile):
    document = ap.Document(infile)
    # Collect all checkbox fields in the document
    checkboxes = [
        field for field in document.form if is_assignable(field, CheckboxField)
    ]

    # Create the hide button
    rect = Rectangle(10, 410, 140, 440, True)
    hide_button = ButtonField(document.pages[1], rect)
    hide_button.partial_name = "HideButton"
    hide_button.value = "Hide Checkboxes"

    # Add HideAction to button - will hide all checkboxes when clicked
    hide_button.actions.on_release_mouse_btn = HideAction(checkboxes, True)

    # Add button to the form on page 1
    document.form.add(hide_button, 1)

    # Save the modified PDF
    document.save(outfile)
```

Cet extrait de code ajoute un bouton à la première page d'un PDF qui, lorsqu'il est cliqué, masque tous les champs de case à cocher dans le document. Il commence par résoudre les chemins complets des fichiers d'entrée et de sortie à l'aide d'une méthode d'assistance. Le PDF est chargé, et tous les champs de case à cocher sont collectés en filtrant les champs du formulaire pour les instances de `ap.CheckboxField`.

Une zone rectangulaire est définie pour la position du nouveau bouton près du haut de la page. Un ButtonField est créé à cet emplacement, nommé "HideButton", et étiqueté "Hide Checkboxes". Le bouton est configuré de sorte que lorsqu'il est cliqué (au relâchement du bouton de la souris), il déclenche une HideAction qui masque toutes les cases à cocher collectées.

Le bouton est ensuite ajouté aux champs du formulaire sur la première page, et le PDF modifié est enregistré dans le fichier de sortie. Si des erreurs surviennent durant ce processus, elles sont capturées et affichées. Cette fonctionnalité offre aux utilisateurs un moyen de masquer rapidement toutes les cases à cocher dans le PDF, ce qui peut être utile pour personnaliser l’apparence ou le flux de travail du document.

### Appliquer l'action de soumission

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_submit_action(infile, outfile):
    document = ap.Document(infile)

    # Create the submit action
    submit_action = SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
    )

    # Create the submit button
    rect = Rectangle(10, 10, 100, 40, True)
    submit_button = ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    # Add the button to the form on page 1
    document.form.add(submit_button, 1)

    # Save the document
    document.save(outfile)
```

Cette fonction ajoute un bouton « Submit » à la première page d’un formulaire PDF, permettant aux utilisateurs de soumettre les données du formulaire à un point de terminaison Web spécifié. Elle commence par construire les chemins complets pour les fichiers PDF d’entrée et de sortie, puis charge le PDF d’entrée en utilisant la bibliothèque Aspose.PDF.

A `SubmitFormAction` est créé pour définir le comportement lorsque le bouton est cliqué. L'URL de l'action est définie en utilisant un `FileSpecification` pointant vers http://localhost:3000/submit, ce qui signifie que les données du formulaire seront envoyées à cette URL. La propriété flags combine `EXPORT_FORMAT` et `SUBMIT_COORDINATES`, en veillant à ce que les données du formulaire soient exportées dans un format standard et que les coordonnées du clic du bouton soient incluses dans la soumission.

Une zone rectangulaire est définie pour la position et la taille du bouton sur la page. Un ButtonField est créé à cet emplacement sur la première page, nommé "SubmitButton," et sa valeur d'affichage est définie sur "Submit." L'action de soumission est assignée à l'événement de relâchement de la souris du bouton, de sorte que l'action se déclenche lorsque l'utilisateur clique sur le bouton.

Enfin, le bouton est ajouté aux champs de formulaire de la première page, et le PDF modifié est enregistré dans le fichier de sortie. Si des erreurs surviennent pendant ce processus, elles sont capturées et affichées. Cette approche offre un moyen convivial pour les utilisateurs de PDF de soumettre les données du formulaire directement à un point de terminaison serveur.

## Sujets de navigation associés

- [Navigation et interaction dans le PDF avec Python](/pdf/fr/python-net/navigation-and-interaction/)
- [Travailler avec les signets dans le PDF en Python](/pdf/fr/python-net/bookmarks/)
- [Travailler avec les liens dans le PDF en Python](/pdf/fr/python-net/links/)
