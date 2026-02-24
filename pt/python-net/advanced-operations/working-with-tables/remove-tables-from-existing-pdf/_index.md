---
title: Remover tabelas de um PDF existente
linktitle: Remover tabelas
type: docs
weight: 50
url: /pt/python-net/removing-tables/
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como excluir tabelas de PDF usando Python
Abstract: Este artigo discute a funcionalidade do Aspose.PDF para Python via .NET, focando especificamente na manipulação de tabelas em documentos PDF. A biblioteca permite que os usuários insiram ou criem tabelas tanto em arquivos PDF novos quanto existentes, bem como manipulem ou removam tabelas de PDFs existentes. O artigo apresenta a classe `TableAbsorber`, que é crucial para identificar e interagir com tabelas em um PDF. Um novo método, `remove()`, foi adicionado para permitir a remoção de tabelas. O documento fornece dois trechos de código – um demonstrando como remover uma única tabela de um PDF, e outro ilustrando a remoção de múltiplas tabelas. Esses exemplos destacam a aplicação prática da classe `TableAbsorber` para alcançar a remoção de tabelas de documentos PDF.
---

## Remover tabela de documento PDF

Aspose.PDF para Python permite que você remova uma tabela de um PDF. Ele abre um PDF existente, detecta a primeira tabela na primeira página com TableAbsorber, exclui essa tabela usando o [remove_one_table](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods). Depois de salvar o PDF atualizado em um novo arquivo.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(path_outfile)
```

## Remover todas as tabelas de um documento PDF

Com nossa biblioteca, você pode remover todas as tabelas de uma página específica em um PDF. O código abre um PDF existente, detecta todas as tabelas na segunda página com TableAbsorber, percorre as tabelas detectadas, remove cada uma e, em seguida, salva o PDF modificado em um novo arquivo. É útil quando você precisa remover tabelas em massa de uma página, mantendo o restante do conteúdo do PDF intacto.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit second page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(path_outfile)
```


