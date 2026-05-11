---
title: Informacion de firmas
linktitle: Informacion de firmas
type: docs
weight: 60
url: /es/python-net/signature-information/
description: Aprenda a leer nombres de firmas, detalles del firmante, marcas de tiempo y metadatos de firmas de archivos PDF firmados usando PdfFileSignature en Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Leer detalles de firmas de documentos PDF en Python
Abstract: Este articulo explica como inspeccionar metadatos de firmas en documentos PDF firmados con Aspose.PDF for Python via .NET. Muestra como listar nombres de firmas, leer detalles del firmante, obtener la fecha y hora de firma, y extraer el motivo y la ubicacion de la firma.
---

Aspose.PDF for Python via .NET proporciona la fachada [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) para inspeccionar firmas digitales en documentos PDF. Despues de que un documento se ha firmado, puede usarla para leer los nombres de las firmas y recuperar metadatos como el nombre del firmante, la informacion de contacto, la hora de firma, el motivo y la ubicacion.

Este ejemplo demuestra cuatro tareas comunes de informacion de firmas:

1. Listar todos los nombres de firma en un PDF firmado.
1. Leer los detalles del firmante para una firma seleccionada.
1. Obtener la fecha y hora de firma.
1. Leer el motivo y la ubicacion de la firma.

## Obtener nombres de firmas

Use este metodo cuando un PDF pueda contener una o varias firmas y desee inspeccionar que entradas de firma estan disponibles. El ejemplo abre el documento e imprime la lista devuelta por `get_sign_names()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_names(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature_names = list_signature_names(pdf_signature)
        print(f"Signature Names: {signature_names}")
    finally:
        pdf_signature.close()
```

## Obtener detalles del firmante

Una vez que conoce el nombre de la firma, puede recuperar metadatos especificos del firmante. Este ejemplo lee el nombre del firmante y la informacion de contacto para la primera firma disponible en el documento.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signer_details(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signer_name = pdf_signature.get_signer_name(sign_name)
        contact_info = pdf_signature.get_contact_info(sign_name)
        print(
            f"Signer Details for '{sign_name}': "
            f"signer_name={signer_name}, contact_info={contact_info}"
        )
    finally:
        pdf_signature.close()
```

## Obtener la fecha y hora de la firma

Use `get_date_time()` para determinar cuando se aplico una firma especifica. Esto resulta util para auditorias y para mostrar el historial de firmas en flujos de trabajo de documentos.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_date_and_time(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_date = pdf_signature.get_date_time(sign_name)
        print(f"Signature Date and Time for '{sign_name}': {signature_date}")
    finally:
        pdf_signature.close()
```

## Obtener el motivo y la ubicacion de la firma

Las firmas digitales tambien pueden almacenar metadatos descriptivos, como el motivo y la ubicacion de la firma. Este ejemplo recupera ambos valores para la firma seleccionada y los imprime juntos.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_reason_and_location(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_reason = pdf_signature.get_reason(sign_name)
        signature_location = pdf_signature.get_location(sign_name)
        print(
            f"Signature Reason and Location for '{sign_name}': "
            f"reason={signature_reason}, location={signature_location}"
        )
    finally:
        pdf_signature.close()
```
