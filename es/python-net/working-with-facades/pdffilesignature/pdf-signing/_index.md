---
title: Firmar documentos PDF
type: docs
weight: 10
url: /es/python-net/pdf-signing/
description: Aprenda cómo firmar documentos PDF en Python usando PdfFileSignature con firmas digitales basadas en certificado, con nombre y visibles.
lastmod: "2026-04-14"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Firmar documentos PDF con firmas digitales en Python
Abstract: Este artículo muestra cómo firmar documentos PDF con Aspose.PDF for Python via .NET usando la fachada PdfFileSignature. Cubre la configuración de certificados, la firma con parámetros básicos, la firma con un objeto PKCS7, la asignación de un nombre de firma y la aplicación de una apariencia de firma visible.
---

Aspose.PDF for Python via .NET proporciona la [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) fachada para aplicar firmas digitales a documentos PDF existentes. Usando un archivo de certificado, puedes firmar un documento programáticamente, colocar la firma en una página, asignar metadatos de la firma y personalizar cómo se muestra la firma.

Este artículo demuestra varios flujos de trabajo de firma comunes:

1. Crear y vincular un `PdfFileSignature` objeto al PDF de entrada.
1. Configure el certificado de firma.
1. Aplique una firma digital a la página objetivo.
1. Opcionalmente asigne un nombre de firma y una apariencia visible.
1. Guarde el PDF firmado.

## Preparar auxiliares reutilizables de firma

Antes de aplicar una firma digital a un PDF, es útil configurar un pequeño conjunto de funciones auxiliares reutilizables. Estas ayudas inicializan el manejador de firmas, definen el área visible de la firma, configuran el certificado y crean objetos de firma PKCS#7 reutilizables, de modo que los ejemplos de firma a continuación sean autocontenidos y más fáciles de seguir.

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

## Firmar un PDF con parámetros de certificado básicos

Este enfoque configura el certificado directamente en el `PdfFileSignature` objeto. Es útil cuando deseas un flujo de firma sencillo con metadatos de firma estándar y sin una gestión separada del objeto de firma.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_basic_parameters(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        configure_signature_certificate(pdf_signature, certificate_path)
        pdf_signature.sign(
            1,
            "Document approval",
            "qa@example.com",
            "New York, USA",
            False,
            create_signature_rectangle(),
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Firmar un PDF con un objeto PKCS7

Usa un `PKCS7` objeto cuando necesita preparar la firma primero y luego pasarla a la llamada de firma. Este patrón le brinda más control sobre la configuración de la firma y es una buena base para flujos de trabajo más avanzados.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_certificate_object(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        pdf_signature.sign(1, False, create_signature_rectangle(), signature)
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Firmar un PDF con una firma nombrada

Si el flujo de trabajo de su documento depende de un nombre de campo de firma predefinido, pase ese nombre a `sign()`. Esto hace que sea más fácil referenciar la firma más tarde para validación, procesamiento o integración con un flujo de aprobación.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def sign_pdf_with_named_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        signature.reason = "Approved by signing workflow"
        pdf_signature.sign(
            1,
            DEFAULT_SIGNATURE_NAME,
            "Approved by signing workflow",
            "qa@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```

## Aplicar una firma visible

Puede hacer que la firma sea visible en la página PDF asignando una apariencia personalizada al `PKCS7` objeto. Esto es útil cuando el documento de salida debe mostrar detalles de aprobación, como la razón, la ubicación y la información de contacto a los usuarios finales.

```python
import aspose.pdf.facades as pdf_facades
import sys
from os import path


def apply_visible_signature(infile, outfile, certificate_path):
    pdf_signature = create_pdf_file_signature(infile)
    try:
        signature = create_pkcs7_signature(certificate_path)
        signature.reason = "Visible approval signature"
        signature.custom_appearance = create_custom_signature_appearance()
        pdf_signature.sign(
            1,
            "Visible approval signature",
            "qa@example.com",
            "New York, USA",
            True,
            create_signature_rectangle(),
            signature,
        )
        pdf_signature.save(outfile)
    finally:
        pdf_signature.close()
```
