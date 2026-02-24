---
title: Adicionar assinatura digital ou assinar PDF digitalmente em Python
linktitle: Assinar PDF digitalmente
type: docs
weight: 10
url: /pt/python-net/digitally-sign-pdf-file/
description: Assine documentos PDF digitalmente, verifique ou valide os PDFs assinados digitalmente usando Python.
lastmod: "2025-06-07"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Assine arquivos PDF digitalmente com Python
Abstract: Este guia explica como assinar documentos PDF digitalmente usando Aspose.PDF para Python via .NET. Detalha o processo de aplicação de assinaturas digitais padrão e avançadas, utilizando certificados (PFX e PKCS#12), e personalizando a aparência e o comportamento da assinatura. A documentação inclui exemplos de código que demonstram como assinar PDFs existentes, adicionar carimbos de tempo e verificar a validade da assinatura. Isso permite que os desenvolvedores garantam a autenticidade, integridade e conformidade dos documentos com os padrões de assinatura digital em suas aplicações Python.
---

## Assinar PDF com assinaturas digitais

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    ppath_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate PdfFileSignature object
        with ap.facades.PdfFileSignature(document) as signature:
            # Create PKCS#7 object for sign
            pkcs = ap.forms.PKCS7(path_pfxfile, "12345")
            # Sign PDF file
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            #  Save PDF document
            signature.save(path_outfile)
```

Uma **assinatura PKCS#7 destacada** adiciona uma assinatura digital a um documento sem incorporar o conteúdo ao bloco da assinatura.

O próximo exemplo assina um documento PDF usando uma assinatura digital PKCS#7 destacada, aplicando a assinatura na primeira página em uma área retangular especificada.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate PdfFileSignature object using the opened document
        with ap.facades.PdfFileSignature(document) as signature:
            # Create PKCS#7 detached object for sign
            pkcs = ap.forms.PKCS7Detached(path_pfxfile, password, ap.DigestHashAlgorithm.SHA256)
            # Sign PDF file
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            #  Save PDF document
            signature.save(path_outfile)
```

Este trecho de código Python verifica uma assinatura digital em um arquivo PDF usando o método 'file_sign.verify_signature()'.

1. Cria uma instância de PdfFileSignature que permite interagir com assinaturas em PDF.
1. Obtém uma lista de nomes de assinaturas `get_signature_names(True)`.
1. Verifica a primeira assinatura da lista `verify_signature` em conformidade com o certificado especificado.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Create an instance of PdfFileSignature for working with signatures in the document
    with ap.facades.PdfFileSignature(path_infile) as file_sign:
        # Get a list of signatures
        signature_names = file_sign.get_signature_names(True)
        # Verify the signature with the given name.
        return file_sign.verify_signature(signature_names[0], certificate)
```

## Adicionar carimbo de tempo à assinatura digital

### Como assinar digitalmente um PDF com carimbo de tempo

Aspose.PDF para Python oferece suporte para assinar digitalmente o PDF com um servidor ou serviço web de carimbo de tempo.

Para atender a esse requisito, a classe [TimestampSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) foi adicionada ao namespace Aspose.PDF. Por favor, veja o trecho de código a seguir que obtém o carimbo de tempo e o adiciona ao documento PDF:

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of PdfFileSignature for working with signatures in the document
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(path_pfxfile, password)
            # Create TimestampSettings settings
            timestamp_settings = ap.TimestampSettings("https://freetsa.org/tsr",
                                                                "", ap.DigestHashAlgorithm.SHA256)  # User/Password can be omitted
            pkcs.timestamp_settings = timestamp_settings
            rect = drawing.Rectangle(100, 100, 200, 100)  # Creating a rectangle for the signature
            # Create any of the three signature types
            signature.sign(1, "Signature Reason", "Contact", "Location", True, rect, pkcs)
            # Save PDF document
                signature.save(path_outfile)
```

## Assinando documentos PDF usando ECDSA

Assinar documentos PDF usando ECDSA (Algoritmo de Assinatura Digital de Curva Elíptica) envolve a utilização de criptografia de curva elíptica para gerar assinaturas digitais.

O trecho de código acima ilustra como aplicar uma assinatura digital PKCS#7 destacada a um documento PDF usando Aspose.PDF para Python. Ao carregar o documento, configurar a aparência da assinatura e as configurações de segurança, e salvar o resultado, este exemplo demonstra um fluxo de trabalho completo e confiável para assinar digitalmente arquivos PDF.

Este método garante a autenticidade e integridade do documento ao incorporar uma assinatura segura e verificável na primeira página. O uso de SHA-256 como algoritmo de digest atende aos padrões criptográficos modernos, enquanto a capacidade de controlar a posição da assinatura oferece flexibilidade para marcas de aprovação visíveis.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of PdfFileSignature to sign the document
        with ap.facades.PdfFileSignature(document) as signature:
            # Create a PKCS7Detached object using the provided certificate and password
            pkcs = ap.forms.PKCS7Detached(path_pfxfile, password, ap.DigestHashAlgorithm.SHA256)

            # Sign the first page of the document, setting the signature's appearance at the specified location
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)

            # Save PDF document
            signature.save(path_outfile)
```
