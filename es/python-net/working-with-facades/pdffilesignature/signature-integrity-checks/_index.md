---
title: Comprobaciones de Integridad de Firma
linktitle: Comprobaciones de Integridad de Firma
type: docs
weight: 70
url: /es/python-net/signature-integrity-checks/
description: Aprenda cómo comprobar si una firma PDF cubre todo el documento y valide la integridad del documento firmado usando PdfFileSignature en Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Validar la cobertura e integridad de la firma PDF en Python
Abstract: Este artículo explica cómo inspeccionar la integridad de la firma digital en documentos PDF firmados con Aspose.PDF for Python via .NET. Muestra cómo verificar si una firma cubre todo el documento y cómo validar la integridad del contenido firmado.
---

Aspose.PDF for Python via .NET proporciona el [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) fachada para validar documentos PDF firmados. Después de que un archivo ha sido firmado, puedes usarla para comprobar si la firma se aplica al documento completo y si el contenido firmado sigue siendo válido.

Este ejemplo muestra dos comprobaciones de integridad comunes:

1. Comprueba si una firma cubre todo el documento.
1. Valida la integridad del contenido PDF firmado.

## Comprueba si una firma cubre todo el documento

Usar `covers_whole_document()` cuando necesita confirmar que la firma se aplica a todo el PDF y no solo a una parte de su contenido. El ejemplo lee el primer nombre de firma disponible y verifica su cobertura.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def check_signature_coverage(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        covers_document = pdf_signature.covers_whole_document(sign_name)
        print(f"Signature '{sign_name}' covers the whole document: {covers_document}")
    finally:
        pdf_signature.close()
```

## Validar la integridad del documento

Usar `verify_signed()` para confirmar que el contenido del documento firmado no ha sido alterado después de que se aplicó la firma. Este método ayuda a verificar si el documento sigue siendo válido para la firma seleccionada.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def validate_document_integrity(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        is_valid = pdf_signature.verify_signed(sign_name)
        print(f"Document integrity for '{sign_name}' is valid: {is_valid}")
    finally:
        pdf_signature.close()
```

