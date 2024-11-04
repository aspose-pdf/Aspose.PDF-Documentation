---
title: Noções básicas da API DOM do Aspose.PDF
linktitle: Noções básicas da API DOM
type: docs
weight: 10
url: /androidjava/basics-of-dom-api/
description: Aspose.PDF para Android via Java também utiliza a ideia de DOM para representar a estrutura de um documento PDF em termos de objetos. Aqui você pode ler a descrição dessa estrutura.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introdução à API DOM

O Modelo de Objeto de Documento (DOM) é uma forma de representação de documentos estruturados como um modelo orientado a objetos. DOM é o padrão oficial do World Wide Web Consortium (W3C) para representar documentos estruturados de maneira neutra em relação à plataforma e à linguagem.

Em palavras simples, DOM é uma árvore de objetos que representa a estrutura de algum documento.
 Aspose.PDF para Android via Java também utiliza a ideia de DOM para representar a estrutura de um documento PDF em termos de objetos. No entanto, os aspectos do DOM (como seus Elementos) são manipulados dentro da sintaxe da linguagem de programação em uso. A interface pública de um DOM é especificada em sua interface de programação de aplicativos (API).

### Introdução ao Documento PDF

Portable Document Format (PDF) é um padrão aberto para troca de documentos. Um documento PDF é uma combinação de texto e dados binários. Se você abri-lo em um editor de texto, verá os objetos brutos que definem a estrutura e o conteúdo do documento.

A estrutura lógica de um arquivo PDF é hierárquica e determina a sequência pela qual um aplicativo de visualização desenha as páginas do documento e seus conteúdos. Um PDF é composto por quatro componentes: objetos, estrutura de arquivo, estrutura de documento e fluxos de conteúdo.

### Estrutura do Documento PDF

Como a estrutura de um arquivo PDF é hierárquica, Aspose.PDF para Java também acessa os elementos da mesma forma. A hierarquia a seguir mostra como o documento PDF é estruturado logicamente e como o Aspose.PDF para Java DOM API o constrói.

![Estrutura do Documento PDF](https://docs.aspose.com/pdf/java/images/structure.png)

### Acessando Elementos do Documento PDF

O objeto Documento está no nível raiz do modelo de objeto. O Aspose.PDF para Android via Java DOM API permite que você crie um objeto Documento e então acesse todos os outros objetos na hierarquia. Você pode acessar qualquer uma das coleções como Páginas ou elementos individuais como Página, etc. A API DOM fornece pontos de entrada e saída únicos para manipular o documento PDF como mostrado abaixo:

- Abrir documento PDF
- Acessar estrutura do documento PDF no estilo DOM
- Atualizar dados no documento PDF
- Validar documento PDF
- Exportar documento PDF em diferentes formatos
- Finalmente, salvar o documento PDF atualizado

## Como Usar o Novo Aspose.PDF para Android via Java API

Este tópico explicará o novo Aspose.PDF para Android via Java API e o guiará para começar rápida e facilmente. Observe que os detalhes sobre o uso das funcionalidades específicas não fazem parte deste artigo.

O Aspose.PDF para Android via Java é composto por duas partes:

- Aspose.PDF para Android via Java DOM API
- Aspose.PDF.Facades 

Você encontrará os detalhes de cada uma dessas áreas abaixo.

### Aspose.PDF para Android via Java DOM API

O novo Aspose.PDF para Android via Java DOM API corresponde à estrutura do documento PDF, o que ajuda você a trabalhar com documentos PDF não apenas no nível de arquivo e documento, mas também no nível de objeto. Fornecemos mais flexibilidade aos desenvolvedores para acessar todos os elementos e objetos do documento PDF. Usando as classes do Aspose.PDF DOM API, você pode obter acesso programático aos elementos e formatação do documento. Esta nova API DOM é composta por vários namespaces, conforme dado abaixo:

### com.aspose.pdf

Este namespace fornece a classe Document, que permite abrir e salvar um documento PDF. A classe License também faz parte deste namespace. Ela também fornece classes relacionadas a páginas PDF, anexos e marcadores como com.aspose.pdf.Page, com.aspose.pdf.PageCollection, com.aspose.pdf.FileSpecification, com.aspose.pdf.EmbeddedFileCollection, com.aspose.pdf.OutlineItemCollection e com.aspose.pdf.OutlineCollection etc.

#### com.aspose.pdf.text

Este namespace fornece classes que ajudam a trabalhar com o texto e seus vários aspectos, por exemplo com.aspose.pdf.Font, com.aspose.pdf.FontCollection, com.aspose.pdf.FontRepository, com.aspose.pdf.FontStyles, com.aspose.pdf.TextAbsorber, com.aspose.pdf.TextFragment, com.aspose.pdf.TextFragmentAbsorber, com.aspose.pdf.TextFragmentCollection, com.aspose.pdf.TextFragmentState, com.aspose.pdf.TextSegment e com.aspose.pdf.TextSegmentCollection etc.

#### com.aspose.pdf.TextOptions

Este namespace fornece classes que permitem definir diferentes opções para pesquisar, editar ou substituir texto, por exemplo com.aspose.pdf.TextEditOptions, com.aspose.pdf.TextReplaceOptions e com.aspose.pdf.TextSearchOptions.
#### com.aspose.pdf.PdfAction

Este namespace contém classes que ajudam a trabalhar com os recursos interativos do documento PDF, por exemplo, trabalhar com o documento e outras ações. Este namespace contém classes como com.aspose.pdf.GoToAction, com.aspose.pdf.GoToRemoteAction e com.aspose.pdf.GoToURIAction etc.

#### com.aspose.pdf.Annotation

Anotações são parte dos recursos interativos de um documento PDF. Dedicamos um namespace para anotações. Este namespace contém classes que ajudam a trabalhar com as anotações, por exemplo, com.aspose.pdf.Annotation, com.aspose.pdf.AnnotationCollection, com.aspose.pdf.CircleAnnotation e com.aspose.pdf.LinkAnnotation etc.

#### com.aspose.pdf.Form

Este namespace contém classes que ajudam a trabalhar com formulários PDF e campos de formulário, por exemplo, com.aspose.pdf.Form, com.aspose.pdf.Field, com.aspose.pdf.TextBoxField e com.aspose.pdf.OptionCollection etc.

#### com.aspose.pdf.devices

Podemos realizar várias operações nos documentos PDF, como converter documentos PDF para vários formatos de imagem.
 No entanto, tais operações não pertencem ao objeto Document e não podemos estender a classe Document para tais operações. É por isso que introduzimos o conceito de Device na nova API DOM.

##### com.aspose.pdf.facades

Antes do Aspose.PDF para Java t.o.o, você precisava do Aspose.PDF.Kit para Java para manipular arquivos PDF existentes. Para executar o código antigo do Aspose.PDF.Kit, pode usar o namespace com.aspose.pdf.facades.