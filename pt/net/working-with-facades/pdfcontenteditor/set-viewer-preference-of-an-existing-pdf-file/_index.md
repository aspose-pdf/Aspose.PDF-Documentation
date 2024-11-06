---
title: Definir Preferência do Visualizador de PDF
type: docs
weight: 60
url: pt/net/set-viewer-preference-of-an-existing-pdf-file/
description: Esta seção mostra como definir a preferência do visualizador de um arquivo PDF existente usando a Classe PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Definir Preferência do Visualizador de um Arquivo PDF Existente

A classe [ViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference) representa modos de exibição de arquivos PDF; por exemplo, posicionar a janela do documento no centro da tela, ocultar a barra de menu do aplicativo visualizador etc.

O método [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) na classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) permite que você altere a preferência do visualizador. Para fazer isso, você precisa criar um objeto da classe [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) e vincular o arquivo PDF de entrada usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/bindpdf/index).

Depois disso, você pode chamar o método [ChangeViewerPreference](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/changeviewerpreference) para definir qualquer preferência. Finalmente, você deve salvar o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index). O trecho de código a seguir mostra como alterar a preferência do visualizador em um arquivo PDF existente.

Por exemplo, especificamos o parâmetro [CenterWindow](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/centerwindow) com o qual centralizamos a janela, após remover a barra de ferramentas superior com [HideMenubar](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/hidemenubar) e com [PageModeUseNone](https://reference.aspose.com/pdf/net/aspose.pdf.facades/viewerpreference/fields/pagemodeusenone) abrir o modo de tela cheia.
```csharp
 public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Alterar Preferências do Visualizador
            editor.ChangeViewerPreference(ViewerPreference.CenterWindow);
            editor.ChangeViewerPreference(ViewerPreference.HideMenubar);
            editor.ChangeViewerPreference(ViewerPreference.PageModeFullScreen);
            // Salva o arquivo PDF resultante
            editor.Save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```