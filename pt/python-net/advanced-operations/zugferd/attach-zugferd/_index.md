---
title: Criando PDF compatível com PDF/3-A e anexando fatura ZUGFeRD em Python
linktitle: Anexar ZUGFeRD ao PDF
type: docs
weight: 10
url: /pt/python-net/attach-zugferd/
description: Aprenda como gerar um documento PDF com ZUGFeRD no Aspose.PDF para Python via .NET
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como anexar ZUGFeRD a um documento PDF
Abstract: O artigo fornece um guia passo a passo sobre como anexar ZUGFeRD (um formato de notas fiscais eletrônicas) a um documento PDF usando a biblioteca Aspose.PDF. O procedimento começa com a importação da biblioteca necessária e a configuração dos caminhos de diretórios para arquivos de entrada e saída. Envolve carregar o arquivo PDF de destino em um objeto Document e criar um objeto FileSpecification para o arquivo XML de metadados da fatura. Propriedades-chave como `mime_type` e `af_relationship` são definidas para garantir a integração adequada dos metadados. O arquivo XML é então adicionado à coleção de arquivos incorporados do PDF, anexando-o efetivamente como metadados. Subsequentemente, o documento PDF é convertido para o formato PDF/A-3A, que é adequado para arquivamento de documentos eletrônicos, antes de salvar o PDF final com o ZUGFeRD incorporado. O artigo conclui com um trecho de código Python que demonstra a implementação dessas etapas, mostrando a integração do ZUGFeRD com um PDF para melhorar o gerenciamento de documentos.
---

## Anexar ZUGFeRD ao PDF

Recomendamos as seguintes etapas para anexar ZUGFeRD ao PDF:

1. Importe a biblioteca Aspose.PDF e dê-lhe um alias de ap para conveniência.
1. Defina o caminho para o diretório onde os arquivos PDF de entrada e saída estão localizados.
1. Defina o caminho para o arquivo PDF que será processado.
1. Carregue o arquivo PDF a partir da variável de caminho e crie um objeto Document.
1. Crie um objeto FileSpecification para o arquivo XML que contém os metadados da fatura. Use a variável de caminho e uma string de descrição para criar o objeto FileSpecification.
1. Defina as propriedades `mime_type` e `af_relationship` do objeto FileSpecification para `text/xml` e `ALTERNATIVE`, respectivamente.
1. Adicione o objeto fileSpecification à coleção de arquivos incorporados do objeto document. Isso anexa o arquivo XML ao documento PDF como um arquivo de metadados da fatura.
1. Converta o documento PDF para o formato PDF/A-3A. Use o caminho para o arquivo de log, a enumeração `PdfFormat.PDF_A_3A` e a enumeração `ConvertErrorAction.DELETE` para converter o objeto document.
1. Salve o documento PDF com o ZUGFeRD anexado.

```python
import aspose.pdf as ap

# Define the path to the directory where the input and output PDF files are located
_dataDir = "./"

# Load the PDF file that will be processed
path = _dataDir + "ZUGFeRD/ZUGFeRD-test.pdf"
document = ap.Document(path)

# Create a FileSpecification object for the XML file that contains the invoice metadata
description = "Invoice metadata conforming to ZUGFeRD standard"
path = _dataDir + "ZUGFeRD/factur-x.xml"
fileSpecification = ap.FileSpecification(path, description)

# Set the MIME type and the AFRelationship properties of the embedded file
fileSpecification.mime_type = "text/xml"
fileSpecification.af_relationship = ap.AFRelationship.ALTERNATIVE

# Add the embedded file to the PDF document's embedded files collection
document.embedded_files.add("factur",fileSpecification)

# Convert the PDF document to the PDF/A-3A format
path = _dataDir + "ZUGFeRD/log.xml"
document.convert(path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)

# Save the PDF document with the attached ZUGFeRD
path = _dataDir + "ZUGFeRD/ZUGFeRD-res.pdf"
document.save(path)
```

