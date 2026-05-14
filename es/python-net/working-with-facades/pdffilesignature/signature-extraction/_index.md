---
title: Extracción de firma
linktitle: Extracción de firma
type: docs
weight: 50
url: /es/python-net/signature-extraction/
description: Aprenda cómo extraer una imagen de firma y el certificado de firma de un PDF firmado usando PdfFileSignature en Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extraer imagen de firma y certificado de PDF en Python
Abstract: Este artículo explica cómo extraer datos relacionados con firmas de documentos PDF firmados con Aspose.PDF for Python via .NET. Muestra cómo leer la primera firma disponible, exportar su imagen y guardar el flujo del certificado asociado en un archivo de salida.
---

Aspose.PDF for Python via .NET proporciona el [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) fachada para inspeccionar y extraer datos de documentos PDF firmados. Después de que un PDF ha sido firmado, puedes usarla para exportar recursos de firma como la imagen de firma visual y el certificado asociado a la firma.

Este ejemplo demuestra dos tareas comunes de extracción:

1. Extraer la imagen visual asociada a una firma.
1. Extraer el certificado de firma de un PDF firmado.

## Extraer una imagen de firma

Utiliza este método cuando el PDF contiene una firma visible y deseas exportar sus datos de imagen. El ejemplo abre el documento firmado, obtiene el primer nombre de firma disponible, extrae el flujo de la imagen y lo escribe en un archivo.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_image(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_image = pdf_signature.extract_image(sign_name)
        write_stream_data(signature_image, outfile)
    finally:
        pdf_signature.close()
```

## Extraer un certificado de firma

Usar `extract_certificate()` cuando necesites los datos del certificado adjuntos a una firma. Esto es útil para inspección, flujos de trabajo de validación o para almacenar el certificado del firmante por separado del documento PDF.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def extract_signature_certificate(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_certificate = pdf_signature.extract_certificate(sign_name)
        write_stream_data(signature_certificate, outfile)
    finally:
        pdf_signature.close()
```

