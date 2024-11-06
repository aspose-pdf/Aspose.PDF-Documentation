---
title: Obter Preferência do Visualizador de um Arquivo PDF Existente
type: docs
weight: 70
url: pt/java/get-viewer-preference-of-an-existing-pdf-file/
description: Esta seção mostra como trabalhar com Aspose.PDF Facades usando a Classe PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Obter Preferência do Visualizador de um Arquivo PDF Existente

A classe [ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) representa modos de exibição de arquivos PDF; por exemplo, posicionar a janela do documento no centro da tela, ocultar a barra de menu do aplicativo visualizador etc.

Para ler as configurações, usamos 'getViewerPreference'. Este método retorna uma variável onde todas as configurações são salvas.

```java
 public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Alterar Preferências do Visualizador
            var preferences = editor.getViewerPreference();
            if ((preferences & ViewerPreference.CENTER_WINDOW) != 0)
                System.out.println("Centralizar Janela");
            if ((preferences & ViewerPreference.HIDE_MENUBAR) != 0)
                System.out.println("Barra de menu ocultada");
        }
```