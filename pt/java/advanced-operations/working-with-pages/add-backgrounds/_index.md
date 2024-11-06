---
title: Adicionar fundo ao PDF 
linktitle: Adicionar fundos
type: docs
weight: 110
url: pt/java/add-backgrounds/
descriptions: Adicione uma imagem de fundo ao seu arquivo PDF com Java. Use o objeto BackgroundArtifact.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Imagens de fundo podem ser usadas para adicionar uma marca d'água ou outro design sutil a documentos. No Aspose.PDF para Java, cada documento PDF é uma coleção de páginas e cada página contém uma coleção de artefatos. A classe [BackgroundArtifact](https://reference.aspose.com/pdf/java/com.aspose.pdf/BackgroundArtifact) pode ser usada para adicionar uma imagem de fundo a um objeto de página.

O seguinte trecho de código mostra como adicionar uma imagem de fundo às páginas de um PDF usando o objeto BackgroundArtifact com Java.

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

import com.aspose.pdf.BackgroundArtifact;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;

public class ExampleAddBackground {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void InsertEmptyPageInPDFFileAtDesiredLocation() throws FileNotFoundException {
        // Para exemplos completos e arquivos de dados, por favor vá para
        // https://github.com/aspose-pdf/Aspose.Pdf-for-Java
        String myDir = "";
        // Cria um novo objeto Documento
        Document doc = new Document();
        // Adiciona uma nova página ao objeto documento
        Page page = doc.getPages().add();
        // Cria objeto BackgroundArtifact
        BackgroundArtifact background = new BackgroundArtifact();
        // Especifica a imagem para o objeto backgroundartifact
        background.setBackgroundImage(new FileInputStream(myDir + "logo.png"));
        // Adiciona backgroundartifact à coleção de artefatos da página
        page.getArtifacts().add(background);
        // Salva o documento
        doc.save(_dataDir + "BackGround.pdf");
    }
}
```