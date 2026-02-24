---
title: Otimizar, Compactar ou Reduzir o Tamanho de PDF em Python
linktitle: Otimizar PDF
type: docs
weight: 30
url: /pt/python-net/optimize-pdf/
description: Aprenda a otimizar documentos PDF em Python para melhorar o desempenho da web e reduzir o tamanho dos arquivos usando Aspose.PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Compactar páginas PDF usando Python
Abstract: Este artigo fornece um guia abrangente sobre a otimização de arquivos PDF para reduzir seu tamanho e melhorar o desempenho em várias plataformas, como páginas da web, e‑mails e sistemas de armazenamento. As técnicas de otimização incluem reduzir o tamanho das imagens, remover recursos não utilizados e desincorporar fontes. Métodos específicos para otimizar PDFs para a web e reduzir o tamanho geral do arquivo são discutidos, utilizando os métodos `Optimize` e `OptimizeResources` no Aspose.PDF para Python. A personalização das estratégias de otimização é possível via `OptimizationOptions`, permitindo ações direcionadas como compactar imagens, remover objetos e fluxos não utilizados, vincular fluxos duplicados e desincorporar fontes. Estratégias adicionais cobrem a planificação de anotações, a remoção de campos de formulário e a conversão de arquivos PDF de RGB para escala de cinza para diminuir ainda mais o tamanho. O artigo também destaca o uso da compressão FlateDecode para otimização de imagens, garantindo uma gestão eficaz de arquivos PDF enquanto mantém a qualidade e a funcionalidade.
---

Um documento PDF pode às vezes conter dados adicionais. Reduzir o tamanho de um arquivo PDF ajudará a otimizar a transferência de rede e o armazenamento. Isso é especialmente útil para publicação em páginas da web, compartilhamento em redes sociais, envio por e‑mail ou arquivamento em armazenamento. Podemos usar várias técnicas para otimizar PDF:

- Otimizar o conteúdo da página para navegação online
- Reduzir ou compactar todas as imagens
- Habilitar a reutilização do conteúdo da página
- Mesclar fluxos duplicados
- Desincorporar fontes
- Remover objetos não utilizados
- Remover campos de formulário achatados
- Remover ou achatar anotações

{{% alert color="primary" %}}

Explicação detalhada dos métodos de otimização pode ser encontrada na página Visão Geral dos Métodos de Otimização.

{{% /alert %}}

## Otimizar Documento PDF para a Web

Otimização, ou linearização para a Web, refere-se ao processo de tornar um arquivo PDF adequado para navegação online usando um navegador web. Para otimizar um arquivo para exibição na web:

1. Abra o documento de entrada em um objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. Use o método [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) .
1. Salve o documento otimizado usando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) .

O trecho de código a seguir mostra como otimizar um documento PDF para a web.

```python

    import aspose.pdf as ap

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document(path_infile)
    document.optimize()
    document.save(path_outfile)
```

## Reduzir Tamanho do PDF

O método [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) permite reduzir o tamanho do documento eliminando informações desnecessárias. Por padrão, este método funciona da seguinte forma:

- Recursos que não são usados nas páginas do documento são removidos
- Recursos iguais são unidos em um único objeto
- Objetos não utilizados são excluídos

O trecho abaixo é um exemplo. Observe, porém, que este método não pode garantir a redução do documento.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(output_pdf)
```

## Gerenciamento de Estratégia de Otimização

Também podemos personalizar a estratégia de otimização. Atualmente, o método [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) usa 5 técnicas. Essas técnicas podem ser aplicadas usando o método OptimizeResources() com o parâmetro [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/).

### Reduzir ou Compactar Todas as Imagens

Temos duas maneiras de trabalhar com imagens: reduzir a qualidade da imagem e/ou mudar sua resolução. Em qualquer caso, [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) deve ser aplicado. No exemplo a seguir, reduzimos as imagens diminuindo ImageQuality para 50.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Remoção de Objetos Não Utilizados

Um documento PDF às vezes contém objetos PDF que não são referenciados por nenhum outro objeto no documento. Isso pode acontecer, por exemplo, quando uma página é removida da árvore de páginas do documento, mas o próprio objeto da página não é removido. Remover esses objetos não torna o documento inválido, mas sim o reduz.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set RemoveUsedObject option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Remoção de Fluxos Não Utilizados

Às vezes, o documento contém fluxos de recursos não utilizados. Esses fluxos não são “objetos não utilizados” porque são referenciados por um dicionário de recursos de página. Assim, eles não são removidos com um método “remover objetos não utilizados”. Mas esses fluxos nunca são usados com o conteúdo da página. Isso pode acontecer quando uma imagem foi removida da página, mas não dos recursos da página. Além disso, essa situação frequentemente ocorre quando páginas são extraídas do documento e as páginas do documento têm recursos “comuns”, isto é, o mesmo objeto Resources. O conteúdo das páginas é analisado para determinar se um fluxo de recurso é usado ou não. Fluxos não utilizados são removidos. Isso às vezes diminui o tamanho do documento. O uso desta técnica é semelhante ao passo anterior:

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set RemoveUsedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Vinculação de Fluxos Duplicados

Alguns documentos podem conter vários fluxos de recursos idênticos (como imagens, por exemplo). Isso pode acontecer, por exemplo, quando um documento é concatenado consigo mesmo. O documento de saída contém duas cópias independentes do mesmo fluxo de recurso. Analisamos todos os fluxos de recursos e os comparamos. Se os fluxos forem duplicados, eles são mesclados, isto é, apenas uma cópia permanece. As referências são alteradas adequadamente e as cópias do objeto são removidas. Em alguns casos, isso ajuda a diminuir o tamanho do documento.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set LinkDuplicateStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplcate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
```

### Desincorporar Fontes

Se o documento usa fontes incorporadas, isso significa que todos os dados da fonte estão armazenados no documento. A vantagem é que o documento pode ser visualizado independentemente de a fonte estar instalada na máquina do usuário ou não. Mas incorporar fontes torna o documento maior. O método de desincorporar fontes remove todas as fontes incorporadas. Assim, o tamanho do documento diminui, mas o próprio documento pode se tornar ilegível se a fonte correta não estiver instalada.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Set UnembedFonts  option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(output_pdf)
    file_stats_1 = os.stat(input_pdf)
    file_stats_2 = os.stat(output_pdf)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

Os recursos de otimização aplicam esses métodos ao documento. Se algum desses métodos for aplicado, o tamanho do documento provavelmente diminuirá. Se nenhum desses métodos for aplicado, o tamanho do documento não mudará, o que é óbvio.

## Formas adicionais de reduzir o tamanho do documento PDF

### Removendo ou achatando anotações

Anotações podem ser excluídas quando são desnecessárias. Quando são necessárias, mas não exigem edição adicional, podem ser achatadas. Ambas as técnicas reduzirão o tamanho do arquivo.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(output_pdf)
```

### Removendo campos de formulário

Se o documento PDF contiver AcroForms, podemos tentar reduzir o tamanho do arquivo achatando os campos de formulário.

```python

    import aspose.pdf as ap

    # Load source PDF form
    doc = ap.Document(input_pdf)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(output_pdf)
```

### Converter um PDF do espaço de cores RGB para escala de cinza

Um arquivo PDF compreende Texto, Imagem, Anexo, Anotações, Gráficos e outros objetos. Você pode se deparar com a necessidade de converter um PDF do espaço de cores RGB para escala de cinza, de modo que a impressão desses arquivos PDF seja mais rápida. Além disso, quando o arquivo é convertido para escala de cinza, o tamanho do documento também é reduzido, embora possa também causar uma diminuição na qualidade do documento. Esse recurso é suportado atualmente pelo recurso Preflight do Adobe Acrobat, mas ao falar de automação Office, o Aspose.PDF é uma solução definitiva para oferecer tais vantagens para manipulação de documentos. Para atender a esse requisito, o trecho de código a seguir pode ser usado.

```python

    import aspose.pdf as ap

    # Load source PDF file
    document = ap.Document(input_pdf)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(output_pdf)
```

### Compactação FlateDecode

O Aspose.PDF for Python via .NET oferece suporte à compactação FlateDecode para a funcionalidade de Otimização de PDF. O trecho de código a seguir demonstra como usar a opção de Otimização para armazenar imagens com compactação **FlateDecode**:

```python

    import aspose.pdf as ap

    # Open Document
    doc = ap.Document(input_pdf)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(output_pdf)
```


