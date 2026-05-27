---
title: Criar livreto PDF
type: docs
weight: 20
url: /pt/python-net/create-pdf-booklet/
description: Gerar um PDF no estilo livreto a partir de um documento existente usando Aspose.PDF for Python
lastmod: "2026-05-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Criar um livreto PDF a partir de um PDF existente usando Python
Abstract: Saiba como gerar um PDF no estilo livreto a partir de um documento existente usando Aspose.PDF for Python. Este exemplo demonstra como usar a classe PdfFileEditor para reorganizar páginas de modo que elas possam ser impressas e dobradas como um livreto. O método ordena automaticamente as páginas para produzir um layout de livreto adequado.
---

Criar documentos no estilo livreto é uma exigência comum ao preparar PDFs para impressão. Em um layout de livreto, as páginas são reorganizadas para que, ao serem impressas e dobradas, apareçam na ordem correta.

Usando Aspose.PDF for Python, os desenvolvedores podem converter facilmente um PDF padrão em um livreto usando o [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe. O método 'make_booklet' reorganiza automaticamente as páginas do documento de entrada e gera um novo PDF otimizado para impressão em forma de livrinho.

1. Abra um documento PDF existente.
1. Crie uma instância de PdfFileEditor.
1. Use o método make_booklet para reorganizar as páginas.
1. Salve a saída como um arquivo PDF pronto para livrinho.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


# Create PDF Booklet
def create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    booklet_maker.make_booklet(FileIO(infile), FileIO(outfile, "w"))
```

Este trecho de código mostra como usar o método 'try_make_booklet' da [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/) classe para reorganizar páginas para impressão em livreto sem lançar exceções caso a operação falhe.

Um layout de livreto reorganiza as páginas de modo que, quando impresso e dobrado, o documento seja lido na ordem correta. Automatizar esse processo garante resultados consistentes e elimina a necessidade de reorganização manual de páginas.

O método 'try_make_booklet' funciona de forma semelhante ao 'make_booklet', mas com uma diferença importante:

- 'make_booklet' lança uma exceção se a operação falhar.
- 'try_make_booklet' retorna True ou False, permitindo que os desenvolvedores gerenciem erros com mais segurança.

1. Abra um documento PDF existente.
1. Crie uma instância de PdfFileEditor.
1. Tente criar o livreto.
1. Manipule o resultado.

```python
import aspose.pdf as ap
import aspose.pdf.facades as pdf_facades
from io import FileIO

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def try_create_pdf_booklet(infile, outfile):
    # Create BookletMaker object
    booklet_maker = pdf_facades.PdfFileEditor()
    # Make booklet from input PDF file and save to output PDF file
    # The try_make_booklet method is like the make_booklet method,
    # except the try_make_booklet method does not throw an exception if the operation fails.
    if not booklet_maker.try_make_booklet(FileIO(infile), FileIO(outfile, "w")):
        print("Failed to create booklet.")
```
