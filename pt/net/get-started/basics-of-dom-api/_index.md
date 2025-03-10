---
title: Fundamentos da API DOM do Aspose.PDF
linktitle: Fundamentos da API DOM
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 130
url: /pt/net/basics-of-dom-api/
description: Aspose.PDF for .NET também usa a ideia de DOM para representar a estrutura de um documento PDF em termos de objetos.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Basics of Aspose.PDF DOM API",
    "alternativeHeadline": "Enhanced PDF Manipulation with Aspose.PDF DOM API in C#",
    "abstract": "A nova API DOM Aspose.PDF for .NET fornece uma abordagem robusta orientada a objetos para manipular documentos PDF, representando sua estrutura como uma árvore hierárquica. Esse recurso permite que os desenvolvedores acessem, atualizem e exportem elementos PDF facilmente, enquanto aprimoram a flexibilidade e o controle sobre a manipulação de documentos por meio de uma interface de programação intuitiva.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "891",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
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
    "url": "/net/basics-of-dom-api/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/basics-of-dom-api/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Introdução à API DOM

O Modelo de Objeto de Documento (DOM) é uma forma de representação de documentos estruturados como um modelo orientado a objetos. O DOM é o padrão oficial do World Wide Web Consortium (W3C) para representar documentos estruturados de maneira neutra em relação a plataforma e linguagem.

Em palavras simples, o DOM é uma árvore de objetos que representa a estrutura de algum documento. Aspose.PDF for .NET também usa a ideia de DOM para representar a estrutura de um documento PDF em termos de objetos. No entanto, os aspectos do DOM (como seus Elementos) são manipulados dentro da sintaxe da linguagem de programação em uso. A interface pública de um DOM é especificada em sua interface de programação de aplicativos (API).

### Introdução ao Documento PDF

O Formato de Documento Portátil (PDF) é um padrão aberto para troca de documentos. Um documento PDF é uma combinação de dados de texto e binários. Se você abri-lo em um editor de texto, verá os objetos brutos que definem a estrutura e o conteúdo do documento.

A estrutura lógica de um arquivo PDF é hierárquica e determina a sequência pela qual um aplicativo de visualização desenha as páginas do documento e seus conteúdos. Um PDF é composto por quatro componentes: objetos, estrutura de arquivo, estrutura de documento e fluxos de conteúdo.

### Estrutura do Documento PDF

Como a estrutura de um arquivo PDF é hierárquica, Aspose.PDF for .NET também acessa os elementos da mesma forma. A seguinte hierarquia mostra como o documento PDF está logicamente estruturado e como a API DOM do Aspose.PDF for .NET o constrói.

![Estrutura do Documento PDF](../images/structure.png)

### Acessando Elementos do Documento PDF

O objeto Document está no nível raiz do modelo de objeto. A API DOM do Aspose.PDF for .NET permite que você crie um objeto Document e, em seguida, acesse todos os outros objetos na hierarquia. Você pode acessar qualquer uma das coleções, como Pages, ou elementos individuais, como Page, etc. A API DOM fornece pontos de entrada e saída únicos para manipular o documento PDF, conforme mostrado abaixo:

- Abrir documento PDF.
- Acessar a estrutura do documento PDF no estilo DOM.
- Atualizar dados no documento PDF.
- Validar documento PDF.
- Exportar documento PDF para diferentes formatos.
- Por fim, salvar o documento PDF atualizado.

## Como Usar a Nova API Aspose.PDF for .NET

Este tópico explicará a nova API Aspose.PDF for .NET e orientará você a começar rapidamente e facilmente. Observe que os detalhes sobre o uso de recursos específicos não fazem parte deste artigo.

O Aspose.PDF for .NET é composto por duas partes:

- API DOM Aspose.PDF for .NET.
- Aspose.Pdf.Facades (antigo Aspose.PDF.Kit para .NET).

Você encontrará os detalhes de cada uma dessas áreas abaixo.

### API DOM Aspose.PDF for .NET

A API DOM Aspose.PDF for .NET corresponde à estrutura do documento PDF, que ajuda você a trabalhar com os documentos PDF não apenas no nível de arquivo e documento, mas também no nível de objeto. Nós fornecemos mais flexibilidade aos desenvolvedores para acessar todos os elementos e objetos do documento PDF. Usando as classes da API DOM do Aspose.PDF, você pode obter acesso programático aos elementos e formatação do documento. Esta nova API DOM é composta por vários namespaces, conforme dado abaixo:

### Aspose.PDF

Este namespace fornece a classe Document, que permite abrir e salvar um documento PDF. A classe License também faz parte deste namespace. Ele também fornece classes relacionadas a páginas PDF, anexos e marcadores, como Page, PageCollection, FileSpecification, EmbeddedFileCollection, OutlineItemCollection e OutlineCollection, etc.

#### Aspose.Text

Este namespace fornece classes que ajudam você a trabalhar com o texto e seus vários aspectos, por exemplo, Font, FontCollection, FontRepository, FontStyles, TextAbsorber, TextFragment, TextFragmentAbsorber, TextFragmentCollection, TextFragmentState, TextSegment e TextSegmentCollection, etc.

#### Aspose.Text.TextOptions

Este namespace fornece classes que permitem definir diferentes opções para pesquisar, editar ou substituir texto, por exemplo, TextEditOptions, TextReplaceOptions e TextSearchOptions.

#### Aspose.InteractiveFeatures

Este namespace contém classes que ajudam você a trabalhar com os recursos interativos do documento PDF, por exemplo, trabalhando com o documento e outras ações. Este namespace contém classes como GoToAction, GoToRemoteAction e GoToURIAction, etc.

#### Aspose.InteractiveFeatures.Annotations

Anotações são uma parte dos recursos interativos de um documento PDF. Nós dedicamos um namespace para anotações. Este namespace contém classes que ajudam você a trabalhar com as anotações, por exemplo, Annotation, AnnotationCollection, CircleAnnotation e LinkAnnotation, etc.

#### Aspose.InteractiveFeatures.Forms

Este namespace contém classes que ajudam você a trabalhar com formulários PDF e campos de formulário, por exemplo, Form, Field, TextBoxField e OptionCollection, etc.

#### Aspose.Pdf.Devices

Podemos realizar várias operações nos documentos PDF, como converter documentos PDF para vários formatos de imagem. No entanto, tais operações não pertencem ao objeto Document e não podemos estender a classe Document para tais operações. É por isso que introduzimos o conceito de Device na nova API DOM.

#### Aspose.Pdf.Facades

Antes do Aspose.PDF for .NET, você precisava do Aspose.PDF.Kit para .NET para manipular arquivos PDF existentes. Para executar o código antigo do Aspose.PDF.Kit, você pode usar o namespace Aspose.PDF.Facades.