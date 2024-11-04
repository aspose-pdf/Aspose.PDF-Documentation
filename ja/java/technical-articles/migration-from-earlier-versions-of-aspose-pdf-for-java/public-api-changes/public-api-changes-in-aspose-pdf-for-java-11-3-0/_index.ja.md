---
title: Aspose.PDF for Java 11.3.0におけるパブリックAPIの変更
type: docs
weight: 130
url: /java/public-api-changes-in-aspose-pdf-for-java-11-3-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

このページでは、Aspose.PDF for Java 11.3.0で導入されたパブリックAPIの変更を一覧表示しています。新しいパブリックメソッドや廃止されたメソッドだけでなく、Aspose.PDF for Javaの裏で動作に影響を与える可能性のある変更の説明も含まれています。既存の動作を変更する可能性があり、リグレッションとして見なされる動作は特に重要であり、ここに記録されています。

{{% /alert %}}

**com.aspose.pdf.Annotationクラスの変更:**

追加されたメソッド:

- public boolean isUpdateAppearanceOnConvert()
- public void setUpdateAppearanceOnConvert(boolean value)

**com.aspose.pdf.BaseParagraphクラスの変更:**

追加されたメソッド:

- public int getZIndex()
- public void setZIndex(int)

**com.aspose.pdf.MemoryCleanerクラスの変更:**

追加されたメソッド:

- public void clearAllTempFiles()

**com.aspose.pdf.Pageクラスの変更:**

Methods added:

- public byte[] asByteArray(com.aspose.pdf.devices.Resolution)

**クラス com.aspose.pdf.Table の変更:**

Methods added:

- public com.aspose.pdf.Table getParentTable()
- public void setParentTable(com.aspose.pdf.Table)

**クラス com.aspose.pdf.TextSearchOptions の変更:**

Methods added:

- public boolean isIgnoreShadowText()
- public void setIgnoreShadowText(boolean value)