---
title: Como adicionar assinatura de Smart Card ao PDF
linktitle: Assinatura de PDF com Smart Card
type: docs
weight: 30
url: /pt/python-net/sign-pdf-document-from-smart-card/
description: Aspose.PDF para Python via .NET permite que você assine documentos PDF a partir de um smart card usando campo de assinatura.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Assine documentos PDF a partir de um Smart Card com Python
Abstract: Este guia explica como assinar digitalmente documentos PDF usando um smart card com Aspose.PDF para Python via .NET. Ele demonstra como acessar certificados armazenados em dispositivos de hardware (como tokens USB ou smart cards) através do Windows Certificate Store e aplicá‑los para assinar arquivos PDF. A documentação inclui exemplos de código que mostram como localizar o certificado apropriado, configurar as propriedades da assinatura e incorporar a assinatura digital no PDF. Isso permite assinaturas seguras, suportadas por hardware, em conformidade com os padrões de assinatura digital, adequadas para fluxos de trabalho empresariais e jurídicos de alta confiabilidade.
---

Aspose.PDF fornece recursos robustos para integrar componentes de assinatura visual e criptográfica, garantindo tanto autenticidade quanto apresentação profissional em documentos PDF assinados digitalmente.

## Assinar com Smart Card usando Campo de Assinatura

Este exemplo demonstra como assinar digitalmente um documento PDF usando um certificado externo com Aspose.PDF para Python e aplicar uma imagem de aparência de assinatura personalizada:

1. Abrindo o documento PDF.
1. Criando um objeto PdfFileSignature e vinculando‑o ao documento.
1. Recuperando um certificado digital local usando um método personalizado `get_local_certificate()`.
1. Configurando um ExternalSignature com base no certificado selecionado.
1. Aplicando uma imagem de aparência de assinatura personalizada (por exemplo, o logotipo da empresa ou assinatura manuscrita).
1. Assinando digitalmente a primeira página do documento com metadados especificados (razão, contato, localização).
1. Salvando o documento assinado em um novo arquivo de saída.

Este método é ideal para casos onde as assinaturas devem ser aplicadas programaticamente usando certificados externos — como tokens de hardware, repositórios de certificados ou provedores confiáveis — e apresentadas com um layout visual personalizado.

A seguir, trechos de código para assinar um documento PDF a partir de um smart card:

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
            pdf_signature.sign(1, "Reason", "Contact", "Location", True, drawing.Rectangle(100, 100, 200, 200),
                                external_signature)
            # Save PDF document
            pdf_signature.save(path_outfile)
```

## Verificar Assinaturas Digitais

Este trecho de código demonstra como verificar assinaturas digitais em um documento PDF usando Aspose.PDF para Python:

1. Abrindo o arquivo PDF.
1. Criando um objeto 'PdfFileSignature' e vinculando‑o ao documento.
1. Recuperando a lista de todos os nomes de campos de assinatura usando 'get_signature_names()'.
1. Iterando por cada assinatura e verificando sua validade com 'verify_signature()'.
1. Levantando uma exceção se alguma assinatura falhar na verificação.

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

## Assinar com Certificado Externo

Este trecho de código demonstra como adicionar e assinar um campo de assinatura digital em um documento PDF usando Aspose.PDF para Python com um certificado externo:

1. Abrindo o arquivo PDF como um fluxo binário.
1. Criando um SignatureField e posicionando‑o na primeira página do documento em uma posição especificada.
1. Recuperando um certificado digital local usando um método personalizado `get_local_certificate()`.
1. Configurando um ExternalSignature com metadados como autoridade, razão e informações de contato.
1. Atribuindo um nome de campo único ao campo de assinatura (partial_name = "sig1").
1. Adicionando o campo de assinatura aos campos de formulário do PDF.
1. Assinando o campo com o certificado externo.
1. Salvando o documento assinado em um arquivo de saída.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open a document stream
    with open(path_infile, "rb+") as file_stream:
        # Open PDF document from stream
        document = ap.Document(file_stream)

        # Create a signature field
        signature_field = ap.forms.SignatureField(document.pages[1], ap.Rectangle(100, 400, 10, 10, True))
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


