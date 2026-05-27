---
title: Criptografar e Decifrar Arquivos PDF em Python
linktitle: Criptografar e Decifrar Arquivo PDF
type: docs
weight: 70
url: /pt/python-net/set-privileges-encrypt-and-decrypt-pdf-file/
description: Aprenda como definir privilégios de PDF, criptografar arquivos, descriptografar PDFs protegidos e alterar senhas em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Defina permissões de PDF e gerencie a criptografia em Python.
Abstract: Esta página de documentação explica como definir privilégios de documento, aplicar criptografia e descriptografar arquivos PDF usando Aspose.PDF para Python. Ela orienta os desenvolvedores sobre como configurar senhas de usuário e de proprietário, definir restrições de acesso (como impressão, cópia ou edição). Exemplos de código ilustram como proteger conteúdo sensível e gerenciar a segurança de PDF de forma eficaz em aplicações Python, garantindo acesso controlado e confidencialidade de dados.
---

Gerenciar a segurança de documentos é essencial ao trabalhar com conteúdo sensível ou crítico para os negócios. Aspose.PDF for Python via .NET fornece uma API robusta para aplicar criptografia programaticamente, controlar o acesso por meio de permissões e descriptografar arquivos PDF protegidos.

Este artigo orienta desenvolvedores Python através de exemplos práticos para definir privilégios, aplicar e remover criptografia, alterar senhas e detectar estados de proteção — tudo dentro de um fluxo de trabalho PDF.

Aspose.PDF for Python via .NET oferece aos desenvolvedores controle total sobre a segurança de PDF:

**Definir privilégios** - Controle de acesso refinado usando permissões.
**Criptografar Arquivo** - Aplicar criptografia AES ou RC4 com senhas personalizadas.
**Descriptografar Arquivo** - Remover a segurança usando a senha do proprietário.
**Alterar senhas** - Rotacione ou atualize credenciais sem alterar o conteúdo.
**Inspecionar Segurança** - Detectar o status de criptografia ou tipos de senha necessários.

Use esta página quando precisar proteger documentos PDF com senhas, restringir impressão ou cópia, girar credenciais ou verificar se um documento está criptografado.

## Definir privilégios em um arquivo PDF existente

Você pode restringir ou permitir operações específicas (por exemplo, impressão, cópia, preenchimento de formulários) atribuindo senhas de usuário e de proprietário juntamente com privilégios de acesso.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def set_privileges_on_existing_pdf_file(infile: str, outfile: str) -> None:
    """Set restricted privileges on an existing PDF document."""
    with ap.Document(infile) as document:
        document_privilege = ap.facades.DocumentPrivilege.forbid_all
        document_privilege.allow_screen_readers = True
        document.encrypt(
            "user",
            "owner",
            document_privilege,
            ap.CryptoAlgorithm.AESx128,
            False,
        )
        document.save(outfile)
```

## Criptografar arquivo PDF usando diferentes tipos e algoritmos de criptografia

Criptografar um PDF garante que somente usuários com credenciais válidas possam abrir ou modificar o arquivo.

>Termos-chave:

- Senha do usuário. Necessária para abrir o documento.

- Senha do proprietário. Necessária para alterar permissões ou remover a criptografia.

- Tamanho da Chave. Use AE_SX128 para máxima segurança em fluxos de trabalho modernos.

O trecho de código a seguir mostra como criptografar arquivos PDF.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def encrypt_pdf_file(infile: str, outfile: str) -> None:
    """Encrypt a PDF document with user and owner passwords."""
    with ap.Document(infile) as document:
        document.encrypt(
            "user",
            "owner",
            ap.Permissions.EXTRACT_CONTENT,
            ap.CryptoAlgorithm.AESx128,
        )
        document.save(outfile)
```

## Descriptografar arquivo PDF usando a senha do proprietário

Para remover a proteção por senha e restaurar o acesso total:

1. Carrega o PDF criptografado usando a senha correta ('password' é a senha de usuário ou de proprietário).
1. Remove toda a proteção por senha e as configurações de criptografia do documento.
1. Salva o PDF agora desprotegido no arquivo de saída especificado.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def decrypt_pdf_file(infile: str, outfile: str) -> None:
    """Decrypt a password-protected PDF document."""
    with ap.Document(infile, "password") as document:
        document.decrypt()
        document.save(outfile)
```

## Criptografar e descriptografar um PDF com certificados de chave pública

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def pub_sec_encryption(
    crypto_algorithm,
    pub_cert: str,
    in_pfx: str,
    outfile: str,
) -> None:
    """Demonstrate public-key encryption and decryption."""
    pfx_password = "12345"

    with ap.Document() as document:
        document.info.title = "TestTitle"
        document.info.author = "TestAuthor"
        page = document.pages.add()
        page.paragraphs.add(ap.text.TextFragment("Hello World!"))

        with open(pub_cert, "rb") as file_stream:
            byte_content = file_stream.read()

        document.encrypt(
            ap.Permissions.PRINT_DOCUMENT,
            crypto_algorithm,
            [byte_content],
        )
        document.save(outfile)

    with ap.Document(
        outfile,
        ap.security.CertificateEncryptionOptions(pub_cert, in_pfx, pfx_password),
    ) as document:
        print(document.info.title)
        print(document.info.author)

        text_absorber = ap.text.TextAbsorber()
        document.pages[1].accept(text_absorber)
        print(text_absorber.text)

        document.decrypt()
        document.save(path.join(path.dirname(outfile), "pubsec_decrypted_out.pdf"))
```

## Alterar senha de um arquivo PDF

Atualizar as credenciais de segurança (senhas de usuário e proprietário) de um documento PDF enquanto preserva seu conteúdo e estrutura.

1. Abre o PDF usando a senha de proprietário existente ('owner'), que fornece acesso total, incluindo permissão para alterar as configurações de segurança.
1. Substitui as senhas antigas por uma nova senha de usuário ('newuser') e uma nova senha de proprietário ('newowner').
1. Salva o PDF com as configurações de senha atualizadas.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def change_password(infile: str, outfile: str) -> None:
    """Change the passwords of a password-protected PDF document."""
    with ap.Document(infile, "owner") as document:
        document.change_passwords("owner", "newuser", "newowner")
        document.save(outfile)
```

## Como - determinar se o PDF de origem está protegido por senha

### Determinar a senha correta a partir de um Array

Em alguns cenários, pode ser necessário identificar a senha correta a partir de uma lista de candidatos potenciais para acessar um PDF protegido. O trecho de código abaixo demonstra como verificar se um arquivo PDF está protegido por senha e, em seguida, tentar desbloqueá‑lo iterando sobre uma lista predefinida de senhas usando Aspose.PDF for Python via .NET.

O processo inclui:

1. Usando PdfFileInfo para detectar se o PDF está criptografado.
1. Tenta abrir o PDF com cada senha usando ap.Document().
1. Se for bem-sucedido, ele imprime o número de páginas.
1. Caso contrário, ele captura a exceção e relata a senha falhada.

```python
import sys
from os import path

import aspose.pdf as ap
import aspose.pydrawing as drawing

def determine_correct_password_from_array(infile: str) -> None:
    """Try a list of passwords until the document opens successfully."""
    with ap.facades.PdfFileInfo() as pdf_file_info:
        pdf_file_info.bind_pdf(infile)
        print(f"File is password protected {pdf_file_info.is_encrypted}")

    passwords = ["test", "test1", "test2", "test3", "sample"]

    for password in passwords:
        try:
            with ap.Document(infile, password) as document:
                if len(document.pages) > 0:
                    print(f"Password = {password} is correct")
                    print(f"Number of pages in document = {len(document.pages)}")
                    break
        except Exception:
            print(f"Password = {password} is not correct")
```

## Tópicos de Segurança Relacionados

- [Proteja e assine arquivos PDF em Python](/pdf/pt/python-net/securing-and-signing/)
- [Assinar digitalmente arquivos PDF em Python](/pdf/pt/python-net/digitally-sign-pdf-file/)
- [Extrair informações de assinatura de PDF em Python](/pdf/pt/python-net/extract-image-and-signature-information/)
- [Assine documentos PDF a partir de um cartão inteligente em Python](/pdf/pt/python-net/sign-pdf-document-from-smart-card/)

