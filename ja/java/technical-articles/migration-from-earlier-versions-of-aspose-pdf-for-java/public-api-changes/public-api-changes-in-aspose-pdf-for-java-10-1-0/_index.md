---
title: Aspose.PDF for Java 10.1.0 における公開APIの変更
type: docs
weight: 100
url: ja/java/public-api-changes-in-aspose-pdf-for-java-10-1-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

このページでは、[Aspose.PDF for Java 10.1.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry615512.aspx) に導入された公開APIの変更を一覧にしています。新しい公開メソッドや廃止されたメソッドだけでなく、既存のコードに影響を与える可能性のあるAspose.PDF for Javaの内部動作の変更についても説明しています。回帰として見なされる可能性がある動作と既存の動作を変更するものは特に重要であり、ここに記載されています。

{{% /alert %}}


**公開APIと後方互換性のない変更**

## 新しい例外クラスを追加しました:

- com.aspose.pdf.exceptions.UnsupportedFontTypeException
- com.aspose.pdf.exceptions.InvalidFormTypeOperationException
- com.aspose.pdf.exceptions.InvalidCgmFileFormatException

**com.aspose.pdf.facades.PdfViewer**


メソッドを追加しました:

- public boolean getUseIntermidiateImage()  
- public void setUseIntermidiateImage(boolean value)  

**com.aspose.pdf.XForm**  

追加されたメソッド:  

- public void freeMemory()  

**com.aspose.pdf.TextSearchOptions**  

追加されたメソッド:  

- public boolean getUseFontEngineEncoding()  
- public void setUseFontEngineEncoding(boolean value)  

**com.aspose.pdf.TextEditOptions**  

追加されたメソッド:  

- public TextEditOptions(boolean allowLanguageTransformation)  
- public boolean getAllowLanguageTransformation()  
- public void setAllowLanguageTransformation(boolean value)  

**com.aspose.pdf.Page**  

追加されたメソッド:  

- public void processParagraphs()  
- public void dispose()  

**com.aspose.pdf.IDocument**  

追加されたメソッド:  

- public void processParagraphs();  

**com.aspose.pdf.Document**  

追加されたメソッド:  

- public void processParagraphs();  

**com.aspose.pdf.DocSaveOptions**  

追加されたメソッド:  

- public boolean getAddReturnToLineEnd()  
- public void setAddReturnToLineEnd(boolean value)  

**com.aspose.pdf.HtmlDocumentTypeInternal - 削除されました。**