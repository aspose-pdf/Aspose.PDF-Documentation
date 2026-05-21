---
title: Converter PDF/A e PDF/UA para PDF em Python
linktitle: Converter PDF/A e PDF/UA para PDF
type: docs
weight: 120
url: /pt/python-net/convert-pdf_x-to-pdf/
lastmod: "2026-05-18"
description: Saiba como remover a conformidade PDF/A e PDF/UA de arquivos PDF em Python com Aspose.PDF for Python via .NET e salvá-los como documentos PDF padrão.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Como converter PDF/A e PDF/UA para PDF padrão em Python
Abstract: Este artigo explica como remover a conformidade PDF/A e PDF/UA de documentos PDF baseados em padrões usando Aspose.PDF for Python via .NET. Ele aborda cenários em que você pode precisar de um PDF padrão em vez de um arquivo de arquivamento ou com restrições de acessibilidade, e mostra como salvar o resultado após remover os metadados e restrições de conformidade.
---

Use esta página quando precisar converter um PDF baseado em padrões, como PDF/A ou PDF/UA, de volta para um documento PDF regular para edição, processamento ou redistribuição posteriores.

PDFs compatíveis com padrões são úteis para fluxos de trabalho de arquivamento, impressão e acessibilidade, mas em alguns casos pode ser necessário remover essa conformidade antes de integrar o arquivo em outros sistemas ou pipelines. Aspose.PDF for Python via .NET permite fazer isso programaticamente e então salvar o resultado como um arquivo PDF padrão.

## Converter PDF/A para PDF

Este exemplo remove os metadados e restrições de conformidade PDF/A de um PDF para que o documento possa ser salvo novamente como um arquivo PDF padrão.

1. Carregue o documento PDF usando 'ap.Document'.
1. Chame ‘remove_pdfa_compliance()’ para remover todas as configurações e metadados de conformidade relacionados ao PDF/A.
1. Salve o PDF resultante no caminho de saída.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDFA_to_PDF(infile, outfile):
    document = ap.Document(infile)
    document.remove_pdfa_compliance()
    document.save(outfile)
```

## Removendo conformidade PDF/UA

Este exemplo demonstra como remover a conformidade relacionada ao PDF/UA para que o documento possa ser salvo como um PDF padrão para fluxos de trabalho que não são específicos de acessibilidade.

1. Carregue o documento PDF usando 'ap.Document()'.
1. Chame 'document.remove_pdfa_compliance()' para remover quaisquer restrições ou configurações de conformidade PDF/A.
1. Salve o PDF modificado em 'path_outfile'.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDFUA_to_PDF(infile, outfile):
    document = ap.Document(infile)
    document.remove_pdf_ua_compliance()
    document.save(outfile)
```

## Quando usar este fluxo de trabalho

- Remova as configurações de conformidade antes de enviar um documento para uma cadeia de ferramentas que não requer restrições de PDF/A ou PDF/UA.
- Simplifique o processamento do documento a jusante quando metadados de arquivamento ou acessibilidade não são mais necessários.
- Normalize PDFs de entrada antes de exportá-los para outros formatos.

## Conversões relacionadas

- [Converter PDF para PDF/A, PDF/E e PDF/X](/pdf/pt/python-net/convert-pdf-to-pdf_x/) se você precisar do fluxo de trabalho inverso e quiser criar PDFs compatíveis com padrões.
- [Converter PDF para Word](/pdf/pt/python-net/convert-pdf-to-word/) para saída de documento editável após remover restrições de conformidade.
- [Converter PDF para HTML](/pdf/pt/python-net/convert-pdf-to-html/) para saída amigável ao navegador a partir de arquivos PDF padrão.
