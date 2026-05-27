---
title: Criptografar arquivo PDF
type: docs
weight: 30
url: /pt/python-net/encrypt-pdf-file/
description: Criptografe um documento PDF e configure permissões para controlar o que os usuários podem fazer com o arquivo.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criptografar PDF e controlar as ações do usuário
Abstract: Aprenda como criptografar um PDF enquanto define permissões específicas de usuário usando Aspose.PDF for Python via .NET. Este guia mostra como permitir ou restringir ações como impressão e cópia, mantendo o documento seguro.
---

## Criptografar PDF com senha de usuário e senha de proprietário

Proteger documentos PDF é essencial ao compartilhar conteúdo sensível ou restrito. A criptografia permite proteger um documento com senhas e definir quais ações os usuários podem executar. Este trecho de código mostra como aplicar senhas de usuário e de proprietário juntamente com permissões de acesso para proteger um arquivo PDF.

1. Criar um objeto PdfFileSecurity.
1. Vincule o PDF de entrada.
1. Definir privilégios do Document.
1. Criptografar o PDF.
1. Salvar o PDF criptografado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with User and Owner Password
def encrypt_pdf_with_user_owner_password(infile, outfile):
    """Encrypt a PDF document using user and owner passwords."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define document privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## Criptografar PDF com Permissões

O próximo trecho de código explica como permitir ações selecionadas, como impressão e cópia, enquanto restringe outras.

1. Inicializar o [PdfFileSecurity](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesecurity/) classe.
1. Vincular o PDF de entrada.
1. Configurar privilégios do Document.
1. Chamar o método 'encrypt_file()'.
1. Salvar o PDF criptografado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with Permissions
def encrypt_pdf_with_permissions(infile, outfile):
    """Encrypt a PDF document and configure specific permissions."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Configure privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True
    privilege.allow_copy = True

    # Encrypt the PDF
    file_security.encrypt_file(
        "user_password", "owner_password", privilege, pdf_facades.KeySize.X128
    )

    # Save encrypted PDF
    file_security.save(outfile)
```

## Criptografar PDF com Algoritmo de Criptografia

A criptografia de PDF não apenas protege documentos com senhas, mas também permite escolher o algoritmo de criptografia e a força. Selecionar o algoritmo apropriado garante segurança mais forte para documentos confidenciais.

1. Criar um objeto PdfFileSecurity.
1. Vincular o PDF de entrada.
1. Definir privilégios do Document.
1. Criptografar o PDF com Algoritmo.
1. Salvar o PDF criptografado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Encrypt PDF with Encryption Algorithm
def encrypt_pdf_with_encryption_algorithm(infile, outfile):
    """Encrypt a PDF document using a specific encryption algorithm."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Define privileges
    privilege = pdf_facades.DocumentPrivilege.forbid_all
    privilege.allow_print = True

    # Encrypt the PDF using AES algorithm
    file_security.encrypt_file(
        "user_password",
        "owner_password",
        privilege,
        pdf_facades.KeySize.X256,
        pdf_facades.Algorithm.AES,
    )

    # Save encrypted PDF
    file_security.save(outfile)
```
