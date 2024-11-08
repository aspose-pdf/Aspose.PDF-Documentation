---
title: Converter PNG para PDF 
linktitle: Converter PNG para PDF
type: docs
weight: 200
url: /pt/androidjava/convert-png-to-pdf/
lastmod: "2021-06-05"
description: Este artigo mostra como converter PNG para PDF com a biblioteca Aspose.PDF em suas aplicações Android via Java. Você pode converter imagens PNG para o formato PDF usando etapas simples.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF para Android via Java** suporta o recurso de converter imagens PNG para o formato PDF. Confira o próximo trecho de código para realizar sua tarefa.

<abbr title="Portable Network Graphics">PNG</abbr> refere-se a um tipo de formato de arquivo de imagem raster que usa compressão sem perdas, o que o torna popular entre seus usuários.

Você pode converter PNG para imagem PDF usando as etapas abaixo:

1. Carregar imagem PNG de entrada
1. Ler valores de altura e largura
1. Criar novo documento e adicionar Página
1. Definir dimensões da página
1. Salvar arquivo de saída

Além disso, o trecho de código abaixo mostra como converter PNG para PDF em suas aplicações Java:

```java
    public void convertPNGtoPDF () {
        // Inicializar objeto de documento
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/sample.png");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
```