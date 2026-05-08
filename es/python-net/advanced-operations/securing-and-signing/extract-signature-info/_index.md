---
title: Extraer información de la firma del PDF en Python
linktitle: Extraer detalles de la firma
type: docs
weight: 20
url: /es/python-net/extract-image-and-signature-information/
description: Aprenda cómo extraer imágenes de firmas, certificados y detalles de firmas digitales de archivos PDF en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraiga imágenes de firmas y detalles de certificados de PDFs en Python
Abstract: Este artículo explica cómo extraer información de imágenes y firmas digitales de documentos PDF utilizando Aspose.PDF for Python. Aprenda cómo recuperar imágenes de firmas, extraer datos de certificados, inspeccionar algoritmos de firma y detectar firmas comprometidas en archivos PDF firmados.
---

## Extraer imagen de un campo de firma

Aspose.PDF for Python via .NET le permite recuperar la imagen visual incrustada en un [CampoDeFirma](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/). Esto es útil cuando necesitas mostrar o archivar la apariencia de la firma sin renderizar el PDF completo.

El ejemplo a continuación itera sobre todos los campos de formulario, encontrando cada uno `SignatureField`, y guarda su imagen como un archivo JPEG:

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

## Leer detalles del algoritmo de firma

Usar `PdfFileSignature.get_signatures_info()` leer los metadatos criptográficos de cada firma en un documento — incluyendo el algoritmo de resumen, el tipo de algoritmo, la norma criptográfica y el nombre de la firma:

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

## Extraer un certificado digital de un campo de firma

Usa el [extract_certificate](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) método en un `SignatureField` para recuperar el certificado incrustado como un flujo de bytes y guardarlo en disco para validación externa:

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

## Extraer certificados usando la fachada PdfFileSignature

`PdfFileSignature.try_extract_certificate()` proporciona una forma alternativa de obtener certificados por nombre de firma. El siguiente ejemplo itera sobre todos los nombres de firma e intenta la extracción para cada uno:

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

## Verificar firmas digitales externas

Para confirmar que un documento no ha sido modificado después de firmarlo, verifique cada firma externa usando `PdfFileSignature.verify_signature()`. El ejemplo a continuación genera una excepción para cualquier firma que falle la verificación:

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

## Detectar firmas comprometidas

`SignaturesCompromiseDetector` verifica si alguna firma digital en un documento ha sido invalidada por cambios posteriores. Utilízalo en flujos de trabajo legales, financieros o de cumplimiento donde se debe garantizar la integridad del documento.

El siguiente ejemplo verifica firmas comprometidas y reporta sus nombres junto con la cobertura total de firmas del documento:

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

## Temas de Seguridad Relacionados

- [Protege y firma archivos PDF en Python](/pdf/es/python-net/securing-and-signing/)
- [Firmar digitalmente archivos PDF en Python](/pdf/es/python-net/digitally-sign-pdf-file/)
- [Firmar documentos PDF desde una tarjeta inteligente en Python](/pdf/es/python-net/sign-pdf-document-from-smart-card/)
- [Cifrar y descifrar archivos PDF en Python](/pdf/es/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
