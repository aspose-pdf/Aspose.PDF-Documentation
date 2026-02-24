---
title: Converter PDF/x para formatos PDF em Python
linktitle: Converter PDF/x para formatos PDF
type: docs
weight: 120
url: /pt/python-net/convert-pdf_x-to-pdf/
lastmod: "2025-09-27"
description: Este tópico mostra como converter PDF/x para formatos PDF usando Aspose.PDF para Python via .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Como converter PDF/x para formatos PDF
Abstract: O artigo fornece um guia abrangente sobre como converter PDF/UA e PDF/A para arquivo PDF usando Aspose.PDF para Python.
---

**PDF/x para formato PDF significa a capacidade de converter PDF/UA e PDF/A para arquivo PDF.**

## Converter PDF/A para PDF

1. Carregue o documento PDF usando 'ap.Document'.
1. Chame 'remove_pdfa_compliance()' para remover todas as configurações de conformidade e metadados relacionados ao PDF/A.
1. Salve o PDF resultante no caminho de saída.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Removendo conformidade PDF/UA

Esta função demonstra um processo de conversão em duas etapas: primeiro removendo a conformidade PDF/UA (Acessibilidade Universal) e, em seguida, convertendo o PDF resultante para o formato PDF/A-1B com marcação automática para acessibilidade e estrutura semântica.

1. Carregue o documento PDF usando 'ap.Document()'.
1. Chame 'document.remove_pdfa_compliance()' para remover quaisquer restrições ou configurações de conformidade PDF/A.
1. Salve o PDF modificado em 'path_outfile'.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.remove_pdfa_compliance()
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```
