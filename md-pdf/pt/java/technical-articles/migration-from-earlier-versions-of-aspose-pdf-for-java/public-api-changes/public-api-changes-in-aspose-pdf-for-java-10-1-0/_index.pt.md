---
title: Mudanças na API Pública no Aspose.PDF para Java 10.1.0
type: docs
weight: 100
url: /java/public-api-changes-in-aspose-pdf-for-java-10-1-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página lista as mudanças na API pública introduzidas no [Aspose.PDF para Java 10.1.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry615512.aspx). Inclui não apenas métodos públicos novos e obsoletos, mas também uma descrição de quaisquer alterações no comportamento por trás das cenas no Aspose.PDF para Java que podem afetar o código existente. Qualquer comportamento introduzido que possa ser visto como uma regressão e modifique o comportamento existente é especialmente importante e está documentado aqui.

{{% /alert %}}


**Mudanças na API Pública e Incompatibilidades Retroativas**

## Novas classes de exceção adicionadas:

- com.aspose.pdf.exceptions.UnsupportedFontTypeException
- com.aspose.pdf.exceptions.InvalidFormTypeOperationException
- com.aspose.pdf.exceptions.InvalidCgmFileFormatException

**com.aspose.pdf.facades.PdfViewer**


Métodos adicionados:

- public boolean getUseIntermidiateImage()
- public void setUseIntermidiateImage(boolean valor)

**com.aspose.pdf.XForm**

Método adicionado:

- public void freeMemory()

**com.aspose.pdf.TextSearchOptions**

Métodos adicionados:

- public boolean getUseFontEngineEncoding()
- public void setUseFontEngineEncoding(boolean valor)

**com.aspose.pdf.TextEditOptions**

Métodos adicionados:

- public TextEditOptions(boolean allowLanguageTransformation)
- public boolean getAllowLanguageTransformation()
- public void setAllowLanguageTransformation(boolean valor)

**com.aspose.pdf.Page**

Métodos adicionados:

- public void processParagraphs()
- public void dispose()

**com.aspose.pdf.IDocument**

Métodos adicionados:

- public void processParagraphs();

**com.aspose.pdf.Document**

Métodos adicionados:

- public void processParagraphs();

**com.aspose.pdf.DocSaveOptions**

Métodos adicionados:

- public boolean getAddReturnToLineEnd()
- public void setAddReturnToLineEnd(boolean valor)

**com.aspose.pdf.HtmlDocumentTypeInternal - removido.**