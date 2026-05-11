---
title: Cambiar la contraseña del archivo PDF
type: docs
weight: 10
url: /es/python-net/change-password/
description: Cambiar las contraseñas de usuario y propietario de un documento PDF protegido utilizando Aspose.PDF for Python via .NET.
lastmod: "2026-03-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Actualizar contraseñas de PDF
Abstract: Aprenda cómo cambiar tanto las contraseñas de usuario como de propietario en un archivo PDF protegido utilizando Aspose.PDF for Python via .NET. Este ejemplo muestra cómo actualizar de forma segura las credenciales de acceso mientras se mantiene el cifrado y los permisos existentes intactos.
---

## Cambiar contraseña de usuario y propietario

En muchos casos, es posible que necesite actualizar las contraseñas de un PDF protegido sin cambiar su configuración de seguridad actual. Esto puede ser útil al rotar credenciales, transferir la propiedad o mejorar la seguridad del documento.

El método \u0027change_password\u0027 de [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) la clase le permite:

- Actualizar la contraseña del usuario (necesaria para abrir el documento)
- Actualizar la contraseña del propietario (utilizada para controlar los permisos)
- Mantener la configuración actual de cifrado y permisos

1. Cree un objeto 'PdfFileSecurity'.
1. Vincular el PDF de entrada.
1. Cambie contraseñas con el método 'change_password()'.
1. Guarde el PDF actualizado.

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

## Cambiar la contraseña y restablecer la seguridad

Al trabajar con documentos PDF seguros, simplemente cambiar las contraseñas puede no ser suficiente. También puede ser necesario ajustar los permisos, como los de impresión, copia o edición.

Aprenda cómo actualizar las contraseñas de usuario y propietario mientras restablece la configuración de seguridad PDF con Aspose.PDF for Python via .NET. Este ejemplo muestra cómo redefinir los permisos del documento y la fuerza de cifrado junto con nuevas credenciales de acceso.

1. Cree un objeto 'PdfFileSecurity'.
1. Vincular el PDF de entrada.
1. Cree un objeto 'DocumentPrivilege' y configure las acciones permitidas.
1. Cambie las contraseñas y restablezca la seguridad.
1. Guarde el PDF actualizado.

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

## Intentar cambiar la contraseña sin excepción

En algunos flujos de trabajo, especialmente en procesamiento por lotes o sistemas automatizados, es importante evitar excepciones que puedan interrumpir la ejecución. En lugar de lanzar errores, puede preferir una operación segura que informe el éxito o el fracaso.

El método 'try_change_password' de [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) clase proporciona esta funcionalidad mediante:

1. Cree un objeto 'PdfFileSecurity'.
1. Cargue el documento PDF usando el método 'bind_pdf()'.
1. Intentar cambiar contraseñas.
1. Verificar el resultado.
1. Guarde el PDF actualizado.

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
