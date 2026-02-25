---
title: Travailler avec les actions dans le document PDF
linktitle: Actions
type: docs
weight: 20
url: /fr/python-net/actions/
description: Explorez comment extraire et gérer les métadonnées PDF, telles que l'auteur et le titre, en Python avec Aspose.PDF.
lastmod: "2025-07-10"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Gestion des actions dans un document PDF avec Python
Abstract: Cet article explore comment travailler avec les actions dans les documents PDF en utilisant la bibliothèque Aspose.PDF, couvrant les interactions au niveau du document, de la page et du formulaire. Les actions PDF sont des déclencheurs prédéfinis ou personnalisables qui répondent aux événements utilisateur, permettant la navigation, l'exécution de JavaScript, la lecture multimédia, la soumission de formulaires, et plus encore. Le guide montre comment ajouter, personnaliser et supprimer des actions, telles que l'ouverture d'URL lors d'événements du document, la création de navigation ou d'effets de zoom spécifiques à une page, l'ajout de boutons interactifs pour l'impression et la navigation, la dissimulation dynamique d'éléments de formulaire, et la soumission de données de formulaire vers des points d'accès Web. Grâce à des exemples de code Python détaillés, les lecteurs apprennent à améliorer l'interactivité des PDF, à rationaliser les flux de travail et à intégrer les PDF avec des systèmes externes tout en comprenant les considérations de compatibilité des visionneuses.
---

Les actions dans un PDF sont des tâches prédéfinies qui sont déclenchées par l'interaction de l'utilisateur ou des événements du document. Elles peuvent être utilisées pour :

- Naviguer vers une page spécifique ou un fichier externe
- Ouvrir un lien web
- Lire du contenu multimédia
- Exécuter du JavaScript
- Soumettre ou réinitialiser un formulaire
- Afficher/masquer des champs
- Modifier le niveau de zoom ou le mode d'affichage

Presque toutes les actions utilisent des paramètres intégrés, mais certaines peuvent être personnalisées. Par exemple : les actions JavaScript.

## Actions au niveau du document

### Ajouter des actions au document PDF

Les documents PDF prennent en charge plusieurs actions au niveau du document, y compris du code qui s'exécute à l'ouverture du document ou en réponse à des événements spécifiques. Utilisez la propriété `open_action` pour les actions à l'ouverture ; les autres actions sont gérées dans la collection `actions`.

Considérons comment utiliser `open_action`.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.open_action = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/open');"
)
document.save(path_outfile)
```

Dans cet exemple, nous appelons la méthode `launchURL` de l'objet `app` et ouvrons un site web (à des fins de démonstration).

D'autres actions peuvent être ajoutées de la même manière, mais avec de légères modifications :

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.actions.before_saving = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/save');"
)
document.actions.before_printing = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/print');"
)
```

Vous pouvez ajouter des actions pour les événements suivants : `before_saving`, `before_printing`, `before_closing`, `after_saving`, `after_printing`.

Cet extrait de code montre comment attacher des actions JavaScript à divers événements au niveau du document dans un PDF. Tout d'abord, il charge un document PDF existant depuis le chemin de fichier d'entrée spécifié. La propriété `document.open_action` est définie sur une action JavaScript qui lance une URL lorsque le document est ouvert, incitant le visualiseur PDF à ouvrir `http://localhost:3000/open` dans le navigateur de l'utilisateur.

Ensuite, deux actions JavaScript supplémentaires sont assignées aux événements `before_saving` et `before_printing` du document. Ces actions se déclenchent lorsque l'utilisateur tente d'enregistrer ou d'imprimer le document, respectivement, chaque fois en lançant une URL différente (`/save` ou `/print`) dans le navigateur. Cela peut être utile pour suivre les interactions des utilisateurs ou pour s'intégrer à des flux de travail basés sur le web.

### Supprimer des actions du document PDF

Pour nettoyer (ou supprimer) les actions, il suffit de définir le gestionnaire sur `None`.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.open_action = None
document.actions.before_saving = None
document.actions.before_printing = None
document.save(path_outfile)
```

## Actions au niveau de la page

### Ajouter des actions à la page dans le document PDF

Des déclencheurs similaires sont fournis pour les pages : `on_open`, `on_close`.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_page_actions(self, infile, outfile):
    """
    Add actions to the third page of the PDF.

    Adds two actions to page 3:
    - On page open: Navigate to the top of the page with specific zoom
    - On page close: Launch a URL with page-specific information

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Raises:
        ValueError: If document has fewer than 3 pages

    Example:
        >>> actions.add_page_actions("multipage.pdf", "page_actions.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    document = ap.Document(path_infile)

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

    document.save(path_outfile)

```

Nous ajoutons deux actions à cette page. D'abord, elle crée une action "GoTo" qui se déclenche lorsque la page est ouverte. Cette action utilise une destination explicite pour se rendre au coin supérieur gauche de la page à un niveau de zoom spécifique. Ensuite, elle attache une action JavaScript qui s'exécute lorsque la page est fermée, indiquant au visualiseur PDF d'ouvrir une URL spécifique dans le navigateur. Enfin, le document modifié est enregistré au chemin de sortie spécifié.

Un point subtil à surveiller concerne l'indexation des pages, car l'utilisation d'un mauvais indice peut entraîner un comportement inattendu ou des erreurs. De plus, l'utilisation d'actions JavaScript dans les PDF n'est peut‑être pas prise en charge par tous les visionneuses PDF, de sorte que cette fonctionnalité peut ne pas fonctionner partout.

### Supprimer des actions d'une page PDF

Utilisez `remove_actions` pour supprimer l'action sur la page.

```python

import aspose.pdf as ap
from os import path

document = ap.Document(path_infile)

if len(document.pages) < 3:
    print("Error: The document does not have at least 3 pages.")
    return

page = document.pages[3]
page.actions.remove_actions()

document.save(path_outfile)

```

## Actions dans les AcroForms

### Utiliser les actions de navigation

La norme PDF prévoit un certain ensemble d'actions nommées. La signification de ces actions est déterminée par leur nom.
Dans le code suivant, nous utiliserons des actions pour la navigation.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_navigation_buttons(self, infile, outfile):
    """
    Add navigation buttons to each page of the PDF.

    Creates four navigation buttons on each page:
    - First Page: Navigate to the first page
    - Previous Page: Navigate to the previous page
    - Next Page: Navigate to the next page
    - Last Page: Navigate to the last page

    Buttons are automatically disabled when not applicable (e.g.,
    "Previous" is disabled on the first page).

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_navigation_buttons("multipage.pdf", "nav_buttons.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    # Configuration for each navigation button
    button_config = [
        ("First Page", 10.0, PredefinedAction.FIRST_PAGE, lambda p, t: p == 1),
        ("Previous Page", 120.0, PredefinedAction.PREV_PAGE, lambda p, t: p == 1),
        ("Next Page", 230.0, PredefinedAction.NEXT_PAGE, lambda p, t: p == t),
        ("Last Page", 340.0, PredefinedAction.LAST_PAGE, lambda p, t: p == t),
    ]

    try:
        document = ap.Document(path_infile)
        total_pages = len(document.pages)

        # Add navigation buttons to each page
        for page in document.pages:
            page_number = page.number

            for name, x_pos, action, is_readonly_fn in button_config:
                # Create button rectangle
                rect = Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
                button = ButtonField(page, rect)
                button.partial_name = name

                # Disable button when not applicable
                button.read_only = is_readonly_fn(page_number, total_pages)
                button.actions.on_release_mouse_btn = NamedAction(action)

                document.form.add(button)

        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding navigation buttons: {e}")

```

Ce code ajoute des boutons de navigation à chaque page d'un document PDF, facilitant le déplacement des utilisateurs entre les pages. Il commence par déterminer les chemins de fichier complets pour les fichiers d'entrée et de sortie à l'aide d'une méthode d'aide. La liste `button_config` définit quatre types de boutons de navigation — Première page, Page précédente, Page suivante et Dernière page — avec leurs positions horizontales, les actions de navigation prédéfinies qu'ils déclenchent, et une fonction lambda qui détermine si chaque bouton doit être en lecture seule sur une page donnée (par exemple, les boutons « Première page » et « Page précédente » sont en lecture seule sur la première page).

Le code charge ensuite le PDF et parcourt chaque page. Pour chaque page, il boucle à travers les configurations de boutons, crée une zone rectangulaire pour chaque bouton et instancie un `ButtonField` à cet emplacement. Chaque bouton reçoit un nom, son statut lecture seule est défini en fonction de la page actuelle, et son action de clic est assignée à l'action de navigation correspondante. Le bouton est ensuite ajouté aux champs de formulaire du PDF.

Après que tous les boutons ont été ajoutés à toutes les pages, le document modifié est enregistré. Si des erreurs surviennent pendant ce processus, elles sont capturées et affichées. Cette approche garantit que chaque page dispose d’un jeu cohérent de contrôles de navigation, améliorant la convivialité des PDF multipages. Un détail subtil est l’utilisation de la lambda `is_readonly_fn` pour désactiver les boutons de navigation lorsqu’ils n’auraient pas de sens (par ex., « Page suivante » sur la dernière page), ce qui aide à éviter la confusion de l'utilisateur.

### Utiliser les actions d'impression

Lors de l'utilisation de formulaires PDF, il est souvent nécessaire d'imprimer ces documents PDF. Cette action peut être réalisée à l'aide d'un lecteur PDF, mais il est parfois plus pratique de le faire directement depuis le document en utilisant un bouton spécial.

En fait, c'est un autre exemple d'utilisation des actions nommées. Nous utiliserons `PredefinedAction.FILE_PRINT` (simulant l'utilisation du menu Fichier → Imprimer), mais vous pouvez également utiliser `PredefinedAction.PRINT` ou `PredefinedAction.PRINT_DIALOG`, selon vos besoins.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_named_action_print(self, infile, outfile):
    """
    Add a print button to the first page of the PDF.

    Creates a button labeled "Print" that triggers the system print dialog
    when clicked. The button is positioned at the bottom-left corner of
    the first page with a 1-pixel border.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_named_action_print("input.pdf", "output.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    document = ap.Document(path_infile)
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
    document.save(path_outfile)

```

Cet extrait de code montre comment ajouter un bouton "Imprimer" à la première page d'un document PDF. Il commence par charger le PDF depuis le chemin de fichier d'entrée spécifié et sélectionner la première page (document.pages[1]).

Une zone rectangulaire est définie pour la position et la taille du bouton sur la page. Un ButtonField est alors créé à cet emplacement, nommé "printButton", et sa valeur d'affichage est définie sur "Imprimer". Le bouton est configuré de sorte que, lorsqu'il est cliqué (plus précisément, lorsque le bouton de la souris est relâché), il déclenche l'action prédéfinie "Print File", invitant le visualiseur PDF à ouvrir la boîte de dialogue d'impression.

Pour améliorer l'apparence du bouton, une bordure est créée et assignée au bouton, sa largeur étant réglée à 1 unité. Le bouton est ensuite ajouté aux champs de formulaire PDF de la première page. Enfin, le document modifié est enregistré sur le chemin de fichier de sortie. Cette approche offre aux utilisateurs un moyen pratique d'imprimer le document directement depuis le PDF. Notez que l'efficacité de cette fonction dépend du support du visualiseur PDF pour les champs de formulaire interactifs et les actions prédéfinies.

### Utilisation de l'action Masquer

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_named_action_hide(self, infile, outfile):
    """
    Add a hide button that toggles visibility of all checkbox fields.

    Creates a button labeled "Hide Checkboxes" that can hide or show
    all checkbox fields in the document. Useful for forms with many
    checkboxes that might clutter the interface.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_named_action_hide("form.pdf", "form_with_hide.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    try:
        document = ap.Document(path_infile)
        # Collect all checkbox fields in the document
        checkboxes = [field for field in document.form if isinstance(field, ap.CheckboxField)]

        # Create the hide button
        rect = Rectangle(10, 510, 100, 540)
        hide_button = ButtonField(document.pages[1], rect)
        hide_button.partial_name = "HideButton"
        hide_button.value = "Hide Checkboxes"

        # Add HideAction to button - will hide all checkboxes when clicked
        hide_button.actions.on_release_mouse_btn = ap.HideAction(checkboxes, True)

        # Add button to the form on page 1
        document.form.add(hide_button, 1)

        # Save the modified PDF
        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding hide button: {e}")

```

Cet extrait de code ajoute un bouton à la première page d'un PDF qui, lorsqu'il est cliqué, masque tous les champs de case à cocher du document. Il commence par résoudre les chemins complets des fichiers d'entrée et de sortie à l'aide d'une méthode d'assistance. Le PDF est chargé, et tous les champs de case à cocher sont récupérés en filtrant les champs de formulaire pour les instances de `ap.CheckboxField`.

Une zone rectangulaire est définie pour la position du nouveau bouton près du haut de la page. Un ButtonField est créé à cet endroit, nommé "HideButton", et intitulé "Masquer les cases à cocher". Le bouton est configuré de sorte que, lorsqu'il est cliqué (au relâchement du bouton de la souris), il déclenche une HideAction qui masque toutes les cases à cocher récupérées.

Le bouton est ensuite ajouté aux champs de formulaire de la première page, et le PDF modifié est enregistré dans le fichier de sortie. Si des erreurs surviennent pendant ce processus, elles sont interceptées et affichées. Cette fonction offre aux utilisateurs un moyen de masquer rapidement toutes les cases à cocher dans le PDF, ce qui peut être utile pour personnaliser l'apparence ou le flux de travail du document.

### Application de l'action Soumettre

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_submit_action(self, infile, outfile):
    """
    Submit form.

    Parameters:
    - infile (str): The name of the input PDF file.
    - outfile (str): The name of the output PDF file.
    """
    path_infile = self.dataDir + infile
    path_outfile = self.dataDir + outfile

    try:
        document = ap.Document(path_infile)

        # Create the submit action
        submit_action = ap.SubmitFormAction()
        submit_action.url = FileSpecification("http://localhost:3000/submit")
        submit_action.flags = (
            SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
        )

        # Create the submit button
        rect = Rectangle(10, 10, 100, 40)
        submit_button = ButtonField(document.pages[1], rect)
        submit_button.partial_name = "SubmitButton"
        submit_button.value = "Submit"
        submit_button.actions.on_release_mouse_btn = submit_action

        # Add the button to the form on page 1
        document.form.add(submit_button, 1)

        # Save the document
        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding submit button: {e}")

```

Cette fonction ajoute un bouton "Soumettre" à la première page d'un formulaire PDF, permettant aux utilisateurs d'envoyer les données du formulaire à un point de terminaison Web spécifié. Elle commence par construire les chemins complets des fichiers PDF d'entrée et de sortie, puis charge le PDF d'entrée à l'aide de la bibliothèque Aspose.PDF.

Un `SubmitFormAction` est créé pour définir le comportement lorsque le bouton est cliqué. L'URL de l'action est définie à l'aide d'un `FileSpecification` pointant vers http://localhost:3000/submit, ce qui signifie que les données du formulaire seront envoyées à cette URL. La propriété flags combine `EXPORT_FORMAT` et `SUBMIT_COORDINATES`, garantissant que les données du formulaire sont exportées dans un format standard et que les coordonnées du clic du bouton sont incluses dans la soumission.

Une zone rectangulaire est définie pour la position et la taille du bouton sur la page. Un ButtonField est créé à cet emplacement sur la première page, nommé "SubmitButton", et sa valeur d'affichage est définie sur "Soumettre". L'action de soumission est assignée à l'événement de relâchement de la souris du bouton, de sorte que l'action se déclenche lorsque l'utilisateur clique sur le bouton.

Enfin, le bouton est ajouté aux champs de formulaire de la première page, et le PDF modifié est enregistré dans le fichier de sortie. Si des erreurs surviennent pendant ce processus, elles sont interceptées et affichées. Cette approche offre aux utilisateurs de PDF un moyen convivial d'envoyer les données du formulaire directement à un point de terminaison serveur.

