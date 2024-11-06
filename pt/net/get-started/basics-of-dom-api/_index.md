---
title: Noções básicas da API DOM do Aspose.PDF
linktitle: Noções básicas da API DOM
type: docs
weight: 140
url: pt/net/basics-of-dom-api/
description: O Aspose.PDF para .NET também utiliza a ideia de DOM para representar a estrutura de um documento PDF em termos de objetos.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introdução à API DOM

Modelo de Objeto de Documento (DOM) é uma forma de representação de documentos estruturados como um modelo orientado a objetos. DOM é o padrão oficial do World Wide Web Consortium (W3C) para representar documentos estruturados de uma maneira neutra em relação à plataforma e à linguagem.

Em palavras simples, DOM é uma árvore de objetos que representam a estrutura de algum documento.
Em palavras simples, DOM é uma árvore de objetos que representam a estrutura de algum documento.

### Introdução ao Documento PDF

O Formato de Documento Portátil (PDF) é um padrão aberto para troca de documentos. Um documento PDF é uma combinação de texto e dados binários. Se você o abrir em um editor de texto, verá os objetos brutos que definem a estrutura e o conteúdo do documento.

A estrutura lógica de um arquivo PDF é hierárquica e determina a sequência pela qual uma aplicação de visualização desenha as páginas do documento e seus conteúdos. Um PDF é composto por quatro componentes: objetos, estrutura de arquivo, estrutura de documento e fluxos de conteúdo.

### Estrutura do Documento PDF

Como a estrutura de um arquivo PDF é hierárquica, o Aspose.PDF para .NET também acessa os elementos da mesma maneira. A seguinte hierarquia mostra como o documento PDF é estruturado logicamente e como o DOM API do Aspose.PDF para .NET o constrói.

![Estrutura do Documento PDF](../images/structure.png)

### Acessando os Elementos do Documento PDF

O objeto Document está no nível raiz do modelo de objeto.
O objeto Documento está no nível raiz do modelo de objeto.

- Abrir documento PDF
- Acessar a estrutura do documento PDF em estilo DOM
- Atualizar dados no documento PDF
- Validar documento PDF
- Exportar documento PDF em diferentes formatos
- Finalmente, salvar o documento PDF atualizado

## Como Usar a Nova API Aspose.PDF para .NET

Este tópico explicará a nova API Aspose.PDF para .NET e orientará você a começar de forma rápida e fácil. Por favor, observe que os detalhes sobre o uso das funcionalidades específicas não fazem parte deste artigo.

O Aspose.PDF para .NET é composto de duas partes:

- Aspose.PDF para .NET DOM API
- Aspose.PDF.Facades (antigo Aspose.PDF.Kit para .NET)
Você encontrará os detalhes de cada uma dessas áreas abaixo.

### Aspose.PDF para .NET DOM API

A API DOM Aspose.PDF para .NET corresponde à estrutura do documento PDF, que ajuda você a trabalhar com os documentos PDF não apenas no nível de arquivo e documento, mas também no nível de objeto.
### Aspose.PDF

Este namespace fornece a classe Document que permite abrir e salvar um documento PDF. A classe License também faz parte deste namespace. Ele também fornece classes relacionadas às páginas do PDF, anexos e favoritos como Page, PageCollection, FileSpecification, EmbeddedFileCollection, OutlineItemCollection e OutlineCollection etc.

#### Aspose.Text

Este namespace fornece classes que ajudam a trabalhar com o texto e seus vários aspectos, por exemplo Font, FontCollection, FontRepository, FontStyles, TextAbsorber, TextFragment, TextFragmentAbsorber, TextFragmentCollection, TextFragmentState, TextSegment e TextSegmentCollection etc.

#### Aspose.Text.TextOptions

Este namespace fornece classes que permitem definir diferentes opções para pesquisar, editar ou substituir texto, por exemplo TextEditOptions, TextReplaceOptions e TextSearchOptions.
Este namespace fornece classes que permitem definir diferentes opções para pesquisar, editar ou substituir texto, por exemplo, TextEditOptions, TextReplaceOptions e TextSearchOptions.

#### Aspose.InteractiveFeatures

Este namespace contém classes que ajudam você a trabalhar com os recursos interativos do documento PDF, por exemplo, trabalhando com o documento e outras ações. Este namespace contém classes como GoToAction, GoToRemoteAction e GoToURIAction etc.

#### Aspose.InteractiveFeatures.Annotations

As anotações são parte dos recursos interativos de um documento PDF. Dedicamos um namespace para anotações. Este namespace contém classes que ajudam você a trabalhar com as anotações, por exemplo, Annotation, AnnotationCollection, CircleAnnotation e LinkAnnotation etc.

#### Aspose.InteractiveFeatures.Forms

Este namespace contém classes que ajudam você a trabalhar com formulários PDF e campos de formulário, por exemplo, Form, Field, TextBoxField e OptionCollection etc.

#### Aspose.PDF.Devices

Podemos realizar várias operações nos documentos PDF, como converter o documento PDF para vários formatos de imagem.
Podemos realizar várias operações em documentos PDF, como converter documentos PDF em vários formatos de imagem.

##### Aspose.PDF.Facades

Antes do Aspose.PDF para .NET, era necessário o Aspose.PDF.Kit para .NET para manipular arquivos PDF existentes. Para executar o código antigo do Aspose.PDF.Kit, pode usar o namespace Aspose.PDF.Facades.
