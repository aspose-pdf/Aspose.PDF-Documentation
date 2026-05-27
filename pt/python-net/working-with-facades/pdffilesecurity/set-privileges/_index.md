---
title: Definir privilégios em um arquivo PDF existente
type: docs
weight: 40
url: /pt/python-net/set-privileges/
description: Defina e gerencie privilégios de documentos PDF para controlar ações do usuário, como impressão, cópia e edição.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Gerenciar permissões e controles de acesso de PDF
Abstract: Aprenda como controlar o que os usuários podem fazer com um PDF definindo privilégios de documento usando Aspose.PDF for Python via .NET. Este guia aborda a aplicação de permissões com ou sem senhas para restringir ações como impressão, cópia ou edição.
---

## Definir privilégios de PDF sem senhas

Verifique como aplicar privilégios de documento a um PDF sem especificar senhas de usuário ou proprietário usando Aspose.PDF for Python via .NET. Este trecho de código mostra como controlar as ações permitidas mantendo o documento acessível.

1. Criar um 'PdfFileSecurity' Objeto.
1. Vincule o PDF de entrada.
1. Definir privilégios de Document.
1. Chame o método 'set_privilege()' sem passar senhas.
1. Salve o PDF atualizado.

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

## Definir privilégios de PDF com senhas de usuário e proprietário

Para proteger totalmente um documento PDF, muitas vezes você precisa tanto de controle de acesso (senhas) quanto de restrições de uso (permissões). Ao combinar esses recursos, você pode garantir que apenas usuários autorizados abram o documento e realizem ações específicas.

Usando o método set_privilege com parâmetros de senha, você pode:

- Proteja o documento com uma senha de usuário
- Defina uma senha de proprietário para controle total
- Configure ações permitidas e restritas
- Aplique políticas de segurança ao nível do documento

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

## Tente definir privilégios de PDF sem exceção

Este trecho de código explica como controlar o acesso e restringir ações como copiar, permitindo outras como imprimir.

1. Crie um objeto 'PdfFileSecurity'.
1. Carregue o PDF de origem usando o método 'bind_pdf()'.
1. Definir privilégios de Document.
1. Aplicar privilégios com senhas.
1. Salve o PDF atualizado.

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
