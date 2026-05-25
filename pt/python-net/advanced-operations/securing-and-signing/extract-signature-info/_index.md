---
title: Extrair informações da assinatura de PDF em Python
linktitle: Extrair detalhes da assinatura
type: docs
weight: 20
url: /pt/python-net/extract-image-and-signature-information/
description: Aprenda a extrair imagens de assinatura, certificados e detalhes de assinatura digital de arquivos PDF em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraia imagens de assinatura e detalhes de certificados de PDFs em Python
Abstract: Este artigo explica como extrair informações de imagem e assinatura digital de documentos PDF usando Aspose.PDF for Python. Aprenda como recuperar imagens de assinatura, extrair dados de certificado, inspecionar algoritmos de assinatura e detectar assinaturas comprometidas em arquivos PDF assinados.
---

## Extrair Imagem de um Campo de Assinatura

Aspose.PDF for Python via .NET permite que você recupere a imagem visual incorporada em um [Campo de Assinatura](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/). Isto é útil quando você precisa exibir ou arquivar a aparência da assinatura sem renderizar o PDF completo.

O exemplo abaixo itera sobre todos os campos de formulário, encontra cada `SignatureField`, e salva sua imagem como um arquivo JPEG:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_images_from_signature_field(infile: str, outfile: str) -> None:
    """Extract the image stored in a signature field."""
    with ap.Document(infile) as document:
        for field in document.form:
            if not isinstance(field, ap.forms.SignatureField):
                continue

            image_stream = field.extract_image()
            if image_stream is None:
                continue

            image = drawing.Bitmap.from_stream(image_stream)
            image.save(outfile, drawing.imaging.ImageFormat.jpeg)
```

## Ler detalhes do algoritmo de assinatura

Usar `PdfFileSignature.get_signatures_info()` para ler metadados criptográficos de cada assinatura em um documento — incluindo o algoritmo de digestão, o tipo de algoritmo, o padrão criptográfico e o nome da assinatura:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def get_signatures_info(infile: str) -> None:
    """Print information about all signatures in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_info in signature.get_signatures_info():
                print(signature_info.DIGEST_HASH_ALGORITHM)
                print(signature_info.ALGORITHM_TYPE)
                print(signature_info.CRYPTOGRAPHIC_STANDARD)
                print(signature_info.signature_name)
```

## Extrair um Certificado Digital de um Campo de Assinatura

Use o [extract_certificate](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) método em um `SignatureField` para recuperar o certificado incorporado como um fluxo de bytes e salvá-lo no disco para validação externa:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_certificate(infile: str, outfile: str) -> None:
    """Extract a certificate from a signature field and save it to disk."""
    with ap.Document(infile, password="owner") as document:
        for field in document.form:
            if not isinstance(field, ap.forms.SignatureField):
                continue

            certificate_stream = field.extract_certificate()
            if certificate_stream is None:
                continue

            with certificate_stream:
                bytes_data = bytearray(certificate_stream.length)
                certificate_stream.read(bytes_data, 0, len(bytes_data))
                with open(outfile, "wb") as file_stream:
                    file_stream.write(bytes_data)
                return
```

## Extrair Certificados Usando a Fachada PdfFileSignature

`PdfFileSignature.try_extract_certificate()` fornece uma maneira alternativa de recuperar certificados pelo nome da assinatura. O exemplo a seguir itera sobre todos os nomes de assinatura e tenta a extração para cada um:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def extract_certificate_try_extract_certificate_method(infile: str) -> None:
    """Extract certificates with the try_extract_certificate facade method."""
    with ap.Document(infile, password="owner") as document:
        with ap.facades.PdfFileSignature(document) as signature:
            for signature_name in signature.get_signature_names(True):
                certificate = []
                if signature.try_extract_certificate(signature_name, certificate):
                    print("The certificate extraction succeeded")
```

## Verificar Assinaturas Digitais Externas

Para confirmar que um documento não foi modificado após a assinatura, verifique cada assinatura externa usando `PdfFileSignature.verify_signature()`. O exemplo abaixo gera uma exceção para qualquer assinatura que falhar na verificação:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_external_signature(infile: str) -> None:
    """Verify an external signature in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            for signature_name in pdf_signature.get_signature_names(True):
                if not pdf_signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## Detectar assinaturas comprometidas

`SignaturesCompromiseDetector` verifica se alguma assinatura digital em um documento foi invalidada por alterações subsequentes. Use isso em fluxos de trabalho jurídicos, financeiros ou de conformidade onde a integridade do documento deve ser garantida.

O exemplo abaixo verifica assinaturas comprometidas e relata seus nomes juntamente com a cobertura geral de assinaturas do documento:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def check(infile: str) -> None:
    """Check whether a PDF contains compromised signatures."""
    with ap.Document(infile) as document:
        detector = ap.SignaturesCompromiseDetector(document)
        result = []

        if detector.check(result):
            print("No signature compromise detected")
            return

        if result[0].has_compromised_signatures:
            print(
                f"Count of compromised signatures: {len(result[0].COMPROMISED_SIGNATURES)}"
            )
            for signature_name in result[0].COMPROMISED_SIGNATURES:
                print(f"Signature name: {signature_name.FULL_NAME}")

        print(result[0].signatures_coverage)
```

## Tópicos de Segurança Relacionados

- [Proteja e assine arquivos PDF em Python](/pdf/pt/python-net/securing-and-signing/)
- [Assinar digitalmente arquivos PDF em Python](/pdf/pt/python-net/digitally-sign-pdf-file/)
- [Assine documentos PDF a partir de um cartão inteligente em Python](/pdf/pt/python-net/sign-pdf-document-from-smart-card/)
- [Criptografar e descriptografar arquivos PDF em Python](/pdf/pt/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
