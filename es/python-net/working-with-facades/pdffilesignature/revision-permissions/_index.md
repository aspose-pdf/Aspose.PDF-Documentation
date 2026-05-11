---
title: Revisión y Permisos
type: docs
weight: 40
url: /es/python-net/revision-permissions/
description: Aprende cómo inspeccionar revisiones de firmas, revisiones de documentos y permisos de certificación en archivos PDF utilizando PdfFileSignature en Python.
lastmod: "2026-04-02"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Leer datos de revisión de firma PDF y permisos de acceso en Python
Abstract: Este artículo explica cómo inspeccionar la información de revisión y permisos en archivos PDF firmados o certificados con Aspose.PDF for Python via .NET. Muestra cómo obtener el número de revisión de una firma, contar el total de revisiones del documento y leer los permisos de acceso de un PDF certificado.
---

Aspose.PDF for Python via .NET proporciona la [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) fachada para trabajar con documentos PDF firmados y certificados. Además de agregar firmas, también puedes inspeccionar los metadatos de la firma para entender cuántas revisiones contiene un documento y qué cambios están permitidos después de la certificación.

Este ejemplo demuestra tres tareas comunes de inspección:

1. Obtener el número de revisión de una firma existente.
1. Obtener el número total de revisiones en un documento firmado.
1. Lea los permisos de acceso de un PDF certificado.

## Obtenga el número de revisión de una firma

Utilice este enfoque cuando un PDF ya contiene una o más firmas y necesite identificar la revisión asociada a una firma específica. El ejemplo resuelve el primer nombre de firma disponible y luego llama `get_revision()`.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_signature_revision(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        sign_name = require_signature_name(pdf_signature)
        signature_revision = pdf_signature.get_revision(sign_name)
        print(f"Signature Revision for '{sign_name}': {signature_revision}")
    finally:
        pdf_signature.close()
```

## Obtener el número total de revisiones del documento

Usar `get_total_revision()` cuando necesitas saber cuántas revisiones se almacenan en el PDF firmado. Esto es útil para comprobar si el documento ha pasado por múltiples actualizaciones después de que se aplicó la firma original.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_total_document_revisions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        total_revisions = pdf_signature.get_total_revision()
        print(f"Total Document Revisions: {total_revisions}")
    finally:
        pdf_signature.close()
```

## Obtener permisos de acceso de un PDF certificado

Los documentos certificados pueden definir qué cambios están permitidos después de la certificación. Usar `get_access_permissions()` para inspeccionar ese nivel de permiso y determinar si el documento permite no realizar cambios, rellenar formularios u otras modificaciones controladas.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def get_access_permissions(infile):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        access_permissions = pdf_signature.get_access_permissions()
        print(f"Access Permissions: {access_permissions}")
    finally:
        pdf_signature.close()
```

