---
title: Firma documentos PDF desde una tarjeta inteligente en Python
linktitle: Firma de PDF con tarjeta inteligente
type: docs
weight: 30
url: /es/python-net/sign-pdf-document-from-smart-card/
description: Aprende cómo firmar documentos PDF con tarjetas inteligentes y certificados externos en Python.
lastmod: "2026-04-15"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true 
AlternativeHeadline: Firma documentos PDF desde una tarjeta inteligente con Python
Abstract: Esta guia explica como firmar digitalmente documentos PDF usando una tarjeta inteligente con Aspose.PDF para Python a traves de .NET. Demuestra como acceder a los certificados almacenados en dispositivos de hardware, como tokens USB o tarjetas inteligentes, a traves del almacen de certificados de Windows y aplicarlos para firmar archivos PDF. La documentacion incluye ejemplos de codigo que muestran como localizar el certificado adecuado, configurar las propiedades de la firma e incrustar la firma digital en el PDF. Esto permite una firma segura respaldada por hardware, adecuada para flujos de trabajo empresariales y legales de alta confianza.
---

Aspose.PDF ofrece capacidades robustas para integrar componentes de firma visual y criptográfica, garantizando tanto la autenticidad como la presentación profesional en documentos PDF firmados digitalmente.

Utilice este flujo de trabajo cuando su proceso de firma dependa de certificados almacenados en dispositivos respaldados por hardware, como tarjetas inteligentes, tokens USB o almacenes de certificados administrados.

## Firmar con tarjeta inteligente usando campo de firma

Este ejemplo muestra cómo firmar digitalmente un documento PDF utilizando un certificado externo con Aspose.PDF for Python y aplicar una imagen personalizada de apariencia de firma:

1. Abriendo el documento PDF.
1. Creando un objeto PdfFileSignature y vinculándolo al documento.
1. Recuperando un certificado digital local mediante un método personalizado `get_local_certificate()`.
1. Configurando una ExternalSignature basada en el certificado seleccionado.
1. Aplicando una imagen de apariencia de firma personalizada (p. ej., un logotipo de la empresa o una firma manuscrita).
1. Firmando digitalmente la primera página del documento con los metadatos especificados (razón, contacto, ubicación).
1. Guardando el documento firmado en un nuevo archivo de salida.

Este método es ideal para los casos en los que las firmas deben aplicarse programáticamente utilizando certificados externos —como tokens de hardware, almacenes de certificados o proveedores confiables— y presentarse con un diseño visual personalizado.

A continuación se muestran los fragmentos de código para firmar un documento PDF desde una tarjeta inteligente:

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing

path_infile = self.data_dir + infile
path_outfile = self.data_dir + outfile
path_pngfile = self.data_dir + pngfile

# Open PDF document
with ap.Document(path_infile) as document:
    with ap.facades.PdfFileSignature() as pdf_signature:
        # Bind PDF document
        pdf_signature.bind_pdf(document)
        selected_certificates = self.get_local_certificate()
        # Set an external signature settings
        external_signature = ap.forms.ExternalSignature(selected_certificates)
        pdf_signature.signature_appearance = path_pngfile
        # Sign the document
        pdf_signature.sign(
            1,
            "Reason",
            "Contact",
            "Location",
            True,
            drawing.Rectangle(100, 100, 200, 200),
            external_signature,
        )
        # Save PDF document
        pdf_signature.save(path_outfile)
```

## Verificar firmas digitales

Este fragmento de código muestra cómo verificar firmas digitales en un documento PDF utilizando Aspose.PDF for Python:

1. Abriendo el archivo PDF.
1. Crear un objeto 'PdfFileSignature' y vincularlo al documento.
1. Recuperar la lista de todos los nombres de campos de firma usando 'get_signature_names()'.
1. Iterar a través de cada firma y verificar su validez con 'verify_signature()'.
1. Lanzar una excepción si alguna firma falla la verificación.

```python
import aspose.pdf as ap

path_infile = self.data_dir + infile

# Open PDF document
with ap.Document(path_infile) as document:
    with ap.facades.PdfFileSignature(document) as pdf_signature:
        signature_names = pdf_signature.get_signature_names(True)
        for index in range(len(signature_names)):
            if not pdf_signature.verify_signature(signature_names[index]):
                raise Exception("Not verified")
```

## Firmar con certificado externo

Este fragmento de código demuestra cómo agregar y firmar un campo de firma digital en un documento PDF usando Aspose.PDF for Python con un certificado externo:

1. Abriendo el archivo PDF como una secuencia binaria.
1. Crear un SignatureField y colocarlo en la primera página del documento en una posición especificada.
1. Recuperando un certificado digital local mediante un método personalizado `get_local_certificate()`.
1. Configurar un ExternalSignature con metadatos como autoridad, razón e información de contacto.
1. Asignar un nombre de campo único al campo de firma (partial_name = "sig1").
1. Agregar el campo de firma a los campos de formulario del PDF.
1. Firmando el campo con el certificado externo.
1. Guardando el documento firmado en un archivo de salida.

```python
import aspose.pdf as ap

path_infile = self.data_dir + infile
path_outfile = self.data_dir + outfile

# Open a document stream
with open(path_infile, "rb+") as file_stream:
    # Open PDF document from stream
    document = ap.Document(file_stream)

    # Create a signature field
    signature_field = ap.forms.SignatureField(
        document.pages[1], ap.Rectangle(100, 400, 10, 10, True)
    )
    selected_certificate = self.get_local_certificate()

    # Set external signature settings
    external_signature = ap.forms.ExternalSignature(selected_certificate)
    external_signature.authority = "Me"
    external_signature.reason = "Reason"
    external_signature.contact_info = "Contact"

    # Set a name of signature field
    signature_field.partial_name = "sig1"

    # Add the signature field to the document
    document.form.add(signature_field, 1)

    # Sign the document
    signature_field.sign(external_signature)

    # Save PDF document
    document.save(path_outfile)
```

## Temas de seguridad relacionados

- [Asegurar y firmar archivos PDF en Python](/pdf/es/python-net/securing-and-signing/)
- [Firmar digitalmente archivos PDF en Python](/pdf/es/python-net/digitally-sign-pdf-file/)
- [Extraer información de la firma del PDF en Python](/pdf/es/python-net/extract-image-and-signature-information/)
- [Cifrar y descifrar archivos PDF en Python](/pdf/es/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)

