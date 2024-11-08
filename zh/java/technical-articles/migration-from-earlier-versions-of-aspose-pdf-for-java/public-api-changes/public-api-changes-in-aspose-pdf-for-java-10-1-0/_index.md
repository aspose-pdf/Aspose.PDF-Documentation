---
title: Aspose.PDF for Java 10.1.0 中的公共 API 更改
type: docs
weight: 100
url: /zh/java/public-api-changes-in-aspose-pdf-for-java-10-1-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

此页面列出了 [Aspose.PDF for Java 10.1.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry615512.aspx) 中引入的公共 API 更改。它不仅包括新的和已废弃的公共方法，还包括对 Aspose.PDF for Java 背后行为的任何更改的描述，这些更改可能会影响现有代码。任何被视为回归并修改现有行为的行为尤为重要，并在此记录。

{{% /alert %}}


**公共 API 和向后不兼容的更改**

## 添加了新的异常类：

- com.aspose.pdf.exceptions.UnsupportedFontTypeException
- com.aspose.pdf.exceptions.InvalidFormTypeOperationException
- com.aspose.pdf.exceptions.InvalidCgmFileFormatException

**com.aspose.pdf.facades.PdfViewer**

添加了方法：

- public boolean getUseIntermidiateImage()  
- public void setUseIntermidiateImage(boolean value)  

**com.aspose.pdf.XForm**  

添加的方法:  

- public void freeMemory()  

**com.aspose.pdf.TextSearchOptions**  

添加的方法:  

- public boolean getUseFontEngineEncoding()  
- public void setUseFontEngineEncoding(boolean value)  

**com.aspose.pdf.TextEditOptions**  

添加的方法:  

- public TextEditOptions(boolean allowLanguageTransformation)  
- public boolean getAllowLanguageTransformation()  
- public void setAllowLanguageTransformation(boolean value)  

**com.aspose.pdf.Page**  

添加的方法:  

- public void processParagraphs()  
- public void dispose()  

**com.aspose.pdf.IDocument**  

添加的方法:  

- public void processParagraphs();  

**com.aspose.pdf.Document**  

添加的方法:  

- public void processParagraphs();  

**com.aspose.pdf.DocSaveOptions**  

添加的方法:  

- public boolean getAddReturnToLineEnd()  
- public void setAddReturnToLineEnd(boolean value)  

**com.aspose.pdf.HtmlDocumentTypeInternal - 已移除.**