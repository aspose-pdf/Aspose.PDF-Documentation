---
title: Aspose.PDF for Java 11.3.0의 공개 API 변경 사항
type: docs
weight: 130
url: /java/public-api-changes-in-aspose-pdf-for-java-11-3-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

이 페이지는 Aspose.PDF for Java 11.3.0에서 도입된 공개 API 변경 사항을 나열합니다. 새로운 공개 메서드와 사용되지 않는 메서드뿐만 아니라 Aspose.PDF for Java에서 기존 코드를 영향을 줄 수 있는 내부 동작의 변경 사항에 대한 설명도 포함되어 있습니다. 회귀로 보일 수 있는 동작을 도입하고 기존 동작을 수정하는 모든 사항은 특히 중요하며 여기 문서화되어 있습니다.

{{% /alert %}}

**com.aspose.pdf.Annotation 클래스의 변경 사항:**

추가된 메서드:

- public boolean isUpdateAppearanceOnConvert()
- public void setUpdateAppearanceOnConvert(boolean value)

**com.aspose.pdf.BaseParagraph 클래스의 변경 사항:**

추가된 메서드:

- public int getZIndex()
- public void setZIndex(int)

**com.aspose.pdf.MemoryCleaner 클래스의 변경 사항:**

추가된 메서드:

- public void clearAllTempFiles()

**com.aspose.pdf.Page 클래스의 변경 사항:**

Methods added:

- public byte[] asByteArray(com.aspose.pdf.devices.Resolution)

**클래스 com.aspose.pdf.Table의 변경 사항:**

Methods added:

- public com.aspose.pdf.Table getParentTable()
- public void setParentTable(com.aspose.pdf.Table)

**클래스 com.aspose.pdf.TextSearchOptions의 변경 사항:**

Methods added:

- public boolean isIgnoreShadowText()
- public void setIgnoreShadowText(boolean value)