---
title: Criar Links em Arquivo PDF
linktitle: Criar Links
type: docs
weight: 10
url: /pt/java/create-links/
description: Esta seção explica como criar links em seu documento PDF com Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Criar Links

Aspose.PDF para Java permite adicionar um link a um arquivo PDF externo para que você possa interligar vários documentos.
Ao adicionar um link a um aplicativo em um documento, é possível vincular a aplicativos a partir de um documento. Isso é útil quando você deseja que os leitores tomem uma certa ação em um ponto específico de um tutorial, por exemplo, ou para criar um documento rico em recursos. Para criar um link de aplicativo:

1. [Crie um Objeto Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Obtenha a [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) à qual você deseja adicionar o link.

1. Crie um objeto [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) usando os objetos [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) e [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).
1. Defina os atributos do link usando o objeto [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation).
1. Além disso, defina para os objetos [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction) e chame o método setAction(..).
1. Ao criar o objeto [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/LaunchAction), especifique o aplicativo que você deseja iniciar.
1. Adicione o link à coleção [Annotations](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) do objeto Page.
1. Finalmente, salve o PDF atualizado usando o método Save do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

O seguinte trecho de código mostra como criar um link para um aplicativo em um arquivo PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;


public class ExampleLinks {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    private static String GetDataDir() {
        String os = System.getProperty("os.name");
        if (os.startsWith("Windows"))
            _dataDir = "C:\\Samples\\Links-Actions";
        return _dataDir;
    }

    public static void CreateLink() {

        // Abrir documento
        Document document = new Document(GetDataDir() + "CreateApplicationLink.pdf");

        // Criar link
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, _dataDir + "sample.pdf"));
        page.getAnnotations().add(link);

        // Salvar documento atualizado
        document.save(_dataDir + "CreateApplicationLink_out.pdf");
    }
```

### Criar Link de Documento PDF em um Arquivo PDF

Aspose.PDF para Java permite adicionar um link para um arquivo PDF externo, para que você possa conectar vários documentos juntos.
 Para criar um link de documento PDF:

1. Primeiro, crie um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Em seguida, obtenha a [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) específica à qual você deseja adicionar o link.
1. Crie um objeto [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation) usando os objetos [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) e [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).
1. Defina os atributos do link usando o objeto [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation).
1. Chame o método setAction(..) e passe o objeto [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction).
1. Ao criar o objeto [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/GoToRemoteAction), especifique o arquivo PDF que deve ser lançado, bem como o número da página que deve ser aberta.
1. Adicione o link à coleção de [Anotações](https://reference.aspose.com/pdf/java/com.aspose.pdf/AnnotationCollection) do objeto Page.
2. Finalmente, salve o PDF atualizado usando o método Save do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

O trecho de código a seguir mostra como criar um link de documento PDF em um arquivo PDF.

```java
    public static void CreatePDFDocumentLink() {

        // Abrir documento
        Document document = new Document(_dataDir + "CreateDocumentLink.pdf");

        // Criar link
        Page page = document.getPages().get_Item(1);
        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(100, 200, 300, 300));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(_dataDir + "sample.pdf", 1));
        page.getAnnotations().add(link);

        // Salvar documento atualizado
        document.save(_dataDir + "CreateDocumentLink_out.pdf");
    }
```