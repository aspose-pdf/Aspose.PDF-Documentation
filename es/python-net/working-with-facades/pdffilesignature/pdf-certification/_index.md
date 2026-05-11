---
title: Certificación PDF
type: docs
weight: 30
url: /es/python-net/pdf-certification/
description: Aprenda cómo certificar documentos PDF en Python usando PdfFileSignature y DocMDPSignature con diferentes permisos de modificación del documento.
lastmod: "2026-04-02"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Certifique documentos PDF con permisos DocMDP en Python
Abstract: Este artículo explica cómo certificar documentos PDF con Aspose.PDF for Python via .NET usando la fachada PdfFileSignature. Muestra cómo crear una DocMDPSignature, aplicar la certificación con permisos de llenado de formularios y bloquear un documento con un nivel de certificación sin cambios.
---

Aspose.PDF for Python via .NET le permite certificar documentos PDF aplicando una firma a nivel de documento con [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/). La certificación es diferente de una firma de aprobación estándar porque define qué cambios, si los hay, están permitidos después de que el documento ha sido certificado.

Este artículo muestra dos flujos de trabajo de certificación comunes:

1. Certificar un PDF y permitir el relleno de formularios después de la certificación.
1. Certificar un PDF y evitar cualquier cambio posterior.

## Certificar un PDF para rellenar formularios

Utilice este enfoque cuando el documento deba permanecer certificado pero los usuarios aún necesiten completar formularios interactivos o continuar firmando el archivo. El `FILLING_IN_FORMS` El nivel de permiso permite esos cambios controlados mientras se mantiene la certificación válida.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def certify_pdf_with_mdp_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        doc_mdp_signature = create_doc_mdp_signature(
            certificate_path,
            ap.forms.DocMDPAccessPermissions.FILLING_IN_FORMS,
            reason="Certified for form filling and signing",
        )
        pdf_signature.certify(
            1,
            "Certified for form filling and signing",
            "security@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            doc_mdp_signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Aplicar certificación a nivel de documento sin permitir cambios

Utilice este modo cuando el documento certificado debe permanecer sin cambios después de la certificación. El `NO_CHANGES` el nivel de permiso es apropiado para PDFs finalizados donde cualquier modificación posterior debería invalidar el estado de certificación.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def apply_document_level_certification(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        doc_mdp_signature = create_doc_mdp_signature(
            certificate_path,
            ap.forms.DocMDPAccessPermissions.NO_CHANGES,
            reason="Certified with no further changes allowed",
        )
        pdf_signature.certify(
            1,
            "Certified with no further changes allowed",
            "security@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            doc_mdp_signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
