---
title: Comparar documentos PDF
linktitle: Comparar PDF
type: docs
weight: 130
url: /pt/python-net/compare-pdf-documents/
description: É possível comparar o conteúdo de documentos PDF com marcas de anotação e saída lado a lado.
lastmod: "2025-05-12"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 
Abstract: 
---

## Formas de comparar documentos PDF

Ao trabalhar com documentos PDF, há momentos em que é necessário comparar o conteúdo de dois documentos para identificar diferenças. A biblioteca Aspose.PDF for Python via .NET oferece um conjunto de ferramentas poderosas para esse propósito. Neste artigo, exploraremos como comparar documentos PDF usando alguns trechos de código simples.

A funcionalidade de comparação no Aspose.PDF permite comparar dois documentos PDF página por página. Você pode escolher comparar páginas específicas ou documentos inteiros. O documento de comparação resultante destaca as diferenças, facilitando a identificação de alterações entre os dois arquivos.

Aqui está uma lista de possíveis maneiras de comparar documentos PDF usando a biblioteca Aspose.PDF for Python via .NET:

1. **Comparando páginas específicas** - Compare as primeiras páginas de dois documentos PDF.
1. **Comparando documentos inteiros** - Compare todo o conteúdo de dois documentos PDF.
1. **Comparar documentos PDF graficamente**:

- Compare PDF com o método 'comparer.get_difference' - imagens individuais onde as alterações são marcadas.
- Compare PDF com o método 'comparer.compare_documents_to_pdf' - documento PDF com imagens onde as alterações são marcadas.

## Comparando páginas específicas

O primeiro trecho de código demonstra como comparar as primeiras páginas de dois documentos PDF usando a classe SideBySidePdfComparer.

1. Inicialização do documento.
1. Crie uma função para realizar a comparação.
1. Processo de comparação:

- document1.pages[1] e document2.pages[1]: - especificam a primeira página de cada documento para comparação. Note que a indexação de páginas começa em 1 no Aspose.PDF.
- SideBySideComparisonOptions - esta classe permite a personalização do comportamento da comparação.
- additional_change_marks = True - habilita a exibição de marcadores de mudança adicionais, destacando diferenças que podem estar presentes em outras páginas, mesmo que não estejam na página atual sendo comparada.
- comparison_mode = ComparisonMode.IgnoreSpaces - define o modo de comparação para ignorar espaços no texto, concentrando-se apenas nas alterações dentro das palavras.

1. O resultado da comparação é salvo como um novo arquivo PDF chamado ComparingSpecificPages_out.pdf no data_dir especificado.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

    def comparing_specific_pages():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparingSpecificPages1.pdf")
        document2 = ap.Document(data_dir + "ComparingSpecificPages2.pdf")

        # Compare
        options = SideBySideComparisonOptions()
        options.additional_change_marks = True
        options.comparison_mode = ComparisonMode.IgnoreSpaces

        # Perform comparison and save the result
        SideBySidePdfComparer.compare(document1.pages[1], document2.pages[1], data_dir + "ComparingSpecificPages_out.pdf", options)
```

## Comparando documentos inteiros

O segundo trecho de código amplia o escopo para comparar todo o conteúdo de dois documentos PDF.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

    def comparing_entire_documents():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparingEntireDocuments1.pdf")
        document2 = ap.Document(data_dir + "ComparingEntireDocuments2.pdf")

        # Compare
        options = SideBySideComparisonOptions()
        options.additional_change_marks = True
        options.comparison_mode = ComparisonMode.IgnoreSpaces

        # Perform comparison and save the result
        SideBySidePdfComparer.compare(document1, document2, data_dir + "ComparingEntireDocuments_out.pdf", options)
```

O código fornecido demonstra a comparação de dois documentos PDF usando o Aspose.PDF for Python via .NET. Ele utiliza a classe SideBySidePdfComparer para realizar uma comparação página a página, gerando um novo PDF que exibe as diferenças lado a lado. A comparação é configurada com SideBySideComparisonOptions, onde additional_change_marks está definido como True para destacar alterações não apenas na página atual, mas também em outras páginas, e comparison_mode está definido como IgnoreSpaces para focar nas diferenças de conteúdo significativo ao ignorar variações de espaços em branco.

## Comparar usando GraphicalPdfComparer

Ao colaborar em documentos, especialmente em ambientes profissionais, você frequentemente acaba com várias versões do mesmo arquivo.
O código fornecido demonstra como comparar visualmente páginas específicas de dois documentos PDF usando o Aspose.PDF for Python via .NET. Ao utilizar a classe `GraphicalPdfComparer`, ele destaca as diferenças entre as primeiras páginas dos dois PDFs e gera imagens correspondentes para representar essas diferenças.

Você pode definir as seguintes propriedades da classe:

- Resolution - resolução em unidades DPI para imagens de saída, bem como para imagens geradas durante a comparação.
- Color - a cor das marcas de alteração.
- Threshold - limiar de mudança em porcentagem. O valor padrão é zero. Definir um valor diferente de zero permite ignorar alterações gráficas que são insignificantes para você.

Com o Aspose.PDF for Python via .NET, é possível comparar documentos e páginas e gerar o resultado da comparação em um documento PDF ou arquivo de imagem.

A classe `GraphicalPdfComparer` tem um método que permite obter diferenças de imagens de página em um formato adequado para processamento posterior: `get_difference(document1.pages[1], document2.pages[1])`.

Este método retorna um objeto do tipo `images_difference`, que contém uma imagem da primeira página comparada e um array de diferenças.

O objeto `images_difference` permite gerar uma imagem distinta e obter uma imagem da segunda página comparada aplicando um array de diferenças à imagem original. Para isso, use os métodos `difference_to_image` e `get_destination_image`.

### Comparar PDF com o método Get Difference

O código fornecido define um método `get_difference` que compara dois documentos PDF e gera representações visuais das diferenças entre eles.

Este método compara as primeiras páginas de dois arquivos PDF e gera duas imagens PNG:

- Uma imagem destaca as diferenças entre as páginas em vermelho.
- A outra imagem é uma representação visual da página PDF de destino (segunda).

Este processo pode ser útil para comparar visualmente as alterações ou diferenças entre duas versões de um documento.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import GraphicalPdfComparer

    def compare_pdf_with_get_difference_method():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod1.pdf")
        document2 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod2.pdf")

        # Create comparer
        comparer = GraphicalPdfComparer()

        # Compare specific pages
        images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

        # Get image showing differences in red over a white background
        diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
        diff_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png")

        # Get the second image representing the destination page
        dest_img = images_difference.get_destination_image()
        dest_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png")
```

### Comparar PDF com o método CompareDocumentsToPdf

O trecho de código fornecido usa o método `compare_documents_to_pdf`, que compara dois documentos e gera um relatório PDF dos resultados da comparação.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import GraphicalPdfComparer
    from aspose.pdf.devices import Resolution

    def compare_pdf_with_compare_documents_to_pdf_method():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf")
        document2 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf")

        # Create comparer and set options
        comparer = GraphicalPdfComparer()
        comparer.threshold = 3.0
        comparer.color = ap.Color.blue
        comparer.resolution = Resolution(300)

        # Compare and output to a PDF file
        comparer.compare_documents_to_pdf(document1, document2, data_dir + "compareDocumentsToPdf_out.pdf")
```

Este exemplo demonstra como realizar uma comparação gráfica de dois documentos PDF completos usando Aspose.PDF para Python via .NET. Ao aproveitar a classe `GraphicalPdfComparer`, ele gera um novo arquivo PDF que destaca visualmente as diferenças entre os documentos.

- A propriedade de limiar está definida como 3.0, indicando que diferenças menores que essa porcentagem são ignoradas durante a comparação, focando em alterações mais significativas.
- As diferenças são marcadas em azul definindo a propriedade de cor para ap.Color.blue, permitindo uma distinção visual clara.
- A comparação é realizada com uma resolução de 300 DPI definindo a propriedade de resolução, garantindo uma saída detalhada e nítida.

O método `compare_documents_to_pdf` compara todas as páginas de ambos os documentos e produz o resultado em um novo arquivo PDF, compareDocumentsToPdf_out.pdf, com as diferenças destacadas visualmente.

