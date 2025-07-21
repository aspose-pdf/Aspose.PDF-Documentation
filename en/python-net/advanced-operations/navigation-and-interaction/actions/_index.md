---
title: Working with Actions in PDF document
linktitle: Working with Actions
type: docs
weight: 20
url: /python-net/actions/
description: Explore how to extract and manage PDF metadata, such as author and title, in Python using Aspose.PDF.
lastmod: "2025-07-10"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Dealing with Actions in PDF document using Python
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

## Document-Level Actions

### Adding Actions to PDF Document

PDF documents support several document-level actions, including code that runs on opening the document or in response to specific events. Use the `open_action` property for actions on open; other actions are managed in the `actions` collection.

Let’s consider how to use `open_action.`

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

In this example we call `launchURL` method from `app` obejct and open web site (for demo purposes).

Other actions can be added in the same way, but with minor changes:

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

You can add actions for the following events: `before_saving`, `before_printing`, `before_closing`, `after_saving`, `after_printing`.

This code snippet demonstrates how to attach JavaScript actions to various document-level events in a PDF. First, it loads an existing PDF document from the specified input file path. The `document.open_action` property is set to a JavaScript action that launches a URL when the document is opened, prompting the PDF viewer to open `http://localhost:3000/open` in the user's browser.

Next, two additional JavaScript actions are assigned to the document's `before_saving` and `before_printing` events. These actions trigger when the user attempts to save or print the document, respectively, each time launching a different URL (`/save` or `/print`) in the browser. This can be useful for tracking user interactions or integrating with web-based workflows.

### Removing Actions from PDF Document

To clean (or remove) actions just set handler to `None`.

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

## Page-Level Actions

### Adding Actions to the page in PDF Document

The similar triggers are provided for pages: `on_open`, `on_close`.

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

We add two actions to this page. First, it creates a "GoTo" action that triggers when the page is opened. This action uses an explicit destination to jump to the top-left corner of the page at a specific zoom level. Second, it attaches a JavaScript action that runs when the page is closed, instructing the PDF viewer to open a specific URL in the browser. Finally, the modified document is saved to the specified output path.

A subtle point to watch for is the page indexing, as using the wrong index could lead to unexpected behavior or errors. Additionally, the use of JavaScript actions in PDFs may not be supported by all PDF viewers, so this feature might not work everywhere.

### Removing Actions from PDF page

Use `remove_actions` to remove action on page.

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

## Actions in AcroForms

### Using navigation actions

The PDF standard provides for a certain set of named actions. The meaning of such actions is determined by their name.
In the following code we will use actions for navigations.

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

This code adds navigation buttons to every page of a PDF document, making it easier for users to move between pages. It starts by determining the full file paths for the input and output files using a helper method. The button_config list defines four types of navigation buttons—First Page, Previous Page, Next Page, and Last Page—along with their horizontal positions, the predefined navigation actions they trigger, and a lambda function that determines if each button should be read-only on a given page (for example, the "First Page" and "Previous Page" buttons are read-only on the first page).

The code then loads the PDF and iterates through each page. For every page, it loops through the button configurations, creating a rectangular area for each button and instantiating a ButtonField at that location. Each button is given a name, its read-only status is set based on the current page, and its click action is assigned to the corresponding navigation action. The button is then added to the PDF form fields.

After all buttons are added to all pages, the modified document is saved. If any errors occur during this process, they are caught and printed. This approach ensures that every page has a consistent set of navigation controls, improving the usability of multi-page PDFs. One subtlety is the use of the is_readonly_fn lambda to disable navigation buttons when they would not make sense (e.g., "Next Page" on the last page), which helps prevent user confusion.

### Using print actions

When using PDF forms, there is often a need to print such PDF documents. This action can be performed using a PDF Reader, but it is sometimes more convenient to do it directly from the document using a special button.

In fact, this is yet another example of how to use named actions. We will use `PredefinedAction.FILE_PRINT` (simulating the use of the File->Print menu item), but you can also use `PredefinedAction.PRINT` or `PredefinedAction.PRINT_DIALOG`, depending on your own purposes.

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

This code snippet demonstrates how to add a "Print" button to the first page of a PDF document. It begins by loading the PDF from the specified input file path and selecting the first page (document.pages[1]).

A rectangular area is defined for the button's position and size on the page. A ButtonField is then created at this location, given the name "printButton," and its display value is set to "Print." The button is configured so that when it is clicked (specifically, when the mouse button is released), it triggers the predefined "Print File" action, prompting the PDF viewer to open the print dialog.

To enhance the button's appearance, a border is created and assigned to the button, with its width set to 1 unit. The button is then added to the PDF form fields on the first page. Finally, the modified document is saved to the output file path. This approach provides users with a convenient way to print the document directly from within the PDF. Note that the effectiveness of this feature depends on the PDF viewer's support for interactive form fields and predefined actions.

### Using Hide action

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

This code snippet adds a button to the first page of a PDF that, when clicked, hides all checkbox fields in the document. It starts by resolving the full input and output file paths using a helper method. The PDF is loaded, and all checkbox fields are collected by filtering the form fields for instances of `ap.CheckboxField`.

A rectangular area is defined for the new button's position near the top of the page. A ButtonField is created at this location, named "HideButton," and labeled "Hide Checkboxes." The button is configured so that when it is clicked (on mouse button release), it triggers a HideAction that hides all the collected checkboxes.

The button is then added to the form fields on the first page, and the modified PDF is saved to the output file. If any errors occur during this process, they are caught and printed. This feature provides users with a way to quickly hide all checkboxes in the PDF, which can be useful for customizing the document's appearance or workflow.

### Appling Submit Action

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

This function adds a "Submit" button to the first page of a PDF form, allowing users to submit the form data to a specified web endpoint. It begins by constructing the full paths for the input and output PDF files, then loads the input PDF using the Aspose.PDF library.

A `SubmitFormAction` is created to define the behavior when the button is clicked. The action's url is set using a `FileSpecification` pointing to http://localhost:3000/submit, which means the form data will be sent to this URL. The flags property combines `EXPORT_FORMAT` and `SUBMIT_COORDINATES`, ensuring that the form data is exported in a standard format and that the coordinates of the button click are included in the submission.

A rectangular area is defined for the button's position and size on the page. A ButtonField is created at this location on the first page, given the name "SubmitButton," and its display value is set to "Submit." The submit action is assigned to the button's mouse release event, so the action triggers when the user clicks the button.

Finally, the button is added to the form fields on the first page, and the modified PDF is saved to the output file. If any errors occur during this process, they are caught and printed. This approach provides a user-friendly way for PDF users to submit form data directly to a server endpoint.
