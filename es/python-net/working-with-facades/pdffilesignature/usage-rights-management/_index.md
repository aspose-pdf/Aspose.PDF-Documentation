---
title: Administracion de derechos de uso
linktitle: Administracion de derechos de uso
type: docs
weight: 100
url: /es/python-net/usage-rights-management/
description: Aprenda a detectar y quitar derechos de uso de documentos PDF usando PdfFileSignature en Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Quitar derechos de uso de PDF en Python
Abstract: Este articulo explica como inspeccionar y quitar derechos de uso de documentos PDF con Aspose.PDF for Python via .NET. Muestra como comprobar si un PDF contiene derechos de uso y como guardar una nueva version del documento despues de quitar esos derechos.
---

Aspose.PDF for Python via .NET proporciona la fachada [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) para trabajar con PDF firmados y configuraciones relacionadas de derechos de uso. En algunos flujos de trabajo, puede que necesite inspeccionar si un documento contiene derechos de uso y quitarlos antes de guardar una version actualizada del archivo.

Este ejemplo demuestra una tarea comun de administracion de derechos de uso:

1. Comprobar si un PDF contiene derechos de uso.
1. Quitar los derechos de uso del documento.
1. Guardar el archivo PDF actualizado.

## Comprobar si el PDF contiene derechos de uso

Antes de quitar derechos de uso, el ejemplo comprueba el estado actual del documento llamando a `contains_usage_rights()`. Esto le permite confirmar si los derechos de uso estan presentes antes de realizar cambios.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_usage_rights(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights: {had_usage_rights}")
    finally:
        pdf_signature.close()
```

## Quitar derechos de uso del PDF

Use `remove_usage_rights()` cuando el documento ya no deba conservar su configuracion existente de derechos de uso. El ejemplo comprueba el estado inicial, quita los derechos y guarda el PDF actualizado en un nuevo archivo.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_usage_rights(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        had_usage_rights = pdf_signature.contains_usage_rights()
        print(f"PDF contains usage rights before removal: {had_usage_rights}")
        pdf_signature.remove_usage_rights()
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
