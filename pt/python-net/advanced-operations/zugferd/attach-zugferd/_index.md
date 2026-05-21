---
title: Criando PDF compatível com PDF/3-A e anexando fatura ZUGFeRD em Python
linktitle: Anexar ZUGFeRD ao PDF
type: docs
weight: 10
url: /pt/python-net/attach-zugferd/
description: Aprenda como gerar um documento PDF com ZUGFeRD no Aspose.PDF for Python via .NET
lastmod: "2026-05-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como anexar ZUGFeRD a um documento PDF
Abstract: O artigo oferece um guia passo a passo sobre como anexar ZUGFeRD (um formato para faturas eletrônicas) a um documento PDF usando a biblioteca Aspose.PDF. O procedimento começa com a importação da biblioteca necessária e a configuração dos caminhos de diretório para arquivos de entrada e saída. Ele envolve carregar o arquivo PDF de destino em um objeto Document e criar um objeto FileSpecification para o arquivo XML de metadados da fatura. Propriedades chave como `mime_type` e `af_relationship` são definidas para garantir a integração adequada dos metadados. O arquivo XML é então adicionado à coleção de arquivos incorporados do PDF, anexando-o efetivamente como metadados. Em seguida, o documento PDF é convertido para o formato PDF/A-3A, que é adequado para arquivamento de documentos eletrônicos, antes de salvar o PDF final com o ZUGFeRD incorporado. O artigo conclui com um trecho de código Python que demonstra a implementação dessas etapas, exibindo a integração do ZUGFeRD com um PDF para melhorar a gestão de documentos.
---

## Anexar ZUGFeRD ao PDF

Recomendamos os seguintes passos para anexar ZUGFeRD ao PDF:

1. Importe a biblioteca Aspose.PDF e dê-lhe um alias de ap para conveniência.
1. Defina o caminho para o diretório onde os arquivos PDF de entrada e saída estão localizados.
1. Defina o caminho para o arquivo PDF que será processado.
1. Carregue o arquivo PDF a partir da variável de caminho e crie um objeto Document.
1. Crie um objeto FileSpecification para o arquivo XML que contém os metadados da fatura. Use a variável de caminho e uma string de descrição para criar o objeto FileSpecification.
1. Definir o `mime_type` e o `af_relationship` propriedades do objeto FileSpecification para `text/xml` e `ALTERNATIVE`, respectivamente.
1. Adicione o objeto fileSpecification à coleção de arquivos incorporados do objeto document. Isso anexa o arquivo XML ao documento PDF como um arquivo de metadados de fatura.
1. Converta o documento PDF para o formato PDF/A-3A. Use o caminho para o arquivo de log, o `PdfFormat.PDF_A_3A` enumeração, e o `ConvertErrorAction.DELETE` enumeração para converter o objeto do documento.
1. Salve o documento PDF com o ZUGFeRD anexado.

```python
import sys
import os
import aspose.pdf as ap

def attach_invoice_zugferd_format(infile, invoice, outfile):
    document = ap.Document(infile)

    # Create a FileSpecification object for the XML file that contains the invoice metadata
    description = "Invoice metadata conforming to ZUGFeRD standard"
    file_specification = ap.FileSpecification(invoice, description)

    # Set the MIME type and the AFRelationship properties of the embedded file
    file_specification.mime_type = "text/xml"
    file_specification.af_relationship = ap.AFRelationship.ALTERNATIVE

    # Add the embedded file to the PDF document's embedded files collection
    document.embedded_files.add("factur", file_specification)

    # Convert the PDF document to the PDF/A-3A format
    log_path = outfile.replace(".pdf", "_log.xml")
    document.convert(log_path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```
