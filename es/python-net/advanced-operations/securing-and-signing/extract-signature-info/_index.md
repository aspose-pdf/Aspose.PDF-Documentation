---
title: Extraer información de la firma de PDF en Python
linktitle: Extraer detalles de la firma
type: docs
weight: 20
url: /es/python-net/extract-image-and-signature-information/
description: Aprende cómo extraer imágenes de firmas, certificados y detalles de firmas digitales de archivos PDF en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Extraer imágenes de firmas y detalles de certificados de PDFs en Python
Abstract: Este artículo explica cómo extraer información de imágenes y firmas digitales de documentos PDF usando Aspose.PDF for Python. Aprende cómo recuperar imágenes de firmas, extraer datos de certificados, inspeccionar algoritmos de firma y detectar firmas comprometidas en archivos PDF firmados.
---

## Extrayendo imagen del campo de firma

Aspose.PDF for Python via .NET admite la funcionalidad de firmar digitalmente los archivos PDF usando el [signature_field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/) clase.

Utilice estos ejemplos cuando necesite inspeccionar documentos PDF firmados, exportar visuales de firmas o auditar la integridad de las firmas en flujos de trabajo de validación.

Este fragmento de código muestra cómo extraer imágenes de firmas digitales de un documento PDF usando Aspose.PDF for Python.

Pasos:

1. Abriendo el documento PDF.
1. Iterando a través de los campos del formulario para localizar cualquier objeto SignatureField.
1. Extrayendo la imagen asociada a cada firma (si está disponible).
1. Guardando la imagen de firma extraída como un archivo JPEG.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

path_infile = self.data_dir + infile
path_outfile = self.data_dir + outfile

# Open PDF document
with ap.Document(path_infile) as document:
    # Searching for signature fields
    for field in document.form:
        signature_field = field if isinstance(field, ap.forms.SignatureField) else None
        if signature_field is None:
            continue

        image_stream = signature_field.extract_image()
        if image_stream is None:
            continue

        image = drawing.Bitmap.from_stream(image_stream)
        # Save the image
        image.save(path_outfile, drawing.imaging.ImageFormat.jpeg)
```

## Extraer información de la firma

Aspose.PDF for Python via .NET soporta la función de firmar digitalmente los archivos PDF usando la clase SignatureField. Actualmente, también podemos determinar la validez del certificado pero no podemos extraer el certificado completo. La información que se puede extraer es una clave pública, huella digital, emisor, etc.

Para extraer información de la firma, hemos introducido el [ExtractCertificate](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) método al [SignatureField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/) class. Por favor, eche un vistazo al siguiente fragmento de código que demuestra los pasos para extraer el certificado del objeto SignatureField:

```python
import aspose.pdf as ap

path_infile = self.data_dir + infile
path_outfile = self.data_dir + outfile

# Open PDF document
with ap.Document(path_infile) as document:
    # Searching for signature fields
    for field in document.form:
        signature_field = field if isinstance(field, ap.forms.SignatureField) else None
        if signature_field is None:
            continue
        # Extract certificate
        certificate_stream = signature_field.extract_certificate()
        if certificate_stream is None:
            continue
        # Save certificate
        with certificate_stream:
            bytes_data = bytearray(certificate_stream.length)
            with open(path_outfile, "wb") as file_stream:
                certificate_stream.read(bytes_data, 0, len(bytes_data))
                file_stream.write(bytes_data)
```

Puede obtener información sobre los algoritmos de firma de documentos.

```python
import aspose.pdf as ap

# Open PDF document
with ap.Document(path_infile) as document:
    with ap.facades.PdfFileSignature(document) as signature:
        # Get signature names
        signature_names = signature.get_signature_names(True)
        signatures_info_list = signature.get_signatures_info()
        for sig_info in signatures_info_list:
            print(sig_info.DIGEST_HASH_ALGORITHM)
            print(sig_info.ALGORITHM_TYPE)
            print(sig_info.CRYPTOGRAPHIC_STANDARD)
            print(sig_info.signature_name)
```

## Comprobando firmas en busca de compromiso

Este fragmento de código demuestra cómo detectar firmas digitales comprometidas en un documento PDF utilizando Aspose.PDF for Python.

Los pasos incluyen:

1. Abriendo el documento PDF.
1. Crear una 'SignaturesCompromiseDetector' instancia para analizar el documento.
1. Comprobar si hay firmas digitales comprometidas (inválidas o modificadas).
1. Imprimiendo los nombres de cualquier firma comprometida encontrada.
1. Informando la cobertura de firmas—indicando cuánto del documento está protegido por firmas válidas.

Esta característica es fundamental en casos de uso donde se debe verificar la autenticidad e integridad del documento, como entornos legales, financieros y de cumplimiento. Permite a los desarrolladores detectar automáticamente manipulaciones o corrupciones de PDFs firmados.

Aspose.PDF ofrece un conjunto completo de herramientas para la validación de firmas digitales, facilitando la creación de aplicaciones seguras y conscientes de las firmas que mantienen la fiabilidad del documento.

```python
import aspose.pdf as ap

path_infile = self.data_dir + infile

# Open PDF document
with ap.Document(path_infile) as document:
    # Create the compromise detector instance
    detector = ap.SignaturesCompromiseDetector(document)
    result = []

    # Check for compromise
    if detector.check(result):
        print("No signature compromise detected")
        return

    # Get information about compromised signatures
    if result[0].has_compromised_signatures:
        print(
            f"Count of compromised signatures: {len(result[0].COMPROMISED_SIGNATURES)}"
        )
        for signature_name in result[0].COMPROMISED_SIGNATURES:
            print(f"Signature name: {signature_name.FULL_NAME}")

    # Get info about signatures coverage
    print(result[0].signatures_coverage)
```

## Temas de seguridad relacionados

- [Asegurar y firmar archivos PDF en Python](/pdf/es/python-net/securing-and-signing/)
- [Firmar digitalmente archivos PDF en Python](/pdf/es/python-net/digitally-sign-pdf-file/)
- [Firmar documentos PDF desde una tarjeta inteligente en Python](/pdf/es/python-net/sign-pdf-document-from-smart-card/)
- [Cifrar y descifrar archivos PDF en Python](/pdf/es/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
