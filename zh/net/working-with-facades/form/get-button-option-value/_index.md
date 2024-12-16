---
title: 获取按钮选项值
type: docs
weight: 40
url: /zh/net/get-button-option-value/
description: 本节介绍如何使用 Form 类通过 Aspose.PDF Facades 获取按钮选项值。
lastmod: "2021-06-05"
draft: false
---

## 从现有 PDF 文件中获取按钮选项值

单选按钮提供了一种显示不同选项的方法。 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 类允许您获取特定单选按钮的所有按钮选项值。您可以使用 [GetButtonOptionValues](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptionvalues) 方法获取这些值。此方法需要单选按钮的名称作为输入参数，并返回一个 Hashtable。您可以遍历此 Hashtable 来获取选项值。以下代码片段向您展示如何从现有 PDF 文件中获取按钮选项值。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-GetButtonOptionValue-GetButtonOptionValue.cs" >}}

## 从现有 PDF 文件获取当前按钮选项值

单选按钮提供了一种设置选项值的方法，但一次只能选择其中一个。如果您想获取当前选定的选项值，则可以使用 [GetButtonOptionCurrentValue** 方法。[Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) 类提供了此方法。[GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue) 方法需要单选按钮名称作为输入参数，并返回值作为字符串。以下代码片段向您展示了如何从现有 PDF 文件中获取当前按钮选项值。

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Forms-GetButtonOptionValue-GetCurrentValue.cs" >}}