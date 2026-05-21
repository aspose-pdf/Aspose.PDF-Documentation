---
title: Classe PdfFileSignature
type: docs
weight: 60
url: /pt/python-net/pdffilesignature-class/
description: Explore como adicionar, verificar e remover assinaturas digitais de documentos PDF em Python usando a classe PdfFileSignature com Aspose.PDF.
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

- [Assinatura de PDF](/pdf/pt/python-net/pdf-signing/)
- [Certificação de PDF](/pdf/pt/python-net/pdf-certification/)
- [Gerenciamento de Assinaturas](/pdf/pt/python-net/signature-management/)
- [Verificação de Assinatura](/pdf/pt/python-net/signature-verification/)
- [Informações da Assinatura](/pdf/pt/python-net/signature-information/)
- [Verificações de Integridade de Assinatura](/pdf/pt/python-net/signature-integrity-checks/)
- [Revisão & Permissões](/pdf/pt/python-net/revision-permissions/)
- [Extração de Assinatura](/pdf/pt/python-net/signature-extraction/)
- [Gerenciamento de Direitos de Uso](/pdf/pt/python-net/usage-rights-management/)

## Preparando Auxiliares de Assinatura Digital PDF

Antes de aplicar uma assinatura digital a um PDF, é uma prática recomendada configurar um grupo de funções auxiliares reutilizáveis. Essas funções encapsulam tarefas comuns — como inicializar o manipulador de assinatura, definir a posição visual da assinatura e configurar a assinatura baseada em certificado — para que a lógica principal de assinatura permaneça limpa, consistente e fácil de manter.

### O que esta configuração alcança

Esta camada auxiliar prepara tudo o que é necessário para um fluxo de assinatura tranquilo:

- Inicializa um objeto PdfFileSignature e o vincula a um documento
- Define onde a assinatura aparecerá na página
- Carrega e aplica um certificado de assinatura
- Cria um objeto de assinatura PKCS#7 reutilizável com metadados
- Personaliza a aparência visual da assinatura

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
