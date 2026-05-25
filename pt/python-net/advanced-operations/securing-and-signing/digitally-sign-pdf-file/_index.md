---
title: Adicionar assinatura digital ou assinar PDF digitalmente em Python
linktitle: Assinar PDF digitalmente
type: docs
weight: 10
url: /pt/python-net/digitally-sign-pdf-file/
description: Aprenda a assinar digitalmente documentos PDF, adicionar carimbos de horário e validar assinaturas em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Assine digitalmente arquivos PDF com Python
Abstract: Este guia explica como assinar digitalmente documentos PDF usando Aspose.PDF for Python via .NET. Ele detalha o processo de aplicação de assinaturas digitais padrão e avançadas, utilizando certificados (PFX e PKCS#12), e personalizando a aparência e o comportamento da assinatura. A documentação inclui exemplos de código que demonstram como assinar PDFs existentes, adicionar carimbos de data/hora e verificar a validade da assinatura. Isso permite que os desenvolvedores garantam a autenticidade, integridade e conformidade dos documentos com os padrões de assinatura digital em suas aplicações Python.
---

## Assinar PDF com assinaturas digitais

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_document(infile: str, outfile: str, pfxfile: str) -> None:
    """Sign a PDF document with a PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, "12345")
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

A **assinatura PKCS#7 destacada** adiciona uma assinatura digital a um documento sem incorporar o conteúdo ao bloco de assinatura.

Use estes exemplos quando precisar aplicar assinaturas baseadas em certificado a arquivos PDF, verificar a validade da assinatura ou adicionar carimbos de tempo confiáveis a documentos assinados.

O próximo exemplo assina um documento PDF usando uma assinatura digital PKCS#7 destacada, aplicando a assinatura à primeira página em uma área retangular especificada.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_document_PKCS7_detached(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document with a detached PKCS#7 certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

**Verificar todas as assinaturas digitais em um documento PDF**

1. Cria uma instância de PdfFileSignature que permite interagir com assinaturas em PDF.
1. Obtenha uma lista de nomes de assinatura `get_signature_names(True)`.
1. Verifica a primeira assinatura na lista `verify_signature` para conformidade com o certificado especificado.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify(infile: str) -> None:
    """Verify all digital signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

**Verificar uma assinatura com um arquivo de certificado de chave pública**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_with_public_key_certificate1(certificate: str, infile: str) -> None:
    """Verify a signature with a public key certificate file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        with open(certificate, "rb") as file_stream:
            certificate_bytes = file_stream.read()
        print(file_sign.verify_signature(signature_names[0], certificate_bytes))
```

**Verificar uma assinatura com o certificado extraído do arquivo**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_with_public_key_certificate_from_signature(infile: str) -> None:
    """Verify a signature with the certificate extracted from the file."""
    with ap.facades.PdfFileSignature(infile) as file_sign:
        signature_names = file_sign.get_signature_names(True)
        certificate = []
        if file_sign.try_extract_certificate(signature_names[0], certificate):
            print(file_sign.verify_signature(signature_names[0], certificate[0]))
        else:
            print(False)
```

**Verificar assinaturas com validação de cadeia de certificados habilitada**

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_signature_with_certificate_check(infile: str) -> None:
    """Verify signatures with certificate-chain validation enabled."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                options = ap.security.ValidationOptions()
                options.validation_mode = ap.security.ValidationMode.STRICT
                options.validation_method = ap.security.ValidationMethod.AUTO
                options.check_certificate_chain = True
                options.request_timeout = 20000
                validation_result = []
                verified = signature.verify_signature(
                    signature_name,
                    options,
                    validation_result,
                )
                print(f"Certificate validation result: {validation_result[0].status}")
                print(f"Is verified: {verified}")
```

## Adicionar carimbo de tempo à assinatura digital

### Como assinar digitalmente um PDF com carimbo de tempo

Aspose.PDF for Python suporta assinar digitalmente o PDF com um servidor de timestamp ou serviço Web.

Para atender a esse requisito, o [Configurações de Carimbo de Tempo](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) classe foi adicionada ao namespace Aspose.PDF. Por favor, dê uma olhada no trecho de código a seguir que obtém o timestamp e o adiciona ao documento PDF:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_with_time_stamp_server(
    infile: str,
    outfile: str,
    pfxfile: str,
    password: str,
) -> None:
    """Sign a PDF document and apply a timestamp from an external server."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(pfxfile, password)
            pkcs.timestamp_settings = ap.TimestampSettings(
                "https://freetsa.org/tsr",
                "",
                ap.DigestHashAlgorithm.SHA256,
            )
            rect = drawing.Rectangle(100, 100, 200, 100)
            signature.sign(
                1, "Signature Reason", "Contact", "Location", True, rect, pkcs
            )
            signature.save(outfile)
```

## Assinando documentos PDF usando ECDSA

Assinar documentos PDF usando ECDSA (Algoritmo de Assinatura Digital de Curva Elíptica) envolve a utilização de criptografia de curva elíptica para gerar assinaturas digitais.

O trecho de código acima ilustra como aplicar uma assinatura digital PKCS#7 destacada a um documento PDF usando Aspose.PDF for Python. Ao carregar o documento, configurar a aparência da assinatura e as configurações de segurança, e salvar o resultado, este exemplo demonstra um fluxo de trabalho completo e confiável para assinar digitalmente arquivos PDF.

Este método garante a autenticidade e integridade do documento ao incorporar uma assinatura segura e verificável na primeira página. O uso do SHA-256 como algoritmo de digestão atende aos padrões criptográficos modernos, enquanto a capacidade de controlar a colocação da assinatura oferece flexibilidade para marcas de aprovação visíveis.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_ecdsa(infile: str, outfile: str, pfxfile: str, password: str) -> None:
    """Sign a PDF document with an ECDSA signature."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7Detached(
                pfxfile,
                password,
                ap.DigestHashAlgorithm.SHA256,
            )
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            signature.save(outfile)
```

**Verificar assinaturas ECDSA em um documento PDF**

```python
def verify_ecdsa(infile: str) -> None:
    """Verify ECDSA signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            if not signature.contains_signature():
                raise Exception("Not contains signature")

            for signature_name in signature.get_signature_names(True):
                if not signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## Tópicos de Segurança Relacionados

- [Proteja e assine arquivos PDF em Python](/pdf/pt/python-net/securing-and-signing/)
- [Extrair informações de imagem e assinatura em Python](/pdf/pt/python-net/extract-image-and-signature-information/)
- [Assine documentos PDF a partir de um cartão inteligente em Python](/pdf/pt/python-net/sign-pdf-document-from-smart-card/)
- [Criptografar e descriptografar arquivos PDF em Python](/pdf/pt/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)