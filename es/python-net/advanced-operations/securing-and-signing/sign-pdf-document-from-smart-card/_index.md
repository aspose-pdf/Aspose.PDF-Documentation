---
title: Firmar documentos PDF desde una Smart Card en Python
linktitle: Firma de PDF con Smart Card
type: docs
weight: 30
url: /es/python-net/sign-pdf-document-from-smart-card/
description: Aprenda a firmar documentos PDF con tarjetas inteligentes y certificados externos en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Firmar documentos PDF desde una Smart Card con Python
Abstract: Esta guía explica cómo firmar digitalmente documentos PDF usando una tarjeta inteligente con Aspose.PDF for Python via .NET. Demuestra cómo acceder a los certificados almacenados en dispositivos de hardware (como USB tokens o smart cards) a través del Windows Certificate Store y utilizarlos para firmar archivos PDF. La documentación incluye ejemplos de código que muestran cómo localizar el certificado adecuado, configurar las propiedades de la firma y incrustar la firma digital en el PDF. Esto permite una firma segura, respaldada por hardware, cumpliendo con los estándares de firma digital, adecuada para flujos de trabajo empresariales y legales de alta confianza.
---

Aspose.PDF ofrece capacidades robustas para integrar componentes de firma visual y criptográfica, garantizando tanto la autenticidad como una presentación profesional en documentos PDF firmados digitalmente.

Utilice este flujo de trabajo cuando su proceso de firma dependa de certificados almacenados en dispositivos con soporte de hardware, como tarjetas inteligentes, tokens USB o almacenes de certificados gestionados.

## Firmar con tarjeta inteligente usando campo de firma

Este ejemplo muestra cómo firmar digitalmente un documento PDF utilizando un certificado externo con Aspose.PDF for Python y aplicar una imagen personalizada de apariencia de firma:

1. Abriendo el documento PDF.
1. Creando un objeto PdfFileSignature y vinculándolo al documento.
1. Recuperando un certificado digital local mediante un método personalizado `get_local_certificate()`.
1. Configurando una ExternalSignature basada en el certificado seleccionado.
1. Aplicando una imagen de apariencia de firma personalizada (p.ej., un logotipo de la empresa o una firma manuscrita).
1. Firmando digitalmente la primera página del documento con metadatos especificados (razón, contacto, ubicación).
1. Guardando el documento firmado en un nuevo archivo de salida.

Este método es ideal para casos en los que las firmas deben aplicarse programáticamente usando certificados externos—como tokens de hardware, almacenes de certificados o proveedores de confianza—y presentarse con un diseño visual personalizado.

A continuación se muestran los fragmentos de código para firmar un documento PDF desde una tarjeta inteligente:

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def sign_with_smart_card(infile: str, outfile: str, pngfile: str) -> None:
    """Sign a PDF document using a smart-card certificate."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature() as pdf_signature:
            pdf_signature.bind_pdf(document)
            external_signature = ap.forms.ExternalSignature(get_local_certificate())
            pdf_signature.signature_appearance = pngfile
            pdf_signature.sign(
                1,
                "Reason",
                "Contact",
                "Location",
                True,
                drawing.Rectangle(100, 100, 200, 200),
                external_signature,
            )
            pdf_signature.save(outfile)
```

## Verificar firmas digitales

Este fragmento de código muestra cómo verificar firmas digitales en un documento PDF usando Aspose.PDF for Python:

1. Abriendo el archivo PDF.
1. Crear un objeto 'PdfFileSignature' y vincularlo al documento.
1. Recuperar la lista de todos los nombres de campos de firma usando 'get_signature_names()'.
1. Iterar a través de cada firma y verificar su validez con 'verify_signature()'.
1. Lanzar una excepción si alguna firma no pasa la verificación.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def verify_external_signature(infile: str) -> None:
    """Verify an external signature in a PDF document."""
    with ap.Document(infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            for signature_name in pdf_signature.get_signature_names(True):
                if not pdf_signature.verify_signature(signature_name):
                    raise Exception("Not verified")
```

## Firmar con certificado externo

Este fragmento de código muestra cómo agregar y firmar un campo de firma digital en un documento PDF usando Aspose.PDF for Python con un certificado externo:

1. Abriendo el archivo PDF como un flujo binario.
1. Creando un SignatureField y colocándolo en la primera página del documento en una posición especificada.
1. Recuperando un certificado digital local mediante un método personalizado `get_local_certificate()`.
1. Configurando un ExternalSignature con metadatos como autoridad, motivo y información de contacto.
1. Asignando un nombre de campo único al campo de firma (partial_name = \"sig1\").
1. Agregar el campo de firma a los campos del formulario del PDF.
1. Firmando el campo con el certificado externo.
1. Guardando el documento firmado en un archivo de salida.

```python
import sys
from os import path
import aspose.pdf as ap
import aspose.pydrawing as drawing

def get_signature_info_using_signature_field(infile: str, outfile: str) -> None:
    """Create a signature field and sign it with an external certificate."""
    with open(infile, "rb+") as file_stream:
        document = ap.Document(file_stream)
        signature_field = ap.forms.SignatureField(
            document.pages[1],
            ap.Rectangle(100, 400, 10, 10, True),
        )
        selected_certificate = get_local_certificate()
        external_signature = ap.forms.ExternalSignature(selected_certificate)
        external_signature.authority = "Me"
        external_signature.reason = "Reason"
        external_signature.contact_info = "Contact"
        signature_field.partial_name = "sig1"
        document.form.add(signature_field, 1)
        signature_field.sign(external_signature)
        document.save(outfile)
```

## Temas de Seguridad Relacionados

- [Protege y firma archivos PDF en Python](/pdf/es/python-net/securing-and-signing/)
- [Firmar digitalmente archivos PDF en Python](/pdf/es/python-net/digitally-sign-pdf-file/)
- [Extraer información de la firma del PDF en Python](/pdf/es/python-net/extract-image-and-signature-information/)
- [Cifrar y descifrar archivos PDF en Python](/pdf/es/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)

