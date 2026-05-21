---
title: Comparar documentos PDF em Python
linktitle: Comparar PDF
type: docs
weight: 130
url: /pt/python-net/compare-pdf-documents/
description: Saiba como comparar documentos PDF em Python usando saída de diferenças lado a lado e gráfica com Aspose.PDF for Python via .NET.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Comparar páginas PDF e documentos completos com saída visual de diferenças em Python
Abstract: Este artigo explica como comparar documentos PDF no Aspose.PDF for Python via .NET. Aprenda como comparar páginas específicas ou arquivos PDF inteiros com saída lado a lado, e como usar métodos de comparação gráfica para gerar relatórios de diferenças baseados em imagem ou em PDF.
---

## Maneiras de Comparar Documentos PDF

Ao trabalhar com documentos PDF, há momentos em que você precisa comparar o conteúdo de dois documentos para identificar diferenças. A biblioteca Aspose.PDF for Python via .NET fornece um conjunto de ferramentas poderoso para esse propósito. Neste artigo, exploraremos como comparar documentos PDF usando alguns trechos de código simples.

Use a comparação lado a lado quando quiser uma saída PDF que destaque alterações de texto e layout entre as páginas. Use a comparação gráfica quando precisar de detecção de diferenças baseada em imagens para fluxos de trabalho de revisão visual, verificações de regressão ou relatórios de comparação de PDF.

A funcionalidade de comparação no Aspose.PDF permite comparar dois documentos PDF página por página. Você pode escolher comparar páginas específicas ou documentos inteiros. O documento de comparação resultante destaca as diferenças, facilitando a identificação das alterações entre os dois arquivos.

Aqui está uma lista de possíveis maneiras de comparar documentos PDF usando a biblioteca Aspose.PDF for Python via .NET:

1. **Comparando Páginas Específicas** - Compare as primeiras páginas de dois documentos PDF.
1. **Comparando Documentos Inteiros** - Compare todo o conteúdo de dois documentos PDF.
1. **Comparar documentos PDF graficamente**:

- Compare PDF com o método 'comparer.get_difference' - imagens individuais onde as alterações são marcadas.
- Compare PDF com o método 'comparer.compare_documents_to_pdf' - documento PDF com imagens onde as alterações são marcadas.

## Comparando Páginas Específicas

O primeiro trecho de código demonstra como comparar as primeiras páginas de dois documentos PDF usando a classe SideBySidePdfComparer.

1. Inicialização do Document.
1. Crie uma função para executar a comparação.
1. Processo de Comparação:

- document1.pages[1] e document2.pages[1]: - estes especificam a primeira página de cada documento para comparação. Observe que a indexação de páginas começa em 1 no Aspose.PDF.
- SideBySideComparisonOptions - esta classe permite a personalização do comportamento da comparação.
- additional_change_marks = True - habilita a exibição de marcadores de alteração adicionais, destacando diferenças que podem estar presentes em outras páginas, mesmo que não estejam na página atual sendo comparada.
- comparison_mode = ComparisonMode.IgnoreSpaces - define o modo de comparação para ignorar espaços no texto, concentrando‑se apenas nas alterações dentro das palavras.

1. O resultado da comparação é salvo como um novo arquivo PDF chamado ComparingSpecificPages_out.pdf no diretório data_dir especificado.

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_specific_pages(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1.pages[1], document_2.pages[1], outfile, options
    )
```

## Comparando Documentos Inteiros

O segundo trecho de código expande o escopo para comparar todo o conteúdo de dois documentos PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_entire_documents(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1, document_2, outfile, options
    )
```

O código fornecido demonstra a comparação de dois documentos PDF usando Aspose.PDF for Python via .NET. Ele utiliza a classe SideBySidePdfComparer para realizar uma comparação página a página, gerando um novo PDF que exibe as diferenças lado a lado. A comparação é configurada com SideBySideComparisonOptions, onde additional_change_marks está definido como True para realçar alterações não apenas na página atual, mas também em outras páginas, e comparison_mode está definido como IgnoreSpaces para focar nas diferenças de conteúdo significativo, ignorando variações de espaços em branco.

## Comparar usando GraphicalPdfComparer

Ao colaborar em documentos, especialmente em ambientes profissionais, você costuma acabar com várias versões do mesmo arquivo.
O código fornecido demonstra como comparar visualmente páginas específicas de dois documentos PDF usando Aspose.PDF for Python via .NET. Ao usar o `GraphicalPdfComparer` classe, realça as diferenças entre as primeiras páginas dos dois PDFs e gera imagens correspondentes para representar essas diferenças.

Você pode definir as seguintes propriedades da classe:

- Resolution - resolução em unidades DPI para imagens de saída, bem como para imagens geradas durante a comparação.
- Color - a cor das marcas de alteração.
- Limite - altere o limite em percentual. O valor padrão é zero. Definir um valor diferente de zero permite ignorar alterações gráficas que são insignificantes para você.

Com Aspose.PDF for Python via .NET, é possível comparar documentos e páginas e gerar o resultado da comparação em um documento PDF ou arquivo de imagem.

O `GraphicalPdfComparer` a classe tem um método que permite obter diferenças de imagem da página em um formato adequado para processamento adicional: `get_difference(document1.pages[1], document2.pages[1])`.

Este método retorna um objeto do `images_difference` tipo, que contém uma imagem da primeira página sendo comparada e um array de diferenças.

O `images_difference` objeto permite gerar uma imagem diferente e obter uma imagem da segunda página sendo comparada aplicando uma matriz de diferenças à imagem original. Para fazer isso, use o `difference_to_image` e `get_destination_image` métodos.

### Comparar PDF com o método Get Difference

O código fornecido define um método `get_difference` que compara dois documentos PDF e gera representações visuais das diferenças entre eles.

Este método compara as primeiras páginas de dois arquivos PDF e gera duas imagens PNG:

- Uma imagem destaca as diferenças entre as páginas em vermelho.
- A outra imagem é uma representação visual da página de destino (segunda) do PDF.

Esse processo pode ser útil para comparar visualmente alterações ou diferenças entre duas versões de um documento.

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_get_difference_method(infile1, infile2, outfile1, outfile2):
    # Open PDF documents
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)

    # Create comparer
    comparer = ap.comparison.GraphicalPdfComparer()

    # Compare specific pages
    images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

    # Get image showing differences in red over a white background
    diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
    diff_img.save(outfile1)

    # Get the second image representing the destination page
    dest_img = images_difference.get_destination_image()
    dest_img.save(outfile2)
```

### Comparar PDF com o método CompareDocumentsToPdf

O trecho de código fornecido usa o `compare_documents_to_pdf` método, que compara dois documentos e gera um relatório em PDF dos resultados da comparação.

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_compare_documents_to_pdf_method(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Create comparer and set options
    pdf_comparer = ap.comparison.GraphicalPdfComparer()
    pdf_comparer.threshold = 3.0
    pdf_comparer.color = ap.Color.blue
    pdf_comparer.resolution = ap.devices.Resolution(300)

    # Compare and output to a PDF file
    pdf_comparer.compare_documents_to_pdf(document_1, document_2, outfile)
```

Este exemplo demonstra como realizar uma comparação gráfica de dois documentos PDF completos usando Aspose.PDF for Python via .NET. Ao aproveitar o `GraphicalPdfComparer` classe, gera um novo arquivo PDF que destaca visualmente as diferenças entre os documentos.

- A propriedade threshold está definida como 3.0, significando que diferenças menores que essa percentagem são ignoradas durante a comparação, focando em alterações mais significativas.
- As diferenças são marcadas em azul definindo a propriedade color para ap.Color.blue, permitindo uma distinção visual clara.
- A comparação é realizada a uma resolução de 300 DPI definindo a propriedade de resolução, garantindo uma saída detalhada e nítida.

O `compare_documents_to_pdf` método compara todas as páginas de ambos os documentos e gera o resultado em um novo arquivo PDF, compareDocumentsToPdf_out.pdf, com as diferenças destacadas visualmente.

## Tópicos Relacionados

- [Operações avançadas de PDF em Python](/pdf/pt/python-net/advanced-operations/)
- [Trabalhe com documentos PDF em Python](/pdf/pt/python-net/working-with-documents/)
- [Trabalhar com páginas PDF em Python](/pdf/pt/python-net/working-with-pages/)
- [Trabalhar com texto PDF em Python](/pdf/pt/python-net/working-with-text/)
