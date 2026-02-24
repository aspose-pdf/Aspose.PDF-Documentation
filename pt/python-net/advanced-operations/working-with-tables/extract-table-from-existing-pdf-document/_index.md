---
title: Extrair Tabela de Documento PDF
linktitle: Extrair Tabela
type: docs
weight: 20
url: /pt/python-net/extracting-table/
description: Aspose.PDF for Python via .NET torna possível realizar várias manipulações nas tabelas contidas no seu documento PDF.
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como extrair Tabela de PDF usando Python
Abstract: Este artigo discute o processo de extração de tabelas de documentos PDF usando Python, especificamente aproveitando a Biblioteca Aspose.PDF for Python via .NET. Ele fornece um exemplo de código que demonstra como carregar um documento PDF, percorrer suas páginas e utilizar a classe `TableAbsorber` para identificar e extrair dados de tabelas. O código itera por cada tabela, linha e célula, coletando fragmentos de texto e imprimindo o texto extraído. Este método é destacado como uma ferramenta poderosa para tarefas de extração e análise de dados envolvendo dados tabulares dentro de PDFs.
---

## Extrair Tabela de PDF

Extrair tabelas de PDFs usando Python pode ser incrivelmente útil para extração e análise de dados. Com a Biblioteca Aspose.PDF for Python via .NET, você pode trabalhar de forma eficiente com tabelas incorporadas em documentos PDF para várias tarefas relacionadas a dados.

Este trecho de código abre um arquivo PDF existente, analisa cada página em busca de tabelas e extrai o conteúdo de texto das células. Ele utiliza o 'TableAbsorber' para detectar tabelas e então itera pelas linhas e células para imprimir o texto interno.

1. Carrega o PDF em um objeto ap.Document.
1. Percorre as páginas.
1. Cria um objeto TableAbsorber.
1. Itera pelas tabelas.
1. Itera pelas linhas e células.
1. Extrai e imprime o texto das células.

Este exemplo lê um PDF, encontra todas as tabelas e imprime o conteúdo de suas células linha por linha.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    document = ap.Document(path_infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row")
                for cell in row.cell_list:
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        txt = ""
                        for seg in fragment.segments:
                            txt += seg.text
                        print(txt)
```


