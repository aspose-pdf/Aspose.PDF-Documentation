---
title: Aspose.PDF for Java 10.4.1におけるパブリックAPIの変更
type: docs
weight: 110
url: ja/java/public-api-changes-in-aspose-pdf-for-java-10-4-1/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

このページでは、[Aspose.PDF for Java 10.4.1](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry641525.aspx)に導入されたパブリックAPIの変更を一覧にしています。新しいおよび廃止されたパブリックメソッドだけでなく、Aspose.PDF for Javaの裏での振る舞いにおける変更で既存のコードに影響を与える可能性のあるものについても説明しています。既存の振る舞いを変更し、リグレッションとして見なされる可能性のある振る舞いは特に重要であり、ここに記載されています。

{{% /alert %}}

**パブリックAPIと後方互換性のない変更**

**com.aspose.pdf.IconFit**クラスでの変更：

- public boolean getSpreadOnBorder() -> public boolean isSpreadOnBorder() 

**com.aspose.pdf.Measure**クラスでの変更：

- public boolean getForceDenominator() -> public boolean isForceDenominator()

**com.aspose.pdf.RedactionAnnotation**クラスでの変更：

- public boolean getRepeat() -> public boolean isRepeat()

**com.aspose.pdf.SaveOptions** クラスの変更:

- public boolean getCloseResponse() -> public boolean isCloseResponse()

**com.aspose.pdf.Signature** クラスの変更:

- public boolean getShowProperties() -> public boolean isShowProperties()

**com.aspose.pdf.TextParagraph** クラスの変更:

- public boolean getJustify() -> public boolean isJustify()

**com.aspose.pdf.TextStamp** クラスの変更:

- public boolean getWordWrap() -> public boolean isWordWrap()
- public boolean getJustify() -> public boolean isJustify()
- public boolean getScale() -> public boolean isScale()

**com.aspose.pdf.TextState** クラスの変更:

- public boolean getUnderline() -> public boolean isUnderline()