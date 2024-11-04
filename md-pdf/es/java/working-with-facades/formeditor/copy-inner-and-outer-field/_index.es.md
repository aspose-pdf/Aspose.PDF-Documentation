---
title: Copiar Campo Interno y Externo
type: docs
weight: 40
url: /java/copy-inner-and-outer-field/
description: Esta sección explica cómo copiar un Campo interno y externo con com.aspose.pdf.facades usando la Clase FormEditor.
lastmod: "2021-06-05"
draft: false
---

El método [copyInnerField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyInnerField-java.lang.String-java.lang.String-int-) te permite copiar un campo en el mismo archivo, en las mismas coordenadas, en la página especificada. Este método requiere el nombre del campo que deseas copiar, el nuevo nombre del campo y el número de página en el que se necesita copiar el campo. La clase [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) proporciona este método. El siguiente fragmento de código te muestra cómo copiar el campo en la misma ubicación en el mismo archivo.

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


## Copiar Campo Externo en un Archivo PDF Existente

El método [copyOuterField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyOuterField-java.lang.String-java.lang.String-) te permite copiar un campo de formulario de un archivo PDF externo y luego agregarlo al archivo PDF de entrada en la misma ubicación y en el número de página especificado. Este método requiere el archivo PDF del cual se necesita copiar el campo, el nombre del campo y el número de página en el que se necesita copiar el campo. Este método es proporcionado por la clase [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). El siguiente fragmento de código te muestra cómo copiar un campo de un archivo PDF externo.

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