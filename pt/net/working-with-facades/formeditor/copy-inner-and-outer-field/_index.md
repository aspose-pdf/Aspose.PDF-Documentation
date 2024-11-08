---
title: Copiar Campo Interno e Externo
type: docs
weight: 40
url: /pt/net/copy-inner-and-outer-field/
description: Esta seção explica como copiar Campo Interno e Externo com Aspose.PDF Facades usando a Classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

O método [CopyInnerField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyinnerfield/index) permite copiar um campo no mesmo arquivo, nas mesmas coordenadas, na página especificada. Este método requer o nome do campo que você deseja copiar, o novo nome do campo e o número da página onde o campo precisa ser copiado. A classe [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) fornece este método. O trecho de código a seguir mostra como copiar o campo na mesma localização no mesmo arquivo.

```csharp
  public static void CopyInnerField()
        {
            var editor = new FormEditor();
            var document = new Aspose.Pdf.Document(_dataDir + "Sample-Form-01.pdf");
            document.Pages.Add();
            editor.BindPdf(document);
            editor.CopyInnerField("Last Name", "Last Name 2", 2);
            editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
        }
```

## Copiar Campo Externo em um Arquivo PDF Existente

O método [CopyOuterField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyouterfield/index) permite copiar um campo de formulário de um arquivo PDF externo e, em seguida, adicioná-lo ao arquivo PDF de entrada na mesma localização e no número de página especificado. Este método requer o arquivo PDF do qual o campo precisa ser copiado, o nome do campo e o número da página em que o campo precisa ser copiado. Este método é fornecido pela classe [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor). O seguinte trecho de código mostra como copiar um campo de um arquivo PDF externo.

```csharp
   public static void CopyOuterField()
        {
            var editor = new FormEditor();
            var document = new Aspose.Pdf.Document();
            document.Pages.Add();
            editor.BindPdf(document);
            editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
            editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
            editor.Save(_dataDir + "Sample-Form-02-mod.pdf");
        }
```