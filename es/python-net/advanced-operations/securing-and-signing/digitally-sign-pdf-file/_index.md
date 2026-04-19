---
title: Agregar firma digital o firmar PDF digitalmente en Python
linktitle: Firmar PDF digitalmente
type: docs
weight: 10
url: /es/python-net/digitally-sign-pdf-file/
description: Aprenda cómo firmar digitalmente documentos PDF, agregar marcas de tiempo y validar firmas en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Firmar archivos PDF digitalmente con Python
Abstract: Esta guia explica como firmar digitalmente documentos PDF usando Aspose.PDF para Python a traves de .NET. Detalla el proceso de aplicar firmas digitales estandar y avanzadas, utilizar certificados (PFX y PKCS#12) y personalizar la apariencia y el comportamiento de la firma. La documentacion incluye ejemplos de codigo que demuestran como firmar PDF existentes, añadir sellos de tiempo y verificar la validez de la firma. Esto permite a los desarrolladores garantizar la autenticidad, la integridad y el cumplimiento de los estandares de firma digital en sus aplicaciones Python.
---

## Firmar PDF con firmas digitales

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

path_infile = self.data_dir + infile
path_outfile = self.data_dir + outfile
path_pfxfile = self.data_dir + pfxfile

# Open PDF document
with ap.Document(path_infile) as document:
    # Instantiate PdfFileSignature object
    with ap.facades.PdfFileSignature(document) as signature:
        # Create PKCS#7 object for sign
        pkcs = ap.forms.PKCS7(path_pfxfile, "12345")
        # Sign PDF file
        signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
        #  Save PDF document
        signature.save(path_outfile)
```

Una **PKCS#7 detached signature** agrega una firma digital a un documento sin incrustar el contenido en el bloque de firma.

Utilice estos ejemplos cuando necesite aplicar firmas basadas en certificados a archivos PDF, verificar la validez de la firma o agregar marcas de tiempo confiables a documentos firmados.

El siguiente ejemplo firma un documento PDF usando una firma digital PKCS#7 separada, aplicando la firma a la primera página en un área rectangular especificada.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

path_infile = self.data_dir + infile
path_outfile = self.data_dir + outfile
path_pfxfile = self.data_dir + pfxfile

# Open PDF document
with ap.Document(path_infile) as document:
    # Instantiate PdfFileSignature object using the opened document
    with ap.facades.PdfFileSignature(document) as signature:
        # Create PKCS#7 detached object for sign
        pkcs = ap.forms.PKCS7Detached(
            path_pfxfile, password, ap.DigestHashAlgorithm.SHA256
        )
        # Sign PDF file
        signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
        #  Save PDF document
        signature.save(path_outfile)
```

Este fragmento de código Python verifica una firma digital en un archivo PDF usando el método 'file_sign.verify_signature()'.

1. Crea una instancia de PdfFileSignature que le permite interactuar con firmas en PDF.
1. Obtén una lista de nombres de firmas `get_signature_names(True)`.
1. Comprueba la primera firma en la lista `verify_signature` para el cumplimiento del certificado especificado.

```python
import aspose.pdf as ap

path_infile = self.data_dir + infile

# Create an instance of PdfFileSignature for working with signatures in the document
with ap.facades.PdfFileSignature(path_infile) as file_sign:
    # Get a list of signatures
    signature_names = file_sign.get_signature_names(True)
    # Verify the signature with the given name.
    return file_sign.verify_signature(signature_names[0], certificate)
```

## Agregar marca de tiempo a la firma digital

### Cómo firmar digitalmente un PDF con marca de tiempo

Aspose.PDF for Python admite firmar digitalmente el PDF con un servidor de marca de tiempo o servicio web.

Para cumplir con este requisito, el [TimestampSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) se ha añadido la clase al espacio de nombres Aspose.PDF. Por favor, echa un vistazo al siguiente fragmento de código que obtiene la marca de tiempo y la agrega al documento PDF:

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

path_infile = self.data_dir + infile
path_outfile = self.data_dir + outfile
path_pfxfile = self.data_dir + pfxfile

# Open PDF document
with ap.Document(path_infile) as document:
    # Create an instance of PdfFileSignature for working with signatures in the document
    with ap.facades.PdfFileSignature(document) as signature:
        pkcs = ap.forms.PKCS7(path_pfxfile, password)
        # Create TimestampSettings settings
        timestamp_settings = ap.TimestampSettings(
            "https://freetsa.org/tsr", "", ap.DigestHashAlgorithm.SHA256
        )  # User/Password can be omitted
        pkcs.timestamp_settings = timestamp_settings
        rect = drawing.Rectangle(
            100, 100, 200, 100
        )  # Creating a rectangle for the signature
        # Create any of the three signature types
        signature.sign(1, "Signature Reason", "Contact", "Location", True, rect, pkcs)
        # Save PDF document
        signature.save(path_outfile)
```

## Firmar documentos PDF usando ECDSA

Firmar documentos PDF usando ECDSA (Algoritmo de Firma Digital de Curva Elíptica) implica utilizar criptografía de curva elíptica para generar firmas digitales.

El fragmento de código anterior ilustra cómo aplicar una firma digital PKCS#7 separada a un documento PDF usando Aspose.PDF for Python. Al cargar el documento, configurar la apariencia de la firma y la configuración de seguridad, y guardar el resultado, este ejemplo demuestra un flujo de trabajo completo y fiable para firmar digitalmente archivos PDF.

Este método garantiza la autenticidad e integridad del documento al incrustar una firma segura y verificable en la primera página. El uso de SHA-256 como algoritmo de resumen cumple con los estándares criptográficos modernos, mientras que la capacidad de controlar la ubicación de la firma ofrece flexibilidad para marcas de aprobación visibles.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

path_infile = self.data_dir + infile
path_outfile = self.data_dir + outfile
path_pfxfile = self.data_dir + pfxfile

# Open PDF document
with ap.Document(path_infile) as document:
    # Create an instance of PdfFileSignature to sign the document
    with ap.facades.PdfFileSignature(document) as signature:
        # Create a PKCS7Detached object using the provided certificate and password
        pkcs = ap.forms.PKCS7Detached(
            path_pfxfile, password, ap.DigestHashAlgorithm.SHA256
        )

        # Sign the first page of the document, setting the signature's appearance at the specified location
        signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)

        # Save PDF document
        signature.save(path_outfile)
```

## Temas de seguridad relacionados

- [Asegurar y firmar archivos PDF en Python](/pdf/es/python-net/securing-and-signing/)
- [Extraer información de imágenes y firmas en Python](/pdf/es/python-net/extract-image-and-signature-information/)
- [Firmar documentos PDF desde una tarjeta inteligente en Python](/pdf/es/python-net/sign-pdf-document-from-smart-card/)
- [Cifrar y descifrar archivos PDF en Python](/pdf/es/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
