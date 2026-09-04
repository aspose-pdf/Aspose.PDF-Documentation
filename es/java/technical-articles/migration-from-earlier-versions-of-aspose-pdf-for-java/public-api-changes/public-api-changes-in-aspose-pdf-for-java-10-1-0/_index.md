---
title: Cambios en la API Pública en Aspose.PDF para Java 10.1.0
type: docs
weight: 100
url: /es/java/public-api-changes-in-aspose-pdf-for-java-10-1-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página enumera los cambios en la API pública introducidos en [Aspose.PDF para Java 10.1.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry615512.aspx). Incluye no solo métodos públicos nuevos y obsoletos, sino también una descripción de cualquier cambio en el comportamiento detrás de escena en Aspose.PDF para Java que pueda afectar el código existente. Cualquier comportamiento introducido que pudiera considerarse una regresión y que modifique el comportamiento existente es especialmente importante y se documenta aquí.

{{% /alert %}}


**Cambios en la API Pública e Incompatibilidades Retroactivas**

## Se agregaron nuevas clases de excepción:

- com.aspose.pdf.exceptions.UnsupportedFontTypeException
- com.aspose.pdf.exceptions.InvalidFormTypeOperationException
- com.aspose.pdf.exceptions.InvalidCgmFileFormatException

**com.aspose.pdf.facades.PdfViewer**


Se agregaron métodos:

- public boolean getUseIntermidiateImage()
- public void setUseIntermidiateImage(boolean value)

**com.aspose.pdf.XForm**

Método añadido:

- public void freeMemory()

**com.aspose.pdf.TextSearchOptions**

Métodos añadidos:

- public boolean getUseFontEngineEncoding()
- public void setUseFontEngineEncoding(boolean value)

**com.aspose.pdf.TextEditOptions**

Métodos añadidos:

- public TextEditOptions(boolean allowLanguageTransformation)
- public boolean getAllowLanguageTransformation()
- public void setAllowLanguageTransformation(boolean value)

**com.aspose.pdf.Page**

Métodos añadidos:

- public void processParagraphs()
- public void dispose()

**com.aspose.pdf.IDocument**

Métodos añadidos:

- public void processParagraphs();

**com.aspose.pdf.Document**

Métodos añadidos:

- public void processParagraphs();

**com.aspose.pdf.DocSaveOptions**

Métodos añadidos:

- public boolean getAddReturnToLineEnd()
- public void setAddReturnToLineEnd(boolean value)

**com.aspose.pdf.HtmlDocumentTypeInternal - eliminado.**