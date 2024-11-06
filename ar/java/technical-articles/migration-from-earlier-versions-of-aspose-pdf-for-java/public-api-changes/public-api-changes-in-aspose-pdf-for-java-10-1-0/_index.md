---
title: تغييرات واجهة برمجة التطبيقات العامة في Aspose.PDF لـ Java 10.1.0
type: docs
weight: 100
url: ar/java/public-api-changes-in-aspose-pdf-for-java-10-1-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

تسرد هذه الصفحة تغييرات واجهة برمجة التطبيقات العامة التي تم تقديمها في [Aspose.PDF لـ Java 10.1.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry615512.aspx). يتضمن ذلك ليس فقط الأساليب العامة الجديدة والمتقادمة، ولكن أيضًا وصف لأي تغييرات في السلوك وراء الكواليس في Aspose.PDF لـ Java والتي قد تؤثر على الكود الحالي. أي سلوك تم تقديمه يمكن اعتباره تراجعًا ويعدل السلوك الحالي هو مهم بشكل خاص ويتم توثيقه هنا.

{{% /alert %}}


**تغييرات واجهة برمجة التطبيقات العامة وتغييرات غير متوافقة مع الإصدارات السابقة**

## إضافة فئات استثناء جديدة:

- com.aspose.pdf.exceptions.UnsupportedFontTypeException
- com.aspose.pdf.exceptions.InvalidFormTypeOperationException
- com.aspose.pdf.exceptions.InvalidCgmFileFormatException

**com.aspose.pdf.facades.PdfViewer**


تمت إضافة الأساليب:

- public boolean getUseIntermidiateImage()  
- public void setUseIntermidiateImage(boolean value)  

**com.aspose.pdf.XForm**  

تمت إضافة طريقة:  

- public void freeMemory()  

**com.aspose.pdf.TextSearchOptions**  

تمت إضافة طرق:  

- public boolean getUseFontEngineEncoding()  
- public void setUseFontEngineEncoding(boolean value)  

**com.aspose.pdf.TextEditOptions**  

تمت إضافة طرق:  

- public TextEditOptions(boolean allowLanguageTransformation)  
- public boolean getAllowLanguageTransformation()  
- public void setAllowLanguageTransformation(boolean value)  

**com.aspose.pdf.Page**  

تمت إضافة طرق:  

- public void processParagraphs()  
- public void dispose()  

**com.aspose.pdf.IDocument**  

تمت إضافة طرق:  

- public void processParagraphs();  

**com.aspose.pdf.Document**  

تمت إضافة طرق:  

- public void processParagraphs();  

**com.aspose.pdf.DocSaveOptions**  

تمت إضافة طرق:  

- public boolean getAddReturnToLineEnd()  
- public void setAddReturnToLineEnd(boolean value)  

**com.aspose.pdf.HtmlDocumentTypeInternal - تمت إزالته.**