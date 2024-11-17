---
title: Otimizar, Comprimir ou Reduzir Tamanho de PDF em Python
linktitle: Otimizar PDF
type: docs
weight: 30
url: /pt/python-net/optimize-pdf/
description: Otimizar arquivo PDF, reduzir todas as imagens, diminuir tamanho do PDF, Desincorporar fontes, Remover objetos não utilizados com Python.
lastmod: "2023-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Otimizar PDF usando Python",
    "alternativeHeadline": "Como otimizar PDF com Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, python, otimizar pdf",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "vendas",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "vendas",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "vendas",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/optimize-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": "Otimizar arquivo PDF, reduzir todas as imagens, diminuir tamanho do PDF, Desincorporar fontes, Remover objetos não utilizados com Python."
}
</script>


Um documento PDF pode, às vezes, conter dados adicionais. Reduzir o tamanho de um arquivo PDF ajudará a otimizar a transferência de rede e o armazenamento. Isso é especialmente útil para publicação em páginas da web, compartilhamento em redes sociais, envio por e-mail ou arquivamento em armazenamento. Podemos usar várias técnicas para otimizar o PDF:

- Otimizar o conteúdo da página para navegação online
- Reduzir ou comprimir todas as imagens
- Permitir reutilização de conteúdo da página
- Mesclar fluxos duplicados
- Desincorporar fontes
- Remover objetos não utilizados
- Remover campos de formulário achatados
- Remover ou achatar anotações

{{% alert color="primary" %}}

 Uma explicação detalhada dos métodos de otimização pode ser encontrada na página Visão Geral dos Métodos de Otimização.

{{% /alert %}}

## Otimizar Documento PDF para a Web

Otimização, ou linearização para a Web, refere-se ao processo de tornar um arquivo PDF adequado para navegação online usando um navegador web. Para otimizar um arquivo para exibição na web:

1. Abra o documento de entrada em um objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. Use o método [Optimize](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).
1. Salve o documento otimizado usando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

O trecho de código a seguir mostra como otimizar um documento PDF para a web.

```python 

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Otimizar para a web
    document.optimize()

    # Salvar documento de saída
    document.save(output_pdf)
```

## Reduzir Tamanho do PDF

O método [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) permite reduzir o tamanho do documento eliminando informações desnecessárias. Por padrão, este método funciona da seguinte forma:

- Recursos que não são usados nas páginas do documento são removidos
- Recursos iguais são unidos em um único objeto

- Objetos não utilizados são deletados

O trecho abaixo é um exemplo. No entanto, observe que este método não pode garantir a redução do documento.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Otimizar documento PDF. No entanto, observe que este método não pode garantir a redução do documento
    document.optimize_resources()
    # Salvar documento atualizado
    document.save(output_pdf)
```

## Gerenciamento de Estratégia de Otimização

Também podemos personalizar a estratégia de otimização. Atualmente, o método [OptimizeResources()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) usa 5 técnicas. Essas técnicas podem ser aplicadas usando o método OptimizeResources() com o parâmetro [OptimizationOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/optimizationoptions/).

### Reduzindo ou Compactando Todas as Imagens

Temos duas maneiras de trabalhar com imagens: reduzir a qualidade da imagem e/ou alterar sua resolução.
 Em qualquer caso, [ImageCompressionOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.optimization/imagecompressionoptions/) deve ser aplicado. No exemplo a seguir, reduzimos as imagens diminuindo a ImageQuality para 50.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Inicializar OptimizationOptions
    optimizeOptions = ap.optimization.OptimizationOptions()
    # Definir opção CompressImages
    optimizeOptions.image_compression_options.compress_images = True
    # Definir opção ImageQuality
    optimizeOptions.image_compression_options.image_quality = 50
    # Otimizar documento PDF usando OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Salvar documento atualizado
    document.save(output_pdf)
```

### Removendo Objetos Não Utilizados

Um documento PDF às vezes contém objetos PDF que não são referenciados por nenhum outro objeto no documento. Isso pode acontecer, por exemplo, quando uma página é removida da árvore de páginas do documento, mas o próprio objeto de página não é removido. Remover esses objetos não torna o documento inválido, mas sim o encolhe.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Definir a opção RemoveUsedObject
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_objects = True

    # Otimizar documento PDF usando OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Salvar documento atualizado
    document.save(output_pdf)
```

### Removendo Fluxos Não Utilizados

Às vezes, o documento contém fluxos de recursos não utilizados. Esses fluxos não são "objetos não utilizados" porque são referenciados a partir de um dicionário de recursos de página. Assim, eles não são removidos com um método de "remover objetos não utilizados". Mas esses fluxos nunca são usados com o conteúdo da página. Isso pode acontecer em casos quando uma imagem foi removida da página, mas não dos recursos da página. Além disso, essa situação geralmente ocorre quando páginas são extraídas do documento e as páginas do documento têm recursos "comuns", ou seja, o mesmo objeto de Recursos. O conteúdo das páginas é analisado para determinar se um fluxo de recursos é usado ou não. Fluxos não utilizados são removidos. Isso às vezes diminui o tamanho do documento. O uso dessa técnica é semelhante ao passo anterior:

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Definir a opção RemoveUsedStreams
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.remove_unused_streams = True
    # Otimizar documento PDF usando OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Salvar documento atualizado
    document.save(output_pdf)
```

### Vinculando Fluxos Duplicados

Alguns documentos podem conter vários fluxos de recursos idênticos (como imagens, por exemplo). Isso pode acontecer, por exemplo, quando um documento é concatenado consigo mesmo. O documento de saída contém duas cópias independentes do mesmo fluxo de recursos. Analisamos todos os fluxos de recursos e os comparamos. Se os fluxos são duplicados, eles são mesclados, ou seja, apenas uma cópia é mantida. As referências são alteradas adequadamente, e as cópias do objeto são removidas. Em alguns casos, isso ajuda a diminuir o tamanho do documento.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Definir a opção LinkDuplcateStreams
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.link_duplcate_streams = True
    # Otimizar o documento PDF usando OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Salvar documento atualizado
    document.save(output_pdf)
```

### Desincorporando Fontes

Se o documento usa fontes incorporadas, isso significa que todos os dados da fonte estão armazenados no documento.
 A vantagem é que o documento pode ser visualizado independentemente de a fonte estar instalada na máquina do usuário ou não. Mas a incorporação de fontes torna o documento maior. O método de remover fontes incorporadas remove todas as fontes incorporadas. Assim, o tamanho do documento diminui, mas o próprio documento pode se tornar ilegível se a fonte correta não estiver instalada.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Definir a opção UnembedFonts
    optimizeOptions = ap.optimization.OptimizationOptions()
    optimizeOptions.unembed_fonts = True
    # Otimizar o documento PDF usando OptimizationOptions
    document.optimize_resources(optimizeOptions)
    # Salvar documento atualizado
    document.save(output_pdf)
    file_stats_1 = os.stat(input_pdf)
    file_stats_2 = os.stat(output_pdf)
    print(
        "Tamanho do arquivo original: {}. Tamanho do arquivo reduzido: {}".format(
            file_stats_1.st_size, file_stats_2.st_size
        )
    )
```

Os recursos de otimização aplicam esses métodos ao documento. Se qualquer um desses métodos for aplicado, o tamanho do documento provavelmente diminuirá. Se nenhum desses métodos for aplicado, o tamanho do documento não mudará, o que é óbvio.

## Formas Adicionais de Reduzir o Tamanho do Documento PDF

### Removendo ou Achatando Anotações

As anotações podem ser deletadas quando são desnecessárias. Quando são necessárias, mas não requerem edição adicional, elas podem ser achatadas. Ambas as técnicas reduzirão o tamanho do arquivo.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)
    # Achar anotações
    for page in document.pages:
        for annotation in page.annotations:
            annotation.flatten()

    # Salvar documento atualizado
    document.save(output_pdf)
```

### Removendo Campos de Formulário

Se o documento PDF contiver AcroForms, podemos tentar reduzir o tamanho do arquivo achatando os campos do formulário.

```python

    import aspose.pdf as ap

    # Carregar formulário PDF de origem
    doc = ap.Document(input_pdf)

    # Achar Formulários
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Salvar o documento atualizado
    doc.save(output_pdf)
```

### Converter um PDF de espaço de cor RGB para escala de cinza

Um arquivo PDF é composto por Texto, Imagem, Anexo, Anotações, Gráficos e outros objetos. Pode surgir a necessidade de converter um PDF de espaço de cor RGB para escala de cinza para que a impressão desses arquivos PDF seja mais rápida. Além disso, quando o arquivo é convertido para escala de cinza, o tamanho do documento também é reduzido, mas isso pode causar uma diminuição na qualidade do documento. Este recurso é atualmente suportado pelo recurso Pre-Flight do Adobe Acrobat, mas quando falamos de automação de escritório, o Aspose.PDF é uma solução definitiva para fornecer tais vantagens para manipulações de documentos. Para realizar essa tarefa, o seguinte trecho de código pode ser usado.

```python

    import aspose.pdf as ap

    # Carregar o arquivo PDF de origem
    document = ap.Document(input_pdf)
    strategy = ap.RgbToDeviceGrayConversionStrategy()
    for page in document.pages:
        # Converter a imagem do espaço de cor RGB para o espaço de cor em escala de cinza
        strategy.convert(page)

    # Salvar o arquivo resultante
    document.save(output_pdf)
```


### Compressão FlateDecode

Aspose.PDF para Python via .NET oferece suporte à compressão FlateDecode para a funcionalidade de Otimização de PDF. O trecho de código abaixo mostra como usar a opção de Otimização para armazenar imagens com compressão **FlateDecode**:

```python

    import aspose.pdf as ap

    # Abrir Documento
    doc = ap.Document(input_pdf)
    # Inicializar OptimizationOptions
    optimizationOptions = ap.optimization.OptimizationOptions()
    # Para otimizar imagem usando Compressão FlateDecode, definir opções de otimização para Flate
    optimizationOptions.image_compression_options.encoding = ap.optimization.ImageEncoding.FLATE
    # Definir Opções de Otimização
    doc.optimize_resources(optimizationOptions)
    # Salvar Documento
    doc.save(output_pdf)
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for Python via .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>