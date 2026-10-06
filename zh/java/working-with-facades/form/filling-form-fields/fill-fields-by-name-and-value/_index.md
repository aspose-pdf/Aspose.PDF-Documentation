---
title: 按名称和值填充字段
linktitle: 按名称和值填充字段
type: docs
weight: 60
url: /zh/java/fill-fields-by-name-and-value/
description: 了解如何在 Java 中使用 Form 外观的字段填充 API，以实现动态的名称-值表单更新。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: 从名称-值对在 Java 中填充多个 PDF 表单字段
Abstract: 当前的 Java 示例集通过重复调用 `fillField(...)` 来逐个填充字段。本文展示了如何将相同的 API 模式应用于您自己的名称-值集合，而无需发明在仓库示例中不存在的单独外观功能。
---
Java `FormExamples` 类直接填充各个字段：

```java
form.fillField("name", "John Doe");
form.fillField("address", "123 Main St, Anytown, USA");
form.fillField("email", "john.doe@example.com");
```

如果您的应用程序已经拥有一组动态的字段名称和值，请应用相同的 `fillField(...)` 在您自己的循环中调用：

```java
for (Map.Entry<String, String> entry : values.entrySet()) {
    form.fillField(entry.getKey(), entry.getValue());
}
```

这是一个源自相同 Java API 的应用层模式 `FormExamples.fillTextFields(...)`; 当前仓库不包含用于基于映射填充的单独专用帮助方法。
