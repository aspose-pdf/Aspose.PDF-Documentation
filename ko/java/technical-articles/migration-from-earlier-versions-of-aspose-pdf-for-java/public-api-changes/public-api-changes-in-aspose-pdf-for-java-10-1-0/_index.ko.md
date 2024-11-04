---
title: Aspose.PDF for Java 10.1.0의 공용 API 변경 사항
type: docs
weight: 100
url: /java/public-api-changes-in-aspose-pdf-for-java-10-1-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

이 페이지는 [Aspose.PDF for Java 10.1.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry615512.aspx)에 도입된 공용 API 변경 사항을 나열합니다. 여기에는 새로운 공용 메서드와 더 이상 사용되지 않는 메서드뿐만 아니라 Aspose.PDF for Java의 작동 방식에서 기존 코드에 영향을 미칠 수 있는 변경 사항에 대한 설명도 포함됩니다. 회귀로 볼 수 있고 기존 동작을 수정하는 모든 동작은 특히 중요하며 여기에 문서화되어 있습니다.

{{% /alert %}}


**공용 API 및 이전과 호환되지 않는 변경 사항**

## 새로운 예외 클래스 추가:

- com.aspose.pdf.exceptions.UnsupportedFontTypeException
- com.aspose.pdf.exceptions.InvalidFormTypeOperationException
- com.aspose.pdf.exceptions.InvalidCgmFileFormatException

**com.aspose.pdf.facades.PdfViewer**


메서드 추가:


- public boolean getUseIntermidiateImage()  
- public void setUseIntermidiateImage(boolean value)  

**com.aspose.pdf.XForm**  

메서드 추가:  

- public void freeMemory()  

**com.aspose.pdf.TextSearchOptions**  

메서드 추가:  

- public boolean getUseFontEngineEncoding()  
- public void setUseFontEngineEncoding(boolean value)  

**com.aspose.pdf.TextEditOptions**  

메서드 추가:  

- public TextEditOptions(boolean allowLanguageTransformation)  
- public boolean getAllowLanguageTransformation()  
- public void setAllowLanguageTransformation(boolean value)  

**com.aspose.pdf.Page**  

메서드 추가:  

- public void processParagraphs()  
- public void dispose()  

**com.aspose.pdf.IDocument**  

메서드 추가:  

- public void processParagraphs();  

**com.aspose.pdf.Document**  

메서드 추가:  

- public void processParagraphs();  

**com.aspose.pdf.DocSaveOptions**  

메서드 추가:  

- public boolean getAddReturnToLineEnd()  
- public void setAddReturnToLineEnd(boolean value)  

**com.aspose.pdf.HtmlDocumentTypeInternal - 제거됨.**