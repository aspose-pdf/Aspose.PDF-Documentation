---
title: Aspose.PDF for Java 11.3.0 中的公共 API 更改
type: docs
weight: 130
url: /zh/java/public-api-changes-in-aspose-pdf-for-java-11-3-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

本页列出了 Aspose.PDF for Java 11.3.0 中引入的公共 API 更改。它不仅包括新的和废弃的公共方法，还描述了 Aspose.PDF for Java 背后行为的任何变化，这可能会影响现有代码。任何可能被视为回归并修改现有行为的行为引入，尤其重要，并在此记录。

{{% /alert %}}

**类 com.aspose.pdf.Annotation 中的更改：**

添加的方法：

- public boolean isUpdateAppearanceOnConvert()
- public void setUpdateAppearanceOnConvert(boolean value)

**类 com.aspose.pdf.BaseParagraph 中的更改：**

添加的方法：

- public int getZIndex()
- public void setZIndex(int)

**类 com.aspose.pdf.MemoryCleaner 中的更改：**

添加的方法：

- public void clearAllTempFiles()


**类 com.aspose.pdf.Page 中的更改：**

Methods added:

- public byte[] asByteArray(com.aspose.pdf.devices.Resolution)

**对类 com.aspose.pdf.Table 的更改:**

Methods added:

- public com.aspose.pdf.Table getParentTable()
- public void setParentTable(com.aspose.pdf.Table)

**对类 com.aspose.pdf.TextSearchOptions 的更改:**

Methods added:

- public boolean isIgnoreShadowText()
- public void setIgnoreShadowText(boolean value)