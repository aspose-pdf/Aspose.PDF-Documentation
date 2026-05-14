---
title: Clase PdfFileSignature
linktitle: Clase PdfFileSignature
type: docs
weight: 60
url: /es/python-net/pdffilesignature-class/
description: Explore como agregar, verificar y quitar firmas digitales de documentos PDF en Python usando la clase PDFFileSignature con Aspose.PDF.
lastmod: "2026-01-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

- [Firma de PDF](/pdf/python-net/pdf-signing/)
- [Certificacion de PDF](/pdf/python-net/pdf-certification/)
- [Administracion de firmas](/pdf/python-net/signature-management/)
- [Verificacion de firmas](/pdf/python-net/signature-verification/)
- [Informacion de firmas](/pdf/python-net/signature-information/)
- [Comprobaciones de integridad de firmas](/pdf/python-net/signature-integrity-checks/)
- [Revision y permisos](/pdf/python-net/revision-permissions/)
- [Extraccion de firmas](/pdf/python-net/signature-extraction/)
- [Administracion de derechos de uso](/pdf/python-net/usage-rights-management/)

## Preparar auxiliares de firma digital PDF

Antes de aplicar una firma digital a un PDF, es una buena practica configurar un conjunto de funciones auxiliares reutilizables. Estas funciones encapsulan tareas comunes, como inicializar el controlador de firmas, definir la ubicacion visual de la firma y configurar la firma basada en certificados, para que la logica principal de firma se mantenga limpia, coherente y facil de mantener.

### Que consigue esta configuracion

Esta capa auxiliar prepara todo lo necesario para un flujo de trabajo de firma fluido:

- Inicializa un objeto PdfFileSignature y lo enlaza a un documento
- Define donde aparecera la firma en la pagina
- Carga y aplica un certificado de firma
- Crea un objeto de firma PKCS#7 reutilizable con metadatos
- Personaliza el aspecto visual de la firma

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
import aspose.pydrawing as apd


DEFAULT_CERTIFICATE_PASSWORD = "Aspose2021"
DEFAULT_SIGNATURE_NAME = "Signature1"


def create_pdf_file_signature(infile):
    pdf_signature = pdf_facades.PdfFileSignature()
    pdf_signature.bind_pdf(infile)
    return pdf_signature


def create_signature_rectangle():
    return apd.Rectangle(10, 10, 200, 60)


def configure_signature_certificate(
    pdf_signature, certificate_path, certificate_password=DEFAULT_CERTIFICATE_PASSWORD
):
    pdf_signature.set_certificate(certificate_path, certificate_password)


def create_pkcs7_signature(
    certificate_path, certificate_password=DEFAULT_CERTIFICATE_PASSWORD
):
    signature = ap.forms.PKCS7(certificate_path, certificate_password)
    signature.reason = "Document approval"
    signature.contact_info = "qa@example.com"
    signature.location = "New York, USA"
    signature.authority = "Aspose.PDF Example"
    return signature


def create_custom_signature_appearance():
    appearance = ap.forms.SignatureCustomAppearance()
    appearance.font_family_name = "Arial"
    appearance.font_size = 10
    appearance.show_contact_info = True
    appearance.show_location = True
    appearance.show_reason = True
    return appearance
```
