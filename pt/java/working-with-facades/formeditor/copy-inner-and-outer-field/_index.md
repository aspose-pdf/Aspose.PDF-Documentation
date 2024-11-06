---
title: Copiar Campo Interno e Externo
type: docs
weight: 40
url: pt/java/copy-inner-and-outer-field/
description: Esta seção explica como copiar Campo Interno e Externo com com.aspose.pdf.facades usando a Classe FormEditor.
lastmod: "2021-06-05"
draft: false
---

O método [copyInnerField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyInnerField-java.lang.String-java.lang.String-int-) permite que você copie um campo no mesmo arquivo, nas mesmas coordenadas, na página especificada. Este método requer o nome do campo que você deseja copiar, o novo nome do campo e o número da página na qual o campo precisa ser copiado. A classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) fornece este método. O trecho de código a seguir mostra como copiar o campo na mesma localização no mesmo arquivo.

```java
    public static void CopyInnerField() {
        FormEditor editor = new FormEditor();
        Document document = new Document(_dataDir + "Sample-Form-01.pdf");
        document.getPages().add();
        editor.bindPdf(document);
        editor.copyInnerField("Last Name", "Last Name 2", 2);
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```


## Copiar Campo Externo em um Arquivo PDF Existente

O método [copyOuterField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyOuterField-java.lang.String-java.lang.String-) permite copiar um campo de formulário de um arquivo PDF externo e depois adicioná-lo ao arquivo PDF de entrada na mesma localização e no número de página especificado. Este método requer o arquivo PDF do qual o campo precisa ser copiado, o nome do campo e o número da página em que o campo precisa ser copiado. Este método é fornecido pela classe [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). O trecho de código a seguir mostra como copiar um campo de um arquivo PDF externo.

```java
  public static void CopyOuterField() {
        FormEditor editor = new FormEditor();
        Document document = new Document();
        document.getPages().add();
        editor.bindPdf(document);
        editor.copyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
        editor.copyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
        editor.save(_dataDir + "Sample-Form-02-mod.pdf");
    }
```