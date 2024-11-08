---
title: Obter Preferência de Visualização de Arquivo PDF
type: docs
weight: 70
url: /pt/net/get-viewer-preference-of-an-existing-pdf-file/
description: Esta seção mostra como obter a preferência de visualização de um arquivo PDF existente usando a Classe PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Obter Preferência de Visualização de um Arquivo PDF Existente

A classe [ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) representa modos de exibição de arquivos PDF; por exemplo, posicionar a janela do documento no centro da tela, ocultar a barra de menu do aplicativo de visualização, etc.

Para ler as configurações, usamos a classe [GetViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/getviewerpreference). Este método retorna uma variável onde todas as configurações são salvas.

```csharp
      public static void GetViewerPreference()
        {
            var document = new Document(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Alterar Preferências de Visualização
            var preferences = editor.GetViewerPreference();
            if ((preferences & ViewerPreference.CenterWindow) != 0)
                Console.WriteLine("CenterWindow");
            if ((preferences & ViewerPreference.HideMenubar) != 0)
                Console.WriteLine("Menu bar hided");
            if ((preferences & ViewerPreference.PageModeFullScreen) != 0)
                Console.WriteLine("Page Mode Full Screen");
        }
```