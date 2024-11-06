---
title: Criando PDF compatível com PDF/3-A e anexando fatura ZUGFeRD em Python
linktitle: Anexar ZUGFeRD ao PDF
type: docs
weight: 10
url: pt/python-net/attach-zugferd/
description: Aprenda a gerar um documento PDF com ZUGFeRD no Aspose.PDF para Python via .NET
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Anexar ZUGFeRD ao PDF

Recomendamos seguir os passos para anexar ZUGFeRD ao PDF:

1. Importe a biblioteca Aspose.PDF e dê-lhe um alias de ap para conveniência.
1. Defina o caminho para o diretório onde os arquivos PDF de entrada e saída estão localizados.
1. Defina o caminho para o arquivo PDF que será processado.
1. Carregue o arquivo PDF a partir da variável de caminho e crie um objeto Document.
1. Crie um objeto FileSpecification para o arquivo XML que contém os metadados da fatura. Use a variável de caminho e uma string de descrição para criar o objeto FileSpecification.

1. Defina as propriedades `mime_type` e `af_relationship` do objeto FileSpecification para `text/xml` e `ALTERNATIVE`, respectivamente.
1. Adicione o objeto fileSpecification à coleção de arquivos incorporados do objeto documento. Isso anexa o arquivo XML ao documento PDF como um arquivo de metadados de fatura.
1. Converta o documento PDF para o formato PDF/A-3A. Use o caminho para o arquivo de log, a enumeração `PdfFormat.PDF_A_3A` e a enumeração `ConvertErrorAction.DELETE` para converter o objeto documento.
1. Salve o documento PDF com o ZUGFeRD anexado.

```python
import aspose.pdf as ap

# Defina o caminho para o diretório onde os arquivos PDF de entrada e saída estão localizados
_dataDir = "./"

# Carregue o arquivo PDF que será processado
path = _dataDir + "ZUGFeRD/ZUGFeRD-test.pdf"
document = ap.Document(path)

# Crie um objeto FileSpecification para o arquivo XML que contém os metadados da fatura
description = "Metadados da fatura em conformidade com o padrão ZUGFeRD"
path = _dataDir + "ZUGFeRD/factur-x.xml"
fileSpecification = ap.FileSpecification(path, description)

# Defina o tipo MIME e as propriedades AFRelationship do arquivo incorporado
fileSpecification.mime_type = "text/xml"
fileSpecification.af_relationship = ap.AFRelationship.ALTERNATIVE

# Adicione o arquivo incorporado à coleção de arquivos incorporados do documento PDF
document.embedded_files.add("factur", fileSpecification)

# Converta o documento PDF para o formato PDF/A-3A
path = _dataDir + "ZUGFeRD/log.xml"
document.convert(path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)

# Salve o documento PDF com o ZUGFeRD anexado
path = _dataDir + "ZUGFeRD/ZUGFeRD-res.pdf"
document.save(path)
```