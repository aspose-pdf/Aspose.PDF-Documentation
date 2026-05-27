---
title: Assinar documentos PDF
type: docs
weight: 10
url: /pt/python-net/pdf-signing/
description: Aprenda como assinar documentos PDF em Python usando PdfFileSignature com assinaturas digitais baseadas em certificado, nomeadas e visíveis.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Assinar documentos PDF com assinaturas digitais em Python
Abstract: Este artigo mostra como assinar documentos PDF com Aspose.PDF for Python via .NET usando a fachada PdfFileSignature. Ele abrange a configuração de certificado, assinatura com parâmetros básicos, assinatura com um objeto PKCS7, atribuição de um nome de assinatura e aplicação de uma aparência de assinatura visível.
---

Aspose.PDF for Python via .NET fornece o [PdfFileSignature](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffilesignature/) fachada para aplicar assinaturas digitais a documentos PDF existentes. Usando um arquivo de certificado, você pode assinar um documento programaticamente, colocar a assinatura em uma página, atribuir metadados da assinatura e personalizar como a assinatura é exibida.

Este artigo demonstra vários fluxos de trabalho comuns de assinatura:

1. Criar e vincular um `PdfFileSignature` objeto para o PDF de entrada.
1. Configure o certificado de assinatura.
1. Aplique uma assinatura digital na página de destino.
1. Opcionalmente, atribua um nome de assinatura e aparência visível.
1. Salve o PDF assinado.

## Prepare reusable signing helpers

Antes de aplicar uma assinatura digital a um PDF, é útil configurar um pequeno conjunto de funções auxiliares reutilizáveis. Essas funções inicializam o manipulador de assinatura, definem a área de assinatura visível, configuram o certificado e criam objetos de assinatura PKCS#7 reutilizáveis, de modo que os exemplos de assinatura abaixo permaneçam autocontidos e mais fáceis de seguir.

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

## Assine um PDF com parâmetros básicos de certificado

Esta abordagem configura o certificado diretamente no `PdfFileSignature` objeto. É útil quando você deseja um fluxo de assinatura direto com metadados de assinatura padrão e sem gerenciamento separado de objetos de assinatura.

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

## Assinar um PDF com um objeto PKCS7

Use um `PKCS7` objeto quando você precisa preparar a assinatura primeiro e então passá‑la para a chamada de assinatura. Esse padrão lhe dá mais controle sobre as configurações da assinatura e é uma boa base para fluxos de trabalho mais avançados.

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

## Assine um PDF com uma assinatura nomeada

Se o fluxo de trabalho do seu documento depende de um nome de campo de assinatura predefinido, passe esse nome para `sign()`. Isso torna mais fácil referenciar a assinatura mais tarde para validação, processamento ou integração com um fluxo de trabalho de aprovação.

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

## Aplicar uma assinatura visível

Você pode tornar a assinatura visível na página PDF atribuindo uma aparência personalizada ao `PKCS7` objeto. Isso é útil quando o documento de saída deve mostrar detalhes de aprovação, como o motivo, a localização e as informações de contato para os usuários finais.

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
