---
title: Verificación de firmas
linktitle: Verificación de firmas
type: docs
weight: 90
url: /es/python-net/signature-verification/
description: Aprenda a verificar firmas digitales y a comprobar si un PDF contiene firmas usando PdfFileSignature en Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Verificar firmas PDF en Python
Abstract: Este artículo explica cómo verificar firmas digitales en documentos PDF con Aspose.PDF for Python via .NET. Muestra cómo validar una firma existente y cómo comprobar si un PDF contiene alguna firma.
---

Aspose.PDF for Python via .NET proporciona el [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) fachada para validar documentos PDF firmados. Después de que un PDF ha sido firmado, puede usarla para confirmar que una firma es válida y detectar si el documento contiene entradas de firmas.

Este ejemplo muestra dos tareas comunes de verificación:

1. Verifique que una firma existente de PDF sea válida.
1. Compruebe si un PDF contiene alguna firma.

## Verificar una firma de PDF

Usar `verify_signature()` cuando necesitas validar una firma específica en el documento. El ejemplo resuelve el primer nombre de firma disponible y verifica si esa firma es válida.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def verify_pdf_signature(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signature(sign_name)
        print(f"Signature '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```

## Verifique si un PDF contiene firmas

Usar `contains_signature()` cuando solo necesitas saber si el PDF incluye alguna firma. Esto es útil como una verificación rápida antes de ejecutar una lógica de verificación o extracción más detallada.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_if_pdf_contains_signatures(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        contains_signatures = pdf_signature.contains_signature()
        print(f"PDF contains signatures: {contains_signatures}")
    finally:
        pdf_signature.close()
```
