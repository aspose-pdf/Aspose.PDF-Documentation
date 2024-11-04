---
title: Teste de Conformidade PDF-UA - Lista de Erros
linktitle: Teste de Conformidade PDF-UA - Lista de Erros
type: docs
weight: 50
url: /net/pdf-ua-compliance-test-errors-list/
description: Este artigo mostra uma lista dos erros que podem ocorrer durante o teste de conformidade PDF/UA usando a API Aspose.PDF e C# ou VB.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Teste de Conformidade PDF-UA - Lista de Erros",
    "alternativeHeadline": "Teste de conformidade PDF/UA usando a API",
    "author": {
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "geração de documentos PDF",
    "keywords": "pdf, c#, geração de documentos",
    "wordcount": "302",
    "proficiencyLevel":"Iniciante",
    "publisher": {
        "@type": "Organization",
        "name": "Equipe de Documentação Aspose.PDF",
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
    "url": "/net/pdf-ua-compliance-test-errors-list/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/pdf-ua-compliance-test-errors-list/"
    },
    "dateModified": "2022-02-04",
    "description": "Este artigo mostra uma lista dos erros que podem ocorrer durante o teste de conformidade PDF/UA usando a API Aspose.PDF e C# ou VB."
}
</script>
Ao realizar testes de conformidade com PDF/UA usando a API Aspose.PDF, você pode estar interessado em conhecer as mensagens de erro que pode receber. Esses erros são de diferentes tipos, como Geral, Texto, Fontes, Cabeçalhos e vários outros. Informações sobre esses erros podem ser úteis para conhecer a causa exata dos erros e seu tratamento.

Neste artigo, listamos os erros que podem surgir durante os testes de conformidade com PDF/UA usando a API.

## **Geral**

|**Code**|**Severity**|**Message**|
| :- | :- | :- |
|5:1|Erro|Identificador de PDF/UA ausente|
|6.2:1.1|Erro|Árvore de pais estrutural: Entrada inconsistente encontrada|
|7.1:1.1(14.8.1)|Erro|Documento não marcado como etiquetado|
|7.1:1.1(14.8)|Erro|Objeto [OBJECT_NAME] não etiquetado|
|7.1:1.2(14.8.2.2)|Erro|Artefato presente dentro do conteúdo etiquetado|
|7.1:1.3(14.8.2.2)|Erro|Conteúdo etiquetado presente dentro de um artefato|
|7.1:2.1|Aviso|Árvore de estrutura ausente|
|7.1:2.2|Aviso|Elemento de estrutura 'Documento' encontrado que não é um elemento raiz|
|7.1:2.3|Aviso|Elemento de estrutura '[ELEMENT_NAME]' usado como elemento raiz|
|7.1:2.3|Aviso|Elemento de estrutura ‘[ELEMENT_NAME]’ usado como elemento raiz|
|7.1:2.4.1|Aviso|Uso possivelmente inapropriado de um elemento de estrutura ‘[ELEMENT_NAME]’|
|7.1:2.4.2|Erro|Uso inválido de um elemento de estrutura ‘[ELEMENT_NAME]’|
|7.1:2.5|Aviso|Possível erro de aninhamento do elemento de estrutura ‘[ELEMENT_NAME]’ em StructTreeRoot|
|7.1:3(14.8.4)|Erro|Tipo de estrutura não padrão ‘[TYPE_NAME]’ não está mapeado para um tipo de estrutura padrão nem para outro tipo de estrutura não padrão|
|7.1:4(14.8.4)|Aviso|Tipo de estrutura padrão ‘[TYPE_NAME]’ está remapeado para ‘[TYPE_NAME]’|
|7.1:5|Necessidade de verificação manual|Contraste de cores|
|7.1:6.1|Erro|Metadados XMP ausentes no documento|
|7.1:6.2|Erro|Título ausente nos metadados XMP do documento|
|7.1:6.3|Aviso|Título está vazio nos metadados XMP do documento|
|7.1:7.1(12.2)|Aviso|Dicionário ‘ViewerPreferences’ ausente|
|7.1:7.2(12.2)|Erro|Entrada ‘DisplayDocTitle’ não está configurada|
|7.1:8(14.7.1)|Erro|Entrada ‘Suspects’ está configurada|
|7.1:9.1(14.7)|Erro|Chave ‘StructParents’ ausente na página|
|7.1:9.2(14.7)|Erro|Entrada ‘StructParent’ ausente na anotação|
|7.1:9.2(14.7)|Erro|Entrada ‘StructParent’ ausente na anotação|
|7.1:9.3(14.7)|Erro|Entrada para ‘StructParents’ dado não encontrado|

## **Texto**

|**Código**|**Severidade**|**Mensagem**|
| :- | :- | :- |
|7.2:1|Necessita de verificação manual|Ordem de Leitura Lógica|
|7.2:2(14.8.2.4.2)|Erro|Caracteres em um objeto de texto não podem ser mapeados para Unicode|
|7.2:3.1(14.9.2.2)|Erro|Não é possível determinar a linguagem natural para o objeto de texto|
|7.2:3.2(14.9.2.2)|Erro|Não é possível determinar a linguagem natural do texto alternativo|
|7.2:3.3(14.9.2.2)|Erro|Não é possível determinar a linguagem natural do texto real|
|7.2:3.4(14.9.2.2)|Erro|Não é possível determinar a linguagem natural do texto de expansão|
|7.2:4(14.9.4)|Erro|Caractere esticável não etiquetado usando ActualText|

## **Fontes**

|**Cláusula**|**Severidade**|**Mensagem**|
| :- | :- | :- |
|7.21.3.1|Erro|Coleção de caracteres em CIDFont não é compatível com a coleção de caracteres do CMap interno|
|7.21.3.2|Erro|CIDToGIDMap não está embutido ou está incompleto na fonte ‘[FONT_NAME]’|
|7.21.3.2|Erro|CMap não está embutido para a fonte ‘[FONT_NAME]’|
|7.21.3.2|Erro|CMap não está incorporado para a fonte ‘[FONT_NAME]’|
|7.21.4.2|Erro|CIDSet está ausente ou incompleto para a fonte ‘[FONT_NAME]’|
|7.21.4.2|Erro|Glifos ausentes na fonte incorporada ‘[FONT_NAME]’|
|7.21.6|Erro|Fonte TrueType não simbólica ‘[FONT_NAME]’ não possui entradas cmap|
|7.21.6|Erro|Entrada de codificação proibida para fonte TrueType simbólica ‘[FONT_NAME]’|
|7.21.6|Erro|Codificação incorreta usada para fonte TrueType ‘[FONT_NAME]’|
|7.21.6|Erro|Array “Differences” incorreto para fonte TrueType não simbólica ‘[FONT_NAME]’|

## **Gráficos**

|**Código**|**Severidade**|**Mensagem**|
| :- | :- | :- |
|7.3:1(14.8.4.5)|Erro|Elemento ‘[ELEMENT_NAME]’ em uma única página sem caixa delimitadora|
|7.3:2|Erro|Texto alternativo ausente para elemento de estrutura ‘[ELEMENT_NAME]’|
|7.3:3|Erro|Legenda acompanhando figura ausente|
|7.3:4(14.8.4.5)|Erro|Objeto gráfico aparece entre os operadores BT e ET|

## **Títulos**

|**Código**|**Severidade**|**Mensagem**|
| :- | :- | :- |
|7.4.2:1|Erro|O primeiro título não está no primeiro nível|
|7.4.2:2|Erro|Título numerado pula um ou mais níveis de título|
|7.4.2:2|Erro|Cabeçalho numerado pula um ou mais níveis de cabeçalho|
|7.4.4:1|Erro|Elementos de estrutura 'H' e 'Hn' encontrados|
|7.4.4:2|Erro|Mais de um elemento de estrutura 'H' dentro do elemento de estrutura pai|

## **Tabelas**

|**Código**|**Severidade**|**Mensagem**|
| :- | :- | :- |
|7.5:1|Aviso|Linha irregular na tabela|
|7.5:2|Erro|Célula de cabeçalho da tabela não tem subcélulas associadas|
|7.5:3.1|Aviso|Cabeçalhos de tabela ausentes|
|7.5:3.2|Aviso|Resumo da tabela ausente|

## **Listas**

|**Código**|**Severidade**|**Mensagem**|
| :- | :- | :- |
|7.6:1|Erro|Elemento de estrutura 'LI' deve ser filho do elemento 'L'|
|7.6:2|Erro|Elementos de estrutura 'Lbl' e 'LBody' devem ser filhos do elemento 'LI'|

## **Notas e referências**

|**Código**|**Severidade**|**Mensagem**|
| :- | :- | :- |
|7.9:2.1|Erro|ID ausente no elemento de estrutura 'Nota'|
|7.9:2.2|Erro|Entrada de ID no elemento de estrutura 'Nota' não é única|

## **Conteúdo opcional**

|**Código**|**Severidade**|**Mensagem**|
| :- | :- | :- |
|7.10:1|Erro|'Nome' ausente no dicionário de configuração de conteúdo opcional|
|7.10:1|Erro|‘Name’ ausente no dicionário de configuração de conteúdo opcional|
|7.10:2|Erro|Dicionário de configuração de conteúdo opcional contém a chave ‘AS’|

## **Arquivos embutidos**

|**Código**|**Severidade**|**Mensagem**|
| :- | :- | :- |
|7.11:1|Erro|Chave ‘F’ ou ‘UF’ ausente na especificação do arquivo|
|7.11:2|Aviso|Chave ‘Desc’ ausente na especificação do arquivo|

## **Assinaturas digitais**

|**Código**|**Severidade**|**Mensagem**|
| :- | :- | :- |
|7.13:1|Erro|Campo de assinatura ‘[FIELD_NAME]’ não está conforme a especificação|
|7.13:2.1|Erro|Não é possível determinar o idioma natural de um nome alternativo de um campo de formulário ‘[FIELD_NAME]’|
|7.13:2.2|Erro|Entrada de nome de campo alternativo ausente no campo de formulário ‘[FIELD_NAME]’|

## **Formulários não interativos**

|**Código**|**Severidade**|**Mensagem**|
| :- | :- | :- |
|7.14:1|Erro|Atributo ‘PrintField’ ausente no item de formulário não interativo|

## **XFA**

|**Código**|**Severidade**|**Mensagem**|
| :- | :- | :- |
|7.15:1|Erro|PDF contém um formulário XFA dinâmico|

## **Segurança**

|**Código**|**Severidade**|**Mensagem**|
|**Código**|**Severidade**|**Mensagem**|
| :- | :- | :- |
|7.16:1(7.6.3.2)|Erro|Configurações de segurança impedem que tecnologias assistivas acessem o conteúdo do documento|
|7.16:2(7.6.3.2)|Erro|A conversão não é permitida por restrições de permissão|

## **Navegação**

|**Código**|**Severidade**|**Mensagem**|
| :- | :- | :- |
|7.17:1|Erro|Erro no contorno do documento|
|7.17:2|Erro|Não é possível determinar o idioma natural dos contornos|
|7.17:3|Necessita verificação manual|Rótulos de Páginas semanticamente apropriados|

## **Anotações**

|**Código**|**Severidade**|**Mensagem**|
| :- | :- | :- |
|7.18.1:1|Erro|Não é possível determinar o idioma natural da entrada de Conteúdos|
|7.18.1:2|Erro|Descrição alternativa ausente para uma anotação|
|7.18.1:3|Erro|Anotação não está aninhada dentro de um elemento de estrutura ‘Annot’|
|7.18.2:1|Erro|Uma anotação com subtipo não definido na ISO 32000 não atende a 7.18.1|
|7.18.2:2|Erro|Existe uma anotação do subtipo TrapNet|
|7.18.3:1|Erro|Entrada de ordem de tabulação em página com anotações não definida como 'S' (Estrutura)|
|7.18.4:1|Erro|Anotação ‘Widget’ não está aninhada dentro de um elemento de estrutura ‘Form’|
|7.18.4:1|Erro|A anotação 'Widget' não está aninhada dentro de um elemento de estrutura 'Form'|
|7.18.5:1|Erro|A anotação 'Link' não está aninhada dentro de um elemento de estrutura 'Link'|
|7.18.6.2:1|Erro|A chave CT está ausente no dicionário de dados do clipe de mídia|
|7.18.6.2:2|Erro|A chave Alt está ausente no dicionário de dados do clipe de mídia|
|7.18.7:1|Erro|Anotação de anexo de arquivo. Chave 'F' ou 'UF' ausente na especificação do arquivo|
|7.18.7:2|Aviso|Anotação de anexo de arquivo. Chave 'Desc' ausente na especificação do arquivo|
|7.18.8:1|Erro|Uma anotação PrinterMark está incluída na estrutura lógica|
|7.18.8:2|Erro|O fluxo de aparência de uma anotação PrinterMark não está marcado como Artefato|

## **Ações**

|**Código**|**Severidade**|**Mensagem**|
| :- | :- | :- |
|7.19:1|Necessita verificação manual|Ações foram encontradas. Necessário verificar as ações de acordo com a especificação PDF/UA manualmente|

## **XObjects**

|**Código**|**Severidade**|**Mensagem**|
| :- | :- | :- |
|7.20:1|Erro|XObject de Referência não deve ser usado em arquivo PDF/UA conforme|
|7.20:2|Erro|O conteúdo do Form XObject não está incorporado nos elementos de estrutura|
|7.20:2|Erro|O conteúdo do Form XObject não é incorporado aos elementos estruturais|

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Biblioteca Aspose.PDF para .NET",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Biblioteca de Manipulação de PDF para .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>


