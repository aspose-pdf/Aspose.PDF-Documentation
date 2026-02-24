---
title: Agregar firma digital o firmar PDF digitalmente en Python
linktitle: Firmar PDF digitalmente
type: docs
weight: 10
url: /es/python-net/digitally-sign-pdf-file/
description: Firmar documentos PDF digitalmente, verificar o validar los PDF firmados digitalmente usando Python.
lastmod: "2025-06-07"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Firmar archivos PDF digitalmente con Python
Abstract: Esta guía explica cómo firmar documentos PDF digitalmente usando Aspose.PDF para Python a través de .NET. Detalla el proceso de aplicar firmas digitales estándar y avanzadas, utilizando certificados (PFX y PKCS#12), y personalizando la apariencia y el comportamiento de la firma. La documentación incluye ejemplos de código que demuestran cómo firmar PDFs existentes, agregar marcas de tiempo y verificar la validez de la firma. Esto permite a los desarrolladores garantizar la autenticidad, integridad y el cumplimiento de los estándares de firma digital en sus aplicaciones Python.
---

## Firmar PDF con firmas digitales

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    ppath_infile = self.data_dir + infile
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

Una **firma PKCS#7 independiente** agrega una firma digital a un documento sin incrustar el contenido en el bloque de firma.

El siguiente ejemplo firma un documento PDF usando una firma digital PKCS#7 independiente, aplicando la firma a la primera página en un área rectangular especificada.

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
            pkcs = ap.forms.PKCS7Detached(path_pfxfile, password, ap.DigestHashAlgorithm.SHA256)
            # Sign PDF file
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            #  Save PDF document
            signature.save(path_outfile)
```

Este fragmento de código Python verifica una firma digital en un archivo PDF usando el método 'file_sign.verify_signature()'.

1. Crea una instancia de PdfFileSignature que le permite interactuar con firmas en PDF.
1. Obtenga una lista de nombres de firmas `get_signature_names(True)`.
1. Verifica la primera firma en la lista `verify_signature` para el cumplimiento con el certificado especificado.

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

Aspose.PDF para Python permite firmar digitalmente el PDF con un servidor de marcas de tiempo o un servicio web.

Para cumplir con este requisito, se ha añadido la clase [TimestampSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) al espacio de nombres Aspose.PDF. Por favor, revise el siguiente fragmento de código que obtiene la marca de tiempo y la agrega al documento PDF:

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
            timestamp_settings = ap.TimestampSettings("https://freetsa.org/tsr",
                                                                "", ap.DigestHashAlgorithm.SHA256)  # User/Password can be omitted
            pkcs.timestamp_settings = timestamp_settings
            rect = drawing.Rectangle(100, 100, 200, 100)  # Creating a rectangle for the signature
            # Create any of the three signature types
            signature.sign(1, "Signature Reason", "Contact", "Location", True, rect, pkcs)
            # Save PDF document
                signature.save(path_outfile)
```

## Firmar documentos PDF usando ECDSA

Firmar documentos PDF usando ECDSA (Algoritmo de Firma Digital de Curva Elíptica) implica utilizar criptografía de curva elíptica para generar firmas digitales.

El fragmento de código anterior ilustra cómo aplicar una firma digital PKCS#7 independiente a un documento PDF usando Aspose.PDF para Python. Al cargar el documento, configurar la apariencia de la firma y los ajustes de seguridad, y guardar el resultado, este ejemplo demuestra un flujo de trabajo completo y fiable para firmar digitalmente archivos PDF.

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
            pkcs = ap.forms.PKCS7Detached(path_pfxfile, password, ap.DigestHashAlgorithm.SHA256)

            # Sign the first page of the document, setting the signature's appearance at the specified location
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)

            # Save PDF document
            signature.save(path_outfile)
```
