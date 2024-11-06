---
title: Manipular Documento PDF em Python via .NET
linktitle: Manipular Documento PDF
type: docs
weight: 20
url: pt/python-net/manipulate-pdf-document/
description: Este artigo contém informações sobre como validar Documento PDF para o padrão PDF A usando Python, como trabalhar com TOC, como definir data de expiração do PDF, etc.
keywords: "manipular pdf python"
lastmod: "2023-04-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Manipular Documento PDF via Python",
    "alternativeHeadline": "Como manipular arquivo PDF com Python",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documento pdf",
    "keywords": "pdf, dotnet, python, manipular arquivo pdf",
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
    "url": "/python-net/manipulate-pdf-document/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/manipulate-pdf-document/"
    },
    "dateModified": "2023-04-13",
    "description": "Este artigo contém informações sobre como validar Documento PDF para o padrão PDF A usando Python, como trabalhar com TOC, como definir data de expiração do PDF, etc."
}
</script>


## Manipular Documento PDF em Python

## Validar Documento PDF para o Padrão PDF A (A 1A e A 1B)

Para validar um documento PDF para compatibilidade com PDF/A-1a ou PDF/A-1b, use o método [validate](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). Este método permite que você especifique o nome do arquivo no qual o resultado deve ser salvo e o tipo de validação necessário na enumeração PdfFormat: PDF_A_1A ou PDF_A_1B.

O trecho de código a seguir mostra como validar um documento PDF para PDF/A-1A.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Validar PDF para PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1A)
```

O trecho de código a seguir mostra como validar um documento PDF para PDF/A-1b.

```python

    import aspose.pdf as ap

    # Abrir documento
    document = ap.Document(input_pdf)

    # Validar PDF para PDF/A-1a
    document.validate(output_xml, ap.PdfFormat.PDF_A_1B)
```


## Trabalhando com TOC

### Adicionar TOC a um PDF Existente

TOC em PDF significa "Tabela de Conteúdos". É um recurso que permite aos usuários navegar rapidamente por um documento, fornecendo uma visão geral de suas seções e títulos.

Para adicionar um TOC a um arquivo PDF existente, use a classe Heading no namespace [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/). O namespace [aspose.pdf](https://reference.aspose.com/pdf/python-net/aspose.pdf/) pode tanto criar novos arquivos PDF quanto manipular arquivos PDF existentes. Para adicionar um TOC a um PDF existente, use o namespace Aspose.Pdf. O trecho de código a seguir mostra como criar uma tabela de conteúdos dentro de um arquivo PDF existente usando Python via .NET.

```python

    import aspose.pdf as ap

    # Carregar um arquivo PDF existente
    doc = ap.Document(input_pdf)

    # Obter acesso à primeira página do arquivo PDF
    tocPage = doc.pages.insert(1)

    # Criar objeto para representar informações do TOC
    tocInfo = ap.TocInfo()
    title = ap.text.TextFragment("Tabela de Conteúdos")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD

    # Definir o título para o TOC
    tocInfo.title = title
    tocPage.toc_info = tocInfo

    # Criar objetos de string que serão usados como elementos do TOC
    titles = ["Primeira página", "Segunda página", "Terceira página", "Quarta página"]
    for i in range(0, 2):
        # Criar objeto Heading
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = tocPage
        heading2.segments.append(segment2)

        # Especificar a página de destino para o objeto heading
        heading2.destination_page = doc.pages[i + 2]

        # Página de destino
        heading2.top = doc.pages[i + 2].rect.height

        # Coordenada de destino
        segment2.text = titles[i]

        # Adicionar heading à página que contém o TOC
        tocPage.paragraphs.add(heading2)

    # Salvar o documento atualizado
    doc.save(output_pdf)
```


### Definir diferentes TabLeaderType para diferentes níveis de TOC

Aspose.PDF para Python também permite definir diferentes TabLeaderType para diferentes níveis de TOC. Você precisa definir a propriedade [line_dash](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) de [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/).

```python

    import aspose.pdf as ap

    doc = ap.Document()
    tocPage = doc.pages.add()
    toc_info = ap.TocInfo()

    # definir LeaderType
    toc_info.line_dash = ap.text.TabLeaderType.SOLID
    title = ap.text.TextFragment("Índice")
    title.text_state.font_size = 30
    toc_info.title = title

    # Adicionar a seção de lista à coleção de seções do documento Pdf
    tocPage.toc_info = toc_info
    # Definir o formato da lista de quatro níveis configurando as margens à esquerda
    # e
    # configurações de formato de texto de cada nível

    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.left = 0
    toc_info.format_array[0].margin.right = 30
    toc_info.format_array[0].line_dash = ap.text.TabLeaderType.DOT
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 10
    toc_info.format_array[1].margin.right = 30
    toc_info.format_array[1].line_dash = 3
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].margin.left = 20
    toc_info.format_array[2].margin.right = 30
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].line_dash = ap.text.TabLeaderType.SOLID
    toc_info.format_array[3].margin.left = 30
    toc_info.format_array[3].margin.right = 30
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD

    # Criar uma seção no documento Pdf
    page = doc.pages.add()

    # Adicionar quatro cabeçalhos na seção
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        heading2.toc_page = tocPage
        segment2.text = "Cabeçalho de Exemplo" + str(Level)
        heading2.text_state.font = ap.text.FontRepository.find_font("Arial")

        # Adicionar o cabeçalho ao Índice.
        heading2.is_in_list = True
        page.paragraphs.add(heading2)

    # salvar o Pdf
    doc.save(output_pdf)
```


### Ocultar Números de Página no TOC

Caso você não queira exibir números de página, junto com os títulos no TOC, você pode usar a propriedade [is_show_page_numbers](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) da Classe [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) como falso. Por favor, verifique o seguinte trecho de código para ocultar os números de página no índice:

```python

    import aspose.pdf as ap

    doc = ap.Document()
    toc_page = doc.pages.add()
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Índice")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.title = title
    # Adicionar a seção da lista à coleção de seções do documento Pdf
    toc_page.toc_info = toc_info
    # Definir o formato da lista de quatro níveis configurando as margens esquerdas e
    # configurações de formato de texto de cada nível

    toc_info.is_show_page_numbers = False
    toc_info.format_array_length = 4
    toc_info.format_array[0].margin.right = 0
    toc_info.format_array[0].text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    toc_info.format_array[1].margin.left = 30
    toc_info.format_array[1].text_state.underline = True
    toc_info.format_array[1].text_state.font_size = 10
    toc_info.format_array[2].text_state.font_style = ap.text.FontStyles.BOLD
    toc_info.format_array[3].text_state.font_style = ap.text.FontStyles.BOLD
    page = doc.pages.add()
    # Adicionar quatro títulos na seção
    for Level in range(1, 5):
        heading2 = ap.Heading(Level)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        heading2.is_auto_sequence = True
        segment2.text = "este é o título do nível " + str(Level)
        heading2.is_in_list = True
        page.paragraphs.add(heading2)
    doc.save(output_pdf)

```


### Personalizar Números de Página ao Adicionar TOC

É comum personalizar a numeração de páginas no TOC ao adicionar TOC em um documento PDF. Por exemplo, podemos precisar adicionar algum prefixo antes do número da página como P1, P2, P3 e assim por diante. Nesse caso, o Aspose.PDF para Python fornece a propriedade [page_numbers_prefix](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/#properties) da classe [TocInfo](https://reference.aspose.com/pdf/python-net/aspose.pdf/tocinfo/) que pode ser usada para personalizar os números de página conforme mostrado no exemplo de código a seguir.

```python

    import aspose.pdf as ap

    # Carregar um arquivo PDF existente
    doc = ap.Document(input_pdf)
    # Obter acesso à primeira página do arquivo PDF
    toc_page = doc.pages.insert(1)
    # Criar objeto para representar as informações do TOC
    toc_info = ap.TocInfo()
    title = ap.text.TextFragment("Índice")
    title.text_state.font_size = 20
    title.text_state.font_style = ap.text.FontStyles.BOLD
    # Definir o título para o TOC
    toc_info.title = title
    toc_info.page_numbers_prefix = "P"
    toc_page.toc_info = toc_info
    for i in range(len(doc.pages)):
        # Criar objeto de Título
        heading2 = ap.Heading(1)
        segment2 = ap.text.TextSegment()
        heading2.toc_page = toc_page
        heading2.segments.append(segment2)
        # Especificar a página de destino para o objeto de título
        heading2.destination_page = doc.pages[i + 1]
        # Página de destino
        heading2.top = doc.pages[i + 1].rect.height
        # Coordenada de destino
        segment2.text = "Página " + str(i)
        # Adicionar título à página contendo o TOC
        toc_page.paragraphs.add(heading2)

    # Salvar o documento atualizado
    doc.save(output_pdf)

```


## Como definir a data de expiração do PDF

Aplicamos privilégios de acesso em arquivos PDF para que um determinado grupo de usuários possa acessar recursos/objetos específicos de documentos PDF. Para restringir o acesso ao arquivo PDF, geralmente aplicamos criptografia e podemos ter a necessidade de definir a expiração do arquivo PDF, para que o usuário que acessa/visualiza o documento receba um aviso válido sobre a expiração do arquivo PDF.

```python

    import aspose.pdf as ap

    # Instanciar objeto Document
    doc = ap.Document()
    # Adicionar página à coleção de páginas do arquivo PDF
    doc.pages.add()
    # Adicionar fragmento de texto à coleção de parágrafos do objeto página
    doc.pages[1].paragraphs.add(ap.text.TextFragment("Olá Mundo..."))
    # Criar objeto JavaScript para definir a data de expiração do PDF
    javaScript = ap.annotations.JavascriptAction(
        "var year=2017;"
        + "var month=5;"
        + "today = new Date(); today = new Date(today.getFullYear(), today.getMonth());"
        + "expiry = new Date(year, month);"
        + "if (today.getTime() > expiry.getTime())"
        + "app.alert('O arquivo expirou. Você precisa de um novo.');"
    )
    # Definir JavaScript como ação de abertura do PDF
    doc.open_action = javaScript

    # Salvar documento PDF
    doc.save(output_pdf)
```


## Flatten Fillable PDF em Python

Documentos PDF frequentemente incluem formulários com widgets interativos preenchíveis, tais como botões de rádio, caixas de seleção, caixas de texto, listas, etc. Para torná-los não editáveis para várias finalidades de aplicação, precisamos achatar o arquivo PDF. Aspose.PDF fornece a função para achatar seu PDF em Python com apenas algumas linhas de código:

```python

    import aspose.pdf as ap

    # Carregar formulário PDF de origem
    doc = ap.Document(input_pdf)

    # Achatar PDF preenchível
    if len(doc.form.fields) > 0:
        for item in doc.form.fields:
            item.flatten()

    # Salvar o documento atualizado
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
    "downloadUrl": "https://releases.aspose.com/pdf/python-net",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/example.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>