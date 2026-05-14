---
title: Administracion de firmas
linktitle: Administracion de firmas
type: docs
weight: 80
url: /es/python-net/signature-management/
description: Aprenda a quitar firmas digitales de documentos PDF y, opcionalmente, limpiar campos de firma usando PdfFileSignature en Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Quitar firmas PDF y limpiar campos de firma en Python
Abstract: Este articulo explica como administrar firmas digitales existentes en documentos PDF con Aspose.PDF for Python via .NET. Muestra como quitar una firma de un PDF y como quitar una firma junto con su campo de firma asociado.
---

Aspose.PDF for Python via .NET proporciona la fachada [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) para trabajar con firmas digitales existentes en documentos PDF. Ademas de leer y validar firmas, tambien puede quitarlas cuando un flujo de trabajo requiere actualizar el contenido firmado o limpiar el campo de firma.

Este ejemplo demuestra dos tareas comunes de administracion de firmas:

1. Quitar una firma de un documento PDF.
1. Quitar una firma y limpiar el campo de firma asociado.

## Quitar una firma de un PDF

Use `remove_signature()` cuando desee eliminar la firma seleccionada del documento y conservar la estructura del campo de firma subyacente. El ejemplo abre el PDF firmado, resuelve el nombre de la firma, la quita y guarda el archivo de salida actualizado.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_signature_from_pdf(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Quitar una firma y limpiar el campo

Use la sobrecarga con el indicador adicional `True` cuando desee quitar la firma y tambien limpiar el campo de firma relacionado. Esto es util cuando el campo no debe permanecer en el documento despues de que la firma se haya eliminado.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def remove_signature_with_field_cleanup(infile, outfile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        pdf_signature.remove_signature(sign_name, True)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
