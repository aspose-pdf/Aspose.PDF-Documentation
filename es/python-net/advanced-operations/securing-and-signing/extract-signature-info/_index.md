---
title: Extraer detalles de la firma
linktitle: Extraer detalles de la firma
type: docs
weight: 20
url: /es/python-net/extract-image-and-signature-information/
description: Cómo extraer una imagen de la firma digital en documentos PDF usando Aspose.PDF para Python.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Obtener detalles de la firma en PDFs usando Python
Abstract: Este artículo demuestra cómo extraer la imagen y la información de la firma digital de documentos PDF usando Aspose.PDF para Python. Proporciona instrucciones paso a paso y ejemplos de código para identificar, acceder y guardar imágenes incrustadas, así como para obtener los metadatos y el estado de validación de las firmas digitales.
---

## Extraer imagen del campo de firma

Aspose.PDF para Python a través de .NET admite la función de firmar digitalmente los archivos PDF usando la clase [signature_field](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/).

Este fragmento de código muestra cómo extraer imágenes de firmas digitales de un documento PDF usando Aspose.PDF para Python.

Pasos:

1. Abrir el documento PDF.
1. Recorrer los campos del formulario para localizar cualquier objeto SignatureField.
1. Extraer la imagen asociada a cada firma (si está disponible).
1. Guardar la imagen de firma extraída como archivo JPEG.

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

Aspose.PDF para Python a través de .NET admite la función de firmar digitalmente los archivos PDF usando la clase SignatureField. Actualmente, también podemos determinar la validez del certificado pero no podemos extraer el certificado completo. La información que se puede extraer es una clave pública, huella digital, emisor, etc.

Para extraer información de la firma, hemos introducido el método [ExtractCertificate](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) en la clase [SignatureField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/). Por favor, observa el siguiente fragmento de código que muestra los pasos para extraer el certificado del objeto SignatureField:

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

Puedes obtener información sobre los algoritmos de firma del documento.

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

## Verificar firmas comprometidas

Este fragmento de código muestra cómo detectar firmas digitales comprometidas en un documento PDF usando Aspose.PDF para Python.

Los pasos incluyen:

1. Abrir el documento PDF.
1. Crear una instancia de 'SignaturesCompromiseDetector' para analizar el documento.
1. Verificar si hay firmas digitales comprometidas (inválidas o alteradas).
1. Imprimir los nombres de cualquier firma comprometida encontrada.
1. Informar la cobertura de firmas—indicando cuánto del documento está protegido por firmas válidas.

Esta función es crítica en casos donde se debe verificar la autenticidad e integridad del documento, como entornos legales, financieros y de cumplimiento. Permite a los desarrolladores detectar automáticamente la manipulación o corrupción de PDFs firmados.

Aspose.PDF ofrece un conjunto completo de herramientas para la validación de firmas digitales, facilitando la creación de aplicaciones seguras y conscientes de firmas que mantienen la confiabilidad del documento.

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
            print(f"Count of compromised signatures: {len(result[0].COMPROMISED_SIGNATURES)}")
            for signature_name in result[0].COMPROMISED_SIGNATURES:
                print(f"Signature name: {signature_name.FULL_NAME}")

        # Get info about signatures coverage
        print(result[0].signatures_coverage)
```

