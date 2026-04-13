---
title: Change Password of PDF File
type: docs
weight: 10
url: /python-net/change-password/
description: Change the user and owner passwords of a secured PDF document using Aspose.PDF for Python via .NET.
lastmod: "2026-03-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Update PDF Passwords 
Abstract: Learn how to change both user and owner passwords in a secured PDF file using Aspose.PDF for Python via .NET. This example demonstrates how to safely update access credentials while keeping the existing encryption and permissions intact.    
---

## Change User and Owner Password

In many cases, you might need to update the passwords of a protected PDF without changing its existing security setup. This can be helpful when rotating credentials, transferring ownership, or enhancing document security.

The 'change_password' method of the [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) class lets you:

- Update the user password (needed to open the document)
- Update the owner password (used to control permissions)
- Keep the current encryption and permission settings

1. Create a 'PdfFileSecurity' object.
1. Bind the input PDF.
1. Change passwords with 'change_password()' method.
1. Save the updated PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Change User and Owner Password
def change_user_and_owner_password(infile, outfile):
    """Change user and owner passwords while keeping existing security settings."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Change passwords
    file_security.change_password(
        "owner_password", "new_user_password", "new_owner_password"
    )

    # Save updated PDF
    file_security.save(outfile)
```

## Change Password and Reset Security

When working with secured PDF documents, simply changing passwords may not be enough. You might also need to adjust permissions, such as printing, copying, or editing rights.

Learn how to update user and owner passwords while resetting PDF security settings with Aspose.PDF for Python via .NET. This example shows how to redefine document permissions and encryption strength along with new access credentials.

1. Create a 'PdfFileSecurity' object.
1. Bind the input PDF.
1. Create a 'DocumentPrivilege' object and configure allowed actions.
1. Change passwords and reset security.
1. Save the updated PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Change Password and Reset Security
def change_password_and_reset_security(infile, outfile):
    """Change passwords and reset document security settings."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define new privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Change passwords and reset security
    file_security.change_password(
        "owner_password",
        "new_user_password",
        "new_owner_password",
        privilege,
        pdf_facades.KeySize.X128,
    )

    # Save updated PDF
    file_security.save(outfile)
```

## Try Change Password Without Exception

In some workflows, especially in batch processing or automated systems, it is important to avoid exceptions that may interrupt execution. Instead of throwing errors, you may prefer a safe operation that reports success or failure.

The 'try_change_password' method of the [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) class provides this functionality by:

1. Create a 'PdfFileSecurity' object.
1. Load the PDF document using the 'bind_pdf()' method.
1. Attempt to change passwords.
1. Check the result.
1. Save the updated PDF.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir

# Try Change Password Without Exception
def try_change_password_without_exception(infile, outfile):
    """Attempt to change passwords without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Attempt to change passwords
    result = file_security.try_change_password(
        "owner_password", "new_user_password", "new_owner_password"
    )

    # Save only if operation succeeded
    if result:
        file_security.save(outfile)
    else:
        print("Password change failed. Check owner password or document security.")
```
