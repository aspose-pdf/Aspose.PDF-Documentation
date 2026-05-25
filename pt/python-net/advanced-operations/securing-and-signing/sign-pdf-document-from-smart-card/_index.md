---
title: Assinar documentos PDF de um Cartão Inteligente em Python
linktitle: Assinatura de PDF com Cartão Inteligente
type: docs
weight: 30
url: /pt/python-net/sign-pdf-document-from-smart-card/
description: Aprenda como assinar documentos PDF com Cartões Inteligentes e certificados externos em Python
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Assinar documentos PDF de um Cartão Inteligente com Python
Abstract: Este guia explica como assinar digitalmente documentos PDF usando um smart card com Aspose.PDF for Python via .NET. Ele demonstra como acessar certificados armazenados em dispositivos de hardware (como tokens USB ou smart cards) através do Windows Certificate Store e aplicá‑los para assinar arquivos PDF. A documentação inclui exemplos de código que mostram como localizar o certificado apropriado, configurar as propriedades da assinatura e incorporar a assinatura digital no PDF. Isso permite assinaturas seguras, baseadas em hardware, em conformidade com os padrões de assinatura digital, adequadas para fluxos de trabalho empresariais e jurídicos de alta confiança.
---

Aspose.PDF oferece recursos robustos para integrar componentes de assinatura visual e criptográfica, garantindo tanto a autenticidade quanto a apresentação profissional em documentos PDF assinados digitalmente.

Use este fluxo de trabalho quando seu processo de assinatura depender de certificados armazenados em dispositivos com suporte de hardware, como smart cards, tokens USB ou repositórios de certificados gerenciados.

## Assinar com Smart Card usando Campo de Assinatura

Este exemplo demonstra como assinar digitalmente um documento PDF usando um certificado externo com Aspose.PDF for Python e aplicar uma imagem personalizada de aparência da assinatura:

1. Abrindo o documento PDF.
1. Criando um objeto PdfFileSignature e vinculando‑o ao documento.
1. Recuperando um certificado digital local usando um método personalizado `get_local_certificate()`.
1. Configurando um ExternalSignature com base no certificado selecionado.
1. Aplicando uma imagem de aparência de assinatura personalizada (por exemplo, um logotipo da empresa ou assinatura manuscrita).
1. Assinando digitalmente a primeira página do documento com metadados especificados (razão, contato, localização).
1. Salvando o documento assinado em um novo arquivo de saída.

Este método é ideal para casos em que as assinaturas precisam ser aplicadas programaticamente usando certificados externos — como tokens de hardware, armazenamentos de certificados ou provedores confiáveis — e apresentadas com um layout visual personalizado.

A seguir estão os trechos de código para assinar um documento PDF a partir de um smart card:

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

## Verificar Assinaturas Digitais

Este trecho de código demonstra como verificar assinaturas digitais em um documento PDF usando Aspose.PDF for Python:

1. Abrindo o arquivo PDF.
1. Criando um 'PdfFileSignature object' e vinculando‑o ao documento.
1. Recuperando a lista de todos os nomes de campos de assinatura usando 'get_signature_names()'.
1. Iterando por cada assinatura e verificando sua validade com 'verify_signature()'.
1. Lançando uma exceção se alguma assinatura falhar na verificação.

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

## Assinar com Certificado Externo

Este trecho de código demonstra como adicionar e assinar um campo de assinatura digital em um documento PDF usando Aspose.PDF for Python com um certificado externo:

1. Abrindo o arquivo PDF como um fluxo binário.
1. Criando um SignatureField e posicionando‑o na primeira página do documento em uma posição especificada.
1. Recuperando um certificado digital local usando um método personalizado `get_local_certificate()`.
1. Configurando um ExternalSignature com metadados como autoridade, motivo e informações de contato.
1. Atribuindo um nome de campo exclusivo ao campo de assinatura (partial_name = "sig1").
1. Adicionando o campo de assinatura aos campos de formulário do PDF.
1. Assinando o campo com o certificado externo.
1. Salvando o documento assinado em um arquivo de saída.

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

## Tópicos de Segurança Relacionados

- [Proteja e assine arquivos PDF em Python](/pdf/pt/python-net/securing-and-signing/)
- [Assinar digitalmente arquivos PDF em Python](/pdf/pt/python-net/digitally-sign-pdf-file/)
- [Extrair informações de assinatura de PDF em Python](/pdf/pt/python-net/extract-image-and-signature-information/)
- [Criptografar e descriptografar arquivos PDF em Python](/pdf/pt/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)

