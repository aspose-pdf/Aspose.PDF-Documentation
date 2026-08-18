---
title: 按名称和值填写字段
linktitle: 按名称和值填写字段
type: docs
weight: 60
url: /java/fill-fields-by-name-and-value/
description: 了解如何调整 Java 中的表单外观字段填充 API 以进行动态名称-值表单更新。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 使用 Java 中的名称/值对填充多个 PDF 表单字段
Abstract: 当前的 Java 示例集通过重复的 `fillField(...)` 调用单独填充字段。本文展示了如何将相同的 API 模式应用于您自己的名称-值集合，而无需发明存储库示例中不存在的单独外观功能。
---
Java `FormExamples` 类直接填充各个字段：

```java
form.fillField("name", "John Doe");
form.fillField("address", "123 Main St, Anytown, USA");
form.fillField("email", "john.doe@example.com");
```

如果您的应用程序已经具有一组动态字段名称和值，请在您自己的循环中应用相同的 `fillField(...)` 调用：

```java
for (Map.Entry<String, String> entry : values.entrySet()) {
    form.fillField(entry.getKey(), entry.getValue());
}
```

这是一个应用程序级模式，源自 `FormExamples.fillTextFields(...)` 中使用的相同 Java API；当前存储库不包含用于基于地图的填充的单独的专用辅助方法。
