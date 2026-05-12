---
title: Agregar firma digital o firmar digitalmente PDF en Python
linktitle: Firmar PDF digitalmente
type: docs
weight: 10
url: /es/python-net/digitally-sign-pdf-file/
description: Aprenda a firmar digitalmente documentos PDF, agregar marcas de tiempo y validar firmas en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Firme digitalmente archivos PDF con Python
Abstract: Esta guía explica cómo firmar digitalmente documentos PDF utilizando Aspose.PDF for Python via .NET. Detalla el proceso de aplicar firmas digitales estándar y avanzadas, utilizando certificados (PFX y PKCS#12), y personalizando la apariencia y el comportamiento de la firma. La documentación incluye ejemplos de código que demuestran cómo firmar PDFs existentes, agregar marcas de tiempo y verificar la validez de la firma. Esto permite a los desarrolladores garantizar la autenticidad, integridad y el cumplimiento de los estándares de firma digital en sus aplicaciones Python.
---

## Firmar PDF con firmas digitales

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

Una **firma PKCS#7 separada** agrega una firma digital a un documento sin incrustar el contenido en el bloque de firma.

Utilice estos ejemplos cuando necesite aplicar firmas basadas en certificados a archivos PDF, verificar la validez de la firma o agregar marcas de tiempo confiables a documentos firmados.

El siguiente ejemplo firma un documento PDF usando una firma digital PKCS#7 separada, aplicando la firma a la primera página en una zona rectangular especificada.

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

**Verificar todas las firmas digitales en un documento PDF**

1. Crea una instancia de PdfFileSignature que le permite interactuar con firmas en PDF.
1. Obtener una lista de nombres de firma `get_signature_names(True)`.
1. Comprueba la primera firma en la lista `verify_signature` para el cumplimiento del certificado especificado.

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

**Verificar una firma con un archivo de certificado de clave pública**

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

**Verificar una firma con el certificado extraído del archivo**

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

**Verificar firmas con validación de cadena de certificados habilitada**

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

## Agregar marca de tiempo a la firma digital

### Cómo firmar digitalmente un PDF con sello de tiempo

Aspose.PDF for Python permite firmar digitalmente el PDF con un servidor de marca de tiempo o un servicio web.

Para cumplir con este requisito, el [Configuración de marca de tiempo](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) Se ha añadido una clase al espacio de nombres Aspose.PDF. Por favor, consulte el siguiente fragmento de código que obtiene la marca de tiempo y la añade al documento PDF:

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

## Firmar documentos PDF usando ECDSA

Firmar documentos PDF usando ECDSA (Elliptic Curve Digital Signature Algorithm) implica utilizar criptografía de curva elíptica para generar firmas digitales.

El fragmento de código anterior ilustra cómo aplicar una firma digital PKCS#7 separada a un documento PDF usando Aspose.PDF for Python. Al cargar el documento, configurar la apariencia de la firma y los ajustes de seguridad, y guardar el resultado, este ejemplo demuestra un flujo de trabajo completo y fiable para firmar digitalmente archivos PDF.

Este método garantiza la autenticidad e integridad del documento al incrustar una firma segura y verificable en la primera página. El uso de SHA-256 como algoritmo de resumen cumple con los estándares criptográficos modernos, mientras que la capacidad de controlar la ubicación de la firma ofrece flexibilidad para marcas de aprobación visibles.

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

**Verificar firmas ECDSA en un documento PDF**

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

## Temas de Seguridad Relacionados

- [Protege y firma archivos PDF en Python](/pdf/es/python-net/securing-and-signing/)
- [Extraer información de imágenes y firmas en Python](/pdf/es/python-net/extract-image-and-signature-information/)
- [Firmar documentos PDF desde una tarjeta inteligente en Python](/pdf/es/python-net/sign-pdf-document-from-smart-card/)
- [Cifrar y descifrar archivos PDF en Python](/pdf/es/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)