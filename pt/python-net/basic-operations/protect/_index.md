---
title: Proteger arquivos PDF em Python
linktitle: Criptografar e descriptografar arquivo PDF
type: docs
weight: 70
url: /pt/python-net/protect-pdf-file/
description: Aprenda a criptografar arquivos, descriptografar PDFs protegidos e alterar senhas em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Definir permissões de PDF e gerenciar criptografia em Python
Abstract: Esta página explica como definir privilégios de documento, aplicar criptografia, descriptografar arquivos PDF e alterar senhas usando Aspose.PDF for Python via .NET. Ela cobre a configuração de senhas de usuário e proprietário, a definição de restrições de acesso (como impressão, cópia e edição) e o gerenciamento da segurança de PDF em aplicações Python.
---

## Criptografar PDF com senha e permissões

Use Aspose.PDF for Python via .NET para proteger um documento PDF com criptografia baseada em senha e permissões restritas.

1. Carregue o documento PDF.
1. Criar um `DocumentPrivilege` objeto de permissões.
1. Habilite as permissões necessárias.
1. Defina as senhas de usuário e proprietário.
1. Escolha o algoritmo de criptografia.
1. Aplicar criptografia ao documento.
1. Salvar o PDF criptografado.

```python
import aspose.pdf as ap

def encrypt_password(infile, outfile):
    """
    Encrypt PDF with password and permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_password("sample.pdf", "sample_protected.pdf")

    Note:
        Uses AES 128-bit encryption. Allows screen readers, forbids all other operations.
        User password: "userpassword", Owner password: "ownerpassword".
    """
    document = ap.Document(infile)
    document_privilege = ap.facades.DocumentPrivilege.forbid_all
    document_privilege.allow_screen_readers = True

    document.encrypt(
        "userpassword",
        "ownerpassword",
        document_privilege,
        ap.CryptoAlgorithm.AESx128,
        False,
    )
    document.save(outfile)
```

## Criptografar PDF com permissões totais

Criptografar um documento PDF permitindo permissões de acesso total usando Aspose.PDF for Python via .NET. Este exemplo usa criptografia RC4 de 128 bits para compatibilidade com visualizadores de PDF mais antigos.

1. Carregue o documento PDF.
1. Defina as senhas de usuário e de proprietário.
1. Defina permissões de acesso total.
1. Escolha o algoritmo de criptografia.
1. Chamada `encrypt()` com senhas, permissões e algoritmo.
1. Salvar o PDF criptografado.

```python
import aspose.pdf as ap

def encrypt_pdf_file(infile, outfile):
    """
    Encrypt PDF with full permissions.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        encrypt_pdf_file("sample.pdf", "sample_protected.pdf")

    Note:
        Uses RC4 128-bit encryption with allow_all privileges.
    """
    document = ap.Document(infile)
    document.encrypt(
        "userpassword",
        "ownerpassword",
        ap.facades.DocumentPrivilege.allow_all,
        ap.CryptoAlgorithm.RC4x128,
        False,
    )
    document.save(outfile)
```

## Descriptografar arquivo PDF usando senha do proprietário

Para remover a proteção por senha e restaurar o acesso total:

1. Carregue o PDF criptografado usando a senha correta (usuário ou proprietário).
1. Remova todas as proteções por senha e configurações de criptografia do documento.
1. Salve o PDF agora desprotegido no arquivo de saída especificado.

```python
import aspose.pdf as ap

def decrypt_pdf_file(infile, outfile):
    """
    Decrypt password-protected PDF.

    Args:
        infile (str): Input encrypted PDF filename
        outfile (str): Output decrypted PDF filename

    Returns:
        None

    Example:
        decrypt_pdf_file("sample_protected.pdf", "sample_unprotected.pdf")

    Note:
        Requires user password to open document.
    """
    document = ap.Document(infile, "userpassword")
    document.decrypt()
    document.save(outfile)
```

## Alterar senha de um arquivo PDF

Atualizar as credenciais de segurança (senhas de usuário e proprietário) de um documento PDF enquanto preserva seu conteúdo e estrutura.

1. Abra o PDF usando a senha de proprietário existente, que fornece acesso total às configurações de segurança.
1. Substitua as senhas antigas por uma nova senha de usuário e uma nova senha de proprietário.
1. Salve o PDF com as configurações de senha atualizadas.

```python
import aspose.pdf as ap

def change_password(infile, outfile):
    """
    Change user and owner passwords.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Returns:
        None

    Example:
        change_password("sample_protected.pdf", "sample_changepassword.pdf")

    Note:
        Changes from ownerpassword to newuser/newowner.
    """
    document = ap.Document(infile, "ownerpassword")
    document.change_passwords("ownerpassword", "newuser", "newowner")
    document.save(outfile)

```

## Determine a senha correta a partir do Array

Em alguns cenários, pode ser necessário identificar a senha correta a partir de uma lista de possíveis candidatas para acessar um PDF protegido. O trecho abaixo verifica se um arquivo PDF está criptografado e então tenta abri‑lo iterando por uma lista pré‑definida de senhas.

O processo inclui:

1. Usar `PdfFileInfo` para detectar se o PDF está criptografado.
1. Abra o PDF com cada senha usando `ap.Document()`.
1. Se for bem-sucedido, ele imprime o número de páginas.
1. Se não, ele captura a exceção e relata a senha falhada.

```python
import aspose.pdf as ap

def determine_correct_password_from_list(infile):
    """
    Test multiple passwords to find correct one.

    Args:
        infile (str): Input encrypted PDF filename

    Returns:
        None

    Example:
        determine_correct_password_from_list("sample_protected.pdf")

    Note:
        Tries passwords: test, test1, test2, test3, userpassword.
        Prints page count if password is correct.
    """
    info = ap.facades.PdfFileInfo(infile)
    print(f"File is password protected {info.is_encrypted}")

    passwords = "test", "test1", "test2", "test3", "userpassword"

    for password in passwords:
        try:
            document = ap.Document(infile, password)
            count = len(document.pages)
            if count > 0:
                print(f"Number of Page in document are = {count}")
        except RuntimeError as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
```
