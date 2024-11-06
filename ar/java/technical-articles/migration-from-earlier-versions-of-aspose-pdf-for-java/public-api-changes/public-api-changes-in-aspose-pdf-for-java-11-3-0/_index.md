---
title: تغييرات واجهة برمجة التطبيقات العامة في Aspose.PDF لـ Java 11.3.0
type: docs
weight: 130
url: ar/java/public-api-changes-in-aspose-pdf-for-java-11-3-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

تسرد هذه الصفحة تغييرات واجهة برمجة التطبيقات العامة التي تم تقديمها في Aspose.PDF لـ Java 11.3.0. وهي تشمل ليس فقط الطرق العامة الجديدة والملغاة، بل أيضًا وصف لأي تغييرات في السلوك خلف الكواليس في Aspose.PDF لـ Java التي قد تؤثر على الشيفرة الحالية. أي سلوك يتم تقديمه يمكن اعتباره تراجعًا ويعدل السلوك الحالي هو أمر مهم بشكل خاص ويتم توثيقه هنا.

{{% /alert %}}

**التغييرات في الفئة com.aspose.pdf.Annotation:**

الطرق المضافة:

- public boolean isUpdateAppearanceOnConvert()
- public void setUpdateAppearanceOnConvert(boolean value)

**التغييرات في الفئة com.aspose.pdf.BaseParagraph:**

الطرق المضافة:

- public int getZIndex()
- public void setZIndex(int)

**التغييرات في الفئة com.aspose.pdf.MemoryCleaner:**

الطرق المضافة:

- public void clearAllTempFiles()

**التغييرات في الفئة com.aspose.pdf.Page:**

Methods added:

- public byte[] asByteArray(com.aspose.pdf.devices.Resolution)

**التغييرات في الفئة com.aspose.pdf.Table:**

طرق أضيفت:

- public com.aspose.pdf.Table getParentTable()
- public void setParentTable(com.aspose.pdf.Table)

**التغييرات في الفئة com.aspose.pdf.TextSearchOptions:**

طرق أضيفت:

- public boolean isIgnoreShadowText()
- public void setIgnoreShadowText(boolean value)