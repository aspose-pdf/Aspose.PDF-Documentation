---
title: Alterar senha do arquivo PDF
type: docs
weight: 10
url: /pt/python-net/change-password/
description: Altere as senhas de usuário e proprietário de um documento PDF seguro usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Atualizar senhas do PDF
Abstract: Saiba como alterar tanto as senhas de usuário quanto as de proprietário em um arquivo PDF seguro usando Aspose.PDF for Python via .NET. Este exemplo demonstra como atualizar de forma segura as credenciais de acesso mantendo a criptografia e as permissões existentes intactas.
---

## Alterar senha de usuário e do proprietário

Em muitos casos, pode ser necessário atualizar as senhas de um PDF protegido sem alterar sua configuração de segurança existente. Isso pode ser útil ao rotacionar credenciais, transferir a propriedade ou aprimorar a segurança do documento.

O método 'change_password' de [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) a classe permite:

- Atualize a senha do usuário (necessária para abrir o documento)
- Atualize a senha do proprietário (usada para controlar permissões)
- Mantenha as configurações atuais de criptografia e permissões

1. Crie um objeto 'PdfFileSecurity'.
1. Vincule o PDF de entrada.
1. Altere as senhas com o método 'change_password()'.
1. Salve o PDF atualizado.

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

## Alterar senha e redefinir segurança

Ao trabalhar com documentos PDF seguros, simplesmente alterar as senhas pode não ser suficiente. Você também pode precisar ajustar permissões, como impressão, cópia ou direitos de edição.

Aprenda como atualizar as senhas de usuário e de proprietário ao redefinir as configurações de segurança do PDF com Aspose.PDF for Python via .NET. Este exemplo mostra como redefinir as permissões do documento e a força da criptografia juntamente com novas credenciais de acesso.

1. Crie um objeto 'PdfFileSecurity'.
1. Vincule o PDF de entrada.
1. Crie um objeto 'DocumentPrivilege' e configure as ações permitidas.
1. Altere as senhas e redefina a segurança.
1. Salve o PDF atualizado.

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

## Tente Alterar Senha Sem Exceção

Em alguns fluxos de trabalho, especialmente em processamento em lote ou sistemas automatizados, é importante evitar exceções que possam interromper a execução. Em vez de lançar erros, você pode preferir uma operação segura que reporte sucesso ou falha.

O método 'try_change_password' da [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) classe fornece esta funcionalidade por:

1. Crie um objeto 'PdfFileSecurity'.
1. Carregue o documento PDF usando o método 'bind_pdf()'.
1. Tentativa de alterar senhas.
1. Verifique o resultado.
1. Salve o PDF atualizado.

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
