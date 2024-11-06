---
title: Criando um PDF complexo usando Aspose.PDF
linktitle: Criando um PDF complexo
type: docs
weight: 30
url: pt/androidjava/complex-pdf-example/
description: Aspose.PDF para Android via Java permite criar documentos mais complexos que contêm imagens, fragmentos de texto e tabelas em um único documento.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

O exemplo [Hello, World](/pdf/java/hello-world-example/) mostrou etapas simples para criar um documento PDF usando Java e Aspose.PDF. Neste artigo, vamos dar uma olhada em como criar um documento mais complexo com Java e Aspose.PDF para Java. Como exemplo, usaremos um documento de uma empresa fictícia que opera serviços de ferry para passageiros.
Nosso documento conterá uma imagem, dois fragmentos de texto (cabeçalho e parágrafo), e uma tabela. Para construir tal documento, usaremos a abordagem baseada em DOM. Você pode ler mais na seção [Noções básicas da API DOM](/pdf/java/basics-of-dom-api/).

Se criarmos um documento do zero, precisamos seguir certas etapas:

1. Instanciar um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). Neste passo, criaremos um documento PDF vazio com alguns metadados, mas sem páginas.
1. Adicionar uma [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) ao objeto do documento. Agora, nosso documento terá uma página.
1. Para adicionar uma imagem, criamos um FileInputStream, indicando o caminho para o arquivo que precisamos. Em seguida, adicionamos a imagem ao retângulo com as coordenadas fornecidas.
1. Criar um [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) para o cabeçalho. Para o cabeçalho, usaremos a fonte Arial com tamanho de fonte 24pt e alinhamento centralizado.
1. Adicionar o cabeçalho aos [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--) da página.
1. Criar um [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) para a descrição. Para a descrição, usaremos a fonte Arial com tamanho de fonte 24pt e alinhamento centralizado.

1. Adicione (descrição) aos parágrafos da página. Usamos as fontes "Helvetica" e "Times Roman" em nosso exemplo, mas lembre-se de que há apenas três fontes de sistema no Android:

- normal (Droid Sans);
- serif (Droid Serif);
- monospace (Droid Sans Mono).

1. Crie uma tabela, adicione propriedades à tabela.
1. Adicione (tabela) à página [Parágrafos](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Salve um documento "Complex.pdf".

No final, é exibido um pop-up com a mensagem "Documento PDF foi gerado!".


```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="32dp"
        android:layout_marginLeft="32dp"
        android:layout_marginRight="32dp"
        android:text="@string/title"
        android:textSize="24sp"
        android:visibility="visible"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <Button
        android:id="@+id/button"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="64dp"
        android:layout_marginLeft="32dp"
        android:layout_marginRight="32dp"
        android:text="@string/generate_btn" />

</LinearLayout>
```