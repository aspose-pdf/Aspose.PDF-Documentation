---
title: Set Privileges on an Existing PDF File
type: docs
weight: 40
url: /python-net/set-privileges/
description: Set and manage PDF document privileges to control user actions such as printing, copying, and editing.
lastmod: "2026-03-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Manage PDF Permissions and Access Controls
Abstract: Learn how to control what users can do with a PDF by setting document privileges using Aspose.PDF for Python via .NET. This guide covers applying permissions with or without passwords to restrict actions such as printing, copying, or editing.    
---

## Set PDF Privileges Without Passwords

Check how to apply document privileges to a PDF without specifying user or owner passwords using Aspose.PDF for Python via .NET. This code snippet shows how to control allowed actions while keeping the document accessible.

1. Create a 'PdfFileSecurity' Object.
1. Bind the input PDF.
1. Define Document privileges.
1. Call the 'set_privilege()' method without passing passwords.
1. Save the updated PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Set PDF Privileges Without Passwords
def set_pdf_privileges_without_passwords(infile, outfile):
    """Set PDF privileges without specifying user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Apply privileges (owner password will be generated automatically)
    file_security.set_privilege(privilege)

    # Save updated PDF
    file_security.save(outfile)
```

## Set PDF Privileges with User and Owner Passwords

To fully secure a PDF document, you often need both access control (passwords) and usage restrictions (permissions). By combining these, you can ensure that only authorized users can open the document and perform specific actions.

Using the set_privilege method with password parameters, you can:

- Protect the document with a user password
- Define an owner password for full control
- Configure allowed and restricted actions
- Enforce document-level security policies

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Set PDF Privileges with User and Owner Passwords
def set_pdf_privileges_with_passwords(infile, outfile):
    """Set PDF privileges using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = False

    # Apply privileges with passwords
    file_security.set_privilege("user_password", "owner_password", privilege)

    # Save updated PDF
    file_security.save(outfile)
```

## Try Set PDF Privileges Without Exception

This code snippet explains how to control access and restrict actions such as copying while allowing others like printing.

1. Create a 'PdfFileSecurity' object.
1. Load the source PDF using the 'bind_pdf()' method.
1. Define Document privileges.
1. Apply Privileges with Passwords.
1. Save the updated PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Set PDF Privileges Without Exception
def try_set_pdf_privileges_without_exception(infile, outfile):
    """Attempt to set PDF privileges without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Attempt to apply privileges
    result = file_security.try_set_privilege(
        "user_password", "owner_password", privilege
    )

    # Save only if operation succeeded
    if result:
        file_security.save(outfile)
    else:
        print("Setting privileges failed. Check passwords or document state.")
```
