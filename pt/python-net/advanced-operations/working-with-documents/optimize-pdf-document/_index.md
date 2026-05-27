---
title: Otimizar arquivos PDF em Python
linktitle: Otimizar PDF
type: docs
weight: 30
url: /pt/python-net/optimize-pdf/
description: Aprenda a otimizar, compactar e reduzir o tamanho de arquivos PDF em Python usando Aspose.PDF.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Compacte páginas PDF usando Python
Abstract: Este artigo fornece um guia abrangente sobre otimização de arquivos PDF para reduzir seu tamanho e melhorar o desempenho em várias plataformas, como páginas da Web, e‑mails e sistemas de armazenamento. As técnicas de otimização incluem a redução do tamanho das imagens, a remoção de recursos não utilizados e a desvinculação de fontes. Métodos específicos para otimizar PDFs para a web e reduzir o tamanho geral do arquivo são discutidos, utilizando os métodos `Optimize` e `OptimizeResources` no Aspose.PDF for Python. A personalização das estratégias de otimização é possível via `OptimizationOptions`, permitindo ações direcionadas como compactar imagens, remover objetos e fluxos não utilizados, vincular fluxos duplicados e desvincular fontes. Estratégias adicionais cobrem o achatamento de anotações, a remoção de campos de formulário e a conversão de arquivos PDF de RGB para escala de cinza para diminuir ainda mais o tamanho. O artigo também destaca o uso da compressão FlateDecode para otimização de imagens, garantindo uma gestão eficaz de arquivos PDF enquanto mantém a qualidade e a funcionalidade.
---

Um documento PDF pode, às vezes, conter dados adicionais. Reduzir o tamanho de um arquivo PDF ajudará a otimizar a transferência de rede e o armazenamento. Isso é especialmente útil para publicação em páginas da web, compartilhamento em redes sociais, envio por e‑mail ou arquivamento em armazenamento. Podemos usar várias técnicas para otimizar o PDF:

Use esta página quando precisar reduzir o tamanho do PDF para entrega na web, compartilhamento por e‑mail, economia de armazenamento ou saída pronta para impressão, sem reconstruir o document do zero.

- Otimizar o conteúdo da página para navegação online
- Reduza ou comprima todas as imagens
- Habilitar reutilização de conteúdo da página
- Mesclar fluxos duplicados
- Desincorporar fontes
- Remover objetos não utilizados
- Remover flattening de campos de formulário
- Remover ou achatar anotações

{{% alert color="primary" %}}

 A explicação detalhada dos métodos de otimização pode ser encontrada na página Visão geral dos Métodos de Otimização.

{{% /alert %}}

## Otimizar Documento PDF para a Web

Otimização, ou linearização para Web, refere-se ao processo de tornar um arquivo PDF adequado para navegação online usando um navegador web. Para otimizar um arquivo para exibição na web:

1. Abra o documento de entrada em um [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto.
1. Use o [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.
1. Salve o documento otimizado usando o [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.

O trecho de código a seguir mostra como otimizar um documento PDF para a web.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def optimize_pdf(infile, outfile):
    document = ap.Document(infile)
    document.optimize()
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## Reduzir tamanho PDF

O [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) O método permite reduzir o tamanho do documento ao remover as informações desnecessárias. Por padrão, este método funciona da seguinte forma:

- Recursos que não são usados nas páginas do documento são removidos
- Recursos iguais são unidos em um único objeto
- Objetos não usados são excluídos

O trecho abaixo é um exemplo. Note, porém, que este método não pode garantir a redução do documento.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def reduce_size_pdf(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
    document.optimize_resources()
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

## Gerenciamento de Estratégia de Otimização

Também podemos personalizar a estratégia de otimização. Atualmente, o [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método usa 5 técnicas. Estas técnicas podem ser aplicadas usando o método OptimizeResources() com o [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/) parâmetro.

### Reduzindo ou Compactando Todas as Imagens

Temos duas maneiras de trabalhar com imagens: reduzir a qualidade da imagem e/ou alterar sua resolução. Em qualquer caso, [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) deve ser aplicado. No exemplo a seguir, reduzimos as imagens diminuindo ImageQuality para 50.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def shrinking_or_compressing_all_images(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Set CompressImages option
    optimizeOptions.image_compression_options.compress_images = True
    # Set ImageQuality option
    optimizeOptions.image_compression_options.image_quality = 50
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Removendo objetos não utilizados

Um documento PDF às vezes contém objetos PDF que não são referenciados por nenhum outro objeto no documento. Isso pode acontecer, por exemplo, quando uma página é removida da árvore de páginas do documento, mas o próprio objeto da página não é removido. A remoção desses objetos não torna o documento inválido, mas sim o diminui.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_objects(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedObjects option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Removendo fluxos não usados

Às vezes o documento contém fluxos de recursos não utilizados. Esses fluxos não são “objetos não utilizados” porque são referenciados a partir de um dicionário de recursos da página. Portanto, não são removidos com um método “remove unused objects”. Mas esses fluxos nunca são usados com o conteúdo da página. Isso pode acontecer quando uma imagem foi removida da página, mas não dos recursos da página. Além disso, essa situação costuma ocorrer quando páginas são extraídas do documento e as páginas do documento têm recursos “comuns”, ou seja, o mesmo objeto Resources. O conteúdo das páginas é analisado para determinar se um fluxo de recurso está sendo usado ou não. Fluxos não utilizados são removidos. Isso às vezes diminui o tamanho do documento. O uso desta técnica é semelhante ao passo anterior:

```python
import aspose.pdf as ap
from os import path, stat
import sys


def removing_unused_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set RemoveUnusedStreams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Vinculando Fluxos Duplicados

Alguns documentos podem conter vários fluxos de recursos idênticos (como imagens, por exemplo). Isso pode acontecer, por exemplo, quando um documento é concatenado com ele mesmo. O documento de saída contém duas cópias independentes do mesmo fluxo de recurso. Analisamos todos os fluxos de recurso e os comparamos. Se os fluxos forem duplicados, eles são mesclados, ou seja, apenas uma cópia permanece. As referências são alteradas adequadamente e as cópias do objeto são removidas. Em alguns casos, isso ajuda a diminuir o tamanho do documento.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def linking_duplicate_streams(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set link_duplicate_streams option
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplicate_streams = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Desincorporação de fontes

Se o documento usar fontes incorporadas, isso significa que todos os dados da fonte estão armazenados no documento. A vantagem é que o documento pode ser visualizado independentemente de a fonte estar instalada na máquina do usuário ou não. Mas incorporar fontes aumenta o tamanho do documento. O método de desincorporar fontes remove todas as fontes incorporadas. Assim, o tamanho do documento diminui, mas o próprio documento pode ficar ilegível se a fonte correta não estiver instalada.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def unembed_fonts(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Set unembed_fonts option
    optimize_options = ap.optimization.OptimizationOptions()
    optimize_options.unembed_fonts = True
    # Optimize PDF document using OptimizationOptions
    document.optimize_resources(optimize_options)
    # Save updated document
    document.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

Os recursos de otimização aplicam esses métodos ao documento. Se algum desses métodos for aplicado, o tamanho do documento provavelmente diminuirá. Se nenhum desses métodos for aplicado, o tamanho do documento não mudará, o que é óbvio.

## Outras maneiras de reduzir o tamanho do documento PDF

### Removendo ou Aplanando Anotações

As anotações podem ser excluídas quando são desnecessárias. Quando são necessárias, mas não exigem edição adicional, podem ser achatadas. Ambas as técnicas reduzirão o tamanho do arquivo.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_annotations(infile, outfile):
    # Open document
    document = ap.Document(infile)
    # Flatten annotations
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Save updated document
    document.save(outfile)
```

### Removendo FormFields

Se o documento PDF contiver AcroForms, podemos tentar reduzir o tamanho do arquivo achatando os campos de formulário.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def flatten_forms(infile, outfile):
    # Load source PDF form
    doc = ap.Document(infile)

    # Flatten Forms
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Save the updated document
    doc.save(outfile)
    file_stats_1 = stat(infile)
    file_stats_2 = stat(outfile)
    print(
        "Original file size: {}. Reduced file size: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

### Converter um PDF do espaço de cores RGB para escala de cinza

Um arquivo PDF é composto por Texto, Imagem, Anexo, Anotações, Gráficos e outros objetos. Você pode se deparar com a necessidade de converter um PDF do espaço de cores RGB para escala de cinza, de modo que a impressão desses arquivos PDF seja mais rápida. Além disso, quando o arquivo é convertido para escala de cinza, o tamanho do documento também é reduzido, mas isso pode também causar uma diminuição na qualidade do documento. Esse recurso é atualmente suportado pelo recurso Pre-Flight do Adobe Acrobat, mas ao falar de automação de Office, Aspose.PDF é uma solução definitiva para fornecer tais vantagens para manipulação de documentos. Para atender a essa necessidade, o seguinte trecho de código pode ser usado.

```python
import aspose.pdf as ap
from os import path, stat
import sys


def сonvert_PDF_from_RGB_colorspace_to_grayscale(infile, outfile):
    document = ap.Document(infile)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Convert the RGB colorspace image to GrayScale colorspace
        strategy.convert(page)

    # Save resultant file
    document.save(outfile)
```

### Compressão FlateDecode

Aspose.PDF for Python via .NET fornece suporte à compressão FlateDecode para a funcionalidade de Otimização de PDF. O trecho de código a seguir demonstra como usar a opção em Otimização para armazenar imagens com compressão **FlateDecode**:

```python
import aspose.pdf as ap
from os import path, stat
import sys


def using_flatedecode_compression(infile, outfile):

    # Open Document
    doc = ap.Document(infile)
    # Initialize OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # To optimise image using FlateDecode Compression set optimization options to Flate
    optimizationOptions.image_compression_options.encoding = (
        ap.optimization.ImageEncoding.FLATE
    )
    # Set Optimization Options
    doc.optimize_resources(optimizationOptions)
    # Save Document
    doc.save(outfile)
```

## Tópicos Relacionados ao Documento

- [Trabalhe com documentos PDF em Python](/pdf/pt/python-net/working-with-documents/)
- [Mesclar arquivos PDF em Python](/pdf/pt/python-net/merge-pdf-documents/)
- [Dividir arquivos PDF em Python](/pdf/pt/python-net/split-document/)
- [Manipular documentos PDF em Python](/pdf/pt/python-net/manipulate-pdf-document/)

