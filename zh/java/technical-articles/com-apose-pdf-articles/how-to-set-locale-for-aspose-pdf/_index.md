---
title: 如何为 Aspose.PDF 设置区域设置
type: docs
weight: 30
url: zh/java/how-to-set-locale-for-aspose-pdf/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Aspose.PDF for Java 库无法支持具有特定语言-国家组合的区域设置（例如 "en-KR"）。但是，API 中存在为 Aspose.PDF 设置经典区域设置的功能，可以通过调用 com.aspose.pdf.LocaleOptions.setLocale() 方法来使用。

{{% /alert %}}

以下代码片段展示了如何使用 Aspose.PDF for Java 设置区域设置：

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-SetLocale.java" >}}