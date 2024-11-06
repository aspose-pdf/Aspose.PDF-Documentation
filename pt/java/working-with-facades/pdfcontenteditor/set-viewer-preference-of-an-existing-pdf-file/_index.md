---
title: Definir Preferência de Visualização de um Arquivo PDF Existente
type: docs
weight: 60
url: pt/java/set-viewer-preference-of-an-existing-pdf-file/
description: Esta seção mostra como trabalhar com Aspose.PDF Facades usando a Classe PdfContentEditor.
lastmod: "2021-06-05"
draft: false
---

## Definir Preferência de Visualização de um Arquivo PDF Existente

A classe [ViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/viewerpreference) representa modos de exibição de arquivos PDF; por exemplo, posicionar a janela do documento no centro da tela, ocultar a barra de menu do aplicativo visualizador, etc.

O método [ChangeViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) na classe [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) permite que você altere a preferência de visualização.
 Para fazer isso, você precisa criar um objeto da classe [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor) e vincular o arquivo PDF de entrada usando o método [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#bindPdf-java.lang.String-).

Depois disso, você pode chamar o método [ChangeViewerPreference](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#changeViewerPreference-int-) para definir qualquer preferência. Finalmente, você deve salvar o arquivo PDF atualizado usando o método Save. O trecho de código a seguir mostra como alterar a preferência do visualizador em um arquivo PDF existente.

Por exemplo, especificamos o parâmetro [CENTER WINDOW](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#CENTER_WINDOW) com o qual centralizamos a janela, depois removemos a barra de ferramentas superior com [HIDE MENUBAR](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#HIDE_MENUBAR) e com [PAGE MODE USE NONE](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/ViewerPreference#PAGE_MODE_USE_NONE) abrimos o modo de tela cheia.
```java
public static void SetViewerPreference()
        {
            var document = new Document(_dataDir + "Sample.pdf");
            PdfContentEditor editor = new PdfContentEditor(document);

            // Alterar Preferências do Visualizador
            editor.changeViewerPreference(ViewerPreference.CENTER_WINDOW);
            editor.changeViewerPreference(ViewerPreference.HIDE_MENUBAR);
            editor.changeViewerPreference(ViewerPreference.PAGE_MODE_USE_NONE);
            
            editor.save(_dataDir + "PdfContentEditorDemo_SetViewerPreference.pdf");
            GetViewerPreference();
        }
```