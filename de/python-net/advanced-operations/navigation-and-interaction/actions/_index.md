---
title: Arbeiten mit PDF-Aktionen in Python
linktitle: Aktionen
type: docs
weight: 20
url: /de/python-net/actions/
description: Erfahren Sie, wie Sie Dokument-, Seiten- und Form-Aktionen in PDF-Dateien mit Python hinzufügen, aktualisieren und entfernen.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Fügen Sie Dokument-, Seiten- und Form-Aktionen zu PDF-Dateien in Python hinzu.
Abstract: Dieser Artikel untersucht, wie man mit Aktionen in PDF-Dokumenten unter Verwendung der Aspose.PDF-Bibliothek arbeitet und dabei Interaktionen auf Dokumenten‑, Seiten‑ und Formularebene abdeckt. PDF‑Aktionen sind vordefinierte oder anpassbare Auslöser, die auf Benutzerereignisse reagieren und Navigation, JavaScript‑Ausführung, Multimedia‑Wiedergabe, Formularübermittlung und mehr ermöglichen. Die Anleitung zeigt, wie man Aktionen hinzufügt, anpasst und entfernt, beispielsweise das Öffnen von URLs bei Dokumentereignissen, das Erstellen von seiten­spezifischer Navigation oder Zoom‑Effekten, das Hinzufügen interaktiver Schaltflächen zum Drucken und Navigieren, das dynamische Ausblenden von Formularelementen und das Senden von Formulardaten an Web‑Endpunkte. Anhand ausführlicher Python‑Codebeispiele lernen die Leser, die Interaktivität von PDFs zu verbessern, Arbeitsabläufe zu optimieren und PDFs in externe Systeme zu integrieren, wobei sie die Kompatibilitätsaspekte von Viewern verstehen.
---

Aktionen in einem PDF sind vordefinierte Aufgaben, die durch Benutzerinteraktionen oder Dokumentereignisse ausgelöst werden. Sie können verwendet werden, um:

- Navigieren Sie zu einer bestimmten Seite oder einer externen Datei
- Öffne einen Weblink
- Multimedia-Inhalt abspielen
- JavaScript ausführen
- Formular senden oder zurücksetzen
- Felder anzeigen/ausblenden
- Zoomstufe oder Ansichtsmodus ändern

Fast alle Aktionen verwenden integrierte Parameter, aber es gibt einige, die angepasst werden können. Zum Beispiel - JavaScript-Aktionen.

## PDF-Startaktionen hinzufügen

Fügen Sie einem PDF-Dokument mithilfe von Python und Aspose.PDF JavaScript-basierte Startaktionen hinzu. Es weist Aktionen Schlüsselereignissen des Dokuments zu, wie dem Öffnen, Speichern und Drucken, sodass URLs automatisch gestartet werden können, wenn diese Ereignisse in unterstützten PDF‑Viewer auftreten.

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

## Aktionen aus PDF-Dokument entfernen

Um Aktionen zu bereinigen (oder zu entfernen), setzen Sie den Handler auf `None`.

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

## Hinzufügen von Aktionen zur Seite im PDF Document

Die ähnlichen Trigger werden für Seiten bereitgestellt: `on_open`, `on_close`.

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

## Aktionen in AcroForms

### Verwendung von Navigationsaktionen

Der PDF-Standard sieht eine bestimmte Menge benannter Aktionen vor. Die Bedeutung solcher Aktionen wird durch ihren Namen bestimmt.
Im folgenden Code verwenden wir Aktionen für die Navigation.

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

Dieser Code fügt jedem Seite eines PDF-Dokuments Navigationsschaltflächen hinzu, wodurch es für Benutzer einfacher wird, zwischen den Seiten zu wechseln. Er beginnt damit, die vollständigen Dateipfade für die Eingabe‑ und Ausgabedateien mithilfe einer Hilfsmethode zu bestimmen. Die Liste button_config definiert vier Arten von Navigationsschaltflächen—Erste Seite, Vorherige Seite, Nächste Seite und Letzte Seite—zusammen mit ihren horizontalen Positionen, den vordefinierten Navigationsaktionen, die sie auslösen, und einer Lambda‑Funktion, die bestimmt, ob jede Schaltfläche auf einer bestimmten Seite schreibgeschützt sein soll (zum Beispiel sind die Schaltflächen “Erste Seite” und “Vorherige Seite” auf der ersten Seite schreibgeschützt).

Der Code lädt dann das PDF und iteriert über jede Seite. Für jede Seite wird über die Button‑Konfigurationen geschleift, wobei für jeden Button ein rechteckiger Bereich erstellt und an dieser Stelle ein ButtonField instanziiert wird. Jeder Button erhält einen Namen, sein Nur‑Lese‑Status wird basierend auf der aktuellen Seite gesetzt, und seine Klick‑Aktion wird der entsprechenden Navigationsaktion zugewiesen. Der Button wird dann zu den PDF‑Formularfeldern hinzugefügt.

Nachdem alle Schaltflächen zu allen Seiten hinzugefügt wurden, wird das geänderte Dokument gespeichert. Wenn während dieses Vorgangs Fehler auftreten, werden sie abgefangen und ausgegeben. Dieser Ansatz stellt sicher, dass jede Seite über ein konsistentes Set von Navigationssteuerelementen verfügt, was die Benutzerfreundlichkeit von mehrseitigen PDFs verbessert. Eine Feinheit ist die Verwendung der is_readonly_fn Lambda, um Navigationsschaltflächen zu deaktivieren, wenn sie keinen Sinn ergeben würden (z. B. \"Next Page\" auf der letzten Seite), was dazu beiträgt, Benutzerverwirrung zu vermeiden.

### Druckaktionen verwenden

Bei der Verwendung von PDF-Formularen besteht häufig die Notwendigkeit, solche PDF-Dokumente zu drucken. Diese Aktion kann mit einem PDF-Reader durchgeführt werden, jedoch ist es manchmal praktischer, sie direkt aus dem Dokument über eine spezielle Schaltfläche auszuführen.

Tatsächlich ist dies ein weiteres Beispiel dafür, wie benannte Aktionen verwendet werden. Wir werden verwenden `PredefinedAction.FILE_PRINT` (Simulation der Verwendung des File‑>Print-Menüpunkts), aber Sie können auch verwenden `PredefinedAction.PRINT` oder `PredefinedAction.PRINT_DIALOG`, je nach Ihren eigenen Zwecken.

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

Dieses Code‑Snippet demonstriert, wie man einen „Print“-Button zur ersten Seite eines PDF‑Dokuments hinzufügt. Es beginnt mit dem Laden des PDFs vom angegebenen Eingabedateipfad und der Auswahl der ersten Seite (document.pages[1]).

Ein rechteckiger Bereich wird für die Position und Größe des Buttons auf der Seite definiert. Ein ButtonField wird dann an dieser Stelle erstellt, erhält den Namen „printButton“ und sein Anzeigewert wird auf „Print“ gesetzt. Der Button ist so konfiguriert, dass er, wenn er angeklickt wird (genauer gesagt, wenn die Maustaste losgelassen wird), die vordefinierte Aktion „Print File“ auslöst, wodurch der PDF‑Viewer aufgefordert wird, den Druckdialog zu öffnen.

Um das Aussehen der Schaltfläche zu verbessern, wird ein Rand erstellt und der Schaltfläche zugewiesen, wobei seine Breite auf 1 Einheit eingestellt wird. Die Schaltfläche wird dann zu den PDF-Formularfeldern auf der ersten Seite hinzugefügt. Schließlich wird das modifizierte Dokument am Ausgabepfad gespeichert. Dieser Ansatz bietet den Benutzern eine bequeme Möglichkeit, das Dokument direkt aus dem PDF zu drucken. Hinweis: Die Wirksamkeit dieser Funktion hängt von der Unterstützung des PDF-Viewers für interaktive Formularfelder und vordefinierte Aktionen ab.

### Verwenden der Hide-Aktion

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

Dieses Code‑Snippet fügt der ersten Seite eines PDFs einen Button hinzu, der beim Klicken alle Checkbox‑Felder im Dokument ausblendet. Es beginnt damit, die vollständigen Eingabe‑ und Ausgabepfade mithilfe einer Hilfsmethode zu ermitteln. Das PDF wird geladen und alle Checkbox‑Felder werden gesammelt, indem die Formularfelder nach Instanzen von `ap.CheckboxField`.

Ein rechteckiger Bereich wird für die Position des neuen Buttons nahe dem oberen Rand der Seite definiert. An dieser Stelle wird ein ButtonField erstellt, mit dem Namen "HideButton" und der Bezeichnung "Hide Checkboxes". Der Button ist so konfiguriert, dass er bei einem Klick (bei Loslassen der Maustaste) eine HideAction auslöst, die alle gesammelten Kontrollkästchen ausblendet.

Der Button wird dann zu den Formularfeldern auf der ersten Seite hinzugefügt, und das modifizierte PDF wird in die Ausgabedatei gespeichert. Wenn während dieses Vorgangs Fehler auftreten, werden sie abgefangen und ausgegeben. Diese Funktion bietet Benutzern eine Möglichkeit, alle Kontrollkästchen im PDF schnell auszublenden, was nützlich sein kann, um das Erscheinungsbild oder den Arbeitsablauf des Dokuments anzupassen.

### Anwenden der Sendeaktion

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

Diese Funktion fügt der ersten Seite eines PDF-Formulars einen "Submit"-Button hinzu, der es den Benutzern ermöglicht, die Formulardaten an einen angegebenen Web-Endpunkt zu senden. Sie beginnt damit, die vollständigen Pfade für die Eingabe- und Ausgabedateien zu erstellen, und lädt dann das Eingabe-PDF mithilfe der Aspose.PDF-Bibliothek.

A `SubmitFormAction` wird erstellt, um das Verhalten zu definieren, wenn die Schaltfläche angeklickt wird. Die URL der Aktion wird mit einem `FileSpecification` zeigt auf http://localhost:3000/submit, was bedeutet, dass die Formulardaten an diese URL gesendet werden. Die flags-Eigenschaft kombiniert `EXPORT_FORMAT` und `SUBMIT_COORDINATES`, wobei sichergestellt wird, dass die Formulardaten in einem Standardformat exportiert werden und die Koordinaten des Button-Klicks in der Übermittlung enthalten sind.

Ein rechteckiger Bereich wird für die Position und Größe der Schaltfläche auf der Seite definiert. Ein ButtonField wird an dieser Stelle auf der ersten Seite erstellt, mit dem Namen "SubmitButton," und sein Anzeigewert wird auf "Submit." gesetzt. Die Submit-Aktion wird dem Mausfreigabeereignis der Schaltfläche zugewiesen, sodass die Aktion ausgelöst wird, wenn der Benutzer die Schaltfläche anklickt.

Schließlich wird die Schaltfläche zu den Formularfeldern auf der ersten Seite hinzugefügt und das modifizierte PDF in der Ausgabedatei gespeichert. Wenn während dieses Vorgangs Fehler auftreten, werden sie abgefangen und ausgegeben. Dieser Ansatz bietet eine benutzerfreundliche Möglichkeit für PDF‑Benutzer, Formulardaten direkt an einen Server‑Endpunkt zu senden.

## Verwandte Navigationsthemen

- [Navigation und Interaktion in PDF mit Python](/pdf/de/python-net/navigation-and-interaction/)
- [Arbeiten mit Lesezeichen in PDF mit Python](/pdf/de/python-net/bookmarks/)
- [Links in PDF mit Python bearbeiten](/pdf/de/python-net/links/)
