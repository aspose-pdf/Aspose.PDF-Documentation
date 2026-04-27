---
title: Work with PDF Actions in Python
linktitle: Actions
type: docs
weight: 20
url: /python-net/actions/
description: Learn how to add, update, and remove document, page, and form actions in PDF files using Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Add document, page, and form actions to PDF files in Python
Abstract: This article explores how to work with actions in PDF documents using the Aspose.PDF library, covering document-level, page-level, and form-level interactions. PDF actions are predefined or customizable triggers that respond to user events, enabling navigation, JavaScript execution, multimedia playback, form submission, and more. The guide demonstrates how to add, customize, and remove actions, such as opening URLs on document events, creating page-specific navigation or zoom effects, adding interactive buttons for printing and navigation, hiding form elements dynamically, and submitting form data to web endpoints. Through detailed Python code examples, readers learn to enhance PDF interactivity, streamline workflows, and integrate PDFs with external systems while understanding viewer compatibility considerations.
---

Actions in a PDF are predefined tasks that get triggered by user interaction or document events. They can be used to:

- Navigate to a specific page or external file
- Open a web link
- Play multimedia content
- Run JavaScript
- Submit or reset a form
- Show/hide fields
- Change zoom level or view mode

Almost all actions use built-in parameters but there are some that can be customized. For example - JavaScript Actions.

## Add PDF Launch Actions

Add JavaScript-based launch actions to a PDF document using Python and Aspose.PDF. It assigns actions to key document events such as opening, saving, and printing, allowing URLs to be launched automatically when those events occur in supported PDF viewers.

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

## Removing Actions from PDF Document

To clean (or remove) actions just set handler to `None`.

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

## Adding Actions to the page in PDF Document

The similar triggers are provided for pages: `on_open`, `on_close`.

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

## Actions in AcroForms

### Using navigation actions

The PDF standard provides for a certain set of named actions. The meaning of such actions is determined by their name.
In the following code we will use actions for navigations.

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

This code adds navigation buttons to every page of a PDF document, making it easier for users to move between pages. It starts by determining the full file paths for the input and output files using a helper method. The button_config list defines four types of navigation buttons—First Page, Previous Page, Next Page, and Last Page—along with their horizontal positions, the predefined navigation actions they trigger, and a lambda function that determines if each button should be read-only on a given page (for example, the "First Page" and "Previous Page" buttons are read-only on the first page).

The code then loads the PDF and iterates through each page. For every page, it loops through the button configurations, creating a rectangular area for each button and instantiating a ButtonField at that location. Each button is given a name, its read-only status is set based on the current page, and its click action is assigned to the corresponding navigation action. The button is then added to the PDF form fields.

After all buttons are added to all pages, the modified document is saved. If any errors occur during this process, they are caught and printed. This approach ensures that every page has a consistent set of navigation controls, improving the usability of multi-page PDFs. One subtlety is the use of the is_readonly_fn lambda to disable navigation buttons when they would not make sense (e.g., "Next Page" on the last page), which helps prevent user confusion.

### Using print actions

When using PDF forms, there is often a need to print such PDF documents. This action can be performed using a PDF Reader, but it is sometimes more convenient to do it directly from the document using a special button.

In fact, this is yet another example of how to use named actions. We will use `PredefinedAction.FILE_PRINT` (simulating the use of the File->Print menu item), but you can also use `PredefinedAction.PRINT` or `PredefinedAction.PRINT_DIALOG`, depending on your own purposes.

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
This code snippet demonstrates how to add a "Print" button to the first page of a PDF document. It begins by loading the PDF from the specified input file path and selecting the first page (document.pages[1]).

A rectangular area is defined for the button's position and size on the page. A ButtonField is then created at this location, given the name "printButton," and its display value is set to "Print." The button is configured so that when it is clicked (specifically, when the mouse button is released), it triggers the predefined "Print File" action, prompting the PDF viewer to open the print dialog.

To enhance the button's appearance, a border is created and assigned to the button, with its width set to 1 unit. The button is then added to the PDF form fields on the first page. Finally, the modified document is saved to the output file path. This approach provides users with a convenient way to print the document directly from within the PDF. Note that the effectiveness of this feature depends on the PDF viewer's support for interactive form fields and predefined actions.

### Using Hide action

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

This code snippet adds a button to the first page of a PDF that, when clicked, hides all checkbox fields in the document. It starts by resolving the full input and output file paths using a helper method. The PDF is loaded, and all checkbox fields are collected by filtering the form fields for instances of `ap.CheckboxField`.

A rectangular area is defined for the new button's position near the top of the page. A ButtonField is created at this location, named "HideButton," and labeled "Hide Checkboxes." The button is configured so that when it is clicked (on mouse button release), it triggers a HideAction that hides all the collected checkboxes.

The button is then added to the form fields on the first page, and the modified PDF is saved to the output file. If any errors occur during this process, they are caught and printed. This feature provides users with a way to quickly hide all checkboxes in the PDF, which can be useful for customizing the document's appearance or workflow.

### Applying Submit Action

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

This function adds a "Submit" button to the first page of a PDF form, allowing users to submit the form data to a specified web endpoint. It begins by constructing the full paths for the input and output PDF files, then loads the input PDF using the Aspose.PDF library.

A `SubmitFormAction` is created to define the behavior when the button is clicked. The action's url is set using a `FileSpecification` pointing to http://localhost:3000/submit, which means the form data will be sent to this URL. The flags property combines `EXPORT_FORMAT` and `SUBMIT_COORDINATES`, ensuring that the form data is exported in a standard format and that the coordinates of the button click are included in the submission.

A rectangular area is defined for the button's position and size on the page. A ButtonField is created at this location on the first page, given the name "SubmitButton," and its display value is set to "Submit." The submit action is assigned to the button's mouse release event, so the action triggers when the user clicks the button.

Finally, the button is added to the form fields on the first page, and the modified PDF is saved to the output file. If any errors occur during this process, they are caught and printed. This approach provides a user-friendly way for PDF users to submit form data directly to a server endpoint.

## Related Navigation Topics

- [Navigation and interaction in PDF using Python](/pdf/python-net/navigation-and-interaction/)
- [Work with bookmarks in PDF using Python](/pdf/python-net/bookmarks/)
- [Work with links in PDF using Python](/pdf/python-net/links/)
