---
title: Classe PdfFileEditor
type: docs
weight: 10
url: pt/net/pdffileeditor-class/
description: Esta seção explica como trabalhar com Aspose.PDF Facades usando a classe PdfFileEditor.
lastmod: "2021-06-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Trabalhar com documentos PDF inclui várias funções. Gerenciar as páginas de um arquivo PDF é uma parte importante deste trabalho. Aspose.PDF.Facaded fornece a classe `PdfFileEditor` para este propósito.

A classe PdfFileEditor contém os métodos que ajudam a manipular páginas individuais; esta classe não edita ou manipula o conteúdo de uma página. Você pode inserir uma nova página, excluir uma página existente, dividir as páginas ou especificar a imposição das páginas usando PdfFileEditor.

Os recursos fornecidos por esta classe podem ser divididos em três categorias principais, ou seja, Edição de Arquivos, Imposição de PDF e Divisão. Vamos discutir essas seções em detalhes abaixo:

## Edição de Arquivos

Os recursos que podemos incluir nesta seção são Inserir, Anexar, Excluir, Concatenar e Extrair. Você pode inserir uma nova página em um local especificado usando o método Insert, ou anexar as páginas no final do arquivo. Você também pode excluir qualquer número de páginas do arquivo usando o método Delete, especificando um array de inteiros contendo os números das páginas a serem excluídas. O método Concatenate ajuda a juntar páginas de vários arquivos PDF. Você pode extrair qualquer número de páginas usando o método Extract e salvar essas páginas em outro arquivo PDF ou fluxo de memória.

Esta seção explora as capacidades desta classe e explica o propósito de seus métodos.

- [Concatenar documentos PDF](/pdf/net/concatenate-pdf-documents/)
- [Extrair páginas PDF](/pdf/net/extract-pdf-pages/)
- [Inserir páginas PDF](/pdf/net/insert-pdf-pages/)
- [Excluir páginas PDF](/pdf/net/delete-pdf-pages/)

## Usando Quebras de Página

Quebra de Página é um recurso especial que permite o reflow do documento.

- [Quebra de Página em PDF existente](/pdf/net/page-break-in-existing-pdf/)

## Imposição de PDF

A imposição é o processo de organizar as páginas corretamente antes da impressão. `PdfFileEditor` fornece dois métodos para este propósito, ou seja, `MakeBooklet` e `MakeNUp`. O método MakeBooklet ajuda a organizar as páginas para que seja fácil dobrá-las ou encaderná-las após a impressão, no entanto, o método MakeNUp permite imprimir várias páginas em uma página do arquivo PDF.

- [Fazer Booklet de PDF](/pdf/net/make-booklet-of-pdf/)
- [Fazer NUp de arquivos PDF](/pdf/net/make-nup-of-pdf-files/)

## Divisão

A funcionalidade de divisão permite que você divida um arquivo PDF existente em diferentes partes. Você pode dividir a parte frontal do arquivo PDF ou a parte traseira. Como o PdfFileEditor fornece uma variedade de métodos para fins de divisão, você também pode dividir um arquivo em páginas individuais ou muitos conjuntos de várias páginas.

- [Dividir páginas de PDF](/pdf/net/split-pdf-pages/)