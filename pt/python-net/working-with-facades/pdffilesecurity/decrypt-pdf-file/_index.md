---
title: Descriptografar arquivo PDF
type: docs
weight: 20
url: /pt/python-net/decrypt-pdf-file/
description: Este guia explica como remover restrições como impressão, cópia e edição para obter acesso total ao seu documento PDF.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Remover proteção por senha de um PDF
Abstract: Este artigo demonstra como descriptografar um arquivo PDF usando uma senha de proprietário. Ele aborda o processo de remoção de restrições de segurança que limitam ações como impressão, edição ou cópia de conteúdo. Ao aplicar a senha de proprietário correta, os usuários podem desbloquear o documento e recuperar o controle total sobre sua funcionalidade.
---

## Descriptografar PDF com senha de proprietário

Descriptografar um documento PDF protegido por senha usando a senha de proprietário com Aspose.PDF for Python via .NET. Esta operação remove a criptografia e permite acesso irrestrito ao documento.

1. Crie um objeto 'PdfFileSecurity'.
1. Carregue o PDF criptografado usando o método 'bind_pdf()'.
1. Descriptografe o Document.
1. Salve o PDF descriptografado.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Decrypt PDF with Owner Password
def decrypt_pdf_with_owner_password(infile, outfile):
    """Decrypt a PDF document using the owner password."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Decrypt the PDF
    file_security.decrypt_file("owner_password")

    # Save decrypted PDF
    file_security.save(outfile)
```

## Tente descriptografar PDF sem exceção

Documentos PDF costumam ser protegidos com senhas para restringir o acesso e o uso. Para acessar ou modificar totalmente esses documentos, pode ser necessário remover a criptografia. Descriptografe um documento PDF protegido usando a senha do proprietário para remover a criptografia e restrições de acesso com Aspose.PDF for Python via .NET.

1. Crie um objeto 'PdfFileSecurity'.
1. Vincule o PDF de entrada.
1. Descriptografar o PDF.
1. Salvar o PDF de saída.

```python
from io import FileIO
import sys
from os import path
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Try Decrypt PDF Without Exception
def try_decrypt_pdf_without_exception(infile, outfile):
    """Attempt to decrypt a PDF without throwing an exception on failure."""
    # Create PdfFileSecurity object
    file_security = pdf_facades.PdfFileSecurity()

    # Bind PDF document
    file_security.bind_pdf(infile)

    # Attempt to decrypt the PDF
    result = file_security.try_decrypt_file("owner_password")

    # Save only if decryption was successful
    if result:
        file_security.save(outfile)
    else:
        print("Decryption failed. Check password or document security.")
```
