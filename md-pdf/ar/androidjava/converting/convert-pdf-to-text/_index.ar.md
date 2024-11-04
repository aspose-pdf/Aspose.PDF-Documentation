---
title: تحويل PDF إلى نص
linktitle: تحويل PDF إلى نص
type: docs
weight: 120
url: /androidjava/convert-pdf-to-txt/
lastmod: "2021-06-05"
description: باستخدام Aspose.PDF لنظام Android عبر Java يمكنك تحويل مستند PDF بالكامل إلى ملف نصي أو تحويل صفحة PDF فقط إلى ملف نصي.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}} 

جرب عبر الإنترنت. يمكنك التحقق من جودة تحويل Aspose.PDF وعرض النتائج عبر الإنترنت من خلال هذا الرابط [products.aspose.app/pdf/conversion/pdf-to-txt](https://products.aspose.app/pdf/conversion/pdf-to-txt)

{{% /alert %}}

## تحويل صفحة PDF إلى ملف نصي

يمكنك تحويل مستند PDF إلى ملف TXT باستخدام Aspose.PDF لنظام Android عبر Java. يجب عليك استخدام طريقة Visit من فئة [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber) لحل هذه المهمة.

يوضح مقطع الشيفرة التالي كيفية استخراج النصوص من الصفحات المحددة.

```java
public void convertPDFPagesToTXT() {
        // افتح المستند
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        TextAbsorber ta = new TextAbsorber();
        int[] pages = new int[] { 1, 3, 4 };

        for (int page : pages) {
            ta.visit(document.getPages().get_Item(page));
        }
        File txtFileName = new File(fileStorage, "PDF-to-Text.txt");

        // احفظ النص المستخرج في ملف نصي
        BufferedWriter writer;
        try {
            writer = new BufferedWriter(new FileWriter(txtFileName));
            writer.write(ta.getText());
            writer.close();
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```