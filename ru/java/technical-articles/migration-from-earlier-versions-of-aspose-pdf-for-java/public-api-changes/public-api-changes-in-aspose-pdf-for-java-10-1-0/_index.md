---
title: Изменения в публичном API в Aspose.PDF для Java 10.1.0
type: docs
weight: 100
url: ru/java/public-api-changes-in-aspose-pdf-for-java-10-1-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

На этой странице перечислены изменения в публичном API, введенные в [Aspose.PDF для Java 10.1.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry615512.aspx). Она включает не только новые и устаревшие публичные методы, но и описание любых изменений в поведении за кулисами в Aspose.PDF для Java, которые могут повлиять на существующий код. Любое поведение, которое может быть воспринято как регрессия и изменяет существующее поведение, особенно важно и документируется здесь.

{{% /alert %}}


**Публичный API и несовместимые изменения**

## Добавлены новые классы исключений:

- com.aspose.pdf.exceptions.UnsupportedFontTypeException
- com.aspose.pdf.exceptions.InvalidFormTypeOperationException
- com.aspose.pdf.exceptions.InvalidCgmFileFormatException

**com.aspose.pdf.facades.PdfViewer**


Добавлены методы:

- public boolean getUseIntermidiateImage()  
- public void setUseIntermidiateImage(boolean value)

**com.aspose.pdf.XForm**

Добавлен метод:

- public void freeMemory()

**com.aspose.pdf.TextSearchOptions**

Добавлены методы:

- public boolean getUseFontEngineEncoding()  
- public void setUseFontEngineEncoding(boolean value)

**com.aspose.pdf.TextEditOptions**

Добавлены методы:

- public TextEditOptions(boolean allowLanguageTransformation)  
- public boolean getAllowLanguageTransformation()  
- public void setAllowLanguageTransformation(boolean value)

**com.aspose.pdf.Page**

Добавлены методы:

- public void processParagraphs()  
- public void dispose()

**com.aspose.pdf.IDocument**

Добавлены методы:

- public void processParagraphs();

**com.aspose.pdf.Document**

Добавлены методы:

- public void processParagraphs();

**com.aspose.pdf.DocSaveOptions**

Добавлены методы:

- public boolean getAddReturnToLineEnd()  
- public void setAddReturnToLineEnd(boolean value)

**com.aspose.pdf.HtmlDocumentTypeInternal - удалено.**